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

from gql_client.runtime.enum_utils import enum_field_metadata
from .enum.relations import Relations


# fmt: off
QUERY: List[str] = ["""
query conceptnetGrounding($text: String!, $relations: [Relations]!) {
  result: callPredictRelation(text: $text, relations: $relations) {
    relation: name
    predictions: texts
  }
}

"""
]


class conceptnetGrounding:
    @dataclass(frozen=True)
    class conceptnetGroundingData(DataClassJsonMixin):
        @dataclass(frozen=True)
        class RelationResult(DataClassJsonMixin):
            relation: Optional[str]
            predictions: Optional[List[str]]

        result: Optional[List[RelationResult]]

    # fmt: off
    @classmethod
    def execute(cls, client: Client, text: str, relations: List[Relations] = []) -> List[Optional[conceptnetGroundingData.RelationResult]]:
        variables: Dict[str, Any] = {"text": text, "relations": relations}
        new_variables = encode_variables(variables, custom_scalars)
        response_text = client.execute(
            gql("".join(set(QUERY))), variable_values=new_variables
        )
        res = cls.conceptnetGroundingData.from_dict(response_text)
        return res.result

    # fmt: off
    @classmethod
    async def execute_async(cls, client: Client, text: str, relations: List[Relations] = []) -> List[Optional[conceptnetGroundingData.RelationResult]]:
        variables: Dict[str, Any] = {"text": text, "relations": relations}
        new_variables = encode_variables(variables, custom_scalars)
        response_text = await client.execute_async(
            gql("".join(set(QUERY))), variable_values=new_variables
        )
        res = cls.conceptnetGroundingData.from_dict(response_text)
        return res.result