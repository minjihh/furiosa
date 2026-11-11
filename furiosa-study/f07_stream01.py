# f05 카피

from openai import OpenAI
from langchain_openai import ChatOpenAI


client = OpenAI(
    base_url = "http://127.0.0.1:8000/v1",
    api_key = "EMPTY"

)


# 서버에 로드된 모델 확인
model = client.models.list().data[0].id

print("모델: ", model)

# 추론 
streaming = client.chat.completions.create(
    model = model,
    messages = [
        {
            "role" : "user",
            "content" : "NPU와 GPU의 차이점을 설명해줘",
        }
    ],
    max_tokens = 3000,
    stream  = True,
)


for chunk in streaming:
    if chunk.choices:
        content = chunk.choices[0].delta.content
        if content:
            print(content, end="", flush=True)




# import os
# from openai import OpenAI

# base_url = os.getenv("OPENAI_BASE_URL", "http://localhost:8000/v1")
# api_key = os.getenv("OPENAI_API_KEY", "EMPTY")
# client = OpenAI(api_key=api_key, base_url=base_url)
# model = client.models.list().data[0].id

# with client.responses.stream(
#     model=model,
#     input="What is the capital of France?",
# ) as stream:
#     for event in stream:
#         if event.type == "response.output_text.delta":
#             print(event.delta, end="", flush=True)
# print()