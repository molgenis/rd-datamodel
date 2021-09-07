# birddata

Reporting Rates of Australian Birds (v0.9, 2022-01-01)

## Model Overview

| package | label | label-nl | Name | Description |
|-----|-----|-----|-----|-----|
| birddata | Species | Soorten | species | Reporting Counts and Rates by Species |
| birddata | Australian States | Australische Staten | states | Australian States and Codes |

## Entity: species

Reporting Counts and Rates by Species

| Name | Label | Description | Data Type | ID Attribute |
|-----|-----|-----|-----|-----|
| birdID | BirdID | Species Identifier | string | True |
| commonName | Common Name | Commonly used name for a species | string | False |
| scientificName | Scientific Name | Scientific name for a species | string | False |
| count | Count | --- | int | False |
| reportingRate | Reporting Rate | Percent reported | decimal | False |

## Entity: states

Australian States and Codes

| Name | Label | Description | Data Type | ID Attribute |
|-----|-----|-----|-----|-----|
| code | --- | --- | string | True |
| category | --- | --- | string | False |
| name | --- | --- | string | False |
