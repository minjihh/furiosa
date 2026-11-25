"""
furiosa-llm serve furiosa-ai/Qwen3-8B-FP8 \
--devices npu:5 \
--host 127.0.0.1 \
--port 8000 \
--enable-overlap-scheduling \
--enable-auto-tool-choice \
--tool-call-parser hermes
"""

from kingkeras import get_llm
from langchain_core.tools import tool

#1. 도구 정의
@tool  # @ 데코레이터
def add(aaa: int, bbb: int) -> int:   # -> return 값에 대한 typehint
    """ 두 정수를 더합니다. """
    return aaa + bbb

print(add.name)  # add
print(add.description)  # 두 정수를 더합니다.
print(add.args)  # {'aaa': {'title': 'Aaa', 'type': 'integer'}, 'bbb': {'title': 'Bbb', 'type': 'integer'}}


#2. llm 생성
llm = get_llm(max_tokens = 1000)


#3. 도구 등록
llm_with_tools = llm.bind_tools([add])


#4. 질문
response = llm_with_tools.invoke(
    "237341과 31321을 add로 더해줘."
)

#5. 결과확인
print("일반 응답 :", response.content)
print("======================================")
print("Tool Calls :", response.tool_calls)   # Tool Calls : [{'name': 'add', 'args': {'aaa': 237341, 'bbb': 31321}, 'id': 'call-c012c94d5590483c806587f528b7b2b7', 'type': 'tool_call'}]
print("메타 데이터 :", response.response_metadata)




