# Model Schema

## Packages

| Name | Description |
|:---- |:-----------|
| urdm | The Unified Rare Disease Model (URDM) for NGS data in research and healthcare (v0.9.0, 2021-11-09) |
| urdm_lookups | URDM Lookup tables (v0.9.0, 2021-11-10) |

## Entities

| Name | Description | Package |
|:---- |:-----------|:-------|
| subjects | Persons who are observed, analyzed, examined, investigated, experimented upon, or/and treated in the course of a particular study | urdm |
| study | A detailed examination, analysis, or critical inspection of one or multiple subjects designed to discover facts. | urdm |
| consent | Consent given by a patient to a surgical or medical procedure or participation in a study, examination or analysis after achieving an understanding of the relevant medical facts and the risks involved. | urdm |
| clinical | Findings and circumstances relating to the examination and treatment of a patient. | urdm |
| material | A natural substance derived from living organisms such as cells, tissues, proteins, and DNA. | urdm |
| samplePreparation | A sample preparation for a nucleic acids sequencing assay. | urdm |
| sequencing | The determination of complete (typically nucleotide) sequences, including those of genomes (full genome sequencing, de novo sequencing and resequencing), amplicons and transcriptomes. | urdm |
| files | A set of related records (either written or electronic) kept together. | urdm |
| anatomicalSource | Biological entity that constitutes the structural organization of an individual member of a biological species from which this material was taken. | urdm_lookups |
| ancestry | Population category defined using ancestry informative markers (AIMs) based on genetic/genomic data. | urdm_lookups |
| biospecimenType | The type of material taken from a biological entity for testing, diagnostic, propagation, treatment or research purposes. | urdm_lookups |
| country | A collective generic term that refers here to a wide variety of dependencies, areas of special sovereignty, uninhabited islands, and other entities in addition to the traditional countries or independent states. | urdm_lookups |
| genotypicSex | A biological sex quality inhering in an individual based upon genotypic composition of sex chromosomes. | urdm_lookups |
| inclusionStatus | An indicator that provides information on the current health status of this person. | urdm_lookups |
| labIndication | The explanation for why a test, measurement, or assessment is executed. | urdm_lookups |
| molecularDiagnosis | Gene affected by pathogenic variation that is causal for disease of the patient. | urdm_lookups |
| pathologicalState | The pathological state of the tissue from which this material was derived. | urdm_lookups |
| phenotype | Human Phenotype Ontology (HPO) release v2021-08-02 | urdm_lookups |
| phenotypicSex | An organismal quality inhering in a bearer by virtue of the bearer's physical expression of sexual characteristics. | urdm_lookups |
| releases | The act of making data or other structured information accessible to the public or to the user group of a database. | urdm_lookups |

## Attributes

### Entity: urdm_subjects

