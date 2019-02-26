# Tags

## Get list of tags

### Request

**URL**: `/tags/index.json`  
**HTTP method**: GET  

```sh
curl \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    http://superfakturag.local/tags/index.json
```

### Attributes

none

### Response

JSON object in form of `key: value`, where `key` is tag ID and `value` is tag name.
The tags belong to logged user profile. 

```json
{
   "2" : "hello",
   "4" : "world",
   "1" : "foo",
   "3" : "bar"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


## Add tag

### Request

**URL**: `/tags/add`  
**HTTP method**: POST  

```sh
curl -X POST \
    -d 'data={"name":"abc"}' \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    http://superfakturag.local/tags/add
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
   "error" : 0,
   "message" : "Tag bol uložený",
   "tag_id" : "235",
   "tag_name" : "abc"
}
```

#### Insufficient privileges

Returns HTTP status 403.

```json
{
   "error" : 1,
   "error_message" : "You cannot add tags",
   "message" : "You cannot add tags"
}
```

#### Duplicate name

Returns HTTP status 409.

```json
{
   "error" : 1,
   "message" : "This tag already exists",
   "error_message" : "This tag already exists"
}
```

#### Wrong data

Returns HTTP status 400.

```json
{
   "error" : 1,
   "message" : "Chýbajúce údaje",
   "error_message" : "Chýbajúce údaje"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


## Edit tag

### Request

**URL**: `/tags/edit/{ID}`  
**HTTP method**: POST  

```sh
data='{"name":"xyz"}';

curl -X POST \
    -d "data=$data" \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    http://superfakturag.local/tags/edit/233
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
   "error" : 1,
   "error_message" : "Tag bol uložený",
   "message" : "Tag bol uložený"
}
```

#### Wrong tag

Returns HTTP status 404.

```json
{
   "error" : 1,
   "error_message" : "No tag found",
   "message" : "No tag found"
}
```

#### Bad data

Returns HTTP status 400.

```json
{
   "error" : 1,
   "error_message" : "Chýbajúce údaje",
   "message" : "Chýbajúce údaje"
}
```

#### Insufficient privileges

Returns HTTP status 403.

```json
{
   "error" : 1,
   "error_message" : "You cannot edit tags",
   "message" : "You cannot edit tags"
}
```



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


## Delete tag

### Request

**URL**: `/tags/delete/{ID}`  
**HTTP method**: GET  

```sh
curl -X GET \
    -H "Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=" \
    http://superfakturag.local/tags/delete/236
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
   "error" : 1,
   "error_message" : "Tag zmazaný",
   "message" : "Tag zmazaný"
}

```

#### Wrong tag

Returns HTTP status 404.

```json
{
   "error" : 1,
   "error_message" : "No tag found",
   "message" : "No tag found"
}
```

#### Insufficient privileges

Returns HTTP status 403.

```json
{
   "error" : 1,
   "error_message" : "You cannot remove tags",
   "message" : "You cannot remove tags"
}
```