from dotenv import load_dotenv
from langchain_openai import OpenAI, ChatOpenAI

# Carrega as variáveis de ambiente definidas no arquivo .env para a memória da aplicação
load_dotenv()

# Instancia o cliente da OpenAI. Ele busca automaticamente pela variável OPENAI_API_KEY no ambiente
client = OpenAI()

# Exemplo 1: Utilizando o modelo de texto tradicional (LLM)

# Instancia o modelo base da OpenAI (para geração/completude de texto)
model = OpenAI()

# Realiza a chamada ao modelo enviando o prompt e definindo os parâmetros de geração diretamente no invoke
response = model.invoke(
    input="liste as 5 maiores campeões do mundo?",
    temperature=0.5,  # Controla a criatividade da resposta (0.0 mais determinístico, 1.0 mais criativo)
    max_tokens=300    # Limita o número máximo de tokens na resposta
)

# Exibe a resposta retornada pelo modelo (no modelo OpenAI base, o retorno já é uma string)
print(response)


# Exemplo 2: Utilizando o modelo de chat (ChatModel)

# Instancia o modelo otimizado para conversação (estruturado em mensagens)
model = ChatOpenAI(
    model="gpt-4",  # Especifica a versão do modelo de chat a ser utilizada
)

# Define a lista de mensagens representando o histórico ou papéis da conversa (System e User)
messages = [
    {'role': 'system', 'content': 'Você é um assistente especialista em explicar logica de programação de um jeito simples e didático.'},
    {'role': 'user', 'content': 'me explica o que é a logica de programação de um jeito simples e didático.'}
]

# Realiza a chamada ao modelo passando a lista de mensagens
response = model.invoke(messages)

# Exibe o objeto AIMessage completo retornado pelo ChatOpenAI (contém a resposta + metadados)
print(response)

# Exibe apenas o texto puro contido na resposta da IA
print(response.content)
