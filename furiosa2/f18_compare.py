from kingkeras import get_llm
import time
llm = get_llm(max_tokens=2000,)

prompts = [
    "NPU란?",
    "NPU와 GPU의 차이를 10가지 설명해줘",
    "NPU의 구조와 장점, 활용 분야를 더더더 자세히 설명해줘."
]

for prompt in prompts:
    start = time.perf_counter()
    response = llm.invoke(prompt)
    elapsed = time.perf_counter() - start

    input_tokens = response.usage_metadata["input_tokens"]
    output_tokens = response.usage_metadata["output_tokens"]

    print("질문 :", prompt)
    print("입력 토큰:", input_tokens)
    print("출력 토큰:", output_tokens)
    print("응답시간 : ", round(elapsed, 2), "초")
    print("===================================")


# 질문 : NPU란?
# 입력 토큰: 12
# 출력 토큰: 1009
# 응답시간 :  11.07 초
# ===================================
# 질문 : NPU와 GPU의 차이를 10가지 설명해줘
# 입력 토큰: 24
# 출력 토큰: 1401
# 응답시간 :  15.33 초
# ===================================
# 질문 : NPU의 구조와 장점, 활용 분야를 더더더 자세히 설명해줘.
# 입력 토큰: 31
# 출력 토큰: 2000
# 응답시간 :  21.85 초
# ===================================