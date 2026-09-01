#python -m pip install openai

from openai import OpenAI
client = OpenAI()
text = input("Enter text to summarize: ")
response = client.responses.create(
    model="gpt-5-turbo",
    input=f"Summarize the following text:\n{text}"
)
print("\nSummary:", response.output_text)