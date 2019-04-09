# Expenses

- [Add expense](#add-expense)
- [Edit expense](#edit-expense)
- [Delete expense](#delete-expense)
- [Delete expense payment](#delete-expense-payment)
- [Get list of expenses](#get-list-of-expenses)
- [Add expense payment](#add-expense-payment)
- [Expense detail](#expense-detail)

## Add expense

Add new expense.
If you want to add tags to expense, refer to [FAQ > How do I add tags to an entity?](faq.md#how-do-i-add-tags-to-an-entity).

### Request

**URL**: `/expenses/add`  
**HTTP method**: POST  

```sh
data='{"Expense":{"name":"Foo bar","currency":"NOK","amount":12.14}}';

curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/expenses/add
```  

### Attributes

#### Required

| name     | type   | description  | default value |
| -------- | ------ | ------------ | ------------- |
| **name** | string | expense name |               |

#### Optional

| name                    | type   | description                                                  | default value |
| ----------------------- | ------ | ------------------------------------------------------------ | ------------- |
| **already_paid**        | int    | is invoice already paid? (0=no, 1=yes)                       | 0 |
| **amount**              | float  | amount of money without VAT                                  | 0 |
| **client_id**           | int    | client ID                                                    | |
| **comment**             | string | comment                                                      | |
| **constant**            | string | constant symbol                                              | |
| **created**             | date   | issue date                                                   | &lt;current date&gt; |
| **currency**            | string | currency (see [Value lists > Currencies](value-lists.md#currencies))                    | &lt;home currency&gt; |
| **delivery**            | date   | delivery date                                                | &lt;current date&gt; |
| **document_number**     | string | document number, (e.g. invoice number, bill number, ...)     | |
| **due**                 | date   | due date                                                     | &lt;current date&gt; |
| **expense_category_id** | int    | expense category ID (see [Value lists > Expense categories](value-lists.md#expense-categories)) | |
| **payment_type**        | string | payment type (see [Value lists > Payment types](value-lists.md#payment-types))             | |
| **specific**            | string | specific symbol                                              | |
| **taxable_supply**      | date   | date of taxable transaction                                  | null |
| **type**                | string | expense typ (see [Value lists > Invoice types](value-lists.md#invoice-types))              | 'invoice' |
| **variable**            | string | variable symbol                                              | |
| **vat**                 | string | VAT in percent                                               | 0 |


### Response

#### Successful creation
```json
{
   "data" : {
      "Expense" : {
         "amount" : 12.14,
         "created" : "2019-02-11 00:00:00",
         "currency" : "NOK",
         "delivery" : "2019-02-11 00:00:00",
         "due" : "2019-02-11 00:00:00",
         "exchange_rate" : 9.7693,
         "id" : "75",
         "name" : "Foo bar",
         "taxable_supply" : null,
         "type" : "invoice",
         "variable" : "",
         "vat" : 0
      }
   },
   "error" : 0,
   "error_message" : "",
   "status" : 1
}
```

#### Insufficient privileges
HTTP status 403.

```json
{
   "error_message" : "Nemáte právo vytvárať náklady",
   "message" : "Nemáte právo vytvárať náklady",
   "error" : 1
}
```

#### Not enough data
```json
{
   "error_message" : {
      "name" : "Táto položka nemôže ostať nevyplnená"
   },
   "error" : 1
}
```

#### Missing data
HTTP status 400.

```json
{
   "error" : 1,
   "message" : "Chýbajúce údaje",
   "error_message" : "Chýbajúce údaje"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Edit expense

Edit expense.

It's strongly recommended to fetch data for expense, change required values, and then request edit.
If you want to add tags to expense, refer to [FAQ > How do I add tags to an entity?](faq.md#how-do-i-add-tags-to-an-entity).

### Request

**URL**: `/expenses/edit`  
**HTTP method**: POST  

```sh
data='{
    "Expense":{
        "id":"77",
        "name":"Foo bar",
        "currency":"NOK",
        "amount":19.95,
        "due":"2014-01-01"
    }
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

Same as for **Add expense**. With the exception of *name* is optional.

### Response

#### Successfully edited
```json
{
   "data" : {
      "Expense" : {
         "amount" : 19.95,
         "created" : "2019-02-11 00:00:00",
         "currency" : "NOK",
         "delivery" : "2019-02-11 00:00:00",
         "due" : "2014-01-01 00:00:00",
         "expense_category_id" : null,
         "id" : "77",
         "name" : "Foo bar",
         "taxable_supply" : null,
         "vat" : 0
      },
      "Document" : null
   },
   "error_message" : "",
   "error" : 0
}
```

#### Bad data format / missing expense ID
```json
{
   "error" : "3",
   "message" : "Bad data format."
}
```

#### Wrong expense
```json
{
   "error" : "2",
   "message" : "Expense id no found."
}
```

#### Insufficient privileges

HTTP status 403.

```json
{
   "error" : 1,
   "error_message" : "Nemáte právo editovať tento náklad",
   "message" : "Nemáte právo editovať tento náklad"
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

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Delete expense

Delete expense.

### Request

**URL**: `/expenses/delete/{ID}`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
    https://moja.superfaktura.sk/expenses/delete/63
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
   "data" : {
      "Expense" : {
         "amount" : "122.0000",
         "amount2" : "0.0000",
         "amount3" : "0.0000",
         "amount_paid" : "0.00",
         "client_id" : null,
         "comment" : "",
         "constant" : "",
         "country_exchange_rate" : "1.00000000000000",
         "created" : "2019-01-31 00:00:00",
         "currency" : "EUR",
         "delivery" : "2019-01-31 00:00:00",
         "demo" : "0",
         "document_number" : "",
         "due" : "2019-01-31 00:00:00",
         "exchange_rate" : "1.00000000000000",
         "expense_category_id" : null,
         "id" : "63",
         "modified" : "2019-01-31 10:14:37",
         "name" : "test",
         "paid" : "0.00",
         "paydate" : null,
         "recurring" : null,
         "specific" : "",
         "status" : "1",
         "tags" : "",
         "taxable_supply" : null,
         "taxdate" : "2019-01-31",
         "type" : "invoice",
         "user_id" : "384",
         "user_profile_id" : "393",
         "variable" : "",
         "vat" : "20",
         "vat2" : "0",
         "vat3" : "10"
      }
   },
   "error_message" : "",
   "error" : 0
}
```

#### Non existent ID
```json
{
   "error": 1,
   "error_message": "Expense id not found."
}
```

#### Unsuccessful deletion  
```json
{
    "error": 2,
    "error_message": "Error deleting expense."
}
```

#### Insufficient privileges
```json
{
   "error" : 1,
   "message" : "Nemôžete zmazať túto položku",
   "error_message" : "Nemôžete zmazať túto položku"
}
```



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


## Delete expense payment

Delete expense payment.

### Request

**URL**: `/expense_payments/delete/{PAYMENT_ID}`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/expense_payments/delete/133
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
   "message": "Úhrada nákladu bola zmazaná",
   "error": 0
}
```

#### Payment not found
```json
{
   "message": "Payment not found",
   "error": 1
}
```

#### Unsuccessful deletion
```json
{
   "error": 1,
   "message": "Expense payment was not deleted"
}
```


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
| **created_since**      | date   | created date since | |
| **created_to**         | date   | created date until | |
| **delivery**           | int    | constant specifying time filtering (see [Value lists > Time filter constants](value-lists.md#time-filter-constants)) | |
| **delivery_since**     | date   | delivery date since | |
| **delivery_to**        | date   | delivery date until | |
| **direction**          | string | sorting direction (ASC or DESC) | DESC |
| **due**                | date   | due date | |
| **list_info**          | int    | show meta data about result? (0=no, 1=yes) | 0 |
| **page**               | int    | page number | 1 |
| **payment_type**       | string | payment type (see [Value lists > Payment types](value-lists.md#payment-types)) | |
| **per_page**           | int    | number of items per page (max 100) | &gt;as set in profile&lt; |
| **search**             | string | base64 encoded string (e.g. `test` = `dGVzdA,,` | |
| **sort**               | string | attribute to sort by, default regular_count | ASC |
| **status**             | int / string | expense status (see [Value lists > Expense statuses](value-lists.md#expense-statuses)). When used as string, use pipe (<code>&#x7c;</code>) to add various statuses (e.g. <code>1&#x7c;2</code>) | |
| **type**               | string | expense type (see [Value lists > Expense types](value-lists.md#expense-types) | |

### Response

```json
{
   "items" : [
      {
         "0" : {
            "paid" : "0.0000",
            "paid_date" : null,
            "to_pay" : "12.000000",
            "total" : "12.00"
         },
         "Expense" : {
            "amount" : "10.0000",
            "amount2" : "0.0000",
            "amount3" : "0.0000",
            "amount_paid" : "0.00",
            "client_id" : null,
            "comment" : "",
            "constant" : "",
            "country_exchange_rate" : "1.00000000000000",
            "created" : "2019-02-01 00:00:00",
            "currency" : "EUR",
            "delivery" : "2019-02-01 00:00:00",
            "demo" : "0",
            "document_number" : "",
            "due" : "2019-02-01 00:00:00",
            "exchange_rate" : "1.00000000000000",
            "expense_category_id" : null,
            "flag" : "issued",
            "id" : "65",
            "modified" : "2019-02-01 10:05:47",
            "name" : "naklad 1",
            "paid" : "0.00",
            "paydate" : null,
            "recurring" : null,
            "specific" : "",
            "status" : "1",
            "tags" : "",
            "taxable_supply" : null,
            "taxdate" : "2019-02-01",
            "type" : "bill",
            "user_id" : "384",
            "user_profile_id" : "393",
            "variable" : "",
            "vat" : "20",
            "vat2" : "0",
            "vat3" : "10"
         },
         "Client" : {
            "address" : null,
            "bank_account" : null,
            "bank_account_id" : null,
            "bank_account_prefix" : null,
            "bank_code" : null,
            "city" : null,
            "comment" : null,
            "country" : null,
            "country_id" : null,
            "created" : null,
            "currency" : null,
            "default_variable" : null,
            "delivery_address" : null,
            "delivery_city" : null,
            "delivery_country" : null,
            "delivery_country_id" : null,
            "delivery_name" : null,
            "delivery_phone" : null,
            "delivery_state" : null,
            "delivery_zip" : null,
            "dic" : null,
            "discount" : null,
            "distance" : null,
            "dont_travel" : null,
            "due_date" : null,
            "email" : null,
            "fax" : null,
            "iban" : null,
            "ic_dph" : null,
            "ico" : null,
            "id" : null,
            "modified" : null,
            "name" : null,
            "notices" : null,
            "phone" : null,
            "state" : null,
            "swift" : null,
            "tags" : null,
            "update" : null,
            "user_id" : null,
            "user_profile_id" : null,
            "uuid" : null,
            "zip" : null
         },
         "Document" : {
            "alternative" : null,
            "basename" : null,
            "checksum" : null,
            "created" : null,
            "default" : null,
            "dirname" : null,
            "foreign_key" : null,
            "group" : null,
            "id" : null,
            "model" : null,
            "modified" : null
         },
         "ExpenseCategory" : {
            "id" : null,
            "name" : null
         }
      }
   ],
   "filtered" : false,
   "page" : 2,
   "perPage" : 1,
   "pageCount" : 5,
   "itemCount" : 5
}
```



## Add expense payment

Pays expense.

### Request

**URL**: `/expense_payments/add`  
**HTTP method**: POST  

```sh
data='{
    "ExpensePayment":{
        "expense_id":64
    }
}';

# another data example
data='{
    "ExpensePayment":{
        "expense_id":64,
        "currency":"NOK",
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
   "error_message" : "Úhrada bola uložená",
   "error" : 0,
   "data" : {
      "ExpensePayment" : {
         "amount" : 11,
         "created" : "2019-01-31",
         "currency" : "AUD",
         "exchange_rate" : 1,
         "expense_id" : 64,
         "id" : "139"
      },
      "Expense" : {
         "amount" : "100.0000",
         "amount2" : "0.0000",
         "amount3" : "0.0000",
         "amount_paid" : "37.92",
         "client_id" : null,
         "comment" : "",
         "constant" : "",
         "country_exchange_rate" : "1.00000000000000",
         "created" : "2019-01-31 00:00:00",
         "currency" : "EUR",
         "delivery" : "2019-01-31 00:00:00",
         "demo" : "0",
         "document_number" : "",
         "due" : "2019-01-31 00:00:00",
         "exchange_rate" : "1.00000000000000",
         "expense_category_id" : null,
         "id" : "64",
         "modified" : "2019-01-31 12:40:16",
         "name" : "Nakladka",
         "paid" : "37.92",
         "paydate" : "2019-01-31 00:00:00",
         "recurring" : null,
         "specific" : "",
         "status" : "2",
         "tags" : "",
         "taxable_supply" : null,
         "taxdate" : "2019-01-31",
         "type" : "invoice",
         "user_id" : "384",
         "user_profile_id" : "393",
         "variable" : "",
         "vat" : "20",
         "vat2" : "0",
         "vat3" : "10"
      }
   }
}
```

#### Missing data
```json
{
   "error_message" : "Chýbajúce údaje",
   "message" : "Chýbajúce údaje",
   "error" : 1
}
```

#### Wrong expense
```json
{
   "error" : 1,
   "error_message" : "Expense not found."
}
```


## Expense detail

### Request

**URL**: `/expense/edit/{ID}.json`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/expenses/edit/64.json
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
   "Tag" : [],
   "ExpensePayment" : [
      {
         "amount" : "0.0000",
         "created" : "31.01.2019",
         "currency" : "EUR",
         "document_no" : "",
         "exchange_rate" : 1,
         "expense_id" : "64",
         "force_paid" : "0",
         "id" : "134",
         "payment_type" : "transfer",
         "user_id" : "384",
         "user_profile_id" : "393",
         "vat" : "20.0000"
      },
      {
         "amount" : "0.0000",
         "created" : "31.01.2019",
         "currency" : "EUR",
         "document_no" : "",
         "exchange_rate" : 1,
         "expense_id" : "64",
         "force_paid" : "0",
         "id" : "137",
         "payment_type" : "",
         "user_id" : "384",
         "user_profile_id" : "393",
         "vat" : "0.0000"
      },
      {
         "amount" : "11.0000",
         "created" : "31.01.2019",
         "currency" : "EUR",
         "document_no" : "",
         "exchange_rate" : 1,
         "expense_id" : "64",
         "force_paid" : "0",
         "id" : "138",
         "payment_type" : "",
         "user_id" : "384",
         "user_profile_id" : "393",
         "vat" : "0.0000"
      },
      {
         "amount" : "11.0000",
         "created" : "31.01.2019",
         "currency" : "AUD",
         "document_no" : "",
         "exchange_rate" : 1,
         "expense_id" : "64",
         "force_paid" : "0",
         "id" : "139",
         "payment_type" : "",
         "user_id" : "384",
         "user_profile_id" : "393",
         "vat" : "0.0000"
      }
   ],
   "Client" : null,
   "Expense" : {
      "amount" : 100,
      "amount2" : 0,
      "amount3" : 0,
      "amount_paid" : "37.92",
      "client_id" : null,
      "comment" : "",
      "constant" : "",
      "country_exchange_rate" : "1.00000000000000",
      "created" : "2019-01-31 00:00:00",
      "currency" : "EUR",
      "delivery" : "2019-01-31 00:00:00",
      "demo" : "0",
      "document_number" : "",
      "due" : "2019-01-31 00:00:00",
      "exchange_rate" : "1.00000000000000",
      "expense_category_id" : null,
      "id" : "64",
      "modified" : "2019-01-31 12:40:16",
      "name" : "Nakladka",
      "paid" : "37.92",
      "paydate" : "2019-01-31 00:00:00",
      "recurring" : null,
      "specific" : "",
      "status" : "2",
      "tags" : "",
      "taxable_supply" : null,
      "taxdate" : "2019-01-31",
      "type" : "invoice",
      "user_id" : "384",
      "user_profile_id" : "393",
      "variable" : "",
      "vat" : "20",
      "vat2" : "0",
      "vat3" : "10"
   }
}
```

#### Insufficient privileges
```json
{
   "error_message" : "K tejto stránke nemáte prístup!",
   "error" : 1,
   "message" : "K tejto stránke nemáte prístup!"
}
```

#### Wrong expense
```json
{
   "error_message" : "K tejto stránke nemáte prístup!",
   "error" : 1,
   "message" : "K tejto stránke nemáte prístup!"
}
```