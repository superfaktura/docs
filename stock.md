# Stock

- [Add stock item](#add-stock-item)
- [Edit stock item](#edit-stock-item)
- [View stock item details](#view-stock-item-details)
- [Get list of stock items](#get-list-of-stock-items)
- [Delete stock item](#delete-stock-item)
- [Add stock movement](#add-stock-movement)

## Add stock item

Adds item to stock

### Request

**URL**: `/stock_items/add`  
**HTTP method**: POST  

```sh
data='{
  "StockItem":{
    "description":"Public description of this item",
    "hide_in_autocomplete":1,
    "internal_comment":"Secret comment",
    "name":"Item B",
    "sku":"itemb1241",
    "unit":"m",
    "unit_price":19.95,
    "purchase_unit_price":10.99,
    "vat":20,
    "watch_stock":1,
    "stock":123
  }
}';

curl -X POST \
    -d "$data" \
    -H "Content-Type: application/json" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=123" \
    https://moja.superfaktura.sk/stock_items/add
```


### Attributes

#### Required
none

#### Optional

| name                      | type   | description                                                                  | default value |
| ------------------------- | ------ | ---------------------------------------------------------------------------- | ------------- |
| **description**           | string | item description                                                             | |
| **hide_in_autocomplete**  | int    | hide item in autocomplete (0=no, 1=yes)                                      | |
| **internal_comment**      | string | internal comment - will not be displayed on invoice                          | |
| **name**                  | string | item name                                                                    | |
| **sku**                   | string | unique identifier of stock item                                              | |
| **stock**                 | float  | number of units in stock. If is not set, stock movements will not be watched | |
| **unit**                  | string | unit, e.g.: pcs, mm, m2, ...                                                 | |
| **unit_price**            | float  | unit price                                                                   | |
| **purchase_unit_price**   | float  | purchase unit price                                                          | |
| **vat**                   | float  | VAT in percent                                                               | |
| **watch_stock**           | int    | track inventory level (0=no, 1=yes)                                          | |


### Response

#### Successful addition

```json
{
  "data": {
    "StockItem": {
      "description": "Public description of this item",
      "hide_in_autocomplete": 1,
      "id": "1",
      "internal_comment": "Secret comment",
      "name": "Item B",
      "sku": "itemb1241",
      "stock": 123,
      "unit": "m",
      "unit_price": 19.95,
      "purchase_unit_price":10.99,
      "vat": 20,
      "watch_stock": 1
    },
    "StockLog": [
      {
        "log_data": "{\"purchase_unit_price\":10.99,\"purchase_vat\":null,\"purchase_currency\":null,\"unit_price\":19.95,\"vat\":20,\"currency\":null}",
        "note": "Počiatočný stav skladu",
        "quantity": 123
      }
    ]
  },
  "error": 0,
  "error_message": ""
}
```

#### Missing data
Returns HTTP Status 400 (Bad request).

```sh
{
  "error": 1,
  "error_message": "Chýbajúce údaje",
  "message": "Chýbajúce údaje"
}
```

#### Insufficient privileges
Returns HTTP Status 403 (Forbidden).

```sh
{
  "error": 1,
  "error_message": "Ako používateľ typu Hosť nemáte oprávnenie na túto akciu.",
  "message": "Ako používateľ typu Hosť nemáte oprávnenie na túto akciu."
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Edit stock item

Updates stock item

### Request

**URL**: `/stock_items/edit/{ID}`  
**HTTP method**: PATCH  

```sh
data='{
  "StockItem":{
    "name":"Item B",
    "unit":"kg"
  }
}';

curl -X PATCH \
    -d "$data" \
    -H "Content-Type: application/json" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=123" \
    https://moja.superfaktura.sk/stock_items/edit/1
```

### Attributes

#### Required

| name   | type | description   | default value |
| ------ | ---- | ------------- | ------------- |
| **id** | int  | stock item id |               |

#### Optional

| name                      | type   | description | default value |
| ------------------------- | ------ | ----------- | ------------- |
| **description**           | string | item description | |
| **hide_in_autocomplete**  | int    | hide item in autocomplete (0=no, 1=yes) | |
| **internal_comment**      | string | internal comment - will not be displayed on invoice | |
| **name**                  | string | item name | |
| **sku**                   | string | unique identifier of stock item | |
| **stock**                 | float  | number of units in stock. If is not set, stock movements will not be watched | |
| **unit**                  | string | unit, e.g.: pcs, mm, m2, ... | |
| **unit_price**            | float  | unit price | |
| **vat**                   | float  | VAT in percent | |
| **watch_stock**           | int    | track inventory level (0=no, 1=yes) | |


### Response

#### Successful update
```json
{
  "data": {
    "StockItem": {
      "created": "2050-01-01 23:59:59",
      "description": "Public description of this item",
      "hide_in_autocomplete": true,
      "id": 1,
      "import_id": null,
      "import_type": null,
      "internal_comment": "Secret comment",
      "modified": "2050-01-01 23:59:59",
      "name": "Item B",
      "purchase_currency": null,
      "purchase_unit_price": null,
      "purchase_vat": null,
      "sku": "itemb1241",
      "stock": 123,
      "stock_previous": 123,
      "unit": "kg",
      "unit_price": 19.95,
      "user_id": "1",
      "user_profile_id": "1",
      "vat": 20,
      "watch_stock": true
    },
    "StockLog": [
      {
        "log_data": "{\"purchase_unit_price\":\"\",\"purchase_tax\":null,\"purchase_exchange_rate\":1,\"purchase_country_exchange_rate\":1,\"purchase_currency\":null,\"unit_price\":\"19.95\",\"tax\":20,\"exchange_rate\":1,\"country_exchange_rate\":1,\"currency\":\"EUR\",\"home_currency\":\"EUR\"}",
        "note": "Ručná úprava stavu na sklade",
        "quantity": 0
      }
    ]
  },
  "error": 0,
  "error_message": ""
}
```

#### Insufficient privileges
Returns HTTP status 403 (Forbidden).

```json
{
  "error": 1,
  "error_message": "Ako používateľ typu Hosť nemáte oprávnenie na túto akciu.",
  "message": "Ako používateľ typu Hosť nemáte oprávnenie na túto akciu."
}
```

#### Wrong item ID
Returns HTTP status 400 (Bad request).
```json
{
  "error": 2,
  "error_message": "StockItem id not found.",
  "message": "StockItem id not found."
}
```

#### Item not found
Returns HTTP status 404 (Not found).
```json
{
  "error": 2,
  "error_message": "StockItem not found.",
  "message": "StockItem not found."
}
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## View stock item details

Get details about stock item.

### Request

**URL**: `/stock_items/view/{ID}`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=123" \
    https://moja.superfaktura.sk/stock_items/view/1
```

### Attributes
#### Required

URL parameters:

| name   | type   | description | default value |
| ------ | ------ | ----------- | ------------- |
| **id** | int    | stock item ID |             |


#### Optional
none

### Response

#### Successfully showing details

```json
{
  "StockItem": {
    "created": "2050-01-01 23:59:59",
    "description": "Public description of this item",
    "hide_in_autocomplete": true,
    "id": "1",
    "import_id": null,
    "import_type": null,
    "internal_comment": "Secret comment",
    "modified": "2050-01-01 23:59:59",
    "name": "Item B",
    "purchase_currency": null,
    "purchase_unit_price": null,
    "purchase_vat": null,
    "sku": "itemb1241",
    "stock": 123,
    "unit": "m",
    "unit_price": 19.95,
    "user_id": "1",
    "user_profile_id": "1",
    "vat": 20,
    "watch_stock": true
  }
}
```

#### Wrong stock item
Returns HTTP status 404 (Not found).
```json
{
  "error": 1,
  "error_message": "StockItem not found",
  "message": "StockItem not found"
}
```
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Get list of stock items

Return list of stock items.

### Request

**URL**: `/stock_items/index.json[/{ATTRIBUTE}:{VALUE}]*`  
**HTTP method**: GET  

````sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=123" \
    https://moja.superfaktura.sk/stock_items/index.json
````

### Attributes

#### Required
none

#### Optional

URL parameters:

| name              | type   | description | default value |
| ----------------- | ------ | ----------- | ------------- |
| **direction**     | string | sorting type, ASC or DESC | DESC |
| **listinfo**      | int    | show meta information for results (0=no, 1=yes)| 0 |
| **page**          | int    | page number | 1 |
| **per_page**      | int    | number of results per page | |
| **price_from**    | float  | price from | |
| **price_to**      | float  | price to | |
| **search**        | string | searches substring in the following fields: <ul><li>name</li>base64 encoded string (e.g. Maslo = "TWFzbG8=")<li>sku</li><li>description</li></ul> | |
| **sku**           | string | search by sku (base64 encoded string: "itemb1241" = "aXRlbWIxMjQx") | |
| **sort**          | string | sorting attribute | 'regular_count' |
| **status**        | int    | if 1 - shows only items that are in stock | |


### Response
JSON array of objects

Fields:

| name                      | type     | description                                   | default value |
| ------------------------- | -------- | --------------------------------------------- | ------------- |
| **created**               | datetime | date and time of creation                     |               |
| **description**           | string   | item description (is displayed on invoice)    |               |
| **hide_in_autocomplete**  | bool     | hide in autocomplete (null = no)              |               |
| **id**                    | int      | item ID                                       |               |
| **import_id**             | int      | import ID (if is not from import = null)      |               |
| **import_type**           | string   | import type ('efaktury' or `null`)            |               |
| **internal_comment**      | string   | internal comment (isn't displayed on invoice) |               | 
| **modified**              | datetime | date and time of modification                 |               |
| **name**                  | string   | item name                                     |               |
| **sku**                   | int      | stock item identifier (e.g. ABC123)           |               |
| **stock**                 | float    | number of items in stock                      |               |
| **unit**                  | string   | unit (e.g. ks, kg)                            |               |
| **unit_price**            | float    | unit price                                    |               |
| **user_id**               | int      | user ID                                       |               |
| **user_profile_id**       | int      | user profile ID                               |               |
| **vat**                   | float    | VAT in percent (e.g. 20)                      |               |
| **watch_stock**           | bool     | track inventory level                         |               |

### Success
```json
[
  {
    "StockItem": {
      "created": "2050-01-01 23:59:59",
      "description": "Public description of this item",
      "hide_in_autocomplete": true,
      "id": "1",
      "import_id": null,
      "import_type": null,
      "internal_comment": "Secret comment",
      "modified": "2050-01-01 23:59:59",
      "name": "Item B",
      "purchase_currency": null,
      "purchase_unit_price": null,
      "purchase_vat": null,
      "sku": "itemb1241",
      "stock": 123,
      "unit": "m",
      "unit_price": 19.95,
      "user_id": "1",
      "user_profile_id": "1",
      "vat": 20,
      "watch_stock": true
    }
  }
]
```

### Success with listing information

```json
{
  "itemCount": 1,
  "items": [
    {
      "StockItem": {
        "created": "2050-01-01 23:59:59",
        "description": "Public description of this item",
        "hide_in_autocomplete": true,
        "id": "1",
        "import_id": null,
        "import_type": null,
        "internal_comment": "Secret comment",
        "modified": "2050-01-01 23:59:59",
        "name": "Item B",
        "purchase_currency": null,
        "purchase_unit_price": null,
        "purchase_vat": null,
        "sku": "itemb1241",
        "stock": 123,
        "unit": "m",
        "unit_price": 19.95,
        "user_id": "1",
        "user_profile_id": "1",
        "vat": 20,
        "watch_stock": true
      }
    }
  ],
  "page": 1,
  "pageCount": 1,
  "perPage": 50
}
```

- - - - - - - - - - - - - - - - - - - - - 


## Delete stock item

Delete stock item


### Request
**URL**: `/stock_items/delete/{ID}`  
**HTTP method**: DELETE  


```sh
curl -X DELETE \
     -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=123" \
     https://moja.superfaktura.sk/stock_items/delete/1
```

### Attributes
#### Required

URL parameters:

| name    | type   | description | default value |
| ------- | ------ | ----------- | ------------- |
| **id**  | int    | stock item ID |             |


#### Optional
none

### Response

#### Successful deletion
```json
{
  "data": {
    "StockItem": {
      "created": "2050-01-01 23:59:59",
      "description": "Public description of this item",
      "hide_in_autocomplete": true,
      "id": "1",
      "import_id": null,
      "import_type": null,
      "internal_comment": "Secret comment",
      "modified": "2050-01-01 23:59:59",
      "name": "Item B",
      "purchase_currency": null,
      "purchase_unit_price": null,
      "purchase_vat": null,
      "sku": "itemb1241",
      "stock": 123,
      "unit": "m",
      "unit_price": 19.95,
      "user_id": "1",
      "user_profile_id": "1",
      "vat": 20,
      "watch_stock": true
    }
  },
  "error": 0,
  "error_message": ""
}
```

#### Invalid item ID
Returns HTTP status 400 (Bad request).
```json
{
  "error": 1,
  "error_message": "Invalid stock item id",
  "message": "Invalid stock item id"
}
```

#### Item not found
Returns HTTP status 404 (Not found).
```json
{
  "error": 1,
  "error_message": "StockItem not found",
  "message": "StockItem not found"
}
```
#### Unsuccessful deletion
Returns HTTP status 500 (Internal server error)
```json
{
    "error": 2,
    "error_message": "Error deleting stock item."
}
```

#### Insufficient privileges

Returns HTTP status 403 (Forbidden).

```json
{
  "error": 1,
  "error_message": "Ako používateľ typu Hosť nemáte oprávnenie na túto akciu.",
  "message": "Ako používateľ typu Hosť nemáte oprávnenie na túto akciu."
}
```




- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Add stock movement

### Request

**URL**: `/stock_items/addStockMovement`  
**HTTP method**: POST  

```sh
data='{
    "StockLog":[
        {
          "currency":"EUR",
          "purchase_currency":"SEK",
          "purchase_unit_price":0.97,
          "purchase_tax":22,
          "quantity":5,
          "sku":"itemb1241",
          "unit_price":1.23,
          "tax":25
        }
    ]
}';

curl -X POST \
    -d "$data" \
    -H "Content-Type: application/json" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=123" \
    https://moja.superfaktura.sk/stock_items/addStockMovement
```  

### Attributes
#### Required
none

Either `sku` or `stock_item_id` is required.

#### Optional

| name                    | type   | description                                      | default value   |
|-------------------------|--------|--------------------------------------------------|-----------------|
| **created**             | date   | date of movement in `YYYY-MM-DD`                 | &lt;current&gt; |
| **note**                | string | description of movement                          |                 |
| **purchase_currency**   | string |                                                  |                 |
| **purchase_unit_price** | float  |                                                  |                 |
| **purchase_tax**        | float  | VAT                                              |                 |
| **quantity**            | float  | negative number = outgo, positive = income       | 1               |
| **sku**                 | string | unique stock item identifier                     |                 |
| **stock_item_id**       | int    | stock item ID to which movement will be assigned |                 |
| **unit_price**          | float  | stock item ID to which movement will be assigned |                 |
| **tax**                 | float  | VAT                                              |                 |

### Response

#### Successfully added

```json
{
  "data": {
    "StockLog": [
      {
        "currency": "EUR",
        "id": 0,
        "log_data": "{\"purchase_unit_price\":0.97,\"purchase_tax\":22,\"purchase_currency\":\"SEK\",\"unit_price\":1.23,\"tax\":25,\"currency\":\"EUR\"}",
        "purchase_currency": "SEK",
        "purchase_tax": 22,
        "purchase_unit_price": 0.97,
        "quantity": 5,
        "sku": "itemb1241",
        "stock_item_id": "1",
        "tax": 25,
        "unit_price": 1.23
      }
    ]
  },
  "error": 0,
  "error_message": ""
}
```

#### Invalid data
```json
{
  "error": 3,
  "error_message": "StockItem empty data."
}
```




- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Get stock logs of item
### Request

**URL**: `/stock_items/movements/{ID}`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=123" \
    https://moja.superfaktura.sk/stock_items/movements/1
```  

### Attributes
#### Required
URL parameters:

| name    | type   | description   | default value |
| ------- | ------ |---------------|---------------|
| **id**  | int    | stock item ID |               |

#### Optional
URL parameters:

| name              | type   | description                | default value |
| ----------------- | ------ |----------------------------|---------------|
| **direction**     | string | sorting type, ASC or DESC  | ASC           |
| **page**          | int    | page number                | 1             |
| **per_page**      | int    | number of results per page |               |
| **sort**          | string | sorting attribute          |               |

### Response

#### Successfully showing logs

```json
{
  "itemCount": 9,
  "pageCount": 5,
  "perPage": 2,
  "page": 2,
  "items": [
    {
      "StockLog": {
        "id": "1",
        "stock_item_id": "9",
        "user_id": "22",
        "user_profile_id": "12",
        "invoice_id": null,
        "expense_id": null,
        "document_item_id": null,
        "quantity": 0,
        "note": "Ručná úprava stavu na sklade",
        "document": null,
        "document_subtype": null,
        "log_data": "{\"purchase_unit_price\":\"0.1200\",\"purchase_tax\":null,\"purchase_exchange_rate\":1,\"purchase_country_exchange_rate\":1,\"purchase_currency\":null,\"unit_price\":\"0.1\",\"tax\":20,\"exchange_rate\":1,\"country_exchange_rate\":1,\"currency\":\"EUR\",\"home_currency\":\"EUR\"}",
        "created": "2050-10-10 09:27:17",
        "modified": "2050-10-10 09:27:17"
      }
    },
    {
      "StockLog": {
        "id": "2",
        "stock_item_id": "9",
        "user_id": "22",
        "user_profile_id": "12",
        "invoice_id": null,
        "expense_id": null,
        "document_item_id": null,
        "quantity": 2,
        "note": "Test",
        "document": null,
        "document_subtype": null,
        "log_data": "{\"purchase_unit_price\":\"0.1200\",\"purchase_tax\":null,\"purchase_exchange_rate\":1,\"purchase_country_exchange_rate\":1,\"purchase_currency\":null,\"unit_price\":\"0.1\",\"tax\":20,\"exchange_rate\":1,\"country_exchange_rate\":1,\"currency\":\"EUR\",\"home_currency\":\"EUR\"}",
        "created": "2050-10-10 09:27:25",
        "modified": "2050-10-10 09:27:25"
      }
    }
  ]
}
```

#### Wrong stock item
Returns HTTP status 404 (Not found).
```json
{
  "error": 1,
  "error_message": "StockItem not found",
  "message": "StockItem not found"
}
```