Persons who are observed, analyzed, examined, investigated, experimented upon, or/and treated in the course of a particular study

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| subjectID | - | An individual who is the subject of personal data, persons to whom data refers, and from whom data are collected, processed, and stored. | string | True |
| belongsToFamily | - | A domestic group, or a number of domestic groups linked through descent (demonstrated or stipulated) from a common ancestor, marriage, or adoption. | string | False |
| belongsToMother | - | A designation that has some relationship to motherhood. | xref | False |
| belongsToFather | - | Having to do with the father, coming from the father, or related through the father. | xref | False |
| belongsWithFamilyMembers | - | Any individual related biologically or legally to another individual. | mref | False |
| inclusionStatus | - | An indicator that provides information on the current health status of this person. | string | False |
| dateOfBirth | - | The calendar date on which a person was born. | date | False |
| yearOfBirth | - | The year in which a person was born. | int | False |
| dateOfDeath | - | The calendar date of subject's death. | date | False |
| ageAtDeath | - | The age at which death occurred. | decimal | False |
| phenotypicSex | - | An organismal quality inhering in a bearer by virtue of the bearer's physical expression of sexual characteristics. | xref | False |
| genotypicSex | - | A biological sex quality inhering in an individual based upon genotypic composition of sex chromosomes. | xref | False |
| countryOfBirth | - | The country that this person was born in. | xref | False |
| countryOfResidence | - | Country of residence at enrollment. | xref | False |
| ancestry | - | Population category defined using ancestry informative markers (AIMs) based on genetic/genomic data. | xref | False |
| primaryAffiliation | - | The most significant institute for medical consultation and/or study inclusion in context of the genetic disease of this person. | string | False |
| contactPerson | - | A person acting as a channel for communication between groups or on behalf of a group. | string | False |
| contactEmail | - | Email address of the contact person or organization | email | False |
| alternativeIdentifiers | - | A backup sequence of characters used to identify an entity. | string | False |
| firstVisitDate | - | The date for the first patient visit. | date | False |
| belongsWithTwin | - | Either of two offspring born from the same pregnancy. | bool | False |
| fetalStatus | - | Any tissue from a fetus. | bool | False |
| consanguinity | - | Genetic relatedness between individuals who are descendants of at least one common ancestor. | bool | False |
| belongsToStudy | - | Reference to the study or studies in which this person participates. | mref | False |
| belongsWithDataRelease | - | The act of making data or other structured information accessible to the public or to the user group of a database. | mref | False |
| recordMetadata | - | metadata is data that provides information about data. | compound | False |
| comments | - | A written explanation, observation or criticism added to textual material. | text | False |
| dateRecordCreated | - | The date on which the activity or entity is created. | string | False |
| dateRecordUpdated | - | The date (and time) on which report was updated after it had been submitted. | string | False |

### Entity: urdm_study

A detailed examination, analysis, or critical inspection of one or multiple subjects designed to discover facts.

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| studyID | - | A unique proper name or character sequence that identifies this particular study. | string | True |
| name | - | A name that designates this study. | string | False |
| inclusionCriteria | - | The conditions which, if met, make an person eligible for participation in this study. | string | False |
| principleInvestigator | - | The principle investigator or responsible person for this study. | string | False |
| contactInformation | - | An email address for the purpose of contacting the study contact person. | email | False |
| studyDescription | - | A plan specification comprised of protocols (which may specify how and what kinds of data will be gathered) that are executed as part of this study. | text | False |
| startDate | - | The date on which this study began. | date | False |
| completionDate | - | The date on which the concluding information for this study is completed. Usually, this is when the last subject has a final visit, or the main analysis has finished, or any other protocol-defined completion date. | date | False |
| studyStatus | - | The status of a study or trial. | string | False |
| participantsEnrolled | - | An integer specifying the quantity of study subjects enrolled in the study at the current time. | int | False |
| samplesCollected | - | An integer specifying the quantity of samples collected at the current time. | int | False |
| belongsWithDataRelease | - | The act of making data or other structured information accessible to the public or to the user group of a database. | mref | False |
| recordMetadata | - | metadata is data that provides information about data. | compound | False |
| comments | - | A written explanation, observation or criticism added to textual material. | text | False |
| dateRecordCreated | - | The date on which the activity or entity is created. | string | False |
| dateRecordUpdated | - | The date (and time) on which report was updated after it had been submitted. | string | False |

### Entity: urdm_consent

