from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import pandas as pd

search_key = "your_search_key"
endpoint = "your_endpoint"
index_name = "your_index_name"

# Create SearchClient with credentials
credential = AzureKeyCredential(search_key)
search_client = SearchClient(endpoint, index_name, credential)

# Get all documents (adjust filter and top parameters as needed)
filter = None  # Optional filter string for specific documents
top = 10000  # Adjust to retrieve desired number of documents
df_dct=[]
try:
    results = search_client.search(search_text="*", filter=filter, top=top)
    for doc in results:
        df_dct.append(doc)
        #print(doc.to_dict())
except Exception as ex:
    print("Error retrieving data:", ex)

aiSearch_df = pd.DataFrame(df_dct)
aiSearch_df.to_pickle(f'data/{index_name}.pkl')
