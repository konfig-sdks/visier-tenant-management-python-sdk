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

from visier_tenant_management_python_sdk.type.metric_validation_summary_dto import MetricValidationSummaryDTO

class RequiredTenantPreviewEntriesSummaryDTO(TypedDict):
    pass

class OptionalTenantPreviewEntriesSummaryDTO(TypedDict, total=False):
    # The tenant code of the analytic tenant. For example, \"WFF_j1r~i1o\".
    tenantCode: str

    # The data version ID.
    dataVersion: str

    # The date that the data version was created.
    dataVersionDate: str

    # A list of metrics and their values.
    metrics: typing.List[MetricValidationSummaryDTO]

class TenantPreviewEntriesSummaryDTO(RequiredTenantPreviewEntriesSummaryDTO, OptionalTenantPreviewEntriesSummaryDTO):
    pass
