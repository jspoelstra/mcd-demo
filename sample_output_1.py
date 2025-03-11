from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

{
    "messages": [
        HumanMessage(
            content="what's (3 + 5) x 12?",
            additional_kwargs={},
            response_metadata={},
            id="c26acec4-f077-4c05-81d8-7e58cb9448a4",
        ),
        AIMessage(
            content="",
            additional_kwargs={
                "tool_calls": [
                    {
                        "id": "call_LgabhhUNCEBFiePZHaMCLtKi",
                        "function": {"arguments": '{"a":3,"b":5}', "name": "add"},
                        "type": "function",
                    }
                ],
                "refusal": None,
            },
            response_metadata={
                "token_usage": {
                    "completion_tokens": 17,
                    "prompt_tokens": 96,
                    "total_tokens": 113,
                    "completion_tokens_details": {
                        "accepted_prediction_tokens": 0,
                        "audio_tokens": 0,
                        "reasoning_tokens": 0,
                        "rejected_prediction_tokens": 0,
                    },
                    "prompt_tokens_details": {"audio_tokens": 0, "cached_tokens": 0},
                },
                "model_name": "gpt-4o-mini-2024-07-18",
                "system_fingerprint": "fp_b705f0c291",
                "prompt_filter_results": [
                    {
                        "prompt_index": 0,
                        "content_filter_results": {
                            "hate": {"filtered": False, "severity": "safe"},
                            "jailbreak": {"filtered": False, "detected": False},
                            "self_harm": {"filtered": False, "severity": "safe"},
                            "sexual": {"filtered": False, "severity": "safe"},
                            "violence": {"filtered": False, "severity": "safe"},
                        },
                    }
                ],
                "finish_reason": "tool_calls",
                "logprobs": None,
                "content_filter_results": {},
            },
            id="run-4d4cfa3b-a91a-4b39-84c2-a8367db83b92-0",
            tool_calls=[
                {
                    "name": "add",
                    "args": {"a": 3, "b": 5},
                    "id": "call_LgabhhUNCEBFiePZHaMCLtKi",
                    "type": "tool_call",
                }
            ],
            usage_metadata={
                "input_tokens": 96,
                "output_tokens": 17,
                "total_tokens": 113,
                "input_token_details": {"audio": 0, "cache_read": 0},
                "output_token_details": {"audio": 0, "reasoning": 0},
            },
        ),
        ToolMessage(
            content="8",
            name="add",
            id="fc76b74c-7d10-4bcf-938d-95f7c6077c16",
            tool_call_id="call_LgabhhUNCEBFiePZHaMCLtKi",
        ),
        AIMessage(
            content="",
            additional_kwargs={
                "tool_calls": [
                    {
                        "id": "call_CXVDWnoVvQggeP3XdbDtz5HA",
                        "function": {"arguments": '{"a":8,"b":12}', "name": "multiply"},
                        "type": "function",
                    }
                ],
                "refusal": None,
            },
            response_metadata={
                "token_usage": {
                    "completion_tokens": 17,
                    "prompt_tokens": 121,
                    "total_tokens": 138,
                    "completion_tokens_details": {
                        "accepted_prediction_tokens": 0,
                        "audio_tokens": 0,
                        "reasoning_tokens": 0,
                        "rejected_prediction_tokens": 0,
                    },
                    "prompt_tokens_details": {"audio_tokens": 0, "cached_tokens": 0},
                },
                "model_name": "gpt-4o-mini-2024-07-18",
                "system_fingerprint": "fp_b705f0c291",
                "prompt_filter_results": [
                    {
                        "prompt_index": 0,
                        "content_filter_results": {
                            "hate": {"filtered": False, "severity": "safe"},
                            "jailbreak": {"filtered": False, "detected": False},
                            "self_harm": {"filtered": False, "severity": "safe"},
                            "sexual": {"filtered": False, "severity": "safe"},
                            "violence": {"filtered": False, "severity": "safe"},
                        },
                    }
                ],
                "finish_reason": "tool_calls",
                "logprobs": None,
                "content_filter_results": {},
            },
            id="run-474f6c39-06ea-4d1b-8098-1ba3186a8571-0",
            tool_calls=[
                {
                    "name": "multiply",
                    "args": {"a": 8, "b": 12},
                    "id": "call_CXVDWnoVvQggeP3XdbDtz5HA",
                    "type": "tool_call",
                }
            ],
            usage_metadata={
                "input_tokens": 121,
                "output_tokens": 17,
                "total_tokens": 138,
                "input_token_details": {"audio": 0, "cache_read": 0},
                "output_token_details": {"audio": 0, "reasoning": 0},
            },
        ),
        ToolMessage(
            content="96",
            name="multiply",
            id="424f48dc-49a2-48fb-a3db-ae7925a2199b",
            tool_call_id="call_CXVDWnoVvQggeP3XdbDtz5HA",
        ),
        AIMessage(
            content="The result of \\((3 + 5) \\times 12\\) is \\(96\\).",
            additional_kwargs={"refusal": None},
            response_metadata={
                "token_usage": {
                    "completion_tokens": 22,
                    "prompt_tokens": 146,
                    "total_tokens": 168,
                    "completion_tokens_details": {
                        "accepted_prediction_tokens": 0,
                        "audio_tokens": 0,
                        "reasoning_tokens": 0,
                        "rejected_prediction_tokens": 0,
                    },
                    "prompt_tokens_details": {"audio_tokens": 0, "cached_tokens": 0},
                },
                "model_name": "gpt-4o-mini-2024-07-18",
                "system_fingerprint": "fp_b705f0c291",
                "prompt_filter_results": [
                    {
                        "prompt_index": 0,
                        "content_filter_results": {
                            "hate": {"filtered": False, "severity": "safe"},
                            "jailbreak": {"filtered": False, "detected": False},
                            "self_harm": {"filtered": False, "severity": "safe"},
                            "sexual": {"filtered": False, "severity": "safe"},
                            "violence": {"filtered": False, "severity": "safe"},
                        },
                    }
                ],
                "finish_reason": "stop",
                "logprobs": None,
                "content_filter_results": {
                    "hate": {"filtered": False, "severity": "safe"},
                    "protected_material_code": {"filtered": False, "detected": False},
                    "protected_material_text": {"filtered": False, "detected": False},
                    "self_harm": {"filtered": False, "severity": "safe"},
                    "sexual": {"filtered": False, "severity": "safe"},
                    "violence": {"filtered": False, "severity": "safe"},
                },
            },
            id="run-b591adcb-b15e-4e73-96de-50d2b709b3dc-0",
            usage_metadata={
                "input_tokens": 146,
                "output_tokens": 22,
                "total_tokens": 168,
                "input_token_details": {"audio": 0, "cache_read": 0},
                "output_token_details": {"audio": 0, "reasoning": 0},
            },
        ),
    ]
}
