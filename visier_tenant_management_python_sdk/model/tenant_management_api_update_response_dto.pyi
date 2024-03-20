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


class TenantManagementAPIUpdateResponseDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            tenantCode = schemas.StrSchema
            tenantDisplayName = schemas.StrSchema
            industryCode = schemas.IntSchema
        
            @staticmethod
            def primaryBusinessLocation() -> typing.Type['BusinessLocationDTO']:
                return BusinessLocationDTO
        
            @staticmethod
            def purchasedModules() -> typing.Type['TenantManagementAPIUpdateResponseDTOPurchasedModules']:
                return TenantManagementAPIUpdateResponseDTOPurchasedModules
        
            @staticmethod
            def embeddableDomains() -> typing.Type['TenantManagementAPIUpdateResponseDTOEmbeddableDomains']:
                return TenantManagementAPIUpdateResponseDTOEmbeddableDomains
            
            
            class customProperties(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CustomPropertyDTO']:
                        return CustomPropertyDTO
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CustomPropertyDTO'], typing.List['CustomPropertyDTO']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'customProperties':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CustomPropertyDTO':
                    return super().__getitem__(i)
        
            @staticmethod
            def ssoInstanceIssuers() -> typing.Type['TenantManagementAPIUpdateResponseDTOSsoInstanceIssuers']:
                return TenantManagementAPIUpdateResponseDTOSsoInstanceIssuers
            homeAnalysisId = schemas.StrSchema
            
            
            class homeAnalysisByUserGroup(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['HomeAnalysisByUserGroupDTO']:
                        return HomeAnalysisByUserGroupDTO
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['HomeAnalysisByUserGroupDTO'], typing.List['HomeAnalysisByUserGroupDTO']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'homeAnalysisByUserGroup':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'HomeAnalysisByUserGroupDTO':
                    return super().__getitem__(i)
            status = schemas.StrSchema
            clickThroughLink = schemas.StrSchema
            vanityUrlName = schemas.StrSchema
            __annotations__ = {
                "tenantCode": tenantCode,
                "tenantDisplayName": tenantDisplayName,
                "industryCode": industryCode,
                "primaryBusinessLocation": primaryBusinessLocation,
                "purchasedModules": purchasedModules,
                "embeddableDomains": embeddableDomains,
                "customProperties": customProperties,
                "ssoInstanceIssuers": ssoInstanceIssuers,
                "homeAnalysisId": homeAnalysisId,
                "homeAnalysisByUserGroup": homeAnalysisByUserGroup,
                "status": status,
                "clickThroughLink": clickThroughLink,
                "vanityUrlName": vanityUrlName,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tenantCode"]) -> MetaOapg.properties.tenantCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tenantDisplayName"]) -> MetaOapg.properties.tenantDisplayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["industryCode"]) -> MetaOapg.properties.industryCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primaryBusinessLocation"]) -> 'BusinessLocationDTO': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["purchasedModules"]) -> 'TenantManagementAPIUpdateResponseDTOPurchasedModules': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["embeddableDomains"]) -> 'TenantManagementAPIUpdateResponseDTOEmbeddableDomains': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customProperties"]) -> MetaOapg.properties.customProperties: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssoInstanceIssuers"]) -> 'TenantManagementAPIUpdateResponseDTOSsoInstanceIssuers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["homeAnalysisId"]) -> MetaOapg.properties.homeAnalysisId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["homeAnalysisByUserGroup"]) -> MetaOapg.properties.homeAnalysisByUserGroup: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clickThroughLink"]) -> MetaOapg.properties.clickThroughLink: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vanityUrlName"]) -> MetaOapg.properties.vanityUrlName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tenantCode", "tenantDisplayName", "industryCode", "primaryBusinessLocation", "purchasedModules", "embeddableDomains", "customProperties", "ssoInstanceIssuers", "homeAnalysisId", "homeAnalysisByUserGroup", "status", "clickThroughLink", "vanityUrlName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tenantCode"]) -> typing.Union[MetaOapg.properties.tenantCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tenantDisplayName"]) -> typing.Union[MetaOapg.properties.tenantDisplayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["industryCode"]) -> typing.Union[MetaOapg.properties.industryCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primaryBusinessLocation"]) -> typing.Union['BusinessLocationDTO', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["purchasedModules"]) -> typing.Union['TenantManagementAPIUpdateResponseDTOPurchasedModules', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["embeddableDomains"]) -> typing.Union['TenantManagementAPIUpdateResponseDTOEmbeddableDomains', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customProperties"]) -> typing.Union[MetaOapg.properties.customProperties, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssoInstanceIssuers"]) -> typing.Union['TenantManagementAPIUpdateResponseDTOSsoInstanceIssuers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["homeAnalysisId"]) -> typing.Union[MetaOapg.properties.homeAnalysisId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["homeAnalysisByUserGroup"]) -> typing.Union[MetaOapg.properties.homeAnalysisByUserGroup, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clickThroughLink"]) -> typing.Union[MetaOapg.properties.clickThroughLink, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vanityUrlName"]) -> typing.Union[MetaOapg.properties.vanityUrlName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tenantCode", "tenantDisplayName", "industryCode", "primaryBusinessLocation", "purchasedModules", "embeddableDomains", "customProperties", "ssoInstanceIssuers", "homeAnalysisId", "homeAnalysisByUserGroup", "status", "clickThroughLink", "vanityUrlName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        tenantCode: typing.Union[MetaOapg.properties.tenantCode, str, schemas.Unset] = schemas.unset,
        tenantDisplayName: typing.Union[MetaOapg.properties.tenantDisplayName, str, schemas.Unset] = schemas.unset,
        industryCode: typing.Union[MetaOapg.properties.industryCode, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        primaryBusinessLocation: typing.Union['BusinessLocationDTO', schemas.Unset] = schemas.unset,
        purchasedModules: typing.Union['TenantManagementAPIUpdateResponseDTOPurchasedModules', schemas.Unset] = schemas.unset,
        embeddableDomains: typing.Union['TenantManagementAPIUpdateResponseDTOEmbeddableDomains', schemas.Unset] = schemas.unset,
        customProperties: typing.Union[MetaOapg.properties.customProperties, list, tuple, schemas.Unset] = schemas.unset,
        ssoInstanceIssuers: typing.Union['TenantManagementAPIUpdateResponseDTOSsoInstanceIssuers', schemas.Unset] = schemas.unset,
        homeAnalysisId: typing.Union[MetaOapg.properties.homeAnalysisId, str, schemas.Unset] = schemas.unset,
        homeAnalysisByUserGroup: typing.Union[MetaOapg.properties.homeAnalysisByUserGroup, list, tuple, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        clickThroughLink: typing.Union[MetaOapg.properties.clickThroughLink, str, schemas.Unset] = schemas.unset,
        vanityUrlName: typing.Union[MetaOapg.properties.vanityUrlName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TenantManagementAPIUpdateResponseDTO':
        return super().__new__(
            cls,
            *args,
            tenantCode=tenantCode,
            tenantDisplayName=tenantDisplayName,
            industryCode=industryCode,
            primaryBusinessLocation=primaryBusinessLocation,
            purchasedModules=purchasedModules,
            embeddableDomains=embeddableDomains,
            customProperties=customProperties,
            ssoInstanceIssuers=ssoInstanceIssuers,
            homeAnalysisId=homeAnalysisId,
            homeAnalysisByUserGroup=homeAnalysisByUserGroup,
            status=status,
            clickThroughLink=clickThroughLink,
            vanityUrlName=vanityUrlName,
            _configuration=_configuration,
            **kwargs,
        )

from visier_tenant_management_python_sdk.model.business_location_dto import BusinessLocationDTO
from visier_tenant_management_python_sdk.model.custom_property_dto import CustomPropertyDTO
from visier_tenant_management_python_sdk.model.home_analysis_by_user_group_dto import HomeAnalysisByUserGroupDTO
from visier_tenant_management_python_sdk.model.tenant_management_api_update_response_dto_embeddable_domains import TenantManagementAPIUpdateResponseDTOEmbeddableDomains
from visier_tenant_management_python_sdk.model.tenant_management_api_update_response_dto_purchased_modules import TenantManagementAPIUpdateResponseDTOPurchasedModules
from visier_tenant_management_python_sdk.model.tenant_management_api_update_response_dto_sso_instance_issuers import TenantManagementAPIUpdateResponseDTOSsoInstanceIssuers
