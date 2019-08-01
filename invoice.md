# Invoice

- [Delete invoice item](#delete-invoice-item)
- [Get invoice detail](#get-invoice-details)
- [Add invoice](#add-invoice)
- [Edit invoice](#edit-invoice)
- [Get list of invoices](#get-list-of-invoices)
- [Pay invoice](#pay-invoice)
- [Set invoice language](#set-invoice-language)
- [Mark invoice as sent via email](#mark-invoice-as-sent-via-email)
- [Delete invoice payment](#delete-invoice-payment)
- [Delete invoice](#delete-invoice)
- [Get invoice details](#get-invoice-details)
- [Get invoice PDF](#get-invoice-pdf)
- [Send invoice via e-mail](#send-invoice-via-mail)
- [Send invoice via post](#send-invoice-via-post)
- [Set invoice as "will not be paid"](#set-invoice-as-will-not-be-paid)
- [Mark invoice as sent](#mark-invoice-as-sent)

## Delete invoice item

### Request
**URL**: `/invoice_items/delete/{ITEM_ID}/invoice_id:{INVOICE_ID}`  
**HTTP method**: GET  

```
curl -X GET \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
    https://moja.superfaktura.sk/invoice_items/delete/1707/invoice_id:1285
```


### Attributes
#### Required

URL parameters:

| name            | type         | description                                                           | default value |
| --------------- | ------------ | --------------------------------------------------------------------- | ------------- |
| **item_id**     | int / string | invoice item ID, if used as string, use comma to separate various IDs |               |
| **invoice_id**  | int          | invoice ID                                                            |               |

#### Optional
none

### Response

#### Successful deletion
```json
{
   "error" : 0,
   "data" : {
      "InvoiceItem" : [],
      "Invoice" : {
         "amount" : "0.00",
         "amount_paid" : "0.00",
         "client_data" : "{\"Client\":{\"id\":\"431\",\"name\":\"2day, s. r. o.\",\"address\":\"Pri Suchom mlyne 6\",\"ico\":\"44981082\",\"email\":\"\",\"zip\":\"811 04\",\"dic\":\"2022903949\",\"phone\":\"\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"ic_dph\":\"\",\"fax\":\"\",\"country_id\":\"191\",\"state\":\"\",\"delivery_name\":\"\",\"delivery_zip\":\"\",\"delivery_city\":\"\",\"delivery_address\":\"\",\"delivery_phone\":\"\",\"delivery_country_id\":\"191\",\"delivery_state\":\"\",\"updateClient\":\"0\",\"country\":\"Slovensko\",\"delivery_country\":\"Slovensko\"}}",
         "client_id" : "431",
         "comment" : "",
         "constant" : "",
         "country_exchange_rate" : "1.00000000",
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
         "items_data" : "",
         "items_name" : null,
         "lang" : "slo",
         "mask" : "YYYYNNN",
         "modified" : "2019-01-30 12:58:58",
         "my_data" : "{\"MyData\":{\"id\":\"393\",\"user_id\":\"384\",\"user_profile_id\":\"\",\"country_id\":\"191\",\"company_name\":\"superfaktura.sk, s.r.o.\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"tax_payer\":\"1\",\"logo_key\":\"\",\"logo_id\":\"\",\"web\":\"\",\"Logo\":\"[{\\\"id\\\":\\\"168\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"393\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"9997f862be767814ce9b_393_screen_shot_2018_10_03_at_10_03_19.png\\\",\\\"checksum\\\":\\\"dd3300a5a4fc754b0f1361baa2ac2e3f\\\",\\\"group\\\":\\\"logo\\\",\\\"default\\\":\\\"1\\\",\\\"alternative\\\":null,\\\"created\\\":\\\"2019-01-23 08:37:27\\\",\\\"modified\\\":\\\"2019-01-23 08:39:56\\\"}]\",\"Signature\":\"{\\\"id\\\":\\\"169\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"393\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"51ee3f8bbd61561eb5f0_393_podpis_1.png\\\",\\\"checksum\\\":\\\"33b5238616646ca28ebabc02f713a59f\\\",\\\"group\\\":\\\"signature\\\",\\\"default\\\":\\\"0\\\",\\\"alternative\\\":null,\\\"created\\\":\\\"2019-01-23 08:37:27\\\",\\\"modified\\\":\\\"2019-01-23 08:37:27\\\"}\",\"travel_agencies\":\"0\",\"business_register\":\"Bratislava I, odd. Sro, vl.\\u010d.81403\\/B\",\"BankAccount\":[{\"show_account\":\"1\",\"id\":\"264\",\"default\":\"0\",\"country_id\":\"191\",\"bank_name\":\"FatraBanka\",\"bank_code\":\"\",\"account\":\"\",\"iban\":\" SK 31 1200 000019 8742637541\",\"swift\":\"9876\"},{\"show_account\":\"1\",\"id\":\"265\",\"default\":\"\",\"country_id\":\"191\",\"bank_name\":\"SuperBanka\",\"bank_code\":\"1200\",\"account\":\"8742637541\",\"iban\":\"\",\"swift\":\"\"}],\"update_profile\":\"0\",\"country\":\"Slovensko\"}}",
         "name" : "Faktúra 2019003",
         "order_no" : "",
         "paid" : "0.00",
         "parent_id" : null,
         "paydate" : null,
         "payment_type" : "",
         "proforma_id" : null,
         "recurring" : null,
         "rounding" : "item",
         "sequence_id" : "2815",
         "special_vat_scheme" : null,
         "specific" : "",
         "status" : "1",
         "summary_invoice" : null,
         "tags" : "",
         "tax_document" : "0",
         "taxdate" : "2019-01-30",
         "token" : "aa582995",
         "type" : "regular",
         "user_id" : "384",
         "user_profile_id" : "393",
         "variable" : "2019003",
         "vat" : "0.00",
         "vat_transfer" : "0"
      }
   },
   "error_message" : ""
}
```


#### Error while deleting

E.g. trying to delete already deleted item.

```json
{
   "error" : 1,
   "message" : "Chyba pri mazaní položky"
}
```


#### Invalid request
```json
{
   "error" : 3,
   "error_message" : "Bad data format."
}
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


## Get invoice detail

Get invoice details.

### Request
**URL**: `/invoices/view/{INVOICE_ID}.json`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoices/view/1285.json
```

### Attributes
#### Required
URL parameters:

| name           | type | description | default value |
| -------------- | ---- | ----------- | ------------- |
| **invoice_id** | int  | invoice ID  |               |

#### Optional
none

### Response

#### Success
```json
{
   "Summary" : {
      "discount" : 0,
      "vat_base_separate" : {
         "20" : 30.95
      },
      "vat_base_total" : 30.95,
      "invoice_total" : 37.14,
      "vat_separate" : {
         "20" : 6.19
      },
      "vat_total" : 6.19
   },
   "PaymentLink" : null,
   "Invoice" : {
      "amount" : "30.95",
      "amount_paid" : "24.00",
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
      "exchange_rate" : 1,
      "flag" : "partially-paid",
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
      "modified" : "2019-02-06 11:43:28",
      "my_data" : "{\"MyData\":{\"id\":\"393\",\"user_id\":\"384\",\"user_profile_id\":\"\",\"country_id\":\"191\",\"company_name\":\"superfaktura.sk, s.r.o.\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"tax_payer\":\"1\",\"logo_key\":\"\",\"logo_id\":\"\",\"web\":\"\",\"Logo\":\"[{\\\"id\\\":\\\"168\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"393\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"9997f862be767814ce9b_393_screen_shot_2018_10_03_at_10_03_19.png\\\",\\\"checksum\\\":\\\"dd3300a5a4fc754b0f1361baa2ac2e3f\\\",\\\"group\\\":\\\"logo\\\",\\\"default\\\":\\\"1\\\",\\\"alternative\\\":null,\\\"created\\\":\\\"2019-01-23 08:37:27\\\",\\\"modified\\\":\\\"2019-01-23 08:39:56\\\"}]\",\"Signature\":\"{\\\"id\\\":\\\"169\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"393\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"51ee3f8bbd61561eb5f0_393_podpis_1.png\\\",\\\"checksum\\\":\\\"33b5238616646ca28ebabc02f713a59f\\\",\\\"group\\\":\\\"signature\\\",\\\"default\\\":\\\"0\\\",\\\"alternative\\\":null,\\\"created\\\":\\\"2019-01-23 08:37:27\\\",\\\"modified\\\":\\\"2019-01-23 08:37:27\\\"}\",\"travel_agencies\":\"0\",\"business_register\":\"Bratislava I, odd. Sro, vl.\\u010d.81403\\/B\",\"BankAccount\":[{\"show_account\":\"1\",\"id\":\"264\",\"default\":\"0\",\"country_id\":\"191\",\"bank_name\":\"FatraBanka\",\"bank_code\":\"\",\"account\":\"\",\"iban\":\" SK 31 1200 000019 8742637541\",\"swift\":\"9876\"},{\"show_account\":\"1\",\"id\":\"265\",\"default\":\"\",\"country_id\":\"191\",\"bank_name\":\"SuperBanka\",\"bank_code\":\"1200\",\"account\":\"8742637541\",\"iban\":\"\",\"swift\":\"\"}],\"update_profile\":\"0\",\"country\":\"Slovensko\"}}",
      "name" : "Faktúra 2019003",
      "order_no" : "",
      "paid" : "24.00",
      "parent_id" : null,
      "paydate" : "2019-02-06 12:05:50",
      "payment_type" : "cash",
      "proforma_id" : null,
      "recurring" : null,
      "rounding" : "item",
      "sequence_id" : "2815",
      "show_items_with_dph" : true,
      "show_special_vat" : false,
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
   "InvoiceItem" : [
      {
         "description" : "",
         "discount" : 0,
         "discount_description" : "Zľava",
         "discount_no_vat" : 0,
         "discount_no_vat_total" : 0,
         "discount_with_vat" : 0,
         "discount_with_vat_total" : 0,
         "hide_in_autocomplete" : null,
         "id" : "1708",
         "invoice_id" : "1285",
         "item_price" : 11,
         "item_price_no_discount" : 11,
         "item_price_vat" : 13.2,
         "item_price_vat_check" : 13.2,
         "item_price_vat_no_discount" : 13.2,
         "name" : "asdf",
         "ordernum" : "0",
         "quantity" : null,
         "sku" : null,
         "stock_item_id" : "0",
         "tax" : "20",
         "tax_deposit" : "0",
         "unit" : "",
         "unit_price" : 11,
         "unit_price_discount" : 11,
         "unit_price_vat" : 13.2,
         "unit_price_vat_no_discount" : 13.2,
         "user_id" : "384",
         "user_profile_id" : "393"
      },
      {
         "description" : "SKU: itemb1241\r\nPublic description of this item",
         "discount" : 0,
         "discount_description" : "Zľava",
         "discount_no_vat" : 0,
         "discount_no_vat_total" : 0,
         "discount_with_vat" : 0,
         "discount_with_vat_total" : 0,
         "hide_in_autocomplete" : "1",
         "id" : "1710",
         "invoice_id" : "1285",
         "item_price" : 19.95,
         "item_price_no_discount" : 19.95,
         "item_price_vat" : 23.94,
         "item_price_vat_check" : 23.94,
         "item_price_vat_no_discount" : 23.94,
         "name" : "Item B",
         "ordernum" : "1",
         "quantity" : null,
         "sku" : "itemb1241",
         "stock_item_id" : "19",
         "tax" : "20",
         "tax_deposit" : "0",
         "unit" : "kg",
         "unit_price" : 19.95,
         "unit_price_discount" : 19.95,
         "unit_price_vat" : 23.94,
         "unit_price_vat_no_discount" : 23.94,
         "user_id" : "384",
         "user_profile_id" : "393"
      }
   ],
   "SummaryInvoice" : {
      "vat_separate_positive" : {
         "20" : 6.19
      },
      "vat_base_separate_negative" : {
         "20" : 0
      },
      "vat_base_separate_positive" : {
         "20" : 30.95
      },
      "vat_separate_negative" : {
         "20" : 0
      }
   },
   "Tag" : [],
   "0" : {
      "sent_by" : "regular,regular,regular,regular,regular,regular,regular,regular",
      "sent_to_email" : "name.surname@superfaktura.sk,name.surname@superfaktura.sk,name.surname@superfaktura.sk,name.surname@superfaktura.sk,name.surname@superfaktura.sk,name.surname@superfaktura.sk,name.surname@superfaktura.sk,name.surname@superfaktura.sk",
      "sent_to_email_cc" : "[],[],[],[],[],[],[],[]",
      "to_pay" : "13.140000",
      "total" : "37.14"
   },
   "Client" : {
      "address" : "Pri Suchom mlyne 6",
      "city" : "Bratislava - mestská časť Staré Mesto",
      "country" : "Slovensko",
      "country_id" : "191",
      "delivery_address" : "",
      "delivery_city" : "",
      "delivery_country" : "Slovensko",
      "delivery_country_id" : "191",
      "delivery_name" : "",
      "delivery_phone" : "",
      "delivery_state" : "",
      "delivery_zip" : "",
      "dic" : "2022903949",
      "email" : "",
      "fax" : "",
      "ic_dph" : "",
      "ico" : "44981082",
      "id" : "431",
      "name" : "2day, s. r. o.",
      "phone" : "",
      "state" : "",
      "updateClient" : "0",
      "zip" : "811 04",
      "Country" : {
         "eu" : "1",
         "id" : "191",
         "iso" : "sk",
         "name" : "Slovensko"
      },
      "DeliveryCountry" : {
         "eu" : "1",
         "id" : "191",
         "iso" : "sk",
         "name" : "Slovensko"
      }
   },
   "Paypal" : false,
   "InvoiceEmail" : [
      {
         "created" : "2019-02-04 10:01:09",
         "due" : null,
         "email" : "name.surname@superfaktura.sk",
         "email_cc" : "[]",
         "id" : "134",
         "invoice_id" : "1285",
         "message" : "Dobrý deň,\n\nv prílohe posielame faktúru č. 2019003.\n\nSuma na úhradu: 37,14 €\nVariabilný symbol: 2019003\nČíslo účtu:  SK 31 1200 000019 8742637541\n\nĎakujeme za úhradu a prajeme príjemný deň.",
         "phone" : null,
         "subject" : "Faktúra 2019003",
         "type" : "regular",
         "user_id" : "384",
         "user_profile_id" : "393"
      }
   ],
   "UnitCount" : {
      "kg" : 0
   },
   "InvoiceSetting" : {
      "bysquare" : "1",
      "force_iban" : true,
      "language" : "deu",
      "online_payment" : null,
      "payment_info" : true,
      "paypal" : false,
      "show_prices" : false,
      "show_summary" : true,
      "signature" : true
   },
   "PostStamp" : [
      {
         "bysquare" : "1",
         "created" : "2019-02-04 11:28:17",
         "external_response" : null,
         "external_service" : null,
         "external_service_id" : null,
         "external_status" : null,
         "id" : "1016",
         "invoice_id" : "1285",
         "invoice_language" : "slo",
         "modified" : "2019-02-04 11:56:47",
         "no_signature" : "0",
         "payment_info" : "1",
         "post_stamp_package_id" : "7",
         "recycled" : "0",
         "requested" : "2019-02-04 11:56:47",
         "sent" : "0000-00-00 00:00:00",
         "sent_to" : "{\"name\":\"Mr. Incognito\",\"address\":\"Pri Vlhkom mlyne 6\",\"city\":\"Bratislava\",\"zip\":\"811 04\",\"country\":\"Slovensko\"}",
         "status" : "waiting",
         "user_id" : "384",
         "user_profile_id" : "393"
      }
   ],
   "InvoicePayment" : [
      {
         "amount" : "5.81",
         "created" : "2019-02-06 12:05:50",
         "document_no" : "",
         "exchange_rate" : "1.00000000000000",
         "home_currency" : "CZK",
         "id" : "211",
         "import_payment_id" : null,
         "invoice_id" : "1285",
         "payment_currency" : "EUR",
         "payment_type" : "cash",
         "user_id" : "384",
         "user_profile_id" : "393",
         "vat" : "6.19"
      }
   ],
   "MyData" : {
      "zip" : "811 04",
      "address" : "Pri Suchom mlyne 6",
      "user_profile_id" : "",
      "LogoRaw" : [
         {
            "alternative" : null,
            "basename" : "9997f862be767814ce9b_393_screen_shot_2018_10_03_at_10_03_19.png",
            "checksum" : "dd3300a5a4fc754b0f1361baa2ac2e3f",
            "created" : "2019-01-23 08:37:27",
            "default" : "1",
            "dirname" : "img",
            "foreign_key" : "393",
            "group" : "logo",
            "id" : "168",
            "model" : "User",
            "modified" : "2019-01-23 08:39:56"
         }
      ],
      "SignatureRaw" : {
         "alternative" : null,
         "basename" : "51ee3f8bbd61561eb5f0_393_podpis_1.png",
         "checksum" : "33b5238616646ca28ebabc02f713a59f",
         "created" : "2019-01-23 08:37:27",
         "default" : "0",
         "dirname" : "img",
         "foreign_key" : "393",
         "group" : "signature",
         "id" : "169",
         "model" : "User",
         "modified" : "2019-01-23 08:37:27"
      },
      "business_register" : "Bratislava I, odd. Sro, vl.č.81403/B",
      "city" : "Bratislava - mestská časť Staré Mesto",
      "dic" : "2023513470",
      "ic_dph" : "SK2023513470",
      "ico" : "46655034",
      "id" : "393",
      "Logo" : "[{\"id\":\"168\",\"model\":\"User\",\"foreign_key\":\"393\",\"dirname\":\"img\",\"basename\":\"9997f862be767814ce9b_393_screen_shot_2018_10_03_at_10_03_19.png\",\"checksum\":\"dd3300a5a4fc754b0f1361baa2ac2e3f\",\"group\":\"logo\",\"default\":\"1\",\"alternative\":null,\"created\":\"2019-01-23 08:37:27\",\"modified\":\"2019-01-23 08:39:56\"}]",
      "logo_id" : "",
      "logo_key" : "",
      "Signature" : "{\"id\":\"169\",\"model\":\"User\",\"foreign_key\":\"393\",\"dirname\":\"img\",\"basename\":\"51ee3f8bbd61561eb5f0_393_podpis_1.png\",\"checksum\":\"33b5238616646ca28ebabc02f713a59f\",\"group\":\"signature\",\"default\":\"0\",\"alternative\":null,\"created\":\"2019-01-23 08:37:27\",\"modified\":\"2019-01-23 08:37:27\"}",
      "tax_payer" : "1",
      "travel_agencies" : "0",
      "update_profile" : "0",
      "user_id" : "384",
      "web" : "",
      "BankAccount" : [
         {
            "account" : "",
            "bank_code" : "",
            "bank_name" : "FatraBanka",
            "country_id" : "191",
            "default" : "0",
            "iban" : " SK 31 1200 000019 8742637541",
            "id" : "264",
            "show_account" : "1",
            "swift" : "9876"
         },
         {
            "account" : "8742637541",
            "bank_code" : "1200",
            "bank_name" : "SuperBanka",
            "country_id" : "191",
            "default" : "",
            "iban" : "",
            "id" : "265",
            "show_account" : "1",
            "swift" : ""
         }
      ],
      "country" : {
         "eu" : "1",
         "id" : "191",
         "iso" : "sk",
         "name" : "Slovensko"
      },
      "company_name" : "superfaktura.sk, s.r.o.",
      "country_id" : "191"
   },
   "ClientData" : {
      "address" : "Pri Suchom mlyne 6",
      "city" : "Bratislava - mestská časť Staré Mesto",
      "country" : "Slovensko",
      "country_id" : "191",
      "delivery_address" : "",
      "delivery_city" : "",
      "delivery_country" : "Slovensko",
      "delivery_country_id" : "191",
      "delivery_name" : "",
      "delivery_phone" : "",
      "delivery_state" : "",
      "delivery_zip" : "",
      "dic" : "2022903949",
      "email" : "",
      "fax" : "",
      "ic_dph" : "",
      "ico" : "44981082",
      "id" : "431",
      "name" : "2day, s. r. o.",
      "phone" : "",
      "state" : "",
      "updateClient" : "0",
      "zip" : "811 04",
      "Country" : {
         "name" : "Slovensko",
         "iso" : "sk",
         "id" : "191",
         "eu" : "1"
      },
      "DeliveryCountry" : {
         "id" : "191",
         "eu" : "1",
         "name" : "Slovensko",
         "iso" : "sk"
      }
   }
}
```

#### Wrong invoice

```json
{
   "message" : "Invoice not found",
   "error" : 1,
   "error_message" : "Invoice not found"
}
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Add invoice

Create new invoice.
If you want to add tags to invoice, refer to [FAQ > How do I add tags to an entity?](faq.md#how-do-i-add-tags-to-an-entity).

### Request

**URL**: `/invoices/create`  
**HTTP method**: POST  

```sh

# minimal example
data='{
    "Invoice":{
        "name": "Test API"
    },
    "InvoiceItem":[
        {
            "description": "description of item 1",
            "name": "item 1",
            "tax": 20,
            "unit_price": 10
        }
    ],
    "Client":{
        "ico": "44981082"
    }
}';

# more complicate example
data='{
    "Invoice":{
        "name": "Test API",
        "bank_accounts": [
            {
                "bank_name": "New Bank",
                "iban": "SK0000000000000000",
                "swift": "12345"
            }
        ],
        "issued_by": "John Doe",
        "issued_by_email": "john@d.oe",
        "issued_by_phone": "+9999999",
        "issued_by_web": "https://superfaktura.sk",
        "created": "2019-01-01",
        "discount": 10,
        "header_comment": "Header comment",
        "internal_comment": "Internal comment",
        "invoice_currency": "NOK",
        "rounding": "item_ext",
        "specific": "SS123456",
        "type": "delivery",
        "variable": "VS87654"
    },
    "InvoiceItem":[
        {
            "description": "description of item 1",
            "name": "item 1",
            "tax": 20,
            "unit_price": 10
        }
    ],
    "Client":{
        "ico": "44981082",
        "comment": "Client comment",
        "update_addressbook": 1,
        "iban": "XX00000000001",
        "swift": "98765"
    }
}';


curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoices/create
```



Example with invoice data, invoice items, client, invoice extras, accounting details and invoice settings (full options specified):
```
data='{
    "Invoice":{
        "name": "Test API",
        "bank_accounts": [
            {
                "bank_name": "New Bank",
                "iban": "SK0000000000000000",
                "swift": "12345"
            }
        ],
        "issued_by": "John Doe",
        "issued_by_email": "john@d.oe",
        "issued_by_phone": "+9999999",
        "issued_by_web": "https://superfaktura.sk",
        "created": "2019-01-01",
        "discount": 10,
        "header_comment": "Header comment",
        "internal_comment": "Internal comment",
        "invoice_currency": "NOK",
        "rounding": "item_ext",
        "specific": "SS123456",
        "type": "delivery",
        "variable": "VS87654",
        "created": "2019-02-28"
    },
    "InvoiceItem":[
        {
            "description": "description of item 1",
            "name": "item 1",
            "tax": 20,
            "unit_price": 10,
            "AccountingDetail": { 
                "place": "Slovakia",
                "order": "PLA", 
                "operation": "UXW", 
                "type": "item",
                "analytics_account": "311", 
                "synthetic_account": "000",
                "preconfidence": "5ZV"
            }
        }
    ],
    "Client":{
        "ico": "44981082",
        "comment": "Client comment",
        "update_addressbook": 1,
        "iban": "XX00000000001",
        "swift": "98765"
    },
    "InvoiceSetting": {
        "settings": "{\"language\":\"eng\",\"signature\":true,\"payment_info\":true,\"online_payment\": true,\"bysquare\": true,\"paypal\": true}"
    },
    "InvoiceExtra": {
        "pickup_point_id": 23
    },
    "MyData": {
        "address": "Fiktivna 1",
        "business_register": "-",
        "city": "Prague",
        "company_name": "MyData Inc.",
        "country_id": "123",
        "dic": "SK99999999",
        "ic_dph": "ABCDE",
        "update_profile": "0",
        "zip": "999 88"
    }
}';
```

### Attributes
#### Required

##### Client

| name      | type   | description  | default value |
| --------- | ------ | ------------ | ------------- |
| **name**  | string | client name  |               |

##### Invoice

none


##### InvoiceItem
At least one of `unit_price` and `name` must be filled and not empty.
At least one Invoice item must be specified.


#### Optional

##### Client

| name                        | type   | description  | default value |
| --------------------------- | ------ | ------------ | ------------- |
| **address**                 | string | address (street + number) | |
| **bank_account**            | string | bank account | |
| **city**                    | string | city | |
| **comment**                 | string | comment | |
| **country**                 | string | custom country name | |
| **country_id**              | int    | country ID (see [Value lists > Country list](value-lists.md#country-list)) | |
| **country_iso_id**          | string | country code ([ISO-3166-1 (Alpha-2)](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)) | |
| **delivery_address**        | string | delivery address (street + number) | |
| **delivery_city**           | string | delivery city | |
| **delivery_country**        | string | custom delivery country name | |
| **delivery_country_id**     | int    | delivery country ID (see [Value lists > Country list](value-lists.md#country-list)) | |
| **delivery_country_iso_id** | string | country code ([ISO-3166-1 (Alpha-2)](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)) | |
| **delivery_name**           | string | delivery country name | |
| **delivery_phone**          | string | delivery phone number | |
| **delivery_zip**            | string | delivery ZIP code | |
| **dic**                     | string | Tax ID (DIČ) | |
| **email**                   | string | email | |
| **fax**                     | string | fax | |
| **iban**                    | string | IBAN | |
| **ic_dph**                  | string | VAT ID (IČ DPH) | |
| **ico**                     | string | ID (IČO) | |
| **match_address**           | int    | if this parameter is set, address is included in client searching | |
| **phone**                   | string | phone number | |
| **swift**                   | string | SWIFT code | |
| **update_addressbook**      | int    | update client data when invoice is issued? (0=no, 1=true) | |
| **zip**                     | string | ZIP code | |


In case of foreign client it is necessary to correctly fill `country_id`.
If `country_id` is empty, predefined value is used (SK version - Slovakia, CZ version - Czech republic).
To get `country_id` see [Value lists > Country list](value-lists.md#country-list).


##### Invoice

| name                     | type     | description  | default value |
| ------------------------ | -------- | ------------ | ------------- |
| **already_paid**         | int      | is invoice already paid (0=no, 1=yes) | |
| **bank_accounts**        | array    | list of bank accounts | |
| **comment**              | string   | comment | |
| **constant**             | string   | constant symbol | |
| **created**              | date     | issue date | |
| **delivery**             | date     | delivery date | |
| **delivery_type**        | string   | delivery type (see [Value lists > Delivery types](value-lists.md#delivery-types)) | |
| **deposit**              | float    | deposit paid | |
| **discount**             | float    | discount in percent | 0 |
| **discount_total**       | float    | nominal discount, is used only if `discount` is *not* set | |
| **due**                  | date     | due date | |
| **estimate_id**          | int      | estimate ID, based on which is invoice issued | |
| **header_comment**       | string   | comment above invoice items | |
| **internal_comment**     | string   | internal comment - will not be displayed on invoice | |
| **invoice_currency**     | string   | currency (see [Value lists > Currencies](value-lists.md#currencies)) | |
| **invoice_no_formatted** | string   | invoice number | |
| **issued_by**            | string   | who issued invoice (person)| |
| **issued_by_email**      | string   | who issued invoice (email) | |
| **issued_by_phone**      | string   | who issued invoice (phone) | |
| **issued_by_web**        | string   | website displayed on invoice | |
| **logo_id**              | int      | logo ID | |
| **order_no**             | string   | order number | |
| **name**                 | string   | invoice name | |
| **parent_id**            | int      | invoice ID, that we want to cancel | |
| **paydate**              | datetime | payment date (if set together with `already_paid=1`, the set date will be used) | |
| **payment_type**         | string   | payment type (see [Value lists > Payment types](value-lists.md#payment-types))| |
| **proforma_id**          | string   | proforma invoice ID, based on which regular invoice is issued. Invoice will get information about paid invoice | |
| **rounding**             | string   | rounding type (see [Value lists > Rounding types](value-lists.md#rounding-types)) | |
| **sequence_id**          | int      | sequence ID (see [Value lists > Sequences](value-lists.md#sequences)) | |
| **specific**             | string   | specific symbol | |
| **tax_document**         | int      | is there a receipt? (for correct connection with proforma invoice is necessary to fill `proforma_id`) (0=no, 1=yes) | |
| **type**                 | string   | invoice type (see [Value lists > Invoice types](value-lists.md#invoice-types)) | |
| **variable**             | string   | variable symbol (if left empty, invoice number will be used) | |


##### InvoiceItem

| name                     | type   | description  | default value |
| ------------------------ | ------ | ------------ | ------------- |
| **description**          | string | invoice item description - will be displayed on invoice | |
| **discount**             | float  | discount in percent | 0 |
| **discount_description** | string | discount description | |
| **load_data_from_stock** | int    | load data from stock? (0=no, 1=yes) | 0 |
| **name**                 | string | item name | |
| **quantity**             | float  | quantity | 1 |
| **sku**                  | string | stock number | |
| **stock_item_id**        | int    | 123 | |
| **tax**                  | float  | VAT (if you are not a tax payer, use 0) | |
| **unit**                 | string | unit (e.g. m, l, hour) | |
| **unit_price**           | float  | price without VAT (or full price, if you are not a tax payer) | 0 |


###### Accounting Detail

| name                  | type   | description                                     | default value |
| --------------------- | ------ | ----------------------------------------------- | ------------- |
| **analytics_account** | string | analytics account                               |               |
| **operation**         | string | operation                                       |               |
| **order**             | string | order name                                      |               |
| **place**             | string | place name                                      |               |
| **preconfidence**     | string | preconfidence                                   |               |
| **synthetic_account** | string | synthetic account                               |               |
| **type**              | string | item type (`item` (goods), `service` (service)) |               |



##### MyData

| name                     | type   | description                               | default value |
| ------------------------ | ------ | ----------------------------------------- | ------------- |
| **address**              | string | my address                                | |
| **business_register**    | string | business register                         | |
| **city**                 | string | my city                                   | |
| **company_name**         | string | my company name                           | |
| **country_id**           | string | country ID (see [Value lists > Country list](value-lists.md#country-list)) | |
| **dic**                  | string | tax ID (DIČ)                              | |
| **ic_dph**               | string | VAT ID (IČ DPH)                           | |
| **update_profile**       | int    | should profile be updated with these data | |
| **zip**                  | string | ZIP code                                  | |



##### Invoice Settings

| name               | type   | description                               | default value |
| ------------------ | ------ | ----------------------------------------- | ------------- |
| **bysquare**       | bool   | show pay by square                        |               |
| **language**       | string | invoice language  (for list of possible values see [Value lists > Language list](value-lists.md#language-list)) |               |
| **online_payment** | bool   | show online payments                      |               |
| **payment_info**   | bool   | show payment information                  |               |
| **paypal**         | bool   | show PayPal                               |               |
| **show_prices**    | bool   | show prices (only effective for delivery) |               |
| **signature**      | bool   | show signature                            |               |


##### Invoice Extras

| name                | type   | description                               | default value |
| ------------------- | ------ | ----------------------------------------- | ------------- |
| **pickup_point_id** | int    | pickup point ID for Zásielkovňa           |               |


### Response

#### Successful addition
```json
{
   "error_message" : "Invoice created",
   "error" : 0,
   "data" : {
      "SummaryInvoice" : {
         "vat_separate_positive" : {
            "20" : 1.8
         },
         "vat_base_separate_negative" : {
            "20" : 0
         },
         "vat_separate_negative" : {
            "20" : 0
         },
         "vat_base_separate_positive" : {
            "20" : 9
         }
      },
      "PaymentLink" : "",
      "InvoiceSetting" : {
         "bysquare" : "1",
         "language" : "slo",
         "online_payment" : false,
         "payment_info" : true,
         "signature" : true
      },
      "Tag" : [],
      "PostStamp" : [],
      "Signature" : {
         "alternative" : null,
         "basename" : "51ee3f8bbd61561eb5f0_393_podpis_1.png",
         "checksum" : "33b5238616646ca28ebabc02f713a59f",
         "created" : "2019-01-23 08:37:27",
         "default" : "0",
         "dirname" : "img",
         "foreign_key" : "393",
         "group" : "signature",
         "id" : "169",
         "model" : "User",
         "modified" : "2019-01-23 08:37:27"
      },
      "Invoice" : {
         "amount" : "9.00",
         "amount_paid" : "0.00",
         "client_data" : "{\"Client\":{\"id\":\"431\",\"user_id\":\"384\",\"user_profile_id\":\"393\",\"uuid\":\"NULL\",\"country_id\":\"191\",\"name\":\"2day, s. r. o.\",\"ico\":\"44981082\",\"dic\":\"2022903949\",\"ic_dph\":\"\",\"iban\":\"XX00000000001\",\"swift\":\"98765\",\"bank_account_prefix\":\"\",\"bank_account\":\"\",\"bank_code\":\"\",\"email\":\"name.surname@superfaktura.sk\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"state\":\"\",\"country\":null,\"delivery_name\":\"\",\"delivery_address\":\"\",\"delivery_city\":\"\",\"delivery_zip\":\"\",\"delivery_state\":\"\",\"delivery_country\":null,\"delivery_country_id\":\"191\",\"phone\":\"\",\"delivery_phone\":\"\",\"fax\":\"\",\"due_date\":null,\"default_variable\":\"\",\"discount\":null,\"currency\":null,\"bank_account_id\":\"0\",\"comment\":\"Client comment\",\"tags\":null,\"distance\":null,\"dont_travel\":\"0\",\"created\":\"2019-01-23 08:41:37\",\"modified\":\"2019-02-12 11:51:47\",\"update\":\"2\",\"notices\":\"1\"}}",
         "client_id" : "431",
         "comment" : null,
         "constant" : "",
         "country_exchange_rate" : "9.94830036",
         "created" : "2019-01-01 00:00:00",
         "delivery" : null,
         "delivery_type" : "",
         "demo" : "0",
         "deposit" : "0.00",
         "discount" : "10",
         "due" : "2019-01-15",
         "estimate_id" : null,
         "exchange_rate" : 9.9483,
         "flag" : false,
         "header_comment" : "Header comment",
         "home_currency" : "EUR",
         "id" : "1294",
         "import_id" : null,
         "import_parent_id" : null,
         "import_type" : null,
         "internal_comment" : "Internal comment",
         "invoice_currency" : "NOK",
         "invoice_no" : "1",
         "invoice_no_formatted" : "DOD2019001",
         "issued_by" : "John Doe",
         "issued_by_email" : "john@d.oe",
         "issued_by_phone" : " 9999999",
         "issued_by_web" : "https://superfaktura.sk",
         "items_data" : "item 1 description of item 1, ",
         "items_name" : null,
         "lang" : null,
         "mask" : "YYYYNNN",
         "modified" : "2019-02-12 11:51:48",
         "my_data" : "{\"MyData\":{\"id\":\"393\",\"user_id\":\"384\",\"country_id\":\"191\",\"company_name\":\"superfaktura.sk, s.r.o.\",\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"tax_payer\":\"1\",\"BankAccount\":[{\"bank_name\":\"New Bank\",\"iban\":\"SK0000000000000000\",\"swift\":\"12345\",\"show_account\":true,\"country_id\":\"\",\"account\":\"\",\"bank_code\":\"\"}],\"Logo\":[{\"id\":\"168\",\"model\":\"User\",\"foreign_key\":\"393\",\"dirname\":\"img\",\"basename\":\"9997f862be767814ce9b_393_screen_shot_2018_10_03_at_10_03_19.png\",\"checksum\":\"dd3300a5a4fc754b0f1361baa2ac2e3f\",\"group\":\"logo\",\"default\":\"1\",\"alternative\":null,\"created\":\"2019-01-23 08:37:27\",\"modified\":\"2019-01-23 08:39:56\"}],\"Signature\":{\"id\":\"169\",\"model\":\"User\",\"foreign_key\":\"393\",\"dirname\":\"img\",\"basename\":\"51ee3f8bbd61561eb5f0_393_podpis_1.png\",\"checksum\":\"33b5238616646ca28ebabc02f713a59f\",\"group\":\"signature\",\"default\":\"0\",\"alternative\":null,\"created\":\"2019-01-23 08:37:27\",\"modified\":\"2019-01-23 08:37:27\"}}}",
         "name" : "Test API",
         "order_no" : null,
         "paid" : "0.00",
         "parent_id" : null,
         "paydate" : null,
         "payment_type" : null,
         "proforma_id" : null,
         "recurring" : null,
         "rounding" : "item_ext",
         "sequence_id" : "2822",
         "show_items_with_dph" : true,
         "show_special_vat" : false,
         "special_vat_scheme" : null,
         "specific" : "SS123456",
         "status" : "1",
         "summary_invoice" : "0",
         "tags" : null,
         "tax_document" : null,
         "taxdate" : "2019-01-01",
         "token" : "6cbc8660",
         "type" : "delivery",
         "user_id" : "384",
         "user_profile_id" : "393",
         "variable" : "VS87654",
         "vat" : "1.80",
         "vat_transfer" : null
      },
      "Summary" : {
         "vat_base_total" : 9,
         "discount" : 1.2,
         "vat_base_separate" : {
            "20" : 9
         },
         "invoice_total" : 10.8,
         "vat_total" : 1.8,
         "vat_separate" : {
            "20" : 1.8
         }
      },
      "InvoiceItem" : [
         {
            "description" : "description of item 1",
            "discount" : 0,
            "discount_description" : "",
            "discount_no_vat" : 0,
            "discount_no_vat_total" : 0,
            "discount_with_vat" : 0,
            "discount_with_vat_total" : 0,
            "hide_in_autocomplete" : null,
            "id" : "1722",
            "invoice_id" : "1294",
            "item_price" : 10,
            "item_price_no_discount" : 10,
            "item_price_vat" : 12,
            "item_price_vat_no_discount" : 12,
            "name" : "item 1",
            "ordernum" : "0",
            "quantity" : null,
            "sku" : null,
            "stock_item_id" : null,
            "tax" : "20",
            "tax_deposit" : "0",
            "unit" : "",
            "unit_price" : 10,
            "unit_price_discount" : 10,
            "unit_price_vat" : 12,
            "unit_price_vat_no_discount" : 12,
            "user_id" : "384",
            "user_profile_id" : "393"
         }
      ],
      "InvoiceEmail" : [],
      "0" : {
         "to_pay" : "1.085613",
         "total" : "10.80"
      },
      "Paypal" : false,
      "Logo" : [
         {
            "alternative" : null,
            "basename" : "9997f862be767814ce9b_393_screen_shot_2018_10_03_at_10_03_19.png",
            "checksum" : "dd3300a5a4fc754b0f1361baa2ac2e3f",
            "created" : "2019-01-23 08:37:27",
            "default" : "1",
            "dirname" : "img",
            "foreign_key" : "393",
            "group" : "logo",
            "id" : "168",
            "model" : "User",
            "modified" : "2019-01-23 08:39:56"
         }
      ],
      "UnitCount" : [],
      "InvoicePayment" : [],
      "MyData" : {
         "company_name" : "superfaktura.sk, s.r.o.",
         "ico" : "46655034",
         "tax_payer" : "1",
         "user_id" : "384",
         "zip" : "811 04",
         "BankAccount" : [
            {
               "account" : "",
               "bank_code" : "",
               "bank_name" : "New Bank",
               "country_id" : "",
               "iban" : "SK0000000000000000",
               "show_account" : true,
               "swift" : "12345"
            }
         ],
         "id" : "393",
         "Logo" : "[{\"id\":\"168\",\"model\":\"User\",\"foreign_key\":\"393\",\"dirname\":\"img\",\"basename\":\"9997f862be767814ce9b_393_screen_shot_2018_10_03_at_10_03_19.png\",\"checksum\":\"dd3300a5a4fc754b0f1361baa2ac2e3f\",\"group\":\"logo\",\"default\":\"1\",\"alternative\":null,\"created\":\"2019-01-23 08:37:27\",\"modified\":\"2019-01-23 08:39:56\"}]",
         "country" : {
            "eu" : "1",
            "iso" : "sk",
            "name" : "Slovensko",
            "id" : "191"
         },
         "SignatureRaw" : {
            "alternative" : null,
            "basename" : "51ee3f8bbd61561eb5f0_393_podpis_1.png",
            "checksum" : "33b5238616646ca28ebabc02f713a59f",
            "created" : "2019-01-23 08:37:27",
            "default" : "0",
            "dirname" : "img",
            "foreign_key" : "393",
            "group" : "signature",
            "id" : "169",
            "model" : "User",
            "modified" : "2019-01-23 08:37:27"
         },
         "LogoRaw" : [
            {
               "alternative" : null,
               "basename" : "9997f862be767814ce9b_393_screen_shot_2018_10_03_at_10_03_19.png",
               "checksum" : "dd3300a5a4fc754b0f1361baa2ac2e3f",
               "created" : "2019-01-23 08:37:27",
               "default" : "1",
               "dirname" : "img",
               "foreign_key" : "393",
               "group" : "logo",
               "id" : "168",
               "model" : "User",
               "modified" : "2019-01-23 08:39:56"
            }
         ],
         "address" : "Pri Suchom mlyne 6",
         "city" : "Bratislava - mestská časť Staré Mesto",
         "country_id" : "191",
         "dic" : "2023513470",
         "ic_dph" : "SK2023513470",
         "Signature" : "{\"id\":\"169\",\"model\":\"User\",\"foreign_key\":\"393\",\"dirname\":\"img\",\"basename\":\"51ee3f8bbd61561eb5f0_393_podpis_1.png\",\"checksum\":\"33b5238616646ca28ebabc02f713a59f\",\"group\":\"signature\",\"default\":\"0\",\"alternative\":null,\"created\":\"2019-01-23 08:37:27\",\"modified\":\"2019-01-23 08:37:27\"}"
      },
      "ClientData" : {
         "Country" : {
            "name" : "Slovensko",
            "id" : "191",
            "eu" : "1",
            "iso" : "sk"
         },
         "address" : "Pri Suchom mlyne 6",
         "bank_account_id" : "0",
         "bank_account_prefix" : "",
         "bank_code" : "",
         "city" : "Bratislava - mestská časť Staré Mesto",
         "comment" : "Client comment",
         "country_id" : "191",
         "created" : "2019-01-23 08:41:37",
         "currency" : null,
         "delivery_address" : "",
         "delivery_city" : "",
         "delivery_name" : "",
         "delivery_phone" : "",
         "delivery_state" : "",
         "delivery_zip" : "",
         "dic" : "2022903949",
         "discount" : null,
         "due_date" : null,
         "fax" : "",
         "iban" : "XX00000000001",
         "ic_dph" : "",
         "id" : "431",
         "modified" : "2019-02-12 11:51:47",
         "name" : "2day, s. r. o.",
         "notices" : "1",
         "phone" : "",
         "state" : "",
         "swift" : "98765",
         "update" : "2",
         "user_profile_id" : "393",
         "uuid" : "NULL",
         "zip" : "811 04",
         "DeliveryCountry" : {
            "id" : "191",
            "name" : "Slovensko",
            "iso" : "sk",
            "eu" : "1"
         },
         "bank_account" : "",
         "country" : null,
         "default_variable" : "",
         "delivery_country" : null,
         "delivery_country_id" : "191",
         "distance" : null,
         "dont_travel" : "0",
         "email" : "name.surname@superfaktura.sk",
         "ico" : "44981082",
         "tags" : null,
         "user_id" : "384"
      },
      "Client" : {
         "address" : "Pri Suchom mlyne 6",
         "bank_account" : "",
         "bank_account_id" : "0",
         "bank_account_prefix" : "",
         "bank_code" : "",
         "city" : "Bratislava - mestská časť Staré Mesto",
         "comment" : "Client comment",
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
         "iban" : "XX00000000001",
         "ic_dph" : "",
         "ico" : "44981082",
         "id" : "431",
         "modified" : "2019-02-12 11:51:48",
         "name" : "2day, s. r. o.",
         "notices" : "1",
         "phone" : "",
         "state" : "",
         "swift" : "98765",
         "tags" : null,
         "update" : "1",
         "user_id" : "384",
         "user_profile_id" : "393",
         "uuid" : "NULL",
         "zip" : "811 04"
      }
   }
}
```

#### Insufficient privileges
HTTP status 403.

```json
{
   "message" : "You can't create invoice",
   "error_message" : "You can't create invoice",
   "error" : 1
}
```

#### Missing required data
```json
{
   "error" : 4,
   "error_message" : {
      "data_bad_format" : "Missing required client data."
   }
}
```

#### Missing data
```json
{
   "error" : 4,
   "error_message" : {
      "data_bad_format" : "Missing required client data."
   }
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


## Edit invoice

Edit invoice.
If you want to add tags to invoice, refer to [FAQ > How do I add tags to an entity?](faq.md#how-do-i-add-tags-to-an-entity).

### Request

**URL**: `/invoices/edit`  
**HTTP method**: POST  

```sh
data='{
    "Invoice": {
        "id": 1291,
        "discount": 5
    }
}';

curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoices/edit
```

### Attributes
#### Required

##### Invoice

| name   | type | description                       | default value |
| ------ | ---- | --------------------------------- | ------------- |
| **id** | int  | ID of invoice that will be edited |               |

#### Optional

Same as for **Add invoice**. With the exception of *name* being optional.

### Response

#### Successfully edited
```json
{
    "data": {
        "0": {
            "to_pay": "11.400000",
            "total": "11.40"
        },
        "Client": {
            "address": "Pri Suchom mlyne 6",
            "bank_account": "",
            "bank_account_id": "0",
            "bank_account_prefix": "",
            "bank_code": "",
            "city": "Bratislava - mestská časť Staré Mesto",
            "comment": "Client comment",
            "country": null,
            "country_id": "191",
            "created": "2019-01-23 08:41:37",
            "currency": null,
            "default_variable": "",
            "delivery_address": "",
            "delivery_city": "",
            "delivery_country": null,
            "delivery_country_id": "191",
            "delivery_name": "",
            "delivery_phone": "",
            "delivery_state": "",
            "delivery_zip": "",
            "dic": "2022903949",
            "discount": null,
            "distance": null,
            "dont_travel": "0",
            "due_date": null,
            "email": "name.surname@superfaktura.sk",
            "fax": "",
            "iban": "XX00000000001",
            "ic_dph": "",
            "ico": "44981082",
            "id": "431",
            "modified": "2019-02-13 08:33:09",
            "name": "2day, s. r. o.",
            "notices": "1",
            "phone": "",
            "state": "",
            "swift": "98765",
            "tags": null,
            "update": "1",
            "user_id": "384",
            "user_profile_id": "393",
            "uuid": "NULL",
            "zip": "811 04"
        },
        "ClientData": {
            "address": "Pri Suchom mlyne 6",
            "bank_account": "",
            "bank_account_id": "0",
            "bank_account_prefix": "",
            "bank_code": "",
            "city": "Bratislava - mestská časť Staré Mesto",
            "comment": "Client comment",
            "country": "Slovensko",
            "Country": {
                "eu": "1",
                "id": "191",
                "iso": "sk",
                "name": "Slovensko"
            },
            "country_id": "191",
            "created": "2019-01-23 08:41:37",
            "currency": null,
            "default_variable": "",
            "delivery_address": "",
            "delivery_city": "",
            "delivery_country": "Slovensko",
            "delivery_country_id": "191",
            "delivery_name": "",
            "delivery_phone": "",
            "delivery_state": "",
            "delivery_zip": "",
            "DeliveryCountry": {
                "eu": "1",
                "id": "191",
                "iso": "sk",
                "name": "Slovensko"
            },
            "dic": "2022903949",
            "discount": null,
            "distance": null,
            "dont_travel": "0",
            "due_date": null,
            "email": "name.surname@superfaktura.sk",
            "fax": "",
            "iban": "XX00000000001",
            "ic_dph": "",
            "ico": "44981082",
            "id": "431",
            "modified": "2019-02-13 07:48:40",
            "name": "2day, s. r. o.",
            "notices": "1",
            "phone": "",
            "state": "",
            "swift": "98765",
            "tags": null,
            "update": "1",
            "user_id": "384",
            "user_profile_id": "393",
            "uuid": "NULL",
            "zip": "811 04"
        },
        "Invoice": {
            "amount": "9.50",
            "amount_paid": "0.00",
            "client_data": "{\"Client\":{\"id\":\"431\",\"user_id\":\"384\",\"user_profile_id\":\"393\",\"uuid\":\"NULL\",\"country_id\":\"191\",\"name\":\"2day, s. r. o.\",\"ico\":\"44981082\",\"dic\":\"2022903949\",\"ic_dph\":\"\",\"iban\":\"XX00000000001\",\"swift\":\"98765\",\"bank_account_prefix\":\"\",\"bank_account\":\"\",\"bank_code\":\"\",\"email\":\"name.surname@superfaktura.sk\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"state\":\"\",\"country\":\"Slovensko\",\"delivery_name\":\"\",\"delivery_address\":\"\",\"delivery_city\":\"\",\"delivery_zip\":\"\",\"delivery_state\":\"\",\"delivery_country\":\"Slovensko\",\"delivery_country_id\":\"191\",\"phone\":\"\",\"delivery_phone\":\"\",\"fax\":\"\",\"due_date\":null,\"default_variable\":\"\",\"discount\":null,\"currency\":null,\"bank_account_id\":\"0\",\"comment\":\"Client comment\",\"tags\":null,\"distance\":null,\"dont_travel\":\"0\",\"created\":\"2019-01-23 08:41:37\",\"modified\":\"2019-02-13 07:48:40\",\"update\":\"1\",\"notices\":\"1\"}}",
            "client_id": "431",
            "comment": null,
            "constant": "",
            "country_exchange_rate": "1.00000000",
            "created": "2019-02-12 00:00:00",
            "delivery": "2019-02-12 00:00:00",
            "delivery_type": "",
            "demo": "0",
            "deposit": "0.00",
            "discount": "5",
            "due": "2019-02-26",
            "estimate_id": null,
            "exchange_rate": 1,
            "flag": "issued",
            "header_comment": null,
            "home_currency": "EUR",
            "id": "1291",
            "import_id": null,
            "import_parent_id": null,
            "import_type": null,
            "internal_comment": null,
            "invoice_currency": "EUR",
            "invoice_no": "4",
            "invoice_no_formatted": "2019004",
            "issued_by": null,
            "issued_by_email": "api@example.com",
            "issued_by_phone": "",
            "issued_by_web": null,
            "items_data": "item 1 description of item 1, ",
            "items_name": null,
            "lang": null,
            "mask": "YYYYNNN",
            "modified": "2019-02-13 08:33:09",
            "my_data": "{\"MyData\":{\"id\":\"393\",\"user_id\":\"384\",\"country_id\":\"191\",\"company_name\":\"superfaktura.sk, s.r.o.\",\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"tax_payer\":\"1\",\"BankAccount\":[{\"id\":\"264\",\"user_id\":\"384\",\"user_profile_id\":\"393\",\"default\":\"0\",\"show\":\"1\",\"country_id\":\"191\",\"bank_name\":\"FatraBanka\",\"bank_code\":\"\",\"account\":\"\",\"iban\":\" SK 31 1200 000019 8742637541\",\"swift\":\"9876\",\"created\":\"2019-01-23 08:38:47\",\"modified\":\"2019-01-23 09:35:38\",\"show_account\":\"1\"},{\"id\":\"265\",\"user_id\":\"384\",\"user_profile_id\":\"393\",\"default\":null,\"show\":\"1\",\"country_id\":\"191\",\"bank_name\":\"SuperBanka\",\"bank_code\":\"1200\",\"account\":\"8742637541\",\"iban\":\"\",\"swift\":\"\",\"created\":\"2019-01-23 08:39:56\",\"modified\":\"2019-01-23 08:39:56\",\"show_account\":\"1\"}],\"Logo\":[{\"id\":\"168\",\"model\":\"User\",\"foreign_key\":\"393\",\"dirname\":\"img\",\"basename\":\"9997f862be767814ce9b_393_screen_shot_2018_10_03_at_10_03_19.png\",\"checksum\":\"dd3300a5a4fc754b0f1361baa2ac2e3f\",\"group\":\"logo\",\"default\":\"1\",\"alternative\":null,\"created\":\"2019-01-23 08:37:27\",\"modified\":\"2019-01-23 08:39:56\"}],\"Signature\":{\"id\":\"169\",\"model\":\"User\",\"foreign_key\":\"393\",\"dirname\":\"img\",\"basename\":\"51ee3f8bbd61561eb5f0_393_podpis_1.png\",\"checksum\":\"33b5238616646ca28ebabc02f713a59f\",\"group\":\"signature\",\"default\":\"0\",\"alternative\":null,\"created\":\"2019-01-23 08:37:27\",\"modified\":\"2019-01-23 08:37:27\"},\"country\":\"Slovensko\"}}",
            "name": "Test API",
            "order_no": null,
            "paid": "0.00",
            "parent_id": null,
            "paydate": null,
            "payment_type": null,
            "proforma_id": null,
            "recurring": null,
            "rounding": "item",
            "sequence_id": "2815",
            "show_items_with_dph": true,
            "show_special_vat": false,
            "special_vat_scheme": null,
            "specific": null,
            "status": "1",
            "summary_invoice": "0",
            "tags": "",
            "tax_document": null,
            "taxdate": "2019-02-12",
            "token": "1b089581",
            "type": "regular",
            "user_id": "384",
            "user_profile_id": "393",
            "variable": "2019004",
            "vat": "1.90",
            "vat_transfer": null
        },
        "InvoiceEmail": [],
        "InvoiceItem": [
            {
                "description": "description of item 1",
                "discount": 0,
                "discount_description": "",
                "discount_no_vat": 0,
                "discount_no_vat_total": 0,
                "discount_with_vat": 0,
                "discount_with_vat_total": 0,
                "hide_in_autocomplete": null,
                "id": "1719",
                "invoice_id": "1291",
                "item_price": 10,
                "item_price_no_discount": 10,
                "item_price_vat": 12,
                "item_price_vat_check": 12,
                "item_price_vat_no_discount": 12,
                "name": "item 1",
                "ordernum": "0",
                "quantity": null,
                "sku": null,
                "stock_item_id": null,
                "tax": "20",
                "tax_deposit": "0",
                "unit": "",
                "unit_price": 10,
                "unit_price_discount": 10,
                "unit_price_vat": 12,
                "unit_price_vat_no_discount": 12,
                "user_id": "384",
                "user_profile_id": "393"
            }
        ],
        "InvoicePayment": [],
        "InvoiceSetting": {
            "bysquare": "1",
            "language": "slo",
            "online_payment": false,
            "payment_info": true,
            "signature": true
        },
        "Logo": [
            {
                "alternative": null,
                "basename": "9997f862be767814ce9b_393_screen_shot_2018_10_03_at_10_03_19.png",
                "checksum": "dd3300a5a4fc754b0f1361baa2ac2e3f",
                "created": "2019-01-23 08:37:27",
                "default": "1",
                "dirname": "img",
                "foreign_key": "393",
                "group": "logo",
                "id": "168",
                "model": "User",
                "modified": "2019-01-23 08:39:56"
            }
        ],
        "MyData": {
            "address": "Pri Suchom mlyne 6",
            "BankAccount": [
                {
                    "account": "",
                    "bank_code": "",
                    "bank_name": "FatraBanka",
                    "country_id": "191",
                    "created": "2019-01-23 08:38:47",
                    "default": "0",
                    "iban": " SK 31 1200 000019 8742637541",
                    "id": "264",
                    "modified": "2019-01-23 09:35:38",
                    "show": "1",
                    "show_account": "1",
                    "swift": "9876",
                    "user_id": "384",
                    "user_profile_id": "393"
                },
                {
                    "account": "8742637541",
                    "bank_code": "1200",
                    "bank_name": "SuperBanka",
                    "country_id": "191",
                    "created": "2019-01-23 08:39:56",
                    "default": null,
                    "iban": "",
                    "id": "265",
                    "modified": "2019-01-23 08:39:56",
                    "show": "1",
                    "show_account": "1",
                    "swift": "",
                    "user_id": "384",
                    "user_profile_id": "393"
                }
            ],
            "city": "Bratislava - mestská časť Staré Mesto",
            "company_name": "superfaktura.sk, s.r.o.",
            "country": {
                "eu": "1",
                "id": "191",
                "iso": "sk",
                "name": "Slovensko"
            },
            "country_id": "191",
            "dic": "2023513470",
            "ic_dph": "SK2023513470",
            "ico": "46655034",
            "id": "393",
            "Logo": "[{\"id\":\"168\",\"model\":\"User\",\"foreign_key\":\"393\",\"dirname\":\"img\",\"basename\":\"9997f862be767814ce9b_393_screen_shot_2018_10_03_at_10_03_19.png\",\"checksum\":\"dd3300a5a4fc754b0f1361baa2ac2e3f\",\"group\":\"logo\",\"default\":\"1\",\"alternative\":null,\"created\":\"2019-01-23 08:37:27\",\"modified\":\"2019-01-23 08:39:56\"}]",
            "LogoRaw": [
                {
                    "alternative": null,
                    "basename": "9997f862be767814ce9b_393_screen_shot_2018_10_03_at_10_03_19.png",
                    "checksum": "dd3300a5a4fc754b0f1361baa2ac2e3f",
                    "created": "2019-01-23 08:37:27",
                    "default": "1",
                    "dirname": "img",
                    "foreign_key": "393",
                    "group": "logo",
                    "id": "168",
                    "model": "User",
                    "modified": "2019-01-23 08:39:56"
                }
            ],
            "Signature": "{\"id\":\"169\",\"model\":\"User\",\"foreign_key\":\"393\",\"dirname\":\"img\",\"basename\":\"51ee3f8bbd61561eb5f0_393_podpis_1.png\",\"checksum\":\"33b5238616646ca28ebabc02f713a59f\",\"group\":\"signature\",\"default\":\"0\",\"alternative\":null,\"created\":\"2019-01-23 08:37:27\",\"modified\":\"2019-01-23 08:37:27\"}",
            "SignatureRaw": {
                "alternative": null,
                "basename": "51ee3f8bbd61561eb5f0_393_podpis_1.png",
                "checksum": "33b5238616646ca28ebabc02f713a59f",
                "created": "2019-01-23 08:37:27",
                "default": "0",
                "dirname": "img",
                "foreign_key": "393",
                "group": "signature",
                "id": "169",
                "model": "User",
                "modified": "2019-01-23 08:37:27"
            },
            "tax_payer": "1",
            "user_id": "384",
            "zip": "811 04"
        },
        "Paypal": false,
        "PostStamp": [],
        "Signature": {
            "alternative": null,
            "basename": "51ee3f8bbd61561eb5f0_393_podpis_1.png",
            "checksum": "33b5238616646ca28ebabc02f713a59f",
            "created": "2019-01-23 08:37:27",
            "default": "0",
            "dirname": "img",
            "foreign_key": "393",
            "group": "signature",
            "id": "169",
            "model": "User",
            "modified": "2019-01-23 08:37:27"
        },
        "Summary": {
            "discount": 0.6,
            "invoice_total": 11.4,
            "vat_base_separate": {
                "20": 9.5
            },
            "vat_base_total": 9.5,
            "vat_separate": {
                "20": 1.9
            },
            "vat_total": 1.9
        },
        "SummaryInvoice": {
            "vat_base_separate_negative": {
                "20": 0
            },
            "vat_base_separate_positive": {
                "20": 9.5
            },
            "vat_separate_negative": {
                "20": 0
            },
            "vat_separate_positive": {
                "20": 1.9
            }
        },
        "Tag": [],
        "UnitCount": []
    },
    "status": true
}
```

#### Wrong invoice
```json
{
   "error" : "2",
   "message" : "Invoice ID not found."
}
```

#### Wrong ID format
```json
{
   "error" : "1",
   "message" : "Bad data format."
}
```

#### Bad data
```json
{
   "error" : "1",
   "message" : "Bad data format."
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
 
## Get list of invoices

Get list of invoices.

### Request

**URL**: `/invoices/index.json[/{ATTRIBUTE}:{VALUE}]*`  
**HTTP method**: GET  


```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoices/index.json/listinfo:1/per_page:1/page:2
```  

### Attributes
#### Required
none

#### Optional

URL paremeters:  

| name          | type   | description                                                                          | default value |
| ------------- | ------ | ------------------------------------------------------------------------------------ | ------------- |
| **direction** | string | sorting direction (ASC or DESC)                                                      | 'DESC' |
| **list_info** | int    | show meta data about result? (0=no, 1=yes)                                           | 0 |
| **page**      | int    | page number                                                                          | 1 |
| **per_page**  | int    | number of items per page (max 200)                                                   | |
| **sort**      | string | attribute to sort by                                                                 | 'regular_count' |
| **type**      | string | type of document (proforma, regular, ...). Use <code>&#x7c;</code> as separator for multiple values. | 'regular' |

Filtering parameters

| name               | type         | description    | default value |
| ------------------ | ------------ | ------------   | ------------- |
| **amount_from**    | float        | amount from    | 0             |
| **amount_to**      | float        | amount to      | 0             |
| **client_id**      | int          | client ID      | |
| **created**        | int          | constant specifying time filtering (see [Value lists > Time filter constants](value-lists.md#time-filter-constants)) | |
| **created_since**  | date         | creation date since | |
| **created_to**     | date         | creation date to    | |
| **delivery**       | int          | constant specifying time filtering (see [Value lists > Time filter constants](value-lists.md#time-filter-constants)) | |
| **delivery_since** | date         | delivery date from  | |
| **delivery_to**    | date         | delivery date to    | |
| **delivery_type**  | string       | delivery type (see [Value lists > Delivery types](value-lists.md#delivery-types)). Use <code>&#x7c;</code> as separator for multiple values. | |
| **ignore**         | string / int | IDs of invoices to be ignored. Use <code>&#x7c;</code> as separator for multiple values. | |
| **modified**       | int          | last modification date constant specifying time filtering (see [Value lists > Time filter constants](value-lists.md#time-filter-constants)) | |
| **modified_since** | date         | last modification date from | |
| **modified_to**    | date         | last modification date to   | |
| **order_no**       | string       | order number, from which invoice is created | |
| **paid**           | int          | constant specifying time filtering (see [Value lists > Time filter constants](value-lists.md#time-filter-constants)) | |
| **paid_since**     | date         | pay date since | |
| **paid_to**        | date         | pay date to    | |
| **payment_type**   | string       | payment types (see [Value lists > Payment types](value-lists.md#payment-types)). Use <code>&#x7c;</code> as separator for multiple values. | |
| **search**         | string       | base64 encoded string | |
| **status**         | string / int | invoice status (see [Value lists > Invoice statuses](value-lists.md#invoice-statuses)) | |



### Response

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoices/index.json/listinfo:1/per_page:1/type:regular
```


```json
{
    "filtered": false,
    "itemCount": 7,
    "items": [
        {
            "0": {
                "to_pay": "12.000000",
                "total": "12.00"
            },
            "Client": {
                "address": "Pri Suchom mlyne 6",
                "bank_account": "",
                "bank_account_id": "0",
                "bank_account_prefix": "",
                "bank_code": "",
                "city": "Bratislava - mestská časť Staré Mesto",
                "comment": "Client comment",
                "country": null,
                "country_id": "191",
                "created": "2019-01-23 08:41:37",
                "currency": null,
                "default_variable": "",
                "delivery_address": "",
                "delivery_city": "",
                "delivery_country": null,
                "delivery_country_id": "191",
                "delivery_name": "",
                "delivery_phone": "",
                "delivery_state": "",
                "delivery_zip": "",
                "dic": "2022903949",
                "discount": null,
                "distance": null,
                "dont_travel": "0",
                "due_date": null,
                "email": "name.surname@superfaktura.sk",
                "fax": "",
                "iban": "XX00000000001",
                "ic_dph": "",
                "ico": "44981082",
                "id": "431",
                "modified": "2019-02-12 12:54:50",
                "name": "2day, s. r. o.",
                "notices": "1",
                "phone": "",
                "state": "",
                "swift": "98765",
                "tags": null,
                "update": "1",
                "user_id": "384",
                "user_profile_id": "393",
                "uuid": "NULL",
                "zip": "811 04"
            },
            "ClientData": {
                "address": "Pri Suchom mlyne 6",
                "city": "Bratislava - mestská časť Staré Mesto",
                "Country": {
                    "eu": "1",
                    "id": "191",
                    "iso": "sk",
                    "name": "Slovensko"
                },
                "country": "Slovensko",
                "country_id": "191",
                "delivery_address": "",
                "delivery_city": "",
                "delivery_country": "Slovensko",
                "delivery_country_id": "191",
                "delivery_name": "",
                "delivery_phone": "",
                "delivery_state": "",
                "delivery_zip": "",
                "DeliveryCountry": {
                    "eu": "1",
                    "id": "191",
                    "iso": "sk",
                    "name": "Slovensko"
                },
                "dic": "2022903949",
                "email": "name.surname@superfaktura.sk",
                "fax": "",
                "ic_dph": "",
                "ico": "44981082",
                "id": "431",
                "name": "2day, s. r. o.",
                "phone": "",
                "state": "",
                "updateClient": "0",
                "zip": "811 04"
            },
            "Invoice": {
                "amount": "10.00",
                "amount_paid": "0.00",
                "client_data": "{\"Client\":{\"id\":\"431\",\"name\":\"2day, s. r. o.\",\"address\":\"Pri Suchom mlyne 6\",\"ico\":\"44981082\",\"email\":\"name.surname@superfaktura.sk\",\"zip\":\"811 04\",\"dic\":\"2022903949\",\"phone\":\"\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"ic_dph\":\"\",\"fax\":\"\",\"country_id\":\"191\",\"state\":\"\",\"delivery_name\":\"\",\"delivery_zip\":\"\",\"delivery_city\":\"\",\"delivery_address\":\"\",\"delivery_phone\":\"\",\"delivery_country_id\":\"191\",\"delivery_state\":\"\",\"updateClient\":\"0\",\"country\":\"Slovensko\",\"delivery_country\":\"Slovensko\"}}",
                "client_id": "431",
                "comment": "",
                "constant": "",
                "country_exchange_rate": "1.00000000",
                "created": "2019-02-12 00:00:00",
                "delivery": "2019-02-12 00:00:00",
                "delivery_type": "",
                "demo": "0",
                "deposit": "0.00",
                "discount": "0",
                "due": "2019-02-26",
                "estimate_id": null,
                "exchange_rate": 1,
                "flag": "issued",
                "header_comment": "",
                "home_currency": "EUR",
                "id": "1295",
                "import_id": null,
                "import_parent_id": null,
                "import_type": null,
                "internal_comment": null,
                "invoice_currency": "EUR",
                "invoice_no": "7",
                "invoice_no_formatted": "2019007",
                "issued_by": "superfaktura.sk, s.r.o.",
                "issued_by_email": "api@example.com",
                "issued_by_phone": "",
                "issued_by_web": "",
                "items_data": "item 1 description of item 1, ",
                "items_name": null,
                "lang": "slo",
                "mask": "YYYYNNN",
                "modified": "2019-02-12 12:54:50",
                "my_data": "{\"MyData\":{\"id\":\"393\",\"user_id\":\"384\",\"user_profile_id\":\"\",\"country_id\":\"191\",\"company_name\":\"superfaktura.sk, s.r.o.\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"tax_payer\":\"1\",\"logo_key\":\"\",\"logo_id\":\"\",\"web\":\"\",\"Logo\":\"\",\"Signature\":\"\",\"travel_agencies\":\"0\",\"business_register\":\"Bratislava I, odd. Sro, vl.\\u010d.81403\\/B\",\"BankAccount\":[{\"show_account\":\"1\",\"id\":\"264\",\"default\":\"0\",\"country_id\":\"191\",\"bank_name\":\"FatraBanka\",\"bank_code\":\"\",\"account\":\"\",\"iban\":\" SK 31 1200 000019 8742637541\",\"swift\":\"9876\"},{\"show_account\":\"1\",\"id\":\"265\",\"default\":\"\",\"country_id\":\"191\",\"bank_name\":\"SuperBanka\",\"bank_code\":\"1200\",\"account\":\"8742637541\",\"iban\":\"\",\"swift\":\"\"}],\"update_profile\":\"0\",\"country\":\"Slovensko\"}}",
                "name": "1291 - kopia",
                "order_no": "",
                "paid": "0.00",
                "parent_id": null,
                "paydate": null,
                "payment_type": "",
                "proforma_id": null,
                "recurring": null,
                "rounding": "item",
                "sequence_id": "2815",
                "show_items_with_dph": true,
                "show_special_vat": false,
                "special_vat_scheme": null,
                "specific": "",
                "status": "1",
                "summary_invoice": null,
                "tags": "",
                "tax_document": "0",
                "taxdate": "2019-02-12",
                "token": "b940621e",
                "type": "regular",
                "user_id": "384",
                "user_profile_id": "393",
                "variable": "2019007",
                "vat": "2.00",
                "vat_transfer": "0"
            },
            "InvoiceEmail": [],
            "InvoiceItem": [
                {
                    "description": "description of item 1",
                    "discount": 0,
                    "discount_description": "",
                    "discount_no_vat": 0,
                    "discount_no_vat_total": 0,
                    "discount_with_vat": 0,
                    "discount_with_vat_total": 0,
                    "hide_in_autocomplete": null,
                    "id": "1723",
                    "invoice_id": "1295",
                    "item_price": 10,
                    "item_price_no_discount": 10,
                    "item_price_vat": 12,
                    "item_price_vat_check": 12,
                    "item_price_vat_no_discount": 12,
                    "name": "item 1",
                    "ordernum": "0",
                    "quantity": null,
                    "sku": null,
                    "stock_item_id": "0",
                    "tax": "20",
                    "tax_deposit": "0",
                    "unit": "",
                    "unit_price": 10,
                    "unit_price_discount": 10,
                    "unit_price_vat": 12,
                    "unit_price_vat_no_discount": 12,
                    "user_id": "384",
                    "user_profile_id": "393"
                }
            ],
            "InvoicePayment": [],
            "InvoiceSetting": {
                "bysquare": "1",
                "force_iban": "",
                "language": "slo",
                "online_payment": "",
                "payment_info": "1",
                "paypal": "",
                "show_prices": "",
                "show_summary": "",
                "signature": "1"
            },
            "Logo": [
                {
                    "alternative": null,
                    "basename": "9997f862be767814ce9b_393_screen_shot_2018_10_03_at_10_03_19.png",
                    "checksum": "dd3300a5a4fc754b0f1361baa2ac2e3f",
                    "created": "2019-01-23 08:37:27",
                    "default": "1",
                    "dirname": "img",
                    "foreign_key": "393",
                    "group": "logo",
                    "id": "168",
                    "model": "User",
                    "modified": "2019-01-23 08:39:56"
                }
            ],
            "MyData": {
                "address": "Pri Suchom mlyne 6",
                "BankAccount": [
                    {
                        "account": "",
                        "bank_code": "",
                        "bank_name": "FatraBanka",
                        "country_id": "191",
                        "default": "0",
                        "iban": " SK 31 1200 000019 8742637541",
                        "id": "264",
                        "show_account": "1",
                        "swift": "9876"
                    },
                    {
                        "account": "8742637541",
                        "bank_code": "1200",
                        "bank_name": "SuperBanka",
                        "country_id": "191",
                        "default": "",
                        "iban": "",
                        "id": "265",
                        "show_account": "1",
                        "swift": ""
                    }
                ],
                "business_register": "Bratislava I, odd. Sro, vl.č.81403/B",
                "city": "Bratislava - mestská časť Staré Mesto",
                "company_name": "superfaktura.sk, s.r.o.",
                "country": {
                    "eu": "1",
                    "id": "191",
                    "iso": "sk",
                    "name": "Slovensko"
                },
                "country_id": "191",
                "dic": "2023513470",
                "ic_dph": "SK2023513470",
                "ico": "46655034",
                "id": "393",
                "Logo": "[{\"id\":\"168\",\"model\":\"User\",\"foreign_key\":\"393\",\"dirname\":\"img\",\"basename\":\"9997f862be767814ce9b_393_screen_shot_2018_10_03_at_10_03_19.png\",\"checksum\":\"dd3300a5a4fc754b0f1361baa2ac2e3f\",\"group\":\"logo\",\"default\":\"1\",\"alternative\":null,\"created\":\"2019-01-23 08:37:27\",\"modified\":\"2019-01-23 08:39:56\"}]",
                "logo_id": "",
                "logo_key": "",
                "LogoRaw": [
                    {
                        "alternative": null,
                        "basename": "9997f862be767814ce9b_393_screen_shot_2018_10_03_at_10_03_19.png",
                        "checksum": "dd3300a5a4fc754b0f1361baa2ac2e3f",
                        "created": "2019-01-23 08:37:27",
                        "default": "1",
                        "dirname": "img",
                        "foreign_key": "393",
                        "group": "logo",
                        "id": "168",
                        "model": "User",
                        "modified": "2019-01-23 08:39:56"
                    }
                ],
                "Signature": "{\"id\":\"169\",\"model\":\"User\",\"foreign_key\":\"393\",\"dirname\":\"img\",\"basename\":\"51ee3f8bbd61561eb5f0_393_podpis_1.png\",\"checksum\":\"33b5238616646ca28ebabc02f713a59f\",\"group\":\"signature\",\"default\":\"0\",\"alternative\":null,\"created\":\"2019-01-23 08:37:27\",\"modified\":\"2019-01-23 08:37:27\"}",
                "SignatureRaw": {
                    "alternative": null,
                    "basename": "51ee3f8bbd61561eb5f0_393_podpis_1.png",
                    "checksum": "33b5238616646ca28ebabc02f713a59f",
                    "created": "2019-01-23 08:37:27",
                    "default": "0",
                    "dirname": "img",
                    "foreign_key": "393",
                    "group": "signature",
                    "id": "169",
                    "model": "User",
                    "modified": "2019-01-23 08:37:27"
                },
                "tax_payer": "1",
                "travel_agencies": "0",
                "update_profile": "0",
                "user_id": "384",
                "user_profile_id": "",
                "web": "",
                "zip": "811 04"
            },
            "Paypal": false,
            "PostStamp": [],
            "Signature": {
                "alternative": null,
                "basename": "51ee3f8bbd61561eb5f0_393_podpis_1.png",
                "checksum": "33b5238616646ca28ebabc02f713a59f",
                "created": "2019-01-23 08:37:27",
                "default": "0",
                "dirname": "img",
                "foreign_key": "393",
                "group": "signature",
                "id": "169",
                "model": "User",
                "modified": "2019-01-23 08:37:27"
            },
            "Summary": {
                "discount": 0,
                "invoice_total": 12,
                "vat_base_separate": {
                    "20": 10
                },
                "vat_base_total": 10,
                "vat_separate": {
                    "20": 2
                },
                "vat_total": 2
            },
            "SummaryInvoice": {
                "vat_base_separate_negative": {
                    "20": 0
                },
                "vat_base_separate_positive": {
                    "20": 10
                },
                "vat_separate_negative": {
                    "20": 0
                },
                "vat_separate_positive": {
                    "20": 2
                }
            },
            "Tag": [],
            "UnitCount": []
        }
    ],
    "page": 1,
    "pageCount": 7,
    "perPage": 1
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
 

## Pay invoice

Pay invoice

### Request
**URL**: `/invoice_payments/add/ajax:1/api:1`  
**HTTP method**: POST  

```
data='{
    "InvoicePayment":{
        "invoice_id":1276,
        "payment_type":"cash",
        "amount":100,
        "created":"2019-01-01",
        "currency":"NOK"
    }
};

curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoice_payments/add/ajax:1/api:1
```

### Attributes

#### Required

| name                  | type   | description | default value |
| --------------------- | ------ | ----------- | ------------- |
| **invoice_id**        | int    | invoice ID | |

#### Optional

| name                  | type   | description | default value |
| --------------------- | ------ | ----------- | ------------- |
| **amount**            | float  | amount of money paid | invoice total price |
| **cash_register_id**  | int    | cash register ID | |
| **currency**          | string | currency (see [Value lists > Currencies](value-lists.md#currencies))| EUR in SK, CZK in CZ |
| **date**              | date   | date when payment was done (format: `YYYY-MM-DD`) | &lt;current date&gt; |
| **payment_type**      | string | payment type (see [Value lists > Payment types](value-lists.md#payment-types)) | transfer |



### Response


#### Successfully added payment
```json
{
   "overdue" : false,
   "exchange_rate" : 9.9483,
   "error" : 0,
   "currency" : null,
   "home_currency" : "€",
   "created" : "2019-01-01",
   "invoice_id" : 1276,
   "to_pay_home_cur" : -0.46942693726566,
   "status" : 3,
   "invoice_type" : "regular",
   "invoice_currency" : "€",
   "to_pay" : -4.67,
   "parent_id" : null,
   "payment_id" : "197",
   "flash_message" : {
      "text" : "Úhrada bola uložená",
      "type" : "success"
   },
   "paid" : 10.67
}
```

#### Adding payment to already fully paid invoice
```json
{
   "message" : "Faktúra je už plne uhradená",
   "error_messages" : [],
   "error" : 1
}
```

#### Invalid ID
```json
{
   "error" : 1,
   "message" : "Payment not found"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


## Set invoice language

Sets invoice language

### Request
**URL**: `/invoices/setinvoicelanguage/{INVOICE_ID}/lang:{LANG}`  
**HTTP method**: GET  

```
curl -X GET \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
    https://moja.superfaktura.sk/invoices/setinvoicelanguage/1276/lang:deu
```


### Attributes
#### Required

| name           | type   | description | default value |
| -------------- | ------ | ----------- | ------------- |
| **invoice_id** | int    | invoice ID | |
| **lang**       | string | invoice language (for list of possible values see [Value lists > Language list](value-lists.md#language-list)) | |

#### Optional
none


### Response
#### Successfully changed language

```json
{
   "status" : 1,
   "message" : "Success"
}
```

#### Invalid language
```json
{
   "status" : 0,
   "message" : "Language is not supported."
}
```

#### Insufficient permissions
```json
{
   "status" : 0,
   "message" : "Permission denied."
}
```

 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


## Mark invoice as sent via email

Mark invoice as sent via email.

### Request
**URL**: `/invoices/mark_as_sent`  
**HTTP method**: POST  

```sh
data='{
    "InvoiceEmail":{
        "invoice_id":1276,
        "email":"user@example.com",
        "subject":"subject",
        "message":"hello world"
    }
}';

curl -X POST \
  -d "data=$data" \
  -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
  https://moja.superfaktura.sk/invoices/mark_as_sent
```

 

### Attributes
#### Required

```json
{
  "InvoiceEmail": {
    "invoice_id": 1276,
    "email": "user@example.com",
    "subject": "subject",
    "message": "hello world"
  }
}
```
#### Optional
none

### Response

#### Successfully marked
```json
{
   "error_message" : "Invoice marked as sent",
   "error" : 0
}
```

#### Invalid post data
  
```json
{
    "error": 1,
    "error_message": "Invalid post data"
}
```

#### Wrong HTTP method
```json
{
    "error": 2,
    "error_message": "This method is POST only"
}
```

#### Invalid JSON or no data   
```json
{
    "error": 3,
    "error_message": "Invalid invoice data"
}
```

#### Invalid data

In `error_messages` is list of validation errors.

```json
{
    "error": 4,
    "error_message": "Invalid email data",
    "error_messages": []
}
```

#### Invalid invoice ID  
```json
{
    "error": 5,
    "error_message": "Invalid invoice id"
}
```


- - - - - - - - - -


## Delete invoice payment

Delete invoice payment.

### Request
**URL**: `/invoice_payments/delete/{PAYMENT_ID}`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoice_payments/delete/2
```

### Attributes
#### Required

| name           | type | description | default value |
| -------------- | ---- | ----------- | ------------- |
| **payment_id** | int  | payment ID  |               |

### Response

#### Successful deletion
```json
{
   "error" : 0,
   "invoice_id" : "16",
   "paid" : "0.00",
   "status" : 1,
   "to_pay" : 30
}
```

#### Payment not found 
```json
{
   "message" : "Payment not found",
   "error" : 1
}
```

#### Unsuccessful deletion  
```json
{
    "error": 1,
    "message": "Error deleting payment"   
}
```

#### Invalid ID
```json
{
    "error": 1,
    "message": "Invalid id for invoice payment"   
}
```



- - - - - - - - -

## Delete invoice

Delete invoice by ID.

### Request
**URL**: `/invoices/delete/{ID}`  
**HTTP method**: GET  


```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoices/delete/48
```

### Attributes
#### Required

| name   | type | description | default value |
| ------ | ---- | ----------- | ------------- |
| **ID** | int  | invoice ID  |               |

#### Optional
none

### Response

#### Successful deletion

```json
{
   "error" : 0,
   "message" : "Invoice deleted"
}
```

#### Wrong ID
Returns HTTP status 404.

```json
{
  "message" : "Invoice not found",
  "error" : 1,
  "error_message" : "Invoice not found"
}
```

#### Deleting locked invoice
```json
{
   "error_message" : "Invoice locked for editing",
   "error" : 1,
   "message" : "Invoice locked for editing"
}
```

#### Error during deletion
If an error occurs, HTTP status 404 is returned.

```json
{
   "message" : "Invoice could not be deleted",
   "error" : 1,
   "error_message" : "Invoice could not be deleted"
}
```




- - - - - - - - - - - - - - - - - - - - - - - - - - -


## Get invoice details

Get information about multiple invoices at once.
You can specify up to 100 invoice IDs.

### Request
**URL**: `/invoices/getInvoiceDetails/{IDS}`  
**HTTP method**: GET  

```sh
curl -X GET \
     -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
     https://moja.superfaktura.sk/invoices/getInvoiceDetails/1275,1276
```

### Attributes
#### Required
URL parameters:

| name    | type   | description | default value |
| ------- | ------ | ----------- | ------------- |
| **ids** | string | list of invoice IDs separated by comma | |


#### Optional
none

### Response

Returns list of invoices with all the information about them.
The list consists of keys (invoice ID) and value which is JSON object.
For more details about fields present in result see example response.

#### Success
```json
{
   "1276" : {
      "Paypal" : false,
      "MyData" : {
         "country_id" : "191",
         "dic" : "2023513470",
         "ic_dph" : "SK2023513470",
         "id" : "393",
         "travel_agencies" : "0",
         "user_id" : "384",
         "web" : "",
         "BankAccount" : [
            {
               "account" : "",
               "bank_code" : "",
               "bank_name" : "FatraBanka",
               "country_id" : "191",
               "default" : "1",
               "iban" : " SK 31 1200 000019 8742637541",
               "id" : "264",
               "show_account" : "1",
               "swift" : "9876"
            },
            {
               "account" : "8742637541",
               "bank_code" : "1200",
               "bank_name" : "SuperBanka",
               "country_id" : "191",
               "default" : "",
               "iban" : "",
               "id" : "265",
               "show_account" : "1",
               "swift" : ""
            }
         ],
         "Logo" : "[{\"id\":\"168\",\"model\":\"User\",\"foreign_key\":\"393\",\"dirname\":\"img\",\"basename\":\"9997f862be767814ce9b_393_screen_shot_2018_10_03_at_10_03_19.png\",\"checksum\":\"dd3300a5a4fc754b0f1361baa2ac2e3f\",\"group\":\"logo\",\"default\":\"1\",\"alternative\":null,\"created\":\"2019-01-23 08:37:27\",\"modified\":\"2019-01-23 08:39:56\"}]",
         "zip" : "811 04",
         "country" : {
            "eu" : "1",
            "iso" : "sk",
            "name" : "Slovensko",
            "id" : "191"
         },
         "address" : "Pri Suchom mlyne 6",
         "business_register" : "Bratislava I, odd. Sro, vl.č.81403/B",
         "city" : "Bratislava - mestská časť Staré Mesto",
         "company_name" : "superfaktura.sk, s.r.o.",
         "ico" : "46655034",
         "logo_id" : "",
         "logo_key" : "",
         "Signature" : "{\"id\":\"169\",\"model\":\"User\",\"foreign_key\":\"393\",\"dirname\":\"img\",\"basename\":\"51ee3f8bbd61561eb5f0_393_podpis_1.png\",\"checksum\":\"33b5238616646ca28ebabc02f713a59f\",\"group\":\"signature\",\"default\":\"0\",\"alternative\":null,\"created\":\"2019-01-23 08:37:27\",\"modified\":\"2019-01-23 08:37:27\"}",
         "tax_payer" : "1",
         "update_profile" : "0",
         "user_profile_id" : ""
      },
      "InvoiceItem" : [
         {
            "description" : "",
            "discount" : 0,
            "discount_description" : "Zľava",
            "discount_no_vat" : 0,
            "discount_no_vat_total" : 0,
            "discount_with_vat" : 0,
            "discount_with_vat_total" : 0,
            "hide_in_autocomplete" : null,
            "id" : "1696",
            "invoice_id" : "1276",
            "item_price" : 5,
            "item_price_no_discount" : 5,
            "item_price_vat" : 6,
            "item_price_vat_check" : 6,
            "item_price_vat_no_discount" : 6,
            "name" : "Clenstvo",
            "ordernum" : "0",
            "quantity" : "1",
            "sku" : null,
            "stock_item_id" : "0",
            "tax" : "20",
            "tax_deposit" : "0",
            "unit" : "",
            "unit_price" : 5,
            "unit_price_discount" : 5,
            "unit_price_vat" : 6,
            "unit_price_vat_no_discount" : 6,
            "user_id" : "384",
            "user_profile_id" : "393"
         }
      ],
      "PostStamp" : [],
      "Signature" : {
         "alternative" : null,
         "basename" : "51ee3f8bbd61561eb5f0_393_podpis_1.png",
         "checksum" : "33b5238616646ca28ebabc02f713a59f",
         "created" : "2019-01-23 08:37:27",
         "default" : "0",
         "dirname" : "img",
         "foreign_key" : "393",
         "group" : "signature",
         "id" : "169",
         "model" : "User",
         "modified" : "2019-01-23 08:37:27"
      },
      "Logo" : [
         {
            "alternative" : null,
            "basename" : "9997f862be767814ce9b_393_screen_shot_2018_10_03_at_10_03_19.png",
            "checksum" : "dd3300a5a4fc754b0f1361baa2ac2e3f",
            "created" : "2019-01-23 08:37:27",
            "default" : "1",
            "dirname" : "img",
            "foreign_key" : "393",
            "group" : "logo",
            "id" : "168",
            "model" : "User",
            "modified" : "2019-01-23 08:39:56"
         }
      ],
      "UnitCount" : [],
      "InvoicePayment" : [],
      "Client" : {
         "address" : "Pri Suchom mlyne 6",
         "bank_account" : "",
         "bank_account_id" : null,
         "bank_account_prefix" : null,
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
         "dont_travel" : null,
         "due_date" : null,
         "email" : "",
         "fax" : "",
         "iban" : "",
         "ic_dph" : "",
         "ico" : "44981082",
         "id" : "431",
         "modified" : "2019-01-23 08:43:02",
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
      },
      "InvoiceInsurance" : [],
      "Summary" : {
         "discount" : 0,
         "invoice_total" : 6,
         "vat_base_total" : 5,
         "vat_base_separate" : {
            "20" : 5
         },
         "vat_separate" : {
            "20" : 1
         },
         "vat_total" : 1
      },
      "Tag" : [],
      "SummaryInvoice" : {
         "vat_base_separate_negative" : {
            "20" : 0
         },
         "vat_base_separate_positive" : {
            "20" : 5
         },
         "vat_separate_positive" : {
            "20" : 1
         },
         "vat_separate_negative" : {
            "20" : 0
         }
      },
      "InvoiceEmail" : [],
      "Invoice" : {
         "amount" : "5.00",
         "amount_paid" : "0.00",
         "client_data" : "{\"Client\":{\"id\":\"431\",\"name\":\"2day, s. r. o.\",\"address\":\"Pri Suchom mlyne 6\",\"ico\":\"44981082\",\"email\":\"\",\"zip\":\"811 04\",\"dic\":\"2022903949\",\"phone\":\"\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"ic_dph\":\"\",\"fax\":\"\",\"country_id\":\"191\",\"state\":\"\",\"delivery_name\":\"\",\"delivery_zip\":\"\",\"delivery_city\":\"\",\"delivery_address\":\"\",\"delivery_phone\":\"\",\"delivery_country_id\":\"191\",\"delivery_state\":\"\",\"updateClient\":\"0\",\"country\":\"Slovensko\",\"delivery_country\":\"Slovensko\"}}",
         "client_id" : "431",
         "comment" : "",
         "constant" : "",
         "country_exchange_rate" : "1.00000000",
         "created" : "2019-01-23 00:00:00",
         "delivery" : "2019-01-23 00:00:00",
         "delivery_type" : "",
         "demo" : "0",
         "deposit" : "0.00",
         "discount" : "0",
         "due" : "2019-02-06",
         "estimate_id" : null,
         "exchange_rate" : 1,
         "flag" : "issued",
         "header_comment" : "",
         "home_currency" : "EUR",
         "id" : "1276",
         "import_id" : null,
         "import_parent_id" : null,
         "import_type" : null,
         "internal_comment" : null,
         "invoice_currency" : "EUR",
         "invoice_no" : "2",
         "invoice_no_formatted" : "2019002",
         "issued_by" : "superfaktura.sk, s.r.o.",
         "issued_by_email" : "api@example.com",
         "issued_by_phone" : "",
         "issued_by_web" : "",
         "items_data" : "Clenstvo , ",
         "items_name" : null,
         "lang" : "slo",
         "mask" : "YYYYNNN",
         "modified" : "2019-01-23 08:43:02",
         "my_data" : "{\"MyData\":{\"id\":\"393\",\"user_id\":\"384\",\"user_profile_id\":\"\",\"country_id\":\"191\",\"company_name\":\"superfaktura.sk, s.r.o.\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"tax_payer\":\"1\",\"logo_key\":\"\",\"logo_id\":\"\",\"web\":\"\",\"Logo\":\"[{\\\"id\\\":\\\"168\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"393\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"9997f862be767814ce9b_393_screen_shot_2018_10_03_at_10_03_19.png\\\",\\\"checksum\\\":\\\"dd3300a5a4fc754b0f1361baa2ac2e3f\\\",\\\"group\\\":\\\"logo\\\",\\\"default\\\":\\\"1\\\",\\\"alternative\\\":null,\\\"created\\\":\\\"2019-01-23 08:37:27\\\",\\\"modified\\\":\\\"2019-01-23 08:39:56\\\"}]\",\"Signature\":\"{\\\"id\\\":\\\"169\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"393\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"51ee3f8bbd61561eb5f0_393_podpis_1.png\\\",\\\"checksum\\\":\\\"33b5238616646ca28ebabc02f713a59f\\\",\\\"group\\\":\\\"signature\\\",\\\"default\\\":\\\"0\\\",\\\"alternative\\\":null,\\\"created\\\":\\\"2019-01-23 08:37:27\\\",\\\"modified\\\":\\\"2019-01-23 08:37:27\\\"}\",\"travel_agencies\":\"0\",\"business_register\":\"Bratislava I, odd. Sro, vl.\\u010d.81403\\/B\",\"BankAccount\":[{\"show_account\":\"1\",\"id\":\"264\",\"default\":\"1\",\"country_id\":\"191\",\"bank_name\":\"FatraBanka\",\"bank_code\":\"\",\"account\":\"\",\"iban\":\" SK 31 1200 000019 8742637541\",\"swift\":\"9876\"},{\"show_account\":\"1\",\"id\":\"265\",\"default\":\"\",\"country_id\":\"191\",\"bank_name\":\"SuperBanka\",\"bank_code\":\"1200\",\"account\":\"8742637541\",\"iban\":\"\",\"swift\":\"\"}],\"update_profile\":\"0\",\"country\":\"Slovensko\"}}",
         "name" : "Faktúra 2019002",
         "order_no" : "",
         "paid" : "0.00",
         "parent_id" : null,
         "paydate" : null,
         "payment_type" : "",
         "proforma_id" : null,
         "recurring" : null,
         "rounding" : "item",
         "sequence_id" : "2815",
         "show_items_with_dph" : true,
         "show_special_vat" : false,
         "special_vat_scheme" : null,
         "specific" : "",
         "status" : "1",
         "summary_invoice" : null,
         "tags" : "",
         "tax_document" : "0",
         "taxdate" : "2019-01-23",
         "token" : "a452c6e3",
         "type" : "regular",
         "user_id" : "384",
         "user_profile_id" : "393",
         "variable" : "2019002",
         "vat" : "1.00",
         "vat_transfer" : "0"
      },
      "ClientData" : {
         "address" : "Pri Suchom mlyne 6",
         "country" : "Slovensko",
         "country_id" : "191",
         "delivery_address" : "",
         "delivery_city" : "",
         "delivery_country" : "Slovensko",
         "delivery_country_id" : "191",
         "delivery_name" : "",
         "delivery_phone" : "",
         "delivery_state" : "",
         "delivery_zip" : "",
         "dic" : "2022903949",
         "email" : "",
         "fax" : "",
         "ic_dph" : "",
         "ico" : "44981082",
         "id" : "431",
         "name" : "2day, s. r. o.",
         "phone" : "",
         "state" : "",
         "updateClient" : "0",
         "zip" : "811 04",
         "DeliveryCountry" : {
            "eu" : "1",
            "id" : "191",
            "iso" : "sk",
            "name" : "Slovensko"
         },
         "Country" : {
            "eu" : "1",
            "id" : "191",
            "iso" : "sk",
            "name" : "Slovensko"
         },
         "city" : "Bratislava - mestská časť Staré Mesto"
      }
   },
   "1275" : {
      "Client" : {
         "address" : "Pri Suchom mlyne 6",
         "bank_account" : "",
         "bank_account_id" : null,
         "bank_account_prefix" : null,
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
         "dont_travel" : null,
         "due_date" : null,
         "email" : "",
         "fax" : "",
         "iban" : "",
         "ic_dph" : "",
         "ico" : "44981082",
         "id" : "431",
         "modified" : "2019-01-23 08:42:25",
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
      },
      "InvoiceInsurance" : [],
      "Invoice" : {
         "amount" : "120.00",
         "amount_paid" : "144.00",
         "client_data" : "{\"Client\":{\"id\":\"431\",\"name\":\"2day, s. r. o.\",\"address\":\"Pri Suchom mlyne 6\",\"ico\":\"44981082\",\"email\":\"\",\"zip\":\"811 04\",\"dic\":\"2022903949\",\"phone\":\"\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"ic_dph\":\"\",\"fax\":\"\",\"country_id\":\"191\",\"state\":\"\",\"delivery_name\":\"\",\"delivery_zip\":\"\",\"delivery_city\":\"\",\"delivery_address\":\"\",\"delivery_phone\":\"\",\"delivery_country_id\":\"191\",\"delivery_state\":\"\",\"updateClient\":\"0\",\"country\":\"Slovensko\",\"delivery_country\":\"Slovensko\"}}",
         "client_id" : "431",
         "comment" : "",
         "constant" : "",
         "country_exchange_rate" : "1.00000000",
         "created" : "2019-01-23 00:00:00",
         "delivery" : "2019-01-23 00:00:00",
         "delivery_type" : "",
         "demo" : "0",
         "deposit" : "0.00",
         "discount" : "0",
         "due" : "2019-02-06",
         "estimate_id" : null,
         "exchange_rate" : 1,
         "flag" : "fully-paid",
         "header_comment" : "",
         "home_currency" : "EUR",
         "id" : "1275",
         "import_id" : null,
         "import_parent_id" : null,
         "import_type" : null,
         "internal_comment" : null,
         "invoice_currency" : "EUR",
         "invoice_no" : "1",
         "invoice_no_formatted" : "2019001",
         "issued_by" : "superfaktura.sk, s.r.o.",
         "issued_by_email" : "api@example.com",
         "issued_by_phone" : "",
         "issued_by_web" : "",
         "items_data" : "Fiktivna polozka , ",
         "items_name" : null,
         "lang" : "slo",
         "mask" : "YYYYNNN",
         "modified" : "2019-01-23 08:42:25",
         "my_data" : "{\"MyData\":{\"id\":\"393\",\"user_id\":\"384\",\"user_profile_id\":\"\",\"country_id\":\"191\",\"company_name\":\"superfaktura.sk, s.r.o.\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"tax_payer\":\"1\",\"logo_key\":\"\",\"logo_id\":\"\",\"web\":\"\",\"Logo\":\"[{\\\"id\\\":\\\"168\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"393\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"9997f862be767814ce9b_393_screen_shot_2018_10_03_at_10_03_19.png\\\",\\\"checksum\\\":\\\"dd3300a5a4fc754b0f1361baa2ac2e3f\\\",\\\"group\\\":\\\"logo\\\",\\\"default\\\":\\\"1\\\",\\\"alternative\\\":null,\\\"created\\\":\\\"2019-01-23 08:37:27\\\",\\\"modified\\\":\\\"2019-01-23 08:39:56\\\"}]\",\"Signature\":\"{\\\"id\\\":\\\"169\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"393\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"51ee3f8bbd61561eb5f0_393_podpis_1.png\\\",\\\"checksum\\\":\\\"33b5238616646ca28ebabc02f713a59f\\\",\\\"group\\\":\\\"signature\\\",\\\"default\\\":\\\"0\\\",\\\"alternative\\\":null,\\\"created\\\":\\\"2019-01-23 08:37:27\\\",\\\"modified\\\":\\\"2019-01-23 08:37:27\\\"}\",\"travel_agencies\":\"0\",\"business_register\":\"Bratislava I, odd. Sro, vl.\\u010d.81403\\/B\",\"BankAccount\":[{\"show_account\":\"1\",\"id\":\"264\",\"default\":\"1\",\"country_id\":\"191\",\"bank_name\":\"FatraBanka\",\"bank_code\":\"\",\"account\":\"\",\"iban\":\" SK 31 1200 000019 8742637541\",\"swift\":\"9876\"},{\"show_account\":\"1\",\"id\":\"265\",\"default\":\"\",\"country_id\":\"191\",\"bank_name\":\"SuperBanka\",\"bank_code\":\"1200\",\"account\":\"8742637541\",\"iban\":\"\",\"swift\":\"\"}],\"update_profile\":\"0\",\"country\":\"Slovensko\"}}",
         "name" : "Faktúra 2019001",
         "order_no" : "",
         "paid" : "144.00",
         "parent_id" : null,
         "paydate" : "2019-01-23 00:00:00",
         "payment_type" : "transfer",
         "proforma_id" : null,
         "recurring" : null,
         "rounding" : "item",
         "sequence_id" : "2815",
         "show_items_with_dph" : true,
         "show_special_vat" : false,
         "special_vat_scheme" : null,
         "specific" : "",
         "status" : "3",
         "summary_invoice" : null,
         "tags" : "2day",
         "tax_document" : "0",
         "taxdate" : "2019-01-23",
         "token" : "09feb1bd",
         "type" : "regular",
         "user_id" : "384",
         "user_profile_id" : "393",
         "variable" : "2019001",
         "vat" : "24.00",
         "vat_transfer" : "0"
      },
      "ClientData" : {
         "address" : "Pri Suchom mlyne 6",
         "city" : "Bratislava - mestská časť Staré Mesto",
         "country" : "Slovensko",
         "country_id" : "191",
         "delivery_address" : "",
         "delivery_city" : "",
         "delivery_country" : "Slovensko",
         "delivery_country_id" : "191",
         "delivery_name" : "",
         "delivery_phone" : "",
         "delivery_state" : "",
         "delivery_zip" : "",
         "dic" : "2022903949",
         "email" : "",
         "fax" : "",
         "ic_dph" : "",
         "ico" : "44981082",
         "id" : "431",
         "name" : "2day, s. r. o.",
         "phone" : "",
         "state" : "",
         "updateClient" : "0",
         "zip" : "811 04",
         "Country" : {
            "eu" : "1",
            "id" : "191",
            "iso" : "sk",
            "name" : "Slovensko"
         },
         "DeliveryCountry" : {
            "eu" : "1",
            "id" : "191",
            "iso" : "sk",
            "name" : "Slovensko"
         }
      },
      "InvoiceEmail" : [],
      "SummaryInvoice" : {
         "vat_base_separate_positive" : {
            "20" : 120
         },
         "vat_separate_negative" : {
            "20" : 0
         },
         "vat_separate_positive" : {
            "20" : 24
         },
         "vat_base_separate_negative" : {
            "20" : 0
         }
      },
      "Tag" : [
         {
            "Tag" : {
               "client_count" : 0,
               "expense_count" : 0,
               "id" : "222",
               "invoice_count" : 1,
               "name" : "2day",
               "user_profile_id" : "393"
            }
         }
      ],
      "Summary" : {
         "discount" : 0,
         "invoice_total" : 144,
         "vat_base_separate" : {
            "20" : 120
         },
         "vat_base_total" : 120,
         "vat_separate" : {
            "20" : 24
         },
         "vat_total" : 24
      },
      "PostStamp" : [],
      "InvoiceItem" : [
         {
            "description" : "",
            "discount" : 0,
            "discount_description" : "Zľava",
            "discount_no_vat" : 0,
            "discount_no_vat_total" : 0,
            "discount_with_vat" : 0,
            "discount_with_vat_total" : 0,
            "hide_in_autocomplete" : null,
            "id" : "1695",
            "invoice_id" : "1275",
            "item_price" : 120,
            "item_price_no_discount" : 120,
            "item_price_vat" : 144,
            "item_price_vat_check" : 144,
            "item_price_vat_no_discount" : 144,
            "name" : "Fiktivna polozka",
            "ordernum" : "0",
            "quantity" : "10",
            "sku" : null,
            "stock_item_id" : "0",
            "tax" : "20",
            "tax_deposit" : "0",
            "unit" : "",
            "unit_price" : 12,
            "unit_price_discount" : 12,
            "unit_price_vat" : 14.4,
            "unit_price_vat_no_discount" : 14.4,
            "user_id" : "384",
            "user_profile_id" : "393"
         }
      ],
      "MyData" : {
         "ico" : "46655034",
         "business_register" : "Bratislava I, odd. Sro, vl.č.81403/B",
         "BankAccount" : [
            {
               "account" : "",
               "bank_code" : "",
               "bank_name" : "FatraBanka",
               "country_id" : "191",
               "default" : "1",
               "iban" : " SK 31 1200 000019 8742637541",
               "id" : "264",
               "show_account" : "1",
               "swift" : "9876"
            },
            {
               "account" : "874267541",
               "bank_code" : "1200",
               "bank_name" : "SuperBanka",
               "country_id" : "191",
               "default" : "",
               "iban" : "",
               "id" : "265",
               "show_account" : "1",
               "swift" : ""
            }
         ],
         "Logo" : "[{\"id\":\"168\",\"model\":\"User\",\"foreign_key\":\"393\",\"dirname\":\"img\",\"basename\":\"9997f862be767814ce9b_393_screen_shot_2018_10_03_at_10_03_19.png\",\"checksum\":\"dd3300a5a4fc754b0f1361baa2ac2e3f\",\"group\":\"logo\",\"default\":\"1\",\"alternative\":null,\"created\":\"2019-01-23 08:37:27\",\"modified\":\"2019-01-23 08:39:56\"}]",
         "zip" : "811 04",
         "Signature" : "{\"id\":\"169\",\"model\":\"User\",\"foreign_key\":\"393\",\"dirname\":\"img\",\"basename\":\"51ee3f8bbd61561eb5f0_393_podpis_1.png\",\"checksum\":\"33b5238616646ca28ebabc02f713a59f\",\"group\":\"signature\",\"default\":\"0\",\"alternative\":null,\"created\":\"2019-01-23 08:37:27\",\"modified\":\"2019-01-23 08:37:27\"}",
         "country" : {
            "eu" : "1",
            "iso" : "sk",
            "id" : "191",
            "name" : "Slovensko"
         },
         "address" : "Pri Suchom mlyne 6",
         "city" : "Bratislava - mestská časť Staré Mesto",
         "company_name" : "superfaktura.sk, s.r.o.",
         "country_id" : "191",
         "dic" : "2023513470",
         "ic_dph" : "SK2023513470",
         "id" : "393",
         "logo_id" : "",
         "logo_key" : "",
         "tax_payer" : "1",
         "travel_agencies" : "0",
         "update_profile" : "0",
         "user_id" : "384",
         "user_profile_id" : "",
         "web" : ""
      },
      "Paypal" : false,
      "InvoicePayment" : [
         {
            "amount" : "120.00",
            "count" : "0",
            "created" : "2019-01-23 00:00:00",
            "document_no" : "",
            "exchange_rate" : "1.00000000000000",
            "home_currency" : "EUR",
            "id" : "184",
            "import_payment_id" : null,
            "invoice_id" : "1275",
            "payment_currency" : "EUR",
            "payment_type" : "transfer",
            "user_id" : "384",
            "user_profile_id" : "393",
            "vat" : "24.00"
         }
      ],
      "UnitCount" : [],
      "Logo" : [
         {
            "alternative" : null,
            "basename" : "9997f862be767814ce9b_393_screen_shot_2018_10_03_at_10_03_19.png",
            "checksum" : "dd3300a5a4fc754b0f1361baa2ac2e3f",
            "created" : "2019-01-23 08:37:27",
            "default" : "1",
            "dirname" : "img",
            "foreign_key" : "393",
            "group" : "logo",
            "id" : "168",
            "model" : "User",
            "modified" : "2019-01-23 08:39:56"
         }
      ],
      "Signature" : {
         "alternative" : null,
         "basename" : "51ee3f8bbd61561eb5f0_393_podpis_1.png",
         "checksum" : "33b5238616646ca28ebabc02f713a59f",
         "created" : "2019-01-23 08:37:27",
         "default" : "0",
         "dirname" : "img",
         "foreign_key" : "393",
         "group" : "signature",
         "id" : "169",
         "model" : "User",
         "modified" : "2019-01-23 08:37:27"
      }
   }
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

## Get invoice PDF

Return invoice PDF file.

### Request
**URL**: `/[{LANGUAGE}/]invoices/pdf/{INVOICE_ID}/token:{TOKEN}`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    -o /tmp/faktura1275.pdf \
    https://moja.superfaktura.sk/slo/invoices/pdf/1275/token:09feb1bd
```    

### Attributes

#### Required
URL parameters:

| name              | type   | description   | default value |
| ----------------- | ------ | ------------- | ------------- | 
| **invoice_id**    | int    | invoice ID    |               |
| **token**         | string | invoice token |               |

#### Optional
URL parameters:  

| name              | type   | description | default value |
| ----------------- | ------ | ----------- | ------------- |
| **language**      | string | language in which the invoice will be created | as set by `pdf_language` (language of document - language above invoice detail in web application) |

For list of available languages see [Value lists > Language list](value-lists.md#language-list).


### Response  
PDF document on success.
Check for HTTP code 404 in case of error.



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

## Send invoice via mail

Sends invoice to specified email address.
Sending emails has a limit of 100 emails / hour.

### Request
**URL**: `/invoices/send`  
**HTTP method**: POST  

```sh
data='{
    "Email":{
        "invoice_id":1285,
        "to":"name.surname@superfaktura.sk",
        "pdf_language":"eng"
    }
}';

curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoices/send
```

### Attributes
### Required

| name             | type     | description   | default value |
| ---------------- | -------- | ------------- | ------------- |
| **invoice_id**   | int      | ID of invoice that will be sent | |
| **to**           | string   | email address to which email will be sent | |

### Optional

| name             | type     | description   | default value |
| ---------------- | -------- | ------------- | ------------- |
| **bcc**          | string[] | list of email addresses to send BCC to | |
| **body**         | string   | message body | &lt;as defined in templates&gt; |
| **cc**           | string[] | list of email addresses to send CC to | |
| **pdf_language** | string   | document language (see [Value lists > Language list](value-lists.md#language-list)) | |
| **subject**      | string   | email subject | &lt;as defined in templates&gt; |

### Response

#### Successfully sent
```json
{
   "error" : 0,
   "error_message" : "",
   "data" : {
      "Invoice" : {
         "bysquare" : "1",
         "cc" : "[]",
         "email" : "name.surname@superfaktura.sk",
         "invoice_id" : "1285",
         "invoice_lang" : "",
         "message" : "Dobrý deň,\n\nv prílohe posielame faktúru č. 2019003.\n\nSuma na úhradu: 37,14 €\nVariabilný symbol: 2019003\nČíslo účtu:  SK 31 1200 000019 8742637541\n\nĎakujeme za úhradu a prajeme príjemný deň.",
         "no-signature" : false,
         "payment_info" : true,
         "paypal" : false,
         "recipient" : "name.surname@superfaktura.sk",
         "subject" : "Faktúra 2019003",
         "trustpay" : null
      }
   }
}
```

#### Sent with CC  
```sh
data='{
    "Email":{
        "bcc":["sft02@centrum.sk"],
        "body":"api body",
        "cc":["sft01@centrum.sk"],
        "invoice_id":1285,
        "pdf_language":"deu",
        "subject":"api subject",
        "to":"test@superfaktura.sk"
    }
}';

curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoices/send
```

```json
{
   "error_message" : "",
   "error" : 0,
   "data" : {
      "Invoice" : {
         "recipient" : "test@superfaktura.sk",
         "paypal" : false,
         "cc" : "[\"sft01@centrum.sk\"]",
         "subject" : "api subject",
         "bysquare" : "1",
         "message" : "api body",
         "payment_info" : true,
         "trustpay" : null,
         "invoice_id" : "1285",
         "invoice_lang" : "deu",
         "email" : "test@superfaktura.sk",
         "no-signature" : false
      }
   }
}
```


#### Invoice not found
```json
{
   "error_message" : "Invoice not found",
   "error" : 1,
   "message" : "Invoice not found"
}
```


#### Invalid recipient email address
```json
{
   "error" : 13,
   "error_message" : "Please insert valid recipient email address."
}
```

#### Any other problem
```json
{
   "error" : 1,
   "error_message" : "Invoice not found",
   "message" : "Invoice not found"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Send invoice via post

Send invoice via post.

### Request
**URL**: `/invoices/post`  
**HTTP method**: POST  

```sh
data='{
    "Post":{
        "delivery_address":"Vymyslena 1",
        "delivery_city":"Bratislava",
        "delivery_country":"Slovakia",
        "delivery_state":"",
        "delivery_zip":"99999",
        "invoice_id":12850
    }
}';

curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoices/post
```

### Attributes
### Required

| name             | type     | description                     | default value |
| ---------------- | -------- | ------------------------------- | ------------- |
| **invoice_id**   | int      | ID of invoice that will be sent |               |

### Optional

| name                  | type   | description                                                      | default value |
| --------------------- | ------ | ---------------------------------------------------------------- | ------------- |
| **delivery_address**  | string | delivery address (are not required, if invoice contains address) |               |
| **delivery_city**     | string | delivery city (are not required, if invoice contains city)       |               |
| **delivery_country**  | string | delivery country (are not required, if invoice contains country) |               |
| **delivery_state**    | string | delivery state (are not required, if invoice contains state)     |               |
| **delivery_zip**      | string | delivery zip (are not required, if invoice contains zip)         |               |

### Response

#### Successfully posted
```json
{
   "error_message" : "",
   "data" : {
      "Invoice" : {
         "amount" : "30.95",
         "amount_paid" : "0.00",
         "client_data" : "{\"Client\":{\"id\":\"431\",\"name\":\"2day, s. r. o.\",\"address\":\"Pri Suchom mlyne 6\",\"ico\":\"44981082\",\"email\":\"\",\"zip\":\"811 04\",\"dic\":\"2022903949\",\"phone\":\"\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"ic_dph\":\"\",\"fax\":\"\",\"country_id\":\"191\",\"state\":\"\",\"delivery_name\":\"Mr. Incognito\",\"delivery_zip\":\"811 04\",\"delivery_city\":\"Bratislava\",\"delivery_address\":\"Pri Vlhkom mlyne 6\",\"delivery_phone\":\"\",\"delivery_country_id\":\"191\",\"delivery_state\":\"\",\"updateClient\":\"0\",\"country\":\"Slovensko\",\"delivery_country\":\"Slovensko\"}}",
         "client_id" : "431",
         "comment" : "",
         "constant" : "",
         "country_exchange_rate" : "1.00000000",
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
         "modified" : "2019-02-04 11:48:54",
         "my_data" : "{\"MyData\":{\"id\":\"393\",\"user_id\":\"384\",\"user_profile_id\":\"\",\"country_id\":\"191\",\"company_name\":\"superfaktura.sk, s.r.o.\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"tax_payer\":\"1\",\"logo_key\":\"\",\"logo_id\":\"\",\"web\":\"\",\"Logo\":\"[{\\\"id\\\":\\\"168\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"393\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"9997f862be767814ce9b_393_screen_shot_2018_10_03_at_10_03_19.png\\\",\\\"checksum\\\":\\\"dd3300a5a4fc754b0f1361baa2ac2e3f\\\",\\\"group\\\":\\\"logo\\\",\\\"default\\\":\\\"1\\\",\\\"alternative\\\":null,\\\"created\\\":\\\"2019-01-23 08:37:27\\\",\\\"modified\\\":\\\"2019-01-23 08:39:56\\\"}]\",\"Signature\":\"{\\\"id\\\":\\\"169\\\",\\\"model\\\":\\\"User\\\",\\\"foreign_key\\\":\\\"393\\\",\\\"dirname\\\":\\\"img\\\",\\\"basename\\\":\\\"51ee3f8bbd61561eb5f0_393_podpis_1.png\\\",\\\"checksum\\\":\\\"33b5238616646ca28ebabc02f713a59f\\\",\\\"group\\\":\\\"signature\\\",\\\"default\\\":\\\"0\\\",\\\"alternative\\\":null,\\\"created\\\":\\\"2019-01-23 08:37:27\\\",\\\"modified\\\":\\\"2019-01-23 08:37:27\\\"}\",\"travel_agencies\":\"0\",\"business_register\":\"Bratislava I, odd. Sro, vl.\\u010d.81403\\/B\",\"BankAccount\":[{\"show_account\":\"1\",\"id\":\"264\",\"default\":\"0\",\"country_id\":\"191\",\"bank_name\":\"FatraBanka\",\"bank_code\":\"\",\"account\":\"\",\"iban\":\" SK 31 1200 000019 8742637541\",\"swift\":\"9876\"},{\"show_account\":\"1\",\"id\":\"265\",\"default\":\"\",\"country_id\":\"191\",\"bank_name\":\"SuperBanka\",\"bank_code\":\"1200\",\"account\":\"8742637541\",\"iban\":\"\",\"swift\":\"\"}],\"update_profile\":\"0\",\"country\":\"Slovensko\"}}",
         "name" : "Faktúra 2019003",
         "order_no" : "",
         "paid" : "0.00",
         "parent_id" : null,
         "paydate" : null,
         "payment_type" : "",
         "proforma_id" : null,
         "recurring" : null,
         "rounding" : "item",
         "sequence_id" : "2815",
         "special_vat_scheme" : null,
         "specific" : "",
         "status" : "1",
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
      }
   },
   "error" : 0
}
```

#### Missing address data
```json
{
   "message" : "Address data error.",
   "error" : 6
}
```

#### Not enough post stamps
```json
{
   "message" : "No post stamps left.",
   "error" : 7
}
```



## Set invoice as "will not be paid"

Set invoice as "will not be paid".
Only works for regular and proforma invoices.

### Request

**URL**: `/invoices/will_not_be_paid/{ID}`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoices/will_not_be_paid/1295
```

### Attributes
#### Required

URL parameters:

| name   | type     | description | default value |
| ------ | -------- | ----------- | ------------- |
| **id** | int      | invoice ID  |               |

#### Optional

none

### Response

#### Successfully marked

```json
{
    "data": {
        "Invoice": {
            "amount": "10.00",
            "amount_paid": "0.00",
            "client_data": "{\"Client\":{\"id\":\"431\",\"name\":\"2day, s. r. o.\",\"address\":\"Pri Suchom mlyne 6\",\"ico\":\"44981082\",\"email\":\"name.surname@superfaktura.sk\",\"zip\":\"811 04\",\"dic\":\"2022903949\",\"phone\":\"\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"ic_dph\":\"\",\"fax\":\"\",\"country_id\":\"191\",\"state\":\"\",\"delivery_name\":\"\",\"delivery_zip\":\"\",\"delivery_city\":\"\",\"delivery_address\":\"\",\"delivery_phone\":\"\",\"delivery_country_id\":\"191\",\"delivery_state\":\"\",\"updateClient\":\"0\",\"country\":\"Slovensko\",\"delivery_country\":\"Slovensko\"}}",
            "client_id": "431",
            "comment": "",
            "constant": "",
            "country_exchange_rate": "1.00000000",
            "created": "2019-02-12 00:00:00",
            "delivery": "2019-02-12 00:00:00",
            "delivery_type": "",
            "demo": "0",
            "deposit": "0.00",
            "discount": "0",
            "due": "2019-02-26",
            "estimate_id": null,
            "exchange_rate": "1.00000000000000",
            "header_comment": "",
            "home_currency": "EUR",
            "id": "1295",
            "import_id": null,
            "import_parent_id": null,
            "import_type": null,
            "internal_comment": null,
            "invoice_currency": "EUR",
            "invoice_no": "7",
            "invoice_no_formatted": "2019007",
            "issued_by": "superfaktura.sk, s.r.o.",
            "issued_by_email": "api@example.com",
            "issued_by_phone": "",
            "issued_by_web": "",
            "items_data": "item 1 description of item 1, ",
            "items_name": null,
            "lang": "slo",
            "mask": "YYYYNNN",
            "modified": "2019-02-18 09:31:47",
            "my_data": "{\"MyData\":{\"id\":\"393\",\"user_id\":\"384\",\"user_profile_id\":\"\",\"country_id\":\"191\",\"company_name\":\"superfaktura.sk, s.r.o.\",\"address\":\"Pri Suchom mlyne 6\",\"city\":\"Bratislava - mestsk\\u00e1 \\u010das\\u0165 Star\\u00e9 Mesto\",\"zip\":\"811 04\",\"ico\":\"46655034\",\"dic\":\"2023513470\",\"ic_dph\":\"SK2023513470\",\"tax_payer\":\"1\",\"logo_key\":\"\",\"logo_id\":\"\",\"web\":\"\",\"Logo\":\"\",\"Signature\":\"\",\"travel_agencies\":\"0\",\"business_register\":\"Bratislava I, odd. Sro, vl.\\u010d.81403\\/B\",\"BankAccount\":[{\"show_account\":\"1\",\"id\":\"264\",\"default\":\"0\",\"country_id\":\"191\",\"bank_name\":\"FatraBanka\",\"bank_code\":\"\",\"account\":\"\",\"iban\":\" SK 31 1200 000019 8742637541\",\"swift\":\"9876\"},{\"show_account\":\"1\",\"id\":\"265\",\"default\":\"\",\"country_id\":\"191\",\"bank_name\":\"SuperBanka\",\"bank_code\":\"1200\",\"account\":\"8742637541\",\"iban\":\"\",\"swift\":\"\"}],\"update_profile\":\"0\",\"country\":\"Slovensko\"}}",
            "name": "1291 - kopia",
            "order_no": "",
            "paid": "0.00",
            "parent_id": null,
            "paydate": null,
            "payment_type": "",
            "proforma_id": null,
            "recurring": null,
            "rounding": "item",
            "sequence_id": "2815",
            "special_vat_scheme": null,
            "specific": "",
            "status": "4",
            "summary_invoice": null,
            "tags": "",
            "tax_document": "0",
            "taxdate": "2019-02-12",
            "token": "b940621e",
            "type": "regular",
            "user_id": "384",
            "user_profile_id": "393",
            "variable": "2019007",
            "vat": "2.00",
            "vat_transfer": "0"
        }
    },
    "error": 0,
    "error_message": "Document marked as \"will not be paid\""
}
```

#### Wrong invoice

```json
{
   "error" : 1,
   "error_message" : "Document can not be canceled"
}
```

#### Insufficient privileges

```json
{
   "message" : "Nemáte právo meniť faktúru",
   "error" : 1,
   "error_message" : "Nemáte právo meniť faktúru"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


## Mark invoice as sent

Mark invoice as sent. If already marked so, will be unmarked.

### Request

**URL**: `/invoices/mark_sent/{ID}`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoices/mark_sent/1295
```

### Attributes
#### Required

URL parameters:

| name   | type     | description | default value |
| ------ | -------- | ----------- | ------------- |
| **id** | int      | invoice ID  |               |

#### Optional

none

### Response


#### Successfully marked

```json
{
   "error_message" : "",
   "marked" : true,
   "error" : 0
}
```

#### Wrong invoice

```json
{
   "error_message" : "Snažíte sa označiť cudziu faktúru",
   "error" : 1
}
```
