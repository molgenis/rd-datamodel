# Model Schema

## Packages

| Name | Description |
|-----|-----|
| rdModel | Rare Disease Shared Data Model (v0.0002, 2021-09-07) |

## Entities

| Name | Description | Package |
|-----|-----|-----|
| patients | - | rdModel |
| clinical | - | rdModel |
| samples | Sample metadata including tests performed and results | rdModel |
| experiments | - | rdModel |
| files | - | rdModel |

## Entity: rdModel_patients

| Name | Label | Description | Data Type | ID Attribute |
|-----|-----|-----|-----|-----|
| umcgID | - | - | string | True |
| familyID | - | - | string | False |
| maternalID | - | - | string | False |
| paternalID | - | - | string | False |
| linkedFamilyIDs | - | - | string | False |
| dateOfBirth | - | - | date | False |
| yearOfBirth | - | - | string | False |
| inclusionStatus | - | - | categorical | False |
| dateOfDeath | - | - | date | False |
| ageAtDeath | - | - | integer | False |
| biologicalSex | - | - | categorical | False |
| biologicalSex | - | - | categorical | False |
| countryOfBirth | - | - | string | False |
| countryOfResidence | - | - | string | False |
| ancestry | - | - | string | False |
| primaryAffiliation | - | - | string | False |
| affiliatedNetworks | - | - | string | False |
| consanguinity | - | - | bool | False |
| is_fetus | - | - | bool | False |
| is_twin | - | - | bool | False |
| altPatientID | - | - | string | False |
| firstContact | - | - | date | False |
| consentStatus | - | - | categoricalmref | False |
| dateLastUpdated | - | - | dateTime | False |

## Entity: rdModel_clinical

| Name | Label | Description | Data Type | ID Attribute |
|-----|-----|-----|-----|-----|
| umcgID | - | - | string | True |
| clinicalID | - | - | string | False |
| dateOfDiagnosis | - | - | date | False |
| ageAtDiagnosis | - | - | string | False |
| ageOfOnset | - | - | string | False |
| confirmedPhenotype | - | - | string | False |
| confirmedPhenotype | - | - | string | False |
| excludedPhenotypeHpo | - | - | string | False |
| molecularDiagnosis | Causal Variant | - | string | False |
| solvedStatus | - | - | bool | False |
| dateSolved | - | - | string | False |
| dateLastUpdated | - | - | dateTime | False |

## Entity: rdModel_samples

Sample metadata including tests performed and results

| Name | Label | Description | Data Type | ID Attribute |
|-----|-----|-----|-----|-----|
| umcgID | - | - | string | True |
| sampleID | - | - | string | False |
| requestID | - | - | string | False |
| dnaID | - | - | string | False |
| testDate | - | - | date | False |
| materialType | - | - | string | False |
| tissueType | - | - | string | False |
| labIndication | - | - | string | False |
| sampleStatus | - | - | string | False |
| dateLastUpdated | - | - | dateTime | False |

## Entity: rdModel_experiments

| Name | Label | Description | Data Type | ID Attribute |
|-----|-----|-----|-----|-----|
| umcgID | - | - | string | False |
| sampleID | - | - | string | False |
| dnaID | - | - | string | False |
| testCode | - | - | string | False |
| testDate | - | - | string | False |
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
| dateLastUpdated | - | - | dateTime | False |

## Entity: rdModel_files

| Name | Label | Description | Data Type | ID Attribute |
|-----|-----|-----|-----|-----|
| umcgID | - | - | string | False |
| sampleID | - | - | string | False |
| testCode | - | - | string | False |
| fileID | - | - | string | False |
| filepath | - | - | string | False |
| filetype | - | - | string | False |
| created | - | - | string | False |
| md5 | Checksum | - | string | False |
| dateLastUpdated | - | - | dateTime | False |
