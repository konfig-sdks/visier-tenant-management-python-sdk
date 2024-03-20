# coding: utf-8

"""
    Visier Tenant Management APIs

    Visier APIs for managing tenants

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from visier_tenant_management_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from visier_tenant_management_python_sdk.api_response import AsyncGeneratorResponse
from visier_tenant_management_python_sdk import api_client, exceptions
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

from visier_tenant_management_python_sdk.model.tenant_management_api_update_request_dto_sso_instance_issuers import TenantManagementAPIUpdateRequestDTOSsoInstanceIssuers as TenantManagementAPIUpdateRequestDTOSsoInstanceIssuersSchema
from visier_tenant_management_python_sdk.model.tenant_management_api_update_request_dto import TenantManagementAPIUpdateRequestDTO as TenantManagementAPIUpdateRequestDTOSchema
from visier_tenant_management_python_sdk.model.business_location_dto import BusinessLocationDTO as BusinessLocationDTOSchema
from visier_tenant_management_python_sdk.model.custom_property_dto import CustomPropertyDTO as CustomPropertyDTOSchema
from visier_tenant_management_python_sdk.model.home_analysis_by_user_group_dto import HomeAnalysisByUserGroupDTO as HomeAnalysisByUserGroupDTOSchema
from visier_tenant_management_python_sdk.model.tenant_management_api_update_request_dto_embeddable_domains import TenantManagementAPIUpdateRequestDTOEmbeddableDomains as TenantManagementAPIUpdateRequestDTOEmbeddableDomainsSchema
from visier_tenant_management_python_sdk.model.tenant_management_api_update_request_dto_purchased_modules import TenantManagementAPIUpdateRequestDTOPurchasedModules as TenantManagementAPIUpdateRequestDTOPurchasedModulesSchema
from visier_tenant_management_python_sdk.model.status import Status as StatusSchema
from visier_tenant_management_python_sdk.model.tenant_management_api_update_response_dto import TenantManagementAPIUpdateResponseDTO as TenantManagementAPIUpdateResponseDTOSchema

from visier_tenant_management_python_sdk.type.status import Status
from visier_tenant_management_python_sdk.type.business_location_dto import BusinessLocationDTO
from visier_tenant_management_python_sdk.type.tenant_management_api_update_request_dto_embeddable_domains import TenantManagementAPIUpdateRequestDTOEmbeddableDomains
from visier_tenant_management_python_sdk.type.tenant_management_api_update_request_dto import TenantManagementAPIUpdateRequestDTO
from visier_tenant_management_python_sdk.type.custom_property_dto import CustomPropertyDTO
from visier_tenant_management_python_sdk.type.home_analysis_by_user_group_dto import HomeAnalysisByUserGroupDTO
from visier_tenant_management_python_sdk.type.tenant_management_api_update_request_dto_purchased_modules import TenantManagementAPIUpdateRequestDTOPurchasedModules
from visier_tenant_management_python_sdk.type.tenant_management_api_update_response_dto import TenantManagementAPIUpdateResponseDTO
from visier_tenant_management_python_sdk.type.tenant_management_api_update_request_dto_sso_instance_issuers import TenantManagementAPIUpdateRequestDTOSsoInstanceIssuers

from ...api_client import Dictionary
from visier_tenant_management_python_sdk.pydantic.tenant_management_api_update_request_dto import TenantManagementAPIUpdateRequestDTO as TenantManagementAPIUpdateRequestDTOPydantic
from visier_tenant_management_python_sdk.pydantic.tenant_management_api_update_request_dto_sso_instance_issuers import TenantManagementAPIUpdateRequestDTOSsoInstanceIssuers as TenantManagementAPIUpdateRequestDTOSsoInstanceIssuersPydantic
from visier_tenant_management_python_sdk.pydantic.home_analysis_by_user_group_dto import HomeAnalysisByUserGroupDTO as HomeAnalysisByUserGroupDTOPydantic
from visier_tenant_management_python_sdk.pydantic.tenant_management_api_update_request_dto_embeddable_domains import TenantManagementAPIUpdateRequestDTOEmbeddableDomains as TenantManagementAPIUpdateRequestDTOEmbeddableDomainsPydantic
from visier_tenant_management_python_sdk.pydantic.tenant_management_api_update_request_dto_purchased_modules import TenantManagementAPIUpdateRequestDTOPurchasedModules as TenantManagementAPIUpdateRequestDTOPurchasedModulesPydantic
from visier_tenant_management_python_sdk.pydantic.business_location_dto import BusinessLocationDTO as BusinessLocationDTOPydantic
from visier_tenant_management_python_sdk.pydantic.status import Status as StatusPydantic
from visier_tenant_management_python_sdk.pydantic.custom_property_dto import CustomPropertyDTO as CustomPropertyDTOPydantic
from visier_tenant_management_python_sdk.pydantic.tenant_management_api_update_response_dto import TenantManagementAPIUpdateResponseDTO as TenantManagementAPIUpdateResponseDTOPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = TenantManagementAPIUpdateRequestDTOSchema


request_body_tenant_management_api_update_request_dto = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'ApiKeyAuth',
    'BearerAuth',
    'CookieAuth',
    'OAuth2Auth',
    'OAuth2Auth',
]
SchemaFor200ResponseBodyApplicationJson = TenantManagementAPIUpdateResponseDTOSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: TenantManagementAPIUpdateResponseDTO


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: TenantManagementAPIUpdateResponseDTO


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = StatusSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: Status


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: Status


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_tenant_mapped_args(
        self,
        tenant_code: typing.Optional[str] = None,
        tenant_display_name: typing.Optional[str] = None,
        tenant_short_name: typing.Optional[str] = None,
        vanity_url_name: typing.Optional[str] = None,
        industry_code: typing.Optional[int] = None,
        primary_business_location: typing.Optional[BusinessLocationDTO] = None,
        purchased_modules: typing.Optional[TenantManagementAPIUpdateRequestDTOPurchasedModules] = None,
        embeddable_domains: typing.Optional[TenantManagementAPIUpdateRequestDTOEmbeddableDomains] = None,
        custom_properties: typing.Optional[typing.List[CustomPropertyDTO]] = None,
        sso_instance_issuers: typing.Optional[TenantManagementAPIUpdateRequestDTOSsoInstanceIssuers] = None,
        home_analysis_id: typing.Optional[str] = None,
        home_analysis_by_user_group: typing.Optional[typing.List[HomeAnalysisByUserGroupDTO]] = None,
        update_action: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = None,
        click_through_link: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if tenant_code is not None:
            _body["tenantCode"] = tenant_code
        if tenant_display_name is not None:
            _body["tenantDisplayName"] = tenant_display_name
        if tenant_short_name is not None:
            _body["tenantShortName"] = tenant_short_name
        if vanity_url_name is not None:
            _body["vanityUrlName"] = vanity_url_name
        if industry_code is not None:
            _body["industryCode"] = industry_code
        if primary_business_location is not None:
            _body["primaryBusinessLocation"] = primary_business_location
        if purchased_modules is not None:
            _body["purchasedModules"] = purchased_modules
        if embeddable_domains is not None:
            _body["embeddableDomains"] = embeddable_domains
        if custom_properties is not None:
            _body["customProperties"] = custom_properties
        if sso_instance_issuers is not None:
            _body["ssoInstanceIssuers"] = sso_instance_issuers
        if home_analysis_id is not None:
            _body["homeAnalysisId"] = home_analysis_id
        if home_analysis_by_user_group is not None:
            _body["homeAnalysisByUserGroup"] = home_analysis_by_user_group
        if update_action is not None:
            _body["updateAction"] = update_action
        if enabled is not None:
            _body["enabled"] = enabled
        if click_through_link is not None:
            _body["clickThroughLink"] = click_through_link
        args.body = _body
        return args

    async def _acreate_tenant_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Add an analytic tenant
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/admin/tenants',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_tenant_management_api_update_request_dto.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_tenant_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Add an analytic tenant
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/admin/tenants',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_tenant_management_api_update_request_dto.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateTenantRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_tenant(
        self,
        tenant_code: typing.Optional[str] = None,
        tenant_display_name: typing.Optional[str] = None,
        tenant_short_name: typing.Optional[str] = None,
        vanity_url_name: typing.Optional[str] = None,
        industry_code: typing.Optional[int] = None,
        primary_business_location: typing.Optional[BusinessLocationDTO] = None,
        purchased_modules: typing.Optional[TenantManagementAPIUpdateRequestDTOPurchasedModules] = None,
        embeddable_domains: typing.Optional[TenantManagementAPIUpdateRequestDTOEmbeddableDomains] = None,
        custom_properties: typing.Optional[typing.List[CustomPropertyDTO]] = None,
        sso_instance_issuers: typing.Optional[TenantManagementAPIUpdateRequestDTOSsoInstanceIssuers] = None,
        home_analysis_id: typing.Optional[str] = None,
        home_analysis_by_user_group: typing.Optional[typing.List[HomeAnalysisByUserGroupDTO]] = None,
        update_action: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = None,
        click_through_link: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_tenant_mapped_args(
            tenant_code=tenant_code,
            tenant_display_name=tenant_display_name,
            tenant_short_name=tenant_short_name,
            vanity_url_name=vanity_url_name,
            industry_code=industry_code,
            primary_business_location=primary_business_location,
            purchased_modules=purchased_modules,
            embeddable_domains=embeddable_domains,
            custom_properties=custom_properties,
            sso_instance_issuers=sso_instance_issuers,
            home_analysis_id=home_analysis_id,
            home_analysis_by_user_group=home_analysis_by_user_group,
            update_action=update_action,
            enabled=enabled,
            click_through_link=click_through_link,
        )
        return await self._acreate_tenant_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_tenant(
        self,
        tenant_code: typing.Optional[str] = None,
        tenant_display_name: typing.Optional[str] = None,
        tenant_short_name: typing.Optional[str] = None,
        vanity_url_name: typing.Optional[str] = None,
        industry_code: typing.Optional[int] = None,
        primary_business_location: typing.Optional[BusinessLocationDTO] = None,
        purchased_modules: typing.Optional[TenantManagementAPIUpdateRequestDTOPurchasedModules] = None,
        embeddable_domains: typing.Optional[TenantManagementAPIUpdateRequestDTOEmbeddableDomains] = None,
        custom_properties: typing.Optional[typing.List[CustomPropertyDTO]] = None,
        sso_instance_issuers: typing.Optional[TenantManagementAPIUpdateRequestDTOSsoInstanceIssuers] = None,
        home_analysis_id: typing.Optional[str] = None,
        home_analysis_by_user_group: typing.Optional[typing.List[HomeAnalysisByUserGroupDTO]] = None,
        update_action: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = None,
        click_through_link: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_tenant_mapped_args(
            tenant_code=tenant_code,
            tenant_display_name=tenant_display_name,
            tenant_short_name=tenant_short_name,
            vanity_url_name=vanity_url_name,
            industry_code=industry_code,
            primary_business_location=primary_business_location,
            purchased_modules=purchased_modules,
            embeddable_domains=embeddable_domains,
            custom_properties=custom_properties,
            sso_instance_issuers=sso_instance_issuers,
            home_analysis_id=home_analysis_id,
            home_analysis_by_user_group=home_analysis_by_user_group,
            update_action=update_action,
            enabled=enabled,
            click_through_link=click_through_link,
        )
        return self._create_tenant_oapg(
            body=args.body,
        )

class CreateTenant(BaseApi):

    async def acreate_tenant(
        self,
        tenant_code: typing.Optional[str] = None,
        tenant_display_name: typing.Optional[str] = None,
        tenant_short_name: typing.Optional[str] = None,
        vanity_url_name: typing.Optional[str] = None,
        industry_code: typing.Optional[int] = None,
        primary_business_location: typing.Optional[BusinessLocationDTO] = None,
        purchased_modules: typing.Optional[TenantManagementAPIUpdateRequestDTOPurchasedModules] = None,
        embeddable_domains: typing.Optional[TenantManagementAPIUpdateRequestDTOEmbeddableDomains] = None,
        custom_properties: typing.Optional[typing.List[CustomPropertyDTO]] = None,
        sso_instance_issuers: typing.Optional[TenantManagementAPIUpdateRequestDTOSsoInstanceIssuers] = None,
        home_analysis_id: typing.Optional[str] = None,
        home_analysis_by_user_group: typing.Optional[typing.List[HomeAnalysisByUserGroupDTO]] = None,
        update_action: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = None,
        click_through_link: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> TenantManagementAPIUpdateResponseDTOPydantic:
        raw_response = await self.raw.acreate_tenant(
            tenant_code=tenant_code,
            tenant_display_name=tenant_display_name,
            tenant_short_name=tenant_short_name,
            vanity_url_name=vanity_url_name,
            industry_code=industry_code,
            primary_business_location=primary_business_location,
            purchased_modules=purchased_modules,
            embeddable_domains=embeddable_domains,
            custom_properties=custom_properties,
            sso_instance_issuers=sso_instance_issuers,
            home_analysis_id=home_analysis_id,
            home_analysis_by_user_group=home_analysis_by_user_group,
            update_action=update_action,
            enabled=enabled,
            click_through_link=click_through_link,
            **kwargs,
        )
        if validate:
            return TenantManagementAPIUpdateResponseDTOPydantic(**raw_response.body)
        return api_client.construct_model_instance(TenantManagementAPIUpdateResponseDTOPydantic, raw_response.body)
    
    
    def create_tenant(
        self,
        tenant_code: typing.Optional[str] = None,
        tenant_display_name: typing.Optional[str] = None,
        tenant_short_name: typing.Optional[str] = None,
        vanity_url_name: typing.Optional[str] = None,
        industry_code: typing.Optional[int] = None,
        primary_business_location: typing.Optional[BusinessLocationDTO] = None,
        purchased_modules: typing.Optional[TenantManagementAPIUpdateRequestDTOPurchasedModules] = None,
        embeddable_domains: typing.Optional[TenantManagementAPIUpdateRequestDTOEmbeddableDomains] = None,
        custom_properties: typing.Optional[typing.List[CustomPropertyDTO]] = None,
        sso_instance_issuers: typing.Optional[TenantManagementAPIUpdateRequestDTOSsoInstanceIssuers] = None,
        home_analysis_id: typing.Optional[str] = None,
        home_analysis_by_user_group: typing.Optional[typing.List[HomeAnalysisByUserGroupDTO]] = None,
        update_action: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = None,
        click_through_link: typing.Optional[str] = None,
        validate: bool = False,
    ) -> TenantManagementAPIUpdateResponseDTOPydantic:
        raw_response = self.raw.create_tenant(
            tenant_code=tenant_code,
            tenant_display_name=tenant_display_name,
            tenant_short_name=tenant_short_name,
            vanity_url_name=vanity_url_name,
            industry_code=industry_code,
            primary_business_location=primary_business_location,
            purchased_modules=purchased_modules,
            embeddable_domains=embeddable_domains,
            custom_properties=custom_properties,
            sso_instance_issuers=sso_instance_issuers,
            home_analysis_id=home_analysis_id,
            home_analysis_by_user_group=home_analysis_by_user_group,
            update_action=update_action,
            enabled=enabled,
            click_through_link=click_through_link,
        )
        if validate:
            return TenantManagementAPIUpdateResponseDTOPydantic(**raw_response.body)
        return api_client.construct_model_instance(TenantManagementAPIUpdateResponseDTOPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        tenant_code: typing.Optional[str] = None,
        tenant_display_name: typing.Optional[str] = None,
        tenant_short_name: typing.Optional[str] = None,
        vanity_url_name: typing.Optional[str] = None,
        industry_code: typing.Optional[int] = None,
        primary_business_location: typing.Optional[BusinessLocationDTO] = None,
        purchased_modules: typing.Optional[TenantManagementAPIUpdateRequestDTOPurchasedModules] = None,
        embeddable_domains: typing.Optional[TenantManagementAPIUpdateRequestDTOEmbeddableDomains] = None,
        custom_properties: typing.Optional[typing.List[CustomPropertyDTO]] = None,
        sso_instance_issuers: typing.Optional[TenantManagementAPIUpdateRequestDTOSsoInstanceIssuers] = None,
        home_analysis_id: typing.Optional[str] = None,
        home_analysis_by_user_group: typing.Optional[typing.List[HomeAnalysisByUserGroupDTO]] = None,
        update_action: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = None,
        click_through_link: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_tenant_mapped_args(
            tenant_code=tenant_code,
            tenant_display_name=tenant_display_name,
            tenant_short_name=tenant_short_name,
            vanity_url_name=vanity_url_name,
            industry_code=industry_code,
            primary_business_location=primary_business_location,
            purchased_modules=purchased_modules,
            embeddable_domains=embeddable_domains,
            custom_properties=custom_properties,
            sso_instance_issuers=sso_instance_issuers,
            home_analysis_id=home_analysis_id,
            home_analysis_by_user_group=home_analysis_by_user_group,
            update_action=update_action,
            enabled=enabled,
            click_through_link=click_through_link,
        )
        return await self._acreate_tenant_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        tenant_code: typing.Optional[str] = None,
        tenant_display_name: typing.Optional[str] = None,
        tenant_short_name: typing.Optional[str] = None,
        vanity_url_name: typing.Optional[str] = None,
        industry_code: typing.Optional[int] = None,
        primary_business_location: typing.Optional[BusinessLocationDTO] = None,
        purchased_modules: typing.Optional[TenantManagementAPIUpdateRequestDTOPurchasedModules] = None,
        embeddable_domains: typing.Optional[TenantManagementAPIUpdateRequestDTOEmbeddableDomains] = None,
        custom_properties: typing.Optional[typing.List[CustomPropertyDTO]] = None,
        sso_instance_issuers: typing.Optional[TenantManagementAPIUpdateRequestDTOSsoInstanceIssuers] = None,
        home_analysis_id: typing.Optional[str] = None,
        home_analysis_by_user_group: typing.Optional[typing.List[HomeAnalysisByUserGroupDTO]] = None,
        update_action: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = None,
        click_through_link: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_tenant_mapped_args(
            tenant_code=tenant_code,
            tenant_display_name=tenant_display_name,
            tenant_short_name=tenant_short_name,
            vanity_url_name=vanity_url_name,
            industry_code=industry_code,
            primary_business_location=primary_business_location,
            purchased_modules=purchased_modules,
            embeddable_domains=embeddable_domains,
            custom_properties=custom_properties,
            sso_instance_issuers=sso_instance_issuers,
            home_analysis_id=home_analysis_id,
            home_analysis_by_user_group=home_analysis_by_user_group,
            update_action=update_action,
            enabled=enabled,
            click_through_link=click_through_link,
        )
        return self._create_tenant_oapg(
            body=args.body,
        )

