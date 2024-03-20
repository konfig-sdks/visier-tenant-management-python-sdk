# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from visier_tenant_management_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_ADMIN_TENANTS = "/v1/admin/tenants"
    V1_ADMIN_TENANTS_TENANT_ID = "/v1/admin/tenants/:tenantId"
    V1_ADMIN_TENANTS_TENANT_ID_DISABLE = "/v1/admin/tenants/:tenantId/disable"
    V1_ADMIN_TENANTS_TENANT_ID_ENABLE = "/v1/admin/tenants/:tenantId/enable"
    V1_OP_VALIDATION_TENANTS = "/v1/op/validation/tenants"
    V1_OP_VALIDATION_TENANTS_TENANT_ID = "/v1/op/validation/tenants/:tenantId"
    V2_ADMIN_TENANTS = "/v2/admin/tenants"
    V2_ADMIN_TENANTS_TENANT_ID = "/v2/admin/tenants/:tenantId"
    V2_ADMIN_TENANTS_TENANT_ID = "/v2/admin/tenants/{tenantId}"
