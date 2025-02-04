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


class RequiredMetricValidationSummaryDTO(TypedDict):
    pass

class OptionalMetricValidationSummaryDTO(TypedDict, total=False):
    # The symbol name of the metric. For example, \"employeeCount\".
    symbolName: str

    # An identifiable name that is displayed within Visier. For example, \"Headcount\".
    displayName: str

    # The current value of the metric expressed as an integer.
    value: typing.Union[int, float]

class MetricValidationSummaryDTO(RequiredMetricValidationSummaryDTO, OptionalMetricValidationSummaryDTO):
    pass
