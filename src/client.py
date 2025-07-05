from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

client = OpenAI()

def chat(prompt, tools=None):
  if tools is None:
    tools = []
  completion = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
      {'role':'user', 'content':prompt}
    ],
    tools=tools
  )
  return completion.choices[0].message  


if __name__ == '__main__':
  pass
