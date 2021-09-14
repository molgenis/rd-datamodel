# Model Schema

## Packages

| Name | Description |
|-----|-----|
| birdData | Reporting Rates of Australian Birds (v0.91, 2021-09-14) |
| birdDataRefs | Reference Tables for birdData (v0.9, 2021-09-14) |

## Model Overview

| Name | Description | Package |
|-----|-----|-----|
| species | Reporting Counts and Rates by Species | birdData |
| states | Australian States and Codes | birdDataRefs |

## Entity: birdData_species

Reporting Counts and Rates by Species

### Attributes: birdData_species

| Name | Label | Description | Data Type | ID Attribute |
|-----|-----|-----|-----|-----|
| birdID | BirdID | Species Identifier | string | True |
| commonName | Common Name | Commonly used name for a species | string | False |
| scientificName | Scientific Name | Scientific name for a species | string | False |
| count | Count | - | int | False |
| reportingRate | Reporting Rate | Percent reported | decimal | False |

## Entity: birdDataRefs_states

Australian States and Codes

### Attributes: birdDataRefs_states

| Name | Label | Description | Data Type | ID Attribute |
|-----|-----|-----|-----|-----|
| code | - | - | string | True |
| category | - | - | string | False |
| name | - | - | string | False |
