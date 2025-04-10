import ollama

response = ollama.list()
# print(response)
res = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "tell me a short story about a cat , make it funny",
        }
    ],
    stream=True
)
for chunk in res:
        print(chunk["message"]["content"], end="", flush=True)

res2 = ollama.generate(
    model="llama3.2",
    prompt="tell me a short story about a cat , make it funny",
    stream=True
)
print(ollama.show("llama3.2"))

#create a new model
modelfile="""
FROM llama3.2
SYSTEM you are a helpful assistant
PARAMETER temperature : 0.2
"""
ollama.create(model="DUDE", modelfile=modelfile);


res3 = ollama.generate(
    model="DUDE",
    prompt="tell me a short story about a cat , make it funny",
    stream=False
)
print(res3["response"]);

ollama.delete(model="DUDE")