# Bank accounts

- [Add bank account](#add-bank-account)
- [Update bank account](#update-bank-account)
- [Delete bank account](#delete-bank-account)
- [Get list of bank accounts](#get-list-of-bank-accounts)

## Add bank account

Add new bank account.

### Request

**URL**: `/bank_accounts/add`  
**HTTP method**: POST  

```sh
data='{
    "bank_name": "NovaBanka",
    "iban": "SK000011112222333344",
    "swift": "suzuki",
    "default": 1,
    "show": 1,
    "show_account": 1
}';

curl -X POST \
     -d "data=$data" \
     -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
     https://moja.superfaktura.sk/bank_accounts/add
```

### Attributes
#### Required
none

At least one of: `bank_name`, `iban`, `swift`, `bank_account`, `bank_code` is required.

#### Optional

| name              | type   | description | default value |
| ----------------- | ------ | ----------- | ------------- |
| **bank_account**  | string | bank account number (CZ) | |
| **bank_code**     | string | bank code (CZ) | |
| **bank_name**     | string | bank name | |
| **default**       | int    | is bank account default? Will overwrite previous default account if set to 1. (0=no, 1=yes)) | null (will not be set) |
| **iban**          | string | IBAN code | |
| **show**          | int    | show bank account on documents | null (will not be set) |
| **swift**         | string | SWIFT code | |

### Response

#### Successful creation
```json
{
  "BankAccount": {
    "bank_name": "NovaBanka",
    "country_id": "191",
    "created": "2050-01-01 23:59:59",
    "default": 1,
    "iban": "SK000011112222333344",
    "id": "2",
    "modified": "2050-01-01 23:59:59",
    "show": 1,
    "show_account": 1,
    "swift": "suzuki",
    "user_id": "1",
    "user_profile_id": "1"
  },
  "error": 0
}
```

#### Insufficient privileges

```json
{
   "error" : 1,
   "error_message" : "Nemáte právo pridávať účet",
   "message" : "Nemáte právo pridávať účet"
}
```

#### Missing data

```json
{
   "error" : 1,
   "error_message" : "Chýbajúce údaje",
   "message" : "Chýbajúce údaje"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Update bank account

Update bank account specified by ID.

### Request

**URL**: `/bank_accounts/update/{ID}`  
**HTTP method**: POST  

```sh
data='{
    "bank_name":"StaroNovaBanka",
    "swift":"77777"
}';

curl -X POST \
     -d "data=$data" \
     -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
     https://moja.superfaktura.sk/bank_accounts/update/1
```

### Attributes
#### Required
URL parameters:  

| name   | type   | description     | default value |
| ------ | ------ | --------------- | ------------- |
| **id** | int    | bank account ID |               |

#### Optional
none

### Response

#### Successful update
```json
{
  "error": "0",
  "message": "{\"BankAccount\":{\"account\":\"\",\"bank_code\":\"\",\"bank_name\":\"StaroNovaBanka\",\"default\":true,\"iban\":\"SK012345678901234567890000\",\"show\":true,\"swift\":\"77777\",\"id\":\"1\",\"user_id\":\"1\",\"user_profile_id\":\"1\",\"modified\":\"2050-01-01 23:59:59\"}}"
}
```

#### Insufficient privileges

```json
{
  "error": 1,
  "error_message": "Nemáte právo meniť účet",
  "message": "Nemáte právo meniť účet"
}
```

#### Missing data

```json
{
  "error": 1,
  "error_message": "Chýbajúce údaje",
  "message": "Chýbajúce údaje"
}
```

#### Wrong bank account

```json
{
  "error": 1,
  "error_message": "Účet neexistuje",
  "message": "Účet neexistuje"
}
```




- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Delete bank account

Delete bank account specified by ID.

### Request

**URL**: `/bank_accounts/delete/{ID}`  
**HTTP method**: POST  

```sh
curl -X POST \
     -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
     https://moja.superfaktura.sk/bank_accounts/delete/1
```

### Attributes

#### Required

URL parameters:  

| name   | type   | description | default value |
| ------ | ------ | ----------- | ------------- |
| **id** | int    | bank account ID |           |

#### Optional
none

### Response

#### Successful deletion
```json
{
  "error": "0",
  "message": "{\"message\":\"Bankov\\u00fd \\u00fa\\u010det zmazan\\u00fd\"}"
}
```

#### Insufficient privileges

```json
{
  "error": 1,
  "error_message": "Nemáte právo zmazať účet",
  "message": "Nemáte právo zmazať účet"
}
```

#### Wrong bank account

```json
{
  "error": 1,
  "error_message": "Účet neexistuje",
  "message": "Účet neexistuje"
}
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Get list of bank accounts

Get list of bank accounts.

### Request

**URL**: `/bank_accounts/index`  
**HTTP method**: GET  

```sh
curl -X GET \
     -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
     https://moja.superfaktura.sk/bank_accounts/index
```

### Attributes

#### Required
none

#### Optional
none

### Response

#### Success
```json
{
  "BankAccounts": [
    {
      "BankAccount": {
        "account": "",
        "bank_code": "",
        "bank_name": "FatraBanka",
        "country_id": "191",
        "created": "2050-01-01 23:59:59",
        "currency": null,
        "default": true,
        "iban": "SK012345678901234567890000",
        "id": "1",
        "modified": "2050-01-01 23:59:59",
        "show": true,
        "swift": "SUZUKI",
        "user_id": "1",
        "user_profile_id": "1"
      }
    }
  ],
  "error": 0
}
```

#### No bank account found

```json
{
  "error": 1,
  "message": "Nenašiel sa žiaden bankový účet"
}
```