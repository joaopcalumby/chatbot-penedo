import os
import argparse
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import gradio as gr

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def get_api_key():
    """Obtém a chave da API do ambiente ou levanta um erro se não estiver configurada."""
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("A variável de ambiente OPENROUTER_API_KEY não está configurada.")
    return api_key

def setup_rag_pipeline(pdf_path: str, persist_directory: str = "./chroma_db"):
    """Configura o pipeline RAG a partir de um PDF e retorna a chain de QA."""
    print(f"⚙️ Iniciando processamento de IA para: {pdf_path}")

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"O arquivo {pdf_path} não foi encontrado.")

    api_key = get_api_key()
    base_url = "https://openrouter.ai/api/v1"

    # 1. Carregamento
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    print(f"   📄 PDF lido: {len(docs)} páginas encontradas.")

    # 2. Fragmentação
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(docs)
    print(f"   ✂️ Texto fragmentado em {len(chunks)} blocos de informação.")

    # 3. Vetorização (Embeddings)
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=api_key,
        base_url=base_url
    )

    # 4. Banco Vetorial
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    print("   🗄️ Banco de dados vetorial construído.")

    # 5. Modelo de Linguagem
    llm = ChatOpenAI(
        model="openai/gpt-4o-mini",
        api_key=api_key,
        base_url=base_url,
        temperature=0.7
    )

    # 6. Define a persona e regras estritas
    prompt_template = """
    Você é o "Guia Penedo", um assistente turístico virtual especializado na cidade histórica de Penedo, Alagoas.

    SUAS INSTRUÇÕES:
    1. Use APENAS o contexto fornecido abaixo para responder.
    2. Seja educado, acolhedor e convide o turista a conhecer a cidade.
    3. Se a informação não estiver no contexto, responda: "Desculpe, não tenho essa informação nos meus registros históricos de Penedo no momento."

    CONTEXTO:
    {context}

    PERGUNTA DO USUÁRIO: {question}

    RESPOSTA:
    """
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    # 7. Cadeia de Recuperação (Chain)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={"prompt": prompt}
    )

    return qa_chain

def launch_gradio_interface(qa_pipeline):
    """Inicia a interface web com Gradio."""
    def responder_turista(message, history):
        if not message:
            return ""
        resultado = qa_pipeline.invoke({"query": message})
        return resultado['result']

    interface = gr.ChatInterface(
        fn=responder_turista,
        title="🏰 Guia Virtual de Penedo - AL",
        description="Pergunte sobre a história, igrejas, cultura e turismo de Penedo. Eu respondo com base em documentos oficiais!",
        theme="soft",
        examples=["Quem fundou Penedo?", "Quais as igrejas mais famosas?", "Onde fica o Teatro Sete de Setembro?", "Fale sobre o Rio São Francisco"]
    )
    
    print("🚀 Iniciando interface gráfica...")
    interface.launch(share=False)

def launch_terminal_interface(qa_pipeline):
    """Inicia a interface de linha de comando."""
    print("==================================================")
    print("🤖 CHATBOT INICIADO (Modo Terminal)")
    print("Digite 'sair' para encerrar.")
    print("==================================================\n")

    while True:
        user_input = input("VOCÊ: ")

        if user_input.lower() in ['sair', 'exit', 'fim']:
            print("👋 Até logo!")
            break

        if not user_input.strip():
            continue

        print("⏳ Pesquisando...", end="\r")
        try:
            response = qa_pipeline.invoke({"query": user_input})
            print(f"GUIA PENEDO: {response['result']}")
        except Exception as e:
            print(f"Erro ao processar a pergunta: {e}")
            
        print("-" * 50)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chatbot Guia Virtual de Penedo (RAG)")
    parser.add_argument("--pdf", type=str, default="penedo.pdf", help="Caminho para o arquivo PDF base")
    parser.add_argument("--mode", type=str, choices=["gradio", "terminal"], default="gradio", help="Modo de interface (gradio ou terminal)")
    args = parser.parse_args()

    try:
        qa_pipeline = setup_rag_pipeline(args.pdf)
        print("\n🤖 MOTOR DE IA PRONTO PARA USO!")
        
        if args.mode == "gradio":
            launch_gradio_interface(qa_pipeline)
        else:
            launch_terminal_interface(qa_pipeline)
            
    except Exception as e:
        print(f"Erro fatal: {e}")
