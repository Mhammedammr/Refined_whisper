from groq import Groq

# Set your Groq API key
client = Groq(api_key="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")

# List available models
try:
    models = client.models.list()
    for model in models.data:
        print(model.id)
except Exception as e:
    print(f"Error listing models: {e}")