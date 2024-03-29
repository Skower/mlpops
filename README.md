<p align="center">
    <img src="/docs/logo.png" width="100" height="100">
</p>

The following repository presents an MLOps project developed by students at EPITA. This project involves an LLM chatbot that utilizes a [Milvus](https://milvus.io/) vector database and employs the [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) to assess the necessity of predictions. The models are fine-tuned and monitored using [Weights and Biases](https://wandb.ai/site).

## Authors
- arnaud.baradat
- tom.genlis
- bastien.pouessel

## Architecture

The following schema presents the project's architecture.

<p align="center">
  <img src="/docs/archi.png" width="550" height="450">
</p>

### How to run the project
The project is completely dockerized, except for the Weight and Bias component. A Docker Compose file is provided to launch Apache Pulsar, Milvus Database, the FastAPI, the Gradio user interface, and the embedding services.


The following command will execute the docker-compose.yml
```
docker compose up -d
```

We decided to serve the model using Ollama with a TinyLlama model that was finetuned with QLoRa and quantized to 4 bits.

In addition to that, to ingest data into the database, you need to have instances of Pulsar broker and Zookeeper running on localhost.


Next, you can interact with the UI at the following address: [`localhost:7860`](http://localhost:7860).
