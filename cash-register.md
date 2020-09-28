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
    "CashRegister": {
      "currency": "CZK",
      "description": "My EET Cash Register",
      "eet_certificate_id": "1",
      "id": "2",
      "id_provoz": "123234",
      "items": "2",
      "name": "CR2-EET",
      "sequencein_id": "6",
      "sequenceout_id": "7",
      "total": "1248.00",
      "user_id": "1",
      "user_profile_id": "1"
    }
  },
  {
    "CashRegister": {
      "currency": "EUR",
      "description": "My Cash Register",
      "eet_certificate_id": null,
      "id": "1",
      "id_provoz": null,
      "items": "3",
      "name": "CR1",
      "sequencein_id": "6",
      "sequenceout_id": "7",
      "total": "106.00",
      "user_id": "1",
      "user_profile_id": "1"
    }
  }
]
```