from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_community.cache import SQLiteCache
from langchain_core.globals import set_llm_cache

# Carrega as variáveis de ambiente definidas no arquivo .env para a memória da aplicação
load_dotenv()

# Instancia o cliente da OpenAI. Ele busca automaticamente pela variável OPENAI_API_KEY no ambiente
client = OpenAI()

# 1. Configura o cache global persistente em SQLite
set_llm_cache(SQLiteCache(database_path="cache.db"))

# 2. Instancia o modelo
model = OpenAI()

prompt = "Escreva um poema sobre a natureza."

# Primeira chamada (vai na API da OpenAI + salva no cache.db)
response1 = model.invoke(prompt)
print(f"chamada 1: {response1}")

# Segunda chamada (busca direto do arquivo cache.db local)
response2 = model.invoke(prompt)
print(f"chamada 2: {response2}")