Consent given by a patient to a surgical or medical procedure or participation in a study, examination or analysis after achieving an understanding of the relevant medical facts and the risks involved.

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| consentID | - | A unique proper name or character sequence that identifies this particular signed individual consent. | string | True |
| belongsToSubject | - | An individual who is the subject of personal data, persons to whom data refers, and from whom data are collected, processed, and stored. | xref | False |
| collectedBy | - | Indicates the person, group, or institution who performed the collection act. | string | False |
| signingDate | - | A date specification that designates when this individual consent form was signed. | date | False |
| validFrom | - | Starting date of the validity of this individual consent. | date | False |
| validUntil | - | End date of the validity of this individual consent. | date | False |
| consentWithdrawn | - | An indication that the consent to participate in the study or one or more segments of the study has been revoked. | bool | False |
| dataUsePermission | - | A data item that is used to indicate consent permissions for datasets and/or materials, and relates to the purposes for which datasets and/or material might be used. | string | False |
| dataUseModifiers | - | Data use modifiers indicate additional conditions for use. For instance, a dataset is restricted to investigations into specific diseases or performed at specific geographical locations. | string | False |
| dataUseSpecification | - | Further specification of applied data use permissions and modifiers. For example, a list of countries in case of geographic restrictions or a list of diseases when restricted to disease-specific research. | text | False |
| allowIncidentalFindingRecontact | - | A planned process for a subject agrees not to be informed about any incidental finding. | bool | False |
| allowMatchmaker | - | Permission is given for MatchMaking | bool | False |
| allowRecontacting | - | The procedure of recontacting the patient for specified reasons. This means the patient agrees to be re-identifiable under those circumstances. | bool | False |
| belongsWithDataRelease | - | The act of making data or other structured information accessible to the public or to the user group of a database. | mref | False |
| recordMetadata | - | metadata is data that provides information about data. | compound | False |
| comments | - | A written explanation, observation or criticism added to textual material. | text | False |
| dateRecordCreated | - | The date on which the activity or entity is created. | string | False |
| dateRecordUpdated | - | The date (and time) on which report was updated after it had been submitted. | string | False |

### Entity: urdm_clinical

Findings and circumstances relating to the examination and treatment of a patient.

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| clinicalID | - | A unique proper name or character sequence that identifies this particular clinical examination. | string | True |
| belongsToSubject | - | An individual who is the subject of personal data, persons to whom data refers, and from whom data are collected, processed, and stored. | xref | False |
| affectedStatus | - | Individuals in a pedigree who exhibit the specific phenotype under study. | bool | False |
| dateOfDiagnosis | - | The date on which a diagnosis of disease was made. | date | False |
| ageAtDiagnosis | - | The age (in years), measured from some defined time point (e.g. birth) at which a patient is diagnosed with a disease. | decimal | False |
| ageOfOnset | - | Age (in years) of onset of clinical manifestations related to the disease of the patient. | decimal | False |
| observedPhenotype | - | The outward appearance of the individual. In medical context, these are often the symptoms caused by a disease. | string | False |
| unobservedPhenotype | - | Phenotypes or symptoms that were looked for but not observed, which may help in differential diagnosis or establish incomplete penetrance. | string | False |
| provisionalPhenotype | - | The test or procedure was successfully performed, but the results are borderline and can neither be declared positive / negative nor detected / not detected according to the current established criteria. | string | False |
| clinicalDiagnosis | - | A diagnosis made from a study of the signs and symptoms of a disease. | string | False |
| molecularDiagnosis | - | Gene affected by pathogenic variation that is causal for disease of the patient. | string | False |
| molecularDiagnosisOther | - | Causal variant in HGVS notation with optional classification or free text explaining any other molecular mechanisms involved. | string | False |
| resolved | - | The satisfactory closure of a data item query. | bool | False |
| dateResolved | - | The date (and time) when the adverse event ends or returns to baseline. | date | False |
| belongsToMaterial | - | A unique proper name or character sequence that identifies this particular material. | mref | False |
| belongsWithDataRelease | - | The act of making data or other structured information accessible to the public or to the user group of a database. | mref | False |
| recordMetadata | - | metadata is data that provides information about data. | compound | False |
| comments | - | A written explanation, observation or criticism added to textual material. | text | False |
| dateRecordCreated | - | The date on which the activity or entity is created. | string | False |
| dateRecordUpdated | - | The date (and time) on which report was updated after it had been submitted. | string | False |

### Entity: urdm_material

