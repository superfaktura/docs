# Tags

- [Add tag](#add-tag)
- [Edit tag](#edit-tag)
- [Get list of tags](#get-list-of-tags)
- [Delete tag](#delete-tag)


## Add tag

### Request

**URL**: `/tags/add`  
**HTTP method**: POST  

```sh
curl -X POST \
    -d 'data={"name":"abc"}' \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/tags/add
```

### Attributes
#### Required

| name     | type   | description | default value |
| -------- | ------ | ----------- | ------------- |
| **name** | string | tag name    |               |

#### Optional
none

### Response

#### Successful creation

Returns HTTP status 201.

```json
{
  "error": 0,
  "message": "Tag bol uložený",
  "tag_id": "1",
  "tag_name": "abc"
}
```

#### Insufficient privileges

Returns HTTP status 403.

```json
{
  "error": 1,
  "error_message": "Nemôžete pridávať tagy",
  "message": "Nemôžete pridávať tagy"
}
```

#### Duplicate name

Returns HTTP status 409.

```json
{
  "error": 1,
  "error_message": "Tento tag už existuje",
  "message": "Tento tag už existuje"
}
```

#### Wrong data

Returns HTTP status 400.

```json
{
  "error": 1,
  "error_message": "Chýbajúce údaje",
  "message": "Chýbajúce údaje"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Edit tag

### Request

**URL**: `/tags/edit/{ID}`  
**HTTP method**: POST  

```sh
data='{"name":"xyz"}';

curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/tags/edit/1
```

### Attributes
#### Required

| name     | type   | description             | default value |
| -------- | ------ | ----------------------- | ------------- |
| **id**   | int    | tag ID (HTTP parameter) |               |
| **name** | string | tag name                |               |

#### Optional
none

### Response

#### Successfully edited

```json
{
  "error": 0,
  "message": "Tag bol uložený",
  "tag_id": "1"
}
```

#### Wrong tag

Returns HTTP status 404.

```json
{
  "error": 1,
  "error_message": "Žiadny tag sa nenašiel",
  "message": "Žiadny tag sa nenašiel"
}
```

#### Bad data

Returns HTTP status 400.

```json
{
  "error": 1,
  "error_message": "Chýbajúce údaje",
  "message": "Chýbajúce údaje"
}
```

#### Insufficient privileges

Returns HTTP status 403.

```json
{
  "error": 1,
  "error_message": "Nemôžete editovať tagy",
  "message": "Nemôžete editovať tagy"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Get list of tags

### Request

**URL**: `/tags/index.json`  
**HTTP method**: GET  

```sh
curl \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/tags/index.json
```

### Attributes

none

### Response

JSON object in form of `key: value`, where `key` is tag ID and `value` is tag name.
The tags belong to logged user profile.
If no tags are found, empty array is returned `[]`.

```json
{
  "1": "abc"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Delete tag

### Request

**URL**: `/tags/delete/{ID}`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    https://moja.superfaktura.sk/tags/delete/1
```

### Attributes
#### Required

URL parameters:

| name     | type   | description | default value |
| -------- | ------ | ----------- | ------------- |
| **id**   | int    | tag ID      |               |

#### Optional

none

### Response

#### Successful deletion

```json
{
  "error": 0,
  "message": "Tag zmazaný"
}
```

#### Wrong tag

Returns HTTP status 404.

```json
{
  "error": 1,
  "error_message": "Žiadny tag sa nenašiel",
  "message": "Žiadny tag sa nenašiel"
}
```

#### Insufficient privileges

Returns HTTP status 403.

```json
{
  "error": 1,
  "error_message": "Nemôžete mazať tagy",
  "message": "Nemôžete mazať tagy"
}
```