# Clients

- [Create client](#create-client)
- [View client detail](#view-client-detail)
- [Get client list](#get-client-list)

## Create client

Creates or edits client.

Decision whether clients exists or is new is explained in the following table:

| Property to match       | Status |
| ----------------------- | ------ |
| UUID                    | exists |
| ID (IČO)                | exists |
| Tax ID (DIČ-sk)         | exists |
| client ID               | exists |
| client name and address | exists |
| client name and email   | exists |
| otherwise               | new    |

    ⚠️ BEWARE: this decision making will be changed in near future.
    So we recommend to check for updates to avoid any problems.

If you want to add tags to client, refer to [FAQ > How do I add tags to an entity?](faq.md#how-do-i-add-tags-to-an-entity).


### Request

**URL**: `/clients/create`  
**HTTP method**: POST  

```sh
data='{
  "Client": {
    "name": "FooBar s.r.o."
  }
}';

curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/clients/create
```

### Attributes

#### Optional

| name                      | type   | description                                                     | default value |
| ------------------------- | ------ | --------------------------------------------------------------- | ------------- |
| **address**               | string | street / address                                                | |
| **bank_account**          | string | bank account (when not using IBAN)                              | |
| **bank_account_id**       | int    | bank account ID                                                 | |
| **bank_account_prefix**   | string | bank account prefix                                             | |
| **bank_code**             | string | bank account code (when not using IBAN)                         | |
| **city**                  | string | city                                                            | |
| **comment**               | string | comment                                                         | |
| **country**               | string | country name                                                    | |
| **country_id**            | int    | country ID (see [Value lists > Country list](value-lists.md#country-list))                   | 191 (Slovakia), 57 (Czech republic) |
| **currency**              | string | currency (see [Value lists > Currencies](value-lists.md#currencies))                       | |
| **default_variable**      | string | default variable symbol for client                              | |
| **delivery_address**      | string | delivery address                                                | |
| **delivery_city**         | string | delivery city                                                   | |
| **delivery_country**      | string | delivery country name                                           | |
| **delivery_country_id**   | int    | delivery country ID (see [Value lists > Country list](value-lists.md#country-list))          | |
| **delivery_name**         | string | delivery company name                                           | |
| **delivery_phone**        | string | delivery phone                                                  | |
| **delivery_state**        | string | delivery state (only for the USA)                               | |
| **delivery_zip**          | string | delivery ZIP                                                    | |
| **dic**                   | string | Tax ID (DIČ-sk)                                                 | |
| **discount**              | float  | discount                                                        | |
| **distance**              | float  | distance from you to client (used in Logbook)                   | |
| **dont_travel**           | int    | don't use this client in rides reconstruction (0 = no, 1 = yes) | |
| **due_date**              | int    | default number of days until due date                           | |
| **email**                 | string | email                                                           | |
| **fax**                   | string | fax                                                             | |
| **iban**                  | string | IBAN                                                            | |
| **ic_dph**                | string | VAT ID (IČ DPH🇸🇰, DIČ-cz)                                      | |
| **ico**                   | string | ID (IČO)                                                        | |
| **id**                    | int    | client ID                                                       | |
| **name**                  | string | client name                                                     | |
| **notices**               | int    | send automatic notices, (0 = no, 1 = yes)                       | |
| **phone**                 | string | phone number                                                    | |
| **state**                 | string | state name (only for the USA)                                   | |
| **swift**                 | string | SWIFT code                                                      | |
| **uuid**                  | string | unique client UUID - client identifier in your system           | null |
| **zip**                   | string | ZIP code                                                        | |


### Response

#### Successfully changed name
```sh
data='{
  "Client": {
    "id": 1,
    "name": "Foo Bar Baz",
    "update": 1
  }
}';

curl -X POST --post-data="data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/clients/create
```

```json
{
  "data": {
    "Client": {
      "account": null,
      "address": "Vymyslena 1",
      "bank_account": "",
      "bank_account_id": "0",
      "bank_account_prefix": null,
      "bank_code": "",
      "city": "Bratislava",
      "comment": "",
      "country": "Slovensko",
      "country_id": "191",
      "created": "2050-01-01 23:59:59",
      "currency": null,
      "default_variable": "",
      "delivery_address": "",
      "delivery_city": "",
      "delivery_country": "Slovensko",
      "delivery_country_id": "191",
      "delivery_name": "",
      "delivery_phone": "",
      "delivery_state": "",
      "delivery_zip": "",
      "dic": "123456",
      "discount": null,
      "distance": null,
      "dont_travel": false,
      "due_date": null,
      "email": "",
      "fax": "",
      "iban": "",
      "ic_dph": "",
      "ico": "",
      "id": "1",
      "modified": "2050-01-01 23:59:59",
      "name": "Foo Bar Baz",
      "notices": true,
      "phone": "",
      "state": "",
      "swift": "",
      "tags": null,
      "update": "1",
      "user_id": "1",
      "user_profile_id": "1",
      "uuid": null,
      "zip": "555 55"
    }
  },
  "error": 0,
  "error_message": "Client created"
}
```


#### Successfully created client
```sh
data='{
    "Client":{
        "name":"FooBar s.r.o."
    }
}';

curl -X POST \ 
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/clients/create
```

```json
{
  "data": {
    "Client": {
      "account": null,
      "address": null,
      "bank_account": null,
      "bank_account_id": null,
      "bank_account_prefix": null,
      "bank_code": null,
      "city": null,
      "comment": null,
      "country": null,
      "country_id": "191",
      "created": "2050-01-01 23:59:59",
      "currency": null,
      "default_variable": null,
      "delivery_address": null,
      "delivery_city": null,
      "delivery_country": null,
      "delivery_country_id": null,
      "delivery_name": null,
      "delivery_phone": null,
      "delivery_state": null,
      "delivery_zip": null,
      "dic": null,
      "discount": null,
      "distance": null,
      "dont_travel": null,
      "due_date": null,
      "email": null,
      "fax": null,
      "iban": null,
      "ic_dph": null,
      "ico": null,
      "id": "4",
      "modified": "2050-01-01 23:59:59",
      "name": "FooBar s.r.o.",
      "notices": true,
      "phone": null,
      "state": null,
      "swift": null,
      "tags": null,
      "update": "4",
      "user_id": "1",
      "user_profile_id": "1",
      "uuid": null,
      "zip": null
    }
  },
  "error": 0,
  "error_message": "Client created"
}
```


#### Missing data
```json
{
  "error": 1,
  "error_message": "Missing data"
}
```

#### Duplicate client  
```json
{
  "error": 1,
  "error_message": {
    "name": [
      "Nemožno vytvoriť duplicitného klienta."
    ]
  }
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## View client detail

View client details.

### Request

**URL**: `/clients/view/{ID}`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/clients/view/3
```

### Attributes

#### Required
| name            | type | description | default value |
| --------------- | ---- | ----------- | ------------- |
| **id**          | int  | client ID   |               |

#### Optional
none

### Response

```json
{
  "Client": {
    "account": "",
    "address": "Pri Suchom mlyne 6",
    "bank_account": "",
    "bank_account_id": "0",
    "bank_account_prefix": "",
    "bank_code": "",
    "city": "Bratislava - mestsk&aacute; časť Star&eacute; Mesto",
    "comment": "",
    "country": "Slovensko",
    "country_id": "191",
    "created": "2050-01-01 23:59:59",
    "currency": "",
    "default_variable": "",
    "delivery_address": "",
    "delivery_city": "",
    "delivery_country": "Slovensko",
    "delivery_country_id": "191",
    "delivery_name": "",
    "delivery_phone": "",
    "delivery_state": "",
    "delivery_zip": "",
    "dic": "2023513470",
    "discount": "",
    "distance": "",
    "dont_travel": "",
    "due_date": "",
    "email": "",
    "fax": "",
    "iban": "",
    "ic_dph": "SK2023513470",
    "ico": "46655034",
    "id": "3",
    "modified": "2050-01-01 23:59:59",
    "name": "SuperFaktura, s.r.o.",
    "notices": "1",
    "phone": "",
    "state": "",
    "swift": "",
    "tags": "",
    "update": "4",
    "user_id": "1",
    "user_profile_id": "1",
    "uuid": "",
    "zip": "811 04"
  },
  "ContactPerson": [
    {
      "client_id": "3",
      "created": "2050-01-01 23:59:59",
      "email": "janko.hrasko@example.com",
      "id": "1",
      "modified": "2050-01-01 23:59:59",
      "name": "Janko Hrasko",
      "phone": null,
      "user_id": "1",
      "user_profile_id": "1"
    }
  ],
  "Country": {
    "created": null,
    "eu": true,
    "id": "191",
    "iso": "sk",
    "modified": null,
    "name": "Slovensko",
    "order": "1"
  },
  "Tag": []
}
```

#### Wrong client
```json
{
  "error": 1,
  "error_message": "Client not found"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Get client list

Get list of clients based on filtering parameters.

### Request

**URL**: `/clients/index.json[/{ATTRIBUTE}:{VALUE}]*`  
**HTTP method**: GET  

Other URL examples:
- `/clients/index.json`  
- `/clients/index.json/listinfo:1`  
- `/clients/index.json/search:superfaktura`  
- `/clients/index.json/listinfo:1/search:c3VwZXJmYWt0dXJh`

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/clients/index.json
```


### Attributes  

#### Required
none

#### Optional

| name            | type   | description | default value |
| --------------- | ------ | ----------- | ------------- |
| **char_filter** | string | search by first letter of client name (non letter characters are under `#`) | |
| **direction**   | string | sorting type, `ASC` or `DESC`| `DESC` |
| **list_info**   | int    | should meta information be returned? <ul><li>page number</li><li>number of pages</li><li>number of results per page</li><li>number of results</li></ul> | |
| **per_page**    | int    | number of results per page | |
| **search**      | string | search by base64 encoded substring in the following fields: <ul><li>name</li><li>ID (ICO)</li><li>Tax ID (DIC)</li><li>VAT ID (IC_DPH)</li><li>bank_account</li><li>email</li><li>address</li><li>city</li><li>zip</li><li>state</li><li>country</li><li>phone</li><li>fax</li><li>comment</li><li>tags</li><li>UUID</li></ul> | |
| **search_uuid** | string | search by UUID | | 
| **sort**        | string | sorting attribute | `regular_count` |
| **tag**         | int    | tag ID | |


### Response

#### Get all the clients  
```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/clients/index.json
```

```json
[
  {
    "Client": {
      "account": null,
      "address": "Vymyslena 1",
      "bank_account": "",
      "bank_account_id": "0",
      "bank_account_prefix": null,
      "bank_code": "",
      "city": "Bratislava",
      "comment": "",
      "country": "Slovensko",
      "country_id": "191",
      "created": "2050-01-01 23:59:59",
      "currency": null,
      "default_variable": "",
      "delivery_address": "",
      "delivery_city": "",
      "delivery_country": "Slovensko",
      "delivery_country_id": "191",
      "delivery_name": "",
      "delivery_phone": "",
      "delivery_state": "",
      "delivery_zip": "",
      "dic": "123456",
      "discount": null,
      "distance": null,
      "dont_travel": false,
      "due_date": null,
      "email": "",
      "fax": "",
      "iban": "",
      "ic_dph": "",
      "ico": "",
      "id": "1",
      "modified": "2050-01-01 23:59:59",
      "name": "John Doe",
      "notices": true,
      "phone": "",
      "state": "",
      "swift": "",
      "tags": null,
      "update": "4",
      "user_id": "1",
      "user_profile_id": "1",
      "uuid": null,
      "zip": "555 55"
    },
    "ClientStat": {
      "cancel_count": "0",
      "cancel_total": "0.00",
      "client_id": "1",
      "date_founded": null,
      "delivery_count": "0",
      "delivery_total": "0.00",
      "estimate_count": "0",
      "estimate_total": "0.00",
      "expense_count": "0",
      "expense_total": "0.00",
      "expense_unpaid_count": "0",
      "expense_unpaid_total": "0.00",
      "id": "1",
      "order_count": "0",
      "order_total": "0.00",
      "pay_time": "0.00",
      "proforma_count": "0",
      "proforma_overdue_count": "0",
      "proforma_overdue_total": "0.00",
      "proforma_total": "0.00",
      "regular_count": "0",
      "regular_overdue_count": "0",
      "regular_overdue_total": "0.00",
      "regular_total": "0.00",
      "reverse_order_count": "0",
      "reverse_order_total": "0.00",
      "risk": "0"
    }
  },
  {
    "Client": {
      "account": null,
      "address": "North Pole 1",
      "bank_account": "",
      "bank_account_id": "0",
      "bank_account_prefix": null,
      "bank_code": "",
      "city": "Santa’s Village",
      "comment": "",
      "country": "Finland",
      "country_id": "73",
      "created": "2050-01-01 23:59:59",
      "currency": null,
      "default_variable": "",
      "delivery_address": "",
      "delivery_city": "",
      "delivery_country": "Slovensko",
      "delivery_country_id": "191",
      "delivery_name": "",
      "delivery_phone": "",
      "delivery_state": "",
      "delivery_zip": "",
      "dic": "",
      "discount": null,
      "distance": null,
      "dont_travel": false,
      "due_date": null,
      "email": "",
      "fax": "",
      "iban": "",
      "ic_dph": "",
      "ico": "",
      "id": "2",
      "modified": "2050-01-01 23:59:59",
      "name": "Santa Claus",
      "notices": true,
      "phone": "",
      "state": "",
      "swift": "",
      "tags": null,
      "update": "4",
      "user_id": "1",
      "user_profile_id": "1",
      "uuid": null,
      "zip": "999 99"
    },
    "ClientStat": {
      "cancel_count": "0",
      "cancel_total": "0.00",
      "client_id": "2",
      "date_founded": null,
      "delivery_count": "0",
      "delivery_total": "0.00",
      "estimate_count": "0",
      "estimate_total": "0.00",
      "expense_count": "0",
      "expense_total": "0.00",
      "expense_unpaid_count": "0",
      "expense_unpaid_total": "0.00",
      "id": "2",
      "order_count": "0",
      "order_total": "0.00",
      "pay_time": "0.00",
      "proforma_count": "0",
      "proforma_overdue_count": "0",
      "proforma_overdue_total": "0.00",
      "proforma_total": "0.00",
      "regular_count": "0",
      "regular_overdue_count": "0",
      "regular_overdue_total": "0.00",
      "regular_total": "0.00",
      "reverse_order_count": "0",
      "reverse_order_total": "0.00",
      "risk": "0"
    }
  },
  {
    "Client": {
      "account": null,
      "address": "Pri Suchom mlyne 6",
      "bank_account": "",
      "bank_account_id": "0",
      "bank_account_prefix": null,
      "bank_code": "",
      "city": "Bratislava - mestská časť Staré Mesto",
      "comment": "",
      "country": "Slovensko",
      "country_id": "191",
      "created": "2050-01-01 23:59:59",
      "currency": null,
      "default_variable": "",
      "delivery_address": "",
      "delivery_city": "",
      "delivery_country": "Slovensko",
      "delivery_country_id": "191",
      "delivery_name": "",
      "delivery_phone": "",
      "delivery_state": "",
      "delivery_zip": "",
      "dic": "2023513470",
      "discount": null,
      "distance": null,
      "dont_travel": false,
      "due_date": null,
      "email": "",
      "fax": "",
      "iban": "",
      "ic_dph": "SK2023513470",
      "ico": "46655034",
      "id": "3",
      "modified": "2050-01-01 23:59:59",
      "name": "SuperFaktura, s.r.o.",
      "notices": true,
      "phone": "",
      "state": "",
      "swift": "",
      "tags": null,
      "update": "4",
      "user_id": "1",
      "user_profile_id": "1",
      "uuid": null,
      "zip": "811 04"
    },
    "ClientStat": {
      "cancel_count": null,
      "cancel_total": null,
      "client_id": null,
      "date_founded": null,
      "delivery_count": null,
      "delivery_total": null,
      "estimate_count": null,
      "estimate_total": null,
      "expense_count": null,
      "expense_total": null,
      "expense_unpaid_count": null,
      "expense_unpaid_total": null,
      "id": null,
      "order_count": null,
      "order_total": null,
      "pay_time": null,
      "proforma_count": null,
      "proforma_overdue_count": null,
      "proforma_overdue_total": null,
      "proforma_total": null,
      "regular_count": null,
      "regular_overdue_count": null,
      "regular_overdue_total": null,
      "regular_total": null,
      "reverse_order_count": null,
      "reverse_order_total": null,
      "risk": null
    }
  }
]
```


#### With info listing
  
```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/clients/index.json/listinfo:1
```

In the key `items` is the same content as in the example above.

```json
{
  "itemCount": 3,
  "items": [
    {
      "Client": {
        "account": null,
        "address": "Vymyslena 1",
        "bank_account": "",
        "bank_account_id": "0",
        "bank_account_prefix": null,
        "bank_code": "",
        "city": "Bratislava",
        "comment": "",
        "country": "Slovensko",
        "country_id": "191",
        "created": "2050-01-01 23:59:59",
        "currency": null,
        "default_variable": "",
        "delivery_address": "",
        "delivery_city": "",
        "delivery_country": "Slovensko",
        "delivery_country_id": "191",
        "delivery_name": "",
        "delivery_phone": "",
        "delivery_state": "",
        "delivery_zip": "",
        "dic": "123456",
        "discount": null,
        "distance": null,
        "dont_travel": false,
        "due_date": null,
        "email": "",
        "fax": "",
        "iban": "",
        "ic_dph": "",
        "ico": "",
        "id": "1",
        "modified": "2050-01-01 23:59:59",
        "name": "John Doe",
        "notices": true,
        "phone": "",
        "state": "",
        "swift": "",
        "tags": null,
        "update": "4",
        "user_id": "1",
        "user_profile_id": "1",
        "uuid": null,
        "zip": "555 55"
      },
      "ClientStat": {
        "cancel_count": "0",
        "cancel_total": "0.00",
        "client_id": "1",
        "date_founded": null,
        "delivery_count": "0",
        "delivery_total": "0.00",
        "estimate_count": "0",
        "estimate_total": "0.00",
        "expense_count": "0",
        "expense_total": "0.00",
        "expense_unpaid_count": "0",
        "expense_unpaid_total": "0.00",
        "id": "1",
        "order_count": "0",
        "order_total": "0.00",
        "pay_time": "0.00",
        "proforma_count": "0",
        "proforma_overdue_count": "0",
        "proforma_overdue_total": "0.00",
        "proforma_total": "0.00",
        "regular_count": "0",
        "regular_overdue_count": "0",
        "regular_overdue_total": "0.00",
        "regular_total": "0.00",
        "reverse_order_count": "0",
        "reverse_order_total": "0.00",
        "risk": "0"
      }
    },
    {
      "Client": {
        "account": null,
        "address": "North Pole 1",
        "bank_account": "",
        "bank_account_id": "0",
        "bank_account_prefix": null,
        "bank_code": "",
        "city": "Santa’s Village",
        "comment": "",
        "country": "Finland",
        "country_id": "73",
        "created": "2050-01-01 23:59:59",
        "currency": null,
        "default_variable": "",
        "delivery_address": "",
        "delivery_city": "",
        "delivery_country": "Slovensko",
        "delivery_country_id": "191",
        "delivery_name": "",
        "delivery_phone": "",
        "delivery_state": "",
        "delivery_zip": "",
        "dic": "",
        "discount": null,
        "distance": null,
        "dont_travel": false,
        "due_date": null,
        "email": "",
        "fax": "",
        "iban": "",
        "ic_dph": "",
        "ico": "",
        "id": "2",
        "modified": "2050-01-01 23:59:59",
        "name": "Santa Claus",
        "notices": true,
        "phone": "",
        "state": "",
        "swift": "",
        "tags": null,
        "update": "4",
        "user_id": "1",
        "user_profile_id": "1",
        "uuid": null,
        "zip": "999 99"
      },
      "ClientStat": {
        "cancel_count": "0",
        "cancel_total": "0.00",
        "client_id": "2",
        "date_founded": null,
        "delivery_count": "0",
        "delivery_total": "0.00",
        "estimate_count": "0",
        "estimate_total": "0.00",
        "expense_count": "0",
        "expense_total": "0.00",
        "expense_unpaid_count": "0",
        "expense_unpaid_total": "0.00",
        "id": "2",
        "order_count": "0",
        "order_total": "0.00",
        "pay_time": "0.00",
        "proforma_count": "0",
        "proforma_overdue_count": "0",
        "proforma_overdue_total": "0.00",
        "proforma_total": "0.00",
        "regular_count": "0",
        "regular_overdue_count": "0",
        "regular_overdue_total": "0.00",
        "regular_total": "0.00",
        "reverse_order_count": "0",
        "reverse_order_total": "0.00",
        "risk": "0"
      }
    },
    {
      "Client": {
        "account": null,
        "address": "Pri Suchom mlyne 6",
        "bank_account": "",
        "bank_account_id": "0",
        "bank_account_prefix": null,
        "bank_code": "",
        "city": "Bratislava - mestská časť Staré Mesto",
        "comment": "",
        "country": "Slovensko",
        "country_id": "191",
        "created": "2050-01-01 23:59:59",
        "currency": null,
        "default_variable": "",
        "delivery_address": "",
        "delivery_city": "",
        "delivery_country": "Slovensko",
        "delivery_country_id": "191",
        "delivery_name": "",
        "delivery_phone": "",
        "delivery_state": "",
        "delivery_zip": "",
        "dic": "2023513470",
        "discount": null,
        "distance": null,
        "dont_travel": false,
        "due_date": null,
        "email": "",
        "fax": "",
        "iban": "",
        "ic_dph": "SK2023513470",
        "ico": "46655034",
        "id": "3",
        "modified": "2050-01-01 23:59:59",
        "name": "SuperFaktura, s.r.o.",
        "notices": true,
        "phone": "",
        "state": "",
        "swift": "",
        "tags": null,
        "update": "4",
        "user_id": "1",
        "user_profile_id": "1",
        "uuid": null,
        "zip": "811 04"
      },
      "ClientStat": {
        "cancel_count": null,
        "cancel_total": null,
        "client_id": null,
        "date_founded": null,
        "delivery_count": null,
        "delivery_total": null,
        "estimate_count": null,
        "estimate_total": null,
        "expense_count": null,
        "expense_total": null,
        "expense_unpaid_count": null,
        "expense_unpaid_total": null,
        "id": null,
        "order_count": null,
        "order_total": null,
        "pay_time": null,
        "proforma_count": null,
        "proforma_overdue_count": null,
        "proforma_overdue_total": null,
        "proforma_total": null,
        "regular_count": null,
        "regular_overdue_count": null,
        "regular_overdue_total": null,
        "regular_total": null,
        "reverse_order_count": null,
        "reverse_order_total": null,
        "risk": null
      }
    }
  ],
  "page": 1,
  "pageCount": 1,
  "perPage": 50
}
```