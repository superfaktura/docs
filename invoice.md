# Invoice

- [Add invoice](#add-invoice)
- [Edit invoice](#edit-invoice)
- [Set invoice language](#set-invoice-language)
- [Get invoice PDF](#get-invoice-pdf)
- [Get invoice details](#get-invoice-detail)
- [Get invoices details](#get-invoices-details)
- [Get list of invoices](#get-list-of-invoices)
- [Export invoices](#export-invoices)
- [Delete invoice](#delete-invoice)

Paying invoice  
- [Set invoice as "will not be paid"](#set-invoice-as-will-not-be-paid)
- [Pay invoice](#pay-invoice)

Sending invoice  
- [Send invoice via e-mail](#send-invoice-via-mail)
- [Mark invoice as sent via email](#mark-invoice-as-sent-via-email)
- [Send invoice via post](#send-invoice-via-post)
- [Mark invoice as sent](#mark-invoice-as-sent)

Delete invoice features  
- [Delete invoice item](#delete-invoice-item)
- [Delete invoice payment](#delete-invoice-payment)


## Add invoice

Create new invoice.
If you want to add tags to invoice, refer to [FAQ > How do I add tags to an entity?](faq.md#how-do-i-add-tags-to-an-entity)

### Request

**URL**: `/invoices/create`  
**HTTP method**: POST  

```sh

# minimal example
data='{
    "Invoice":{
        "name": "Test API"
    },
    "InvoiceItem":[
        {
            "description": "description of item 1",
            "name": "item 1",
            "tax": 20,
            "unit_price": 10
        }
    ],
    "Client":{
        "ico": "44981082"
    }
}';

# more complicate example
data='{
    "Invoice":{
        "name": "Test API",
        "bank_accounts": [
            {
                "bank_name": "New Bank",
                "iban": "SK0000000000000000",
                "swift": "12345"
            }
        ],
        "issued_by": "John Doe",
        "issued_by_email": "john@d.oe",
        "issued_by_phone": "+9999999",
        "issued_by_web": "https://superfaktura.sk",
        "created": "2019-01-01",
        "discount": 10,
        "header_comment": "Header comment",
        "internal_comment": "Internal comment",
        "invoice_currency": "NOK",
        "rounding": "item_ext",
        "specific": "123456",
        "type": "delivery",
        "variable": "VS87654"
    },
    "InvoiceItem":[
        {
            "description": "description of item 1",
            "name": "item 1",
            "tax": 20,
            "unit_price": 10
        }
    ],
    "Client":{
        "ico": "44981082",
        "comment": "Client comment",
        "update_addressbook": 1,
        "iban": "XX00000000001",
        "swift": "98765"
    }
}';


curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoices/create
```



Example with invoice data, invoice items, client, invoice extras, accounting details and invoice settings (full options specified):
```
data='{
  "Invoice":{
    "name": "Test API",
    "bank_accounts": [
      {
        "bank_name": "New Bank",
        "iban": "SK0000000000000000",
        "swift": "12345"
      }
    ],
    "issued_by": "John Doe",
    "issued_by_email": "john@d.oe",
    "issued_by_phone": "+9999999",
    "issued_by_web": "https://superfaktura.sk",
    "discount": 10,
    "header_comment": "Header comment",
    "internal_comment": "Internal comment",
    "invoice_currency": "EUR",
    "rounding": "item_ext",
    "specific": "123456",
    "type": "proforma",
    "variable": "VS87654",
    "created": "2019-02-28"
  },
  "InvoiceItem":[
    {
      "description": "description of item 1",
      "name": "item 1",
      "tax": 20,
      "unit_price": 10,
      "AccountingDetail": {
        "place": "Slovakia",
        "order": "PLA",
        "operation": "UXW",
        "type": "item",
        "analytics_account": "311",
        "synthetic_account": "000",
        "preconfidence": "5ZV"
      }
    }
  ],
  "Client":{
    "ico": "46655034",
    "comment": "Client comment",
    "update_addressbook": 1,
    "iban": "XX00000000001",
    "swift": "98765"
  },
  "InvoiceSetting": {
    "settings": "{\"language\":\"eng\",\"signature\":true,\"payment_info\":true,\"online_payment\": true,\"bysquare\": true,\"paypal\": true}"
  },
  "InvoiceExtra": {
    "pickup_point_id": 23
  },
  "MyData": {
    "address": "Fiktivna 1",
    "business_register": "-",
    "city": "Prague",
    "company_name": "MyData Inc.",
    "country_id": 191,
    "dic": "SK99999999",
    "ic_dph": "ABCDE",
    "update_profile": "0",
    "zip": "999 88"
  }
}';
```

### Attributes
#### Required

##### Client

| name      | type   | description  | default value |
| --------- | ------ | ------------ | ------------- |
| **name**  | string | client name  |               |

##### Invoice

none


##### InvoiceItem
At least one of `unit_price` and `name` must be filled and not empty.
At least one Invoice item must be specified.


#### Optional

##### Client

| name                        | type   | description  | default value |
| --------------------------- | ------ | ------------ | ------------- |
| **address**                 | string | address (street + number) | |
| **bank_account**            | string | bank account | |
| **city**                    | string | city | |
| **comment**                 | string | comment | |
| **country**                 | string | custom country name | |
| **country_id**              | int    | country ID (see [Value lists > Country list](value-lists.md#country-list)) | |
| **country_iso_id**          | string | country code ([ISO-3166-1 (Alpha-2)](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)) | |
| **delivery_address**        | string | delivery address (street + number) | |
| **delivery_city**           | string | delivery city | |
| **delivery_country**        | string | custom delivery country name | |
| **delivery_country_id**     | int    | delivery country ID (see [Value lists > Country list](value-lists.md#country-list)) | |
| **delivery_country_iso_id** | string | country code ([ISO-3166-1 (Alpha-2)](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)) | |
| **delivery_name**           | string | delivery country name | |
| **delivery_phone**          | string | delivery phone number | |
| **delivery_zip**            | string | delivery ZIP code | |
| **dic**                     | string | Tax ID (DIČ-sk) | |
| **email**                   | string | email | |
| **fax**                     | string | fax | |
| **iban**                    | string | IBAN | |
| **ic_dph**                  | string | VAT ID (IČ DPH🇸🇰, DIČ-cz) | |
| **ico**                     | string | ID (IČO) | |
| **match_address**           | int    | if this parameter is set, address is included in client searching | |
| **phone**                   | string | phone number | |
| **swift**                   | string | SWIFT code | |
| **update_addressbook**      | int    | update client data when invoice is issued? (0=no, 1=true) | |
| **zip**                     | string | ZIP code | |


In case of foreign client it is necessary to correctly fill `country_id`.
If `country_id` is empty, predefined value is used (SK version - Slovakia, CZ version - Czech republic).
To get `country_id` see [Value lists > Country list](value-lists.md#country-list).


##### Invoice

| name                     | type     | description  | default value |
| ------------------------ | -------- | ------------ | ------------- |
| **already_paid**         | int      | is invoice already paid (0=no, 1=yes) | |
| **bank_accounts**        | array    | list of bank accounts | |
| **comment**              | string   | comment | |
| **constant**             | string   | constant symbol | |
| **created**              | date     | issue date | |
| **delivery**             | date     | delivery date | |
| **delivery_type**        | string   | delivery type (see [Value lists > Delivery types](value-lists.md#delivery-types)) | |
| **deposit**              | float    | deposit paid | |
| **discount**             | float    | discount in percent | 0 |
| **discount_total**       | float    | nominal discount, is used only if `discount` is *not* set | |
| **due**                  | date     | due date | |
| **estimate_id**          | int      | estimate ID, based on which is invoice issued | |
| **header_comment**       | string   | comment above invoice items | |
| **internal_comment**     | string   | internal comment - will not be displayed on invoice | |
| **invoice_currency**     | string   | currency (see [Value lists > Currencies](value-lists.md#currencies)) | |
| **invoice_no_formatted** | string   | invoice number | |
| **issued_by**            | string   | who issued invoice (person)| |
| **issued_by_email**      | string   | who issued invoice (email) | |
| **issued_by_phone**      | string   | who issued invoice (phone) | |
| **issued_by_web**        | string   | website displayed on invoice | |
| **logo_id**              | int      | logo ID | |
| **mark_sent**            | int      | mark invoice as sent via email (0=no, 1=yes) | |
| **mark_sent_message**    | string   | set mail message for _mark_sent_ flag | |
| **mark_sent_subject**    | string   | set mail subject for _mark_sent_ flag | |
| **name**                 | string   | invoice name | |
| **order_no**             | string   | order number | |
| **parent_id**            | int      | invoice ID, that we want to cancel | |
| **paydate**              | datetime | payment date (if set together with `already_paid=1`, the set date will be used) | |
| **payment_type**         | string   | payment type (see [Value lists > Payment types](value-lists.md#payment-types))| |
| **proforma_id**          | string   | proforma invoice ID, based on which regular invoice is issued. Invoice will get information about paid invoice | |
| **rounding**             | string   | rounding type (see [Value lists > Rounding types](value-lists.md#rounding-types)) | |
| **sequence_id**          | int      | sequence ID (see [Value lists > Sequences](value-lists.md#sequences)) | |
| **specific**             | string   | specific symbol | |
| **tax_document**         | int      | is there a receipt? (for correct connection with proforma invoice is necessary to fill `proforma_id`) (0=no, 1=yes) | |
| **type**                 | string   | invoice type (see [Value lists > Invoice types](value-lists.md#invoice-types)) | |
| **variable**             | string   | variable symbol (if left empty, invoice number will be used) | |


##### InvoiceItem

| name                      | type   | description  | default value |
| ------------------------- | ------ | ------------ | ------------- |
| **description**           | string | invoice item description - will be displayed on invoice | |
| **discount**              | float  | discount in percent | 0 |
| **discount_description**  | string | discount description | |
| **load_data_from_stock**  | int    | load data from stock? (0=no, 1=yes) | 0 |
| **name**                  | string | item name | |
| **quantity**              | float  | quantity | 1 |
| **sku**                   | string | stock number | |
| **stock_item_id**         | int    | 123 | |
| **tax**                   | float  | VAT (if you are not a tax payer, use 0) | |
| **unit**                  | string | unit (e.g. m, l, hour) | |
| **unit_price**            | float  | price without VAT (or full price, if you are not a tax payer) | 0 |
| **use_document_currency** | int    | convert stock item to invoice currency (1 = enabled, 0 = disabled) | |


###### AccountingDetail

| name                  | type   | description                                     | default value |
| --------------------- | ------ | ----------------------------------------------- | ------------- |
| **analytics_account** | string | analytics account                               |               |
| **operation**         | string | operation                                       |               |
| **order**             | string | order name                                      |               |
| **place**             | string | place name                                      |               |
| **preconfidence**     | string | preconfidence                                   |               |
| **synthetic_account** | string | synthetic account                               |               |
| **type**              | string | item type (`item` (goods), `service` (service)) |               |



##### MyData

| name                     | type   | description                               | default value |
| ------------------------ | ------ | ----------------------------------------- | ------------- |
| **address**              | string | my address                                | |
| **business_register**    | string | business register                         | |
| **city**                 | string | my city                                   | |
| **company_name**         | string | my company name                           | |
| **country_id**           | string | country ID (see [Value lists > Country list](value-lists.md#country-list)) | |
| **dic**                  | string | tax ID (DIČ-sk)                           | |
| **ic_dph**               | string | VAT ID (IČ DPH🇸🇰, DIČ-cz)                | |
| **update_profile**       | int    | should profile be updated with these data | |
| **zip**                  | string | ZIP code                                  | |



##### InvoiceSettings

| name                 | type   | description                                                                                                     | default value |
| -------------------- | ------ | --------------------------------------------------------------------------------------------------------------- | ------------- |
| **bysquare**         | bool   | show pay by square                                                                                              |               |
| **callback_payment** | string | URL, which will be automatically called after adding payment to the invoice. GET parameter `invoice_id` will be appended to the URL. If you send URL `https://example.com/callback/`, the callback URL for invoice_id 123 will be `https://example.com/callback/?invoice_id=123` or `https://example.com/callback/?invoice_id=123&secret_key={KEY}`. Parameter `secret_key` can be part of sent URL (`https://example.com/callback/?secret_key=SECRET-KEY`) or set in your profile. |               |
| **language**         | string | invoice language  (for list of possible values see [Value lists > Language list](value-lists.md#language-list)) |               |
| **online_payment**   | bool   | show online payments                                                                                            |               |
| **payment_info**     | bool   | show payment information                                                                                        |               |
| **paypal**           | bool   | show PayPal                                                                                                     |               |
| **show_prices**      | bool   | show prices (only effective for delivery)                                                                       |               |
| **signature**        | bool   | show signature                                                                                                  |               |


##### InvoiceExtras

| name                    | type   | description                          | default value |
| ----------------------- | ------ | ------------------------------------ | ------------- |
| **custom_payment_link** | string | Sets custom link for payment button. Is prioritized over other options (e.g. Barion, Besteron) Automatically enables online payments for invoice. This behavior can be disabled by sending `online_payment: false` in [`InvoiceSettings`](#invoicesettings) | |
| **dimension**           | string | package dimensions in cm (l x w x h) |               |
| **insurance**           | float  | insurance price                      |               |
| **oss**                 | bool   | one-stop shop                        |               |
| **parcel_count**        | int    | number of packages                   |               |
| **pickup_point_id**     | int    | pickup point ID for Zásielkovňa      |               |
| **tracking_number**     | string | tracking number                      |               |
| **weight**              | float  | package weight                       |               |


### Response

#### Successful addition
```json
{
  "data": {
    "0": {
      "to_pay": "10.800000",
      "to_pay_in_invoice_currency": "10.80",
      "total": "10.80"
    },
    "Client": {
      "account": null,
      "address": "Pri Suchom mlyne 6",
      "bank_account": "",
      "bank_account_id": "0",
      "bank_account_prefix": null,
      "bank_code": "",
      "city": "Bratislava - mestská časť Staré Mesto",
      "comment": "Client comment",
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
      "iban": "XX00000000001",
      "ic_dph": "SK2023513470",
      "ico": "46655034",
      "id": "3",
      "modified": "2050-01-01 23:59:59",
      "name": "SuperFaktura, s.r.o.",
      "notices": true,
      "phone": "",
      "state": "",
      "swift": "98765",
      "tags": null,
      "user_id": "1",
      "user_profile_id": "1",
      "uuid": null,
      "zip": "811 04"
    },
    "ClientData": {
      "Country": {
        "eu": true,
        "id": "191",
        "iso": "sk",
        "name": "Slovensko"
      },
      "DeliveryCountry": {
        "eu": true,
        "id": "191",
        "iso": "sk",
        "name": "Slovensko"
      },
      "account": null,
      "address": "Pri Suchom mlyne 6",
      "bank_account": "",
      "bank_account_id": "0",
      "bank_account_prefix": null,
      "bank_code": "",
      "city": "Bratislava - mestská časť Staré Mesto",
      "comment": "Client comment",
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
      "iban": "XX00000000001",
      "ic_dph": "SK2023513470",
      "ico": "46655034",
      "id": "3",
      "modified": "2050-01-01 23:59:59",
      "name": "SuperFaktura, s.r.o.",
      "notices": true,
      "phone": "",
      "state": "",
      "swift": "98765",
      "tags": null,
      "user_id": "1",
      "user_profile_id": "1",
      "uuid": null,
      "zip": "811 04"
    },
    "Invoice": {
      "accounting_date": "2050-01-01",
      "amount": "9.00",
      "amount_paid": "0.00",
      "client_data": "{\"Client\":{\"id\":\"3\",\"user_id\":\"1\",\"user_profile_id\":\"1\",\"uuid\":null,\"country_id\":\"191\",\"name\":\"SuperFaktura, s.r.o.\",\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"iban\":\"XX00000000001\",\"swift\":\"98765\",\"bank_account_prefix\":null,\"bank_account\":\"\",\"bank_code\":\"\",\"account\":null,\"email\":\"\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"state\":\"\",\"country\":\"Slovensko\",\"delivery_name\":\"\",\"delivery_address\":\"\",\"delivery_city\":\"\",\"delivery_zip\":\"\",\"delivery_state\":\"\",\"delivery_country\":\"Slovensko\",\"delivery_country_id\":\"191\",\"phone\":\"\",\"delivery_phone\":\"\",\"fax\":\"\",\"due_date\":null,\"default_variable\":\"\",\"discount\":null,\"currency\":null,\"bank_account_id\":\"0\",\"comment\":\"Client comment\",\"tags\":null,\"distance\":null,\"dont_travel\":null,\"created\":\"2050-01-01 23:59:59\",\"modified\":\"2050-01-01 23:59:59\",\"notices\":true}}",
      "client_id": "3",
      "comment": "",
      "constant": "",
      "country_exchange_rate": "1.00000000000000",
      "created": "2050-01-01 23:59:59",
      "delivery": null,
      "delivery_type": "",
      "demo": "0",
      "deposit": "0.00",
      "discount": "10",
      "due": "2050-01-01",
      "estimate_id": null,
      "exchange_rate": 1,
      "flag": "due",
      "header_comment": "Header comment",
      "home_currency": "EUR",
      "id": "2",
      "import_id": null,
      "import_parent_id": null,
      "import_type": null,
      "internal_comment": "Internal comment",
      "invoice_currency": "EUR",
      "invoice_no": "1",
      "invoice_no_formatted": "ZAL12019001",
      "invoice_no_formatted_length": "11",
      "invoice_no_formatted_raw": "12019001",
      "issued_by": "John Doe",
      "issued_by_email": "john@d.oe",
      "issued_by_phone": " 9999999",
      "issued_by_web": "https://superfaktura.sk",
      "items_data": "item 1 description of item 1, ",
      "items_name": null,
      "lang": null,
      "mask": "YYYYNNN",
      "modified": "2050-01-01 23:59:59",
      "my_data": "{\"MyData\":{\"id\":\"1\",\"user_id\":\"1\",\"country_id\":191,\"company_name\":\"MyData Inc.\",\"address\":\"Fiktivna 1\",\"city\":\"Prague\",\"zip\":\"999 88\",\"ico\":\"46655034\",\"dic\":\"SK99999999\",\"ic_dph\":\"ABCDE\",\"tax_payer\":\"1\",\"country\":\"Slovensko\",\"BankAccount\":[{\"bank_name\":\"New Bank\",\"iban\":\"SK0000000000000000\",\"swift\":\"12345\",\"show_account\":true,\"country_id\":\"\",\"account\":\"\",\"bank_code\":\"\"}],\"Logo\":\"[{\\\"id\\\":\\\"1\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"1\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"4311c1895aa334d39ac8_1_exads_logo_rgb.png\\\",\\\"checksum\\\":\\\"a1dcdc392d08d6d1caaf148225f2a7d4\\\",\\\"group\\\":\\\"logo\\\",\\\"default\\\":true,\\\"alternative\\\":null,\\\"size\\\":\\\"49743\\\",\\\"extern_file\\\":\\\"0\\\",\\\"delete_flag\\\":false,\\\"created\\\":\\\"2050-01-01 23:59:59\\\",\\\"modified\\\":\\\"2050-01-01 23:59:59\\\",\\\"path\\\":\\\"img\\\\\\/4311c1895aa334d39ac8_1_exads_logo_rgb.png\\\"}]\",\"Signature\":\"{\\\"id\\\":\\\"2\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"1\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"9b7c9830cb6b6afa7b16_1_podpis_1.png\\\",\\\"checksum\\\":\\\"33b5238616646ca28ebabc02f713a59f\\\",\\\"group\\\":\\\"signature\\\",\\\"default\\\":false,\\\"alternative\\\":null,\\\"size\\\":\\\"2689\\\",\\\"extern_file\\\":\\\"0\\\",\\\"delete_flag\\\":false,\\\"created\\\":\\\"2050-01-01 23:59:59\\\",\\\"modified\\\":\\\"2050-01-01 23:59:59\\\",\\\"path\\\":\\\"img\\\\\\/9b7c9830cb6b6afa7b16_1_podpis_1.png\\\"}\",\"business_register\":\"-\"}}",
      "name": "Test API",
      "order_no": null,
      "paid": "0.00",
      "parent_id": null,
      "paydate": null,
      "payment_type": null,
      "proforma_id": null,
      "recurring": null,
      "rounding": "item_ext",
      "sequence_id": "2",
      "show_items_with_dph": true,
      "show_special_vat": false,
      "special_vat_scheme": null,
      "specific": "123456",
      "status": "1",
      "summary_invoice": null,
      "tags": null,
      "tax_document": null,
      "taxdate": null,
      "token": "c3b05c50",
      "type": "proforma",
      "user_id": "1",
      "user_profile_id": "1",
      "variable": "VS87654",
      "variable_raw": "VS87654",
      "vat": "1.80",
      "vat_transfer": null
    },
    "InvoiceEmail": [],
    "InvoiceExtra": {
      "pickup_point_id": "23"
    },
    "InvoiceItem": [
      {
        "AccountingDetail": {
          "analytics_account": "311",
          "document_id": "2",
          "document_item_id": "2",
          "id": "1",
          "item_type": "invoice",
          "operation": "UXW",
          "order": "PLA",
          "place": "Slovakia",
          "preconfidence": "5ZV",
          "synthetic_account": "000",
          "type": "item",
          "user_profile_id": "1"
        },
        "description": "description of item 1",
        "discount": 0,
        "discount_description": "",
        "discount_no_vat": 0,
        "discount_no_vat_total": 0,
        "discount_with_vat": 0,
        "discount_with_vat_total": 0,
        "hide_in_autocomplete": null,
        "id": "2",
        "invoice_id": "2",
        "item_price": 10,
        "item_price_no_discount": 10,
        "item_price_vat": 12,
        "item_price_vat_no_discount": 12,
        "name": "item 1",
        "ordernum": "0",
        "quantity": null,
        "sku": null,
        "stock_item_id": null,
        "tax": 20,
        "tax_deposit": null,
        "unit": "",
        "unit_price": 10,
        "unit_price_discount": 10,
        "unit_price_vat": 12,
        "unit_price_vat_no_discount": 12,
        "user_id": "1",
        "user_profile_id": "1"
      }
    ],
    "InvoicePayment": [],
    "InvoiceSetting": {
      "bysquare": true,
      "language": "eng",
      "online_payment": true,
      "payment_info": true,
      "paypal": true,
      "signature": true
    },
    "Logo": [
      {
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
        "mobile_path": "",
        "model": "User",
        "modified": "2050-01-01 23:59:59",
        "path": "img/4311c1895aa334d39ac8_1_exads_logo_rgb.png",
        "size": "49743"
      }
    ],
    "MyData": {
      "BankAccount": [
        {
          "account": "",
          "bank_code": "",
          "bank_name": "New Bank",
          "country_id": "",
          "iban": "SK0000000000000000",
          "show_account": true,
          "swift": "12345"
        }
      ],
      "Logo": "[{\"id\":\"1\",\"model\":\"User\",\"foreign_key\":\"1\",\"dirname\":\"img\",\"basename\":\"4311c1895aa334d39ac8_1_exads_logo_rgb.png\",\"checksum\":\"a1dcdc392d08d6d1caaf148225f2a7d4\",\"group\":\"logo\",\"default\":true,\"alternative\":null,\"size\":\"49743\",\"extern_file\":\"0\",\"delete_flag\":false,\"created\":\"2050-01-01 23:59:59\",\"modified\":\"2050-01-01 23:59:59\",\"path\":\"img\\/4311c1895aa334d39ac8_1_exads_logo_rgb.png\",\"mobile_path\":\"\"}]",
      "LogoRaw": [
        {
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
          "mobile_path": "",
          "model": "User",
          "modified": "2050-01-01 23:59:59",
          "path": "img/4311c1895aa334d39ac8_1_exads_logo_rgb.png",
          "size": "49743"
        }
      ],
      "Signature": "{\"id\":\"2\",\"model\":\"User\",\"foreign_key\":\"1\",\"dirname\":\"img\",\"basename\":\"9b7c9830cb6b6afa7b16_1_podpis_1.png\",\"checksum\":\"33b5238616646ca28ebabc02f713a59f\",\"group\":\"signature\",\"default\":false,\"alternative\":null,\"size\":\"2689\",\"extern_file\":\"0\",\"delete_flag\":false,\"created\":\"2050-01-01 23:59:59\",\"modified\":\"2050-01-01 23:59:59\",\"path\":\"img\\/9b7c9830cb6b6afa7b16_1_podpis_1.png\"}",
      "SignatureRaw": {
        "alternative": null,
        "basename": "9b7c9830cb6b6afa7b16_1_podpis_1.png",
        "checksum": "33b5238616646ca28ebabc02f713a59f",
        "created": "2050-01-01 23:59:59",
        "default": false,
        "delete_flag": false,
        "dirname": "img",
        "extern_file": "0",
        "foreign_key": "1",
        "group": "signature",
        "id": "2",
        "model": "User",
        "modified": "2050-01-01 23:59:59",
        "path": "img/9b7c9830cb6b6afa7b16_1_podpis_1.png",
        "size": "2689"
      },
      "address": "Fiktivna 1",
      "business_register": "-",
      "city": "Prague",
      "company_name": "MyData Inc.",
      "country": {
        "eu": true,
        "id": "191",
        "iso": "sk",
        "name": "Slovensko"
      },
      "country_id": 191,
      "dic": "SK99999999",
      "ic_dph": "ABCDE",
      "ico": "46655034",
      "id": "1",
      "tax_payer": "1",
      "user_id": "1",
      "zip": "999 88"
    },
    "PaymentLink": "",
    "Paypal": false,
    "PostStamp": [],
    "RelatedItems": [],
    "Signature": {
      "alternative": null,
      "basename": "9b7c9830cb6b6afa7b16_1_podpis_1.png",
      "checksum": "33b5238616646ca28ebabc02f713a59f",
      "created": "2050-01-01 23:59:59",
      "default": false,
      "delete_flag": false,
      "dirname": "img",
      "extern_file": "0",
      "foreign_key": "1",
      "group": "signature",
      "id": "2",
      "model": "User",
      "modified": "2050-01-01 23:59:59",
      "path": "img/9b7c9830cb6b6afa7b16_1_podpis_1.png",
      "size": "2689"
    },
    "Summary": {
      "discount": 1.2,
      "invoice_total": 10.8,
      "vat_base_separate": {
        "20": 9
      },
      "vat_base_total": 9,
      "vat_separate": {
        "20": 1.8
      },
      "vat_total": 1.8
    },
    "SummaryInvoice": {
      "vat_base_separate_negative": {
        "20": 0
      },
      "vat_base_separate_positive": {
        "20": 9
      },
      "vat_separate_negative": {
        "20": 0
      },
      "vat_separate_positive": {
        "20": 1.8
      }
    },
    "Tag": [],
    "UnitCount": []
  },
  "error": 0,
  "error_message": "Invoice created"
}
```

#### Insufficient privileges
HTTP status 403.

```json
{
  "error": 1,
  "error_message": "You can't create invoice",
  "message": "You can't create invoice"
}
```

#### Missing required data
```json
{
  "error": 4,
  "error_message": {
    "data_bad_format": "Missing required client data."
  }
}
```

#### Missing data
```json
{
  "error": 4,
  "error_message": {
    "data_bad_format": "Missing required client data."
  }
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


## Edit invoice

Edit invoice.
If you want to add tags to invoice, refer to [FAQ > How do I add tags to an entity?](faq.md#how-do-i-add-tags-to-an-entity).

### Request

**URL**: `/invoices/edit`  
**HTTP method**: POST  

```sh
data='{
    "Invoice": {
        "id": 2,
        "discount": 5
    }
}';

curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoices/edit
```

### Attributes
#### Required

##### Invoice

| name   | type | description                       | default value |
| ------ | ---- | --------------------------------- | ------------- |
| **id** | int  | ID of invoice that will be edited |               |

#### Optional

Same as for **Add invoice**. With the exception of *name* being optional.

### Response

#### Successfully edited
```json
{
  "data": {
    "0": {
      "to_pay": "11.400000",
      "to_pay_in_invoice_currency": "11.40",
      "total": "11.40"
    },
    "Client": {
      "account": null,
      "address": "Pri Suchom mlyne 6",
      "bank_account": "",
      "bank_account_id": "0",
      "bank_account_prefix": null,
      "bank_code": "",
      "city": "Bratislava - mestská časť Staré Mesto",
      "comment": "Client comment",
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
      "iban": "XX00000000001",
      "ic_dph": "SK2023513470",
      "ico": "46655034",
      "id": "3",
      "modified": "2050-01-01 23:59:59",
      "name": "SuperFaktura, s.r.o.",
      "notices": true,
      "phone": "",
      "state": "",
      "swift": "98765",
      "tags": null,
      "user_id": "1",
      "user_profile_id": "1",
      "uuid": null,
      "zip": "811 04"
    },
    "ClientData": {
      "Country": {
        "eu": true,
        "id": "191",
        "iso": "sk",
        "name": "Slovensko"
      },
      "DeliveryCountry": {
        "eu": true,
        "id": "191",
        "iso": "sk",
        "name": "Slovensko"
      },
      "account": null,
      "address": "Pri Suchom mlyne 6",
      "bank_account": "",
      "bank_account_id": "0",
      "bank_account_prefix": null,
      "bank_code": "",
      "city": "Bratislava - mestská časť Staré Mesto",
      "comment": "Client comment",
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
      "iban": "XX00000000001",
      "ic_dph": "SK2023513470",
      "ico": "46655034",
      "id": "3",
      "modified": "2050-01-01 23:59:59",
      "name": "SuperFaktura, s.r.o.",
      "notices": true,
      "phone": "",
      "state": "",
      "swift": "98765",
      "tags": null,
      "user_id": "1",
      "user_profile_id": "1",
      "uuid": null,
      "zip": "811 04"
    },
    "Invoice": {
      "accounting_date": "2050-01-01",
      "amount": "9.50",
      "amount_paid": "0.00",
      "client_data": "{\"id\":\"3\",\"user_id\":\"1\",\"user_profile_id\":\"1\",\"uuid\":null,\"country_id\":\"191\",\"name\":\"SuperFaktura, s.r.o.\",\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"iban\":\"XX00000000001\",\"swift\":\"98765\",\"bank_account_prefix\":null,\"bank_account\":\"\",\"bank_code\":\"\",\"account\":null,\"email\":\"\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"state\":\"\",\"country\":\"Slovensko\",\"delivery_name\":\"\",\"delivery_address\":\"\",\"delivery_city\":\"\",\"delivery_zip\":\"\",\"delivery_state\":\"\",\"delivery_country\":\"Slovensko\",\"delivery_country_id\":\"191\",\"phone\":\"\",\"delivery_phone\":\"\",\"fax\":\"\",\"due_date\":null,\"default_variable\":\"\",\"discount\":null,\"currency\":null,\"bank_account_id\":\"0\",\"comment\":\"Client comment\",\"tags\":null,\"distance\":null,\"dont_travel\":null,\"created\":\"2050-01-01 23:59:59\",\"modified\":\"2050-01-01 23:59:59\",\"notices\":true,\"Client\":{\"id\":\"3\",\"user_id\":\"1\",\"user_profile_id\":\"1\",\"uuid\":null,\"country_id\":\"191\",\"name\":\"SuperFaktura, s.r.o.\",\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"iban\":\"XX00000000001\",\"swift\":\"98765\",\"bank_account_prefix\":null,\"bank_account\":\"\",\"bank_code\":\"\",\"account\":null,\"email\":\"\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"state\":\"\",\"country\":\"Slovensko\",\"delivery_name\":\"\",\"delivery_address\":\"\",\"delivery_city\":\"\",\"delivery_zip\":\"\",\"delivery_state\":\"\",\"delivery_country\":\"Slovensko\",\"delivery_country_id\":\"191\",\"phone\":\"\",\"delivery_phone\":\"\",\"fax\":\"\",\"due_date\":null,\"default_variable\":\"\",\"discount\":null,\"currency\":null,\"bank_account_id\":\"0\",\"comment\":\"Client comment\",\"tags\":null,\"distance\":null,\"dont_travel\":null,\"created\":\"2050-01-01 23:59:59\",\"modified\":\"2050-01-01 23:59:59\",\"notices\":true}}",
      "client_id": "3",
      "comment": "",
      "constant": "",
      "country_exchange_rate": "1.00000000000000",
      "created": "2050-01-01 23:59:59",
      "delivery": null,
      "delivery_type": "",
      "demo": "0",
      "deposit": "0.00",
      "discount": "5",
      "due": "2050-01-01",
      "estimate_id": null,
      "exchange_rate": 1,
      "flag": "due",
      "header_comment": "Header comment",
      "home_currency": "EUR",
      "id": "2",
      "import_id": null,
      "import_parent_id": null,
      "import_type": null,
      "internal_comment": "Internal comment",
      "invoice_currency": "EUR",
      "invoice_no": "1",
      "invoice_no_formatted": "ZAL12019001",
      "invoice_no_formatted_length": "11",
      "invoice_no_formatted_raw": "12019001",
      "issued_by": "John Doe",
      "issued_by_email": "john@d.oe",
      "issued_by_phone": " 9999999",
      "issued_by_web": "https://superfaktura.sk",
      "items_data": "item 1 description of item 1, ",
      "items_name": null,
      "lang": null,
      "mask": "YYYYNNN",
      "modified": "2050-01-01 23:59:59",
      "my_data": "{\"MyData\":{\"id\":\"1\",\"user_id\":\"1\",\"country_id\":191,\"company_name\":\"MyData Inc.\",\"address\":\"Fiktivna 1\",\"city\":\"Prague\",\"zip\":\"999 88\",\"ico\":\"46655034\",\"dic\":\"SK99999999\",\"ic_dph\":\"ABCDE\",\"tax_payer\":\"1\",\"country\":\"Slovensko\",\"BankAccount\":[{\"bank_name\":\"New Bank\",\"iban\":\"SK0000000000000000\",\"swift\":\"12345\",\"show_account\":true,\"country_id\":\"\",\"account\":\"\",\"bank_code\":\"\"}],\"Logo\":\"[{\\\"id\\\":\\\"1\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"1\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"4311c1895aa334d39ac8_1_exads_logo_rgb.png\\\",\\\"checksum\\\":\\\"a1dcdc392d08d6d1caaf148225f2a7d4\\\",\\\"group\\\":\\\"logo\\\",\\\"default\\\":true,\\\"alternative\\\":null,\\\"size\\\":\\\"49743\\\",\\\"extern_file\\\":\\\"0\\\",\\\"delete_flag\\\":false,\\\"created\\\":\\\"2050-01-01 23:59:59\\\",\\\"modified\\\":\\\"2050-01-01 23:59:59\\\",\\\"path\\\":\\\"img\\\\\\/4311c1895aa334d39ac8_1_exads_logo_rgb.png\\\"}]\",\"Signature\":\"{\\\"id\\\":\\\"2\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"1\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"9b7c9830cb6b6afa7b16_1_podpis_1.png\\\",\\\"checksum\\\":\\\"33b5238616646ca28ebabc02f713a59f\\\",\\\"group\\\":\\\"signature\\\",\\\"default\\\":false,\\\"alternative\\\":null,\\\"size\\\":\\\"2689\\\",\\\"extern_file\\\":\\\"0\\\",\\\"delete_flag\\\":false,\\\"created\\\":\\\"2050-01-01 23:59:59\\\",\\\"modified\\\":\\\"2050-01-01 23:59:59\\\",\\\"path\\\":\\\"img\\\\\\/9b7c9830cb6b6afa7b16_1_podpis_1.png\\\"}\",\"business_register\":\"-\"}}",
      "name": "Test API",
      "order_no": null,
      "paid": "0.00",
      "parent_id": null,
      "paydate": null,
      "payment_type": null,
      "proforma_id": null,
      "recurring": null,
      "rounding": "item_ext",
      "sequence_id": "2",
      "show_items_with_dph": true,
      "show_special_vat": false,
      "special_vat_scheme": null,
      "specific": "123456",
      "status": "1",
      "summary_invoice": null,
      "tags": "",
      "tax_document": null,
      "taxdate": null,
      "token": "c3b05c50",
      "type": "proforma",
      "user_id": "1",
      "user_profile_id": "1",
      "variable": "VS87654",
      "variable_raw": "VS87654",
      "vat": "1.90",
      "vat_transfer": null
    },
    "InvoiceEmail": [],
    "InvoiceExtra": {
      "pickup_point_id": "23"
    },
    "InvoiceItem": [
      {
        "AccountingDetail": {
          "analytics_account": "311",
          "document_id": "2",
          "document_item_id": "2",
          "id": "1",
          "item_type": "invoice",
          "operation": "UXW",
          "order": "PLA",
          "place": "Slovakia",
          "preconfidence": "5ZV",
          "synthetic_account": "000",
          "type": "item",
          "user_profile_id": "1"
        },
        "description": "description of item 1",
        "discount": 0,
        "discount_description": "",
        "discount_no_vat": 0,
        "discount_no_vat_total": 0,
        "discount_with_vat": 0,
        "discount_with_vat_total": 0,
        "hide_in_autocomplete": null,
        "id": "2",
        "invoice_id": "2",
        "item_price": 10,
        "item_price_no_discount": 10,
        "item_price_vat": 12,
        "item_price_vat_no_discount": 12,
        "name": "item 1",
        "ordernum": "0",
        "quantity": null,
        "sku": null,
        "stock_item_id": null,
        "tax": 20,
        "tax_deposit": null,
        "unit": "",
        "unit_price": 10,
        "unit_price_discount": 10,
        "unit_price_vat": 12,
        "unit_price_vat_no_discount": 12,
        "user_id": "1",
        "user_profile_id": "1"
      }
    ],
    "InvoicePayment": [],
    "InvoiceSetting": {
      "bysquare": true,
      "language": "eng",
      "online_payment": true,
      "payment_info": true,
      "paypal": true,
      "signature": true
    },
    "Logo": [
      {
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
        "mobile_path": "",
        "model": "User",
        "modified": "2050-01-01 23:59:59",
        "path": "img/4311c1895aa334d39ac8_1_exads_logo_rgb.png",
        "size": "49743"
      }
    ],
    "MyData": {
      "BankAccount": [
        {
          "account": "",
          "bank_code": "",
          "bank_name": "New Bank",
          "country_id": "",
          "iban": "SK0000000000000000",
          "show_account": true,
          "swift": "12345"
        }
      ],
      "Logo": "[{\"id\":\"1\",\"model\":\"User\",\"foreign_key\":\"1\",\"dirname\":\"img\",\"basename\":\"4311c1895aa334d39ac8_1_exads_logo_rgb.png\",\"checksum\":\"a1dcdc392d08d6d1caaf148225f2a7d4\",\"group\":\"logo\",\"default\":true,\"alternative\":null,\"size\":\"49743\",\"extern_file\":\"0\",\"delete_flag\":false,\"created\":\"2050-01-01 23:59:59\",\"modified\":\"2050-01-01 23:59:59\",\"path\":\"img\\/4311c1895aa334d39ac8_1_exads_logo_rgb.png\",\"mobile_path\":\"\"}]",
      "LogoRaw": [
        {
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
          "mobile_path": "",
          "model": "User",
          "modified": "2050-01-01 23:59:59",
          "path": "img/4311c1895aa334d39ac8_1_exads_logo_rgb.png",
          "size": "49743"
        }
      ],
      "Signature": "{\"id\":\"2\",\"model\":\"User\",\"foreign_key\":\"1\",\"dirname\":\"img\",\"basename\":\"9b7c9830cb6b6afa7b16_1_podpis_1.png\",\"checksum\":\"33b5238616646ca28ebabc02f713a59f\",\"group\":\"signature\",\"default\":false,\"alternative\":null,\"size\":\"2689\",\"extern_file\":\"0\",\"delete_flag\":false,\"created\":\"2050-01-01 23:59:59\",\"modified\":\"2050-01-01 23:59:59\",\"path\":\"img\\/9b7c9830cb6b6afa7b16_1_podpis_1.png\"}",
      "SignatureRaw": {
        "alternative": null,
        "basename": "9b7c9830cb6b6afa7b16_1_podpis_1.png",
        "checksum": "33b5238616646ca28ebabc02f713a59f",
        "created": "2050-01-01 23:59:59",
        "default": false,
        "delete_flag": false,
        "dirname": "img",
        "extern_file": "0",
        "foreign_key": "1",
        "group": "signature",
        "id": "2",
        "model": "User",
        "modified": "2050-01-01 23:59:59",
        "path": "img/9b7c9830cb6b6afa7b16_1_podpis_1.png",
        "size": "2689"
      },
      "address": "Fiktivna 1",
      "business_register": "-",
      "city": "Prague",
      "company_name": "MyData Inc.",
      "country": {
        "eu": true,
        "id": "191",
        "iso": "sk",
        "name": "Slovensko"
      },
      "country_id": 191,
      "dic": "SK99999999",
      "ic_dph": "ABCDE",
      "ico": "46655034",
      "id": "1",
      "tax_payer": "1",
      "user_id": "1",
      "zip": "999 88"
    },
    "Paypal": false,
    "PostStamp": [],
    "RelatedItems": [],
    "Signature": {
      "alternative": null,
      "basename": "9b7c9830cb6b6afa7b16_1_podpis_1.png",
      "checksum": "33b5238616646ca28ebabc02f713a59f",
      "created": "2050-01-01 23:59:59",
      "default": false,
      "delete_flag": false,
      "dirname": "img",
      "extern_file": "0",
      "foreign_key": "1",
      "group": "signature",
      "id": "2",
      "model": "User",
      "modified": "2050-01-01 23:59:59",
      "path": "img/9b7c9830cb6b6afa7b16_1_podpis_1.png",
      "size": "2689"
    },
    "Summary": {
      "discount": 0.6,
      "invoice_total": 11.4,
      "vat_base_separate": {
        "20": 9.5
      },
      "vat_base_total": 9.5,
      "vat_separate": {
        "20": 1.9
      },
      "vat_total": 1.9
    },
    "SummaryInvoice": {
      "vat_base_separate_negative": {
        "20": 0
      },
      "vat_base_separate_positive": {
        "20": 9.5
      },
      "vat_separate_negative": {
        "20": 0
      },
      "vat_separate_positive": {
        "20": 1.9
      }
    },
    "Tag": [],
    "UnitCount": []
  },
  "status": true
}
```

#### Wrong invoice
```json
{
  "error": 2,
  "message": "Invoice ID not found."
}
```

#### Wrong ID format
```json
{
  "error": 1,
  "message": "Bad data format."
}
```

#### Bad data
```json
{
  "error": 1,
  "message": "Bad data format."
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Set invoice language

Sets invoice language

### Request
**URL**: `/invoices/setinvoicelanguage/{INVOICE_ID}/lang:{LANG}`  
**HTTP method**: GET  

```
curl -X GET \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
    https://moja.superfaktura.sk/invoices/setinvoicelanguage/1/lang:deu
```


### Attributes
#### Required

| name           | type   | description | default value |
| -------------- | ------ | ----------- | ------------- |
| **invoice_id** | int    | invoice ID | |
| **lang**       | string | invoice language (for list of possible values see [Value lists > Language list](value-lists.md#language-list)) | |

#### Optional
none


### Response
#### Successfully changed language

```json
{
  "message": "Success",
  "status": 1
}
```

#### Invalid language
```json
{
  "message": "Language is not supported.",
  "status": 0
}
```

#### Insufficient permissions
```json
{
  "message": "Permission denied.",
  "status": 0
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Get invoice PDF

Return invoice PDF file.

### Request
**URL**: `/[{LANGUAGE}/]invoices/pdf/{INVOICE_ID}/token:{TOKEN}`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    -o /tmp/faktura1275.pdf \
    https://moja.superfaktura.sk/slo/invoices/pdf/1275/token:09feb1bd
```    

### Attributes

#### Required
URL parameters:

| name              | type   | description   | default value |
| ----------------- | ------ | ------------- | ------------- | 
| **invoice_id**    | int    | invoice ID    |               |
| **token**         | string | invoice token |               |

#### Optional
URL parameters:  

| name              | type   | description | default value |
| ----------------- | ------ | ----------- | ------------- |
| **language**      | string | language in which the invoice will be created | as set by `pdf_language` (language of document - language above invoice detail in web application) |

For list of available languages see [Value lists > Language list](value-lists.md#language-list).


### Response  
PDF document on success.
Check for HTTP code 404 in case of error.


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Get invoice detail

Get invoice details.

### Request
**URL**: `/invoices/view/{INVOICE_ID}.json`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoices/view/1.json
```

### Attributes
#### Required
URL parameters:

| name           | type | description | default value |
| -------------- | ---- | ----------- | ------------- |
| **invoice_id** | int  | invoice ID  |               |

#### Optional
none

### Response

#### Success
```json
{
  "0": {
    "to_pay": "12.000000",
    "to_pay_in_invoice_currency": "12.00",
    "total": "12.00"
  },
  "Client": {
    "Country": {
      "eu": true,
      "id": "191",
      "iso": "sk",
      "name": "Slovensko"
    },
    "DeliveryCountry": {
      "eu": true,
      "id": "191",
      "iso": "sk",
      "name": "Slovensko"
    },
    "address": "Vymyslena 1",
    "city": "Bratislava",
    "country": "Slovensko",
    "country_id": "191",
    "delivery_address": "",
    "delivery_city": "",
    "delivery_country": "Slovensko",
    "delivery_country_id": "191",
    "delivery_name": "",
    "delivery_phone": "",
    "delivery_state": "",
    "delivery_zip": "",
    "dic": "123456",
    "email": "",
    "fax": "",
    "ic_dph": "",
    "ico": "",
    "id": "1",
    "name": "John Doe",
    "phone": "",
    "save_contact_from_document": "",
    "state": "",
    "updateClient": "0",
    "zip": "555 55"
  },
  "ClientData": {
    "Country": {
      "eu": true,
      "id": "191",
      "iso": "sk",
      "name": "Slovensko"
    },
    "DeliveryCountry": {
      "eu": true,
      "id": "191",
      "iso": "sk",
      "name": "Slovensko"
    },
    "address": "Vymyslena 1",
    "city": "Bratislava",
    "country": "Slovensko",
    "country_id": "191",
    "delivery_address": "",
    "delivery_city": "",
    "delivery_country": "Slovensko",
    "delivery_country_id": "191",
    "delivery_name": "",
    "delivery_phone": "",
    "delivery_state": "",
    "delivery_zip": "",
    "dic": "123456",
    "email": "",
    "fax": "",
    "ic_dph": "",
    "ico": "",
    "id": "1",
    "name": "John Doe",
    "phone": "",
    "save_contact_from_document": "",
    "state": "",
    "updateClient": "0",
    "zip": "555 55"
  },
  "Invoice": {
    "accounting_date": "2050-01-01",
    "amount": "10.00",
    "amount_paid": "0.00",
    "client_data": "{\"Client\":{\"id\":\"1\",\"name\":\"John Doe\",\"address\":\"Vymyslena 1\",\"ico\":\"\",\"email\":\"\",\"zip\":\"555 55\",\"dic\":\"123456\",\"phone\":\"\",\"city\":\"Bratislava\",\"ic_dph\":\"\",\"fax\":\"\",\"country_id\":\"191\",\"state\":\"\",\"delivery_name\":\"\",\"delivery_zip\":\"\",\"delivery_city\":\"\",\"delivery_address\":\"\",\"delivery_phone\":\"\",\"delivery_country_id\":\"191\",\"delivery_state\":\"\",\"updateClient\":\"0\",\"save_contact_from_document\":\"\",\"country\":\"Slovensko\",\"delivery_country\":\"Slovensko\"}} ",
    "client_id": "1",
    "comment": "",
    "constant": "",
    "country_exchange_rate": "1.00000000000000",
    "created": "2050-01-01 23:59:59",
    "delivery": "2050-01-01 23:59:59",
    "delivery_type": "",
    "demo": "0",
    "deposit": "0.00",
    "discount": "0",
    "due": "2050-01-01",
    "estimate_id": null,
    "exchange_rate": 1,
    "flag": "issued",
    "header_comment": "",
    "home_currency": "EUR",
    "id": "1",
    "import_id": null,
    "import_parent_id": null,
    "import_type": null,
    "internal_comment": null,
    "invoice_currency": "EUR",
    "invoice_no": "1",
    "invoice_no_formatted": "2020001",
    "invoice_no_formatted_length": "7",
    "invoice_no_formatted_raw": "2020001",
    "issued_by": "SuperFaktura, s.r.o.",
    "issued_by_email": "api@example.com",
    "issued_by_phone": "",
    "issued_by_web": "",
    "items_data": "item 1 ,",
    "items_name": null,
    "lang": "slo",
    "mask": "YYYYNNN",
    "modified": "2050-01-01 23:59:59",
    "my_data": "{\"MyData\":{\"id\":\"1\",\"user_id\":\"1\",\"user_profile_id\":\"\",\"country_id\":\"191\",\"company_name\":\"SuperFaktura, s.r.o.\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"update_profile\":\"\",\"tax_payer\":\"1\",\"logo_key\":\"\",\"logo_id\":\"\",\"web\":\"\",\"Logo\":\"[{\\\"id\\\":\\\"1\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"1\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"4311c1895aa334d39ac8_1_exads_logo_rgb.png\\\",\\\"checksum\\\":\\\"a1dcdc392d08d6d1caaf148225f2a7d4\\\",\\\"group\\\":\\\"logo\\\",\\\"default\\\":true,\\\"alternative\\\":null,\\\"size\\\":\\\"49743\\\",\\\"extern_file\\\":\\\"0\\\",\\\"delete_flag\\\":false,\\\"created\\\":\\\"2050-01-01 23:59:59\\\",\\\"modified\\\":\\\"2050-01-01 23:59:59\\\",\\\"path\\\":\\\"img\\\\\\/4311c1895aa334d39ac8_1_exads_logo_rgb.png\\\"}]\",\"Signature\":\"{\\\"id\\\":\\\"2\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"1\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"9b7c9830cb6b6afa7b16_1_podpis_1.png\\\",\\\"checksum\\\":\\\"33b5238616646ca28ebabc02f713a59f\\\",\\\"group\\\":\\\"signature\\\",\\\"default\\\":false,\\\"alternative\\\":null,\\\"size\\\":\\\"2689\\\",\\\"extern_file\\\":\\\"0\\\",\\\"delete_flag\\\":false,\\\"created\\\":\\\"2050-01-01 23:59:59\\\",\\\"modified\\\":\\\"2050-01-01 23:59:59\\\",\\\"path\\\":\\\"img\\\\\\/9b7c9830cb6b6afa7b16_1_podpis_1.png\\\"}\",\"travel_agencies\":\"\",\"business_register\":\"Obchodn\\u00fd register Okresn\\u00e9ho s\\u00fadu Bratislava I, oddiel: Sro, vlo\\u017eka \\u010d. 81403\\/B\",\"BankAccount\":[{\"id\":\"1\",\"show_account\":\"1\",\"default\":\"1\",\"country_id\":\"191\",\"bank_name\":\"FatraBanka\",\"bank_code\":\"\",\"account\":\"\",\"iban\":\"SK012345678901234567890000\",\"swift\":\"SUZUKI\"}],\"country\":\"Slovensko\"}}",
    "name": "Faktúra 2020001",
    "order_no": null,
    "paid": "0.00",
    "parent_id": null,
    "paydate": null,
    "payment_type": "",
    "proforma_id": null,
    "recurring": null,
    "rounding": "item",
    "sequence_id": "1",
    "show_items_with_dph": true,
    "show_special_vat": false,
    "special_vat_scheme": null,
    "specific": "",
    "status": "1",
    "summary_invoice": null,
    "tags": null,
    "tax_document": null,
    "taxdate": null,
    "token": "c3b05c50",
    "type": "regular",
    "user_id": "1",
    "user_profile_id": "1",
    "variable": "2020001",
    "variable_raw": "2020001",
    "vat": "2.00",
    "vat_transfer": null
  },
  "InvoiceEmail": [],
  "InvoiceItem": [
    {
      "description": "",
      "discount": 0,
      "discount_description": "Zľava",
      "discount_no_vat": -0,
      "discount_no_vat_total": -0,
      "discount_with_vat": -0,
      "discount_with_vat_total": -0,
      "hide_in_autocomplete": null,
      "id": "1",
      "invoice_id": "1",
      "item_price": 10,
      "item_price_no_discount": 10,
      "item_price_vat": 12,
      "item_price_vat_check": 12,
      "item_price_vat_no_discount": 12,
      "name": "item 1",
      "ordernum": "0",
      "quantity": "1.00000",
      "sku": null,
      "stock_item_id": null,
      "tax": 20,
      "tax_deposit": null,
      "unit": "",
      "unit_price": 10,
      "unit_price_discount": 10,
      "unit_price_vat": 12,
      "unit_price_vat_no_discount": 12,
      "user_id": "1",
      "user_profile_id": "1"
    }
  ],
  "InvoicePayment": [],
  "InvoiceSetting": {
    "bysquare": true,
    "create_from_multiple_deliveries": "",
    "force_iban": true,
    "language": "slo",
    "online_payment": null,
    "payment_info": true,
    "paypal": false,
    "show_prices": false,
    "show_summary": true,
    "signature": true
  },
  "MyData": {
    "BankAccount": [
      {
        "account": "",
        "bank_code": "",
        "bank_name": "FatraBanka",
        "country_id": "191",
        "default": "1",
        "iban": "SK012345678901234567890000",
        "id": "1",
        "show_account": "1",
        "swift": "SUZUKI"
      }
    ],
    "Logo": "[{\"id\":\"1\",\"model\":\"User\",\"foreign_key\":\"1\",\"dirname\":\"img\",\"basename\":\"4311c1895aa334d39ac8_1_exads_logo_rgb.png\",\"checksum\":\"a1dcdc392d08d6d1caaf148225f2a7d4\",\"group\":\"logo\",\"default\":true,\"alternative\":null,\"size\":\"49743\",\"extern_file\":\"0\",\"delete_flag\":false,\"created\":\"2050-01-01 23:59:59\",\"modified\":\"2050-01-01 23:59:59\",\"path\":\"img\\/4311c1895aa334d39ac8_1_exads_logo_rgb.png\",\"mobile_path\":\"\"}]",
    "LogoRaw": [
      {
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
        "mobile_path": "",
        "model": "User",
        "modified": "2050-01-01 23:59:59",
        "path": "img/4311c1895aa334d39ac8_1_exads_logo_rgb.png",
        "size": "49743"
      }
    ],
    "Signature": "{\"id\":\"2\",\"model\":\"User\",\"foreign_key\":\"1\",\"dirname\":\"img\",\"basename\":\"9b7c9830cb6b6afa7b16_1_podpis_1.png\",\"checksum\":\"33b5238616646ca28ebabc02f713a59f\",\"group\":\"signature\",\"default\":false,\"alternative\":null,\"size\":\"2689\",\"extern_file\":\"0\",\"delete_flag\":false,\"created\":\"2050-01-01 23:59:59\",\"modified\":\"2050-01-01 23:59:59\",\"path\":\"img\\/9b7c9830cb6b6afa7b16_1_podpis_1.png\"}",
    "SignatureRaw": {
      "alternative": null,
      "basename": "9b7c9830cb6b6afa7b16_1_podpis_1.png",
      "checksum": "33b5238616646ca28ebabc02f713a59f",
      "created": "2050-01-01 23:59:59",
      "default": false,
      "delete_flag": false,
      "dirname": "img",
      "extern_file": "0",
      "foreign_key": "1",
      "group": "signature",
      "id": "2",
      "model": "User",
      "modified": "2050-01-01 23:59:59",
      "path": "img/9b7c9830cb6b6afa7b16_1_podpis_1.png",
      "size": "2689"
    },
    "address": "Pri Suchom mlyne 6",
    "business_register": "Obchodný register Okresného súdu Bratislava I, oddiel: Sro, vložka č. 81403/B",
    "city": "Bratislava - mestská časť Staré Mesto",
    "company_name": "SuperFaktura, s.r.o.",
    "country": {
      "eu": true,
      "id": "191",
      "iso": "sk",
      "name": "Slovensko"
    },
    "country_id": "191",
    "dic": "2023513470",
    "ic_dph": "SK2023513470",
    "ico": "46655034",
    "id": "1",
    "logo_id": "",
    "logo_key": "",
    "tax_payer": "1",
    "travel_agencies": "",
    "update_profile": "",
    "user_id": "1",
    "user_profile_id": "",
    "web": "",
    "zip": "811 04"
  },
  "PaymentLink": null,
  "Paypal": false,
  "PostStamp": [],
  "RelatedItems": [],
  "Summary": {
    "discount": 0,
    "invoice_total": 12,
    "vat_base_separate": {
      "20": 10
    },
    "vat_base_total": 10,
    "vat_separate": {
      "20": 2
    },
    "vat_total": 2
  },
  "SummaryInvoice": {
    "vat_base_separate_negative": {
      "20": 0
    },
    "vat_base_separate_positive": {
      "20": 10
    },
    "vat_separate_negative": {
      "20": 0
    },
    "vat_separate_positive": {
      "20": 2
    }
  },
  "Tag": [],
  "UnitCount": []
}
```

#### Wrong invoice

```json
{
  "error": 1,
  "error_message": "Invoice not found",
  "message": "Invoice not found"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Get invoices details

Get information about multiple invoices at once.
You can specify up to 100 invoice IDs.

### Request
**URL**: `/invoices/getInvoiceDetails/{IDS}`  
**HTTP method**: GET  

```sh
curl -X GET \
     -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
     https://moja.superfaktura.sk/invoices/getInvoiceDetails/1,2
```

### Attributes
#### Required
URL parameters:

| name    | type   | description | default value |
| ------- | ------ | ----------- | ------------- |
| **ids** | string | list of invoice IDs separated by comma | |


#### Optional
none

### Response

Returns list of invoices with all the information about them.
The list consists of keys (invoice ID) and value which is JSON object.
For more details about fields present in result see example response.

#### Success
```json
{
  "1": {
    "0": {
      "to_pay": "12.000000",
      "to_pay_in_invoice_currency": "12.00",
      "total": "12.00"
    },
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
    "ClientData": {
      "Country": {
        "eu": true,
        "id": "191",
        "iso": "sk",
        "name": "Slovensko"
      },
      "DeliveryCountry": {
        "eu": true,
        "id": "191",
        "iso": "sk",
        "name": "Slovensko"
      },
      "address": "Vymyslena 1",
      "city": "Bratislava",
      "country": "Slovensko",
      "country_id": "191",
      "delivery_address": "",
      "delivery_city": "",
      "delivery_country": "Slovensko",
      "delivery_country_id": "191",
      "delivery_name": "",
      "delivery_phone": "",
      "delivery_state": "",
      "delivery_zip": "",
      "dic": "123456",
      "email": "",
      "fax": "",
      "ic_dph": "",
      "ico": "",
      "id": "1",
      "name": "John Doe",
      "phone": "",
      "save_contact_from_document": "",
      "state": "",
      "updateClient": "0",
      "zip": "555 55"
    },
    "Invoice": {
      "accounting_date": "2050-01-01",
      "amount": "10.00",
      "amount_paid": "0.00",
      "client_data": "{\"Client\":{\"id\":\"1\",\"name\":\"John Doe\",\"address\":\"Vymyslena 1\",\"ico\":\"\",\"email\":\"\",\"zip\":\"555 55\",\"dic\":\"123456\",\"phone\":\"\",\"city\":\"Bratislava\",\"ic_dph\":\"\",\"fax\":\"\",\"country_id\":\"191\",\"state\":\"\",\"delivery_name\":\"\",\"delivery_zip\":\"\",\"delivery_city\":\"\",\"delivery_address\":\"\",\"delivery_phone\":\"\",\"delivery_country_id\":\"191\",\"delivery_state\":\"\",\"updateClient\":\"0\",\"save_contact_from_document\":\"\",\"country\":\"Slovensko\",\"delivery_country\":\"Slovensko\"}} ",
      "client_id": "1",
      "comment": "",
      "constant": "",
      "country_exchange_rate": "1.00000000000000",
      "created": "2050-01-01 23:59:59",
      "delivery": "2050-01-01 23:59:59",
      "delivery_type": "",
      "demo": "0",
      "deposit": "0.00",
      "discount": "0",
      "due": "2050-01-01",
      "estimate_id": null,
      "exchange_rate": 1,
      "flag": "issued",
      "header_comment": "",
      "home_currency": "EUR",
      "id": "1",
      "import_id": null,
      "import_parent_id": null,
      "import_type": null,
      "internal_comment": null,
      "invoice_currency": "EUR",
      "invoice_no": "1",
      "invoice_no_formatted": "2020001",
      "invoice_no_formatted_length": "7",
      "invoice_no_formatted_raw": "2020001",
      "issued_by": "SuperFaktura, s.r.o.",
      "issued_by_email": "api@example.com",
      "issued_by_phone": "",
      "issued_by_web": "",
      "items_data": "item 1 ,",
      "items_name": null,
      "lang": "slo",
      "mask": "YYYYNNN",
      "modified": "2050-01-01 23:59:59",
      "my_data": "{\"MyData\":{\"id\":\"1\",\"user_id\":\"1\",\"user_profile_id\":\"\",\"country_id\":\"191\",\"company_name\":\"SuperFaktura, s.r.o.\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"update_profile\":\"\",\"tax_payer\":\"1\",\"logo_key\":\"\",\"logo_id\":\"\",\"web\":\"\",\"Logo\":\"[{\\\"id\\\":\\\"1\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"1\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"4311c1895aa334d39ac8_1_exads_logo_rgb.png\\\",\\\"checksum\\\":\\\"a1dcdc392d08d6d1caaf148225f2a7d4\\\",\\\"group\\\":\\\"logo\\\",\\\"default\\\":true,\\\"alternative\\\":null,\\\"size\\\":\\\"49743\\\",\\\"extern_file\\\":\\\"0\\\",\\\"delete_flag\\\":false,\\\"created\\\":\\\"2050-01-01 23:59:59\\\",\\\"modified\\\":\\\"2050-01-01 23:59:59\\\",\\\"path\\\":\\\"img\\\\\\/4311c1895aa334d39ac8_1_exads_logo_rgb.png\\\"}]\",\"Signature\":\"{\\\"id\\\":\\\"2\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"1\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"9b7c9830cb6b6afa7b16_1_podpis_1.png\\\",\\\"checksum\\\":\\\"33b5238616646ca28ebabc02f713a59f\\\",\\\"group\\\":\\\"signature\\\",\\\"default\\\":false,\\\"alternative\\\":null,\\\"size\\\":\\\"2689\\\",\\\"extern_file\\\":\\\"0\\\",\\\"delete_flag\\\":false,\\\"created\\\":\\\"2050-01-01 23:59:59\\\",\\\"modified\\\":\\\"2050-01-01 23:59:59\\\",\\\"path\\\":\\\"img\\\\\\/9b7c9830cb6b6afa7b16_1_podpis_1.png\\\"}\",\"travel_agencies\":\"\",\"business_register\":\"Obchodn\\u00fd register Okresn\\u00e9ho s\\u00fadu Bratislava I, oddiel: Sro, vlo\\u017eka \\u010d. 81403\\/B\",\"BankAccount\":[{\"id\":\"1\",\"show_account\":\"1\",\"default\":\"1\",\"country_id\":\"191\",\"bank_name\":\"FatraBanka\",\"bank_code\":\"\",\"account\":\"\",\"iban\":\"SK012345678901234567890000\",\"swift\":\"SUZUKI\"}],\"country\":\"Slovensko\"}}",
      "name": "Faktúra 2020001",
      "order_no": null,
      "paid": "0.00",
      "parent_id": null,
      "paydate": null,
      "payment_type": "",
      "proforma_id": null,
      "recurring": null,
      "rounding": "item",
      "sequence_id": "1",
      "show_items_with_dph": true,
      "show_special_vat": false,
      "special_vat_scheme": null,
      "specific": "",
      "status": "1",
      "summary_invoice": null,
      "tags": null,
      "tax_document": null,
      "taxdate": null,
      "token": "c3b05c50",
      "type": "regular",
      "user_id": "1",
      "user_profile_id": "1",
      "variable": "2020001",
      "variable_raw": "2020001",
      "vat": "2.00",
      "vat_transfer": null
    },
    "InvoiceEmail": [],
    "InvoiceItem": [
      {
        "description": "",
        "discount": 0,
        "discount_description": "Zľava",
        "discount_no_vat": -0,
        "discount_no_vat_total": -0,
        "discount_with_vat": -0,
        "discount_with_vat_total": -0,
        "hide_in_autocomplete": null,
        "id": "1",
        "invoice_id": "1",
        "item_price": 10,
        "item_price_no_discount": 10,
        "item_price_vat": 12,
        "item_price_vat_check": 12,
        "item_price_vat_no_discount": 12,
        "name": "item 1",
        "ordernum": "0",
        "quantity": "1.00000",
        "sku": null,
        "stock_item_id": null,
        "tax": 20,
        "tax_deposit": null,
        "unit": "",
        "unit_price": 10,
        "unit_price_discount": 10,
        "unit_price_vat": 12,
        "unit_price_vat_no_discount": 12,
        "user_id": "1",
        "user_profile_id": "1"
      }
    ],
    "InvoicePayment": [],
    "InvoiceSetting": {
      "bysquare": true,
      "create_from_multiple_deliveries": "",
      "force_iban": true,
      "language": "slo",
      "online_payment": null,
      "payment_info": true,
      "paypal": false,
      "show_prices": false,
      "show_summary": true,
      "signature": true
    },
    "Logo": [
      {
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
        "mobile_path": "",
        "model": "User",
        "modified": "2050-01-01 23:59:59",
        "path": "img/4311c1895aa334d39ac8_1_exads_logo_rgb.png",
        "size": "49743"
      }
    ],
    "MyData": {
      "BankAccount": [
        {
          "account": "",
          "bank_code": "",
          "bank_name": "FatraBanka",
          "country_id": "191",
          "default": "1",
          "iban": "SK012345678901234567890000",
          "id": "1",
          "show_account": "1",
          "swift": "SUZUKI"
        }
      ],
      "Logo": "[{\"id\":\"1\",\"model\":\"User\",\"foreign_key\":\"1\",\"dirname\":\"img\",\"basename\":\"4311c1895aa334d39ac8_1_exads_logo_rgb.png\",\"checksum\":\"a1dcdc392d08d6d1caaf148225f2a7d4\",\"group\":\"logo\",\"default\":true,\"alternative\":null,\"size\":\"49743\",\"extern_file\":\"0\",\"delete_flag\":false,\"created\":\"2050-01-01 23:59:59\",\"modified\":\"2050-01-01 23:59:59\",\"path\":\"img\\/4311c1895aa334d39ac8_1_exads_logo_rgb.png\",\"mobile_path\":\"\"}]",
      "LogoRaw": [
        {
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
          "mobile_path": "",
          "model": "User",
          "modified": "2050-01-01 23:59:59",
          "path": "img/4311c1895aa334d39ac8_1_exads_logo_rgb.png",
          "size": "49743"
        }
      ],
      "Signature": "{\"id\":\"2\",\"model\":\"User\",\"foreign_key\":\"1\",\"dirname\":\"img\",\"basename\":\"9b7c9830cb6b6afa7b16_1_podpis_1.png\",\"checksum\":\"33b5238616646ca28ebabc02f713a59f\",\"group\":\"signature\",\"default\":false,\"alternative\":null,\"size\":\"2689\",\"extern_file\":\"0\",\"delete_flag\":false,\"created\":\"2050-01-01 23:59:59\",\"modified\":\"2050-01-01 23:59:59\",\"path\":\"img\\/9b7c9830cb6b6afa7b16_1_podpis_1.png\"}",
      "SignatureRaw": {
        "alternative": null,
        "basename": "9b7c9830cb6b6afa7b16_1_podpis_1.png",
        "checksum": "33b5238616646ca28ebabc02f713a59f",
        "created": "2050-01-01 23:59:59",
        "default": false,
        "delete_flag": false,
        "dirname": "img",
        "extern_file": "0",
        "foreign_key": "1",
        "group": "signature",
        "id": "2",
        "model": "User",
        "modified": "2050-01-01 23:59:59",
        "path": "img/9b7c9830cb6b6afa7b16_1_podpis_1.png",
        "size": "2689"
      },
      "address": "Pri Suchom mlyne 6",
      "business_register": "Obchodný register Okresného súdu Bratislava I, oddiel: Sro, vložka č. 81403/B",
      "city": "Bratislava - mestská časť Staré Mesto",
      "company_name": "SuperFaktura, s.r.o.",
      "country": {
        "eu": true,
        "id": "191",
        "iso": "sk",
        "name": "Slovensko"
      },
      "country_id": "191",
      "dic": "2023513470",
      "ic_dph": "SK2023513470",
      "ico": "46655034",
      "id": "1",
      "logo_id": "",
      "logo_key": "",
      "tax_payer": "1",
      "travel_agencies": "",
      "update_profile": "",
      "user_id": "1",
      "user_profile_id": "",
      "web": "",
      "zip": "811 04"
    },
    "Paypal": false,
    "PostStamp": [],
    "RelatedItems": [],
    "Signature": {
      "alternative": null,
      "basename": "9b7c9830cb6b6afa7b16_1_podpis_1.png",
      "checksum": "33b5238616646ca28ebabc02f713a59f",
      "created": "2050-01-01 23:59:59",
      "default": false,
      "delete_flag": false,
      "dirname": "img",
      "extern_file": "0",
      "foreign_key": "1",
      "group": "signature",
      "id": "2",
      "model": "User",
      "modified": "2050-01-01 23:59:59",
      "path": "img/9b7c9830cb6b6afa7b16_1_podpis_1.png",
      "size": "2689"
    },
    "Summary": {
      "discount": 0,
      "invoice_total": 12,
      "vat_base_separate": {
        "20": 10
      },
      "vat_base_total": 10,
      "vat_separate": {
        "20": 2
      },
      "vat_total": 2
    },
    "SummaryInvoice": {
      "vat_base_separate_negative": {
        "20": 0
      },
      "vat_base_separate_positive": {
        "20": 10
      },
      "vat_separate_negative": {
        "20": 0
      },
      "vat_separate_positive": {
        "20": 2
      }
    },
    "Tag": [],
    "UnitCount": []
  }
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Get list of invoices

Get list of invoices.

### Request

**URL**: `/invoices/index.json[/{ATTRIBUTE}:{VALUE}]*`  
**HTTP method**: GET  


```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoices/index.json/listinfo:1/per_page:1/page:2
```  

### Attributes
#### Required
none

#### Optional

URL parameters:  

| name          | type   | description                                                                          | default value |
| ------------- | ------ | ------------------------------------------------------------------------------------ | ------------- |
| **direction** | string | sorting direction (ASC or DESC)                                                      | 'DESC' |
| **listinfo**  | int    | show meta data about result? (0=no, 1=yes)                                           | 0 |
| **page**      | int    | page number                                                                          | 1 |
| **per_page**  | int    | number of items per page (max 200)                                                   | |
| **sort**      | string | attribute to sort by                                                                 | 'regular_count' |
| **type**      | string | type of document (proforma, regular, ...). Use <code>&#x7c;</code> as separator for multiple values. | 'regular' |

Filtering parameters

| name               | type         | description    | default value |
| ------------------ | ------------ | ------------   | ------------- |
| **amount_from**    | float        | amount from    | 0             |
| **amount_to**      | float        | amount to      | 0             |
| **client_id**      | int          | client ID      | |
| **created**        | int          | constant specifying time filtering (see [Value lists > Time filter constants](value-lists.md#time-filter-constants)) | 6 |
| **created_since**  | date         | creation date since (requires `created:3`) | |
| **created_to**     | date         | creation date to (requires `created:3`) | |
| **delivery**       | int          | constant specifying time filtering (see [Value lists > Time filter constants](value-lists.md#time-filter-constants)) | |
| **delivery_since** | date         | delivery date from (requires `delivery:3`) | |
| **delivery_to**    | date         | delivery date to (requires `delivery:3`)   | |
| **delivery_type**  | string       | delivery type (see [Value lists > Delivery types](value-lists.md#delivery-types)). Use <code>&#x7c;</code> as separator for multiple values. | |
| **ignore**         | string / int | IDs of invoices to be ignored. Use <code>&#x7c;</code> as separator for multiple values. | |
| **invoice_no_formatted** | string | formatted invoice number | |
| **modified**       | int          | last modification date constant specifying time filtering (see [Value lists > Time filter constants](value-lists.md#time-filter-constants)) | |
| **modified_since** | date         | last modification date from (requires `modified:3`) | |
| **modified_to**    | date         | last modification date to (requires `modified:3`)   | |
| **order_no**       | string       | order number, from which invoice is created | |
| **paid**           | int          | constant specifying time filtering (see [Value lists > Time filter constants](value-lists.md#time-filter-constants)) | |
| **paid_since**     | date         | pay date since (requires `paid:3`) | |
| **paid_to**        | date         | pay date to (requires `paid:3`)   | |
| **payment_type**   | string       | payment types (see [Value lists > Payment types](value-lists.md#payment-types)). Use <code>&#x7c;</code> as separator for multiple values. | |
| **search**         | string       | base64 encoded string | |
| **status**         | string / int | invoice status (see [Value lists > Invoice statuses](value-lists.md#invoice-statuses)) | |
| **tag**            | int          | tag ID | |
| **variable**       | string       | variable symbol | |



### Response

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoices/index.json/listinfo:1/per_page:1/page:2/type:regular
```


```json
{
  "filtered": false,
  "itemCount": 2,
  "items": [
    {
      "0": {
        "to_pay": "12.000000",
        "to_pay_in_invoice_currency": "12.00",
        "total": "12.00"
      },
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
      "ClientData": {
        "Country": {
          "eu": true,
          "id": "191",
          "iso": "sk",
          "name": "Slovensko"
        },
        "DeliveryCountry": {
          "eu": true,
          "id": "191",
          "iso": "sk",
          "name": "Slovensko"
        },
        "address": "Vymyslena 1",
        "city": "Bratislava",
        "country": "Slovensko",
        "country_id": "191",
        "delivery_address": "",
        "delivery_city": "",
        "delivery_country": "Slovensko",
        "delivery_country_id": "191",
        "delivery_name": "",
        "delivery_phone": "",
        "delivery_state": "",
        "delivery_zip": "",
        "dic": "123456",
        "email": "",
        "fax": "",
        "ic_dph": "",
        "ico": "",
        "id": "1",
        "name": "John Doe",
        "phone": "",
        "save_contact_from_document": "",
        "state": "",
        "updateClient": "0",
        "zip": "555 55"
      },
      "Invoice": {
        "accounting_date": "2050-01-01",
        "amount": "10.00",
        "amount_paid": "0.00",
        "client_data": "{\"Client\":{\"id\":\"1\",\"name\":\"John Doe\",\"address\":\"Vymyslena 1\",\"ico\":\"\",\"email\":\"\",\"zip\":\"555 55\",\"dic\":\"123456\",\"phone\":\"\",\"city\":\"Bratislava\",\"ic_dph\":\"\",\"fax\":\"\",\"country_id\":\"191\",\"state\":\"\",\"delivery_name\":\"\",\"delivery_zip\":\"\",\"delivery_city\":\"\",\"delivery_address\":\"\",\"delivery_phone\":\"\",\"delivery_country_id\":\"191\",\"delivery_state\":\"\",\"updateClient\":\"0\",\"save_contact_from_document\":\"\",\"country\":\"Slovensko\",\"delivery_country\":\"Slovensko\"}} ",
        "client_id": "1",
        "comment": "",
        "constant": "",
        "country_exchange_rate": "1.00000000000000",
        "created": "2050-01-01 23:59:59",
        "delivery": "2050-01-01 23:59:59",
        "delivery_type": "",
        "demo": "0",
        "deposit": "0.00",
        "discount": "0",
        "due": "2050-01-01",
        "estimate_id": null,
        "exchange_rate": 1,
        "flag": "issued",
        "header_comment": "",
        "home_currency": "EUR",
        "id": "1",
        "import_id": null,
        "import_parent_id": null,
        "import_type": null,
        "internal_comment": null,
        "invoice_currency": "EUR",
        "invoice_no": "1",
        "invoice_no_formatted": "2020001",
        "invoice_no_formatted_length": "7",
        "invoice_no_formatted_raw": "2020001",
        "issued_by": "SuperFaktura, s.r.o.",
        "issued_by_email": "api@example.com",
        "issued_by_phone": "",
        "issued_by_web": "",
        "items_data": "item 1 ,",
        "items_name": null,
        "lang": "slo",
        "mask": "YYYYNNN",
        "modified": "2050-01-01 23:59:59",
        "my_data": "{\"MyData\":{\"id\":\"1\",\"user_id\":\"1\",\"user_profile_id\":\"\",\"country_id\":\"191\",\"company_name\":\"SuperFaktura, s.r.o.\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"update_profile\":\"\",\"tax_payer\":\"1\",\"logo_key\":\"\",\"logo_id\":\"\",\"web\":\"\",\"Logo\":\"[{\\\"id\\\":\\\"1\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"1\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"4311c1895aa334d39ac8_1_exads_logo_rgb.png\\\",\\\"checksum\\\":\\\"a1dcdc392d08d6d1caaf148225f2a7d4\\\",\\\"group\\\":\\\"logo\\\",\\\"default\\\":true,\\\"alternative\\\":null,\\\"size\\\":\\\"49743\\\",\\\"extern_file\\\":\\\"0\\\",\\\"delete_flag\\\":false,\\\"created\\\":\\\"2050-01-01 23:59:59\\\",\\\"modified\\\":\\\"2050-01-01 23:59:59\\\",\\\"path\\\":\\\"img\\\\\\/4311c1895aa334d39ac8_1_exads_logo_rgb.png\\\"}]\",\"Signature\":\"{\\\"id\\\":\\\"2\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"1\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"9b7c9830cb6b6afa7b16_1_podpis_1.png\\\",\\\"checksum\\\":\\\"33b5238616646ca28ebabc02f713a59f\\\",\\\"group\\\":\\\"signature\\\",\\\"default\\\":false,\\\"alternative\\\":null,\\\"size\\\":\\\"2689\\\",\\\"extern_file\\\":\\\"0\\\",\\\"delete_flag\\\":false,\\\"created\\\":\\\"2050-01-01 23:59:59\\\",\\\"modified\\\":\\\"2050-01-01 23:59:59\\\",\\\"path\\\":\\\"img\\\\\\/9b7c9830cb6b6afa7b16_1_podpis_1.png\\\"}\",\"travel_agencies\":\"\",\"business_register\":\"Obchodn\\u00fd register Okresn\\u00e9ho s\\u00fadu Bratislava I, oddiel: Sro, vlo\\u017eka \\u010d. 81403\\/B\",\"BankAccount\":[{\"id\":\"1\",\"show_account\":\"1\",\"default\":\"1\",\"country_id\":\"191\",\"bank_name\":\"FatraBanka\",\"bank_code\":\"\",\"account\":\"\",\"iban\":\"SK012345678901234567890000\",\"swift\":\"SUZUKI\"}],\"country\":\"Slovensko\"}}",
        "name": "Faktúra 2020001",
        "order_no": null,
        "paid": "0.00",
        "parent_id": null,
        "paydate": null,
        "payment_type": "",
        "proforma_id": null,
        "recurring": null,
        "rounding": "item",
        "sequence_id": "1",
        "show_items_with_dph": true,
        "show_special_vat": false,
        "special_vat_scheme": null,
        "specific": "",
        "status": "1",
        "summary_invoice": null,
        "tags": null,
        "tax_document": null,
        "taxdate": null,
        "token": "c3b05c50",
        "type": "regular",
        "user_id": "1",
        "user_profile_id": "1",
        "variable": "2020001",
        "variable_raw": "2020001",
        "vat": "2.00",
        "vat_transfer": null
      },
      "InvoiceEmail": [],
      "InvoiceItem": [
        {
          "description": "",
          "discount": 0,
          "discount_description": "Zľava",
          "discount_no_vat": -0,
          "discount_no_vat_total": -0,
          "discount_with_vat": -0,
          "discount_with_vat_total": -0,
          "hide_in_autocomplete": null,
          "id": "1",
          "invoice_id": "1",
          "item_price": 10,
          "item_price_no_discount": 10,
          "item_price_vat": 12,
          "item_price_vat_check": 12,
          "item_price_vat_no_discount": 12,
          "name": "item 1",
          "ordernum": "0",
          "quantity": "1.00000",
          "sku": null,
          "stock_item_id": null,
          "tax": 20,
          "tax_deposit": null,
          "unit": "",
          "unit_price": 10,
          "unit_price_discount": 10,
          "unit_price_vat": 12,
          "unit_price_vat_no_discount": 12,
          "user_id": "1",
          "user_profile_id": "1"
        }
      ],
      "InvoicePayment": [],
      "InvoiceSetting": {
        "bysquare": true,
        "create_from_multiple_deliveries": "",
        "force_iban": true,
        "language": "slo",
        "online_payment": null,
        "payment_info": true,
        "paypal": false,
        "show_prices": false,
        "show_summary": true,
        "signature": true
      },
      "Logo": [
        {
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
          "mobile_path": "",
          "model": "User",
          "modified": "2050-01-01 23:59:59",
          "path": "img/4311c1895aa334d39ac8_1_exads_logo_rgb.png",
          "size": "49743"
        }
      ],
      "MyData": {
        "BankAccount": [
          {
            "account": "",
            "bank_code": "",
            "bank_name": "FatraBanka",
            "country_id": "191",
            "default": "1",
            "iban": "SK012345678901234567890000",
            "id": "1",
            "show_account": "1",
            "swift": "SUZUKI"
          }
        ],
        "Logo": "[{\"id\":\"1\",\"model\":\"User\",\"foreign_key\":\"1\",\"dirname\":\"img\",\"basename\":\"4311c1895aa334d39ac8_1_exads_logo_rgb.png\",\"checksum\":\"a1dcdc392d08d6d1caaf148225f2a7d4\",\"group\":\"logo\",\"default\":true,\"alternative\":null,\"size\":\"49743\",\"extern_file\":\"0\",\"delete_flag\":false,\"created\":\"2050-01-01 23:59:59\",\"modified\":\"2050-01-01 23:59:59\",\"path\":\"img\\/4311c1895aa334d39ac8_1_exads_logo_rgb.png\",\"mobile_path\":\"\"}]",
        "LogoRaw": [
          {
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
            "mobile_path": "",
            "model": "User",
            "modified": "2050-01-01 23:59:59",
            "path": "img/4311c1895aa334d39ac8_1_exads_logo_rgb.png",
            "size": "49743"
          }
        ],
        "Signature": "{\"id\":\"2\",\"model\":\"User\",\"foreign_key\":\"1\",\"dirname\":\"img\",\"basename\":\"9b7c9830cb6b6afa7b16_1_podpis_1.png\",\"checksum\":\"33b5238616646ca28ebabc02f713a59f\",\"group\":\"signature\",\"default\":false,\"alternative\":null,\"size\":\"2689\",\"extern_file\":\"0\",\"delete_flag\":false,\"created\":\"2050-01-01 23:59:59\",\"modified\":\"2050-01-01 23:59:59\",\"path\":\"img\\/9b7c9830cb6b6afa7b16_1_podpis_1.png\"}",
        "SignatureRaw": {
          "alternative": null,
          "basename": "9b7c9830cb6b6afa7b16_1_podpis_1.png",
          "checksum": "33b5238616646ca28ebabc02f713a59f",
          "created": "2050-01-01 23:59:59",
          "default": false,
          "delete_flag": false,
          "dirname": "img",
          "extern_file": "0",
          "foreign_key": "1",
          "group": "signature",
          "id": "2",
          "model": "User",
          "modified": "2050-01-01 23:59:59",
          "path": "img/9b7c9830cb6b6afa7b16_1_podpis_1.png",
          "size": "2689"
        },
        "address": "Pri Suchom mlyne 6",
        "business_register": "Obchodný register Okresného súdu Bratislava I, oddiel: Sro, vložka č. 81403/B",
        "city": "Bratislava - mestská časť Staré Mesto",
        "company_name": "SuperFaktura, s.r.o.",
        "country": {
          "eu": true,
          "id": "191",
          "iso": "sk",
          "name": "Slovensko"
        },
        "country_id": "191",
        "dic": "2023513470",
        "ic_dph": "SK2023513470",
        "ico": "46655034",
        "id": "1",
        "logo_id": "",
        "logo_key": "",
        "tax_payer": "1",
        "travel_agencies": "",
        "update_profile": "",
        "user_id": "1",
        "user_profile_id": "",
        "web": "",
        "zip": "811 04"
      },
      "Paypal": false,
      "PostStamp": [],
      "RelatedItems": [],
      "Signature": {
        "alternative": null,
        "basename": "9b7c9830cb6b6afa7b16_1_podpis_1.png",
        "checksum": "33b5238616646ca28ebabc02f713a59f",
        "created": "2050-01-01 23:59:59",
        "default": false,
        "delete_flag": false,
        "dirname": "img",
        "extern_file": "0",
        "foreign_key": "1",
        "group": "signature",
        "id": "2",
        "model": "User",
        "modified": "2050-01-01 23:59:59",
        "path": "img/9b7c9830cb6b6afa7b16_1_podpis_1.png",
        "size": "2689"
      },
      "Summary": {
        "discount": 0,
        "invoice_total": 12,
        "vat_base_separate": {
          "20": 10
        },
        "vat_base_total": 10,
        "vat_separate": {
          "20": 2
        },
        "vat_total": 2
      },
      "SummaryInvoice": {
        "vat_base_separate_negative": {
          "20": 0
        },
        "vat_base_separate_positive": {
          "20": 10
        },
        "vat_separate_negative": {
          "20": 0
        },
        "vat_separate_positive": {
          "20": 2
        }
      },
      "Tag": [],
      "UnitCount": []
    }
  ],
  "page": 2,
  "pageCount": 2,
  "perPage": 1
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Export invoices

Export multiple invoices in PDF or XLS format.

### Request

**URL**: `/exports`  
**HTTP method**: POST

```sh
data='{
    "Invoice":{
        "ids":[1562,1561,1560]
    },
    "Export":{
        "is_msel":true,
        "invoices_pdf":true,
        "merge_pdf":true,
        "only_merge":true
    }
}';

curl -X POST \
    -d "data=$data" \
    -o /output.pdf \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
    https://moja.superfaktura.sk/exports




data='{
    "Invoice":{
        "ids":[1562,1561,1560]
    },
    "Export":{
        "is_msel":true,
        "invoices_xls":true
    }
}';

curl -X POST \
    -d "data=$data" \
    -o /output.xls \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
    https://moja.superfaktura.sk/exports




data='{
    "Invoice":{
        "ids":[1562,1561,1560]
    },
    "Export":{
        "is_msel":true,
        "invoices_pdf":true
    }
}';

curl -X POST \
    -d "data=$data" \
    -o /output.zip \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
    https://moja.superfaktura.sk/exports
```

### Attributes
#### Required

##### Export
| name                  | type | description                                         | default value |
| --------------------- | ---- | --------------------------------------------------- | ------------- |
| **msel**              | bool | is multiselect; needs to be `true` (required: true) |               |

##### Invoice
| name                  | type  | description | default value |
| --------------------- | ----- | ----------- | ------------- |
| **ids**               | array | list of IDs |               |

#### Optional

##### Export

| name                      | type | description                        | default value |
| ------------------------- | ---- | ---------------------------------- | ------------- |
| **hide_pdf_payment_info** | bool | hide payment information           |             0 |
| **hide_signature**        | bool | hide signature in invoices         |             0 |
| **invoices_pdf**          | bool | export in PDF format               |             0 |
| **invoices_xls**          | bool | export in XLS format               |             0 |
| **merge_pdf**             | bool | only export merged PDF             |             0 |
| **pdf_lang_default**      | bool | translate documents to default language (SK: Slovak, CZ: Czech) | 0 |
| **pdf_sort_client**       | bool | sort documents by client           |             0 |
| **pdf_sort_date**         | bool | sort documents by date             |             0 |


### Response
PDF document on success.


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Delete invoice

Delete invoice by ID.

### Request
**URL**: `/invoices/delete/{ID}`  
**HTTP method**: GET  


```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoices/delete/1
```

### Attributes
#### Required

| name   | type | description | default value |
| ------ | ---- | ----------- | ------------- |
| **ID** | int  | invoice ID  |               |

#### Optional
none

### Response

#### Successful deletion

```json
{
  "error": 0,
  "message": "Invoice deleted"
}
```

#### Wrong ID
Returns HTTP status 404.

```json
{
  "error": 1,
  "error_message": "Invoice not found",
  "message": "Invoice not found"
}
```

#### Deleting locked invoice
```json
{
  "error": 0,
  "message": "Invoice deleted"
}
```

#### Error during deletion
If an error occurs, HTTP status 404 is returned.

```json
{
   "message" : "Invoice could not be deleted",
   "error" : 1,
   "error_message" : "Invoice could not be deleted"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Set invoice as "will not be paid"

Set invoice as "will not be paid".
Only works for regular and proforma invoices.

### Request

**URL**: `/invoices/will_not_be_paid/{ID}`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoices/will_not_be_paid/1
```

### Attributes
#### Required

URL parameters:

| name   | type     | description | default value |
| ------ | -------- | ----------- | ------------- |
| **id** | int      | invoice ID  |               |

#### Optional

none

### Response

#### Successfully marked

```json
{
  "data": {
    "Invoice": {
      "accounting_date": "2050-01-01",
      "amount": "10.00",
      "amount_paid": "0.00",
      "client_data": "{\"Client\":{\"id\":\"1\",\"name\":\"John Doe\",\"address\":\"Vymyslena 1\",\"ico\":\"\",\"email\":\"\",\"zip\":\"555 55\",\"dic\":\"123456\",\"phone\":\"\",\"city\":\"Bratislava\",\"ic_dph\":\"\",\"fax\":\"\",\"country_id\":\"191\",\"state\":\"\",\"delivery_name\":\"\",\"delivery_zip\":\"\",\"delivery_city\":\"\",\"delivery_address\":\"\",\"delivery_phone\":\"\",\"delivery_country_id\":\"191\",\"delivery_state\":\"\",\"updateClient\":\"0\",\"save_contact_from_document\":\"\",\"country\":\"Slovensko\",\"delivery_country\":\"Slovensko\"}} ",
      "client_id": "1",
      "comment": "",
      "constant": "",
      "country_exchange_rate": "1.00000000000000",
      "created": "2050-01-01 23:59:59",
      "delivery": "2050-01-01 23:59:59",
      "delivery_type": "",
      "demo": "0",
      "deposit": "0.00",
      "discount": "0",
      "due": "2050-01-01",
      "estimate_id": null,
      "exchange_rate": "1.00000000000000",
      "header_comment": "",
      "home_currency": "EUR",
      "id": "1",
      "import_id": null,
      "import_parent_id": null,
      "import_type": null,
      "internal_comment": null,
      "invoice_currency": "EUR",
      "invoice_no": "1",
      "invoice_no_formatted": "2020001",
      "invoice_no_formatted_length": "7",
      "invoice_no_formatted_raw": "2020001",
      "issued_by": "SuperFaktura, s.r.o.",
      "issued_by_email": "api@example.com",
      "issued_by_phone": "",
      "issued_by_web": "",
      "items_data": "item 1 ,",
      "items_name": null,
      "lang": "slo",
      "mask": "YYYYNNN",
      "modified": "2050-01-01 23:59:59",
      "my_data": "{\"MyData\":{\"id\":\"1\",\"user_id\":\"1\",\"user_profile_id\":\"\",\"country_id\":\"191\",\"company_name\":\"SuperFaktura, s.r.o.\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"update_profile\":\"\",\"tax_payer\":\"1\",\"logo_key\":\"\",\"logo_id\":\"\",\"web\":\"\",\"Logo\":\"[{\\\"id\\\":\\\"1\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"1\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"4311c1895aa334d39ac8_1_exads_logo_rgb.png\\\",\\\"checksum\\\":\\\"a1dcdc392d08d6d1caaf148225f2a7d4\\\",\\\"group\\\":\\\"logo\\\",\\\"default\\\":true,\\\"alternative\\\":null,\\\"size\\\":\\\"49743\\\",\\\"extern_file\\\":\\\"0\\\",\\\"delete_flag\\\":false,\\\"created\\\":\\\"2050-01-01 23:59:59\\\",\\\"modified\\\":\\\"2050-01-01 23:59:59\\\",\\\"path\\\":\\\"img\\\\\\/4311c1895aa334d39ac8_1_exads_logo_rgb.png\\\"}]\",\"Signature\":\"{\\\"id\\\":\\\"2\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"1\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"9b7c9830cb6b6afa7b16_1_podpis_1.png\\\",\\\"checksum\\\":\\\"33b5238616646ca28ebabc02f713a59f\\\",\\\"group\\\":\\\"signature\\\",\\\"default\\\":false,\\\"alternative\\\":null,\\\"size\\\":\\\"2689\\\",\\\"extern_file\\\":\\\"0\\\",\\\"delete_flag\\\":false,\\\"created\\\":\\\"2050-01-01 23:59:59\\\",\\\"modified\\\":\\\"2050-01-01 23:59:59\\\",\\\"path\\\":\\\"img\\\\\\/9b7c9830cb6b6afa7b16_1_podpis_1.png\\\"}\",\"travel_agencies\":\"\",\"business_register\":\"Obchodn\\u00fd register Okresn\\u00e9ho s\\u00fadu Bratislava I, oddiel: Sro, vlo\\u017eka \\u010d. 81403\\/B\",\"BankAccount\":[{\"id\":\"1\",\"show_account\":\"1\",\"default\":\"1\",\"country_id\":\"191\",\"bank_name\":\"FatraBanka\",\"bank_code\":\"\",\"account\":\"\",\"iban\":\"SK012345678901234567890000\",\"swift\":\"SUZUKI\"}],\"country\":\"Slovensko\"}}",
      "name": "Faktúra 2020001",
      "order_no": null,
      "paid": "0.00",
      "parent_id": null,
      "paydate": null,
      "payment_type": "",
      "proforma_id": null,
      "recurring": null,
      "rounding": "item",
      "sequence_id": "1",
      "special_vat_scheme": null,
      "specific": "",
      "status": "1",
      "summary_invoice": null,
      "tags": null,
      "tax_document": null,
      "taxdate": null,
      "token": "c3b05c50",
      "type": "regular",
      "user_id": "1",
      "user_profile_id": "1",
      "variable": "2020001",
      "variable_raw": "2020001",
      "vat": "2.00",
      "vat_transfer": null
    }
  },
  "error": 0,
  "error_message": "Document marked as \"will not be paid\""
}
```

#### Wrong invoice

```json
{
  "error": 1,
  "error_message": "Document can not be canceled"
}
```

#### Insufficient privileges

```json
{
  "error": 1,
  "error_message": "Nemáte právo meniť faktúru",
  "message": "Nemáte právo meniť faktúru"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


## Pay invoice

Pay invoice.
Only `regular`, `proforma` and `cancel` invoice types can be paid.

### Request
**URL**: `/invoice_payments/add/ajax:1/api:1`  
**HTTP method**: POST  

```
data='{
  "InvoicePayment":{
    "invoice_id":1,
    "payment_type":"cash",
    "amount":12,
    "created":"2019-01-01",
    "currency":"EUR"
  }
}';

curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoice_payments/add/ajax:1/api:1
```

### Attributes

#### Required

| name                  | type   | description | default value |
| --------------------- | ------ | ----------- | ------------- |
| **invoice_id**        | int    | invoice ID | |

#### Optional

| name                  | type   | description | default value |
| --------------------- | ------ | ----------- | ------------- |
| **amount**            | float  | amount of money paid | invoice total price |
| **cash_register_id**  | int    | cash register ID | |
| **currency**          | string | currency (see [Value lists > Currencies](value-lists.md#currencies))| EUR in SK, CZK in CZ |
| **date**              | date   | date when payment was done (format: `YYYY-MM-DD`) | &lt;current date&gt; |
| **document_no**       | string | document number | |
| **payment_type**      | string | payment type (see [Value lists > Payment types](value-lists.md#payment-types)) | transfer |



### Response


#### Successfully added payment
```json
{
  "country_exchange_rate": 1,
  "created": "2050-01-01",
  "currency": "€",
  "error": 0,
  "exchange_rate": 1,
  "flash_message": {
    "text": "Úhrada bola uložená",
    "type": "success"
  },
  "home_currency": "€",
  "invoice_currency": "€",
  "invoice_id": 1,
  "invoice_type": "regular",
  "overdue": false,
  "paid": 12,
  "parent_id": null,
  "payment_id": "1",
  "status": 3,
  "to_pay": 0,
  "to_pay_home_cur": 0
}
```

#### Adding payment to already fully paid invoice
```json
{
  "error": 1,
  "error_messages": [],
  "message": "Faktúra je už plne uhradená"
}
```

#### Invalid ID
```json
{
  "error": 1,
  "message": "Payment not found"
}
```

#### Paying invalid invoice type
```json
{
  "error": 1,
  "message": "Invalid document type"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Send invoice via mail

Sends invoice to specified email address.
Sending emails has a limit of 100 emails / hour.

### Request
**URL**: `/invoices/send`  
**HTTP method**: POST  

```sh
data='{
  "Email":{
    "invoice_id":1,
    "to":"john.doe@example.com",
    "pdf_language":"eng"
  }
}';

curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoices/send
```

### Attributes
### Required

| name             | type     | description   | default value |
| ---------------- | -------- | ------------- | ------------- |
| **invoice_id**   | int      | ID of invoice that will be sent | |
| **to**           | string   | email address to which email will be sent | |

### Optional

| name             | type     | description   | default value |
| ---------------- | -------- | ------------- | ------------- |
| **bcc**          | string[] | list of email addresses to send BCC to | |
| **body**         | string   | message body | &lt;as defined in templates&gt; |
| **cc**           | string[] | list of email addresses to send CC to | |
| **pdf_language** | string   | document language (see [Value lists > Language list](value-lists.md#language-list)) | |
| **subject**      | string   | email subject | &lt;as defined in templates&gt; |

### Response

#### Successfully sent
```json
{
  "data": {
    "Invoice": {
      "bysquare": true,
      "cc": "[]",
      "email": "john.doe@example.com",
      "invoice_id": "1",
      "invoice_lang": "eng",
      "message": "Dobrý deň,\n\nv prílohe posielame faktúru č. 2020001.\n\nSuma na úhradu: 12,00 €\nVariabilný symbol: 2020001\nČíslo účtu: SK012345678901234567890000\n\nĎakujeme za úhradu a prajeme príjemný deň.\nSuperFaktura, s.r.o.",
      "no-signature": false,
      "payment_info": true,
      "paypal": false,
      "recipient": "john.doe@example.com",
      "subject": "Faktúra 2020001",
      "trustpay": null
    }
  },
  "error": 0,
  "error_message": ""
}
```

#### Sent with CC
```sh
data='{
  "Email":{
    "bcc":["foo@example.com"],
    "body":"api body",
    "cc":["bar@example.com"],
    "invoice_id":1,
    "pdf_language":"deu",
    "subject":"api subject",
    "to":"john.doe@example.com"
  }
}';

curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoices/send
```

```json
{
  "data": {
    "Invoice": {
      "bysquare": true,
      "cc": "[\"bar@example.com\"]",
      "email": "john.doe@example.com",
      "invoice_id": "1",
      "invoice_lang": "deu",
      "message": "api body",
      "no-signature": false,
      "payment_info": true,
      "paypal": false,
      "recipient": "john.doe@example.com",
      "subject": "api subject",
      "trustpay": null
    }
  },
  "error": 0,
  "error_message": ""
}
```

#### Invoice not found
```json
{
  "error": 4,
  "error_message": "Invoice not found"
}
```

#### Invalid recipient email address
```json
{
  "error": 13,
  "error_message": "Please insert valid recipient email address."
}
```

#### Any other problem
```json
{
   "error" : 1,
   "error_message" : "Invoice not found",
   "message" : "Invoice not found"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Mark invoice as sent via email

Mark invoice as sent via email.

### Request
**URL**: `/invoices/mark_as_sent`  
**HTTP method**: POST  

```sh
data='{
  "InvoiceEmail":{
    "invoice_id":1,
    "email":"john.doe@example.com",
    "subject":"subject",
    "message":"hello world"
  }
}';

curl -X POST \
  -d "data=$data" \
  -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
  https://moja.superfaktura.sk/invoices/mark_as_sent
```

 

### Attributes
#### Required

```json
{
  "InvoiceEmail": {
    "invoice_id": 1276,
    "email": "user@example.com",
    "subject": "subject",
    "message": "hello world"
  }
}
```
#### Optional
none

### Response

#### Successfully marked
```json
{
  "error": 0,
  "error_message": "Invoice marked as sent"
}
```

#### Invalid post data
  
```json
{
  "error": 1,
  "error_message": "Invalid post data"
}

```

#### Wrong HTTP method
```json
{
  "error": 2,
  "error_message": "This method is POST only"
}
```

#### Invalid JSON or no data
```json
{
  "error": 3,
  "error_message": "Invalid invoice data"
}
```

#### Invalid data

In `error_messages` is list of validation errors.

```json
{
  "error": 4,
  "error_message": "Invalid email data"
}
```

#### Invalid invoice ID
```json
{
  "error": 5,
  "error_message": "Invalid invoice id"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Send invoice via post

Send invoice via post.

### Request
**URL**: `/invoices/post`  
**HTTP method**: POST  

```sh
data='{
  "Post":{
    "delivery_address":"Vymyslena 1",
    "delivery_city":"Bratislava",
    "delivery_country_id":191,
    "delivery_state":"Slovensko",
    "delivery_name":"John Doe",
    "delivery_zip":"99999",
    "invoice_id":1
  }
}';

curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoices/post
```

### Attributes
### Required

| name             | type     | description                     | default value |
| ---------------- | -------- | ------------------------------- | ------------- |
| **invoice_id**   | int      | ID of invoice that will be sent |               |

### Optional

| name                  | type   | description                                                     | default value |
| --------------------- | ------ | --------------------------------------------------------------- | ------------- |
| **delivery_address**  | string | delivery address (is not required, if invoice contains address) |               |
| **delivery_city**     | string | delivery city (is not required, if invoice contains city)       |               |
| **delivery_country**  | string | delivery country (is not required, if invoice contains country) |               |
| **delivery_state**    | string | delivery state (is not required, if invoice contains state)     |               |
| **delivery_zip**      | string | delivery zip (is not required, if invoice contains zip)         |               |

### Response

#### Successfully posted
```json
{
  "data": {
    "Invoice": {
      "accounting_date": "2050-01-01",
      "amount": "10.00",
      "amount_paid": "0.00",
      "client_data": "{\"Client\":{\"id\":\"1\",\"name\":\"John Doe\",\"address\":\"Vymyslena 1\",\"ico\":\"\",\"email\":\"\",\"zip\":\"555 55\",\"dic\":\"123456\",\"phone\":\"\",\"city\":\"Bratislava\",\"ic_dph\":\"\",\"fax\":\"\",\"country_id\":\"191\",\"state\":\"\",\"delivery_name\":\"\",\"delivery_zip\":\"\",\"delivery_city\":\"\",\"delivery_address\":\"\",\"delivery_phone\":\"\",\"delivery_country_id\":\"191\",\"delivery_state\":\"\",\"updateClient\":\"0\",\"save_contact_from_document\":\"\",\"country\":\"Slovensko\",\"delivery_country\":\"Slovensko\"}} ",
      "client_id": "1",
      "comment": "",
      "constant": "",
      "country_exchange_rate": "1.00000000000000",
      "created": "2050-01-01 23:59:59",
      "delivery": "2050-01-01 23:59:59",
      "delivery_type": "",
      "demo": "0",
      "deposit": "0.00",
      "discount": "0",
      "due": "2050-01-01",
      "estimate_id": null,
      "exchange_rate": 1,
      "flag": "issued",
      "header_comment": "",
      "home_currency": "EUR",
      "id": "1",
      "import_id": null,
      "import_parent_id": null,
      "import_type": null,
      "internal_comment": null,
      "invoice_currency": "EUR",
      "invoice_no": "1",
      "invoice_no_formatted": "2020001",
      "invoice_no_formatted_length": "7",
      "invoice_no_formatted_raw": "2020001",
      "issued_by": "SuperFaktura, s.r.o.",
      "issued_by_email": "api@example.com",
      "issued_by_phone": "",
      "issued_by_web": "",
      "items_data": "item 1 ,",
      "items_name": null,
      "lang": "slo",
      "mask": "YYYYNNN",
      "modified": "2050-01-01 23:59:59",
      "my_data": "{\"MyData\":{\"id\":\"1\",\"user_id\":\"1\",\"user_profile_id\":\"\",\"country_id\":\"191\",\"company_name\":\"SuperFaktura, s.r.o.\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"update_profile\":\"\",\"tax_payer\":\"1\",\"logo_key\":\"\",\"logo_id\":\"\",\"web\":\"\",\"Logo\":\"[{\\\"id\\\":\\\"1\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"1\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"4311c1895aa334d39ac8_1_exads_logo_rgb.png\\\",\\\"checksum\\\":\\\"a1dcdc392d08d6d1caaf148225f2a7d4\\\",\\\"group\\\":\\\"logo\\\",\\\"default\\\":true,\\\"alternative\\\":null,\\\"size\\\":\\\"49743\\\",\\\"extern_file\\\":\\\"0\\\",\\\"delete_flag\\\":false,\\\"created\\\":\\\"2050-01-01 23:59:59\\\",\\\"modified\\\":\\\"2050-01-01 23:59:59\\\",\\\"path\\\":\\\"img\\\\\\/4311c1895aa334d39ac8_1_exads_logo_rgb.png\\\"}]\",\"Signature\":\"{\\\"id\\\":\\\"2\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"1\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"9b7c9830cb6b6afa7b16_1_podpis_1.png\\\",\\\"checksum\\\":\\\"33b5238616646ca28ebabc02f713a59f\\\",\\\"group\\\":\\\"signature\\\",\\\"default\\\":false,\\\"alternative\\\":null,\\\"size\\\":\\\"2689\\\",\\\"extern_file\\\":\\\"0\\\",\\\"delete_flag\\\":false,\\\"created\\\":\\\"2050-01-01 23:59:59\\\",\\\"modified\\\":\\\"2050-01-01 23:59:59\\\",\\\"path\\\":\\\"img\\\\\\/9b7c9830cb6b6afa7b16_1_podpis_1.png\\\"}\",\"travel_agencies\":\"\",\"business_register\":\"Obchodn\\u00fd register Okresn\\u00e9ho s\\u00fadu Bratislava I, oddiel: Sro, vlo\\u017eka \\u010d. 81403\\/B\",\"BankAccount\":[{\"id\":\"1\",\"show_account\":\"1\",\"default\":\"1\",\"country_id\":\"191\",\"bank_name\":\"FatraBanka\",\"bank_code\":\"\",\"account\":\"\",\"iban\":\"SK012345678901234567890000\",\"swift\":\"SUZUKI\"}],\"country\":\"Slovensko\"}}",
      "name": "Faktúra 2020001",
      "order_no": null,
      "paid": "0.00",
      "parent_id": null,
      "paydate": null,
      "payment_type": "",
      "proforma_id": null,
      "recurring": null,
      "rounding": "item",
      "sequence_id": "1",
      "show_items_with_dph": true,
      "show_special_vat": false,
      "special_vat_scheme": null,
      "specific": "",
      "status": "1",
      "summary_invoice": null,
      "tags": null,
      "tax_document": null,
      "taxdate": null,
      "token": "c3b05c50",
      "type": "regular",
      "user_id": "1",
      "user_profile_id": "1",
      "variable": "2020001",
      "variable_raw": "2020001",
      "vat": "2.00",
      "vat_transfer": null
    }
  },
  "error": 0,
  "error_message": ""
}
```

#### Missing address data
```json
{
  "error": 6,
  "message": "Address data error."
}
```

#### Not enough post stamps
```json
{
  "error": 7,
  "message": "No post stamps left."
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Mark invoice as sent

Mark invoice as sent. If already marked so, will be unmarked.

### Request

**URL**: `/invoices/mark_sent/{ID}`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoices/mark_sent/1
```

### Attributes
#### Required

URL parameters:

| name   | type     | description | default value |
| ------ | -------- | ----------- | ------------- |
| **id** | int      | invoice ID  |               |

#### Optional

none

### Response


#### Successfully marked

```json
{
  "error": 0,
  "error_message": "",
  "marked": true
}
```

#### Wrong invoice

```json
{
  "error": 1,
  "error_message": "Snažíte sa označiť cudziu faktúru"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Delete invoice item

### Request
**URL**: `/invoice_items/delete/{ITEM_ID}/invoice_id:{INVOICE_ID}`  
**HTTP method**: GET  

```
curl -X GET \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
    https://moja.superfaktura.sk/invoice_items/delete/1/invoice_id:1
```


### Attributes
#### Required

URL parameters:

| name            | type         | description                                                           | default value |
| --------------- | ------------ | --------------------------------------------------------------------- | ------------- |
| **item_id**     | int / string | invoice item ID, if used as string, use comma to separate various IDs |               |
| **invoice_id**  | int          | invoice ID                                                            |               |

#### Optional
none

### Response

#### Successful deletion
```json
{
  "data": {
    "Invoice": {
      "accounting_date": "2050-01-01",
      "amount": "0.00",
      "amount_paid": "0.00",
      "client_data": "{\"Client\":{\"id\":\"1\",\"name\":\"John Doe\",\"address\":\"Vymyslena 1\",\"ico\":\"\",\"email\":\"\",\"zip\":\"555 55\",\"dic\":\"123456\",\"phone\":\"\",\"city\":\"Bratislava\",\"ic_dph\":\"\",\"fax\":\"\",\"country_id\":\"191\",\"state\":\"\",\"delivery_name\":\"\",\"delivery_zip\":\"\",\"delivery_city\":\"\",\"delivery_address\":\"\",\"delivery_phone\":\"\",\"delivery_country_id\":\"191\",\"delivery_state\":\"\",\"updateClient\":\"0\",\"save_contact_from_document\":\"\",\"country\":\"Slovensko\",\"delivery_country\":\"Slovensko\"}} ",
      "client_id": "1",
      "comment": "",
      "constant": "",
      "country_exchange_rate": "1.00000000000000",
      "created": "2050-01-01 23:59:59",
      "delivery": "2050-01-01 23:59:59",
      "delivery_type": "",
      "demo": "0",
      "deposit": "0.00",
      "discount": "0",
      "due": "2050-01-01",
      "estimate_id": null,
      "exchange_rate": "1.00000000000000",
      "header_comment": "",
      "home_currency": "EUR",
      "id": "1",
      "import_id": null,
      "import_parent_id": null,
      "import_type": null,
      "internal_comment": null,
      "invoice_currency": "EUR",
      "invoice_no": "1",
      "invoice_no_formatted": "2020001",
      "invoice_no_formatted_length": "7",
      "invoice_no_formatted_raw": "2020001",
      "issued_by": "SuperFaktura, s.r.o.",
      "issued_by_email": "api@example.com",
      "issued_by_phone": "",
      "issued_by_web": "",
      "items_data": "",
      "items_name": null,
      "lang": "slo",
      "mask": "YYYYNNN",
      "modified": "2050-01-01 23:59:59",
      "my_data": "{\"MyData\":{\"id\":\"1\",\"user_id\":\"1\",\"user_profile_id\":\"\",\"country_id\":\"191\",\"company_name\":\"SuperFaktura, s.r.o.\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"update_profile\":\"\",\"tax_payer\":\"1\",\"logo_key\":\"\",\"logo_id\":\"\",\"web\":\"\",\"Logo\":\"[{\\\"id\\\":\\\"1\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"1\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"4311c1895aa334d39ac8_1_exads_logo_rgb.png\\\",\\\"checksum\\\":\\\"a1dcdc392d08d6d1caaf148225f2a7d4\\\",\\\"group\\\":\\\"logo\\\",\\\"default\\\":true,\\\"alternative\\\":null,\\\"size\\\":\\\"49743\\\",\\\"extern_file\\\":\\\"0\\\",\\\"delete_flag\\\":false,\\\"created\\\":\\\"2050-01-01 23:59:59\\\",\\\"modified\\\":\\\"2050-01-01 23:59:59\\\",\\\"path\\\":\\\"img\\\\\\/4311c1895aa334d39ac8_1_exads_logo_rgb.png\\\"}]\",\"Signature\":\"{\\\"id\\\":\\\"2\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"1\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"9b7c9830cb6b6afa7b16_1_podpis_1.png\\\",\\\"checksum\\\":\\\"33b5238616646ca28ebabc02f713a59f\\\",\\\"group\\\":\\\"signature\\\",\\\"default\\\":false,\\\"alternative\\\":null,\\\"size\\\":\\\"2689\\\",\\\"extern_file\\\":\\\"0\\\",\\\"delete_flag\\\":false,\\\"created\\\":\\\"2050-01-01 23:59:59\\\",\\\"modified\\\":\\\"2050-01-01 23:59:59\\\",\\\"path\\\":\\\"img\\\\\\/9b7c9830cb6b6afa7b16_1_podpis_1.png\\\"}\",\"travel_agencies\":\"\",\"business_register\":\"Obchodn\\u00fd register Okresn\\u00e9ho s\\u00fadu Bratislava I, oddiel: Sro, vlo\\u017eka \\u010d. 81403\\/B\",\"BankAccount\":[{\"id\":\"1\",\"show_account\":\"1\",\"default\":\"1\",\"country_id\":\"191\",\"bank_name\":\"FatraBanka\",\"bank_code\":\"\",\"account\":\"\",\"iban\":\"SK012345678901234567890000\",\"swift\":\"SUZUKI\"}],\"country\":\"Slovensko\"}}",
      "name": "Faktúra 2020001",
      "order_no": null,
      "paid": "0.00",
      "parent_id": null,
      "paydate": null,
      "payment_type": "",
      "proforma_id": null,
      "recurring": null,
      "rounding": "item",
      "sequence_id": "1",
      "special_vat_scheme": null,
      "specific": "",
      "status": "1",
      "summary_invoice": null,
      "tags": null,
      "tax_document": null,
      "taxdate": null,
      "token": "c3b05c50",
      "type": "regular",
      "user_id": "1",
      "user_profile_id": "1",
      "variable": "2020001",
      "variable_raw": "2020001",
      "vat": "0.00",
      "vat_transfer": null
    },
    "InvoiceItem": []
  },
  "error": 0,
  "error_message": ""
}
```


#### Error while deleting

E.g. trying to delete already deleted item.

```json
{
  "error": 1,
  "message": "Chyba pri mazaní položky"
}
```


#### Invalid request
```json
{
  "error": 3,
  "error_message": "Bad data format."
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Delete invoice payment

Delete invoice payment.

### Request
**URL**: `/invoice_payments/delete/{PAYMENT_ID}`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoice_payments/delete/1
```

### Attributes
#### Required

| name           | type | description | default value |
| -------------- | ---- | ----------- | ------------- |
| **payment_id** | int  | payment ID  |               |

### Response

#### Successful deletion
```json
{
  "error": 0,
  "invoice_id": "1",
  "paid": "0.00",
  "status": 1,
  "to_pay": 12
}
```

#### Payment not found 
```json
{
  "error": 1,
  "message": "Platba sa nenašla"
}
```

#### Unsuccessful deletion  
```json
{
    "error": 1,
    "message": "Error deleting payment"   
}
```

#### Invalid ID
```json
{
    "error": 1,
    "message": "Invalid id for invoice payment"   
}
```
