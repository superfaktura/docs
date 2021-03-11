# FAQ


## How do I select changed or paid documents?

Through API you can retrieve list of invoices, which were changed (any kind of change - edited, assigned payment, sent, ...)
for selected interval of time.

Example of filtering invoices changed during last hour:

```
curl -X GET \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
    https://moja.superfaktura.sk/invoices/index.json/modified:11/type:regular
```


We recommend to use one of these options to filter by modification time:

| value  | description                                                                       |
| ------ | --------------------------------------------------------------------------------- |
| **1**  | today                                                                             |
| **2**  | yesterday                                                                         |
| **3**  | since – to (you also need to specify `modified_since` and `modified_to`)          |
| **11** | last hour (if it's 8:36, documents modified between 7:36 – 8:36 will be found)    |
| **12** | current hour (if it's 8:36, documents modified between 8:00 - 8:36 will be found) |

Information whether invoice is paid can be retrieved from `Invoice -> status`.
For possible values of status see [Value lists > Invoice statuses](value-lists.md#invoice-statuses).

Invoice list returns complete invoice data. There is no need to make additional requests to get invoice details.






## How do I get IDs mentioned in the docs?

When the documentation mentions "invoice ID" as a parameter,
you get it from response JSON object - see e.g. "Get list of invoices".
 
See example responses to get an idea which objects return what attributes.


## My sequence masks use different letters than in your examples

Sequence mask depends on language. You might see:
- `YYYYNNN` (English),
- `JJJJNNN` (German),
- `RRRRCCC` (Slovak / Czech).


## My error messages are different from those in examples

Error messages might be localized based on your account settings.
Thus you might see English / Czech / Slovak error messages.


## Have you got any testing account?

No. You can however create a new company - fill just VAT ID (or Tax ID in Slovak version) (leave ID (IČO) empty),
and you get 30 days free premium account.
If you need more time for testing, you can always write us an email :-)


## How many requests can I make?

In accordance with FUP, you can make 1000 requests per day, or 30&nbsp;000 per month.
After reaching the limit all GET requests will be blocked.

Read more about this in section 5.11 https://www.superfaktura.sk/podmienky-pouzivania/.


## I don't get any response for my requests

Most probably you exceeded API requests limit.
Read more about this in section 5.11 https://www.superfaktura.sk/podmienky-pouzivania/.


## How do I add tags to an entity?

By entity we mean Invoice, Expense and Client.
You need to add `Tag` key to your request.


Normally if you want to save Client, request get data like this:
```sh
data='{
  "Client": {
    "name": "Jozko Mrkvicka"
  }
}';
```

When you want to add tags to this client, you modify it like so:
```sh
data='{
  "Client": {
    "name": "Jozko Mrkvicka"
  },
  "Tag": {
    "Tag": [123, 456]
  }
}';
```

Notice that 123 and 456 are tag IDs, not tag names.
So the following example is *incorrect* and will *not* save your tags.

```sh
data='{
  "Client": {
    "name": "Jozko Mrkvicka"
  },
  "Tag": {
    "Tag": ["tag1", "tag2"]
  }
}';
```

Get list of your tags via `/tags/index.json` (*Tags > Get list of tags*).



## I did not receive response. What do I do?

In case invoice creation did not return response - because of Internet failure, timeout or similar - it's possible to obtain response for this request and prevent duplicate creation of the same invoice.

You can get a unique identifier (not `invoice_id`).
This identifier is created on client side.
Its maximum length is 32 characters.
You can store there any original token you choose.


**Steps:**
1. build invoice data
2. calculate checksum from data (preferably with unique piece of data - like order number)
3. set `data[checksum]` in request


If you fail to receive response, you can then call `/api_logs/getResponseByChecksum/CHECKSUM`.
Response contains original response, which you didn't receive for the first time.
Original response is possible to get for requests up to 3 months ago.
`getResponseByChecksum` has to be checked for possible error response as well :)


**Example:**  
This example extends the minimal example of [invoice creation](invoice.md#add-invoice).

```
data='{
    "checksum": "MY-UNIQUE-IDENTIFIER",
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

#
# This request won't return response
#
curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/invoices/create


#
# Let's request the original response
# You can actually try it even if the original responds successfully
#
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/api_logs/getResponseByChecksum/MY-UNIQUE-IDENTIFIER

#
# Based on the result you can repeat creating the invoice
# or not, if it was successfully created the first time
#
```

## Do you have a testing environment?

Yes, you can use our [Slovak 🇸🇰](https://sandbox.superfaktura.sk/)
or [Czech 🇨🇿](https://sandbox.superfaktura.cz/) **sandbox**.