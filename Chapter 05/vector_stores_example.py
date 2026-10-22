from openai import OpenAI

client = OpenAI()

# Create a vector store for one BlueVivo engagement
vector_store = client.vector_stores.create(
    name="bluevivo-bv2042-memory"
)

# Upload and attach a file
file_obj = client.files.create(
    file=open("discovery_notes.pdf", "rb"),
    purpose="assistants"
)

client.vector_stores.files.create(
    vector_store_id=vector_store.id,
    file_id=file_obj.id
)

# In production code, poll the vector store or file batch status
# until processing is complete before querying it.
print(vector_store.id)
