# f21-1 카피

# npu는 continuous batching으로 돌아감

import time
import statistics
from concurrent.futures import ThreadPoolExecutor

from kingkeras import run_once

prompts = [
    f"NPU 추론 최적화 방법 {i}번을 자세히 설명해줘."
    for i in range(8)
]

# print(prompts)
# print(len(prompts))     # 8

# aaa = run_once("NPU가 뭐게?", 1000)
# print(aaa["text"])

# def ask(prompt):
#     return run_once(prompt, 50)

for workers in [1,2,4,8]:
    start = time.perf_counter()

    # with -> 뭔가 닫을 것이 있다.
    with ThreadPoolExecutor(max_workers = workers) as pool:
        results = list(
            pool.map(
                lambda prompts: run_once(prompts, 50),   # prompts 를 run_once 함수에 집어넣고 출력해라
                prompts
                )
        )
    elapsed = time.perf_counter() - start

    total_tokens = sum(
        r['output_tokens'] for r in results 
    )

    # print(len(results))

    # print(total_tokens)


    total_tokens = sum(
        r['output_tokens'] for r in results
    )

    avg_latency = statistics.mean(
        r['elapsed'] for r in results
    )

    print(f"\n동시 요청 수: {workers}")
    print(f"전체 시간: {elapsed:.2f}초")
    print(f"전체 룰력 토큰: {total_tokens}")
    print(f"처리량: {total_tokens / elapsed:.2f} TPS")
    print(f"평균 요청 지연: {avg_latency:.2f} 초")
