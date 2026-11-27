# time to first chunk

from kingkeras import get_llm
import time

llm = get_llm()

prompt = "NPU의 장점 자세히 설명해줘"

start = time.perf_counter()
first_time = None

for chunk in llm.stream(prompt):
    
    if chunk.content:
        if first_time is None:
            first_time = time.perf_counter() - start
        print(chunk.content, end="", flush = True)  ## flush=True를 주면 조각이 도착하는 즉시 한 글자 단위로 흘러나와서 "타이핑되는 것처럼" 보이는 스트리밍 효과

print("===========================================")
print("첫 컨텐츠 응답시간 : ", round(first_time, 2), "초")




