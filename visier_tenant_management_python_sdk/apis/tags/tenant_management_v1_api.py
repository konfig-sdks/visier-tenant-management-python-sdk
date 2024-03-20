# coding: utf-8

"""
    Visier Tenant Management APIs

    Visier APIs for managing tenants

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from visier_tenant_management_python_sdk.paths.v1_admin_tenants.post import AddTenant
from visier_tenant_management_python_sdk.paths.v1_admin_tenants_tenant_id.delete import DeleteTenant
from visier_tenant_management_python_sdk.paths.v1_admin_tenants_tenant_id_disable.put import DisableTenant
from visier_tenant_management_python_sdk.paths.v1_admin_tenants_tenant_id_enable.put import EnableTenant
from visier_tenant_management_python_sdk.paths.v1_admin_tenants_tenant_id.get import GetTenant
from visier_tenant_management_python_sdk.paths.v1_admin_tenants.get import GetTenants
from visier_tenant_management_python_sdk.paths.v1_admin_tenants_tenant_id.put import UpdateTenant
from visier_tenant_management_python_sdk.paths.v1_op_validation_tenants_tenant_id.get import ValidateTenant
from visier_tenant_management_python_sdk.paths.v1_op_validation_tenants.get import ValidateTenants
from visier_tenant_management_python_sdk.apis.tags.tenant_management_v1_api_raw import TenantManagementV1ApiRaw


class TenantManagementV1Api(
    AddTenant,
    DeleteTenant,
    DisableTenant,
    EnableTenant,
    GetTenant,
    GetTenants,
    UpdateTenant,
    ValidateTenant,
    ValidateTenants,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TenantManagementV1ApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TenantManagementV1ApiRaw(api_client)