A natural substance derived from living organisms such as cells, tissues, proteins, and DNA.

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| materialID | - | A unique proper name or character sequence that identifies this particular material. | string | True |
| belongsToSubject | - | An individual who is the subject of personal data, persons to whom data refers, and from whom data are collected, processed, and stored. | xref | False |
| belongsToRequest | - | A sequence of letters, numbers, or other characters that specifically identifies a particular order. | string | False |
| samplingReason | - | The explanation for why a test, measurement, or assessment is executed. | mref | False |
| samplingTimestamp | - | Date and time at which this material was collected. | string | False |
| samplingProtocol | - | The procedure whereby this material was sampled for an analysis. | text | False |
| samplingProtocolDeviation | - | A variation from processes or procedures defined in the sampling protocol. Deviations usually do not preclude the overall evaluability of subject data for either efficacy or safety, and are often acknowledged and accepted in advance by the sponsor. | string | False |
| reasonForSamplingProtocolDeviation | - | The rationale for why a deviation from the sampling protocol has occurred. | text | False |
| biospecimenType | - | The type of material taken from a biological entity for testing, diagnostic, propagation, treatment or research purposes. | xref | False |
| anatomicalSource | - | Biological entity that constitutes the structural organization of an individual member of a biological species from which this material was taken. | xref | False |
| pathologicalState | - | The pathological state of the tissue from which this material was derived. | xref | False |
| biospecimenUsability | - | An indication as to whether a biospecimen is suitable for testing purposes. | string | False |
| alternativeIdentifiers | - | A backup sequence of characters used to identify an entity. | string | False |
| belongsWithDataRelease | - | The act of making data or other structured information accessible to the public or to the user group of a database. | mref | False |
| recordMetadata | - | metadata is data that provides information about data. | compound | False |
| comments | - | A written explanation, observation or criticism added to textual material. | text | False |
| dateRecordCreated | - | The date on which the activity or entity is created. | string | False |
| dateRecordUpdated | - | The date (and time) on which report was updated after it had been submitted. | string | False |

### Entity: urdm_samplePreparation

A sample preparation for a nucleic acids sequencing assay.

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| sampleID | - | A unique proper name or character sequence that identifies this particular sample preparation. | string | True |
| belongsToMaterial | - | A unique proper name or character sequence that identifies this particular material. | xref | False |
| inputAmount | - | Amount of input material in nanogram (ng). | int | False |
| libraryPreparationKit | - | Pre-filled, ready-to-use reagent cartridges intented to improve chemistry, cluster density and read length as well as improve quality (Q) scores for this sample. Reagent components are encoded to interact with the sequencing system to validate compatibility with user-defined applications. | string | False |
| pcrFree | - | Indicates whether a polymerase chain reaction (PCR) was used to prepare this sample. PCR is a method for amplifying a DNA base sequence using multiple rounds of heat denaturation of the DNA and annealing of oligonucleotide primers complementary to flanking regions in the presence of a heat-stable polymerase. | string | False |
| targetEnrichmentKit | - | Indicates which target enrichment kit was used to prepare this sample. Target enrichment is a pre-sequencing DNA preparation step where DNA sequences are either directly amplified (amplicon or multiplex PCR-based) or captured (hybrid capture-based) in order to only focus on specific regions of a genome or DNA sample. | string | False |
| umIsPresent | - | Indicates whether any unique molecular identifiers (UMIs) are present. An UMI barcode is a short nucleotide sequence that is used to identify reads originating from an individual mRNA molecule. | string | False |
| intendedInsertSize | - | In paired-end sequencing, the DNA between the adapter sequences is the insert. The length of this sequence is known as the insert size, not to be confused with the inner distance between reads. So, fragment length equals read adapter length (2x) plus insert size, and insert size equals read lenght (2x) plus inner distance. | int | False |
| intendedReadLength | - | The number of nucleotides intended to be ordered from each side of a nucleic acid fragment obtained after the completion of a sequencing process. | int | False |
| barcode | - | A machine-readable representation of information in a visual format on a surface. | string | False |
| belongsWithDataRelease | - | The act of making data or other structured information accessible to the public or to the user group of a database. | mref | False |
| recordMetadata | - | metadata is data that provides information about data. | compound | False |
| comments | - | A written explanation, observation or criticism added to textual material. | text | False |
| dateRecordCreated | - | The date on which the activity or entity is created. | string | False |
| dateRecordUpdated | - | The date (and time) on which report was updated after it had been submitted. | string | False |

### Entity: urdm_sequencing

