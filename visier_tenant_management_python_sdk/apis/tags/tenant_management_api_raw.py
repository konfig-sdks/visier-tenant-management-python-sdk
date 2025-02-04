# coding: utf-8

"""
    Visier Tenant Management APIs

    Visier APIs for managing tenants

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from visier_tenant_management_python_sdk.paths.v2_admin_tenants.post import CreateTenantRaw
from visier_tenant_management_python_sdk.paths.v2_admin_tenants.get import ListTenantsRaw
from visier_tenant_management_python_sdk.paths.v2_admin_tenants_tenant_id.get import TenantInfoRaw
from visier_tenant_management_python_sdk.paths.v2_admin_tenants_tenant_id.put import UpdateTenantRaw


class TenantManagementApiRaw(
    CreateTenantRaw,
    ListTenantsRaw,
    TenantInfoRaw,
    UpdateTenantRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
