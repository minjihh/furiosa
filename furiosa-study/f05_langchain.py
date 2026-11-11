# 01 카피

"""
furiosa-llm serve furiosa-ai/Qwen3-8B-FP8
furiosa-llm serve furiosa-ai/gpt-oss-20b
furiosa-llm serve furiosa-ai/Meta-Llama-3.1-8B-Instruct (X)
furiosa-llm serve furiosa-ai/Meta-Llama-3.1-8B-Instruct-FP8-dynamic
furiosa-llm serve furiosa-ai/Qwen3.5-0.8B (X)
furiosa-llm serve furiosa-ai/Qwen3-4B-FP8


furiosa-llm serve furiosa-ai/Qwen3-8B-FP8 \
--devices npu:5 \
--host 0.0.0.0 \
--port 8000
"""

from openai import OpenAI
from langchain_openai import ChatOpenAI


# local host : "http://127.0.0.1:8000/v1"  
# pod : 1개의 가상 PC (쿠버네티스)
# client = OpenAI(
#     base_url = "http://127.0.0.1:8000/v1",
#     api_key = "EMPTY"

# )

llm = ChatOpenAI(
    base_url = "http://127.0.0.1:8000/v1",
    api_key = "EMPTY"
)



# # 서버에 로드된 모델 확인
# models = client.models.list()
# model_id = models.data[0].id

# print("모델: ", model_id)

# 추론 
# response = client.chat.completions.create(
#     model = model_id,
#     messages = [
#         {
#             "role" : "user",
#             "content" : "NPU와 GPU의 차이점을 설명해줘",
#         }
#     ],
#     # max_tokens = 3000,
# )

response = llm.invoke("NPU와 GPU의 차이점을 설명해줘")


# print(response.choices[0].message.content)
print(response.content)




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