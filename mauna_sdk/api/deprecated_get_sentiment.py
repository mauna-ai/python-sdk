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
query deprecatedGetSentiment($text: String!) {
  callNlpDoc(text: $text) {
    sentiment
    sentences: sents {
      text
      sentiment
    }
  }
}

"""
]


class deprecatedGetSentiment:
    @dataclass(frozen=True)
    class deprecatedGetSentimentData(DataClassJsonMixin):
        @dataclass(frozen=True)
        class NlpDoc(DataClassJsonMixin):
            @dataclass(frozen=True)
            class Span(DataClassJsonMixin):
                text: Optional[str]
                sentiment: Optional[Number]

            sentiment: Optional[Number]
            sentences: Optional[List[Span]]

        callNlpDoc: Optional[NlpDoc]

    # fmt: off
    @classmethod
    def execute(cls, client: Client, text: str) -> Optional[deprecatedGetSentimentData.NlpDoc]:
        variables: Dict[str, Any] = {"text": text}
        new_variables = encode_variables(variables, custom_scalars)
        response_text = client.execute(
            gql("".join(set(QUERY))), variable_values=new_variables
        )
        res = cls.deprecatedGetSentimentData.from_dict(response_text)
        return res.callNlpDoc

    # fmt: off
    @classmethod
    async def execute_async(cls, client: Client, text: str) -> Optional[deprecatedGetSentimentData.NlpDoc]:
        variables: Dict[str, Any] = {"text": text}
        new_variables = encode_variables(variables, custom_scalars)
        response_text = await client.execute_async(
            gql("".join(set(QUERY))), variable_values=new_variables
        )
        res = cls.deprecatedGetSentimentData.from_dict(response_text)
        return res.callNlpDoc