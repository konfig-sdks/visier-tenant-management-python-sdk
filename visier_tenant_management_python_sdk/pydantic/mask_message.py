# coding: utf-8

"""
    Visier Tenant Management APIs

    Visier APIs for managing tenants

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel


class MaskMessage(BaseModel):
    # A comma separated list of strings that specifies which fields to include in the response.
    mask: typing.Optional[str] = Field(None, alias='mask')
    class Config:
        arbitrary_types_allowed = True
