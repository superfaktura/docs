# Intro

## Authentication

All API requests need authentication header. The header looks like this:

```text
Authorization: SFAPI email=YOUR@EMAIL.TLD&apikey=YOURTOKEN&module=MODULE
```

Fourth attribute, which is optional, is `company_id`.
Then the header looks the following:

```text
Authorization: SFAPI email=YOUR@EMAIL.TLD&apikey=YOURTOKEN&module=MODULE&company_id=YOUR_COMPANY_ID
```

Attributes `email`, `apikey` and `company_id` can be found in your SuperFaktura account (*Tools > API access*).  
Attribute `module` is name of your API module. If you are using a 3rd party module, use its name - e.g. `WordPress 5.2.3 (WC 3.8.0, WC SF 1.9.17)`.
If you are making your own module, use some descriptive name, such as `MyCustomModule 1.0`.

All values need to be URL encoded.
So for example email `hello+world@example.com` will become `hello%2Bworld%40example.com`.

| Attribute  | required | Can be found in SuperFaktura? |
| ---------- | -------- | ----------------------------- |
| email      | ✅ yes   | ✅ yes                        |
| apikey     | ✅ yes   | ✅ yes                        |
| module     | ✅ yes   | ❌ no                         |
| company_id | ❌ no    | ✅ yes                        |

We recommend to create dedicated API user with role Administrator for using API.
You can manage users in *Settings > Users*.

## POST data format

POST requests support two **Content-Type** options:

1. `application/json`
2. `application/x-www-form-urlencoded; charset=UTF-8`

### Option 1: application/json

You can send request data as a standard JSON body.

Example:

```json
{
    "Invoice": {
        "name": "Example"
    },
    "Client": {
        "name": "test & company a.s."
    }
}
```

When using `application/json`, special characters such as `&` are part of the JSON string value and do not need any special handling beyond valid JSON encoding.

### Option 2: application/x-www-form-urlencoded; charset=UTF-8

You can also send request data in the `data` form field as a JSON string.

When using `application/x-www-form-urlencoded; charset=UTF-8`, the `data` parameter must be properly URL encoded by your HTTP client. This is important especially for special characters such as `&`, `=`, `+` and `%`, which have special meaning in form encoding.

How to form data:

1. create JSON from data you want to send
2. serialize this JSON to string
3. URL encode JSON string data
4. assign this string to POST `data` parameter

For example, this JSON payload:

```json
{
    "Client": {
        "name": "test & company a.s."
    }
}
```

is serialized to this JSON string:

```text
{"Client":{"name":"test & company a.s."}}
```

and then sent as the `data` form field in URL-encoded form, for example:

```text
data=%7B%22Client%22%3A%7B%22name%22%3A%22test%20%26%20company%20a.s.%22%7D%7D
```

In this example, the `&` character is encoded as `%26`. If the `data` parameter is not URL encoded properly, the `&` character may be interpreted as a form field separator and the payload can be corrupted.

## Base URLs

Base URLs for different SuperFaktura versions.

| Country        | URL                               |
| -------------- | --------------------------------- |
| Slovakia       | <https://moja.superfaktura.sk>    |
| Czech republic | <https://moje.superfaktura.cz>    |
| Austria        | <https://meine.superfaktura.at>   |
| Sandbox (SK)   | <https://sandbox.superfaktura.sk> |
| Sandbox (CZ)   | <https://sandbox.superfaktura.cz> |

## Data types

### Date

When some attribute / parameter is of type `date`, use format `YYYY-MM-DD`.

### String - base64 encoded

When you should provide a base64 encoded string (usually searching term),
you must also replace special characters. This is specially true in `GET` requests.

| Character | Replacement |
| --------- | ----------- |
| `+`       | `-`         |
| `/`       | `_`         |
| `=`       | `,`         |

## Limit headers

You can get information about API requests limit with the following headers:

| Header name                      | Description                               | Example                                         |
| -------------------------------- | ----------------------------------------- | ----------------------------------------------- |
| **X-RateLimit-DailyLimit**       | How many requests can you make today      | `X-RateLimit-DailyLimit: 1000`                  |
| **X-RateLimit-DailyRemaining**   | How many requests remain for today        | `X-RateLimit-DailyRemaining: 876`               |
| **X-RateLimit-DailyReset**       | When the daily limit will be reset        | `X-RateLimit-DailyReset: 24.12.2030 00:00:00`   |
| **X-RateLimit-MonthlyLimit**     | How many requests can you make this month | `X-RateLimit-MonthlyLimit: 30000`               |
| **X-RateLimit-MonthlyRemaining** | How many requests remain for this month   | `X-RateLimit-MonthlyRemaining: 13995`           |
| **X-RateLimit-MonthlyReset**     | When is the next monthly limit            | `X-RateLimit-MonthlyReset: 01.12.2030 00:00:00` |
| **X-RateLimit-Message**          | Information that you exceeded your API requests (either per day or per month) | `You have exceeded a daily limit of 1000 API requests. You have already made 1000 requests today.` |

## Error messages

Error messages can be translated to other languages, based on user account settings.

## DIČ

In our documentation we provide abbreviations *DIČ* and *IČ DPH* to help people unfamiliar with Tax ID and VAT ID.
However, there is a difference between Slovak and Czech DIČ, so we decided to differentiate them with country suffix.

| field    | English | 🇸🇰     | 🇨🇿  | in documentation      |
| -------- | ------- | ------ | --- | --------------------- |
| `ic_dph` | VAT ID  | IČ DPH | DIČ | `DIČ-cz`, `IČ DPH🇸🇰`  |
| `dic`    | Tax ID  | DIČ    |   - | `DIČ-sk`              |

(<https://en.wikipedia.org/wiki/VAT_identification_number>)
