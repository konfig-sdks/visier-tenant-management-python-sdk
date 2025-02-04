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

from visier_tenant_management_python_sdk.type.business_location_dto import BusinessLocationDTO
from visier_tenant_management_python_sdk.type.custom_property_dto import CustomPropertyDTO
from visier_tenant_management_python_sdk.type.home_analysis_by_user_group_dto import HomeAnalysisByUserGroupDTO
from visier_tenant_management_python_sdk.type.tenant_management_api_update_response_dto_embeddable_domains import TenantManagementAPIUpdateResponseDTOEmbeddableDomains
from visier_tenant_management_python_sdk.type.tenant_management_api_update_response_dto_purchased_modules import TenantManagementAPIUpdateResponseDTOPurchasedModules
from visier_tenant_management_python_sdk.type.tenant_management_api_update_response_dto_sso_instance_issuers import TenantManagementAPIUpdateResponseDTOSsoInstanceIssuers

class RequiredTenantManagementAPIUpdateResponseDTO(TypedDict):
    pass

class OptionalTenantManagementAPIUpdateResponseDTO(TypedDict, total=False):
    # The unique identifier of the newly created analytic tenant.
    tenantCode: str

    # A comma-separated collection of strings that represent the Visier modules assigned to the new analytic tenant.
    tenantDisplayName: str

    # The 6-digit NAICS code for the industry to which the analytic tenant belongs.
    industryCode: int

    # The primary location of operations or where business is performed. If undefined, it is omitted from the response.
    primaryBusinessLocation: BusinessLocationDTO

    purchasedModules: TenantManagementAPIUpdateResponseDTOPurchasedModules

    embeddableDomains: TenantManagementAPIUpdateResponseDTOEmbeddableDomains

    # A list of objects that represent different customizable properties for the analytic tenant.
    customProperties: typing.List[CustomPropertyDTO]

    ssoInstanceIssuers: TenantManagementAPIUpdateResponseDTOSsoInstanceIssuers

    # The unique ID of the analysis to display for this tenant when a user logs in. This is optional.   Retrieve the ID by opening an analysis in the production version of a tenant and copying the string after the last forward slash (/) in the URL. For example: https://jupiter.visier.com/hr/prod/appcontainer?previewId=-eZPm8xvo3SUMpD4Q5pdE-6mCj9CQ9K699XgqRGwtOxagH5x2IzDFawlWn3hYqFEfU7nP0YK9ASEzmrNfAihGg..&previewType=Production#/analytics/myanalyses/8a4c1d4f-eb61-4da0-9e5b-55bef757c30e.  The `homeAnalysisID` is 8a4c1d4f-eb61-4da0-9e5b-55bef757c30e.   Alternatively, retrieve the ID by copying the `contentId` found by following the `Embed a visualization` documentation.
    homeAnalysisId: str

    # A list of objects representing the analysis to display to specific user groups when users log in.
    homeAnalysisByUserGroup: typing.List[HomeAnalysisByUserGroupDTO]

    # Whether the tenant is enabled or disabled. Enabled tenants have access to Visier visualizations.
    status: str

    # A custom URL to redirect users into your portal to see the relevant content. This URL is used for links that are shared by and with your users through the sharing capability or email content.
    clickThroughLink: str

    # The name of the administrating tenant used in Visier URLs.
    vanityUrlName: str

class TenantManagementAPIUpdateResponseDTO(RequiredTenantManagementAPIUpdateResponseDTO, OptionalTenantManagementAPIUpdateResponseDTO):
    pass
