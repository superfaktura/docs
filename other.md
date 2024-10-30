# Other API commands

- [Get list of your accounts](#get-list-of-your-accounts)
- [Get user companies data](#get-user-companies-data)
- [Send SMS reminder](#send-sms-reminder)
- [Get bank account moves](#get-bank-account-moves)
- [Get invoice activity logs](#get-invoice-activity-logs)

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

- - - - - - - - - - - - - - - - - - - - - - - - - - - -

## Get invoice activity logs

Get invoice activity logs.

### Request
**URL**: `/activity_logs/activity_list/{DOCUMENT_TYPE}/{DOCUMENT_ID}/{LIMIT}`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/activity_logs/activity_list/invoice/1/10
```

### Attributes
#### Required
URL parameters:

| name              | type    | description                            | default value |
| ----------------- | ------- | -------------------------------------- | ------------- |
| **document_type** | string  | type of document (invoice or expense)  |               |
| **document_id**   | int     | ID of document                         |               |

#### Optional
| name      | type | description             | default value |
| --------- | ---- | ----------------------- | ------------- |
| **limit** | int  | limit of activity logs  | 10            |

### Response

#### Success
```json
[
    {
        "ActivityLog": {
            "id": "6309",
            "data":"{\"Invoice\":{\"is_duplicated\":\"\",\"from_expense\":\"0\",\"related_item_id\":\"\",\"related_item_type\":\"\",\"child_id\":\"\",\"order_id\":\"\",\"updated_sequence_id\":\"\",\"created\":\"2024-10-30\",\"delivery\":\"2024-10-30\",\"exchange_rate_inverted\":0,\"vat_transfer\":\"0\",\"client\":\"Test\",\"is_summary_invoice\":\"0\",\"client_data\":\"{\\\"Client\\\":{\\\"id\\\":\\\"13032570\\\",\\\"name\\\":\\\"Test\\\",\\\"address\\\":\\\"\\\",\\\"ico\\\":\\\"\\\",\\\"email\\\":\\\"\\\",\\\"zip\\\":\\\"\\\",\\\"dic\\\":\\\"\\\",\\\"phone\\\":\\\"\\\",\\\"city\\\":\\\"\\\",\\\"ic_dph\\\":\\\"\\\",\\\"fax\\\":\\\"\\\",\\\"country_id\\\":\\\"191\\\",\\\"state\\\":\\\"\\\",\\\"delivery_name\\\":\\\"\\\",\\\"delivery_zip\\\":\\\"\\\",\\\"delivery_city\\\":\\\"\\\",\\\"delivery_address\\\":\\\"\\\",\\\"delivery_phone\\\":\\\"\\\",\\\"delivery_country_id\\\":\\\"\\\",\\\"delivery_state\\\":\\\"\\\",\\\"updateClient\\\":\\\"0\\\",\\\"save_contact_from_document\\\":\\\"\\\",\\\"country\\\":\\\"Slovensko\\\",\\\"delivery_country\\\":null}}\",\"force_user_id\":true,\"from_web\":true,\"id\":\"24756187\",\"user_profile_id\":\"44775\",\"type\":\"regular\",\"client_id\":\"13032570\",\"name\":\"Fakt\úra 2024001\",\"invoice_no_formatted\":\"2024001\"},\"MyData\":{\"Logo\":\"[]\",\"Signature\":\"[]\"},\"InvoiceItem\":[{\"tax_deposit\":\"0\",\"unit_type\":\"\",\"discount\":\"0%\",\"unit_price\":\"11\",\"discount_no_vat\":\"0,00\",\"stock_item_id\":\"0\",\"quantity_previous\":\"1\",\"sum\":\"13,31\",\"discount_total\":\"0,00\"}],\"Tag\":{\"Tag\":\"\"}}",
            "created": "2024-10-30 12:33:10",
            "item_id": "24756187",
            "item_type": "invoice",
            "event_type": "update",
            "client_id": "13032570",
            "user_id": "2"
        },
        "User": {
            "name": "Test",
            "email": "test1@test.sk"
        }
    },
    {
        "ActivityLog": {
            "id": "6308",
            "data":"{\"App\":{\"upid_check\":\"44775\",\"csrf_token\":\"lc60Knw45c5v\\/wkklsmy0rpHeBsyOy7AYiMIgVIE7o9YAoxmdKV3WJiobienqPI5OXpoZ3BrVEhuaU9GbjFhQkd5WTFwRThYNFVFbUhSeUphTTlYQnlONnNNNGtJbjk2c0g5SFUxSDRNSFg5YkRZN1IrMjF4MUprMzF1V3VpSWRIbXgxN0FDTlNRME02dlBJQ3NPNm9pajF5bUhKUE5EQTl4cHBmRWtOekM1S2pKeU5QUUlHK1lHRUpHc281NEtrYU9EZksrV1l6dXk1ZWpaTE5CTkdTV3RNWlIybFNrOVFpMU13NGVKYlhvb0pUVjR3VmZ5OUNhbG5oYXZVdGh4VkI0VzFZaXcrcDlZK0FoWVF1UzRJenBIQ08wMHQxcWZFaEE9PQ==\"},\"ClientData\":{\"id\":\"13032570\",\"name\":\"Test\",\"address\":\"\",\"ico\":\"\",\"email\":\"\",\"zip\":\"\",\"dic\":\"\",\"phone\":\"\",\"city\":\"\",\"ic_dph\":\"\",\"fax\":\"\",\"country_id\":\"191\",\"state\":\"\",\"delivery_name\":\"\",\"delivery_zip\":\"\",\"delivery_city\":\"\",\"delivery_address\":\"\",\"delivery_phone\":\"\",\"delivery_country_id\":\"\",\"delivery_state\":\"\",\"updateClient\":\"0\",\"save_contact_from_document\":\"\"},\"Invoice\":{\"from_expense\":\"0\",\"id\":24756187,\"type\":\"regular\",\"user_profile_id\":\"44775\",\"status\":1,\"parent_id\":\"\",\"related_item_id\":\"\",\"related_item_type\":\"\",\"child_id\":\"\",\"estimate_id\":\"\",\"order_id\":\"\",\"sequence_id\":547361,\"updated_sequence_id\":\"\",\"home_currency\":\"CZK\",\"lang\":\"slo\",\"tax_document\":\"\",\"rounding\":\"item_ext\",\"summary_invoice\":\"\",\"invoice_no_formatted\":\"2024001\",\"variable\":\"2024001\",\"name\":\"Fakt\úra 2024001\",\"created\":\"2024-10-30 00:00:00\",\"delivery\":\"2024-10-30 00:00:00\",\"due_in\":\"14\",\"due_date\":\"13.11.2024\",\"delivery_type\":\"\",\"payment_type\":\"\",\"constant\":\"\",\"specific\":\"\",\"order_no\":\"\",\"invoice_currency\":\"CZK\",\"exchange_rate_inverted\":0,\"vat_transfer\":\"0\",\"client_id\":\"13032570\",\"client\":\"Test\",\"header_comment\":\"\",\"items_name\":null,\"comment\":\"\",\"is_summary_invoice\":\"0\",\"discount\":\"0\",\"deposit\":\"\",\"issued_by\":\"Test\",\"issued_by_phone\":\"\",\"issued_by_web\":\"\",\"issued_by_email\":\"test@gmail.com\",\"client_data\":\"{\\\"Client\\\":{\\\"id\\\":\\\"13032570\\\",\\\"name\\\":\\\"Test\\\",\\\"address\\\":\\\"\\\",\\\"ico\\\":\\\"\\\",\\\"email\\\":\\\"\\\",\\\"zip\\\":\\\"\\\",\\\"dic\\\":\\\"\\\",\\\"phone\\\":\\\"\\\",\\\"city\\\":\\\"\\\",\\\"ic_dph\\\":\\\"\\\",\\\"fax\\\":\\\"\\\",\\\"country_id\\\":\\\"191\\\",\\\"state\\\":\\\"\\\",\\\"delivery_name\\\":\\\"\\\",\\\"delivery_zip\\\":\\\"\\\",\\\"delivery_city\\\":\\\"\\\",\\\"delivery_address\\\":\\\"\\\",\\\"delivery_phone\\\":\\\"\\\",\\\"delivery_country_id\\\":\\\"\\\",\\\"delivery_state\\\":\\\"\\\",\\\"updateClient\\\":\\\"0\\\",\\\"save_contact_from_document\\\":\\\"\\\",\\\"country\\\":\\\"Slovensko\\\"}}\",\"my_data\":\"{\\\"MyData\\\":{\\\"id\\\":\\\"44775\\\",\\\"user_id\\\":\\\"2\\\",\\\"user_profile_id\\\":\\\"\\\",\\\"country_id\\\":\\\"191\\\",\\\"company_name\\\":\\\"SuperFaktura, s.r.o.\\\",\\\"address\\\":\\\"Pri Suchom mlyne 6\\\",\\\"city\\\":\\\"Bratislava - mestsk\\\á \\\čas\\\ť Star\\\é Mesto\\\",\\\"zip\\\":\\\"811 04\\\",\\\"ico\\\":\\\"46655034\\\",\\\"dic\\\":\\\"2023513470\\\",\\\"ic_dph\\\":\\\"SK2023513470\\\",\\\"update_profile\\\":\\\"\\\",\\\"tax_payer\\\":\\\"1\\\",\\\"logo_key\\\":\\\"\\\",\\\"logo_id\\\":\\\"\\\",\\\"web\\\":\\\"\\\",\\\"Logo\\\":\\\"[]\\\",\\\"Signature\\\":\\\"[]\\\",\\\"travel_agencies\\\":\\\"\\\",\\\"business_register\\\":\\\"Obchodn\\\ý register Mestsk\\\ého s\\\údu Bratislava III, oddiel: Sro, vlo\\\žka \\\č. 81403\\\\\\/B\\\",\\\"country\\\":\\\"Slovensko\\\"}}\",\"due\":\"2024-11-13\",\"invoice_no\":1,\"exchange_rate\":1},\"MyData\":{\"id\":\"44775\",\"user_id\":\"2\",\"user_profile_id\":\"\",\"country_id\":\"191\",\"company_name\":\"SuperFaktura, s.r.o.\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\á \čas\ť Star\é Mesto\",\"zip\":\"811 04\",\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"update_profile\":\"\",\"tax_payer\":\"1\",\"logo_key\":\"\",\"logo_id\":\"\",\"web\":\"\",\"Logo\":\"[]\",\"Signature\":\"[]\",\"travel_agencies\":\"\",\"business_register\":\"Obchodn\ý register Mestsk\ého s\údu Bratislava III, oddiel: Sro, vlo\žka \č. 81403\\/B\"},\"InvoiceSetting\":{\"signature\":true,\"bysquare\":true,\"payment_info\":true,\"language\":\"slo\",\"online_payment\":false,\"summary_bg_color\":\"#d4eef6\",\"force_iban\":true,\"create_from_multiple_deliveries\":\"\"},\"InvoiceItem\":[{\"id\":103367380,\"tax_deposit\":\"0\",\"name\":\"test\",\"description\":\"\",\"discount_description\":\"Z\ľava\",\"quantity\":null,\"unit_type\":\"\",\"unit\":\"\",\"discount\":\"0%\",\"unit_price\":\"10\",\"discount_no_vat\":\"0,00\",\"tax\":\"21\",\"ordernum\":0,\"stock_item_id\":\"\",\"sku\":\"\",\"hide_in_autocomplete\":\"\",\"quantity_previous\":\"0\",\"sum\":\"12,10\",\"discount_total\":\"0,00\"}],\"Tag\":{\"Tag\":\"\"}}",
            "created": "2024-10-30 12:33:00",
            "item_id": "24756187",
            "item_type": "invoice",
            "event_type": "create",
            "client_id": "13032570",
            "user_id": "2"
        },
        "User": {
            "name": "Test",
            "email": "test1@test.sk"
        }
    }
]
```
