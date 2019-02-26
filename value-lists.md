Value lists
===========

## Period types

| value       | description                                           |
| ----------- | ----------------------------------------------------- |
| **daily**   | must contain `D`* character, is refreshed every day   |
| **monthly** | must contain `M`* character, is refreshed every month |
| **yearly**  | must contain `Y`* character, is refreshed every year  |

&#42; - or its equivalent based on language (e.g. `J` for `Y`, in German) 


## Language list

List of languages as defined by [ISO-639-2](https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes).

| value   | description         |
| ------- | ------------------- |
| **cze** | Czech               |
| **deu** | German              |
| **eng** | English             |
| **hrv** | Croatian            |
| **hun** | Hungarian           |
| **pol** | Polish              |
| **rom** | Romanian            |
| **rus** | Russian             |
| **slo** | Slovak              |
| **slv** | Slovene / Slovenian |
| **ukr** | Ukrainian           |


## Currencies

Currencies use [ISO-4217 format](https://en.wikipedia.org/wiki/ISO_4217).
Accepted currencies are:

| value   | description             |
| ------- | ----------------------- |
| **AUD** | Australian dollar       |
| **BGN** | Bulgarian lev           |
| **CAD** | Canadian dollar         |
| **CHF** | Swiss franc             |
| **CNY** | Renminbi (Chinese) yuan |
| **CZK** | Czech koruna            |
| **DKK** | Danish krone            |
| **EUR** | Euro                    |
| **GBP** | British pound           |
| **HRK** | Croatian kuna           |
| **HUF** | Hungarian forint        |
| **JPY** | Japanese yen            |
| **LKR** | Sri Lankan rupee        |
| **MXN** | Mexican peso            |
| **PLN** | Polish złoty            |
| **RON** | Romanian leu            |
| **RSD** | Serbian dinar           |
| **RUB** | Russian ruble           |
| **SEK** | Swedish krona           |
| **USD** | United States dollar    |


## Payment types

| value               | description              | Slovak           |
| ------------------- | ------------------------ | ---------------- |
| **accreditation**   | mutual credit            | vzajomný zápočet |
| **besteron**        | Besteron (on SK version) |                  |
| **cash**            | cash                     | hotovosť         |
| **cod**             | cash on delivery         | dobierka         |
| **credit**          | credit card              | kreditná karta   |
| **debit**           | debit card               | debetná karta    |
| **gopay**           | GoPay                    |                  |
| **other**           | other                    | iný spôsob       |
| **paypal**          | Paypal                   |                  |
| **postal_order**    | Postal money order       |                  |
| **transfer**        | wire transfer            | bankový prevod   |
| **trustpay**        | Trustpay (on SK version) |                  |
| **viamo**           | Viamo                    |                  |


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Country list

Get list of countries in `id: country_name` format.
You can request more information (`iso`, `eu`)

### Simple example

#### Request
**URL**: `/countries`  
**HTTP method**: GET  

```sh
curl \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
    https://moja.superfaktura.sk/countries
```
  
#### Attributes

none

#### Response
JSON object containing list of countries in key-value format: `country_id: country_name`.

Example (list is shortened):  
```json
{
  "191":"Slovensko",
  "1":"Afganistan",
  "2":"Albania"
}
```


### Advanced example

#### Request
**URL**: `/countries/index/view_full:1`  
**HTTP method**: GET  

```sh
curl \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
    https://moja.superfaktura.sk/countries/index/view_full:1
```
  
#### Attributes

##### Required

In order to get full listing, you need to provide `view_full` equal to 1.

URL parameters:

| name          | type | description                 | default value |
| ------------- | ---- | --------------------------- | ------------- |
| **view_full** | int  | view additional information |               |

##### Optional
none

#### Response
JSON object containing list of countries under country_id index.
`iso` is country code ([ISO-3166-1 (Alpha-2)](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
`eu` tells whether country is in the European Union.

Example (list is shortened):  
```json
{
   "62" : {
      "eu" : "0",
      "iso" : "tp",
      "name" : "East Timor",
      "id": "62"
   },
   "57" : {
      "iso" : "cz",
      "name" : "Česká republika",
      "eu" : "1",
      "id": "57"
   },
   "191" : {
      "name" : "Slovensko",
      "iso" : "sk",
      "eu" : "1",
      "id": "191"
   }
}
```



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Sequences

Get list of sequences categorized by document type (i.e. "regular", "proforma", "reverse_order", ...).

### Request
**URL**: `/sequences/index.json`  
**HTTP method**: GET  


```sh
curl \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
    https://moja.superfaktura.sk/sequences/index.json
```
  
### Attributes

none

### Response  

JSON object.
Key is name of document type. Value is an array of sequences.
Empty key is reserved for Warehouse.

```json
{
   "regular" : [
      {
         "created" : "2017-09-19 08:15:36",
         "default" : "1", 
         "id" : "238534",
         "item_type" : "regular",
         "mask" : "RRRRCCC",
         "modified" : "2017-09-25 13:10:04",
         "name" : "Faktúra",
         "period_type" : "yearly",
         "sequence" : "6",
         "sequence_formatted" : "2017006",
         "user_profile_id" : "123"
      }
   ]
}

```

| name                   | type   | description | default value |
| ---------------------- | ------ | ----------- | ------------- |
| **created**            | date   | creation date | |
| **default**            | int    | is sequence default for document type? (0 = no, 1 = yes) | | 
| **id**                 | int    | sequence ID | |
| **item_type**          | string | document type (invoice, proforma, reverse order, ...) | |
| **mask**               | string | mask (e.g. `YYYYNNN`) | |
| **modified**           | date   | modification date | |
| **name**               | string | sequence name | |
| **period_type**        | string | period type (yearly / monthly / daily) | |
| **sequence**           | string | not formatted next sequence number of document | |
| **sequence_formatted** | string | formatted sequence number according to document type mask | |
| **user_profile_id**    | int    | user profile ID | | 



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Tags

See [Tags > Get list of tags](tags.md#get-list-of-tags).

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Logos

Returns list of logos.

### Request

**URL**: `/users/logo`  
**HTTP method**: GET  

```sh
    curl \
      -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
      https://moja.superfaktura.sk/users/logo
```

### Attributes

none

### Response

Array of logo objects containing the following information.

Fields:

| name              | type   | description | default value |
| ----------------- | ------ | ----------- | ------------- |
| **alternative**   | string | filename of user uploaded file (may not be set) | |
| **basename**      | string | name of logo file | |
| **checksum**      | string | checksum of logo | |
| **created**       | date   | creation date | |
| **default**       | string | is this logo default "0" = no, "1" = yes | |
| **dirname**       | string | directory with logo | |
| **foreign_key**   | int    | user profile ID | |
| **group**         | string | attachment type ("logo", "signature", ...) | |
| **id**            | int    | logo ID | |
| **model**         | string | what model is logo attached to (for logos it's always "User") | |
| **modified**      | date   | modification date | |
| **url**           | string | full URL to logo | |


Example:  
```json
[
   {
      "alternative" : null,
      "basename" : "123_8dcd924a.png",
      "checksum" : "9fb2a07e4ff2e1ffa091c9b38e7bf5fc",
      "created" : "2017-09-26 12:26:05",
      "default" : "0",
      "dirname" : "img",
      "foreign_key" : "123",
      "group" : "logo",
      "id" : "126124",
      "model" : "User",
      "modified" : "2017-09-26 12:26:10",
      "url" : "https://moja.superfaktura.sk/media/transfer/img/123_8dcd924a.png"
   }
]
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 


## Expense categories

Get list of expense categories.

### Request
**URL**: `/expenses/expense_categories`  
**HTTP method**: GET  

```sh
curl \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/expenses/expense_categories
```  

### Attributes

none

### Response
  
JSON array containing expense categories objects.

**Fields**

| name                | type   | description                        | default value |
| ------------------- | ------ | ---------------------------------- | ------------- |
| **children**        | array  | children of expense category       |               |
| **ExpenseCategory** | object | information about expense category |               |

*ExpenseCategory fields*:

| name                | type   | description        | default value |
| ------------------- | ------ | ------------------ | ------------- |
| **id**              | int    | category ID        |               |
| **lft**             | int    | left subtree       |               |
| **name**            | string | item name          |               |
| **parent_id**       | int    | parent category ID |               |
| **rght**            | int    | right subtree      |               |
| **user_id**         | int    | user ID            |               |
| **user_profile_id** | int    | user profile ID    |               |

Via `lft` and `rght` is modeled hierarchical structure of data.
For more information see [*Modified Preorder Tree Traversal*](https://www.sitepoint.com/hierarchical-data-database-2/). 


Example:  
```json
[
   {
      "ExpenseCategory" : {
         "rght" : "2145138936",
         "id" : "639970",
         "user_profile_id" : "27821",
         "lft" : "2145138935",
         "name" : "Administrácia",
         "user_id" : "33559",
         "parent_id" : null
      },
      "children" : [
        {
          "ExpenseCategory" : {
               "rght" : "2145138936",
               "id" : "639971",
               "user_profile_id" : "27821",
               "lft" : "2145138935",
               "name" : "Vnorená administrácia",
               "user_id" : "33559",
               "parent_id" : "639970"
          },
          "children": []
        }
      ]
   }
]
``` 


## Time filters

| value         | description    |
| ------------- | -------------- |
| **today**     | today          |
| **yesterday** | yesterday      |
| **thismonth** | this month     |
| **thisyear**  | this year      |
| **prevmonth** | previous month |
| **prevyear**  | previous year  |


## Expense types

| value                    | description          |
| ------------------------ | -------------------- |
| **bill**                 | Bill                 |
| **contribution**         | Contributions        |
| **internal**             | Internal document    |
| **invoice**              | Received invoice     |
| **nondeductible**        | Non-tax expense      |
| **recieved_credit_note** | Received credit note |


## Invoice statuses

| value  | description    |
| -----: | -------------- |
| **1**  | issued         |
| **2**  | partially_paid |
| **3**  | paid           |
| **99** | overdue        |


## Expense statuses

| value  | description    |
| -----: | -------------- |
| **1**  | new            |
| **2**  | partially_paid |
| **3**  | paid           |
| **99** | overdue        |


## Expense types

| value                    | description          | Slovak           |
| ------------------------ | -------------------- | ---------------- |
| **bill**                 | bill                 | pokladničný blok |
| **contribution**         | contribution         | odvody           |
| **internal**             | internal document    | interný doklad   |
| **invoice**              | received invoice     | prijatá faktúra  |
| **nondeductible**        | non deductible       | nedaňový doklad  |
| **recieved_credit_note** | received credit note | prijatý dobropis |


## Invoice types
| value             | description       | Slovak                        |
| ----------------- | ----------------- | ----------------------------- |
| **cancel**        | credit note       | dobropis                      |
| **delivery**      | delivery note     | dodací list                   |
| **draft**         | concept           | koncept                       |
| **estimate**      | price estimate    | cenová ponuka                 |
| **order**         | order             | prijatá objednávka            |
| **proforma**      | proforma invoice  | zálohová faktúra              |
| **regular**       | regular invoice   | ostrá faktúra / bežná faktúra |
| **reverse_order** | reverse order     | objednávka                    |


## Rounding types

Different rounding types are used for VAT calculations.

| value        | description                      |
| ------------ | -------------------------------- |
| **document** | whole document                   |
| **item**     | per item (default))           |
| **item_ext** | retail (recommended for e-shops) |


**Document**  
VAT is calculated from the sum of items' prices and then rounded.

**Item**  
For each item price without VAT and with VAT is calculated.
Then difference between them, which is VAT.

**Item_ext**  
After each step prices are rounded to 2 decimal numbers.
From each item is calculated price with VAT (rounded), than multiplied by quantity (rounded).
Then difference between this value and value per item without VAT is added to VAT.



## Delivery types

| value            | description       | Slovak           |
| ---------------- | ----------------- | ---------------- |
| **courier**      | courier           | kuriér           |
| **haulage**      | freight transport | nákladná doprava |
| **mail**         | mail / post       | poštou           |
| **personal**     | personal pickup   | osobný odber     |
| **pickup_point** | pickup point      | odberné miesto   |



## Time filter constants

| value  | description  |
| -----: | ------------ |
| **0**  | all          |
| **1**  | today        |
| **2**  | yesterday    |
| **3**  | since to     |
| **4**  | this month   |
| **5**  | last month   |
| **6**  | this year    |
| **7**  | last year    |
| **8**  | this quarter |
| **9**  | this week    |
| **10** | last quarter |
| **11** | last hour    |
| **12** | this hour    |