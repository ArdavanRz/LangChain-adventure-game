from langchain.memory import CassandraChatMessageHistory, ConversationBufferMemory
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from langchain.llms import OpenAI
from langchain import LLMChain, PromptTemplate
from astrapy import DataAPIClient
import json



# Initialize the client
client = DataAPIClient("")
db = client.get_database_by_api_endpoint(


  ""
)

print(f"Connected to Astra DB: {db.list_collection_names()}")

cloud_config= {
  'secure_connect_bundle': 'secure-connect-choose-your-own-adventure.zip'
}

with open("choose_your_own_adventure-token.json") as f:
    secrets = json.load(f)

##########################
CLIENT_ID = secrets["clientId"]
CLIENT_SECRET = secrets["secret"]
ASTRA_DB_KEYSPACE = ""
OPENAI_API_KEY = ""

auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()


message_history = CassandraChatMessageHistory(session_id = "anything", session = "session", keyspace = ASTRA_DB_KEYSPACE, ttl_seconds = 3600)
message_history.clear()

cass_buff_mem = ConversationBufferMemory(memory_key = "chat_history", chat_memory = message_history)

llm = OpenAI(OPENAI_API_KEY=OPENAI_API_KEY)
