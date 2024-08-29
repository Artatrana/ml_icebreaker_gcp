# GPT-2 Text Generator API

This project is a simple text generator API using a pre-trained GPT2 model. It is containerize with Docker and can be deployed on Google Google Kubernetes Engine (GKE).

## Setup and Deployment

1. Build and push a Docker image go Google Container Registry(GCR).
2. Deploy the Kubernetes Deployment and Service.
3. Access the API via the provided external API

## Usage

POST /generate

```json
{
  "prompt": "Once upon a time,"
}