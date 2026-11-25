# f38_agnet_error 카피

from kingkeras import get_llm
from langchain_core.tools import tool
from langchain.agents import create_agent
# pip install langchain
from langchain_core.messages import AIMessage


@tool
def add(a:int, b:int) -> int:
    """ 두 정수를 더합니다. """
    return a + b

@tool
def subtract(a:int, b:int) -> int:
    """ 첫 번째 정수에서 두 번째 정수를 뺍니다. """
    return a - b

@tool
def multiply(a:int, b:int) -> int:  # 타입힌트
    """ 두 정수를 곱합니다. """
    return a * b

@tool
def divide(a:int, b:int) -> float:  # 타입힌트
    """ 첫 번째 정수를 두 번째 정수로 나눕니다. """
    return a / b

llm = get_llm(max_tokens = 10000)

tools = [add, multiply, subtract, divide]

agent = create_agent(
    model = llm,
    tools = tools,
    system_prompt = (
        "당신은 계산 전문 Agent입니다."
        "계산이 필요하면 등록된 도구를 사용하세요."
        "여러 단계의 계산은 순서대로 수행하세요."
        "계산 오류가 발생하면 사용자에게 설명하세요."
    )
    # system_prompt: 에이전트한테 역할과 행동지침을 설정.
)

# Agent 함수 맹글다.

def run_agent(question):
    print("\n사용자 질문 :", question)
    print("======================================")

    result = agent.invoke({
        "messages": [
            {"role":"user", "content": question}
        ]
        },
        config = {"recursoin_limit": 20}
    )


    for i, msg in enumerate(result["messages"]):

        if isinstance(msg, AIMessage) and msg.tool_calls:     # HumanMessage, AIMessage (클래스의 객체) // isinstance :  객체가 있다면~
            for call in msg.tool_calls:
                print("도구 이름:", call['name'])
                print("전달 인자:", call['args'])

    print("=========================================")
    print("최종 답변 :", result['messages'][-1].content)
    print(result['messages'])
    exit()

    return result


# 사용자 입력
while True:
    question = input("\n계산할 질문을 입력하세요 (종로:q):")

    if question.lower() == 'q':
        print("Agent 종료")
        break

    if not question.strip():
        continue

    try:
        run_agent(question)
    except Exception as e:
        print("오류 발생 :", type(e).__name__, e)

