# Expenses

- [Add expense](#add-expense)
- [Edit expense](#edit-expense)
- [Expense detail](#expense-detail)
- [Get list of expenses](#get-list-of-expenses)
- [Delete expense](#delete-expense)

Expense payments  
- [Add expense payment](#add-expense-payment)
- [Delete expense payment](#delete-expense-payment)


## Add expense

Add new expense.
If you want to add tags to expense, refer to [FAQ > How do I add tags to an entity?](faq.md#how-do-i-add-tags-to-an-entity).

### Request

**URL**: `/expenses/add`  
**HTTP method**: POST  

```sh
# simple example
data='{
  "Expense": {
    "name": "Foo bar",
    "currency": "EUR",
    "amount": 12.14
  }
}';

# multiple VAT rates example
data='{
    "Expense":{
        "name":"Expense with multiple VAT rates",
        "vat": 21,
        "amount": 100,
        "vat2": 10,
        "amount2": 100,
        "vat3": 0,
        "amount3": 100
    }
}';

# example with Expense extra
data='{
    "Expense":{
        "name": "Foo bar 2",
        "currency": "NOK",
        "amount": 12.14,
        "vat": 21
    },
    "ExpenseExtra":{
        "vat_transfer": 1
    }
}';

# example with items
data='{
    "Expense":{
        "name":"Expense with items"
    },
    "ExpenseItem":[
        {
            "description": "description of item 1",
            "name": "item 1",
            "tax": 20,
            "unit_price": 10
        }
    ]
}';


curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/expenses/add



# ================================================

# example with attachment
base64_attachment=$(base64 -w 0 /tmp/foo.pdf);

curl -X POST \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    -d @- \
    https://moja.superfaktura.sk/expenses/add <<CURL_DATA
    data={
        "Expense":{
            "name":"Expense with multiple VAT rates",
            "vat": 21,
            "amount": 100,
            "vat2": 10,
            "amount2": 100,
            "vat3": 0,
            "amount3": 100,
            "attachment":"$base64_attachment"
        }
    }
CURL_DATA
```  

### Attributes

#### Required

| name     | type   | description  | default value |
| -------- | ------ | ------------ | ------------- |
| **name** | string | expense name |               |

#### Optional

##### Expense

| name                    | type   | description                                                         | default value |
| ----------------------- | ------ | ------------------------------------------------------------------- | ------------- |
| **attachment**          | string | base64 encoded attachment - max file size: 4MB, allowed types: `jpg`, `jpeg`, `png`, `tif`, `tiff`, `gif`, `pdf`, `tmp`, `xls`, `xlsx`, `ods`, `doc`, `docx`, `xml`, `csv`, `msg` | |
| **already_paid**        | int    | is invoice already paid? (0=no, 1=yes)                              | 0 |
| **amount**              | float  | amount of money without VAT                                         | 0 |
| **amount2**             | float  | amount of money without VAT (when multiple VAT rates are necessary) | 0 |
| **amount3**             | float  | amount of money without VAT (when multiple VAT rates are necessary) | 0 |
| **client_id**           | int    | client ID                                                           | |
| **comment**             | string | comment                                                             | |
| **constant**            | string | constant symbol                                                     | |
| **created**             | date   | issue date                                                          | &lt;current date&gt; |
| **currency**            | string | currency (see [Value lists > Currencies](value-lists.md#currencies))                    | &lt;home currency&gt; |
| **delivery**            | date   | delivery date                                                       | &lt;current date&gt; |
| **document_number**     | string | document number, (e.g. invoice number, bill number, ...)            | |
| **due**                 | date   | due date                                                            | &lt;current date&gt; |
| **expense_category_id** | int    | expense category ID (see [Value lists > Expense categories](value-lists.md#expense-categories)) | |
| **payment_type**        | string | payment type (see [Value lists > Payment types](value-lists.md#payment-types))             | |
| **specific**            | string | specific symbol                                                     | |
| **taxable_supply**      | date   | date of taxable transaction                                         | null |
| **type**                | string | expense typ (see [Value lists > Invoice types](value-lists.md#invoice-types))              | 'invoice' |
| **variable**            | string | variable symbol                                                     | |
| **vat**                 | string | VAT in percent                                                      | 0 |
| **vat2**                | string | VAT in percent (when multiple VAT rates are necessary)              | 0 |
| **vat3**                | string | VAT in percent (when multiple VAT rates are necessary)              | 0 |

##### Expense extras

| name                    | type   | description                                                         | default value |
| ----------------------- | ------ | ------------------------------------------------------------------- | ------------- |
| **vat_transfer**        | int    | Flag determines whether the document VAT is transfered to supplier  | |


### Response

#### Successful creation
```json
{
  "data": {
    "Client": [],
    "Document": [],
    "Expense": {
      "accounting_date": "2050-01-01 23:59:59",
      "amount": 12.14,
      "amount2": null,
      "amount3": null,
      "amount_country_home": "12.1400",
      "amount_home": "12.1400",
      "amount_paid": 0,
      "amount_paid_vat": 0,
      "client_data": null,
      "client_id": null,
      "comment": null,
      "constant": null,
      "country_exchange_rate": "1.00000000000000",
      "created": "2050-01-01 23:59:59",
      "currency": "EUR",
      "delivery": "2050-01-01 23:59:59",
      "demo": "0",
      "discount": "0",
      "discount_total": "0.0000",
      "document_number": null,
      "due": "2050-01-01 23:59:59",
      "exchange_rate": "1.00000000000000",
      "expense_category_id": null,
      "expense_no": "1",
      "flag": "issued",
      "home_currency": "EUR",
      "id": "1",
      "missing_bank_account": true,
      "modified": "2050-01-01 23:59:59",
      "my_data": "{\"id\":\"1\",\"user_id\":1,\"country_id\":\"191\",\"company_name\":\"SuperFaktura, s.r.o.\",\"name\":null,\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"business_register\":\"Obchodn\\u00fd register Okresn\\u00e9ho s\\u00fadu Bratislava I, oddiel: Sro, vlo\\u017eka \\u010d. 81403\\/B\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"tax_payer\":\"1\",\"vat_interval\":null,\"company_type\":\"ltd\"}",
      "name": "Foo bar",
      "number": "2020001",
      "paid": 0,
      "paid_vat": 0,
      "paydate": null,
      "qr": "",
      "qr_type": "",
      "qr_url": "",
      "qr_url_max": "",
      "rates": [],
      "recurring": null,
      "sequence_id": "9",
      "specific": null,
      "status": "1",
      "tags": null,
      "tax": null,
      "tax_code": null,
      "taxable_supply": null,
      "taxdate": "2050-01-01",
      "total": "12.1400",
      "total_country_home": "12.1400",
      "total_home": "12.1400",
      "type": "invoice",
      "user_id": "1",
      "user_profile_id": "1",
      "variable": null,
      "vat": 0,
      "vat2": null,
      "vat3": null,
      "version": "basic"
    },
    "ExpenseBasicRate": [
      {
        "amount": "12.1400",
        "id": "1",
        "tax": "0.00",
        "total": "12.1400"
      }
    ],
    "ExpenseExtra": [],
    "ExpenseItem": [
      {
        "description": null,
        "discount": "0.00000",
        "discount_description": null,
        "id": "1",
        "name": null,
        "ordernum": "0",
        "quantity": "1.00000",
        "stock_item_id": null,
        "tax": "0.00",
        "total": "12.1400",
        "type": "rate",
        "unit": null,
        "unit_price": "12.1400",
        "unit_total": "12.1400"
      }
    ],
    "ExpensePayment": [],
    "MyData": {
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
      "name": null,
      "tax_payer": "1",
      "user_id": 1,
      "vat_interval": null,
      "zip": "811 04"
    },
    "RelatedItem": [],
    "Tag": [],
    "VatSummary": [
      {
        "base": 12.14,
        "vat": 0
      }
    ],
    "attachments": []
  },
  "error": 0,
  "error_message": "",
  "status": 1
}
```

#### Insufficient privileges
HTTP status 403.

```json
{
  "error": 1,
  "error_message": "Ako používateľ typu Hosť nemáte oprávnenie na túto akciu.",
  "message": "Ako používateľ typu Hosť nemáte oprávnenie na túto akciu."
}
```

#### Not enough data
```json
{
  "error": 1,
  "error_message": {
    "name": [
      "Zadajte názov"
    ]
  }
}
```

#### Missing data
HTTP status 400.

```json
{
  "error": 1,
  "error_message": "Chýbajúce údaje",
  "message": "Chýbajúce údaje"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Edit expense

Edit expense.

It's strongly recommended fetching data for expense, change required values, and then request edit.
If you want to add tags to expense, refer to [FAQ > How do I add tags to an entity?](faq.md#how-do-i-add-tags-to-an-entity)

### Request

**URL**: `/expenses/edit`  
**HTTP method**: POST  

```sh
data='{
  "Expense":{
    "id":"1",
    "name":"Foo bar",
    "currency":"EUR",
    "amount":19.95,
    "due":"2148-01-01"
  }
}';

curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/expenses/edit
```  

Edit expense with items:
```sh
data='{
    "Expense":{
        "id": 30,
        "name":"Expense with items edited"
    },
    "ExpenseItem":[
        {
            "id": 32,
            "description": "Description of item 1",
            "name": "Item 1",
            "tax": 25,
            "unit_price": 100
        },
        {
            "description": "Description of new item",
            "name": "Item 2",
            "tax": 15,
            "quantity": 1,
            "unit_price": 100
        }
    ]
}';

curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/expenses/edit
```

### Attributes
#### Required

| name   | type | description  | default value |
| ------ | ---- | ------------ | ------------- |
| **id** | int  | expense id   |               |

#### Optional

Same as for [Add expense](#add-expense). With the exception of *name* being optional.

### Response

#### Successfully edited
```json
{
  "data": {
    "Client": [],
    "Document": [],
    "Expense": {
      "accounting_date": "2050-01-01 23:59:59",
      "amount": 19.95,
      "amount2": null,
      "amount3": null,
      "amount_country_home": "19.9500",
      "amount_home": "19.9500",
      "amount_paid": 0,
      "amount_paid_vat": 0,
      "client_data": null,
      "client_id": null,
      "comment": null,
      "constant": null,
      "country_exchange_rate": "1.00000000000000",
      "created": "2050-01-01 23:59:59",
      "currency": "EUR",
      "delivery": "2050-01-01 23:59:59",
      "demo": "0",
      "discount": "0",
      "discount_total": "0.0000",
      "document_number": null,
      "due": "2148-01-01 00:00:00",
      "exchange_rate": "1.00000000000000",
      "expense_category_id": null,
      "expense_no": "1",
      "flag": "issued",
      "home_currency": "EUR",
      "id": "1",
      "missing_bank_account": true,
      "modified": "2050-01-01 23:59:59",
      "my_data": "{\"id\":\"1\",\"user_id\":1,\"country_id\":\"191\",\"company_name\":\"SuperFaktura, s.r.o.\",\"name\":null,\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"business_register\":\"Obchodn\\u00fd register Okresn\\u00e9ho s\\u00fadu Bratislava I, oddiel: Sro, vlo\\u017eka \\u010d. 81403\\/B\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"tax_payer\":\"1\",\"vat_interval\":null,\"company_type\":\"ltd\"}",
      "name": "Foo bar",
      "number": "2020001",
      "paid": 0,
      "paid_vat": 0,
      "paydate": null,
      "qr": "",
      "qr_type": "",
      "qr_url": "",
      "qr_url_max": "",
      "rates": [],
      "recurring": null,
      "sequence_id": "9",
      "specific": null,
      "status": "1",
      "tags": null,
      "tax": null,
      "tax_code": null,
      "taxable_supply": null,
      "taxdate": "2050-01-01",
      "total": "19.9500",
      "total_country_home": "19.9500",
      "total_home": "19.9500",
      "type": "invoice",
      "user_id": "1",
      "user_profile_id": "1",
      "variable": null,
      "vat": 0,
      "vat2": null,
      "vat3": null,
      "version": "basic"
    },
    "ExpenseBasicRate": [
      {
        "amount": "19.9500",
        "id": "1",
        "tax": "0.00",
        "total": "19.9500"
      }
    ],
    "ExpenseExtra": [],
    "ExpenseItem": [
      {
        "description": null,
        "discount": "0.00000",
        "discount_description": null,
        "id": "1",
        "name": null,
        "ordernum": "0",
        "quantity": "1.00000",
        "stock_item_id": null,
        "tax": "0.00",
        "total": "19.9500",
        "type": "rate",
        "unit": null,
        "unit_price": "19.9500",
        "unit_total": "19.9500"
      }
    ],
    "ExpensePayment": [],
    "MyData": {
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
      "name": null,
      "tax_payer": "1",
      "user_id": 1,
      "vat_interval": null,
      "zip": "811 04"
    },
    "RelatedItem": [],
    "Tag": [],
    "VatSummary": [
      {
        "base": 19.95,
        "vat": 0
      }
    ],
    "attachments": []
  },
  "error": 0,
  "error_message": "",
  "status": 1
}
```

#### Bad data format / missing expense ID
```json
{
  "error": 3,
  "error_message": "Bad data format."
}
```

#### Wrong expense
```json
{
  "error": 1,
  "error_message": "Expense not found",
  "message": "Expense not found"
}
```

#### Insufficient privileges

HTTP status 403.

```json
{
  "error": 1,
  "error_message": "Ako používateľ typu Hosť nemáte oprávnenie na túto akciu.",
  "message": "Ako používateľ typu Hosť nemáte oprávnenie na túto akciu."
}
```

#### Unable to save
```json
{
   "error" : 5,
   "error_message" : "The expense could not be saved. Please, try again.",
   "message" : "The expense could not be saved. Please, try again."
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Expense detail

### Request

**URL**: `/expense/view/{ID}.json`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/expenses/view/1.json
```

### Attributes
#### Required

URL parameters:

| name   | type   | description | default value |
| ------ | ------ | ----------- | ------------- |
| **id** | int    | expense ID  |               |

#### Optional
none

### Response

#### Successfully show details
```json
{
  "Client": [],
  "Document": [],
  "Expense": {
    "accounting_date": "2050-01-01 23:59:59",
    "amount": 12.14,
    "amount2": null,
    "amount3": null,
    "amount_country_home": "12.1400",
    "amount_home": "12.1400",
    "amount_paid": 0,
    "amount_paid_vat": 0,
    "client_data": null,
    "client_id": null,
    "comment": null,
    "constant": null,
    "country_exchange_rate": "1.00000000000000",
    "created": "2050-01-01 23:59:59",
    "currency": "EUR",
    "delivery": "2050-01-01 23:59:59",
    "demo": "0",
    "discount": "0",
    "discount_total": "0.0000",
    "document_number": null,
    "due": "2050-01-01 23:59:59",
    "exchange_rate": "1.00000000000000",
    "expense_category_id": null,
    "expense_no": "1",
    "flag": "issued",
    "home_currency": "EUR",
    "id": "1",
    "missing_bank_account": true,
    "modified": "2050-01-01 23:59:59",
    "my_data": "{\"id\":\"1\",\"user_id\":1,\"country_id\":\"191\",\"company_name\":\"SuperFaktura, s.r.o.\",\"name\":null,\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"business_register\":\"Obchodn\\u00fd register Okresn\\u00e9ho s\\u00fadu Bratislava I, oddiel: Sro, vlo\\u017eka \\u010d. 81403\\/B\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"tax_payer\":\"1\",\"vat_interval\":null,\"company_type\":\"ltd\"}",
    "name": "Foo bar",
    "number": "2020001",
    "paid": 0,
    "paid_vat": 0,
    "paydate": null,
    "qr": "",
    "qr_type": "",
    "qr_url": "",
    "qr_url_max": "",
    "rates": {
      "0.00": {
        "base": 12.14,
        "vat": 0
      }
    },
    "recurring": null,
    "sequence_id": "9",
    "specific": null,
    "status": "1",
    "tags": null,
    "tax": null,
    "tax_code": null,
    "taxable_supply": null,
    "taxdate": "2050-01-01",
    "total": "12.1400",
    "total_country_home": "12.1400",
    "total_home": "12.1400",
    "type": "invoice",
    "user_id": "1",
    "user_profile_id": "1",
    "variable": null,
    "vat": 0,
    "vat2": null,
    "vat3": null,
    "version": "basic"
  },
  "ExpenseBasicRate": [
    {
      "amount": "12.1400",
      "id": "1",
      "tax": "0.00",
      "total": "12.1400"
    }
  ],
  "ExpenseExtra": [],
  "ExpenseItem": [
    {
      "description": null,
      "discount": "0.00000",
      "discount_description": null,
      "id": "1",
      "name": null,
      "ordernum": "0",
      "quantity": "1.00000",
      "stock_item_id": null,
      "tax": "0.00",
      "total": "12.1400",
      "type": "rate",
      "unit": null,
      "unit_price": "12.1400",
      "unit_total": "12.1400"
    }
  ],
  "ExpensePayment": [],
  "MyData": {
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
    "name": null,
    "tax_payer": "1",
    "user_id": 1,
    "vat_interval": null,
    "zip": "811 04"
  },
  "RelatedItem": [],
  "Tag": [],
  "VatSummary": [
    {
      "base": 12.14,
      "vat": 0
    }
  ],
  "attachments": []
}
```

#### Wrong expense
```json
{
  "error": 1,
  "error_message": "Expense not found",
  "message": "Expense not found"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Get list of expenses

Get list of expenses

### Request

**URL**: `/expenses/index.json[/{ATTRIBUTE}:{VALUE}]*`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
    https://moja.superfaktura.sk/expenses/index.json/listinfo:1/per_page:1/page:2/sort:ico
```

### Attributes

From pattern URL, `ATTRIBUTE` is name of attribute in table below.

#### Required
none

#### Optional

URL parameters:

| name                   | type   | description | default value |
| ---------------------- | ------ | ----------- | ------------- |
| **amount_from**        | float  | minimum amount of money | |
| **amount_to**          | float  | maximum amount of money | |
| **category**           | int    | category ID  | |
| **client_id**          | int    | client ID | |
| **created**            | int    | constant specifying time filtering (see [Value lists > Time filter constants](value-lists.md#time-filter-constants)) | |
| **created_since**      | date   | created date since (requires `created:3`) | |
| **created_to**         | date   | created date until (requires `created:3`) | |
| **delivery**           | int    | constant specifying time filtering (see [Value lists > Time filter constants](value-lists.md#time-filter-constants)) | |
| **delivery_since**     | date   | delivery date since (requires `delivery:3`) | |
| **delivery_to**        | date   | delivery date until (requires `delivery:3`) | |
| **direction**          | string | sorting direction (ASC or DESC) | DESC |
| **due**                | date   | due date | |
| **listinfo**           | int    | show meta data about result? (0=no, 1=yes) | 0 |
| **page**               | int    | page number | 1 |
| **payment_type**       | string | payment type (see [Value lists > Payment types](value-lists.md#payment-types)) | |
| **per_page**           | int    | number of items per page (max 100) | &gt;as set in profile&lt; |
| **search**             | string | base64 encoded string (e.g. `test` = `dGVzdA,,`) | |
| **sort**               | string | attribute to sort by, default regular_count | ASC |
| **status**             | int / string | expense status (see [Value lists > Expense statuses](value-lists.md#expense-statuses)). When used as string, use pipe (<code>&#x7c;</code>) to add various statuses (e.g. <code>1&#x7c;2</code>) | |
| **type**               | string | expense type (see [Value lists > Expense types](value-lists.md#expense-types)) | |

### Response

```json
{
  "itemCount": 3,
  "items": [
    {
      "Client": [],
      "Document": [],
      "Expense": {
        "accounting_date": "2050-01-01 23:59:59",
        "amount": 12.14,
        "amount2": null,
        "amount3": null,
        "amount_country_home": "12.1400",
        "amount_home": "12.1400",
        "amount_paid": 0,
        "amount_paid_vat": 0,
        "client_data": null,
        "client_id": null,
        "comment": null,
        "constant": null,
        "country_exchange_rate": "1.00000000000000",
        "created": "2050-01-01",
        "currency": "EUR",
        "delivery": "2050-01-01",
        "demo": "0",
        "discount": "0",
        "discount_total": "0.0000",
        "document_number": null,
        "due": "2050-01-01",
        "exchange_rate": "1.00000000000000",
        "expense_category_id": null,
        "expense_no": "2",
        "flag": "issued",
        "home_currency": "EUR",
        "id": "2",
        "missing_bank_account": true,
        "modified": "2050-01-01 23:59:59",
        "my_data": "{\"id\":\"1\",\"user_id\":1,\"country_id\":\"191\",\"company_name\":\"SuperFaktura, s.r.o.\",\"name\":null,\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"business_register\":\"Obchodn\\u00fd register Okresn\\u00e9ho s\\u00fadu Bratislava I, oddiel: Sro, vlo\\u017eka \\u010d. 81403\\/B\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"tax_payer\":\"1\",\"vat_interval\":null,\"company_type\":\"ltd\"}",
        "name": "Foo bar",
        "number": "2020002",
        "paid": 0,
        "paid_vat": 0,
        "paydate": null,
        "qr": "",
        "qr_type": "",
        "qr_url": "",
        "qr_url_max": "",
        "rates": [],
        "recurring": null,
        "sequence_id": "9",
        "specific": null,
        "status": "1",
        "tags": null,
        "tax": null,
        "tax_code": null,
        "taxable_supply": null,
        "taxdate": "2050-01-01",
        "total": "12.1400",
        "total_country_home": "12.1400",
        "total_home": "12.1400",
        "type": "invoice",
        "user_id": "1",
        "user_profile_id": "1",
        "variable": null,
        "vat": 0,
        "vat2": null,
        "vat3": null,
        "version": "basic"
      },
      "ExpenseBasicRate": [
        {
          "amount": "12.1400",
          "id": "2",
          "tax": "0.00",
          "total": "12.1400"
        }
      ],
      "ExpenseExtra": [],
      "ExpenseItem": [
        {
          "description": null,
          "discount": "0.00000",
          "discount_description": null,
          "id": "2",
          "name": null,
          "ordernum": "0",
          "quantity": "1.00000",
          "stock_item_id": null,
          "tax": "0.00",
          "total": "12.1400",
          "type": "rate",
          "unit": null,
          "unit_price": "12.1400",
          "unit_total": "12.1400"
        }
      ],
      "ExpensePayment": [],
      "MyData": {
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
        "name": null,
        "tax_payer": "1",
        "user_id": 1,
        "vat_interval": null,
        "zip": "811 04"
      },
      "RelatedItem": [],
      "Tag": [],
      "VatSummary": [
        {
          "base": 12.14,
          "vat": 0
        }
      ],
      "attachments": []
    }
  ],
  "page": 2,
  "pageCount": 3,
  "perPage": 1
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Delete expense

Delete expense.

### Request

**URL**: `/expenses/delete/{ID}`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
    https://moja.superfaktura.sk/expenses/delete/1
```


### Attributes

#### Required
URL parameters:

| name   | type   | description | default value |
| ------ | ------ | ----------- | ------------- |
| **id** | int    | expense ID  |               |

### Response
#### Successful deletion
```json
{
  "message": "Expense deleted",
  "status": "success"
}
```

#### Non existent ID
```json
{
  "error": 1,
  "error_message": "Expense not found",
  "message": "Expense not found"
}
```

#### Insufficient privileges
```json
{
  "message": "Expense was not deleted",
  "status": "error"
}
```

#### Unsuccessful deletion
```json
{
    "error": 2,
    "error_message": "Error deleting expense."
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Add expense payment

Pays expense.

### Request

**URL**: `/expense_payments/add`  
**HTTP method**: POST  

```sh
data='{
  "ExpensePayment":{
    "expense_id":1,
    "currency":"EUR",
    "amount":12
  }
}';

curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/expense_payments/add
```


### Attributes
#### Required

| name           | type  | description                                | default value |
| -------------- | ----- | ------------------------------------------ | ------------- |
| **amount**     | float | amount of money                            |               |
| **expense_id** | int   | expense ID, to which payment will be added |               |

#### Optional

| name             | type   | description                                      | default value         |
| ---------------- | ------ | ------------------------------------------------ | --------------------- |
| **created**      | date   | date when payment was made  (`YYYY-MM-DD`)       | &lt;current date&gt;  |
| **currency**     | string | currency code (see [Value lists > Currencies](value-lists.md#currencies))   | &lt;home currency&gt; |
| **payment_type** | string | payment type (see [Value-lists > Payment types](value-lists.md#payment-types)) | transfer              |

### Response


#### Successfully added
```json
{
  "data": {
    "ExpensePayment": {
      "amount": 12,
      "currency": "EUR",
      "expense_id": 1,
      "id": "1"
    }
  },
  "error": 0,
  "expense": {
    "accounting_date": "2050-01-01",
    "amount": "12.1400",
    "amount2": null,
    "amount3": null,
    "amount_country_home": "12.1400",
    "amount_home": "12.1400",
    "amount_paid": 12,
    "amount_paid_vat": 12,
    "client_data": null,
    "client_id": null,
    "comment": null,
    "constant": null,
    "country_exchange_rate": "1.00000000000000",
    "created": "2050-01-01",
    "currency": "EUR",
    "delivery": "2050-01-01",
    "demo": "0",
    "discount": "0",
    "discount_total": "0.0000",
    "document_number": null,
    "due": "2050-01-01",
    "exchange_rate": "1.00000000000000",
    "expense_category_id": null,
    "expense_no": "1",
    "flag": "partially-paid",
    "home_currency": "EUR",
    "id": "1",
    "missing_bank_account": true,
    "modified": "2050-01-01 23:59:59",
    "my_data": "{\"id\":\"1\",\"user_id\":1,\"country_id\":\"191\",\"company_name\":\"SuperFaktura, s.r.o.\",\"name\":null,\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"business_register\":\"Obchodn\\u00fd register Okresn\\u00e9ho s\\u00fadu Bratislava I, oddiel: Sro, vlo\\u017eka \\u010d. 81403\\/B\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"tax_payer\":\"1\",\"vat_interval\":null,\"company_type\":\"ltd\"}",
    "name": "Foo bar",
    "number": "2020001",
    "paid": 12,
    "paid_vat": 12,
    "paydate": "2050-01-01",
    "qr": "",
    "qr_type": "",
    "qr_url": "",
    "qr_url_max": "",
    "rates": [],
    "recurring": null,
    "sequence_id": "9",
    "specific": null,
    "status": "2",
    "tags": null,
    "tax": null,
    "tax_code": null,
    "taxable_supply": null,
    "taxdate": "2050-01-01",
    "total": "12.1400",
    "total_country_home": "12.1400",
    "total_home": "12.1400",
    "type": "invoice",
    "user_id": "1",
    "user_profile_id": "1",
    "variable": null,
    "vat": "0.0000",
    "vat2": null,
    "vat3": null,
    "version": "basic"
  },
  "message": "Úhrada bola uložená"
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

#### Wrong expense
```json
{
  "error": 1,
  "message": "Expense not found"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Delete expense payment

Delete expense payment.

### Request

**URL**: `/expense_payments/delete/{PAYMENT_ID}`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/expense_payments/delete/1
```

### Attributes

#### Required

URL parameters:

| name           | type | description | default value |
| -------------- | ---- | ----------- | ------------- |
| **payment_id** | int  | payment ID  |               |

#### Optional
none  

### Response

#### Successful deletion
```json
{
  "error": 0,
  "message": "Úhrada nákladu bola zmazaná"
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
   "message": "Expense payment was not deleted"
}
```