## Create client

Creates or edits client.

Decision whether clients exists or is new is explained in the following table:

| Property to match       | Status |
| ----------------------- | ------ |
| UUID                    | exists |
| ID (IČO)                | exists |
| Tax ID (DIČ)            | exists |
| client ID               | exists |
| client name and address | exists |
| client name and email   | exists |
| otherwise               | new    |

    BEWARE: this decision making will be changed in near future.
    So we recommend to check for updates to avoid any problems.

If you want to add tags to client, refer to *FAQ > How do I add tags to an entity?*.


### Request

**URL**: `/clients/create`  
**HTTP method**: POST  

```sh
data='{
    "Client":{
        "name":"Superfaktura s.r.o."
    }
}';

curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/clients/create
```

### Attributes

#### Optional

| name                      | type   | description                                                     | default value |
| ------------------------- | ------ | --------------------------------------------------------------- | ------------- |
| **address**               | string | street / address                                                | |
| **bank_account**          | string | bank account (when not using IBAN)                              | |
| **bank_account_id**       | int    | bank account ID                                                 | |
| **bank_account_prefix**   | string | bank account prefix                                             | |
| **bank_code**             | string | bank account code (when not using IBAN)                         | |
| **city**                  | string | city                                                            | |
| **comment**               | string | comment                                                         | |
| **country**               | string | country name                                                    | |
| **country_id**            | int    | country ID (see *Value lists > Country list*)                   | 191 (Slovakia), 57 (Czech republic) |
| **currency**              | string | currency (see *Value lists > Currencies*)                       | |
| **default_variable**      | string | default variable symbol for client                              | |
| **delivery_address**      | string | delivery address                                                | |
| **delivery_city**         | string | delivery city                                                   | |
| **delivery_country**      | string | delivery country name                                           | |
| **delivery_country_id**   | int    | delivery country ID (see *Value lists > Country list*)          | |
| **delivery_name**         | string | delivery company name                                           | |
| **delivery_phone**        | string | delivery phone                                                  | |
| **delivery_state**        | string | delivery state (only for the USA)                               | |
| **delivery_zip**          | string | delivery ZIP                                                    | |
| **dic**                   | string | Tax ID (DIČ)                                                    | |
| **discount**              | float  | discount                                                        | |
| **distance**              | float  | distance from you to client (used in Logbook)                   | |
| **dont_travel**           | int    | don't use this client in rides reconstruction (0 = no, 1 = yes) | |
| **due_date**              | int    | default number of days until due date                           | |
| **email**                 | string | email                                                           | |
| **fax**                   | string | fax                                                             | |
| **iban**                  | string | IBAN                                                            | |
| **ic_dph**                | string | VAT ID (IČ DPH)                                                 | |
| **ico**                   | string | ID (IČO)                                                        | |
| **id**                    | int    | client ID                                                       | |
| **name**                  | string | client name                                                     | |
| **notices**               | int    | send automatic notices, (0 = no, 1 = yes)                       | |
| **phone**                 | string | phone number                                                    | |
| **state**                 | string | state name (only for the USA)                                   | |
| **swift**                 | string | SWIFT code                                                      | |
| **uuid**                  | string | unique client UUID - client identifier in your system           | null |
| **zip**                   | string | ZIP code                                                        | |


### Response

#### Successfully changed name
```sh
data='{
    "Client":{
        "id":23,
        "name":"Foobar",
        "update":1
    }
}';

curl -X POST --post-data="data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/clients/create
```

```json
{
   "error_message" : "Client created",
   "error" : 0,
   "data" : {
      "Client" : {
         "country_id" : "191",
         "created" : "2017-11-08 09:20:33",
         "bank_account_prefix" : null,
         "city" : null,
         "currency" : null,
         "country" : null,
         "modified" : "2017-11-08 09:31:05",
         "delivery_address" : null,
         "uuid" : "NULL",
         "ico" : null,
         "update" : "1",
         "name" : "FooBar",
         "bank_account_id" : null,
         "bank_account" : null,
         "dic" : null,
         "delivery_phone" : null,
         "address" : null,
         "email" : null,
         "delivery_city" : null,
         "phone" : null,
         "delivery_zip" : null,
         "discount" : null,
         "id" : "23",
         "zip" : null,
         "user_id" : "3",
         "notices" : "1",
         "due_date" : null,
         "comment" : null,
         "dont_travel" : null,
         "tags" : null,
         "delivery_name" : null,
         "bank_code" : null,
         "user_profile_id" : "1",
         "delivery_state" : null,
         "state" : null,
         "distance" : null,
         "default_variable" : null,
         "swift" : null,
         "delivery_country_id" : null,
         "fax" : null,
         "delivery_country" : null,
         "iban" : null,
         "ic_dph" : null
      }
   }
}
```


