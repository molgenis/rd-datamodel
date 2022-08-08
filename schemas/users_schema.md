# Model Schema

## Packages

| Name | Description | Parent |
|:---- |:-----------|:------|
| users | List of approved users (v1.2.0, 2022-08-08) | - |

## Entities

| Name | Description | Package |
|:---- |:-----------|:-------|
| users | An individual who uses a computer, program, network, or related service for work or entertainment. | users |
| template | - | users |
| packages | All packages and entities associated with the current project | users |
| userPrivileges | All roles by package | users |
| userGroups | A set of people who have similar interests, goals, or concerns. | users |

## Attributes

### Entity: users_users

An individual who uses a computer, program, network, or related service for work or entertainment.

| Name | Label | Description | Data Type |
|:---- |:-----|:-----------|:---------|
| email&#8251; | Email | A valid email address of an end-user. | email |
| username | User Name | A person's identification on an individual computer system. | string |
| firstname | First Name | A word or group of words indicating a person's first (personal or given) name; the name that precedes the surname. | string |
| lastname | Last Name | A word or group of words indicating a person's last (family) name. | string |
| affiliation | Organizational Affiliation Name | The name of the organization or entity that the person or group has an established relationship with. | string |
| function | Function | Describe the function that user has in relation to the database | string |
| userAccountIsActive | User Account is Active | Specifies whether the entity is active | enum |
| accountStartDate | Account Start Date | The calendar date on which something is to start or did start. | date |
| accountEndDate | Account End Date | The calendar date on which something is to terminate or did terminate. | date |
| hasAuthorization | Has Authorization | Decision of the competent authorities in form of a letter, document, or verbal or electronic form, that confirms that somebody has permission to do something or be somewhere, e.g. to realize a given project. | enum |
| belongsToUserGroup | Belongs To User Group | A set of people who have similar interests, goals, or concerns. | categorical |
| userPrivilege | User Privilege | The operations and access levels which are allowed to a user (e.g Create, Read, Update, Delete). | mref |
| packages | Packages | Select the packages that the user has access to | mref |

### Entity: users_template

| Name | Label | Description | Data Type |
|:---- |:-----|:-----------|:---------|
| id&#8251; | - | One or more characters used to identify, name, or characterize the nature, properties, or contents of a thing. | string |
| label | - | A brief description given for purposes of identification; an identifying or descriptive marker that is attached to an object. | string |
| description | - | A written or verbal account, representation, statement, or explanation of something. | string |

Note: The symbol &#8251; denotes attributes that are primary keys

