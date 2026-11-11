# f05 카피

from openai import OpenAI
from langchain_openai import ChatOpenAI


# client = OpenAI(
#     base_url = "http://127.0.0.1:8000/v1",
#     api_key = "EMPTY"

# )


# # 서버에 로드된 모델 확인
# model = client.models.list().data[0].id

# print("모델: ", model)


llm = ChatOpenAI(
    base_url = "http://127.0.0.1:8000/v1",
    api_key = "EMPTY",
    max_tokens = 1000,
    temperature = 0,
    top_p = 0.9,
)


# 스트리밍 
# streaming = client.chat.completions.create(
#     model = model,
#     messages = [
#         {
#             "role" : "user",
#             "content" : "NPU와 GPU의 차이점을 설명해줘",
#         }
#     ],
#     max_tokens = 3000,
#     stream  = True,
# )


# for chunk in streaming:
#     if chunk.choices:
#         content = chunk.choices[0].delta.content
#         if content:
#             print(content, end="", flush=True)


for chunk in llm.stream("NPU와 GPU의 차이점을 설명해줘"):
    print(chunk.content, end = "", flush = True)




