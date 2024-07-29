# Cash register item

- [Add cash register item](#add-cash-register-item)
- [Get cash register items](#get-cash-register-items)
- [Delete cash register item](#delete-cash-register-item)
- [Get receipt from the cash register in PDF](#get-receipt-from-the-cash-register)


## Add cash register item

Add item to cash register.

### Request

**URL**: `/cash_register_items/add`  
**HTTP method**: POST  

```sh
# minimal example
data='{
    "CashRegisterItem":{
        "amount":12,
        "cash_register_id":14
    }
}';

# with EET
data='{
    "CashRegisterItem":{
        "amount":12,
        "cash_register_id":8,
        "is_eet":true,
        "created":"2019-02-06 12:05:50",
        "currency":"CZK",
        "cash_item_no_formatted":"2019007"
    }
}';

# with more data
data='{
    "CashRegisterItem":{
        "amount":12,
        "cash_register_id":14,
        "created":"2019-02-06 12:05:50",
        "cash_item_no_formatted":"2019007",
        "client_id":431,
        "description":"Test description",
        "invoice_id":1285
    }
}';

curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/cash_register_items/add
```

### Attributes

#### Required

| name                  | type  | description | default value |
| --------------------- | ----- | ----------- | ------------- |
| **amount**            | float | amount of money <ul><li>positive - adding to cash register</li><li>negative - removing from cash register</li></ul>| |
| **cash_register_id**  | int   | cash register ID | |

#### Optional

| name              | type   | description | default value |
| ----------------- | ------ | ----------- | ------------- |
| **client_id**     | int    | client ID - to whom we paid or who paid (is used in link in cash register items list) | |
| **client_name**   | string | client name - to whom we paid or who paid (is visible as link name in cash register items list) | |
| **created**       | date   | datetime when cash register item was created | |
| **currency**      | string | currency | &lt;default currency&gt; |
| **description**   | string | description of cash register item | |
| **expense_id**    | int    | expense, which is paid by this cash register item | |
| **invoice_id**    | int    | invoice, which is paid by this cash register item | |
| **is_eet**        | int    | is EET movement (0 = no, true = yes) | 0 |


### Response


```sh
# minimal example
data='{
      "CashRegisterItem": {
        "amount": 14,
        "cash_register_id": 1
      }
    }
';

# richer example
data='{
      "CashRegisterItem": {
        "amount": 14,
        "cash_register_id": 1,
        "created": "2069-01-31 02:00:00",
        "description": "Invoice no. 2069001",
        "invoice_id": 1
      }
    }
';

curl -X POST \
    -d "data=$data" \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
     https://moja.superfaktura.sk/cash_register_items/add/
```

```json
{
  "CashRegister": {
    "sequence_in_no": "P2020004",
    "sequence_out_no": "V2020001"
  },
  "CashRegisterItem": {
    "amount": 14,
    "amount_formatted": "14,00 <span class=\"currency_symbol\">€</span>",
    "cash_item_no": "2020003",
    "cash_item_no_formatted": "P2020003",
    "cash_register_id": 1,
    "created": "2050-01-01 23:59:59",
    "created_formatted": "01.01.2050",
    "currency": "EUR",
    "exchange_rate": 1,
    "id": "6",
    "sequence_cnt": 3,
    "sequence_id": 6,
    "sequencein_id": 6,
    "sequenceout_id": 7,
    "type": 0
  },
  "Summary": {
    "minus": {
      "formatted": "0,00 <span class=\"currency_symbol\">€</span>",
      "value": null
    },
    "plus": {
      "formatted": "120,00 <span class=\"currency_symbol\">€</span>",
      "value": "120.00"
    },
    "total": {
      "formatted": "120,00 <span class=\"currency_symbol\">€</span>",
      "value": "120.00"
    }
  },
  "status": "1"
}
```


#### Successfully added with invoice ID

```json
{
  "CashRegister": {
    "sequence_in_no": "P2020003",
    "sequence_out_no": "V2020001"
  },
  "CashRegisterItem": {
    "amount": 14,
    "amount_formatted": "14,00 <span class=\"currency_symbol\">€</span>",
    "cash_item_no": "2069001",
    "cash_item_no_formatted": "P2069001",
    "cash_register_id": 1,
    "client_id": "1",
    "client_name": "John Doe",
    "created": "2050-01-01 23:59:59",
    "created_formatted": "01.01.2050",
    "currency": "EUR",
    "description": "Invoice no. 2069001",
    "exchange_rate": 1,
    "id": "6",
    "invoice_id": 1,
    "sequence_cnt": 1,
    "sequence_id": 6,
    "sequencein_id": 6,
    "sequenceout_id": 7,
    "type": 0
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
  },
  "Summary": {
    "minus": {
      "formatted": "0,00 <span class=\"currency_symbol\">€</span>",
      "value": null
    },
    "plus": {
      "formatted": "120,00 <span class=\"currency_symbol\">€</span>",
      "value": "120.00"
    },
    "total": {
      "formatted": "120,00 <span class=\"currency_symbol\">€</span>",
      "value": "120.00"
    }
  },
  "status": "1"
}
```


#### Insufficient privileges

```json
{
  "error": 1,
  "error_message": "Ako používateľ typu Hosť nemáte oprávnenie na túto akciu."
}
```


#### Valid EET request

```json
{
  "CashRegister": {
    "sequence_in_no": "P2020003",
    "sequence_out_no": "V2020001"
  },
  "CashRegisterItem": {
    "amount": 12,
    "amount_formatted": "12,00 <span class=\"currency_symbol\">Kč</span>",
    "cash_item_no": "2020002",
    "cash_item_no_formatted": "P2020002",
    "cash_register_id": 2,
    "created": "2050-01-01 23:59:59",
    "created_formatted": "01.01.2050",
    "currency": "CZK",
    "exchange_rate": 1,
    "id": "6",
    "is_eet": true,
    "sequence_cnt": 2,
    "sequence_id": 6,
    "sequencein_id": 6,
    "sequenceout_id": 7,
    "type": 0
  },
  "EetReceipt": {
    "CashRegister": {
      "currency": "CZK",
      "description": "My EET Cash Register",
      "eet_certificate_id": "1",
      "id": "2",
      "id_provoz": "123234",
      "name": "CR2-EET",
      "sequencein_id": "6",
      "sequenceout_id": "7",
      "user_id": "1",
      "user_profile_id": "1"
    },
    "EetCertificate": {
      "created": "2050-01-01 23:59:59",
      "dic": "CZ1212121218",
      "hash": "237c6fc9",
      "id": "1",
      "modified": "2050-01-01 23:59:59",
      "name": "eet",
      "private_key": "LbKL...CxTmzhq",
      "public_key": "-----BEGIN CERTIFICATE-----x-----END CERTIFICATE-----",
      "user_profile_id": "1",
      "valid_from": "2050-01-01 23:59:59",
      "valid_to": "2050-01-01 23:59:59"
    },
    "amount": 12,
    "bkp": "47ad323c-2d30c1e7-b2a42c05-2b4218d3-0171640b",
    "cash_register_id": "2",
    "celk_trzba": 12,
    "cerp_zuct": 0,
    "cest_sluz": 0,
    "created": "2050-01-01 23:59:59",
    "currency": "CZK",
    "dan1": 0,
    "dan2": 0,
    "dan3": 0,
    "dat_prij": "2050-01-01 23:59:59",
    "dat_trzby": "2050-01-01 23:59:59",
    "dat_trzby_internal": "2050-01-01",
    "data": "{\"uuid_zpravy\":\"f6f53fa6-c590-49a4-9159-616f70a46e9c\",\"prvni_zaslani\":true,\"dic_popl\":\"CZ1212121218\",\"dic_poverujiciho\":null,\"id_provoz\":\"123234\",\"id_pokl\":\"CR2-EET\",\"porad_cis\":\"P2020002\",\"dat_trzby\":{\"date\":\"01.01.2050 23:59:59.000000\",\"timezone_type\":3,\"timezone\":\"UTC\"},\"celk_trzba\":12,\"zakl_nepodl_dph\":0,\"zakl_dan1\":0,\"dan1\":0,\"zakl_dan2\":0,\"dan2\":0,\"zakl_dan3\":0,\"dan3\":0,\"cest_sluz\":0,\"pouzit_zboz1\":0,\"pouzit_zboz2\":0,\"pouzit_zboz3\":0,\"urceno_cerp_zuct\":0,\"cerp_zuct\":0,\"rezim\":0}",
    "dic_popl": "CZ1212121218",
    "dic_poverujiciho": null,
    "exchange_rate": 1,
    "fik": "06d2064d-f8a7-47c1-8668-46bcf8ef009c-ff",
    "id": "1",
    "id_pokl": "CR2-EET",
    "id_provoz": "123234",
    "modified": "2050-01-01 23:59:59",
    "pkp": "a4OD3q...vXtyQ==",
    "porad_cis": "P2020002",
    "pouzit_zboz1": 0,
    "pouzit_zboz2": 0,
    "pouzit_zboz3": 0,
    "prvni_zaslani": true,
    "rezim": 0,
    "test": true,
    "upid": "1",
    "urceno_cerp_zuct": 0,
    "user_id": "1",
    "user_profile_id": "1",
    "uuid_zpravy": "f6f53fa6-c590-49a4-9159-616f70a46e9c",
    "zakl_dan1": 0,
    "zakl_dan2": 0,
    "zakl_dan3": 0,
    "zakl_nepodl_dph": 0
  },
  "Summary": {
    "minus": {
      "formatted": "0,00 <span class=\"currency_symbol\">Kč</span>",
      "value": null
    },
    "plus": {
      "formatted": "1 260,00 <span class=\"currency_symbol\">Kč</span>",
      "value": "1260.00"
    },
    "total": {
      "formatted": "1 260,00 <span class=\"currency_symbol\">Kč</span>",
      "value": "1260.00"
    }
  },
  "flag": "fully-paid",
  "status": "1"
}
```


#### Invalid EET request
```json
{
  "CashRegister": {
    "sequence_in_no": "P2020003",
    "sequence_out_no": "V2020001"
  },
  "CashRegisterItem": {
    "amount": 12,
    "amount_formatted": "12,00 <span class=\"currency_symbol\">Kč</span>",
    "cash_item_no": "2020002",
    "cash_item_no_formatted": "P2020002",
    "cash_register_id": 2,
    "created": "2050-01-01 23:59:59",
    "created_formatted": "01.01.2050",
    "currency": "CZK",
    "exchange_rate": 1,
    "id": "6",
    "is_eet": true,
    "sequence_cnt": 2,
    "sequence_id": 6,
    "sequencein_id": 6,
    "sequenceout_id": 7,
    "type": 0
  },
  "EetReceipt": {
    "CashRegister": {
      "currency": "CZK",
      "description": "My EET Cash Register",
      "eet_certificate_id": "1",
      "id": "2",
      "id_provoz": "123234",
      "name": "CR2-EET",
      "sequencein_id": "6",
      "sequenceout_id": "7",
      "user_id": "1",
      "user_profile_id": "1"
    },
    "EetCertificate": {
      "created": "2050-01-01 23:59:59",
      "dic": "CZ1212121218",
      "hash": "237c6fc9",
      "id": "1",
      "modified": "2050-01-01 23:59:59",
      "name": "eet",
      "private_key": "LbKL...CxTmzhq",
      "public_key": "-----BEGIN CERTIFICATE-----x-----END CERTIFICATE-----",
      "user_profile_id": "1",
      "valid_from": "2050-01-01 23:59:59",
      "valid_to": "2050-01-01 23:59:59"
    },
    "amount": 12,
    "bkp": "47ad323c-2d30c1e7-b2a42c05-2b4218d3-0171640b",
    "cash_register_id": "2",
    "celk_trzba": 12,
    "cerp_zuct": 0,
    "cest_sluz": 0,
    "chyba": "XML zprava nevyhovela kontrole XML schematu",
    "created": "2050-01-01 23:59:59",
    "currency": "CZK",
    "dan1": 0,
    "dan2": 0,
    "dan3": 0,
    "dat_trzby": "2050-01-01 23:59:59",
    "dat_trzby_internal": "2050-01-01",
    "data": "{\"uuid_zpravy\":\"f6f53fa6-c590-49a4-9159-616f70a46e9c\",\"prvni_zaslani\":true,\"dic_popl\":\"1212121218\",\"dic_poverujiciho\":null,\"id_provoz\":\"123234\",\"id_pokl\":\"CR2-EET\",\"porad_cis\":\"P2020002\",\"dat_trzby\":{\"date\":\"01.01.2050 23:59:59.000000\",\"timezone_type\":3,\"timezone\":\"UTC\"},\"celk_trzba\":12,\"zakl_nepodl_dph\":0,\"zakl_dan1\":0,\"dan1\":0,\"zakl_dan2\":0,\"dan2\":0,\"zakl_dan3\":0,\"dan3\":0,\"cest_sluz\":0,\"pouzit_zboz1\":0,\"pouzit_zboz2\":0,\"pouzit_zboz3\":0,\"urceno_cerp_zuct\":0,\"cerp_zuct\":0,\"rezim\":0}",
    "dic_popl": "1212121218",
    "dic_poverujiciho": null,
    "exchange_rate": 1,
    "id": "1",
    "id_pokl": "CR2-EET",
    "id_provoz": "123234",
    "kod": 3,
    "modified": "2050-01-01 23:59:59",
    "pkp": "a4OD3q...vXtyQ==",
    "porad_cis": "P2020002",
    "pouzit_zboz1": 0,
    "pouzit_zboz2": 0,
    "pouzit_zboz3": 0,
    "prvni_zaslani": true,
    "rezim": 0,
    "upid": "1",
    "urceno_cerp_zuct": 0,
    "user_id": "1",
    "user_profile_id": "1",
    "uuid_zpravy": "f6f53fa6-c590-49a4-9159-616f70a46e9c",
    "zakl_dan1": 0,
    "zakl_dan2": 0,
    "zakl_dan3": 0,
    "zakl_nepodl_dph": 0
  },
  "Summary": {
    "minus": {
      "formatted": "0,00 <span class=\"currency_symbol\">Kč</span>",
      "value": null
    },
    "plus": {
      "formatted": "1 260,00 <span class=\"currency_symbol\">Kč</span>",
      "value": "1260.00"
    },
    "total": {
      "formatted": "1 260,00 <span class=\"currency_symbol\">Kč</span>",
      "value": "1260.00"
    }
  },
  "flag": "due",
  "status": "1"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Get cash register items

Get detailed information about cash register and its items.

### Request

**URL**: `/cash_register_items/index/{ID}`  
**HTTP method**: GET  


```sh
curl -X GET \
     -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
     https://moja.superfaktura.sk/cash_register_items/index/2/term:P2020003
```

### Attributes

#### Required

URL parameters:

| name   | type | description | default value |
| ------ | ---- | ----------- | ------------- |
| **id** | int  |cash register ID |           |

#### Optional

URL parameters:

| name           | type   | description | default value |
| -------------- | ------ | ----------- | ------------- |
| **date_from**  | date   | date from, in format `YYYY-MM-DD` | |
| **date_to**    | date   | date to, in format `YYYY-MM-DD` | |
| **datefilter** | string | time filter (possible values `'today'`, `'yesterday'`, `'thismonth'`, `'thisyear'`, `'prevmonth'`, `'prevyear'`) | |
| **sum_from**   | float  | sum from    | |
| **sum_to**     | float  | sum to      | |
| **term**       | string | filter items in output search term (search in `description` and `cash_item_no_formatted`) | |
| **type**       | string | type filter ("in" for income and "out" for outgo) | `null` (both) |




### Response

```json
{
  "CashRegister": {
    "currency": "CZK",
    "description": "My EET Cash Register",
    "id": "2",
    "id_provoz": "123234",
    "name": "CR2-EET",
    "sequence_in_no": "P2020002",
    "sequence_out_no": "V2020001",
    "sequencein_id": "6",
    "sequenceout_id": "7",
    "total": "1248.00",
    "user_id": "1",
    "user_profile_id": "1"
  },
  "error": "",
  "itemCount": 1,
  "items": [
    {
      "0": {
        "has_storno": "0"
      },
      "CashRegisterItem": {
        "amount": "1248.00",
        "cash_item_no_formatted": "P2020003",
        "cash_register_id": "2",
        "client_id": null,
        "client_name": "",
        "created": "2050-01-01 23:59:59",
        "description": "",
        "eet_receipt_id": "1",
        "expense_id": null,
        "id": "5",
        "invoice_id": null,
        "invoice_payment_id": null
      },
      "EetReceipt": {
        "celk_trzba": null,
        "created": null,
        "fik": null,
        "id": null,
        "invoice_payment_id": null,
        "pkp": null
      },
      "Expense": {
        "id": null,
        "name": null
      },
      "Invoice": {
        "id": null,
        "invoice_no_formatted": null
      }
    }
  ],
  "page": 1,
  "pageCount": 1,
  "perPage": 50
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Delete cash register item

Delete cash register item.

### Request

**URL**: `/cash_register_items/delete[/{ID}]`  
**HTTP method**: GET / POST  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/cash_register_items/delete/2
```


```sh
data='{"ids":"2,3"}';

curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/cash_register_items/delete
```

### Attributes

#### Required
none

But either ID or list of IDs must be specified. See *Optional attributes*.


#### Optional
URL parameter (GET method):

| name    | type   | description | default value |
| ------- | ------ | ----------- | ------------- |
| **id**  | int    | cash register item ID (GET method) | |

POST body parameter:

| name    | type   | description | default value |
| ------- | ------ | ----------- | ------------- |
| **ids** | string | list of IDs separated by comma (POST method) | |

### Response

#### Successfully deleted via GET

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/cash_register_items/delete/2
```

```json
{
  "Summary": {
    "minus": {
      "formatted": "0,00 <span class=\"currency_symbol\">€</span>",
      "raw": null
    },
    "plus": {
      "formatted": "102,00 <span class=\"currency_symbol\">€</span>",
      "raw": "102.00"
    },
    "total": {
      "formatted": "102,00 <span class=\"currency_symbol\">€</span>",
      "raw": "102.00"
    }
  },
  "status": 1
}
```

#### Successfully deleted via POST
```sh
data='{"ids":"2,3"}';

curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/cash_register_items/delete
```

```json
{
  "Summary": {
    "minus": {
      "formatted": "0,00 <span class=\"currency_symbol\">€</span>",
      "raw": null
    },
    "plus": {
      "formatted": "2,00 <span class=\"currency_symbol\">€</span>",
      "raw": "2.00"
    },
    "total": {
      "formatted": "2,00 <span class=\"currency_symbol\">€</span>",
      "raw": "2.00"
    }
  },
  "status": 1
}
```

#### Wrong item

```json
{
  "Summary": 0,
  "status": 0
}
```

#### Insufficient privileges
```json
{
  "error": 1,
  "error_message": "Ako používateľ typu Hosť nemáte oprávnenie na túto akciu."
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Get receipt from the cash register

Return receipt from the cash register in PDF file.

### Request

**URL**: `/cash_register_items/receipt/{ID}`  
**HTTP method**: GET

```sh
curl -X GET \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
    https://moja.superfaktura.sk/cash_register_items/receipt/1
```

### Attributes

#### Required

URL parameters:

| name   | type | description | default value |
| ------ | ---- | ----------- | ------------- |
| **id** | int  | receipt ID  |               |

### Response

PDF document on success. Check for HTTP code 404 in case of error.
