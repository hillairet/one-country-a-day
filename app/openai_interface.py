from json import loads
from pathlib import Path

from openai import AsyncOpenAI

from .config import conf

client = AsyncOpenAI(api_key=conf.open_ai_key)

PROMPT = Path('./app/prompt.txt').read_text()


async def query_open_ai(country: str) -> dict:
    results = await client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {
                "role": "user",
                "content": f'I want to learn about {country}. {PROMPT}'
            }
        ],
    )

    return loads(results.choices[0].message.content)
