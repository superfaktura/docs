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
   "error" : 0,
   "error_message" : "",
   "data" : {
      "StockItem" : {
         "description" : "Public description of this item",
         "hide_in_autocomplete" : 1,
         "id" : "19",
         "internal_comment" : "Secret comment",
         "sku" : "itemb1241",
         "stock" : 123,
         "unit" : "m",
         "unit_price" : 19.95,
         "vat" : 20,
         "watch_stock" : 1
      },
      "StockLog" : [
         {
            "quantity" : 123,
            "note" : "Počiatočný stav skladu"
         }
      ]
   }
}
```

#### Missing data
Status 400.

```sh
{
   "error" : 1,
   "message" : "Chýbajúce údaje",
   "error_message" : "Chýbajúce údaje"
}
```

#### Insufficient privileges
Status 403.

```sh
{
   "error" : 1,
   "message" : "Chýbajúce údaje",
   "error_message" : "Chýbajúce údaje"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Delete stock item

Delete stock item


### Request
**URL**: `/stock_items/delete/{ID}`  
**HTTP method**: GET  


```sh
curl -X GET \
     -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
     https://moja.superfaktura.sk/stock_items/delete/196
```

```sh
data='{"ids":"196,197"}';

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
    "data" : {
        "StockItem" : {
            "created" : "2019-01-25 07:45:54",
            "description" : "",
            "hide_in_autocomplete" : null,
            "id" : "18",
            "import_id" : null,
            "import_type" : null,
            "internal_comment" : "",
            "modified" : "2019-01-25 07:45:54",
            "name" : "Vitamin A",
            "sku" : "VitA",
            "stock" : null,
            "unit" : "",
            "unit_price" : 10,
            "user_id" : "384",
            "user_profile_id" : "393",
            "vat" : 20,
            "watch_stock" : "0"
        }
    },
    "error_message" : "",
    "error" : 0
}
```


#### Invalid item ID
```json
{
   "error_message" : "Invalid stock item id.",
   "error" : 1
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
   "error" : 1,
   "error_message" : "Nemôžete zmazať túto skladovú položku",
   "message" : "Nemôžete zmazať túto skladovú položku"
}
```




- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



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
| **created**               | int    | constant specifying time filtering (see *Value lists > Time filer constants*) |               |
| **created_since**         | date   | creation date since                           |               |
| **created_to**            | date   | creation date to                              |               |
| **description**           | string | item description (is displayed on invoice)    |               |
| **hide_in_autocomplete**  | int    | hide in autocomplete (null = no)              |               |
| **id**                    | int    | item ID                                       |               |
| **import_id**             | int    | import ID (if is not from import = null)      |               |
| **import_type**           | string | import type ('efaktury' or `null`)            |               |
| **internal_comment**      | string | internal comment (isn't displayed on invoice) |               | 
| **modified**              | int    | constant specifying time filtering (see *Value lists > Time filer constants*) |               |
| **modified_since**        | date   | last modification date from                   |               |
| **modified_to**           | date   | last modification date to                     |               |
| **name**                  | string | item name                                     |               |
| **sku**                   | int    | stock item identifier (e.g. ABC123)           |               |
| **stock**                 | float  | number of items in stock                      |               |
| **unit**                  | string | unit (e.g. ks, kg)                            |               |
| **unit_price**            | float  | unit price                                    |               |
| **user_id**               | int    | user ID                                       |               |
| **user_profile_id**       | int    | user profile ID                               |               |
| **vat**                   | float  | VAT in percent (e.g. 20)                      |               |
| **watch_stock**           | int    | track inventory level (0=no, 1=yes)           |               |

### Success
```json
[
   {
      "StockItem" : {
         "created" : "2017-09-27 12:40:02",
         "description" : "",
         "hide_in_autocomplete" : null,
         "id" : "1234",
         "import_id" : null,
         "import_type" : null,
         "internal_comment" : "",
         "modified" : "2017-09-27 12:40:02",
         "name" : "Maslo",
         "sku" : "",
         "stock" : 0,
         "unit" : "ks",
         "unit_price" : 4.5,
         "user_id" : "111",
         "user_profile_id" : "123",
         "vat" : 0,
         "watch_stock" : "1"
      }
   }
]
```

### Success with listing information

```json
{
   "page" : 1,
   "perPage" : 50,
   "pageCount" : 1,
   "items" : [
      {
         "StockItem" : {
            "created" : "2019-01-25 10:55:24",
            "description" : "Public description of this item",
            "hide_in_autocomplete" : "1",
            "id" : "19",
            "import_id" : null,
            "import_type" : null,
            "internal_comment" : "Secret comment",
            "modified" : "2019-01-25 10:55:24",
            "name" : "",
            "sku" : "itemb1241",
            "stock" : 123,
            "unit" : "m",
            "unit_price" : 19.95,
            "user_id" : "384",
            "user_profile_id" : "393",
            "vat" : 20,
            "watch_stock" : "1"
         }
      }
   ],
   "itemCount" : 1
}
```

- - - - - - - - - - - - - - - - - - - - - 


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
        "id":19
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
   "error" : 0,
   "error_message" : "",
   "data" : {
      "StockItem" : {
         "id" : 19,
         "name" : "Item B",
         "unit" : "kg"
      }
   }
}
```

#### Insufficient privileges
HTTP status 403

```json
{
   "error" : 1,
   "error_message" : "Nemôžete editovať túto skladovú položku",
   "message" : "Nemôžete editovať túto skladovú položku"
}
```

#### Wrong item ID
```json
{
   "error":2,
   "error_message":"StockItem id not found."
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


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
   "error" : 0,
   "error_message" : "",
   "data" : {
      "StockLog" : [
         {
            "id" : 0,
            "quantity" : 2,
            "stock_item_id" : "19"
         }
      ]
   }
}
```

#### Invalid data
```json
{
   "error" : 3,
   "error_message" : "StockItem empty data."
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
    https://moja.superfaktura.sk/stock_items/view/19
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
   "0" : {
      "StockItem" : {
         "created" : "2019-01-25 10:55:24",
         "description" : "Public description of this item",
         "hide_in_autocomplete" : null,
         "id" : "19",
         "import_id" : null,
         "import_type" : null,
         "internal_comment" : "Secret comment",
         "modified" : "2019-01-30 13:56:54",
         "name" : "Item B",
         "sku" : "itemb1241",
         "stock" : 138,
         "unit" : "kg",
         "unit_price" : 19.95,
         "user_id" : "384",
         "user_profile_id" : "393",
         "vat" : 20,
         "watch_stock" : "1"
      }
   }
}
```

#### Wrong stock item

```json
{
   "error" : 1,
   "error_message" : "Skladová položka nenájdená",
   "message" : "Skladová položka nenájdená"
}
```