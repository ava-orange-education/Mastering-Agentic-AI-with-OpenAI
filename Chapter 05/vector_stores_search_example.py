results = client.vector_stores.search(
    vector_store.id,
    query="What compliance requirements did the client emphasize for AI access?",
    max_num_results=3
)

for item in results.data:
    print(item.filename)
    for block in item.content:
        if block.type == "text":
            print(block.text)
            print("-----")
