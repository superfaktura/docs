# Contact persons

## Add contact person to client

Add new contact person to existing client.

### Request
**URL**: `/contact_people/add/api:1`  
**HTTP method**: POST  

```sh
data='{
    "ContactPerson":{
        "client_id":431,
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
   "state" : "SUCCESS",
   "data" : {
      "ContactPerson" : {
         "modified" : "2019-02-05 08:31:49",
         "user_profile_id" : "393",
         "name" : "John",
         "client_id" : 431,
         "id" : "13",
         "created" : "2019-02-05 08:31:49",
         "user_id" : "384",
         "email" : "john@example.com"
      }
   }
}
```

#### Wrong client

```json
{
   "state" : "ERROR",
   "error" : 1,
   "message" : "Client not found. Please check client_id field."
}
```


#### Insufficient privileges
HTTP status 403

```json
{
   "error" : 1,
   "message" : "Nemôžete pridať kontaktnú osobu",
   "error_message" : "Nemôžete pridať kontaktnú osobu"
}
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


## Delete contact person

Deletes contact person from client.

### Request

**URL**: `/contact_people/delete/{ID}`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
    https://moja.superfaktura.sk/contact_people/delete/16
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
{"error":0}
```
 
#### Wrong contact person

```json
{"error":1}
```


#### Insufficient privileges
HTTP status 403

```json
{
   "error_message" : "Nemôžete vymazať kontaktnú osobu",
   "error" : 1,
   "message" : "Nemôžete vymazať kontaktnú osobu"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


## Get contact people

Get list of contact people for client.

### Request

**URL**: `/contact_people/getContactPeople/{ID}`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
    https://moja.superfaktura.sk/contact_people/getContactPeople/431
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
      "ContactPerson" : {
         "client_id" : "431",
         "created" : "2019-02-05 08:31:49",
         "email" : "john@example.com",
         "id" : "13",
         "modified" : "2019-02-05 08:31:49",
         "name" : "John",
         "phone" : null,
         "user_id" : "384",
         "user_profile_id" : "393"
      }
   },
   {
      "ContactPerson" : {
         "address" : "Pri Suchom mlyne 6",
         "bank_account" : "",
         "bank_account_id" : null,
         "bank_account_prefix" : null,
         "bank_code" : "",
         "city" : "Bratislava - mestská časť Staré Mesto",
         "client" : true,
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
         "email" : "name.surname@superfaktura.sk",
         "fax" : "",
         "iban" : "",
         "ic_dph" : "",
         "ico" : "44981082",
         "id" : "431",
         "modified" : "2019-02-04 12:21:27",
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
      }
   }
]
```
 
#### Wrong client

```json
[
   {
      "ContactPerson" : {
         "client" : true
      }
   }
]
```