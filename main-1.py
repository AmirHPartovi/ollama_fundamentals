import requests
import json

url = "http://localhost:11434/api/generate"
data = {
    "model": "llama3.2",
    "prompt": "tell me a short story about a cat",
}

response = requests.post(url, json=data, stream=True)

# check the response status
if response.status_code == 200:
    print("Response:", end=" ", flush=False)
    # print the response text
    for line in response.iter_lines():
        if line:
            decode_line = line.decode("utf-8")
            result = json.loads(decode_line)

            generated_text = result.get("response", " ")
            print(generated_text, end="", flush=True)


else:
    print(f"Error: {response.status_code}")
