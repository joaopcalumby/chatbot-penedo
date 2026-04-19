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
- **Python:** Linguagem principal do projeto.

## 🚀 Como Executar Localmente

### 1. Clonar o Repositório
```bash
git clone https://github.com/SEU_USUARIO/chatbot-penedo.git
cd chatbot-penedo
```

### 2. Configurar o Ambiente Virtual
É recomendado o uso de um ambiente virtual (venv):
```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
```

### 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar as Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto com a sua chave da OpenRouter:
```env
OPENROUTER_API_KEY=sua_chave_aqui
```

### 5. Adicionar a Base de Conhecimento
Certifique-se de que o arquivo `penedo.pdf` está na pasta raiz do projeto. Caso não possua, você pode baixá-lo a partir do artigo referenciado e renomeá-lo.

### 6. Executar a Aplicação
Para iniciar a interface web com Gradio:
```bash
python chatbot.py --mode gradio
```

Para interagir com o chatbot diretamente pelo terminal:
```bash
python chatbot.py --mode terminal
```

## 📂 Estrutura do Projeto
- `chatbot.py`: Script principal da aplicação, refatorado seguindo as boas práticas de engenharia de software, separando a lógica de negócios da interface.
- `requirements.txt`: Lista de bibliotecas necessárias para executar a aplicação.
- `.env.example`: Exemplo de arquivo de configuração de variáveis de ambiente.
- `JoaoPedroSCPereira_Projeto_Final_Chatbot.ipynb`: Versão original em Jupyter Notebook do projeto.

## 👨‍💻 Autor
**João Pedro Silva Calumby Pereira**

## 📝 Licença
Este projeto é de uso educacional e portfólio pessoal. Todos os créditos do documento PDF estão devidamente atribuídos aos autores originais.
