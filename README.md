<div align="center">

[![Visit Visier](./header.png)](https://visier.com)

# Visier<a id="visier"></a>

Visier APIs for managing tenants


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`visiertenantmanagement.tenant_management.create_tenant`](#visiertenantmanagementtenant_managementcreate_tenant)
  * [`visiertenantmanagement.tenant_management.list_tenants`](#visiertenantmanagementtenant_managementlist_tenants)
  * [`visiertenantmanagement.tenant_management.tenant_info`](#visiertenantmanagementtenant_managementtenant_info)
  * [`visiertenantmanagement.tenant_management.update_tenant`](#visiertenantmanagementtenant_managementupdate_tenant)
  * [`visiertenantmanagement.tenant_management_v1.add_tenant`](#visiertenantmanagementtenant_management_v1add_tenant)
  * [`visiertenantmanagement.tenant_management_v1.delete_tenant`](#visiertenantmanagementtenant_management_v1delete_tenant)
  * [`visiertenantmanagement.tenant_management_v1.disable_tenant`](#visiertenantmanagementtenant_management_v1disable_tenant)
  * [`visiertenantmanagement.tenant_management_v1.enable_tenant`](#visiertenantmanagementtenant_management_v1enable_tenant)
  * [`visiertenantmanagement.tenant_management_v1.get_tenant`](#visiertenantmanagementtenant_management_v1get_tenant)
  * [`visiertenantmanagement.tenant_management_v1.get_tenants`](#visiertenantmanagementtenant_management_v1get_tenants)
  * [`visiertenantmanagement.tenant_management_v1.update_tenant`](#visiertenantmanagementtenant_management_v1update_tenant)
  * [`visiertenantmanagement.tenant_management_v1.validate_tenant`](#visiertenantmanagementtenant_management_v1validate_tenant)
  * [`visiertenantmanagement.tenant_management_v1.validate_tenants`](#visiertenantmanagementtenant_management_v1validate_tenants)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Visier&serviceName=TenantManagement&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from visier_tenant_management_python_sdk import VisierTenantManagement, ApiException

visiertenantmanagement = VisierTenantManagement(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Add an analytic tenant
    create_tenant_response = visiertenantmanagement.tenant_management.create_tenant(
        tenant_code="string_example",
        tenant_display_name="string_example",
        tenant_short_name="string_example",
        vanity_url_name="string_example",
        industry_code=1,
        primary_business_location={
    },
        purchased_modules=[
        "string_example"
    ],
        embeddable_domains=[
        "string_example"
    ],
        custom_properties=[
        {
        }
    ],
        sso_instance_issuers=[
        "string_example"
    ],
        home_analysis_id="string_example",
        home_analysis_by_user_group=[
        {
        }
    ],
        update_action="MERGE",
        enabled=True,
        click_through_link="string_example",
    )
    print(create_tenant_response)
except ApiException as e:
    print("Exception when calling TenantManagementApi.create_tenant: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from visier_tenant_management_python_sdk import VisierTenantManagement, ApiException

visiertenantmanagement = VisierTenantManagement(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

async def main():
    try:
        # Add an analytic tenant
        create_tenant_response = await visiertenantmanagement.tenant_management.acreate_tenant(
            tenant_code="string_example",
            tenant_display_name="string_example",
            tenant_short_name="string_example",
            vanity_url_name="string_example",
            industry_code=1,
            primary_business_location={
    },
            purchased_modules=[
        "string_example"
    ],
            embeddable_domains=[
        "string_example"
    ],
            custom_properties=[
        {
        }
    ],
            sso_instance_issuers=[
        "string_example"
    ],
            home_analysis_id="string_example",
            home_analysis_by_user_group=[
        {
        }
    ],
            update_action="MERGE",
            enabled=True,
            click_through_link="string_example",
        )
        print(create_tenant_response)
    except ApiException as e:
        print("Exception when calling TenantManagementApi.create_tenant: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from visier_tenant_management_python_sdk import VisierTenantManagement, ApiException

visiertenantmanagement = VisierTenantManagement(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Add an analytic tenant
    create_tenant_response = visiertenantmanagement.tenant_management.raw.create_tenant(
        tenant_code="string_example",
        tenant_display_name="string_example",
        tenant_short_name="string_example",
        vanity_url_name="string_example",
        industry_code=1,
        primary_business_location={
    },
        purchased_modules=[
        "string_example"
    ],
        embeddable_domains=[
        "string_example"
    ],
        custom_properties=[
        {
        }
    ],
        sso_instance_issuers=[
        "string_example"
    ],
        home_analysis_id="string_example",
        home_analysis_by_user_group=[
        {
        }
    ],
        update_action="MERGE",
        enabled=True,
        click_through_link="string_example",
    )
    pprint(create_tenant_response.body)
    pprint(create_tenant_response.body["tenant_code"])
    pprint(create_tenant_response.body["tenant_display_name"])
    pprint(create_tenant_response.body["industry_code"])
    pprint(create_tenant_response.body["primary_business_location"])
    pprint(create_tenant_response.body["purchased_modules"])
    pprint(create_tenant_response.body["embeddable_domains"])
    pprint(create_tenant_response.body["custom_properties"])
    pprint(create_tenant_response.body["sso_instance_issuers"])
    pprint(create_tenant_response.body["home_analysis_id"])
    pprint(create_tenant_response.body["home_analysis_by_user_group"])
    pprint(create_tenant_response.body["status"])
    pprint(create_tenant_response.body["click_through_link"])
    pprint(create_tenant_response.body["vanity_url_name"])
    pprint(create_tenant_response.headers)
    pprint(create_tenant_response.status)
    pprint(create_tenant_response.round_trip_time)
except ApiException as e:
    print("Exception when calling TenantManagementApi.create_tenant: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `visiertenantmanagement.tenant_management.create_tenant`<a id="visiertenantmanagementtenant_managementcreate_tenant"></a>

Prior to processing and loading an analytic tenant's data files, you must provision, or create, that tenant. A
 provisioned analytic tenant is automatically enabled. If the tenant's data is loaded after provisioning, that data
 is immediately accessible by their users.

 This API allows you to create an analytic tenant and identify the
 applications assigned to the tenant. Visier organizes content under a set of modules.

 Contact Visier Support to determine the list of modules allocated to you.

 **Note:** API requests that contain **homeAnalysisId**, **homeAnalysisByUserGroup**, or **clickThroughLink** take
 longer to run because they require publishing a project to production.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_tenant_response = visiertenantmanagement.tenant_management.create_tenant(
    tenant_code="string_example",
    tenant_display_name="string_example",
    tenant_short_name="string_example",
    vanity_url_name="string_example",
    industry_code=1,
    primary_business_location={
    },
    purchased_modules=[
        "string_example"
    ],
    embeddable_domains=[
        "string_example"
    ],
    custom_properties=[
        {
        }
    ],
    sso_instance_issuers=[
        "string_example"
    ],
    home_analysis_id="string_example",
    home_analysis_by_user_group=[
        {
        }
    ],
    update_action="MERGE",
    enabled=True,
    click_through_link="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_code: `str`<a id="tenant_code-str"></a>

A unique identifier for the newly created analytic tenant. Required if creating new tenants.

##### tenant_display_name: `str`<a id="tenant_display_name-str"></a>

A new display name to assign to the analytic tenant. Required if creating new tenants.

##### tenant_short_name: `str`<a id="tenant_short_name-str"></a>

A new short name to assign to the tenant. Required for Enterprise tenants

##### vanity_url_name: `str`<a id="vanity_url_name-str"></a>

A new vanity name to assign to the tenant. Required for Enterprise tenants

##### industry_code: `int`<a id="industry_code-int"></a>

The 6-digit NAICS code for the industry to which the analytic tenant belongs. If the code is unknown, type 000000.  For 2-digit codes, add trailing zeros at the end to reach 6 digits, such as 620000. Required if creating new tenants.

##### primary_business_location: [`BusinessLocationDTO`](./visier_tenant_management_python_sdk/type/business_location_dto.py)<a id="primary_business_location-businesslocationdtovisier_tenant_management_python_sdktypebusiness_location_dtopy"></a>


The primary location of operations or where business is performed. This field is optional.

##### purchased_modules: [`TenantManagementAPIUpdateRequestDTOPurchasedModules`](./visier_tenant_management_python_sdk/type/tenant_management_api_update_request_dto_purchased_modules.py)<a id="purchased_modules-tenantmanagementapiupdaterequestdtopurchasedmodulesvisier_tenant_management_python_sdktypetenant_management_api_update_request_dto_purchased_modulespy"></a>

##### embeddable_domains: [`TenantManagementAPIUpdateRequestDTOEmbeddableDomains`](./visier_tenant_management_python_sdk/type/tenant_management_api_update_request_dto_embeddable_domains.py)<a id="embeddable_domains-tenantmanagementapiupdaterequestdtoembeddabledomainsvisier_tenant_management_python_sdktypetenant_management_api_update_request_dto_embeddable_domainspy"></a>

##### custom_properties: List[`CustomPropertyDTO`]<a id="custom_properties-listcustompropertydto"></a>

A list of objects that represent different customizable properties for the analytic tenant. This is optional.

##### sso_instance_issuers: [`TenantManagementAPIUpdateRequestDTOSsoInstanceIssuers`](./visier_tenant_management_python_sdk/type/tenant_management_api_update_request_dto_sso_instance_issuers.py)<a id="sso_instance_issuers-tenantmanagementapiupdaterequestdtossoinstanceissuersvisier_tenant_management_python_sdktypetenant_management_api_update_request_dto_sso_instance_issuerspy"></a>

##### home_analysis_id: `str`<a id="home_analysis_id-str"></a>

The unique ID of the analysis to display for this tenant when a user logs in. This is optional. Causes the API request to take longer because it must publish a project to production.   Retrieve the ID by opening an analysis in the production version of a tenant and copying the string after the last forward slash (/) in the URL. For example: https://jupiter.visier.com/hr/prod/appcontainer?previewId=-eZPm8xvo3SUMpD4Q5pdE-6mCj9CQ9K699XgqRGwtOxagH5x2IzDFawlWn3hYqFEfU7nP0YK9ASEzmrNfAihGg..&previewType=Production#/analytics/myanalyses/8a4c1d4f-eb61-4da0-9e5b-55bef757c30e   The `homeAnalysisID` is 8a4c1d4f-eb61-4da0-9e5b-55bef757c30e. Alternatively, retrieve the ID by copying the `contentId` found by following the `Embed a visualization` documentation.

##### home_analysis_by_user_group: List[`HomeAnalysisByUserGroupDTO`]<a id="home_analysis_by_user_group-listhomeanalysisbyusergroupdto"></a>

A list of objects representing the analysis to display to specific user groups when users log in. This is optional. Causes the API request to take longer because it must publish a project to production.

##### update_action: `str`<a id="update_action-str"></a>

Specifies the way you want to update values. Default is MERGE.  Valid values:  - `MERGE`: Combine the existing values with the new values.  - `REPLACE`: Remove existing values and let the new values take their place.

##### enabled: `bool`<a id="enabled-bool"></a>

If true, the tenant is enabled. Enabled tenants have access to Visier visualizations.

##### click_through_link: `str`<a id="click_through_link-str"></a>

A custom URL to redirect users into your portal to see the relevant content. This URL is used for links that are shared by and with your users through the sharing capability or email content. This is optional. Causes the API request to take longer because it must publish a project to production.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TenantManagementAPIUpdateRequestDTO`](./visier_tenant_management_python_sdk/type/tenant_management_api_update_request_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TenantManagementAPIUpdateResponseDTO`](./visier_tenant_management_python_sdk/pydantic/tenant_management_api_update_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/admin/tenants` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visiertenantmanagement.tenant_management.list_tenants`<a id="visiertenantmanagementtenant_managementlist_tenants"></a>

Use this API to retrieve the full list of analytic tenants managed by you with their current states and the content
 modules assigned to them, and all other relevant details for the tenants if requested.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_tenants_response = visiertenantmanagement.tenant_management.list_tenants(
    mask="tenantDisplayName,purchasedModules",
    limit=1,
    start=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### mask: `str`<a id="mask-str"></a>

A comma separated list of strings that specifies which fields to include in the response.

##### limit: `int`<a id="limit-int"></a>

The maximum number of tenants to return. Default is 400.

##### start: `int`<a id="start-int"></a>

The starting index of the first tenant to return. Default is 0.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MaskMessage`](./visier_tenant_management_python_sdk/type/mask_message.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TenantManagementAPIListResponseDTO`](./visier_tenant_management_python_sdk/pydantic/tenant_management_api_list_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/admin/tenants` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visiertenantmanagement.tenant_management.tenant_info`<a id="visiertenantmanagementtenant_managementtenant_info"></a>

Use this API to retrieve the details for a specified analytic tenant. Doing so allows you to see the current state
 of the tenant, the content modules assigned to it, and all other relevant details for the tenant.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
tenant_info_response = visiertenantmanagement.tenant_management.tenant_info(
    tenant_id="tenantId_example",
    mask="tenantDisplayName,purchasedModules",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_id: `str`<a id="tenant_id-str"></a>

The ID of the tenant to retrieve.

##### mask: `str`<a id="mask-str"></a>

A comma separated list of strings that specifies which fields to include in the response.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MaskMessage`](./visier_tenant_management_python_sdk/type/mask_message.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TenantManagementAPIGetResponseDTO`](./visier_tenant_management_python_sdk/pydantic/tenant_management_api_get_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/admin/tenants/{tenantId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visiertenantmanagement.tenant_management.update_tenant`<a id="visiertenantmanagementtenant_managementupdate_tenant"></a>

You may need to update analytic tenants as they grow and as your organization upgrades the content available to them.
 You may also encounter a scenario where an analytic tenant transitions across different industries. To make updates
 to your tenants, use this API.

 * To ensure that the analytic tenant receives accurate benchmarks and predictive functionality, update their industry code in the Visier system.
 * To programmatically assign the Home analysis that analytic tenants see at login, use this API to set the default Home analysis for a tenant and specific user groups of that tenant.

 You can use this API to update any field on an analytic tenant, except tenantCode.

 **Note:** API requests that contain **homeAnalysisId**, **homeAnalysisByUserGroup**, or **clickThroughLink** take
 longer to run because they require publishing a project to production.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_tenant_response = visiertenantmanagement.tenant_management.update_tenant(
    tenant_code="string_example",
    tenant_display_name="string_example",
    tenant_short_name="string_example",
    vanity_url_name="string_example",
    industry_code=1,
    primary_business_location={
    },
    purchased_modules=[
        "string_example"
    ],
    embeddable_domains=[
        "string_example"
    ],
    custom_properties=[
        {
        }
    ],
    sso_instance_issuers=[
        "string_example"
    ],
    home_analysis_id="string_example",
    home_analysis_by_user_group=[
        {
        }
    ],
    update_action="MERGE",
    enabled=True,
    click_through_link="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_code: `str`<a id="tenant_code-str"></a>

A unique identifier for the newly created analytic tenant. Required if creating new tenants.

##### tenant_display_name: `str`<a id="tenant_display_name-str"></a>

A new display name to assign to the analytic tenant. Required if creating new tenants.

##### tenant_short_name: `str`<a id="tenant_short_name-str"></a>

A new short name to assign to the tenant. Required for Enterprise tenants

##### vanity_url_name: `str`<a id="vanity_url_name-str"></a>

A new vanity name to assign to the tenant. Required for Enterprise tenants

##### industry_code: `int`<a id="industry_code-int"></a>

The 6-digit NAICS code for the industry to which the analytic tenant belongs. If the code is unknown, type 000000.  For 2-digit codes, add trailing zeros at the end to reach 6 digits, such as 620000. Required if creating new tenants.

##### primary_business_location: [`BusinessLocationDTO`](./visier_tenant_management_python_sdk/type/business_location_dto.py)<a id="primary_business_location-businesslocationdtovisier_tenant_management_python_sdktypebusiness_location_dtopy"></a>


The primary location of operations or where business is performed. This field is optional.

##### purchased_modules: [`TenantManagementAPIUpdateRequestDTOPurchasedModules`](./visier_tenant_management_python_sdk/type/tenant_management_api_update_request_dto_purchased_modules.py)<a id="purchased_modules-tenantmanagementapiupdaterequestdtopurchasedmodulesvisier_tenant_management_python_sdktypetenant_management_api_update_request_dto_purchased_modulespy"></a>

##### embeddable_domains: [`TenantManagementAPIUpdateRequestDTOEmbeddableDomains`](./visier_tenant_management_python_sdk/type/tenant_management_api_update_request_dto_embeddable_domains.py)<a id="embeddable_domains-tenantmanagementapiupdaterequestdtoembeddabledomainsvisier_tenant_management_python_sdktypetenant_management_api_update_request_dto_embeddable_domainspy"></a>

##### custom_properties: List[`CustomPropertyDTO`]<a id="custom_properties-listcustompropertydto"></a>

A list of objects that represent different customizable properties for the analytic tenant. This is optional.

##### sso_instance_issuers: [`TenantManagementAPIUpdateRequestDTOSsoInstanceIssuers`](./visier_tenant_management_python_sdk/type/tenant_management_api_update_request_dto_sso_instance_issuers.py)<a id="sso_instance_issuers-tenantmanagementapiupdaterequestdtossoinstanceissuersvisier_tenant_management_python_sdktypetenant_management_api_update_request_dto_sso_instance_issuerspy"></a>

##### home_analysis_id: `str`<a id="home_analysis_id-str"></a>

The unique ID of the analysis to display for this tenant when a user logs in. This is optional. Causes the API request to take longer because it must publish a project to production.   Retrieve the ID by opening an analysis in the production version of a tenant and copying the string after the last forward slash (/) in the URL. For example: https://jupiter.visier.com/hr/prod/appcontainer?previewId=-eZPm8xvo3SUMpD4Q5pdE-6mCj9CQ9K699XgqRGwtOxagH5x2IzDFawlWn3hYqFEfU7nP0YK9ASEzmrNfAihGg..&previewType=Production#/analytics/myanalyses/8a4c1d4f-eb61-4da0-9e5b-55bef757c30e   The `homeAnalysisID` is 8a4c1d4f-eb61-4da0-9e5b-55bef757c30e. Alternatively, retrieve the ID by copying the `contentId` found by following the `Embed a visualization` documentation.

##### home_analysis_by_user_group: List[`HomeAnalysisByUserGroupDTO`]<a id="home_analysis_by_user_group-listhomeanalysisbyusergroupdto"></a>

A list of objects representing the analysis to display to specific user groups when users log in. This is optional. Causes the API request to take longer because it must publish a project to production.

##### update_action: `str`<a id="update_action-str"></a>

Specifies the way you want to update values. Default is MERGE.  Valid values:  - `MERGE`: Combine the existing values with the new values.  - `REPLACE`: Remove existing values and let the new values take their place.

##### enabled: `bool`<a id="enabled-bool"></a>

If true, the tenant is enabled. Enabled tenants have access to Visier visualizations.

##### click_through_link: `str`<a id="click_through_link-str"></a>

A custom URL to redirect users into your portal to see the relevant content. This URL is used for links that are shared by and with your users through the sharing capability or email content. This is optional. Causes the API request to take longer because it must publish a project to production.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TenantManagementAPIUpdateRequestDTO`](./visier_tenant_management_python_sdk/type/tenant_management_api_update_request_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TenantManagementAPIUpdateResponseDTO`](./visier_tenant_management_python_sdk/pydantic/tenant_management_api_update_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/admin/tenants/:tenantId` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visiertenantmanagement.tenant_management_v1.add_tenant`<a id="visiertenantmanagementtenant_management_v1add_tenant"></a>

Prior to processing and loading an analytic tenant's data files, you must provision, or create, that tenant.
 A provisioned analytic tenant is automatically enabled. If the tenant's data is loaded after provisioning, that
 data is immediately accessible by their users.

 This API allows you to create an analytic tenant and identify the applications assigned to the tenant. Visier
 organizes content under a set of modules.

 Contact Visier Support to determine the list of modules allocated to you.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_tenant_response = visiertenantmanagement.tenant_management_v1.add_tenant(
    tenant_code="string_example",
    tenant_display_name="string_example",
    purchased_modules=[
        "string_example"
    ],
    industry_code=1,
    embeddable_domains=[
        "string_example"
    ],
    custom_properties=[
        {
        }
    ],
    sso_instance_issuers=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_code: `str`<a id="tenant_code-str"></a>

The unique identifier of the analytic tenant.

##### tenant_display_name: `str`<a id="tenant_display_name-str"></a>

The display name that is assigned to the analytic tenant.

##### purchased_modules: [`TenantProvisionAPIDTOPurchasedModules`](./visier_tenant_management_python_sdk/type/tenant_provision_apidto_purchased_modules.py)<a id="purchased_modules-tenantprovisionapidtopurchasedmodulesvisier_tenant_management_python_sdktypetenant_provision_apidto_purchased_modulespy"></a>

##### industry_code: `int`<a id="industry_code-int"></a>

The 6-digit NAICS code for the industry to which the analytic tenant belongs. If the code is unknown, type 000000.   For 2-digit codes, add trailing zeros at the end to reach 6 digits, such as 620000.

##### embeddable_domains: [`TenantProvisionAPIDTOEmbeddableDomains`](./visier_tenant_management_python_sdk/type/tenant_provision_apidto_embeddable_domains.py)<a id="embeddable_domains-tenantprovisionapidtoembeddabledomainsvisier_tenant_management_python_sdktypetenant_provision_apidto_embeddable_domainspy"></a>

##### custom_properties: List[`CustomTenantPropertyDTO`]<a id="custom_properties-listcustomtenantpropertydto"></a>

A set of key-value pairs that represent different customizable properties for the analytic tenant.

##### sso_instance_issuers: [`TenantProvisionAPIDTOSsoInstanceIssuers`](./visier_tenant_management_python_sdk/type/tenant_provision_apidto_sso_instance_issuers.py)<a id="sso_instance_issuers-tenantprovisionapidtossoinstanceissuersvisier_tenant_management_python_sdktypetenant_provision_apidto_sso_instance_issuerspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TenantProvisionAPIDTO`](./visier_tenant_management_python_sdk/type/tenant_provision_apidto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TenantProvisionAPIDTO`](./visier_tenant_management_python_sdk/pydantic/tenant_provision_apidto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/tenants` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visiertenantmanagement.tenant_management_v1.delete_tenant`<a id="visiertenantmanagementtenant_management_v1delete_tenant"></a>

Warning! Deprovisioning an analytic tenant is not reversible.
 Before deprovisioning, you must disable an analytic tenant. For more information, see **`/v1/admin/tenants/:tenantId/disable`**.

 This API removes an analytic tenant permanently from the Visier system. If you are unsure whether an analytic tenant
 may be re-enabled on any of the Visier modules at any time, you may instead want to disable the analytic tenant.

 If successful, the response returns the status "Deprovisioned". This indicates that the tenant is scheduled for
 deprovisioning, which may take several days to complete.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_tenant_response = visiertenantmanagement.tenant_management_v1.delete_tenant(
    tenant_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_id: `str`<a id="tenant_id-str"></a>

The ID of the tenant. For example, WFF_{XXX}~{YYY} where {XXX} is the administrating tenant code and {YYY}  is the analytic tenant code.

#### 🔄 Return<a id="🔄-return"></a>

[`TenantStatusAPIDTO`](./visier_tenant_management_python_sdk/pydantic/tenant_status_apidto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/tenants/:tenantId` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visiertenantmanagement.tenant_management_v1.disable_tenant`<a id="visiertenantmanagementtenant_management_v1disable_tenant"></a>

Use this API to disable an analytic tenant and remove access to Visier visualizations for the tenant's users.

 You must disable an analytic tenant before deprovisioning, or removing, it from the system.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
disable_tenant_response = visiertenantmanagement.tenant_management_v1.disable_tenant(
    tenant_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_id: `str`<a id="tenant_id-str"></a>

The ID of the tenant. For example, WFF_{XXX}~{YYY} where {XXX} is the administrating tenant code and {YYY}  is the analytic tenant code.

#### 🔄 Return<a id="🔄-return"></a>

[`TenantStatusAPIDTO`](./visier_tenant_management_python_sdk/pydantic/tenant_status_apidto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/tenants/:tenantId/disable` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visiertenantmanagement.tenant_management_v1.enable_tenant`<a id="visiertenantmanagementtenant_management_v1enable_tenant"></a>

An analytic tenant is enabled when you provision or create the tenant.

 Use this API to enable a tenant that you have specifically disabled; for example, if you previously did not
 want that tenant to have access to Visier visualizations, but now do.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
enable_tenant_response = visiertenantmanagement.tenant_management_v1.enable_tenant(
    tenant_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_id: `str`<a id="tenant_id-str"></a>

The ID of the tenant. For example, WFF_{XXX}~{YYY} where {XXX} is the administrating tenant code and {YYY}  is the analytic tenant code.

#### 🔄 Return<a id="🔄-return"></a>

[`TenantStatusAPIDTO`](./visier_tenant_management_python_sdk/pydantic/tenant_status_apidto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/tenants/:tenantId/enable` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visiertenantmanagement.tenant_management_v1.get_tenant`<a id="visiertenantmanagementtenant_management_v1get_tenant"></a>

Use this API to retrieve all details for a specified analytic tenant. Doing so allows you to see the current state
 of the tenant, the content modules assigned to it, and all other relevant details for the tenant.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tenant_response = visiertenantmanagement.tenant_management_v1.get_tenant(
    tenant_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_id: `str`<a id="tenant_id-str"></a>

The ID of the tenant. For example, WFF_{XXX}~{YYY} where {XXX} is the administrating tenant code and {YYY}  is the analytic tenant code.

#### 🔄 Return<a id="🔄-return"></a>

[`TenantDetailAPIDTO`](./visier_tenant_management_python_sdk/pydantic/tenant_detail_apidto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/tenants/:tenantId` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visiertenantmanagement.tenant_management_v1.get_tenants`<a id="visiertenantmanagementtenant_management_v1get_tenants"></a>

Use this API to retrieve the full list of analytic tenants managed by you with their current states and the
 content modules assigned to them, and all other relevant details for the tenants if requested.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tenants_response = visiertenantmanagement.tenant_management_v1.get_tenants(
    limit=1,
    start=1,
    details=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

The limit of analytic tenant details to retrieve.

##### start: `int`<a id="start-int"></a>

The index to start retrieving results from, also known as offset. The index begins at 0.

##### details: `bool`<a id="details-bool"></a>

If true, the response returns information about the data version and modules.

#### 🔄 Return<a id="🔄-return"></a>

[`AllTenantsStatusAPIDTO`](./visier_tenant_management_python_sdk/pydantic/all_tenants_status_apidto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/tenants` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visiertenantmanagement.tenant_management_v1.update_tenant`<a id="visiertenantmanagementtenant_management_v1update_tenant"></a>

You may need to update analytic tenants as they grow and as your organization upgrades the content available to
 them. You may also encounter a scenario where an analytic tenant transitions across different industries.

 To ensure that the analytic tenant receives accurate benchmarks and predictive functionality, update their
 industry code in the Visier system.

 You can use this API to update any field on an analytic tenant, except tenantCode.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_tenant_response = visiertenantmanagement.tenant_management_v1.update_tenant(
    tenant_display_name="string_example",
    industry_code=1,
    purchased_modules=[
        "string_example"
    ],
    embeddable_domains=[
        "string_example"
    ],
    custom_properties={
        "key": "string_example",
    },
    sso_instance_issuers=[
        "string_example"
    ],
    tenant_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_display_name: `str`<a id="tenant_display_name-str"></a>

A display name that is assigned to the new analytic tenant.

##### industry_code: `int`<a id="industry_code-int"></a>

The 6-digit NAICS code for the industry to which the analytic tenant belongs. If the code is unknown, type 000000.   For 2-digit codes, add trailing zeros at the end to reach 6 digits, such as 620000.

##### purchased_modules: [`UpdateTenantModelPurchasedModules`](./visier_tenant_management_python_sdk/type/update_tenant_model_purchased_modules.py)<a id="purchased_modules-updatetenantmodelpurchasedmodulesvisier_tenant_management_python_sdktypeupdate_tenant_model_purchased_modulespy"></a>

##### embeddable_domains: [`UpdateTenantModelEmbeddableDomains`](./visier_tenant_management_python_sdk/type/update_tenant_model_embeddable_domains.py)<a id="embeddable_domains-updatetenantmodelembeddabledomainsvisier_tenant_management_python_sdktypeupdate_tenant_model_embeddable_domainspy"></a>

##### custom_properties: [`UpdateTenantModelCustomProperties`](./visier_tenant_management_python_sdk/type/update_tenant_model_custom_properties.py)<a id="custom_properties-updatetenantmodelcustompropertiesvisier_tenant_management_python_sdktypeupdate_tenant_model_custom_propertiespy"></a>

##### sso_instance_issuers: [`UpdateTenantModelSsoInstanceIssuers`](./visier_tenant_management_python_sdk/type/update_tenant_model_sso_instance_issuers.py)<a id="sso_instance_issuers-updatetenantmodelssoinstanceissuersvisier_tenant_management_python_sdktypeupdate_tenant_model_sso_instance_issuerspy"></a>

##### tenant_id: `str`<a id="tenant_id-str"></a>

The ID of the tenant to update.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateTenantModel`](./visier_tenant_management_python_sdk/type/update_tenant_model.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TenantProvisionAPIDTO`](./visier_tenant_management_python_sdk/pydantic/tenant_provision_apidto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/tenants/:tenantId` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visiertenantmanagement.tenant_management_v1.validate_tenant`<a id="visiertenantmanagementtenant_management_v1validate_tenant"></a>

Use this API to retrieve the metric values for an individual analytic tenant. The metric values included in the
 response are the tenant's configured summary metrics. Administrators can configure summary metrics in a project:
 - Sign in to Visier as an administrator.
 - In a project, on the navigation bar, click the Home button.
 - Click Dashboard, and then click Edit Summary Metrics.
 - Select the metrics that you want to validate, and then close the Summary Metrics dialog.
 - Publish the project to production.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validate_tenant_response = visiertenantmanagement.tenant_management_v1.validate_tenant(
    tenant_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_id: `str`<a id="tenant_id-str"></a>

The ID of the tenant. For example, WFF_{XXX}~{YYY} where {XXX} is the administrating tenant code and {YYY}  is the analytic tenant code.

#### 🔄 Return<a id="🔄-return"></a>

[`TenantPreviewEntriesSummaryDTO`](./visier_tenant_management_python_sdk/pydantic/tenant_preview_entries_summary_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/validation/tenants/:tenantId` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visiertenantmanagement.tenant_management_v1.validate_tenants`<a id="visiertenantmanagementtenant_management_v1validate_tenants"></a>

As you onboard more analytic tenants, you can validate the data visible to your users to ensure it matches the
 source systems from which it was exported and that it matches what your expectations are for this data.

 The metric values included in the response are the tenant's configured summary metrics. Administrators can
 configure summary metrics in a project:
 - Sign in to Visier as an administrator.
 - In a project, on the navigation bar, click the Home button.
 - Click Dashboard, and then click Edit Summary Metrics.
 - Select the metrics that you want to validate, and then close the Summary Metrics dialog.
 - Publish the project to production.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validate_tenants_response = visiertenantmanagement.tenant_management_v1.validate_tenants(
    limit=1,
    start=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

The limit of analytic tenant details to retrieve.

##### start: `int`<a id="start-int"></a>

The index to start retrieving results from, also known as offset. The index begins at 0.

#### 🔄 Return<a id="🔄-return"></a>

[`TenantPreviewEntriesSummaryListDTO`](./visier_tenant_management_python_sdk/pydantic/tenant_preview_entries_summary_list_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/validation/tenants` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
