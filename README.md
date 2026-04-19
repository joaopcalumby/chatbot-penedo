# Chatbot Guia Virtual de Penedo (RAG) 🏰

Este projeto implementa um **Chatbot com RAG** (Retrieval-Augmented Generation) capaz de responder perguntas sobre a cidade histórica de Penedo-AL. 
O sistema utiliza um documento PDF como base de conhecimento, garantindo que as respostas sejam fundamentadas em fatos históricos e turísticos reais, evitando alucinações da IA.

## 🎯 Objetivo
Desenvolvido como projeto final em uma residência em TIC, o objetivo deste sistema é criar um guia virtual confiável e acessível. 
Ao integrar o LangChain com um banco de dados vetorial, a aplicação extrai respostas precisas diretamente de fontes bibliográficas aprovadas.

## 📚 Fonte de Dados (Créditos)
O documento base utilizado neste projeto (`penedo.pdf`) é derivado do artigo científico:
> **Título:** As riquezas de Penedo - Alagoas/Brasil  
> **Autor:** Thiago Pereira Dantas  
> **Publicação:** Revista Científica Multidisciplinar Núcleo do Conhecimento. Ano 06, Ed. 03, Vol. 08, pp. 165-190. Março de 2021.  
> **Link:** [Acessar Artigo Original](https://www.nucleodoconhecimento.com.br/historia/riquezas-de-penedo)

## 🛠️ Tecnologias Utilizadas
- **LangChain:** Orquestração do fluxo de RAG.
- **ChromaDB:** Banco de dados vetorial para busca semântica.
- **OpenAI (via OpenRouter):** LLM (GPT-4o-mini) e Embeddings (text-embedding-3-small).
- **Gradio:** Interface gráfica web para interação amigável.
- **Jupyter Notebook:** Ambiente de execução e documentação.

## 🚀 Como Executar

### 1. Clonar o Repositório
```bash
git clone https://github.com/joaopcalumby/chatbot-penedo.git
cd chatbot-penedo
```

### 2. Base de Conhecimento e Dependências
Certifique-se de que o arquivo `penedo.pdf` está na pasta raiz do projeto. O próprio notebook (`Chatbot_Guia_Penedo.ipynb`) se encarrega de instalar todas as bibliotecas necessárias (como `langchain`, `chromadb`, etc) na sua primeira célula de código, usando comandos do `pip`.

### 3. Executar o Notebook
Abra o arquivo `Chatbot_Guia_Penedo.ipynb` no **Jupyter Notebook**, **JupyterLab** ou no **VS Code**. 
Siga executando as células em ordem:
- A primeira célula irá instalar as dependências e pedir que você insira a chave da API da OpenRouter.
- A segunda validará a presença do arquivo PDF (`penedo.pdf`).
- A terceira criará o motor RAG.
- As últimas células oferecem a opção de interagir via interface web (Gradio) ou diretamente pelo terminal/console do Jupyter.

## 📂 Estrutura do Projeto
- `Chatbot_Guia_Penedo.ipynb`: O código principal de todo o fluxo, organizado, refatorado e bem documentado em Markdown.
- `penedo.pdf`: O documento base que fornece contexto ao chatbot (adicionado localmente).
- `README.md`: Este arquivo com as instruções e documentação do projeto.
- `.gitignore`: Configuração para impedir que arquivos indesejados (como o banco do ChromaDB) sejam "comitados" por engano.

## 👨‍💻 Autor
**João Pedro Silva Calumby Pereira**

## 📝 Licença
Este projeto é de uso educacional e portfólio pessoal. Todos os créditos do documento PDF estão devidamente atribuídos aos autores originais.
