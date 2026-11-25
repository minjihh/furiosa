# f28 카피

"""
furiosa-llm serve furiosa-ai/Qwen3-8B-FP8 \
--devices npu:5 \
--host 127.0.0.1 \
--port 8000 \
--enable-overlap-scheduling
"""

# --enable-overlap-scheduling은 Furiosa-LLM
# 서빙엔진에서 CPU의 스케줄링 작업과 NPU의 추론 연산을 겹쳐 실행하도록 하는 최적화 옵션

# Continuours Batching: 여러 사용자의 요청을 동ㅈ거으로 묶어 NPU에서 처리하는 기술
# Overlap Scheduling : NPU가 현재 배치를 처리하는 동안 CPU가 다음 배치를 준비하는 기술
# <-> Eager Scheduling 순차처리에 유리. 디폴트.



import time
from kingkeras import get_llm
from concurrent.futures import ThreadPoolExecutor
import statistics


llm = get_llm(max_tokens=500)

prompts = [
    f"NPU 추론 최적화 방법 {i}번을 설명해줘"
    for i in range(16)
]


def ask(prompt):
    start = time.perf_counter()
    response =  llm.invoke(prompt)
    elapsed = time.perf_counter() - start

    usage = response.usage_metadata or {}
    tokens = usage.get("output_tokens", 0)
    return elapsed, tokens


for workers in [1,2,4,8]:

    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers = 4) as executor:
        results = list(executor.map(ask, prompts))   # output tokens이 리스트의 형태로 들어가 있음
    
    total_time = time.perf_counter() - start

    latencies = [r[0] for r in results]
    total_tokens = sum(r[1] for r in results)

    print(f"\n===== Workers: {workers} =====")

    print("전체 시간 :", round(total_time, 3), "초")
    print("평균 지연 :", round(statistics.mean(latencies), 2), "초")
    print("요청 처리량 :", round(len(results) / total_time, 2), "req/s")
    print("Output TPS :", round(total_tokens / total_time, 2))


# ===== Workers: 8 =====  eager
# 전체 시간 : 23.837 초
# 평균 지연 : 5.96 초
# 요청 처리량 : 0.67 req/s
# Output TPS : 335.61

# ===== Workers: 8 =====  enable overlap
# 전체 시간 : 24.096 초
# 평균 지연 : 6.02 초
# 요청 처리량 : 0.66 req/s
# Output TPS : 332.01
