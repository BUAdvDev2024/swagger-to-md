# EmployeeManagementService.Presentation API Document - Version: 1.0
###### OpenAPI Documentation Markdown Document
Open API Version: 3.0.1
Number of Paths: 7
## API Endpoints
* [Disciplinary](#disciplinary)
	* [get-employees-disciplinaries](#/disciplinary/get-employees-disciplinaries)
	* [create-disciplinary](#/disciplinary/create-disciplinary)
* [Profile](#profile)
	* [register](#/profile/register)
	* [terminated-employee](#/profile/terminated-employee)
	* [all](#/profile/all)
* [Role](#role)
	* [create-role](#/role/create-role)
	* [get-roles](#/role/get-roles)
## <a name="disciplinary"></a> Disciplinary
## <a name="/disciplinary/get-employees-disciplinaries"></a>/disciplinary/get-employees-disciplinaries `GET` 
### Parameters
| Name | Schema |
|------|--------|
| employeeId | `integer` `int32` |
### Responses
| Response | Description |
|----------|-------------|
| 200 | Success

## <a name="/disciplinary/create-disciplinary"></a>/disciplinary/create-disciplinary `POST` 
### Content
| Content Type | Schema |
|--------------|--------|
| application/json | CreateDisciplinaryPayload |
| text/json | CreateDisciplinaryPayload |
| application/*+json | CreateDisciplinaryPayload |
### Responses
| Response | Description |
|----------|-------------|
| 200 | Success

## <a name="profile"></a> Profile
## <a name="/profile/register"></a>/profile/register `POST` 
### Content
| Content Type | Schema |
|--------------|--------|
| application/json | EmployeeRegistrationPayload |
| text/json | EmployeeRegistrationPayload |
| application/*+json | EmployeeRegistrationPayload |
### Responses
| Response | Description |
|----------|-------------|
| 200 | Success

## <a name="/profile/terminated-employee"></a>/profile/terminated-employee `POST` 
### Parameters
| Name | Schema |
|------|--------|
| EmployeeId | `integer` `int32` |
### Responses
| Response | Description |
|----------|-------------|
| 200 | Success

## <a name="/profile/all"></a>/profile/all `GET` 
### Parameters
No parameters
### Responses
| Response | Description |
|----------|-------------|
| 200 | Success

## <a name="role"></a> Role
## <a name="/role/create-role"></a>/role/create-role `POST` 
### Content
| Content Type | Schema |
|--------------|--------|
| application/json | CreateRolePayload |
| text/json | CreateRolePayload |
| application/*+json | CreateRolePayload |
### Responses
| Response | Description |
|----------|-------------|
| 200 | Success

## <a name="/role/get-roles"></a>/role/get-roles `GET` 
### Parameters
No parameters
### Responses
| Response | Description |
|----------|-------------|
| 200 | Success

## Schemas
## CreateDisciplinaryPayload `object`
### Properties
| Property Name | Type | Format | Nullable |
|---------------|------|--------|----------|
| employeeId | integer | int32 | false |
| dateOfOffense | string | date-time | True |
| offenseType | string | N/a | True |
| disciplinaryActionTaken | boolean | N/a | false |
## CreateRolePayload `object`
### Properties
| Property Name | Type | Format | Nullable |
|---------------|------|--------|----------|
| title | string | N/a | True |
| description | string | N/a | True |
| hourlyRate | number | double | false |
## EmployeeRegistrationPayload `object`
### Properties
| Property Name | Type | Format | Nullable |
|---------------|------|--------|----------|
| firstName | string | N/a | false |
| lastName | string | N/a | false |
| phoneNumber | string | tel | false |
| emailAddress | string | email | false |
| addressLine1 | string | N/a | True |
| addressLine2 | string | N/a | True |
| addressLine3 | string | N/a | True |
| addressLine4 | string | N/a | True |
| postCode | string | N/a | True |
| roleId | integer | int32 | false |
| restaurantId | string | N/a | True |
