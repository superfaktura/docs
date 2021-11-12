# Clients

- [View client detail](#view-client-detail)
- [Get client list](#get-client-list)

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
    "city": "Bratislava - mestská časť Staré Mesto",
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
    "notices": true,
    "phone": "",
    "state": "",
    "swift": "",
    "tags": "",
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

URL parameters:

| name            | type   | description | default value |
| --------------- | ------ | ----------- | ------------- |
| **direction**   | string | sorting type, `ASC` or `DESC`| `DESC` |
| **listinfo**    | int    | should meta information be returned? <ul><li>page number</li><li>number of pages</li><li>number of results per page</li><li>number of results</li></ul> | |
| **page**        | int    | page number | 1 |
| **per_page**    | int    | number of results per page | |
| **sort**        | string | sorting attribute | `regular_count` 

Filtering parameters

| name               | type         | description    | default value |
| ------------------ | ------------ | ------------   | ------------- |
| **char_filter** | string | search by first letter of client name (non letter characters are under `#`) | |
| **created**        | int          | constant specifying time filtering (see [Value lists > Time filter constants](value-lists.md#time-filter-constants)) | |
| **created_since**  | date         | creation date since (requires `created:3`) | |
| **created_to**     | date         | creation date to (requires `created:3`) | |
| **modified**       | int          | last modification date constant specifying time filtering (see [Value lists > Time filter constants](value-lists.md#time-filter-constants)) | |
| **modified_since** | date         | last modification date from (requires `modified:3`) | |
| **modified_to**    | date         | last modification date to (requires `modified:3`)   | |
| **search**      | string | search by base64 encoded substring in the following fields: <ul><li>name</li><li>ID (ICO)</li><li>Tax ID (DIC)</li><li>VAT ID (IC_DPH)</li><li>bank_account</li><li>email</li><li>address</li><li>city</li><li>zip</li><li>state</li><li>country</li><li>phone</li><li>fax</li><li>comment</li><li>tags</li><li>UUID</li></ul> | |
| **search_uuid** | string | search by UUID | | 
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
      "dont_travel": true,
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
      "dont_travel": null,
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
      "dont_travel": null,
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
        "dont_travel": true,
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
        "dont_travel": null,
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
        "dont_travel": null,
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