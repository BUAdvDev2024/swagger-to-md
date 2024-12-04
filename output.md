# Employee Management API
###### API Version: 1.0 - Open API Version: 3.0.1 - Paths: (7) - Schema (3)
## API Endpoints
* [Disciplinary](#disciplinary)
	* [get-employees-disciplinaries](#/disciplinary/get-employees-disciplinaries)
	* [create-disciplinary](#/disciplinary/create-disciplinary)
* [Profile](#profile)
	* [register-employee](#/profile/register-employee)
	* [terminated-employee](#/profile/terminated-employee)
	* [all](#/profile/all)
* [Role](#role)
	* [create-role](#/role/create-role)
	* [all](#/role/all)
## Schemas
* [Createdisciplinarypayload](#CreateDisciplinaryPayload)
* [Createrolepayload](#CreateRolePayload)
* [Employeeregistrationpayload](#EmployeeRegistrationPayload)
## <a name="disciplinary"></a> Disciplinary Endpoints
## <a name="/disciplinary/get-employees-disciplinaries"></a>/disciplinary/get-employees-disciplinaries `GET` 
#### Summary
Does some really cool stuff!
#### Parameters
| Name | Data Type |
|------|--------|
| employeeId | `integer` `int32` |
#### Responses
| Response | Description |
|----------|-------------|
| 200 | Success

## <a name="/disciplinary/create-disciplinary"></a>/disciplinary/create-disciplinary `POST` 
#### Request Body Content
| Content Type | Schema |
|--------------|--------|
| `application/json` `text/json` `application/*+json` | [CreateDisciplinaryPayload](#CreateDisciplinaryPayload)
#### Responses
| Response | Description |
|----------|-------------|
| 200 | Success

## <a name="profile"></a> Profile Endpoints
## <a name="/profile/register-employee"></a>/profile/register-employee `POST` 
#### Request Body Content
| Content Type | Schema |
|--------------|--------|
| `application/json` `text/json` `application/*+json` | [EmployeeRegistrationPayload](#EmployeeRegistrationPayload)
#### Responses
| Response | Description |
|----------|-------------|
| 200 | Success

## <a name="/profile/terminated-employee"></a>/profile/terminated-employee `POST` 
#### Parameters
| Name | Data Type |
|------|--------|
| EmployeeId | `integer` `int32` |
#### Responses
| Response | Description |
|----------|-------------|
| 200 | Success

## <a name="/profile/all"></a>/profile/all `GET` 
#### Parameters
| Name | Data Type |
|------|--------|
| restaurantId | `string` |
#### Responses
| Response | Description |
|----------|-------------|
| 200 | Success

## <a name="role"></a> Role Endpoints
## <a name="/role/create-role"></a>/role/create-role `POST` 
#### Request Body Content
| Content Type | Schema |
|--------------|--------|
| `application/json` `text/json` `application/*+json` | [CreateRolePayload](#CreateRolePayload)
#### Responses
| Response | Description |
|----------|-------------|
| 200 | Success

## <a name="/role/all"></a>/role/all `GET` 
#### Parameters
No parameters
#### Responses
| Response | Description |
|----------|-------------|
| 200 | Success

## Schemas
## <a name="CreateDisciplinaryPayload"></a>CreateDisciplinaryPayload `object`
### Properties
| Property Name | Type | Format | Nullable? |
|---------------|------|--------|----------|
| employeeId | integer | int32 | -- |
| dateOfOffense | string | date-time | nullable |
| offenseType | string | -- | nullable |
| disciplinaryActionTaken | boolean | -- | -- |
## <a name="CreateRolePayload"></a>CreateRolePayload `object`
### Properties
| Property Name | Type | Format | Nullable? |
|---------------|------|--------|----------|
| title | string | -- | nullable |
| description | string | -- | nullable |
| hourlyRate | number | double | -- |
## <a name="EmployeeRegistrationPayload"></a>EmployeeRegistrationPayload `object`
### Properties
| Property Name | Type | Format | Nullable? |
|---------------|------|--------|----------|
| firstName | string | -- | -- |
| lastName | string | -- | -- |
| phoneNumber | string | tel | -- |
| emailAddress | string | email | -- |
| addressLine1 | string | -- | nullable |
| addressLine2 | string | -- | nullable |
| addressLine3 | string | -- | nullable |
| addressLine4 | string | -- | nullable |
| postCode | string | -- | nullable |
| roleId | integer | int32 | -- |
| restaurantId | string | -- | nullable |

###### API doc created by swagger-to-md.py
