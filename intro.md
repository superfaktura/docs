# Intro

## Authentication

All API requests need authentication header. The header looks like this:
```
Authorization: SFAPI email=YOUR@EMAIL.TLD&apikey=YOURTOKEN
```

Third attribute, which is optional, is `company_id`.
Then the header looks the following:

```
Authorization: SFAPI email=YOUR@EMAIL.TLD&apikey=YOURTOKEN&company_id=YOUR_COMPANY_ID
```

All 3 attributes can be found in your SuperFaktura account (*Tools > API access*)

We recommend to create dedicated API user with role Administrator for using API.
You can manage users in *Settings > Users*.


## POST data format

Data sent via POST method are in `data` key, which holds a JSON object.
Examples of data:

```
data={"key":"value"}

// but more often with nested objects
data={
    "User":{
        "id":1,
        "email":"user@example.com"
    },
    "Invoice":{
        "id":1
    }
}
```

## Base URLs

Base URLs for different SuperFaktura versions.

| Country        | URL                           |
| -------------- | ----------------------------- |
| Slovakia       | https://moja.superfaktura.sk  |
| Czech republic | https://moje.superfaktura.cz  |
| Austria        | https://meine.superfaktura.at |

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

| Header name                      | Description                               | Example                |
| -------------------------------- | ----------------------------------------- | ---------------------- |
| **X-RateLimit-DailyLimit**       | How many requests can you make today      | `X-RateLimit-DailyLimit: 1000` |
| **X-RateLimit-DailyRemaining**   | How many requests remain for today        | `X-RateLimit-DailyRemaining: 876` |
| **X-RateLimit-DailyReset**       | When is the next monthly limit            | `X-RateLimit-DailyReset: 24.12.2030 00:00:00` |
| **X-RateLimit-MonthlyLimit**     | How many requests can you make this month | `X-RateLimit-MonthlyLimit: 30000` |
| **X-RateLimit-MonthlyRemaining** | How many requests remain for this month   | `X-RateLimit-MonthlyRemaining: 13995` |
| **X-RateLimit-MonthlyReset**     | When is the next monthly limit            | `X-RateLimit-MonthlyReset: 01.12.2030 00:00:00` |
| **X-RateLimit-Message**          | Information that you exceeded your API requests (either per day or per month) | `You have exceeded a daily limit of 1000 API requests. You have already made 1000 requests today.` |


## Error messages

Error messages can be translated to other languages, based on user account settings.


## DIČ

In our documentation we provide abbreviations _DIČ_ and _IČ DPH_ to help people unfamiliar with Tax ID and VAT ID.
However, there is a difference between Slovak and Czech DIČ, so we decided to differentiate them with country suffix.

| field    | English | 🇸🇰    | 🇨🇿 | in documentation      |
| -------- | ------- | ------ | --- | --------------------- |
| `ic_dph` | VAT ID  | IČ DPH | DIČ | `DIČ-cz`, `IČ DPH🇸🇰` |
| `dic`    | Tax ID  | DIČ    |   - | `DIČ-sk`              |

(https://en.wikipedia.org/wiki/VAT_identification_number)