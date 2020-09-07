# Cash register

- [Get cash register details](#get-cash-registers-details)

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

## Get cash registers details

Get detailed information about cash registers and its current value status.

### Request

**URL**: `/cash_registers/getDetails`  
**HTTP method**: GET  


```sh
curl -X GET \
     -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=26321' \
     https://moja.superfaktura.sk/cash_registers/getDetails
```

### Response

```json
[
   {
      "CashRegister":{
         "id":"1",
         "user_id":"1",
         "user_profile_id":"1",
         "sequencein_id":"6",
         "sequenceout_id":"7",
         "eet_certificate_id":null,
         "id_provoz":null,
         "name":"cr2",
         "currency":"EUR",
         "description":"My Cash Register",
         "items":"21",
         "total":"106.00"
      }
   },
   {
      "CashRegister":{
         "id":"6",
         "user_id":"1",
         "user_profile_id":"1",
         "sequencein_id":"6",
         "sequenceout_id":"7",
         "eet_certificate_id":"1",
         "id_provoz":"123234",
         "name":"cr1",
         "currency":"EUR",
         "description":"My EET Cash Register",
         "items":"3",
         "total":"7.00"
      }
   }
]
```