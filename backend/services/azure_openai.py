from ..config import config

def generate_text(prompt: str) -> str:
    """Return mock or real response based on placeholder key."""
    if config.AZURE_OPENAI_KEY == 'your-key-here':
        return f'Mock response for: {prompt}'
    # Real Azure OpenAI call would go here (omitted for safety)
    return f'Real response would be generated for: {prompt}'