The determination of complete (typically nucleotide) sequences, including those of genomes (full genome sequencing, de novo sequencing and resequencing), amplicons and transcriptomes.

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| sequencingID | - | A unique proper name or character sequence that identifies this particular nucleic acid sequencing assay. | string | True |
| belongsToSample | - | A unique proper name or character sequence that identifies this particular sample preparation. | xref | False |
| sequencingDate | - | Date on which this sequencing assay was performed. | date | False |
| sequencingFacilityOrganization | - | An organization that provides sequence determination service | string | False |
| sequencingPlatform | - | The used sequencing platform (i.e. brand, name of a company that produces sequencer equipment). | string | False |
| sequencingInstrumentModel | - | The used product name and model number of a manufacturer's genomic (dna) sequencer. | string | False |
| sequencingMethod | - | Method used to determine the order of bases in a nucleic acid sequence. | string | False |
| averageReadDepth | - | The average number of times a particular locus (site, nucleotide, amplicon, region) was sequenced. | int | False |
| observedReadLength | - | The number of nucleotides successfully ordered from each side of a nucleic acid fragment obtained after the completion of a sequencing process. | int | False |
| observedInsertSize | - | In paired-end sequencing, the DNA between the adapter sequences is the insert. The length of this sequence is known as the insert size, not to be confused with the inner distance between reads. So, fragment length equals read adapter length (2x) plus insert size, and insert size equals read lenght (2x) plus inner distance. | int | False |
| percentageQ30 | - | Percentage of reads with a Phred quality score over 30, which indicates less than a 1/1000 chance that the base was called incorrectly. | decimal | False |
| percentageTR20 | - | Percentage of the target sequence on which 20 or more unique reads were successfully mapped. | decimal | False |
| otherQualityMetrics | - | Other NGS quality control metrics, including but not limited to (i) sequencer metrics such as yield, error rate, density (K/mm2), cluster PF (%) and phas/prephas (%), (ii) alignment metrics such as QM insert size, GC content, QM duplicated reads (%), QM error rate, uniformity/evenness of coverage and maternal cell contamination, and (iii) variant call metrics such as number of SNVs/CNVs/SVs called, number of missense/nonsense variants, common variants (%), unique variants (%), gender match and trio inheritance check. | text | False |
| referenceGenomeUsed | - | The specific build of the human genome used as reference for sequence alignment and variant calling. | string | False |
| belongsWithDataRelease | - | The act of making data or other structured information accessible to the public or to the user group of a database. | mref | False |
| recordMetadata | - | metadata is data that provides information about data. | compound | False |
| comments | - | A written explanation, observation or criticism added to textual material. | text | False |
| dateRecordCreated | - | The date on which the activity or entity is created. | string | False |
| dateRecordUpdated | - | The date (and time) on which report was updated after it had been submitted. | string | False |

### Entity: urdm_files

A set of related records (either written or electronic) kept together.

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| filename | - | The literal identifier for an electronic file. | string | True |
| belongsToSequencing | - | A unique proper name or character sequence that identifies this particular nucleic acid sequencing assay. | mref | False |
| belongsToSubject | - | An individual who is the subject of personal data, persons to whom data refers, and from whom data are collected, processed, and stored. | xref | False |
| server | - | A computer which provides some service for other computers connected to it via a network. | string | False |
| path | - | The specification of a node (file or directory) in a hierarchical file system, usually specified by listing the nodes top-down. | string | False |
| format | - | The format of an electronic file. | string | False |
| size | - | The size of an electronic file in bytes. | int | False |
| dateCreated | - | The date a digital resource was created. | date | False |
| md5 | - | A 32-character hexadecimal number that is computed on a file. | string | False |
| uploaded | - | An indication that a submitted file has successfully been uploaded to a data repository. | bool | False |
| released | - | An indication that a file has been released to the users of a database or data repository. | bool | False |
| invalid | - | An indication that a file has invalid data or is in an invalid format and cannot be submitted to a data repository. | bool | False |
| alternativeFileId | - | A backup sequence of characters used to identify an entity. | string | False |
| belongsWithDataRelease | - | The act of making data or other structured information accessible to the public or to the user group of a database. | mref | False |
| recordMetadata | - | metadata is data that provides information about data. | compound | False |
| comments | - | A written explanation, observation or criticism added to textual material. | text | False |
| dateRecordCreated | - | The date on which the activity or entity is created. | string | False |
| dateRecordUpdated | - | The date (and time) on which report was updated after it had been submitted. | string | False |

