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
import time

max_tokens = 1000



llm = ChatOpenAI(
    base_url = "http://127.0.0.1:8000/v1",
    api_key = "EMPTY",
    max_tokens = max_tokens,
    temperature=2,
    top_p= 0.5,
)

start = time.perf_counter()
response = llm.invoke("NPU와 GPU의 차이점을 설명해줘")
end = time.perf_counter()
elapsed = round(end - start, 2)

# print(response.content)
print("추론시간 : ", elapsed, "초")
print("출력토큰 :", max_tokens)
print("평균 처리량 :", round(max_tokens/elapsed, 2), "tokens/s")



