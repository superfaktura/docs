# Other API commands

- [Get list of your accounts](#get-list-of-your-accounts)
- [Get user companies data](#get-user-companies-data)
- [Send SMS reminder](#send-sms-reminder)

## Get list of your accounts

Get list of your profiles with detailed information.

### Request

**URL**: `/users/company_switcher`  
**HTTP method**: GET  

```
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/users/company_switcher
```

### Attributes

#### Required
none

#### Optional
none

### Response

```json
{
  "apikey": "9771ef49cd922da79b20745b7bc0fc24",
  "companies": [
    {
      "Logo": {
        "0": {
          "alternative": null,
          "basename": "4311c1895aa334d39ac8_1_exads_logo_rgb.png",
          "checksum": "a1dcdc392d08d6d1caaf148225f2a7d4",
          "created": "2050-01-01 23:59:59",
          "default": true,
          "delete_flag": false,
          "dirname": "img",
          "extern_file": "0",
          "foreign_key": "1",
          "group": "logo",
          "id": "1",
          "model": "User",
          "modified": "2050-01-01 23:59:59",
          "path": "img/4311c1895aa334d39ac8_1_exads_logo_rgb.png",
          "size": "49743"
        },
        "size": {
          "0": 75,
          "1": 57,
          "2": 3,
          "3": "width=\"75\" height=\"57\"",
          "bits": 8,
          "mime": "image/png"
        },
        "url": "https://moja.superfaktura.sk/img/no-logo.png"
      },
      "UserProfile": {
        "address": "Pri Suchom mlyne 6",
        "affiliate_id": null,
        "business_register": "Obchodný register Okresného súdu Bratislava I, oddiel: Sro, vložka č. 81403/B",
        "bysquare": true,
        "city": "Bratislava - mestská časť Staré Mesto",
        "company_name": "SuperFaktura, s.r.o.",
        "company_type": "ltd",
        "country_id": "191",
        "created": "2050-01-01 23:59:59",
        "date_mask": "d.m.Y",
        "default_constant": "",
        "default_delivery": "created",
        "default_payment_type": null,
        "delete_status": "default",
        "dic": "2023513470",
        "disable_footer": null,
        "due_warning_subject": null,
        "due_warning_template": null,
        "expense_rate": "40.00",
        "header_logo": false,
        "help": "1",
        "home_currency": "EUR",
        "ic_dph": "SK2023513470",
        "ico": "46655034",
        "ico_raw": "46655034",
        "id": "1",
        "invoice_comment": null,
        "invoice_email_subject": null,
        "invoice_email_template": "",
        "invoice_header_comment": null,
        "invoice_item_limit": "50",
        "invoice_items_name": null,
        "invoice_no_mask": "YYYYNNN",
        "invoice_sequence": "1",
        "invoice_sequence_type": "yearly",
        "items_per_page": "50",
        "last_login": "2050-01-01",
        "modified": "2050-01-01 23:59:59",
        "name": null,
        "newsletter": "0",
        "online_payments": false,
        "payment_thankyou_subject": null,
        "payment_thankyou_template": null,
        "phone": "",
        "rounding": "item",
        "setup_finished": false,
        "tax_base": "0.00",
        "tax_payer": "1",
        "update_taxdate": true,
        "user_id": "1",
        "vat_interval": null,
        "web": "",
        "zip": "811 04"
      }
    }
  ],
  "email": "api@example.com",
  "language": "slo",
  "user_name": null
}
```


Or when you have multiple companies
```json
{
  "apikey": "9771ef49cd922da79b20745b7bc0fc24",
  "companies": {
    "1": {
      "Logo": {
        "size": false,
        "url": "https://moja.superfaktura.sk/"
      },
      "Multiaccount": {
        "enabled": true,
        "id": "1",
        "role": "owner",
        "user_profile_id": "1"
      },
      "UserProfile": {
        "Logo": [
          {
            "basename": "4311c1895aa334d39ac8_1_exads_logo_rgb.png",
            "dirname": "img",
            "file": "/var/www/superfaktura/app/webroot/media/transfer/img/4311c1895aa334d39ac8_1_exads_logo_rgb.png",
            "foreign_key": "1"
          }
        ],
        "company_name": "SuperFaktura, s.r.o.",
        "delete_status": "default",
        "id": "1"
      }
    },
    "2": {
      "Logo": {
        "size": {
          "0": 75,
          "1": 57,
          "2": 3,
          "3": "width=\"75\" height=\"57\"",
          "bits": 8,
          "mime": "image/png"
        },
        "url": "https://moja.superfaktura.sk/img/no-logo.png"
      },
      "Multiaccount": {
        "enabled": true,
        "id": "2",
        "role": "owner",
        "user_profile_id": "2"
      },
      "UserProfile": {
        "company_name": "Test a.s.",
        "delete_status": "",
        "id": "2"
      }
    }
  },
  "email": "api@example.com",
  "language": "slo",
  "user_name": null
}
```


## Get user companies data

Get information about company in which user is currently logged in.
Alternatively return information about all companies, to which user has access (see optional attributes).
This information includes list of bank accounts.

### Request

**URL**: `/users/getUserCompaniesData[/{GET_ALL_COMPANIES}]`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=other.user%40superfaktura.sk&apikey=77e41f72268faa33347b7803b96f08e0&company_id=" \
    https://moja.superfaktura.sk/users/getUserCompaniesData
```

### Attributes
#### Required
none

#### Optional
URL parameters:

| name                  | type    | description | default value |
| --------------------- | ------- | ----------- | ------------- |
| **get_all_companies** | int     | return information about all companies to which user has access (0=no, 1=yes) | 0 |

### Response

#### Successful response

```json
{
  "data": {
    "1": {
      "BankAccount": [
        {
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
      ],
      "UserProfile": {
        "address": "Pri Suchom mlyne 6",
        "business_register": "Obchodný register Okresného súdu Bratislava I, oddiel: Sro, vložka č. 81403/B",
        "city": "Bratislava - mestská časť Staré Mesto",
        "company_name": "SuperFaktura, s.r.o.",
        "company_type": "ltd",
        "country_id": "191",
        "dic": "2023513470",
        "ic_dph": "SK2023513470",
        "ico": "46655034",
        "id": "1",
        "modified": "2050-01-01 23:59:59",
        "phone": "",
        "tax_payer": "1",
        "user_id": "1",
        "web": "",
        "zip": "811 04"
      }
    }
  },
  "error": 0,
  "error_message": ""
}
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Send SMS reminder

Send a reminder before or after the maturity of invoices via SMS.
This feature requires you to have bought SMS messages (*Tools > SMS*).

### Request
**URL**: `/sms/send`  
**HTTP method**: POST  

```sh
data='{
  "invoice_id":1,
  "text":"helloworld",
  "phone":"123000456"
}';

curl -X POST \
     -d "data=$data" \
     -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
     https://moja.superfaktura.sk/sms/send
```

### Attributes
#### Required
| name              | type   | description  | default value |
| ----------------- | ------ | ------------ | ------------- |
| **invoice_id**    | int    | invoice ID   |               |
| **text**          | string | message text |               |

#### Optional
| name      | type   | description | default value |
| --------- | ------ | ----------- | ------------- |
| **phone** | string | recipient's phone number | '' (will use phone number from the invoice) | 

### Response

#### Successfully sent
```json
{
  "data": {
    "invoice_id": "1275",
    "phone": "123000456",
    "text": "helloworld"
  },
  "error": 0,
  "error_message": "SMS sent"
}
```

#### Not having prepaid SMS
```json
{
  "error": 3,
  "message": "SMS not sent: Nedostatok voľných sms"
}
```

#### Invalid phone number
```json
{
  "error": 3,
  "message": "SMS not sent: Neplatné tel. číslo"
}
```

#### Invoice not found
```json
{
  "error": 2,
  "message": "Invoice not found"
}
```

#### Empty required fields
```json
{
  "error": 1,
  "message": "Invoice ID and text cannot be empty"
}
```

```json
{
  "error": 1,
  "message": "Text cannot be empty"
}
```

```json
{
  "error": 1,
  "message": "Invoice ID cannot be empty"
}
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Get bank account moves

Get account moves.

### Request
**URL**: `/accounts/index.json`  
**HTTP method**: GET  

```sh
curl -X GET \
     -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
     https://moja.superfaktura.sk/accounts/index.json

# filter by date
curl -X GET \
     -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
     https://moja.superfaktura.sk/accounts/index.json/date:3/date_since:2050-01-27/date_to:2050-01-27
```

### Attributes

#### Required
none

#### Optional
URL parameters:

| name              | type   | description                | default value |
| ----------------- | ------ |----------------------------|---------------|
| **direction**     | string | sorting type, ASC or DESC  | ASC           |
| **page**          | int    | page number                | 1             |
| **per_page**      | int    | number of results per page |               |
| **sort**          | string | sorting attribute          |               |

Filtering parameters

| name            | type        | description                                                                  | default value |
| --------------- |-------------|------------------------------------------------------------------------------|---------------|
| **amount_from** | float\| int | amount from                                                                  | 0             |
| **amount_to**   | float\| int | amount to                                                                    | 0             |
| **date**        | int         | constant specifying time filtering (see Value lists > Time filter constants) |               |
| **date_since**  | date        | date from (requires date:3)                                                  |               |
| **date_to**     | date        | date to (requires date:3)                                                    |               |
| **move_type**   | string      | `credit`\|`debit`                                                            |               |
| **search**      | string      | base64 encoded string                                                        |               |



### Response

#### Successful
```json
{
  "itemCount": 2,
  "items": {
    "1": {
      "account_id": "1",
      "account_settings": "1__debet",
      "amount": "-117.00",
      "client": [],
      "client_account": "",
      "comment": "Platba kartou",
      "currency": "EUR",
      "date": "2050-01-27",
      "documents": [],
      "error": "Žiadna zhoda podľa sumy",
      "from_type": "statement",
      "id": "1",
      "text": "",
      "token": "c3b05c50",
      "transaction_id": null,
      "type": "without_document",
      "variable": ""
    },
    "2": {
      "account_id": "1",
      "account_settings": "1_DE75512108001245126199_debet",
      "amount": "-1000.00",
      "client": [],
      "client_account": "DE75512108001245126199",
      "comment": "Platba kartou",
      "currency": "CZK",
      "date": "2050-01-28",
      "documents": [],
      "error": "Žiadna zhoda podľa VS",
      "from_type": "statement",
      "id": "2",
      "text": "",
      "token": "c3b05c50",
      "transaction_id": null,
      "type": "without_document",
      "variable": ""
    }
  },
  "page": 1,
  "pageCount": 1,
  "perPage": 50
}
```