### Entity: urdm_lookups_anatomicalSource

Biological entity that constitutes the structural organization of an individual member of a biological species from which this material was taken.

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| value | - | The information contained in a data field. It may represent a numeric quantity, a textual characterization, a date or time measurement, or some other state, depending on the nature of the attribute. | string | True |
| description | - | A written or verbal account, representation, statement, or explanation of something | text | False |
| codesystem | - | A systematized collection of concepts that define corresponding codes. | string | False |
| code | - | A symbol or combination of symbols which is assigned to the members of a collection. | string | False |
| iri | - | A unique symbol that establishes identity of the resource. | hyperlink | False |

### Entity: urdm_lookups_ancestry

Population category defined using ancestry informative markers (AIMs) based on genetic/genomic data.

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| value | - | The information contained in a data field. It may represent a numeric quantity, a textual characterization, a date or time measurement, or some other state, depending on the nature of the attribute. | string | True |
| description | - | A written or verbal account, representation, statement, or explanation of something | text | False |
| codesystem | - | A systematized collection of concepts that define corresponding codes. | string | False |
| code | - | A symbol or combination of symbols which is assigned to the members of a collection. | string | False |
| iri | - | A unique symbol that establishes identity of the resource. | hyperlink | False |

### Entity: urdm_lookups_biospecimenType

The type of material taken from a biological entity for testing, diagnostic, propagation, treatment or research purposes.

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| value | - | The information contained in a data field. It may represent a numeric quantity, a textual characterization, a date or time measurement, or some other state, depending on the nature of the attribute. | string | True |
| description | - | A written or verbal account, representation, statement, or explanation of something | text | False |
| codesystem | - | A systematized collection of concepts that define corresponding codes. | string | False |
| code | - | A symbol or combination of symbols which is assigned to the members of a collection. | string | False |
| iri | - | A unique symbol that establishes identity of the resource. | hyperlink | False |

### Entity: urdm_lookups_country

A collective generic term that refers here to a wide variety of dependencies, areas of special sovereignty, uninhabited islands, and other entities in addition to the traditional countries or independent states.

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| value | - | The information contained in a data field. It may represent a numeric quantity, a textual characterization, a date or time measurement, or some other state, depending on the nature of the attribute. | string | True |
| description | - | A written or verbal account, representation, statement, or explanation of something | text | False |
| codesystem | - | A systematized collection of concepts that define corresponding codes. | string | False |
| code | - | A symbol or combination of symbols which is assigned to the members of a collection. | string | False |
| iri | - | A unique symbol that establishes identity of the resource. | hyperlink | False |

### Entity: urdm_lookups_genotypicSex

A biological sex quality inhering in an individual based upon genotypic composition of sex chromosomes.

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| value | - | The information contained in a data field. It may represent a numeric quantity, a textual characterization, a date or time measurement, or some other state, depending on the nature of the attribute. | string | True |
| description | - | A written or verbal account, representation, statement, or explanation of something | text | False |
| codesystem | - | A systematized collection of concepts that define corresponding codes. | string | False |
| code | - | A symbol or combination of symbols which is assigned to the members of a collection. | string | False |
| iri | - | A unique symbol that establishes identity of the resource. | hyperlink | False |

### Entity: urdm_lookups_inclusionStatus

An indicator that provides information on the current health status of this person.

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| value | - | The information contained in a data field. It may represent a numeric quantity, a textual characterization, a date or time measurement, or some other state, depending on the nature of the attribute. | string | True |
| description | - | A written or verbal account, representation, statement, or explanation of something | text | False |
| codesystem | - | A systematized collection of concepts that define corresponding codes. | string | False |
| code | - | A symbol or combination of symbols which is assigned to the members of a collection. | string | False |
| iri | - | A unique symbol that establishes identity of the resource. | hyperlink | False |

