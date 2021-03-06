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
query resolveCoreferences($input: String!) {
  result: callResolveCoreference(input: $input) {
    resolved_text: result
    coreferences {
      mention
      reference {
        score
        text
      }
    }
    has_coreference
  }
}

"""
]


class resolveCoreferences:
    @dataclass(frozen=True)
    class resolveCoreferencesData(DataClassJsonMixin):
        @dataclass(frozen=True)
        class CorefResult(DataClassJsonMixin):
            @dataclass(frozen=True)
            class CorefResultScores(DataClassJsonMixin):
                @dataclass(frozen=True)
                class ResultScores(DataClassJsonMixin):
                    score: Optional[Number]
                    text: Optional[str]

                mention: Optional[str]
                reference: Optional[List[ResultScores]]

            resolved_text: Optional[str]
            coreferences: Optional[List[CorefResultScores]]
            has_coreference: Optional[bool]

        result: Optional[CorefResult]

    # fmt: off
    @classmethod
    def execute(cls, client: Client, input: str) -> Optional[resolveCoreferencesData.CorefResult]:
        variables: Dict[str, Any] = {"input": input}
        new_variables = encode_variables(variables, custom_scalars)
        response_text = client.execute(
            gql("".join(set(QUERY))), variable_values=new_variables
        )
        res = cls.resolveCoreferencesData.from_dict(response_text)
        return res.result

    # fmt: off
    @classmethod
    async def execute_async(cls, client: Client, input: str) -> Optional[resolveCoreferencesData.CorefResult]:
        variables: Dict[str, Any] = {"input": input}
        new_variables = encode_variables(variables, custom_scalars)
        response_text = await client.execute_async(
            gql("".join(set(QUERY))), variable_values=new_variables
        )
        res = cls.resolveCoreferencesData.from_dict(response_text)
        return res.result
