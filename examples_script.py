from pgpt_python.client import PrivateGPTApi

client = PrivateGPTApi(base_url="http://localhost:8001")

# Health
print(client.health.health())

# Sync completion
print("Sync completion")
print(
    client.contextual_completions.prompt_completion(
        prompt="Answer with just the result: 2+2"
    )
    .choices[0]
    .message.content
)

# Async completion
print("\n>Async completion")
for i in client.contextual_completions.prompt_completion_stream(
    prompt="Answer with just the result: 2+2"
):
    # Print  content in an incremental way
    print(i.choices[0].delta.content, end="")

# Sync chat completion
print("\n\n>Sync chat completion")
print(
    client.contextual_completions.chat_completion(
        messages=[{"role": "user", "content": "Answer with just the result: 2+2"}]
    )
    .choices[0]
    .message.content
)

# Async completion
print("\n>Async chat completion")
for i in client.contextual_completions.chat_completion_stream(
    messages=[{"role": "user", "content": "Answer with just the result: 2+2"}]
):
    # Print  content in an incremental way
    print(i.choices[0].delta.content, end="")

# Embeddings
print("\n\n>Sync embeddings")
print(client.embeddings.embeddings_generation(input="Hello world").data[0].embedding)

# Ingestion of text
print("\n>Ingestion of text")
text_to_ingest = (
    "Books bombarded his shoulder, his arms, his upturned face.  A book "
    "lit, almost obediently, like a white pigeon, in his hands, "
    "wings fluttering.  In the dim, wavering light, a page hung open "
    "and it was like a snowy feather, the words delicately painted "
    "thereon.  In all the rush and fervor, Montage had only an instant "
    "to read a line, but it blazed in his mind for the next minute as "
    "if stamped there with fiery steel.  “Time has fallen asleep in the "
    "afternoon sunshine.”  He dropped the book.  Immediately, another "
    "fell into his arms.”"
)

ingested_text_doc_id = (
    client.ingestion.ingest_text(file_name="Fahrenheit 451", text=text_to_ingest)
    .data[0]
    .doc_id
)

print("Ingested text doc id: ", ingested_text_doc_id)

# Ingestion of file
print("\n>Ingestion of file")
with open("example_file.txt", "rb") as f:
    ingested_file_doc_id = client.ingestion.ingest_file(file=f).data[0].doc_id

print("Ingested file doc id: ", ingested_file_doc_id)

# List ingested documents
print("\n>List ingested documents")
for doc in client.ingestion.list_ingested().data:
    print(doc.doc_id)

# Chunks
print("\n>Find related chunks:")
print(client.context_chunks.chunks_retrieval(text="Pigeon fluttering").data[0].text)

print("\n>Contextual completion:")
result = client.contextual_completions.prompt_completion(
    prompt="What did Montage do?",
    use_context=True,
    context_filter={"docs_ids": [ingested_text_doc_id]},
    include_sources=True,
).choices[0]
print(result.message.content)
print(f" # Source: {result.sources[0].document.doc_metadata['file_name']}")

print("\n>Deletion of ingested document")
client.ingestion.delete_ingested(ingested_text_doc_id)
client.ingestion.delete_ingested(ingested_file_doc_id)
print("\nDeletion done")

# Recipes

# Sync summarization
print("\n>Sync summarization")
print(
    client.recipes.summarize.summarize(
        text=(
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
            "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
            "when an unknown printer took a galley of type and scrambled it to make a type specimen book. "
        ),
        instructions=(
            "Summarize the text to 1 sentence."
        )
    ).summary
)

print("\n>Async summarization")
for i in client.recipes.summarize.summarize_stream(
    text=(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
        "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
        "when an unknown printer took a galley of type and scrambled it to make a type specimen book. "
    ),
    instructions=(
        "Summarize the text to 1 sentence."
    )
):
    # Print  content in an incremental way
    print(i.choices[0].delta.content, end="")