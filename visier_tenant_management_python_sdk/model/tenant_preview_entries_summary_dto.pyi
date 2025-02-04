# coding: utf-8

"""
    Visier Tenant Management APIs

    Visier APIs for managing tenants

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from visier_tenant_management_python_sdk import schemas  # noqa: F401


class TenantPreviewEntriesSummaryDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            tenantCode = schemas.StrSchema
            dataVersion = schemas.StrSchema
            dataVersionDate = schemas.StrSchema
            
            
            class metrics(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['MetricValidationSummaryDTO']:
                        return MetricValidationSummaryDTO
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['MetricValidationSummaryDTO'], typing.List['MetricValidationSummaryDTO']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'metrics':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'MetricValidationSummaryDTO':
                    return super().__getitem__(i)
            __annotations__ = {
                "tenantCode": tenantCode,
                "dataVersion": dataVersion,
                "dataVersionDate": dataVersionDate,
                "metrics": metrics,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tenantCode"]) -> MetaOapg.properties.tenantCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataVersion"]) -> MetaOapg.properties.dataVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataVersionDate"]) -> MetaOapg.properties.dataVersionDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metrics"]) -> MetaOapg.properties.metrics: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tenantCode", "dataVersion", "dataVersionDate", "metrics", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tenantCode"]) -> typing.Union[MetaOapg.properties.tenantCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataVersion"]) -> typing.Union[MetaOapg.properties.dataVersion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataVersionDate"]) -> typing.Union[MetaOapg.properties.dataVersionDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metrics"]) -> typing.Union[MetaOapg.properties.metrics, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tenantCode", "dataVersion", "dataVersionDate", "metrics", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        tenantCode: typing.Union[MetaOapg.properties.tenantCode, str, schemas.Unset] = schemas.unset,
        dataVersion: typing.Union[MetaOapg.properties.dataVersion, str, schemas.Unset] = schemas.unset,
        dataVersionDate: typing.Union[MetaOapg.properties.dataVersionDate, str, schemas.Unset] = schemas.unset,
        metrics: typing.Union[MetaOapg.properties.metrics, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TenantPreviewEntriesSummaryDTO':
        return super().__new__(
            cls,
            *args,
            tenantCode=tenantCode,
            dataVersion=dataVersion,
            dataVersionDate=dataVersionDate,
            metrics=metrics,
            _configuration=_configuration,
            **kwargs,
        )

from visier_tenant_management_python_sdk.model.metric_validation_summary_dto import MetricValidationSummaryDTO
