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
query speechToText($audio: String!) {
  result: callSpeechToText(audioB64: $audio) {
    transcript: alternatives {
      text: transcript
    }
  }
}

"""
]


class speechToText:
    @dataclass(frozen=True)
    class speechToTextData(DataClassJsonMixin):
        @dataclass(frozen=True)
        class STTResult(DataClassJsonMixin):
            @dataclass(frozen=True)
            class TextAlternative(DataClassJsonMixin):
                text: Optional[str]

            transcript: Optional[List[TextAlternative]]

        result: Optional[List[STTResult]]

    # fmt: off
    @classmethod
    def execute(cls, client: Client, audio: str) -> List[Optional[speechToTextData.STTResult]]:
        variables: Dict[str, Any] = {"audio": audio}
        new_variables = encode_variables(variables, custom_scalars)
        response_text = client.execute(
            gql("".join(set(QUERY))), variable_values=new_variables
        )
        res = cls.speechToTextData.from_dict(response_text)
        return res.result

    # fmt: off
    @classmethod
    async def execute_async(cls, client: Client, audio: str) -> List[Optional[speechToTextData.STTResult]]:
        variables: Dict[str, Any] = {"audio": audio}
        new_variables = encode_variables(variables, custom_scalars)
        response_text = await client.execute_async(
            gql("".join(set(QUERY))), variable_values=new_variables
        )
        res = cls.speechToTextData.from_dict(response_text)
        return res.result
