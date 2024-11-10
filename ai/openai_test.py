import openai
from constants_ai import constants

openai.api_key = constants["openai_api_key"]

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Who is Batman?",
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response)