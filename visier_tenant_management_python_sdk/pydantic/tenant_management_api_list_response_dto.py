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

from visier_tenant_management_python_sdk.pydantic.tenant_management_api_get_response_dto import TenantManagementAPIGetResponseDTO

class TenantManagementAPIListResponseDTO(BaseModel):
    # A list of objects representing all the analytic tenants.
    tenants: typing.Optional[typing.List[TenantManagementAPIGetResponseDTO]] = Field(None, alias='tenants')

    # The limit of analytic tenants to return. The maximum value is 1000. The default is 150.
    limit: typing.Optional[int] = Field(None, alias='limit')

    # The index to start retrieving values from, also known as offset. The index begins at 0.
    start: typing.Optional[int] = Field(None, alias='start')
    class Config:
        arbitrary_types_allowed = True
