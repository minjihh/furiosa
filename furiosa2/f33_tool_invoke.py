# f32 카피

"""
furiosa-llm serve furiosa-ai/Qwen3-8B-FP8 \
--devices npu:5 \
--host 127.0.0.1 \
--port 8000 \
--enable-overlap-scheduling \
--enable-auto-tool-choice \
--tool-call-parser hermes
"""


# --enable-auto-tool-choice \
# --tool-call-parser hermes
# 위 두개 옵션 넣고 powershell에서 실행해야 코드 돌아감


from kingkeras import get_llm
from langchain_core.tools import tool

#1. 도구 정의
@tool  # @ 데코레이터
def add(aaa: int, bbb: int) -> int:   # -> return 값에 대한 typehint
    """ 두 정수를 더합니다. """
    return aaa + bbb


#2. llm 생성
llm = get_llm(max_tokens = 200)


#3. 도구 등록
llm_with_tools = llm.bind_tools([add])    # tool과 llm을 bind_tools로 엮을 수 있다.


#4. 질문
response = llm_with_tools.invoke(
    "21과 32을 add로 더해줘."
)


for call in response.tool_calls:
    result = add.invoke(call['args'])
    print("계산 결과 :", result)


