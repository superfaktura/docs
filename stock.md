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
    "vat":20,
    "watch_stock":1,
    "stock":123
  }
}';

curl -X POST \
    -d "data=$data" \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
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
      "vat": 20,
      "watch_stock": 1
    },
    "StockLog": [
      {
        "log_data": "{\"purchase_unit_price\":null,\"purchase_vat\":null,\"purchase_currency\":null,\"unit_price\":19.95,\"vat\":20,\"currency\":null}",
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
Status 400.

```sh
{
  "error": 1,
  "error_message": "Chýbajúce údaje",
  "message": "Chýbajúce údaje"
}
```

#### Insufficient privileges
Status 403.

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

**URL**: `/stock_items/edit`  
**HTTP method**: POST  

```sh
data='{
  "StockItem":{
    "name":"Item B",
    "unit":"kg",
    "id":1
  }
}';

curl -X POST \
    -d "data=$data" \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
    https://moja.superfaktura.sk/stock_items/edit
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
    }
  },
  "error": 0,
  "error_message": ""
}
```

#### Insufficient privileges
HTTP status 403

```json
{
  "error": 1,
  "error_message": "Vaša <a href=\"https://pomoc.superfaktura.sk/mozu-moj-ucet-pouzivat-aj-moji-spolupracovnici/\">používateľská rola</a> nemôže vykonať túto akciu.",
  "message": "Vaša <a href=\"https://pomoc.superfaktura.sk/mozu-moj-ucet-pouzivat-aj-moji-spolupracovnici/\">používateľská rola</a> nemôže vykonať túto akciu."
}
```

#### Wrong item ID
```json
{
  "error": 2,
  "error_message": "StockItem id not found."
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
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
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

```json
{
  "error": 1,
  "error_message": "Skladová položka nenájdená",
  "message": "Skladová položka nenájdená"
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
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
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

| name                      | type   | description                                   | default value |
| ------------------------- | ------ | --------------------------------------------- | ------------- |
| **created**               | int    | constant specifying time filtering (see [Value lists > Time filter constants](value-lists.md#time-filter-constants)) |               |
| **created_since**         | date   | creation date since  (requires `created:3`)   |               |
| **created_to**            | date   | creation date to  (requires `created:3`)      |               |
| **description**           | string | item description (is displayed on invoice)    |               |
| **hide_in_autocomplete**  | bool   | hide in autocomplete (null = no)              |               |
| **id**                    | int    | item ID                                       |               |
| **import_id**             | int    | import ID (if is not from import = null)      |               |
| **import_type**           | string | import type ('efaktury' or `null`)            |               |
| **internal_comment**      | string | internal comment (isn't displayed on invoice) |               | 
| **modified**              | int    | constant specifying time filtering (see [Value lists > Time filter constants](value-lists.md#time-filter-constants)) |               |
| **modified_since**        | date   | last modification date from (requires `modified:3`) |               |
| **modified_to**           | date   | last modification date to (requires `modified:3`) |               |
| **name**                  | string | item name                                     |               |
| **sku**                   | int    | stock item identifier (e.g. ABC123)           |               |
| **stock**                 | float  | number of items in stock                      |               |
| **unit**                  | string | unit (e.g. ks, kg)                            |               |
| **unit_price**            | float  | unit price                                    |               |
| **user_id**               | int    | user ID                                       |               |
| **user_profile_id**       | int    | user profile ID                               |               |
| **vat**                   | float  | VAT in percent (e.g. 20)                      |               |
| **watch_stock**           | bool   | track inventory level                         |               |

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
**HTTP method**: GET  


```sh
curl -X GET \
     -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
     https://moja.superfaktura.sk/stock_items/delete/1
```

```sh
data='{"ids":"1,2"}';

curl -X POST \
     -d "data=$data" \
     -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
     https://moja.superfaktura.sk/stock_items/delete
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
```json
{
  "error": 1,
  "error_message": "Invalid stock item id."
}
```

#### Unsuccessful deletion
```json
{
    "error": 2,
    "error_message": "Error deleting stock item."
}
```

#### Insufficient privileges

Returns HTTP status 403.

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
            "quantity":5,
            "sku":"itemb1241"
        }
    ]
}';

curl -X POST \
    -d "data=$data" \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
    https://moja.superfaktura.sk/stock_items/addStockMovement
```  

### Attributes
### Required
none

Either `sku` or `stock_item_id` is required.

### Optional

| name              | type   | description | default value |
| ----------------- | ------ | ----------- | ------------- |
| **created**       | date   | date of movement in `YYYY-MM-DD` | &lt;current&gt; |
| **note**          | string | description of movement |   |
| **quantity**      | float  | negative number = outgo, positive = income | 1 |
| **sku**           | string | unique stock item identifier | |
| **stock_item_id** | int    | stock item ID to which movement will be assigned | |

### Response

#### Successfully added

```json
{
  "data": {
    "StockLog": [
      {
        "id": 0,
        "quantity": 5,
        "sku": "itemb1241",
        "stock_item_id": "1"
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