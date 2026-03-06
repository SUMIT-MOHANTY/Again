from .azure_openai import generate_text

def process_prompt(prompt: str) -> str:
    return generate_text(prompt)
