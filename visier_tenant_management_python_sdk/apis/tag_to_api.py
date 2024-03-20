import typing_extensions

from visier_tenant_management_python_sdk.apis.tags import TagValues
from visier_tenant_management_python_sdk.apis.tags.tenant_management_v1_api import TenantManagementV1Api
from visier_tenant_management_python_sdk.apis.tags.tenant_management_api import TenantManagementApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.TENANT_MANAGEMENT_V1: TenantManagementV1Api,
        TagValues.TENANT_MANAGEMENT: TenantManagementApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.TENANT_MANAGEMENT_V1: TenantManagementV1Api,
        TagValues.TENANT_MANAGEMENT: TenantManagementApi,
    }
)
