from openai import OpenAI
import os
from settings.setting import system_prompt

def call(query:str, context_documents:str):
    client = OpenAI(base_url=os.getenv('API_LINK_LMSTUDIO'), api_key="lm-studio")

    prompt = system_prompt + f'\n\n### CONTEXTO RECUPERADO:\n{context_documents}'
    
    try:
        response = client.chat.completions.create(
            model=os.getenv('MODEL_LMSTUDIO'),
            messages=[
                { 'role': 'system', 'content': prompt },
                { 'role': 'user', 'content': query }
            ],
            extra_body={ "include_reasoning": False },
            temperature=0.3,
            stream=True
        )

        for chunk in response:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
    except Exception as e:
        yield 'Erro: ' + str(e)