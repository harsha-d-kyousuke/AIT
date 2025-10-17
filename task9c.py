import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are a financial expert that specializes in real estate investment and negotiation"}
]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    return reply

gr.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Real Estate Chat Assistant").launch()
