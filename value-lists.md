# Value lists

- [Country list](#country-list)
- [Currencies](#currencies)
- [Delivery types](#delivery-types)
- [Expense categories](#expense-categories)
- [Expense types](#expense-types)
- [Expenses statuses](#expense-statuses)
- [Invoice statuses](#invoice-statuses)
- [Invoice types](#invoice-types)
- [Language list](#language-list)
- [Logos](#logos)
- [Payment types](#payment-types)
- [Period types](#period-types)
- [Rounding types](#rounding-types)
- [Sequences](#sequences)
- [Tags](#tags)
- [Time filter constants](#time-filter-constants)
- [Time filters](#time-filters)


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
  "1": "Afganistan",
  "10": "Argentina",
  "100": "Iceland"
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
Array containing JSON objects.
`iso` is country code ([ISO-3166-1 (Alpha-2)](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
`eu` tells whether country is in the European Union.

Example (list is shortened):  
```json
[
  {
    "Country": {
      "eu": true,
      "id": 191,
      "iso": "sk",
      "name": "Slovensko"
    }
  },
  {
    "Country": {
      "eu": false,
      "id": 1,
      "iso": "af",
      "name": "Afganistan"
    }
  },
  {
    "Country": {
      "eu": false,
      "id": 2,
      "iso": "al",
      "name": "Albania"
    }
  }
]
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Currencies

Currencies use [ISO-4217 format](https://en.wikipedia.org/wiki/ISO_4217).
Accepted currencies are:

| value   | description             |
| ------- | ----------------------- |
| **AED** |  Uae Dirham             |
| **AFN** |  Afghani                |
| **ALL** |  Albanian lek           |
| **AMD** |  Armenian Dram          |
| **ANG** |  Antily gulden          |
| **AOA** |  Angolan Kwanza         |
| **ARS** |  Argentine Peso         |
| **AUD** |  Australian Dollar      |
| **AWG** |  Aruban florin          |
| **AZN** |  Azerbaijanian Manat    |
| **BAM** |  Convertible Marks      |
| **BBD** |  Barbados Dollar        |
| **BDT** |  Bangladeshi Taka       |
| **BGN** |  Bulgarian lev          |
| **BHD** |  Bahraini Dinar         |
| **BIF** |  Burundi Franc          |
| **BMD** |  Bermuda Dollar         |
| **BND** |  Brunei Dollar          |
| **BOB** |  Boliviano              |
| **BRL** |  Brazilian real         |
| **BSD** |  Bahamian Dollar        |
| **BTN** |  Bhutanese Ngultrum     |
| **BWP** |  Botswana Pula          |
| **BYN** |  Belarussian Ruble      |
| **BZD** |  Belize Dollar          |
| **CAD** |  Canadian dollar        |
| **CDF** |  Franc Congolais        |
| **CHF** |  Swiss Franc            |
| **CLP** |  Chilean Peso           |
| **CNY** |  Chinese Yuan           |
| **COP** |  Colombian Peso         |
| **CRC** |  Costa Rican Colon      |
| **CUP** |  Cuban Peso             |
| **CVE** |  Cape Verde Escudo      |
| **CZK** |  Czech Crown            |
| **DJF** |  Djibouti Franc         |
| **DKK** |  Danish krone           |
| **DOP** |  Dominican Peso         |
| **DZD** |  Algerian Dinar         |
| **EGP** |  Egyptian Pound         |
| **ERN** |  Eritrean Nakfa         |
| **ETB** |  Ethiopian Birr         |
| **EUR** |  Euro                   |
| **FJD** |  Fiji Dollar            |
| **FKP** |  Falkland Islands pound |
| **GBP** |  British pound          |
| **GEL** |  Georgian lari          |
| **GHS** |  Chana Cedi             |
| **GIP** |  Gibraltar pound        |
| **GMD** |  Gambian Dalasi         |
| **GNF** |  Guinea Franc           |
| **GTQ** |  Guatemalan quetzal     |
| **GYD** |  Guyana Dollar          |
| **HKD** |  Hong Kong Dollar       |
| **HNL** |  Honduran lempira       |
| **HRK** |  Croatian kuna          |
| **HTG** |  Haitian gourde         |
| **HUF** |  Hungarian forint       |
| **IDR** |  Indonesian Rupiah      |
| **ILS** |  Israeli shekel         |
| **INR** |  Indian Rupee           |
| **IQD** |  Iraqi Dinar            |
| **IRR** |  Iranian Rial           |
| **ISK** |  Icelandic króna        |
| **JMD** |  Jamaican Dollar        |
| **JOD** |  Jordanian Dinar        |
| **JPY** |  Japanese yen           |
| **KES** |  Kenyan Shilling        |
| **KGS** |  Kirghiz Som            |
| **KHR** |  Cambodian Riel         |
| **KMF** |  Comorian Franc         |
| **KPW** |  North Korean Won       |
| **KRW** |  South Korean won       |
| **KWD** |  Kuwaiti Dinar          |
| **KYD** |  Cayman Islands Dollar  |
| **KZT** |  Kazakhstani tenge      |
| **LAK** |  Laotian kip            |
| **LBP** |  Lebanese Pound         |
| **LKR** |  Sri Lanka Rupee        |
| **LRD** |  Liberian Dollar        |
| **LSL** |  Lesotho loti           |
| **LYD** |  Lybian Dinar           |
| **MAD** |  Moroccan Dirham        |
| **MDL** |  Moldovan Leu           |
| **MGA** |  Malagascy Ariary       |
| **MKD** |  North Macedonian Denar |
| **MMK** |  Myanmar kyat           |
| **MNT** |  Mongolian tugrik       |
| **MOP** |  Macau pataca           |
| **MRO** |  Mauritian Ouguiya      |
| **MUR** |  Mauritian rupee        |
| **MVR** |  Maldivian Rupee        |
| **MWK** |  Malawian Kwacha        |
| **MXN** |  Mexican peso           |
| **MYR** |  Malaysian ringgit      |
| **MZN** |  Metical                |
| **NAD** |  Namibia Dollar         |
| **NGN** |  Nigerian naira         |
| **NIO** |  Cordoba Oro            |
| **NOK** |  Norwegian krone        |
| **NPR** |  Nepalese Rupee         |
| **NZD** |  New Zealand Dollar     |
| **OMR** |  Rial Omani             |
| **PAB** |  Balboa                 |
| **PEN** |  Peruvian Nuevo Sol     |
| **PGK** |  Kina Papua New Guinea  |
| **PHP** |  Philippine Peso        |
| **PKR** |  Pakistan Rupee         |
| **PLN** |  Polish zloty           |
| **PYG** |  Paraguayan guarani     |
| **QAR** |  Qatari Rial            |
| **RON** |  Romanian Leu (new)     |
| **RSD** |  Serbian Dinar          |
| **RUB** |  Russian ruble          |
| **RWF** |  Rwanda Franc           |
| **SAR** |  Saudi Riyal            |
| **SBD** |  Solomon Islands Dollar |
| **SCR** |  Seychelles Rupee       |
| **SDG** |  Sudanese Pound         |
| **SEK** |  Swedish Krona          |
| **SGD** |  Singapore dollar       |
| **SHP** |  St. Helena Pound       |
| **SLL** |  Sierra Leone           |
| **SOS** |  Somali Shilling        |
| **SRD** |  Surinam Dollar         |
| **SSP** |  South Sudanese Pound   |
| **STN** |  Dobra                  |
| **SVC** |  El Salvador Colon      |
| **SYP** |  Syrian Pound           |
| **SZL** |  Lilangeni              |
| **THB** |  Thai baht              |
| **TJS** |  Tajikistani Somoni     |
| **TMT** |  Turkmen Manat          |
| **TND** |  Tunisian Dinar         |
| **TOP** |  Tongan paʻanga         |
| **TRY** |  Turkish lira           |
| **TTD** |  Trinidad And Tobago Dollar |
| **TWD** |  New Taiwan Dollar      |
| **TZS** |  Tanzanian Shilling     |
| **UAH** |  Ukrainian Hryvnia      |
| **UGX** |  Uganda Shilling        |
| **USD** |  US Dollar              |
| **UYU** |  Peso Urugayo           |
| **UZS** |  Uzbekistan Sum         |
| **VEF** |  Venezuelan Bolivar     |
| **VND** |  Vietnamese Dong        |
| **VUV** |  Vanuatu Vatu           |
| **WST** |  Samoan tala            |
| **XAF** |  CFA Franc              |
| **XCD** |  East Caribbean Dollar  |
| **XOF** |  Franc BCEAO / CFA      |
| **XPF** |  Frank CFP              |
| **YER** |  Yemeni Rial            |
| **ZAR** |  South African Rand     |
| **ZMW** |  Zambian Kwacha         |
| **ZWL** |  Zimbabwe Dollar        |


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Delivery types

| value            | description       | Slovak           |
| ---------------- | ----------------- | ---------------- |
| **courier**      | courier           | kuriér           |
| **haulage**      | freight transport | nákladná doprava |
| **mail**         | mail / post       | poštou           |
| **personal**     | personal pickup   | osobný odber     |
| **pickup_point** | pickup point      | odberné miesto   |


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


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
    "children": [
      {
        "children": [],
        "icon": "bolt",
        "icon_color": "#1c212b",
        "id": 2,
        "name": "Nájomné / energie"
      },
      {
        "children": [],
        "icon": "paperclip",
        "icon_color": "#2d3239",
        "id": 3,
        "name": "Kancelárske potreby"
      },
      {
        "children": [],
        "icon": "wifi",
        "icon_color": "#585d65",
        "id": 4,
        "name": "Internet"
      },
      {
        "children": [],
        "icon": "phone",
        "icon_color": "#999fab",
        "id": 5,
        "name": "Telefón"
      },
      {
        "children": [],
        "icon": "laptop",
        "icon_color": "#b9c1cf",
        "id": 6,
        "name": "Hardware"
      },
      {
        "children": [],
        "icon": "mouse-pointer",
        "icon_color": "#cfd7e6",
        "id": 7,
        "name": "Software"
      }
    ],
    "icon": "building",
    "icon_color": "#3a4345",
    "id": 1,
    "name": "Kancelária"
  },
  {
    "children": [
      {
        "children": [],
        "icon": "abacus",
        "icon_color": "#004159",
        "id": 9,
        "name": "Účtovníctvo"
      },
      {
        "children": [],
        "icon": "user-tie",
        "icon_color": "#006083",
        "id": 10,
        "name": "Právne služby"
      },
      {
        "children": [],
        "icon": "landmark",
        "icon_color": "#007eac",
        "id": 11,
        "name": "Bankové poplatky a poistné"
      },
      {
        "children": [],
        "icon": "ad",
        "icon_color": "#4bb1d6",
        "id": 12,
        "name": "Reklama a marketing"
      },
      {
        "children": [],
        "icon": "envelope-open-text",
        "icon_color": "#87d0ea",
        "id": 13,
        "name": "Pošta"
      },
      {
        "children": [],
        "icon": "cloud",
        "icon_color": "#c2e5f2",
        "id": 14,
        "name": "Prevádzka"
      }
    ],
    "icon": "handshake",
    "icon_color": "#4cc3d9",
    "id": 8,
    "name": "Služby"
  },
  {
    "children": [
      {
        "children": [],
        "icon": "gas-pump",
        "icon_color": "#00594a",
        "id": 16,
        "name": "Palivo"
      },
      {
        "children": [],
        "icon": "car-mechanic",
        "icon_color": "#00836d",
        "id": 17,
        "name": "Servis"
      },
      {
        "children": [],
        "icon": "shield",
        "icon_color": "#00ac8f",
        "id": 18,
        "name": "Poistenie"
      },
      {
        "children": [],
        "icon": "money-bill",
        "icon_color": "#4bd6be",
        "id": 19,
        "name": "Odpisy"
      }
    ],
    "icon": "car",
    "icon_color": "#79c8a3",
    "id": 15,
    "name": "Auto"
  },
  {
    "children": [
      {
        "children": [],
        "icon": "laugh",
        "icon_color": "#5e2400",
        "id": 21,
        "name": "Mzdy"
      },
      {
        "children": [],
        "icon": "toilet",
        "icon_color": "#803706",
        "id": 22,
        "name": "Odvody"
      },
      {
        "children": [],
        "icon": "gift",
        "icon_color": "#cc5b0a",
        "id": 23,
        "name": "Ostatné"
      }
    ],
    "icon": "user",
    "icon_color": "#fdc65d",
    "id": 20,
    "name": "Zamestnanci"
  }
]
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Expense statuses

| value  | description    |
| -----: | -------------- |
| **1**  | new            |
| **2**  | partially_paid |
| **3**  | paid           |
| **99** | overdue        |


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Expense types

| value                    | description          | Slovak           |
| ------------------------ | -------------------- | ---------------- |
| **bill**                 | bill                 | pokladničný blok |
| **contribution**         | contribution         | odvody           |
| **internal**             | internal document    | interný doklad   |
| **invoice**              | received invoice     | prijatá faktúra  |
| **nondeductible**        | non deductible       | nedaňový doklad  |
| **recieved_credit_note** | received credit note | prijatý dobropis |


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Invoice statuses

| value  | description    |
| -----: | -------------- |
| **1**  | issued         |
| **2**  | partially_paid |
| **3**  | paid           |
| **99** | overdue        |


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Invoice types
| value             | description                  | Slovak                          |
| ----------------- | ---------------------------- | ------------------------------- |
| **cancel**        | credit note                  | dobropis                        |
| **delivery**      | delivery note                | dodací list                     |
| **draft**         | concept                      | koncept                         |
| **estimate**      | price estimate               | cenová ponuka                   |
| **order**         | order                        | prijatá objednávka              |
| **proforma**      | proforma invoice             | zálohová faktúra                |
| **regular**       | regular invoice              | ostrá faktúra / bežná faktúra   |
| **reverse_order** | reverse order                | objednávka                      |
| **tax_document**  | receipt for received payment | daňový doklad k prijatej platbe |


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Language list

List of languages as defined by [ISO-639-2](https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes).

| value   | description         |
| ------- | ------------------- |
| **cze** | Czech               |
| **deu** | German              |
| **eng** | English             |
| **hrv** | Croatian            |
| **hun** | Hungarian           |
| **ita** | Italian             |
| **nld** | Dutch               |
| **pol** | Polish              |
| **rom** | Romanian            |
| **rus** | Russian             |
| **slo** | Slovak              |
| **slv** | Slovene / Slovenian |
| **spa** | Spanish             |
| **ukr** | Ukrainian           |


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


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
| **default**       | bool   | is this logo default | |
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
    "model": "User",
    "modified": "2050-01-01 23:59:59",
    "path": "img/4311c1895aa334d39ac8_1_exads_logo_rgb.png",
    "size": "49743",
    "url": "http://moja.superfaktura.sk/media/transfer/img/4311c1895aa334d39ac8_1_exads_logo_rgb.png"
  }
]
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Payment types

| value               | description              | Slovak           |
| ------------------- | ------------------------ | ---------------- |
| **accreditation**   | mutual credit            | vzajomný zápočet |
| **barion**          | Barion                   |                  |
| **besteron**        | Besteron (on SK version) |                  |
| **cash**            | cash                     | hotovosť         |
| **card**            | card                     | karta            |
| **cod**             | cash on delivery         | dobierka         |
| **credit**          | credit card              | kreditná karta   |
| **debit**           | debit card               | debetná karta    |
| **inkaso**          | encashment               | inkaso           |
| **gopay**           | GoPay                    |                  |
| **other**           | other                    | iný spôsob       |
| **paypal**          | Paypal                   |                  |
| **transfer**        | wire transfer            | bankový prevod   |
| **trustpay**        | Trustpay (on SK version) |                  |
| **viamo**           | Viamo                    |                  |


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Period types

| value       | description                                           |
| ----------- | ----------------------------------------------------- |
| **daily**   | must contain `D`* character, is refreshed every day   |
| **monthly** | must contain `M`* character, is refreshed every month |
| **yearly**  | must contain `Y`* character, is refreshed every year  |

&#42; - or its equivalent based on language (e.g. `J` for `Y`, in German) 


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


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


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


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
  "cash_register_in": [
    {
      "created": "2050-01-01 23:59:59",
      "default": true,
      "id": "6",
      "item_type": "cash_register_in",
      "mask": "PRRRRCCC",
      "modified": "2050-01-01 23:59:59",
      "name": "PPD",
      "period_type": "yearly",
      "sequence": "1",
      "sequence_formatted": "P2020001",
      "user_profile_id": "1"
    }
  ],
  "cash_register_out": [
    {
      "created": "2050-01-01 23:59:59",
      "default": true,
      "id": "7",
      "item_type": "cash_register_out",
      "mask": "VRRRRCCC",
      "modified": "2050-01-01 23:59:59",
      "name": "VPD",
      "period_type": "yearly",
      "sequence": "1",
      "sequence_formatted": "V2020001",
      "user_profile_id": "1"
    }
  ],
  "delivery": [
    {
      "created": "2050-01-01 23:59:59",
      "default": true,
      "id": "8",
      "item_type": "delivery",
      "mask": "DODRRRRCCC",
      "modified": "2050-01-01 23:59:59",
      "name": "Dodací list",
      "period_type": "yearly",
      "sequence": "1",
      "sequence_formatted": "DOD2020001",
      "user_profile_id": "1"
    }
  ],
  "estimate": [
    {
      "created": "2050-01-01 23:59:59",
      "default": true,
      "id": "5",
      "item_type": "estimate",
      "mask": "PONRRRRCCC",
      "modified": "2050-01-01 23:59:59",
      "name": "Cenová ponuka",
      "period_type": "yearly",
      "sequence": "1",
      "sequence_formatted": "PON2020001",
      "user_profile_id": "1"
    }
  ],
  "expense": [
    {
      "created": "2050-01-01 23:59:59",
      "default": true,
      "id": "9",
      "item_type": "expense",
      "mask": "RRRRCCC",
      "modified": "2050-01-01 23:59:59",
      "name": "Náklad",
      "period_type": "yearly",
      "sequence": "1",
      "sequence_formatted": "2020001",
      "user_profile_id": "1"
    }
  ],
  "order": [
    {
      "created": "2050-01-01 23:59:59",
      "default": true,
      "id": "3",
      "item_type": "order",
      "mask": "OBJRRRRCCC",
      "modified": "2050-01-01 23:59:59",
      "name": "Prijatá objednávka",
      "period_type": "yearly",
      "sequence": "1",
      "sequence_formatted": "OBJ2020001",
      "user_profile_id": "1"
    }
  ],
  "proforma": [
    {
      "created": "2050-01-01 23:59:59",
      "default": true,
      "id": "2",
      "item_type": "proforma",
      "mask": "ZAL1RRRRCCC",
      "modified": "2050-01-01 23:59:59",
      "name": "Zálohová faktúra",
      "period_type": "yearly",
      "sequence": "1",
      "sequence_formatted": "ZAL12020001",
      "user_profile_id": "1"
    }
  ],
  "regular": [
    {
      "created": "2050-01-01 23:59:59",
      "default": true,
      "id": "1",
      "item_type": "regular",
      "mask": "RRRRCCC",
      "modified": "2050-01-01 23:59:59",
      "name": "Faktúra",
      "period_type": "yearly",
      "sequence": "1",
      "sequence_formatted": "2020001",
      "user_profile_id": "1"
    }
  ],
  "reverse_order": [
    {
      "created": "2050-01-01 23:59:59",
      "default": true,
      "id": "4",
      "item_type": "reverse_order",
      "mask": "VOBJRRRRCCC",
      "modified": "2050-01-01 23:59:59",
      "name": "Vydaná objednávka",
      "period_type": "yearly",
      "sequence": "1",
      "sequence_formatted": "VOBJ2020001",
      "user_profile_id": "1"
    }
  ]
}
```

| name                   | type   | description | default value |
| ---------------------- | ------ | ----------- | ------------- |
| **created**            | date   | creation date | |
| **default**            | bool   | is sequence default for document type? | | 
| **id**                 | int    | sequence ID | |
| **item_type**          | string | document type (invoice, proforma, reverse order, ...) | |
| **mask**               | string | mask (e.g. `YYYYNNN`) | |
| **modified**           | date   | modification date | |
| **name**               | string | sequence name | |
| **period_type**        | string | period type (yearly / monthly / daily) | |
| **sequence**           | string | not formatted next sequence number of document | |
| **sequence_formatted** | string | formatted sequence number according to document type mask | |
| **user_profile_id**    | int    | user profile ID | | 


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Tags

See [Tags > Get list of tags](tags.md#get-list-of-tags).


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


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


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Time filters

| value         | description    |
| ------------- | -------------- |
| **today**     | today          |
| **yesterday** | yesterday      |
| **thismonth** | this month     |
| **thisyear**  | this year      |
| **prevmonth** | previous month |
| **prevyear**  | previous year  |