#### Successfully created client
```sh
data='{
    "Client":{
        "name":"FooBar s.r.o."
    }
}';

curl -X POST \ 
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/clients/create
```

```json
{
   "data" : {
      "Client" : {
         "address" : null,
         "bank_account" : null,
         "bank_account_id" : null,
         "bank_account_prefix" : null,
         "bank_code" : null,
         "city" : null,
         "comment" : null,
         "country" : null,
         "country_id" : "191",
         "created" : "2017-11-08 09:20:33",
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
         "id" : "23",
         "modified" : "2017-11-08 09:20:33",
         "name" : "FooBar s.r.o.",
         "notices" : "1",
         "phone" : null,
         "state" : null,
         "swift" : null,
         "tags" : null,
         "update" : "0",
         "user_id" : "3",
         "user_profile_id" : "1",
         "uuid" : "NULL",
         "zip" : null
      }
   },
   "error" : 0,
   "error_message" : "Client created"
}
```


#### Missing data
```json
{
   "error_message" : "Chýbajúce údaje",
   "error" : 1
}
```

#### Duplicate client  
```json
{
   "error" : 1,
   "error_message" : {
      "name" : "Nemožno vytvoriť duplicitného klienta."
   }
}
```




- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## View client detail

View client details.

### Request

**URL**: `/clients/view/{ID}`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/clients/view/431
```

### Attributes

#### Required
| name            | type | description | default value |
| --------------- | ---- | ----------- | ------------- |
| **id**          | int  | client ID   |               |

#### Optional
none

### Response

```json
{
   "Country" : {
      "created" : "2010-11-02 22:19:37",
      "eu" : "1",
      "id" : "191",
      "iso" : "sk",
      "modified" : "2010-11-02 22:19:37",
      "name" : "Slovensko",
      "order" : "1"
   },
   "Tag" : [],
   "ContactPerson" : [
      {
         "client_id" : "431",
         "created" : "2019-02-05 10:36:09",
         "email" : "john@example.com",
         "id" : "13",
         "modified" : "2019-02-05 10:36:09",
         "name" : "John",
         "phone" : null,
         "user_id" : "384",
         "user_profile_id" : "393"
      },
      {
         "client_id" : "431",
         "created" : "2019-02-05 10:36:09",
         "email" : "test@tesf.asdk",
         "id" : "18",
         "modified" : "2019-02-05 10:36:09",
         "name" : "test",
         "phone" : null,
         "user_id" : "384",
         "user_profile_id" : "393"
      },
      {
         "client_id" : "431",
         "created" : "2019-02-05 10:43:32",
         "email" : "test@test.com",
         "id" : "19",
         "modified" : "2019-02-05 10:43:32",
         "name" : "ja",
         "phone" : "00421987564321",
         "user_id" : "384",
         "user_profile_id" : "393"
      }
   ],
   "Client" : {
      "address" : "Pri Suchom mlyne 6",
      "bank_account" : "",
      "bank_account_id" : "0",
      "bank_account_prefix" : "",
      "bank_code" : "",
      "city" : "Bratislava - mestsk&aacute; časť Star&eacute; Mesto",
      "comment" : "",
      "country" : "",
      "country_id" : "191",
      "created" : "2019-01-23 08:41:37",
      "currency" : "",
      "default_variable" : "",
      "delivery_address" : "",
      "delivery_city" : "",
      "delivery_country" : "",
      "delivery_country_id" : "191",
      "delivery_name" : "",
      "delivery_phone" : "",
      "delivery_state" : "",
      "delivery_zip" : "",
      "dic" : "2022903949",
      "discount" : "",
      "distance" : "",
      "dont_travel" : "0",
      "due_date" : "",
      "email" : "name.surname@superfaktura.sk",
      "fax" : "",
      "iban" : "",
      "ic_dph" : "",
      "ico" : "44981082",
      "id" : "431",
      "modified" : "2019-02-07 14:29:28",
      "name" : "2day, s. r. o.",
      "notices" : "1",
      "phone" : "",
      "state" : "",
      "swift" : "",
      "tags" : "",
      "update" : "1",
      "user_id" : "384",
      "user_profile_id" : "393",
      "uuid" : "NULL",
      "zip" : "811 04"
   }
}
```

#### Wrong client
```json
{
   "error" : 1,
   "error_message" : "Client not found"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Get client list

Get list of clients based on filtering parameters.

### Request

**URL**: `/clients/index.json[/{ATTRIBUTE}:{VALUE}]*`  
**HTTP method**: GET  

Other URL examples:
- `/clients/index.json`  
- `/clients/index.json/listinfo:1`  
- `/clients/index.json/search:superfaktura`  
- `/clients/index.json/listinfo:1/search:c3VwZXJmYWt0dXJh`

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/clients/index.json
```


### Attributes  

#### Required
none

#### Optional

| name            | type   | description | default value |
| --------------- | ------ | ----------- | ------------- |
| **char_filter** | string | search by first letter of client name (non letter characters are under `#`) | |
| **direction**   | string | sorting type, `ASC` or `DESC`| `DESC` |
| **list_info**   | int    | should meta information be returned? <ul><li>page number</li><li>number of pages</li><li>number of results per page</li><li>number of results</li></ul> | |
| **per_page**    | int    | number of results per page | |
| **search**      | string | search by base64 encoded substring in the following fields: <ul><li>name</li><li>ID (ICO)</li><li>Tax ID (DIC)</li><li>VAT ID (IC_DPH)</li><li>bank_account</li><li>email</li><li>address</li><li>city</li><li>zip</li><li>state</li><li>country</li><li>phone</li><li>fax</li><li>comment</li><li>tags</li><li>UUID</li></ul> | |
| **search_uuid** | string | search by UUID | | 
| **sort**        | string | sorting attribute | `regular_count` |
| **tag**         | int    | tag ID | |


### Response

#### Get all the clients  
```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/clients/index.json
```

```json
[
   {
      "ClientStat" : {
         "cancel_count" : "0",
         "cancel_total" : "0.00",
         "client_id" : "431",
         "date_founded" : "0000-00-00",
         "delivery_count" : "0",
         "delivery_total" : "0.00",
         "estimate_count" : "0",
         "estimate_total" : "0.00",
         "expense_count" : "0",
         "expense_total" : "0.00",
         "expense_unpaid_count" : "0",
         "expense_unpaid_total" : "0.00",
         "id" : "420",
         "order_count" : "0",
         "order_total" : "0.00",
         "pay_time" : "0.00",
         "proforma_count" : "0",
         "proforma_overdue_count" : "0",
         "proforma_overdue_total" : "0.00",
         "proforma_total" : "0.00",
         "regular_count" : "0",
         "regular_overdue_count" : "0",
         "regular_overdue_total" : "0.00",
         "regular_total" : "0.00",
         "reverse_order_count" : "0",
         "reverse_order_total" : "0.00",
         "risk" : "2"
      },
      "Client" : {
         "address" : "Pri Suchom mlyne 6",
         "bank_account" : "",
         "bank_account_id" : "0",
         "bank_account_prefix" : "",
         "bank_code" : "",
         "city" : "Bratislava - mestská časť Staré Mesto",
         "comment" : "",
         "country" : null,
         "country_id" : "191",
         "created" : "2019-01-23 08:41:37",
         "currency" : null,
         "default_variable" : "",
         "delivery_address" : "",
         "delivery_city" : "",
         "delivery_country" : null,
         "delivery_country_id" : "191",
         "delivery_name" : "",
         "delivery_phone" : "",
         "delivery_state" : "",
         "delivery_zip" : "",
         "dic" : "2022903949",
         "discount" : null,
         "distance" : null,
         "dont_travel" : "0",
         "due_date" : null,
         "email" : "name.surname@superfaktura.sk",
         "fax" : "",
         "iban" : "",
         "ic_dph" : "",
         "ico" : "44981082",
         "id" : "431",
         "modified" : "2019-02-08 08:40:00",
         "name" : "2day, s. r. o.",
         "notices" : "1",
         "phone" : "",
         "state" : "",
         "swift" : "",
         "tags" : null,
         "update" : "1",
         "user_id" : "384",
         "user_profile_id" : "393",
         "uuid" : "NULL",
         "zip" : "811 04"
      }
   }
]
```


#### With info listing
  
```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/clients/index.json/listinfo:1
```

In the key `items` is the same content as in the example above.

```json
{
    "pageCount" : 1,
    "itemCount" : 20,
    "page" : 1,
    "perPage" : 50,
    "items" : [
    ]
}
```
