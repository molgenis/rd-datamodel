# Model Schema

## Packages

| Name | Description |
|:---- |:-----------|
| rdmodel | The Rare Disease Unified Data Model (v0.0002, 2021-09-07) |

## Entities

| Name | Description | Package |
|:---- |:-----------|:-------|
| personal | Information about the individuals and family members | rdmodel |
| clinical | - | rdmodel |
| samples | Sample metadata including tests performed and results | rdmodel |
| experiments | - | rdmodel |
| files | - | rdmodel |

## Attributes

### Entity: rdmodel_personal

Information about the individuals and family members

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| personalID | - | - | string | True |
| familyID | - | - | string | False |
| maternalID | - | - | string | False |
| paternalID | - | - | string | False |
| linkedFamilyIDs | - | - | string | False |
| dateOfBirth | - | - | date | False |
| yearOfBirth | - | - | string | False |
| dateOfDeath | - | - | date | False |
| ageAtDeath | - | - | int | False |
| inclusionStatus | - | - | string | False |
| claimedSex | - | - | string | False |
| geneticSex | - | - | string | False |
| countryOfBirth | - | - | string | False |
| countryOfResidence | - | - | string | False |
| ancestry | - | - | string | False |
| primaryAffiliation | - | - | string | False |
| affiliatedNetworks | - | - | string | False |
| consanguinity | - | - | bool | False |
| fetalStatus | - | - | bool | False |
| twinStatus | - | - | bool | False |
| altPersonalIDs | - | - | string | False |
| firstContact | - | - | date | False |
| consentStatus | - | - | string | False |
| dateLastUpdated | - | - | datetime | False |

### Entity: rdmodel_clinical
| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| personalID | - | - | string | True |
| clinicalID | - | - | string | False |
| dateOfDiagnosis | - | - | date | False |
| ageAtDiagnosis | - | - | string | False |
| ageOfOnset | - | - | string | False |
| clinicalDiagnosis | - | - | string | False |
| observedPhenotype | - | - | string | False |
| unobservedPhenotype | - | - | string | False |
| molecularDiagnosis | Causal Variant | - | string | False |
| solvedStatus | - | - | bool | False |
| dateSolved | - | - | string | False |
| dateLastUpdated | - | - | datetime | False |

### Entity: rdmodel_samples

Sample metadata including tests performed and results

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| personalID | - | - | string | True |
| sampleID | - | - | string | False |
| alternateID | - | - | string | False |
| materialID | - | - | string | False |
| samplingDate | - | - | date | False |
| materialType | - | - | string | False |
| tissueType | - | - | string | False |
| labIndication | - | - | string | False |
| sampleStatus | - | - | string | False |
| dateLastUpdated | - | - | datetime | False |

### Entity: rdmodel_experiments
| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| personalID | - | - | string | False |
| sampleID | - | - | string | False |
| materialID | - | - | string | False |
| experimentID | - | - | string | False |
| experimentDate | - | - | string | False |
| sequencingCenter | - | - | string | False |
| sequencingPlatform | - | - | string | False |
| sequencingModel | - | - | string | False |
| sequencingType | - | - | string | False |
| prepKit | - | - | string | False |
| enrichmentKit | - | - | string | False |
| barcode | - | - | string | False |
| avgReadDepth | - | - | string | False |
| percentTR20 | - | - | string | False |
| experimentStatus | - | - | string | False |
| batch | - | - | string | False |
| genomeBuild | - | - | string | False |
| dateLastUpdated | - | - | datetime | False |

### Entity: rdmodel_files
| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| personalID | - | - | string | False |
| sampleID | - | - | string | False |
| experimentID | - | - | string | False |
| fileID | - | - | string | False |
| filePath | - | - | string | False |
| fileType | - | - | string | False |
| dateCreated | - | - | string | False |
| md5 | Checksum | - | string | False |
| dateLastUpdated | - | - | datetime | False |
