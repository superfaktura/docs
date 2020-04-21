import requests
import json

#
# your settings
#
api_url_base = 'https://moja.superfaktura.sk'
auth_email = 'YOUR_EMAIL@SITE.TLD'
auth_api_key = 'API_KEY'
auth_company_id = 'COMPANY_ID'
auth_module = 'YOUR_MODULE_NAME'


# Authorization header
# Please notice Content-Type
# And all parameters in Authorization
headers = {
    'Authorization': "SFAPI email=%s&apikey=%s&company_id=%s&module=%s" % (auth_email, auth_api_key, auth_company_id, auth_module),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}


# In this example we will first create our client
# This is necessary only the first time
clientBody = {
    "Client":{
        "name":"Superfaktura s.r.o.",
        "ico": "46655034"
    }
}


# Invoice body
# Notice we are sending ICO of existing client
invoiceBody ={
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
           "discount": 10,
           "header_comment": "Header comment",
           "internal_comment": "Internal comment",
           "invoice_currency": "NOK",
           "rounding": "item_ext",
           "specific": "SS123456",
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
           "ico": "46655034"
       }
}


# First let's create our client
# Please notice how data is sent.
# Don't send pure JSON.
response = requests.post(api_url_base + "/clients/create", data={"data": json.dumps(clientBody)}, headers=headers)
# check / post-process data
response.headers
response.text


# Once your client is created in your profile, it's enough to send this request to create invoice
#
# Please notice how data is sent.
# Don't send pure JSON.
response = requests.post(api_url_base + "/invoices/create", data={"data": json.dumps(invoiceBody)}, headers=headers)
# check / post-process data
response.headers
response.text