# Cash register

- [Get cash register details](#get-cash-registers-details)
- [Get cash register by id](#get-cash-register-by-id)

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


## Get cash register by ID

Get detailed information about cash register by ID.

### Request

**URL**: `/cash_registers/view/{id}`  
**HTTP method**: GET  


```sh
curl -X GET \
     -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=26321' \
     https://moja.superfaktura.sk/cash_registers/view/1
```

### Response

#### Successful
Returns HTTP status 200.

```json
{
  "CashRegister": {
    "currency": "EUR",
    "description": "My Cash Register",
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
```

#### Cash register not found
Returns HTTP status 404.

```json
{
  "error": 1,
  "error_message": "CashRegister with id: 123 not found",
  "message": "CashRegister with id: 123 not found"
}
```

#### Invalid cash register ID
Returns HTTP status 400.

```json
{
  "error": 1,
  "error_message": "Invalid CashRegister id",
  "message": "Invalid CashRegister id"
}
```