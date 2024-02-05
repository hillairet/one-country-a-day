from openai import AsyncOpenAI

from .config import conf

client = AsyncOpenAI(api_key=conf.open_ai_key)


async def query_open_ai():
    results = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Say this is a test"}],
    )

    return results.choices[0].message.content
