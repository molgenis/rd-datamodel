# Model Schema

## Packages

| Name | Description |
|:---- |:-----------|
| users | List of approved users (v1.0.0, 2021-10-21) |

## Entities

| Name | Description | Package |
|:---- |:-----------|:-------|
| users | Metadata about the user including access levels | users |
| packages | All packages and entities associated with the current project | users |
| roles | All roles by package | users |
| statuses | available account status options and descriptions | users |

## Attributes

### Entity: users_users

Metadata about the user including access levels

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| email | Email | email address that was used to activate the user account | email | True |
| firstname | First Name | - | string | False |
| lastname | Last Name | - | string | False |
| affiliation | Affiliation | Organization that the user is associated with | string | False |
| function | Function | Describe the function that user has in relation to the database | string | False |
| accountStatus | Account Status | If True, the account is active | xref | False |
| accountStartDate | Date Account Activated | Enter the date the account was activated | date | False |
| accountEndDate | Date Account Deactived | Enter the date the account deactivated | date | False |
| hasSubmittedDocuments | Submitted Documents | An indication if the user has submitted the required documents in order to gain access to the database | bool | False |
| hasAuthorization | Authorization | User has submitted all required documentation and authorization has been granted | bool | False |
| roles | Roles | Select the roles that the user has been assigned | mref | False |
| packages | Packages | Select the packages that the user has access to | mref | False |

### Entity: users_packages

All packages and entities associated with the current project

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| id | - | - | string | True |
| label | - | - | string | False |
| description | - | - | string | False |

### Entity: users_roles

All roles by package

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| id | - | - | string | True |
| label | - | - | string | False |
| description | - | - | string | False |

### Entity: users_statuses

available account status options and descriptions

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| id | - | - | string | True |
| label | - | - | string | False |
| description | - | - | string | False |
