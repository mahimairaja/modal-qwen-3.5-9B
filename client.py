from openai import OpenAI

client = OpenAI(
    base_url="<YOUR_MODEL_URL>",
    api_key="not-needed",
)

response = client.chat.completions.create(
    model="Qwen/Qwen3.5-9B",
    messages=[{"role": "user", "content": "What is 2+2? Be brief."}],
    max_tokens=256,
)

print(repr(response))
