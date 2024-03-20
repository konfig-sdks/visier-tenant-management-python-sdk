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


class TenantModuleDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            displayName = schemas.StrSchema
            symbolName = schemas.StrSchema
        
            @staticmethod
            def moduleSettings() -> typing.Type['ModuleSettingsDTO']:
                return ModuleSettingsDTO
            __annotations__ = {
                "displayName": displayName,
                "symbolName": symbolName,
                "moduleSettings": moduleSettings,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbolName"]) -> MetaOapg.properties.symbolName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["moduleSettings"]) -> 'ModuleSettingsDTO': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["displayName", "symbolName", "moduleSettings", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbolName"]) -> typing.Union[MetaOapg.properties.symbolName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["moduleSettings"]) -> typing.Union['ModuleSettingsDTO', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["displayName", "symbolName", "moduleSettings", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        displayName: typing.Union[MetaOapg.properties.displayName, str, schemas.Unset] = schemas.unset,
        symbolName: typing.Union[MetaOapg.properties.symbolName, str, schemas.Unset] = schemas.unset,
        moduleSettings: typing.Union['ModuleSettingsDTO', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TenantModuleDTO':
        return super().__new__(
            cls,
            *args,
            displayName=displayName,
            symbolName=symbolName,
            moduleSettings=moduleSettings,
            _configuration=_configuration,
            **kwargs,
        )

from visier_tenant_management_python_sdk.model.module_settings_dto import ModuleSettingsDTO
