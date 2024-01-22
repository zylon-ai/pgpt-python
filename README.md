# Python SDK for PrivateGPT API

**pgpt_python** is an open-source Python SDK designed to interact with the PrivateGPT API. PrivateGPT is a popular AI Open Source project that provides secure and private access to advanced natural language processing capabilities. This SDK simplifies the integration of PrivateGPT into Python applications, allowing developers to harness the power of PrivateGPT for various language-related tasks.

This SDK has been created using [Fern](https://buildwithfern.com/).

## Installation

To install the pgpt_python SDK, use the following pip command:

```bash
pip install pgpt_python
```

## Getting Started

To begin using pgpt_python with the PrivateGPT API, follow these steps:

1. **Import the PrivateGPTApi class:**

    ```python
    from pgpt_python.client import PrivateGPTApi
    ```

2. **Create a PrivateGPTApi instance. Point it to your PrivateGPT url:**

    ```python
    client = PrivateGPTApi(base_url="http://localhost:8001")
    ```

3. Certainly! Here's the completed "Perform API calls" section:

## Perform API Calls

Once you have set up the PrivateGPTApi instance, you can perform various API calls using the pgpt_python SDK. Below are examples of common API calls:

### 1. **Health Check:**

```python
print(client.health.health())

> status='ok'
```

This call checks the health of the PrivateGPT API and returns information about its status.

### 2. **Completion:**

```python
prompt_result = client.contextual_completions.prompt_completion(
    prompt="Answer with just the result: 2+2"
)
print(prompt_result.choices[0].message.content)

> The answer is 4.
```

This call performs contextual completions based on the provided prompt and retrieves the completion result.

### 3. **Streaming Completion:**

```python
for i in client.contextual_completions.prompt_completion_stream(
    prompt="Answer with just the result: 2+2"
):
    print(i.choices[0].delta.content, end="")

> The answer i...
```

This example demonstrates contextual completions using a streaming approach, allowing you to process results incrementally.

### 4. **Chat Completion:**

```python
chat_result = client.contextual_completions.chat_completion(
    messages=[{"role": "user", "content": "Answer with just the result: 2+2"}]
)
print(chat_result.choices[0].message.content)

> The answer is 4.
```

Perform a chat completion using a list of messages to simulate a conversation.

### 5. **Streaming Chat Completion:**

```python
for i in client.contextual_completions.chat_completion_stream(
    messages=[{"role": "user", "content": "Answer with just the result: 2+2"}]
):
    print(i.choices[0].delta.content, end="")

> The answer i...
```

This example demonstrates streaming chat completions using a streaming approach, allowing you to process results incrementally.

### 6. **Embeddings:**

```python
embedding_result = client.embeddings.embeddings_generation(input="Hello world")
print(embedding_result.data[0].embedding)

> [0.015196125954389572, -0.022570695728063583, 0.008547102101147175, -0.07417059689760208, 0.0038364222273230553, ... ]
```

Retrieve embeddings for a given input using synchronous embeddings generation.

### 7. **Ingestion of Text:**

```python
text_to_ingest = "Books bombarded his shoulder, ... (your long text here)"
ingested_text_doc_id = (
    client.ingestion.ingest_text(file_name="Fahrenheit 451", text=text_to_ingest)
    .data[0]
    .doc_id
)
print("Ingested text doc id: ", ingested_text_doc_id)

> Ingested text doc id:  8cfc93fa-01dd-4644-82d4-e12dfff54dcf
```

Ingest text content and obtain a document ID for future reference.

### 8. **Ingestion of File:**

```python
with open("example_file.txt", "rb") as f:
    ingested_file_doc_id = client.ingestion.ingest_file(file=f).data[0].doc_id
print("Ingested file doc id: ", ingested_file_doc_id)

> Ingested file doc id:  e2989f56-1729-4557-b30a-e4b023628629
```

Ingest a file and obtain a document ID for future reference.

### 9. **List Ingested Documents:**

```python
for doc in client.ingestion.list_ingested().data:
    print(doc.doc_id)

>List ingested documents
e2989f56-1729-4557-b30a-e4b023628629
8cfc93fa-01dd-4644-82d4-e12dfff54dcf
```

Retrieve a list of ingested documents along with their document IDs.

### 10. **Chunks Retrieval:**

```python
chunks_result = client.context_chunks.chunks_retrieval(text="Pigeon fluttering")
print(chunks_result.data[0].text)

> A book lit, almost obediently, like a white pigeon, in his hands, wings fluttering.
```

Retrieve related chunks of text from ingested docs based on a specified query.

### 11. **Contextual Completion:**

```python
result = client.contextual_completions.prompt_completion(
    prompt="What did Montage do?",
    use_context=True,
    context_filter={"docs_ids": ["8cfc93fa-01dd-4644-82d4-e12dfff54dcf"]},
    include_sources=True,
).choices[0]

print("\n>Contextual completion:")
print(result.message.content)
print(f" # Source: {result.sources[0].document.doc_metadata['file_name']}")

> Montage was surrounded by falling books when one of them landed in his hands.
  Source: Fahrenheit 451
```

Perform a contextual completion using the specified context from ingested documents, including in the response the sources used during inference.

### 12. **Deletion of Ingested Documents:**

```python
client.ingestion.delete_ingested("8cfc93fa-01dd-4644-82d4-e12dfff54dcf")
client.ingestion.delete_ingested("e2989f56-1729-4557-b30a-e4b023628629")
```

Delete previously ingested documents using their document IDs.

## Examples

The provided `examples_script.py` showcases various features of the pgpt_python SDK. Feel free to explore and modify this script to suit your specific use cases.

## Documentation

For detailed information on available methods and their parameters, refer to the [official documentation](https://docs.privategpt.dev/api-reference/overview/sd-ks).

## Contributing

We welcome contributions from the community! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the Apache License.

## Acknowledgments

- [Fern](https://buildwithfern.com/) - For providing a powerful SDK generation tool, and supporting PrivateGPT with a free forever license.
- [PrivateGPT Community](https://discord.gg/bK6mRVpErU) - For being the fuel of PrivateGPT and providing valuable feedback.