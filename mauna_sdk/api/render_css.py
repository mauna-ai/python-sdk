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
query renderCSS($ssml: String!, $css: String!) {
  result: callCompose(
    init: { styled_ssml: $ssml, voice_css: $css }
    pipeline: [
      {
        op: "callApplyVoiceCSS"
        transform: "r => ({text: r.$result.callApplyVoiceCSS.ssml})"
      }
      { op: "callTextToSpeech", transform: "" }
    ]
  ) {
    speech: result
  }
}

"""
]


class renderCSS:
    @dataclass(frozen=True)
    class renderCSSData(DataClassJsonMixin):
        @dataclass(frozen=True)
        class ComposeResult(DataClassJsonMixin):
            speech: Optional[dict]

        result: Optional[ComposeResult]

    # fmt: off
    @classmethod
    def execute(cls, client: Client, ssml: str, css: str) -> Optional[renderCSSData.ComposeResult]:
        variables: Dict[str, Any] = {"ssml": ssml, "css": css}
        new_variables = encode_variables(variables, custom_scalars)
        response_text = client.execute(
            gql("".join(set(QUERY))), variable_values=new_variables
        )
        res = cls.renderCSSData.from_dict(response_text)
        return res.result

    # fmt: off
    @classmethod
    async def execute_async(cls, client: Client, ssml: str, css: str) -> Optional[renderCSSData.ComposeResult]:
        variables: Dict[str, Any] = {"ssml": ssml, "css": css}
        new_variables = encode_variables(variables, custom_scalars)
        response_text = await client.execute_async(
            gql("".join(set(QUERY))), variable_values=new_variables
        )
        res = cls.renderCSSData.from_dict(response_text)
        return res.result