### Entity: urdm_lookups_labIndication

The explanation for why a test, measurement, or assessment is executed.

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| value | - | The information contained in a data field. It may represent a numeric quantity, a textual characterization, a date or time measurement, or some other state, depending on the nature of the attribute. | string | True |
| description | - | A written or verbal account, representation, statement, or explanation of something | text | False |
| codesystem | - | A systematized collection of concepts that define corresponding codes. | string | False |
| code | - | A symbol or combination of symbols which is assigned to the members of a collection. | string | False |
| iri | - | A unique symbol that establishes identity of the resource. | hyperlink | False |

### Entity: urdm_lookups_molecularDiagnosis

Gene affected by pathogenic variation that is causal for disease of the patient.

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| value | - | The information contained in a data field. It may represent a numeric quantity, a textual characterization, a date or time measurement, or some other state, depending on the nature of the attribute. | string | True |
| description | - | A written or verbal account, representation, statement, or explanation of something | text | False |
| codesystem | - | A systematized collection of concepts that define corresponding codes. | string | False |
| code | - | A symbol or combination of symbols which is assigned to the members of a collection. | string | False |
| iri | - | A unique symbol that establishes identity of the resource. | hyperlink | False |

### Entity: urdm_lookups_pathologicalState

The pathological state of the tissue from which this material was derived.

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| value | - | The information contained in a data field. It may represent a numeric quantity, a textual characterization, a date or time measurement, or some other state, depending on the nature of the attribute. | string | True |
| description | - | A written or verbal account, representation, statement, or explanation of something | text | False |
| codesystem | - | A systematized collection of concepts that define corresponding codes. | string | False |
| code | - | A symbol or combination of symbols which is assigned to the members of a collection. | string | False |
| iri | - | A unique symbol that establishes identity of the resource. | hyperlink | False |

### Entity: urdm_lookups_phenotype

Human Phenotype Ontology (HPO) release v2021-08-02

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| value | - | The information contained in a data field. It may represent a numeric quantity, a textual characterization, a date or time measurement, or some other state, depending on the nature of the attribute. | string | True |
| definition | - | A written or verbal account, representation, statement, or explanation of something | text | False |
| codesystem | - | A systematized collection of concepts that define corresponding codes. | string | False |
| code | - | A symbol or combination of symbols which is assigned to the members of a collection. | string | False |
| iri | - | A unique symbol that establishes identity of the resource. | hyperlink | False |

### Entity: urdm_lookups_phenotypicSex

An organismal quality inhering in a bearer by virtue of the bearer's physical expression of sexual characteristics.

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| value | - | The information contained in a data field. It may represent a numeric quantity, a textual characterization, a date or time measurement, or some other state, depending on the nature of the attribute. | string | True |
| description | - | A written or verbal account, representation, statement, or explanation of something | text | False |
| codesystem | - | A systematized collection of concepts that define corresponding codes. | string | False |
| code | - | A symbol or combination of symbols which is assigned to the members of a collection. | string | False |
| iri | - | A unique symbol that establishes identity of the resource. | hyperlink | False |

### Entity: urdm_lookups_releases

The act of making data or other structured information accessible to the public or to the user group of a database.

| Name | Label | Description | Data Type | ID Attribute |
|:---- |:-----|:-----------|:---------|:------------|
| id | - | One or more characters used to identify, name, or characterize the nature, properties, or contents of a thing. | string | True |
| name | - | The words or language units by which a thing is known. | string | False |
| description | - | A written or verbal account, representation, statement, or explanation of something. | text | False |
| date | - | A date of database submission refers to the moment in time in which some information was submitted/received to a database system. | date | False |
| createdBy | - | Indicates the person or authoritative body who brought the item into existence. | string | False |
| numberOfEntriesAdded | - | Determining the number or amount of something (NCIT). A database entry is a single, implicitly structured data item in a table. (SIO) | int | False |
| dataSource | - | The person or authoritative body who provided the information. | string | False |
| releaseComments | - | A notation regarding the decisions, and/or clarification of any information pertaining to data management. | text | False |
