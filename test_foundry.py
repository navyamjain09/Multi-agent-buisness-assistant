import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

load_dotenv()

project_endpoint = os.getenv("FOUNDRY_PROJECT_ENDPOINT")
model_deployment = os.getenv("MODEL_DEPLOYMENT_NAME")

if not project_endpoint:
    raise ValueError("FOUNDRY_PROJECT_ENDPOINT is missing")

if not model_deployment:
    raise ValueError("MODEL_DEPLOYMENT_NAME is missing")

print("Connecting to Azure AI Foundry...")

project = AIProjectClient(
    endpoint=project_endpoint,
    credential=DefaultAzureCredential(),
)

openai = project.get_openai_client()

response = openai.responses.create(
    model=model_deployment,
    input="Hello! Give me a one-sentence introduction for a multi-agent business assistant."
)

print("\nAzure response:")
print(response.output_text)