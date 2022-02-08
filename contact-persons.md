# Contact persons

- [Add contact person](#add-contact-person-to-client)
- [Get contact persons](#get-contact-persons)
- [Delete contact person](#delete-contact-person)


## Add contact person to client

Add new contact person to existing client.

### Request
**URL**: `/contact_people/add/api:1`  
**HTTP method**: POST  

```sh
data='{
  "ContactPerson":{
    "client_id":1,
    "name":"John",
    "email":"john@example.com"
  }
}';

curl -X POST \
    -d "data=$data" \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
    https://moja.superfaktura.sk/contact_people/add/api:1
```

### Attributes

#### Required

| name          | type   | description | default value |
| ------------- | ------ | ----------- | ------------- |
| **client_id** | int    | ID of client, whom will be added contact person | |
| **email**     | string | contact person's email |    |
| **name**      | string | contact person's name  |    |

#### Optional

| name      | type   | description | default value |
| --------- | ------ | ----------- | ------------- |
| **phone** | string | contact person's phone |    |

### Response

#### Successfully added person

```json
{
  "data": {
    "ContactPerson": {
      "client_id": 1,
      "created": "2050-01-01 23:59:59",
      "email": "john@example.com",
      "id": "2",
      "modified": "2050-01-01 23:59:59",
      "name": "John",
      "user_id": "1",
      "user_profile_id": "1"
    }
  },
  "state": "SUCCESS"
}
```

#### Wrong client

```json
{
  "error": 1,
  "message": "Klient sa nenašiel. Prosím skontrolujte kľúč client_id.",
  "state": "ERROR"
}
```


#### Insufficient privileges
HTTP status 403

```json
{
  "error": 1,
  "error_message": "Nemôžete pridať kontaktnú osobu",
  "message": "Nemôžete pridať kontaktnú osobu"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Get contact persons

Get list of contact persons for client.

### Request

**URL**: `/contact_people/getContactPeople/{ID}`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
    https://moja.superfaktura.sk/contact_people/getContactPeople/3
```  

### Attributes
#### Required

URL parameters:

| name   | type | description | default value |
| ------ | ---- | ----------- | ------------- |
| **id** | int  | client ID   |               |

#### Optional
none

### Response

#### Successful
```json
[
  {
    "ContactPerson": {
      "client_id": "3",
      "created": "2050-01-01 23:59:59",
      "email": "janko.hrasko@example.com",
      "id": "1",
      "modified": "2050-01-01 23:59:59",
      "name": "Janko Hrasko",
      "phone": null,
      "user_id": "1",
      "user_profile_id": "1"
    }
  },
  {
    "ContactPerson": {
      "account": null,
      "address": "Pri Suchom mlyne 6",
      "bank_account": "",
      "bank_account_id": "0",
      "bank_account_prefix": null,
      "bank_code": "",
      "city": "Bratislava - mestská časť Staré Mesto",
      "client": true,
      "comment": "",
      "country": "Slovensko",
      "country_id": "191",
      "created": "2050-01-01 23:59:59",
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
      "dic": "2023513470",
      "discount": null,
      "distance": null,
      "dont_travel": null,
      "due_date": null,
      "email": "",
      "fax": "",
      "iban": "",
      "ic_dph": "SK2023513470",
      "ico": "46655034",
      "id": "3",
      "modified": "2050-01-01 23:59:59",
      "name": "SuperFaktura, s.r.o.",
      "notices": true,
      "phone": "",
      "state": "",
      "swift": "",
      "tags": null,
      "user_id": "1",
      "user_profile_id": "1",
      "uuid": null,
      "zip": "811 04"
    }
  }
]
```

#### Wrong client

```json
[
  {
    "ContactPerson": {
      "client": true
    }
  }
]
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Delete contact person

Deletes contact person from client.

### Request

**URL**: `/contact_people/delete/{ID}`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
    https://moja.superfaktura.sk/contact_people/delete/1
```  

### Attributes
#### Required

URL parameters:

| name   | type | description | default value |
| ------ | ---- | ----------- | ------------- |
| **id** | int  | contact ID  |               |

#### Optional
none

### Response

#### Successful deletion
```json
{
  "error": 0
}
```


#### Wrong contact person

```json
{
  "error": 1
}
```


#### Insufficient privileges
HTTP status 403

```json
{
  "error": 1,
  "error_message": "Nemôžete vymazať kontaktnú osobu",
  "message": "Nemôžete vymazať kontaktnú osobu"
}
``` 