from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=1.5, max_completion_tokens=10)

result = model.invoke("Write a 5 line poem on cricket")

print(result)
# content = "In the green fields, 'twixt will"
# additional_kwargs = {"refusal": None}
# response_metadata = {
#     "token_usage": {
#         "completion_tokens": 10,
#         "prompt_tokens": 15,
#         "total_tokens": 25,
#         "completion_tokens_details": {
#             "accepted_prediction_tokens": 0,
#             "audio_tokens": 0,
#             "reasoning_tokens": 0,
#             "rejected_prediction_tokens": 0,
#         },
#         "prompt_tokens_details": {"audio_tokens": 0, "cached_tokens": 0},
#     },
#     "model_name": "gpt-4-0613",
#     "system_fingerprint": None,
#     "id": "chatcmpl-BxriXvkcqghoHEl3nZpUAVHuEUXdK",
#     "service_tier": "default",
#     "finish_reason": "length",
#     "logprobs": None,
# }
# id = "run--8ab639e2-14c4-4b5e-8eb0-a1e5fb7d4c44-0"
# usage_metadata = {
#     "input_tokens": 15,
#     "output_tokens": 10,
#     "total_tokens": 25,
#     "input_token_details": {"audio": 0, "cache_read": 0},
#     "output_token_details": {"audio": 0, "reasoning": 0},
# }
print(result.content)
# In the green fields, 'twixt will