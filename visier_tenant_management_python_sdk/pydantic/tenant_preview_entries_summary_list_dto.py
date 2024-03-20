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

from visier_tenant_management_python_sdk.pydantic.tenant_preview_entries_summary_dto import TenantPreviewEntriesSummaryDTO

class TenantPreviewEntriesSummaryListDTO(BaseModel):
    # A list of objects representing all the analytic tenants.
    tenants: typing.Optional[typing.List[TenantPreviewEntriesSummaryDTO]] = Field(None, alias='tenants')

    # The number of analytic tenants to retrieve. The maximum number to retrieve is 1000.
    limit: typing.Optional[int] = Field(None, alias='limit')

    # The index to start retrieving results from, also known as offset. The index begins at 0.
    start: typing.Optional[int] = Field(None, alias='start')
    class Config:
        arbitrary_types_allowed = True
