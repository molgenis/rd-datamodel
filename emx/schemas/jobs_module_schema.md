# Model Schema

## Packages

| Name | Description |
|:---- |:-----------|
| jobs | Overview and statuses of custom processes run in this database (v0.9.0, 2021-10-28) |
| jobs_results | The outcome of process including analyzed data. |

## Entities

| Name | Description | Package |
|:---- |:-----------|:-------|
| jobs | All log of processes run | jobs |
| processStatus | process status is a process quality that describes the state of a process. | jobs |

## Attributes

### Entity: jobs_jobs

All log of processes run

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| id | - | - | string | True |
| name | - | name or title of the job | string | False |
| description | - | a short description of the job | string | False |
| systemUser | - | An individual who executed the job | string | False |
| start | - | date and time the job started | datetime | False |
| end | - | date and time the job ended | datetime | False |
| status | - | outcome of the job (sucessful, failed, in process) | xref | False |
| outputEntity | - | entity where the job output is stored | string | False |
| comment | - | context of the job or outcome of the run | text | False |

### Entity: jobs_processStatus

process status is a process quality that describes the state of a process.

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| value | - | Value | string | True |
| description | - | Description | string | False |
| codesystem | - | The code system (e.g. ontology) this term belongs to | string | False |
| code | - | The code within the code system | string | False |
| iri | - | The Internationalized Resource Identifier for this term | hyperlink | False |
