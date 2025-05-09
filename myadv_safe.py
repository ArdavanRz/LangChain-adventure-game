from astrapy import DataAPIClient

# Initialize the client
client = DataAPIClient("your key")
db = client.get_database_by_api_endpoint(


  "https://ea6839f9-57d1-4042-b8ad-207fdee70842-us-east1.apps.astra.datastax.com"
)

print(f"Connected to Astra DB: {db.list_collection_names()}")

##########################
ASTRA_DB_KEYSPACE = ""
OPENAI_API_KEY = ""

