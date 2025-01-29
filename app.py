import json

import gradio as gr
import requests

url="http://localhost:11434/api/generate"
headers={
    'Content-Type':'application/json'
}

history=[]

def generate_response(prompt):
    history.append(prompt)
    final_prompt="/n".join(history)
    data={
        "model":"Coder",
        "prompt":final_prompt,
        "stream":False
    }

    response=requests.post(url,headers=headers,data=json.dumps(data))

    if response.status_code==200:
        response=response.text
        data=json.loads(response)
        output=data['response']
        return output
    else:
        print("error:",response.text)

# GRADIO_SERVER_PORT=8000

interface=gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4),
    outputs="text",
)
# interface = gr.Interface()
interface.launch()
