# Vertex AI proxy for pre-trained models
This is a simple proxy to send request to Vertex AI Prediction endpoint without authentication. This is used for Lab only.

## Environment Variables
Required the following environment variables:
``` 
PROJECT_ID=
ENDPOINT_REGION=
ENDPOINT_ID=
```

## Deploy to Cloud run
``` 
gcloud run deploy vertexai-proxy \
--source . \
--region=asia-southeast1 \
--allow-unauthenticated \
--set-env-vars "PROJECT_ID=<project-id>" \
--set-env-vars "ENDPOINT_REGION=asia-southeast1" \
--set-env-vars "ENDPOINT_ID=<vertex-ai-prediction-endpoints>" 
```

## Testing the endpoint locally

Command to send the curl request:
``` 
ENDPOINT_URL=http://localhost:8080
curl -X POST -H "Content-Type: application/json" "${ENDPOINT_URL}" -d @json-samples/input-file-1.json
```

## Testing the Cloud Run endpoint

Command to send the curl request:
``` 
ENDPOINT_URL=https://vertexai-proxy-387895767614.asia-southeast1.run.app
curl -X POST -H "Content-Type: application/json" "${ENDPOINT_URL}" -d @json-samples/input-file-1.json
```
