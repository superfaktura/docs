# Export

- [Export invoices](#export-invoices)
- [Get export status](#get-export-status)
- [Download export](#download-export)


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

## Export invoices

Export multiple invoices in PDF or XLS format.

### Request

**URL**: `/exports`  
**HTTP method**: POST

```sh
data='{
    "Invoice":{
        "ids":[1,2,3]
    },
    "Export":{
        "is_msel":true,
        "invoices_pdf":true
    }
}';

curl -X POST \
    -d "data=$data" \
    -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=' \
    https://moja.superfaktura.sk/exports
```

### Attributes
#### Required

##### Export
| name                  | type | description                                         | default value |
| --------------------- | ---- | --------------------------------------------------- | ------------- |
| **msel**              | bool | is multiselect; needs to be `true` (required: true) |               |

##### Invoice
| name                  | type  | description | default value |
| --------------------- | ----- | ----------- | ------------- |
| **ids**               | array | list of IDs |               |

#### Optional

##### Export

| name                      | type | description                        | default value |
| ------------------------- | ---- | ---------------------------------- | ------------- |
| **hide_pdf_payment_info** | bool | hide payment information           |             0 |
| **hide_signature**        | bool | hide signature in invoices         |             0 |
| **invoices_pdf**          | bool | export in PDF format               |             0 |
| **invoices_xls**          | bool | export in XLS format               |             0 |
| **merge_pdf**             | bool | only export merged PDF             |             0 |
| **pdf_lang_default**      | bool | translate documents to default language (SK: Slovak, CZ: Czech) | 0 |
| **pdf_sort_client**       | bool | sort documents by client           |             0 |
| **pdf_sort_date**         | bool | sort documents by date             |             0 |


### Response

#### Successful
HTTP status 200

```json
{
  "Export": {
    "id": 1,
    "type": "invoice_pdf",
    "status": 3,
    "progress": 0,
    "count_total": 0,
    "count_completed": 0
  }
}
```

#### Insufficient privileges
HTTP status 403

```json
{
  "error": 1,
  "message": "Access denied",
  "error_message": "Access denied"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Get export status

Get detailed information about the status of an export by its ID. Export statuses (see [Value lists > Export statuses](value-lists.md#export-statuses))

### Request

**URL**: `/exports/getStatus/{id}`  
**HTTP method**: GET


```sh
curl -X GET \
     -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=26321' \
     https://moja.superfaktura.sk/exports/getStatus/1
```

### Response

#### Successful
HTTP status 200

```json
{
  "Export": {
    "id": 1,
    "type": "invoice_pdf",
    "status": 1,
    "progress": 100,
    "count_total": 50,
    "count_completed": 50
  }
}
```

#### Insufficient privileges
HTTP status 403

```json
{
  "error": 1,
  "message": "Access denied",
  "error_message": "Access denied"
}
```

#### Export not found
HTTP status 404

```json
{
  "error": 1,
  "message": "Export not found",
  "error_message": "Export not found"
}
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


## Download export

Download the completed export by its ID.

> Exports are available for download for two days from the time of completion.

### Request

**URL**: `/exports/download_export/{id}`  
**HTTP method**: GET


```sh
curl -X GET \
     -o /output.zip \
     -H 'Authorization: SFAPI email=api%40example.com&apikey=c0a4cdcdfe98ca660942d60cf7896de6&company_id=26321' \
     https://moja.superfaktura.sk/exports/download_export/1
```

### Response

#### Successful
HTTP status 200

Binary data

#### Insufficient privileges
HTTP status 403

```json
{
  "error": 1,
  "message": "Access denied",
  "error_message": "Access denied"
}
```

#### Export not found
HTTP status 404

```json
{
  "error": 1,
  "message": "Export not found",
  "error_message": "Export not found"
}
```
