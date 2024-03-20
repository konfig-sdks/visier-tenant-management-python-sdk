import typing_extensions

from visier_tenant_management_python_sdk.paths import PathValues
from visier_tenant_management_python_sdk.apis.paths.v1_admin_tenants import V1AdminTenants
from visier_tenant_management_python_sdk.apis.paths.v1_admin_tenants_tenant_id import V1AdminTenantsTenantId
from visier_tenant_management_python_sdk.apis.paths.v1_admin_tenants_tenant_id_disable import V1AdminTenantsTenantIdDisable
from visier_tenant_management_python_sdk.apis.paths.v1_admin_tenants_tenant_id_enable import V1AdminTenantsTenantIdEnable
from visier_tenant_management_python_sdk.apis.paths.v1_op_validation_tenants import V1OpValidationTenants
from visier_tenant_management_python_sdk.apis.paths.v1_op_validation_tenants_tenant_id import V1OpValidationTenantsTenantId
from visier_tenant_management_python_sdk.apis.paths.v2_admin_tenants import V2AdminTenants
from visier_tenant_management_python_sdk.apis.paths.v2_admin_tenants_tenant_id import V2AdminTenantsTenantId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_ADMIN_TENANTS: V1AdminTenants,
        PathValues.V1_ADMIN_TENANTS_TENANT_ID: V1AdminTenantsTenantId,
        PathValues.V1_ADMIN_TENANTS_TENANT_ID_DISABLE: V1AdminTenantsTenantIdDisable,
        PathValues.V1_ADMIN_TENANTS_TENANT_ID_ENABLE: V1AdminTenantsTenantIdEnable,
        PathValues.V1_OP_VALIDATION_TENANTS: V1OpValidationTenants,
        PathValues.V1_OP_VALIDATION_TENANTS_TENANT_ID: V1OpValidationTenantsTenantId,
        PathValues.V2_ADMIN_TENANTS: V2AdminTenants,
        PathValues.V2_ADMIN_TENANTS_TENANT_ID: V2AdminTenantsTenantId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_ADMIN_TENANTS: V1AdminTenants,
        PathValues.V1_ADMIN_TENANTS_TENANT_ID: V1AdminTenantsTenantId,
        PathValues.V1_ADMIN_TENANTS_TENANT_ID_DISABLE: V1AdminTenantsTenantIdDisable,
        PathValues.V1_ADMIN_TENANTS_TENANT_ID_ENABLE: V1AdminTenantsTenantIdEnable,
        PathValues.V1_OP_VALIDATION_TENANTS: V1OpValidationTenants,
        PathValues.V1_OP_VALIDATION_TENANTS_TENANT_ID: V1OpValidationTenantsTenantId,
        PathValues.V2_ADMIN_TENANTS: V2AdminTenants,
        PathValues.V2_ADMIN_TENANTS_TENANT_ID: V2AdminTenantsTenantId,
    }
)
