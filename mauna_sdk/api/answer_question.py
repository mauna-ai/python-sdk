#!/usr/bin/env python3
# @generated AUTOGENERATED file. Do not Change!

from dataclasses import dataclass, field as _field
from ..schema_config.json_scalar import custom_scalars
from gql_client.runtime.variables import encode_variables
from gql import gql, Client
from gql.transport.exceptions import TransportQueryError
from functools import partial
from numbers import Number
from typing import Any, AsyncGenerator, Dict, List, Generator, Optional
from time import perf_counter
from dataclasses_json import DataClassJsonMixin, config


# fmt: off
QUERY: List[str] = ["""
query answerQuestion($input: String!, $context: String!, $min_length: Int!) {
  result: callQA(input: $input, context: $context, min_length: $min_length) {
    answer: result
  }
}

"""
]


class answerQuestion:
    @dataclass(frozen=True)
    class answerQuestionData(DataClassJsonMixin):
        @dataclass(frozen=True)
        class QA_Result(DataClassJsonMixin):
            answer: str

        result: Optional[QA_Result]

    # fmt: off
    @classmethod
    def execute(cls, client: Client, input: str, context: str, min_length: int) -> Optional[answerQuestionData.QA_Result]:
        variables: Dict[str, Any] = {"input": input, "context": context, "min_length": min_length}
        new_variables = encode_variables(variables, custom_scalars)
        response_text = client.execute(
            gql("".join(set(QUERY))), variable_values=new_variables
        )
        res = cls.answerQuestionData.from_dict(response_text)
        return res.result

    # fmt: off
    @classmethod
    async def execute_async(cls, client: Client, input: str, context: str, min_length: int) -> Optional[answerQuestionData.QA_Result]:
        variables: Dict[str, Any] = {"input": input, "context": context, "min_length": min_length}
        new_variables = encode_variables(variables, custom_scalars)
        response_text = await client.execute_async(
            gql("".join(set(QUERY))), variable_values=new_variables
        )
        res = cls.answerQuestionData.from_dict(response_text)
        return res.result
