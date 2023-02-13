from secret_keys import OPENAI_API_KEY
import openai

openai.api_key = OPENAI_API_KEY
openai.Model.list()

#res = openai.File.create(file=open("testFile.jsonl"), purpose="classifications")
#print(res)