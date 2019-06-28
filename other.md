# Other API commands

- [Get list of your accounts](#get-list-of-your-accounts)
- [Get user companies data](#get-user-companies-data)
- [Send SMS reminder](#send-sms-reminder)

## Get list of your accounts

Get list of your profiles with detailed information.

### Request

**URL**: `/users/company_switcher`  
**HTTP method**: GET  

```
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/users/company_switcher
```

### Attributes

#### Required
none

#### Optional
none

### Response

```json
{
   "user_name" : null,
   "apikey" : "c0a4cdcdfe98ca660942d60cf7896de6",
   "companies" : [
      {
         "Logo" : {
            "url" : "https://moja.superfaktura.sk/img/no-logo.png",
            "size" : {
               "3" : "width=\"75\" height=\"57\"",
               "bits" : 8,
               "2" : 3,
               "mime" : "image/png",
               "0" : 75,
               "1" : 57
            },
            "0" : {
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
         },
         "UserProfile" : {
            "account_purged" : "0",
            "address" : "Pri Suchom mlyne 6",
            "aff_visitor_id" : null,
            "affiliate_id" : null,
            "business_register" : "Bratislava I, odd. Sro, vl.č.81403/B",
            "bysquare" : "1",
            "city" : "Bratislava - mestská časť Staré Mesto",
            "company_name" : "superfaktura.sk, s.r.o.",
            "company_type" : "ltd",
            "converted" : null,
            "country_id" : "191",
            "created" : "2019-01-23 08:31:56",
            "date_mask" : "d.m.Y",
            "default_constant" : "",
            "default_delivery" : "created",
            "default_payment_type" : null,
            "dic" : "2023513470",
            "disable_footer" : null,
            "due_warning_subject" : null,
            "due_warning_template" : null,
            "expense_rate" : "40.00",
            "external_apikey" : null,
            "fax" : "",
            "header_logo" : "0",
            "help" : "1",
            "home_currency" : "EUR",
            "ic_dph" : "SK2023513470",
            "ico" : "46655034",
            "ico_raw" : "46655034",
            "id" : "393",
            "invoice_comment" : null,
            "invoice_email_subject" : null,
            "invoice_email_template" : "",
            "invoice_header_comment" : null,
            "invoice_item_limit" : "50",
            "invoice_items_name" : null,
            "invoice_no_mask" : "YYYYNNN",
            "invoice_sequence" : "1",
            "invoice_sequence_type" : "yearly",
            "items_per_page" : "50",
            "modified" : "2019-01-23 08:39:56",
            "name" : null,
            "online_payments" : "0",
            "payment_thankyou_subject" : null,
            "payment_thankyou_template" : null,
            "phone" : "",
            "rounding" : "item",
            "setup_finished" : "0",
            "sk_nace" : null,
            "tax_base" : "0.00",
            "tax_payer" : "1",
            "update_taxdate" : "1",
            "user_id" : "384",
            "vat_interval" : "",
            "verification_token" : "3ff77f",
            "web" : "",
            "zip" : "811 04"
         }
      }
   ]
}
``` 


## Get user companies data

Get information about company in which user is currently logged in.
Alternatively return information about all companies, to which user has access (see optional attributes).
This information includes list of bank accounts.

### Request

**URL**: `/users/getUserCompaniesData[/{GET_ALL_COMPANIES}]`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=other.user%40superfaktura.sk&apikey=77e41f72268faa33347b7803b96f08e0&company_id=" \
    https://moja.superfaktura.sk/users/getUserCompaniesData
```

### Attributes
#### Required
none

#### Optional
URL parameters:

| name                  | type    | description | default value |
| --------------------- | ------- | ----------- | ------------- |
| **get_all_companies** | int     | return information about all companies to which user has access (0=no, 1=yes) | 0 |

### Response

#### Successful response

```json
{
   "data" : {
      "1" : {
         "BankAccount" : [
            {
               "account" : "",
               "bank_code" : "",
               "bank_name" : "FatraBanka",
               "country_id" : "191",
               "created" : "2018-01-15 08:00:29",
               "default" : null,
               "iban" : "sk00 1111 2222 3333 4444",
               "id" : "28",
               "modified" : "2018-11-09 11:52:48",
               "show" : "0",
               "swift" : "",
               "user_id" : "3",
               "user_profile_id" : "1"
            },
            {
               "account" : "951214",
               "bank_code" : "",
               "bank_name" : "AbcBank",
               "country_id" : "191",
               "created" : "2018-01-22 11:32:13",
               "default" : null,
               "iban" : "",
               "id" : "30",
               "modified" : "2018-11-09 11:52:48",
               "show" : "0",
               "swift" : "",
               "user_id" : "3",
               "user_profile_id" : "1"
            }
         ],
         "UserProfile" : {
            "address" : "Fakturova 1",
            "business_register" : "Číslo živn.registra: 000-111222, okresný úrad Bratislava",
            "city" : "Bratislava",
            "company_name" : "SuperFaktura",
            "company_type" : "trade",
            "country_id" : "191",
            "dic" : "040903",
            "ic_dph" : "090304",
            "ico" : "123456789",
            "id" : "1",
            "modified" : "2019-01-10 11:20:34",
            "phone" : "0900123456",
            "tax_payer" : "1",
            "user_id" : "3",
            "web" : "https://superfaktura.sk",
            "zip" : "123 45"
         }
      }
   },
   "error_message" : "",
   "error" : 0
}
```

#### No company in your account
```json
{
   "error" : 1,
   "error_message" : "You have no company in your account"
}
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Send SMS reminder

Send reminder before or after the maturity of invoices via SMS.
This feature requires you to have bought SMS messages (*Tools > SMS*).

### Request
**URL**: `/sms/send`  
**HTTP method**: POST  

```sh
data='{
    "invoice_id":"1275",
    "text":"helloworld",
    "phone":"123000456"
}';

curl -X POST \
     -d "data=$data" \
     -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
     https://moja.superfaktura.sk/sms/send
```

### Attributes
#### Required
| name              | type   | description  | default value |
| ----------------- | ------ | ------------ | ------------- |
| **invoice_id**    | int    | invoice ID   |               |
| **text**          | string | message text |               |

#### Optional
| name      | type   | description | default value |
| --------- | ------ | ----------- | ------------- |
| **phone** | string | recipient's phone number | '' (will use phone number from the invoice) | 

### Response

#### Successfully sent
```json
{
   "data" : {
      "text" : "helloworld",
      "phone" : "123000456",
      "invoice_id" : "1275"
   },
   "error" : 0,
   "error_message" : "SMS sent"
}
```

#### Not having prepaid SMS
```json
{
   "message" : "SMS not sent: Nedostatok voľných sms",
   "error" : 3
}
```

#### Empty message
```json
{
   "message" : "SMS not sent: Text sms je prázdny",
   "error" : 3
}
```

#### Invalid phone number
```json
{
   "message" : "SMS not sent: Neplatné tel. číslo",
   "error" : 3
}
```

#### Invoice not found
```json
{
   "message" : "Invoice not found",
   "error" : 2
}
```

#### Empty required fields
```json
{
   "message" : "Invoice ID and text cannot be empty",
   "error" : 1
}
```

```json
{
   "message" : "Text cannot be empty",
   "error" : 1
}
```

```json
{
   "message" : "Invoice ID cannot be empty",
   "error" : 1
}
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - -
