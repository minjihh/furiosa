from kingkeras import get_llm

llm = get_llm(max_tokens=500)

response = llm.invoke("NPU란 무엇인가")  # "NPU란 무엇인가" -> input_tokens

print(response.content)
print("===============================")
print(response.usage_metadata)  # token량 조절하고 싶을때 사용

# {'input_tokens': 14, 'output_tokens': 500, 
# 'total_tokens': 514, 
# 'input_token_details': {'audio': 0, 'cache_read': 6}, 
# 'output_token_details': {'audio': 0, 'reasoning': 0}}


