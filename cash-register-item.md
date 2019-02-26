# Cash register item

- [Get cash register items](#get-cash-register-items)
- [Delete cash register item](#delete-cash-register-item)
- [Add cash register item](#add-cash-register-item)

## Get cash register items

Get detailed information about cash register and its items.

### Request

**URL**: `/cash_register_items/index/{ID}`  
**HTTP method**: GET  


```sh
curl -X GET \
     -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
     https://moja.superfaktura.sk/cash_register_items/index/14/term:P201903
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
| **datefilter** | string | time filter (see [Value lists > Time filters](value-lists.md#time-filters)) | |
| **sum_from**   | float  | sum from    | |
| **sum_to**     | float  | sum to      | |
| **term**       | string | filter items in output search term (search in `description` and `cash_item_no_formatted`) | |
| **type**       | string | type filter ("in" for income and "out" for outgo) | `null` (both) |




### Response

```json
{
   "error" : "",
   "itemCount" : 1,
   "page" : 1,
   "pageCount" : 1,
   "perPage" : 50,
   "CashRegister" : {
      "currency" : "EUR",
      "description" : "",
      "eet_certificate_id" : null,
      "id" : "14",
      "id_provoz" : null,
      "name" : "Eurova",
      "sequence_in_no" : "P2019004",
      "sequence_out_no" : "V2019001",
      "sequencein_id" : "2820",
      "sequenceout_id" : "2821",
      "total" : "2022.14",
      "user_id" : "384",
      "user_profile_id" : "393"
   },
   "items" : [
      {
         "0" : {
            "has_storno" : "0"
         },
         "Invoice" : {
            "id" : null,
            "invoice_no_formatted" : null
         },
         "CashRegisterItem" : {
            "amount" : "15.00",
            "cash_item_no_formatted" : "P2019003",
            "client_id" : null,
            "client_name" : "",
            "created" : "2019-01-25 00:00:00",
            "description" : "",
            "eet_receipt_id" : null,
            "expense_id" : null,
            "id" : "198",
            "invoice_id" : null,
            "invoice_payment_id" : null
         },
         "EetReceipt" : {
            "celk_trzba" : null,
            "created" : null,
            "fik" : null,
            "id" : null,
            "invoice_payment_id" : null,
            "pkp" : null
         },
         "Expense" : {
            "id" : null,
            "name" : null
         }
      }
   ]
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
    https://moja.superfaktura.sk/cash_register_items/delete/198
```


```sh
data='{"ids":"203,204"}';

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

### Successfully deleted via GET

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/cash_register_items/delete/198
```

```json
{
   "Summary" : {
      "plus" : {
         "formatted" : "2 007,14 <span class=\"currency_symbol\">€</span>",
         "raw" : "2007.14"
      },
      "minus" : {
         "formatted" : "0,00 <span class=\"currency_symbol\">€</span>",
         "raw" : null
      },
      "total" : {
         "raw" : "2007.14",
         "formatted" : "2 007,14 <span class=\"currency_symbol\">€</span>"
      }
   },
   "status" : 1
}
```


### Successfully deleted via POST
```sh
data='{"ids":"203,204"}';

curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/cash_register_items/delete
```

```json
{
   "Summary" : {
      "total" : {
         "raw" : "2007.14",
         "formatted" : "2 007,14 <span class=\"currency_symbol\">€</span>"
      },
      "minus" : {
         "formatted" : "0,00 <span class=\"currency_symbol\">€</span>",
         "raw" : null
      },
      "plus" : {
         "formatted" : "2 007,14 <span class=\"currency_symbol\">€</span>",
         "raw" : "2007.14"
      }
   },
   "status" : 1
}
```

### Wrong item

```json
{
   "status" : 1,
   "Summary" : 0
}
```

#### Insufficient privileges
```json
{
   "message" : "Nemôžete zmazať pohyb v pokladni",
   "error" : 1,
   "error_message" : "Nemôžete zmazať pohyb v pokladni"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



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
    "CashRegisterItem":{
        "amount":14,
        "cash_register_id":6
    }
}';

# richer example
data='{
    "CashRegisterItem":{
        "amount":14,
        "cash_register_id":6,
        "created":"2069-01-31 02:00:00",
        "invoice_id":150,
        "description":"Invoice no. 2069001"
    }
}';

curl -X POST \
    -d "data=$data" \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
     https://moja.superfaktura.sk/cash_register_items/add/
```

```json
{
   "status" : "1",
   "CashRegisterItem" : {
      "cash_register_id" : 6,
      "created_formatted" : "21.05.2018 08:33:15",
      "amount_formatted" : "14.00 <span class=\"currency_symbol\">MXN</span>",
      "exchange_rate" : 1.1781,
      "currency" : "MXN",
      "id" : "112",
      "cash_item_no_formatted" : "",
      "created" : "2018-05-21 08:33:15",
      "type" : 0,
      "cash_item_no" : "",
      "sequence_id" : null,
      "sequence_cnt" : 3,
      "amount" : 14
   },
   "CashRegister" : {
      "sequence_out_no" : "",
      "sequence_in_no" : ""
   },
   "Summary" : {
      "minus" : {
         "value" : null,
         "formatted" : "0.00 <span class=\"currency_symbol\">MXN</span>"
      },
      "plus" : {
         "formatted" : "614.00 <span class=\"currency_symbol\">MXN</span>",
         "value" : "614.00"
      },
      "total" : {
         "value" : "614.00",
         "formatted" : "614.00 <span class=\"currency_symbol\">MXN</span>"
      }
   },
   "flag" : ""
}
```


#### Successfully added with invoice ID

```json
{
   "flag" : "",
   "Invoice" : {
      "amount" : "30.95",
      "amount_paid" : "12.00",
      "client_data" : "{\"Client\":{\"id\":\"431\",\"name\":\"2day, s. r. o.\",\"address\":\"Pri Suchom mlyne 6\",\"ico\":\"44981082\",\"email\":\"\",\"zip\":\"811 04\",\"dic\":\"2022903949\",\"phone\":\"\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"ic_dph\":\"\",\"fax\":\"\",\"country_id\":\"191\",\"state\":\"\",\"delivery_name\":\"\",\"delivery_zip\":\"\",\"delivery_city\":\"\",\"delivery_address\":\"\",\"delivery_phone\":\"\",\"delivery_country_id\":\"191\",\"delivery_state\":\"\",\"updateClient\":\"0\",\"country\":\"Slovensko\",\"delivery_country\":\"Slovensko\"}}",
      "client_id" : "431",
      "comment" : "",
      "constant" : "",
      "country_exchange_rate" : "0.03884249",
      "created" : "2019-01-30 00:00:00",
      "delivery" : "2019-01-30 00:00:00",
      "delivery_type" : "",
      "demo" : "0",
      "deposit" : "0.00",
      "discount" : "0",
      "due" : "2019-02-13",
      "estimate_id" : null,
      "exchange_rate" : "1.00000000000000",
      "header_comment" : "",
      "home_currency" : "EUR",
      "id" : "1285",
      "import_id" : null,
      "import_parent_id" : null,
      "import_type" : null,
      "internal_comment" : null,
      "invoice_currency" : "EUR",
      "invoice_no" : "3",
      "invoice_no_formatted" : "2019003",
      "issued_by" : "superfaktura.sk, s.r.o.",
      "issued_by_email" : "api@example.com",
      "issued_by_phone" : "",
      "issued_by_web" : "",
      "items_data" : "asdf , Item B SKU: itemb1241\r\nPublic description of this item, ",
      "items_name" : null,
      "lang" : "slo",
      "mask" : "YYYYNNN",
      "modified" : "2019-02-06 11:42:22",
      "my_data" : "{\"MyData\":{\"id\":\"393\",\"user_id\":\"384\",\"user_profile_id\":\"\",\"country_id\":\"191\",\"company_name\":\"superfaktura.sk, s.r.o.\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"tax_payer\":\"1\",\"logo_key\":\"\",\"logo_id\":\"\",\"web\":\"\",\"Logo\":\"[{\\\"id\\\":\\\"168\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"393\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"9997f862be767814ce9b_393_screen_shot_2018_10_03_at_10_03_19.png\\\",\\\"checksum\\\":\\\"dd3300a5a4fc754b0f1361baa2ac2e3f\\\",\\\"group\\\":\\\"logo\\\",\\\"default\\\":\\\"1\\\",\\\"alternative\\\":null,\\\"created\\\":\\\"2019-01-23 08:37:27\\\",\\\"modified\\\":\\\"2019-01-23 08:39:56\\\"}]\",\"Signature\":\"{\\\"id\\\":\\\"169\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"393\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"51ee3f8bbd61561eb5f0_393_podpis_1.png\\\",\\\"checksum\\\":\\\"33b5238616646ca28ebabc02f713a59f\\\",\\\"group\\\":\\\"signature\\\",\\\"default\\\":\\\"0\\\",\\\"alternative\\\":null,\\\"created\\\":\\\"2019-01-23 08:37:27\\\",\\\"modified\\\":\\\"2019-01-23 08:37:27\\\"}\",\"travel_agencies\":\"0\",\"business_register\":\"Bratislava I, odd. Sro, vl.\\u010d.81403\\/B\",\"BankAccount\":[{\"show_account\":\"1\",\"id\":\"264\",\"default\":\"0\",\"country_id\":\"191\",\"bank_name\":\"FatraBanka\",\"bank_code\":\"\",\"account\":\"\",\"iban\":\" SK 31 1200 000019 8742637541\",\"swift\":\"9876\"},{\"show_account\":\"1\",\"id\":\"265\",\"default\":\"\",\"country_id\":\"191\",\"bank_name\":\"SuperBanka\",\"bank_code\":\"1200\",\"account\":\"8742637541\",\"iban\":\"\",\"swift\":\"\"}],\"update_profile\":\"0\",\"country\":\"Slovensko\"}}",
      "name" : "Faktúra 2019003",
      "order_no" : "",
      "paid" : "12.00",
      "parent_id" : null,
      "paydate" : "2019-02-06 12:05:50",
      "payment_type" : "cash",
      "proforma_id" : null,
      "recurring" : null,
      "rounding" : "item",
      "sequence_id" : "2815",
      "special_vat_scheme" : null,
      "specific" : "",
      "status" : "2",
      "summary_invoice" : null,
      "tags" : "",
      "tax_document" : "0",
      "taxdate" : "2019-01-30",
      "token" : "aa582995",
      "type" : "regular",
      "user_id" : "384",
      "user_profile_id" : "393",
      "variable" : "2019003",
      "vat" : "6.19",
      "vat_transfer" : "0"
   },
   "Summary" : {
      "total" : {
         "value" : "2283.14",
         "formatted" : "2 283,14 <span class=\"currency_symbol\">€</span>"
      },
      "plus" : {
         "value" : "2283.14",
         "formatted" : "2 283,14 <span class=\"currency_symbol\">€</span>"
      },
      "minus" : {
         "formatted" : "0,00 <span class=\"currency_symbol\">€</span>",
         "value" : null
      }
   },
   "CashRegister" : {
      "sequence_in_no" : "",
      "sequence_out_no" : ""
   },
   "CashRegisterItem" : {
      "amount" : 12,
      "amount_formatted" : "12,00 <span class=\"currency_symbol\">€</span>",
      "cash_item_no" : "",
      "cash_item_no_formatted" : "",
      "cash_register_id" : 14,
      "client_id" : "431",
      "client_name" : "2day, s. r. o.",
      "created" : "2019-02-06 12:05:50",
      "created_formatted" : "06.02.2019 12:05:50",
      "currency" : "EUR",
      "description" : "Test description",
      "exchange_rate" : 1,
      "id" : "230",
      "invoice_id" : 1285,
      "sequence_cnt" : 3,
      "sequence_id" : null,
      "type" : 0
   },
   "status" : "1"
}
```


#### Insufficient privileges

```json
{
   "error" : 1,
   "error_message" : "Nemôžete pridať pohyb v pokladni",
   "message" : "Nemôžete pridať pohyb v pokladni"
}
```


#### Valid EET request

```json
{
   "EetReceipt" : {
      "celk_trzba" : 12,
      "cerp_zuct" : 0,
      "created" : "2019-02-06 11:30:59",
      "dan1" : 0,
      "dan2" : 0,
      "dat_trzby_internal" : "2019-02-06",
      "data" : "{\"uuid_zpravy\":\"f6f53fa6-c590-49a4-9159-616f70a46e9c\",\"prvni_zaslani\":true,\"dic_popl\":\"CZ1212121218\",\"dic_poverujiciho\":null,\"id_provoz\":\"10\",\"id_pokl\":\"eet2\",\"porad_cis\":\"2019007\",\"dat_trzby\":{\"date\":\"2019-02-06 11:30:50.000000\",\"timezone_type\":3,\"timezone\":\"UTC\"},\"celk_trzba\":12,\"zakl_nepodl_dph\":0,\"zakl_dan1\":0,\"dan1\":0,\"zakl_dan2\":0,\"dan2\":0,\"zakl_dan3\":0,\"dan3\":0,\"cest_sluz\":0,\"pouzit_zboz1\":0,\"pouzit_zboz2\":0,\"pouzit_zboz3\":0,\"urceno_cerp_zuct\":0,\"cerp_zuct\":0,\"rezim\":0}",
      "exchange_rate" : 1,
      "fik" : "06d2064d-f8a7-47c1-8668-46bcf8ef009c-ff",
      "id_pokl" : "eet2",
      "id_provoz" : "10",
      "modified" : "2019-02-06 11:30:59",
      "pouzit_zboz2" : 0,
      "prvni_zaslani" : true,
      "rezim" : 0,
      "test" : true,
      "urceno_cerp_zuct" : 0,
      "user_id" : "3",
      "user_profile_id" : "10",
      "uuid_zpravy" : "f6f53fa6-c590-49a4-9159-616f70a46e9c",
      "zakl_dan3" : 0,
      "zakl_nepodl_dph" : 0,
      "CashRegister" : {
         "currency" : "CZK",
         "description" : "",
         "eet_certificate_id" : "1",
         "id" : "8",
         "id_provoz" : "10",
         "name" : "eet2",
         "sequencein_id" : "78",
         "sequenceout_id" : "79",
         "user_id" : "3",
         "user_profile_id" : "10"
      },
      "amount" : 12,
      "cash_register_id" : "8",
      "dan3" : 0,
      "dat_trzby" : "2019-02-06 11:30:50",
      "dic_poverujiciho" : null,
      "id" : "63",
      "pouzit_zboz3" : 0,
      "zakl_dan1" : 0,
      "EetCertificate" : {
         "created" : "2018-02-20 15:16:40",
         "dic" : "CZ1212121218",
         "hash" : "237c6fc9",
         "id" : "1",
         "modified" : "2018-02-20 15:16:40",
         "name" : "test",
         "private_key" : "LbKL...CxTmzhq",
         "public_key" : "-----BEGIN CERTIFICATE-----\nMIIEmD...dE5Jybveo6ae8HNx4w==\n-----END CERTIFICATE-----\n",
         "user_profile_id" : "10",
         "valid_from" : "2016-09-30 09:02:44",
         "valid_to" : "2019-09-30 09:02:44"
      },
      "bkp" : "47ad323c-2d30c1e7-b2a42c05-2b4218d3-0171640b",
      "cest_sluz" : 0,
      "currency" : "CZK",
      "dat_prij" : "2019-02-06 11:31:03",
      "dic_popl" : "CZ1212121218",
      "pkp" : "a4OD3q...vXtyQ==",
      "porad_cis" : "2019007",
      "pouzit_zboz1" : 0,
      "upid" : "10",
      "zakl_dan2" : 0
   },
   "CashRegister" : {
      "sequence_in_no" : "",
      "sequence_out_no" : ""
   },
   "CashRegisterItem" : {
      "amount" : 12,
      "amount_formatted" : "12,00 <span class=\"currency_symbol\">Kč</span>",
      "cash_item_no" : "2019007",
      "cash_item_no_formatted" : "2019007",
      "cash_register_id" : 8,
      "created" : "2019-02-06 12:05:50",
      "created_formatted" : "06.02.2019 12:05:50",
      "currency" : "CZK",
      "exchange_rate" : 1,
      "id" : "227",
      "is_eet" : true,
      "sequence_cnt" : 0,
      "sequence_id" : null,
      "type" : 0
   },
   "flag" : "fully-paid",
   "status" : "1",
   "Summary" : {
      "minus" : {
         "value" : "-607.20",
         "formatted" : "-607,20 <span class=\"currency_symbol\">Kč</span>"
      },
      "plus" : {
         "formatted" : "4 769,00 <span class=\"currency_symbol\">Kč</span>",
         "value" : "4769.00"
      },
      "total" : {
         "value" : "4161.80",
         "formatted" : "4 161,80 <span class=\"currency_symbol\">Kč</span>"
      }
   }
}
```


#### Invalid EET request
```json
{
   "EetReceipt" : {
      "amount" : 12,
      "cash_register_id" : "8",
      "created" : "2019-02-06 11:16:19",
      "currency" : "CZK",
      "dan1" : 0,
      "data" : "{\"uuid_zpravy\":\"c246d2d8-3e40-4d8f-ad65-cf33183d7424\",\"prvni_zaslani\":true,\"dic_popl\":\"CZ1212121218\",\"dic_poverujiciho\":null,\"id_provoz\":\"10\",\"id_pokl\":\"eet2\",\"porad_cis\":\"\",\"dat_trzby\":{\"date\":\"2019-02-06 11:16:19.000000\",\"timezone_type\":3,\"timezone\":\"UTC\"},\"celk_trzba\":12,\"zakl_nepodl_dph\":0,\"zakl_dan1\":0,\"dan1\":0,\"zakl_dan2\":0,\"dan2\":0,\"zakl_dan3\":0,\"dan3\":0,\"cest_sluz\":0,\"pouzit_zboz1\":0,\"pouzit_zboz2\":0,\"pouzit_zboz3\":0,\"urceno_cerp_zuct\":0,\"cerp_zuct\":0,\"rezim\":0}",
      "dic_popl" : "CZ1212121218",
      "exchange_rate" : 1,
      "id" : "56",
      "id_provoz" : "10",
      "kod" : 3,
      "modified" : "2019-02-06 11:16:19",
      "pkp" : "a4OD3q...vXtyQ==",
      "porad_cis" : "",
      "pouzit_zboz1" : 0,
      "pouzit_zboz2" : 0,
      "pouzit_zboz3" : 0,
      "prvni_zaslani" : true,
      "rezim" : 0,
      "upid" : "10",
      "uuid_zpravy" : "c246d2d8-3e40-4d8f-ad65-cf33183d7424",
      "zakl_dan3" : 0,
      "zakl_nepodl_dph" : 0,
      "CashRegister" : {
         "currency" : "CZK",
         "description" : "",
         "eet_certificate_id" : "1",
         "id" : "8",
         "id_provoz" : "10",
         "name" : "eet2",
         "sequencein_id" : "78",
         "sequenceout_id" : "79",
         "user_id" : "3",
         "user_profile_id" : "10"
      },
      "bkp" : "f9a4049e-a83990fc-d5777156-ec888ad7-bb3ec795",
      "chyba" : "XML zprava nevyhovela kontrole XML schematu",
      "dan3" : 0,
      "dat_trzby" : "2019-02-06 11:16:19",
      "dat_trzby_internal" : "2019-02-06",
      "user_profile_id" : "10",
      "zakl_dan1" : 0,
      "EetCertificate" : {
         "created" : "2018-02-20 15:16:40",
         "dic" : "CZ1212121218",
         "hash" : "237c6fc9",
         "id" : "1",
         "modified" : "2018-02-20 15:16:40",
         "name" : "test",
         "private_key" : "LbKL...CxTmzhq",
         "public_key" : "-----BEGIN CERTIFICATE-----\nMIIEmD...dE5Jybveo6ae8HNx4w==\n-----END CERTIFICATE-----\n",
         "user_profile_id" : "10",
         "valid_from" : "2016-09-30 09:02:44",
         "valid_to" : "2019-09-30 09:02:44"
      },
      "celk_trzba" : 12,
      "cerp_zuct" : 0,
      "cest_sluz" : 0,
      "dan2" : 0,
      "dic_poverujiciho" : null,
      "id_pokl" : "eet2",
      "urceno_cerp_zuct" : 0,
      "user_id" : "3",
      "zakl_dan2" : 0
   },
   "CashRegisterItem" : {
      "amount" : 12,
      "amount_formatted" : "12,00 <span class=\"currency_symbol\">Kč</span>",
      "cash_item_no" : "",
      "cash_item_no_formatted" : "",
      "cash_register_id" : 8,
      "created" : "2019-02-06 12:05:50",
      "created_formatted" : "06.02.2019 12:05:50",
      "currency" : "CZK",
      "exchange_rate" : 1,
      "id" : "220",
      "is_eet" : true,
      "sequence_cnt" : 6,
      "sequence_id" : null,
      "type" : 0
   },
   "status" : "1",
   "CashRegister" : {
      "sequence_in_no" : "",
      "sequence_out_no" : ""
   },
   "Summary" : {
      "plus" : {
         "value" : "4698.00",
         "formatted" : "4 698,00 <span class=\"currency_symbol\">Kč</span>"
      },
      "total" : {
         "value" : "4090.80",
         "formatted" : "4 090,80 <span class=\"currency_symbol\">Kč</span>"
      },
      "minus" : {
         "formatted" : "-607,20 <span class=\"currency_symbol\">Kč</span>",
         "value" : "-607.20"
      }
   },
   "flag" : "due"
}
```