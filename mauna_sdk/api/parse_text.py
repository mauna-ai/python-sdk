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
query parseText($input: String!) {
  result: callNLU(input: $input) {
    noun_chunks {
      text
      lemma

      subtree {
        dependency
        entity_type
        lemma
        normalized
        part_of_speech
        tag

        subtree {
          dependency
          entity_type
          lemma
          normalized
          part_of_speech
          tag

          subtree {
            dependency
            entity_type
            lemma
            normalized
            part_of_speech
            tag

            subtree {
              dependency
              entity_type
              lemma
              normalized
              part_of_speech
              tag
            }
          }
        }
      }
    }
    entities {
      text
      lemma

      subtree {
        dependency
        entity_type
        lemma
        normalized
        part_of_speech
        tag

        subtree {
          dependency
          entity_type
          lemma
          normalized
          part_of_speech
          tag

          subtree {
            dependency
            entity_type
            lemma
            normalized
            part_of_speech
            tag

            subtree {
              dependency
              entity_type
              lemma
              normalized
              part_of_speech
              tag
            }
          }
        }
      }
    }
    sentences {
      text
      lemma

      subtree {
        dependency
        entity_type
        lemma
        normalized
        part_of_speech
        tag

        subtree {
          dependency
          entity_type
          lemma
          normalized
          part_of_speech
          tag

          subtree {
            dependency
            entity_type
            lemma
            normalized
            part_of_speech
            tag

            subtree {
              dependency
              entity_type
              lemma
              normalized
              part_of_speech
              tag
            }
          }
        }
      }
    }
  }
}

# FIXME: Unfortunately, fragments are not supported by either codegen framework

# fragment SubtreeFields on NLUToken {
#   dependency
#   entity_type
#   lemma
#   normalized
#   part_of_speech
#   tag
# }
#
# fragment Subtree on NLUSpan {
#   subtree {
#     ...SubtreeFields
#     subtree {
#       ...SubtreeFields
#       subtree {
#         ...SubtreeFields
#         subtree {
#           ...SubtreeFields
#         }
#       }
#     }
#   }
# }

"""
]


class parseText:
    @dataclass(frozen=True)
    class parseTextData(DataClassJsonMixin):
        @dataclass(frozen=True)
        class NLUResult(DataClassJsonMixin):
            @dataclass(frozen=True)
            class NLUSpan(DataClassJsonMixin):
                @dataclass(frozen=True)
                class NLUToken(DataClassJsonMixin):
                    @dataclass(frozen=True)
                    class NLUToken(DataClassJsonMixin):
                        @dataclass(frozen=True)
                        class NLUToken(DataClassJsonMixin):
                            @dataclass(frozen=True)
                            class NLUToken(DataClassJsonMixin):
                                dependency: Optional[str]
                                entity_type: Optional[str]
                                lemma: Optional[str]
                                normalized: Optional[str]
                                part_of_speech: Optional[str]
                                tag: Optional[str]

                            dependency: Optional[str]
                            entity_type: Optional[str]
                            lemma: Optional[str]
                            normalized: Optional[str]
                            part_of_speech: Optional[str]
                            tag: Optional[str]
                            subtree: Optional[List[NLUToken]]

                        dependency: Optional[str]
                        entity_type: Optional[str]
                        lemma: Optional[str]
                        normalized: Optional[str]
                        part_of_speech: Optional[str]
                        tag: Optional[str]
                        subtree: Optional[List[NLUToken]]

                    dependency: Optional[str]
                    entity_type: Optional[str]
                    lemma: Optional[str]
                    normalized: Optional[str]
                    part_of_speech: Optional[str]
                    tag: Optional[str]
                    subtree: Optional[List[NLUToken]]

                text: Optional[str]
                lemma: Optional[str]
                subtree: Optional[List[NLUToken]]

            noun_chunks: Optional[List[NLUSpan]]
            entities: Optional[List[NLUSpan]]
            sentences: Optional[List[NLUSpan]]

        result: Optional[NLUResult]

    # fmt: off
    @classmethod
    def execute(cls, client: Client, input: str) -> Optional[parseTextData.NLUResult]:
        variables: Dict[str, Any] = {"input": input}
        new_variables = encode_variables(variables, custom_scalars)
        response_text = client.execute(
            gql("".join(set(QUERY))), variable_values=new_variables
        )
        res = cls.parseTextData.from_dict(response_text)
        return res.result

    # fmt: off
    @classmethod
    async def execute_async(cls, client: Client, input: str) -> Optional[parseTextData.NLUResult]:
        variables: Dict[str, Any] = {"input": input}
        new_variables = encode_variables(variables, custom_scalars)
        response_text = await client.execute_async(
            gql("".join(set(QUERY))), variable_values=new_variables
        )
        res = cls.parseTextData.from_dict(response_text)
        return res.result
