# Model Schema

## Packages

| Name | Description | Parent |
|:---- |:-----------|:------|
| umdm | The Unified Molgenis Data Model (UMDM) (v1.1.1, 2022-02-17) | - |
| umdm_lookups | Lookup tables for the Unified Molgenis Data Model (UMDM) (v1.1.0, 2022-02-07) | umdm |

## Entities

| Name | Description | Package |
|:---- |:-----------|:-------|
| subjects | Persons who are observed, analyzed, examined, investigated, experimented upon, or/and treated in the course of a particular study | umdm |
| studies | A detailed examination, analysis, or critical inspection of one or multiple subjects designed to discover facts. | umdm |
| consent | Consent given by a patient to a surgical or medical procedure or participation in a study, examination or analysis after achieving an understanding of the relevant medical facts and the risks involved. | umdm |
| clinical | Findings and circumstances relating to the examination and treatment of a patient. | umdm |
| samples | A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a material) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. | umdm |
| samplePreparation | A sample preparation for a nucleic acids sequencing assay. | umdm |
| sequencing | The determination of complete (typically nucleotide) sequences, including those of genomes (full genome sequencing, de novo sequencing and resequencing), amplicons and transcriptomes. | umdm |
| files | A set of related records (either written or electronic) kept together. | umdm |
| cohorts | A group of individuals, identified by a common characteristic. | umdm |
| labProcedures | Any procedure that involves testing or manipulating a sample of blood, urine, or other body substance in a laboratory setting. | umdm |
| organizations | Organization information standardized to the Research Organization Registry (ROR) | umdm |
| releases | The act of making data or other structured information accessible to the public or to the user group of a database. | umdm |
| samplingProtocols | Describes the procedure whereby biological samples for an experiment are sourced. | umdm |
| attributeTemplateDefault | attribute template where value is the primary key | umdm_lookups |
| attributeTemplateCode | attribute template where code is the primary key | umdm_lookups |
| anatomicalSource | Anatomical Source (FAIR Genomes, v1.1) | umdm_lookups |
| ancestry | Ancestry (FAIR Genomes, v1.1) | umdm_lookups |
| biospecimenType | Biospecimen Type (FAIR Genomes, v1.1) | umdm_lookups |
| country | Country (FAIR Genomes, v1.1) | umdm_lookups |
| dataUseModifiers | A data item that is used to indicate consent permissions for datasets and/or materials, and relates to the purposes for which datasets and/or material might be used. | umdm_lookups |
| dataUsePermissions | Data Use Permissions (FAIR Genomes, v1.1) | umdm_lookups |
| diagnosisConfirmationStatuses | The satisfactory closure of a data item query. | umdm_lookups |
| diseases | Diseases (FAIR Genomes, v1.1) | umdm_lookups |
| fileStatus | The condition for an electronic file relative to the current data or file processing step. | umdm_lookups |
| genomeAccessions | Genome Accessions (FAIR Genomes, v1.1) | umdm_lookups |
| genderIdentity | A person's concept of self as being male and masculine or female and feminine, or ambivalent, based in part on physical characteristics, parental responses, and psychological and social pressures. It is the internal experience of gender role. A person's sense of self as a member of a particular gender. | umdm_lookups |
| genderAtBirth | Assigned gender is one's gender which was assigned at birth, typically by a medical and/or legal organization, and then later registered with other organizations. Such a designation is typically based off of the superficial appearance of external genitalia present at birth. | umdm_lookups |
| genotypicSex | Genotypic Sex (FAIR Genomes, v1.1) | umdm_lookups |
| inclusionCriteria | Inclusion Criteria (FAIR Genomes, v1.1) | umdm_lookups |
| molecularDiagnosis | Molecular Diagnosis (FAIR Genomes, v1.1) | umdm_lookups |
| ngsKits | NGS Kits (FAIR Genomes, v1.1) | umdm_lookups |
| pathologicalState | pathological state (FAIR Genomes, v1.1) | umdm_lookups |
| phenotype | Human Phenotype Ontology (HPO, v2021-08-02) | umdm_lookups |
| samplingReason | The explanation for why a test, measurement, or assessment is executed. | umdm_lookups |
| sequencingInstrumentModels | Sequencing instrument models (FAIR Genomes, v1.1) | umdm_lookups |
| sequencingMethods | Sequencing methods (FAIR Genomes, v1.1) | umdm_lookups |
| sequencingPlatform | Sequencing platforms (FAIR Genomes, v1.1) | umdm_lookups |
| studyStatus | The status of a study or trial. | umdm_lookups |
| subjectStatus | A findings domain that contains general subject characteristics that are evaluated periodically to determine if they have changed. | umdm_lookups |

## Attributes

### Entity: umdm_subjects

Persons who are observed, analyzed, examined, investigated, experimented upon, or/and treated in the course of a particular study

| Name | Label | Description | Data Type |
|:---- |:-----|:-----------|:---------|
| subjectID&#8251; | - | An individual who is the subject of personal data, persons to whom data refers, and from whom data are collected, processed, and stored. | string |
| belongsToFamily | - | A domestic group, or a number of domestic groups linked through descent (demonstrated or stipulated) from a common ancestor, marriage, or adoption. | string |
| belongsToMother | - | A designation that has some relationship to motherhood. | xref |
| belongsToFather | - | Having to do with the father, coming from the father, or related through the father. | xref |
| belongsWithFamilyMembers | - | Any individual related biologically or legally to another individual. | mref |
| subjectStatus | - | A findings domain that contains general subject characteristics that are evaluated periodically to determine if they have changed. | xref |
| dateOfBirth | - | The calendar date on which a person was born. | date |
| yearOfBirth | - | The year in which a person was born. | int |
| dateOfDeath | - | The calendar date of subject's death. | date |
| yearOfDeath | - | The year in which an individual derived. | int |
| ageAtDeath | - | The age at which death occurred. | decimal |
| genderIdentity | - | A person's concept of self as being male and masculine or female and feminine, or ambivalent, based in part on physical characteristics, parental responses, and psychological and social pressures. It is the internal experience of gender role. A person's sense of self as a member of a particular gender. | xref |
| genderAtBirth | - | Assigned gender is one's gender which was assigned at birth, typically by a medical and/or legal organization, and then later registered with other organizations. Such a designation is typically based off of the superficial appearance of external genitalia present at birth. | xref |
| genotypicSex | - | A biological sex quality inhering in an individual based upon genotypic composition of sex chromosomes. | xref |
| countryOfBirth | - | The country that this person was born in. | xref |
| countryOfResidence | - | Country of residence at enrollment. | xref |
| ancestry | - | Population category defined using ancestry informative markers (AIMs) based on genetic/genomic data. | xref |
| affiliation | - | A formal association between entities. | compound |
| primaryOrganization | - | The most significant institute for medical consultation and/or study inclusion in context of the genetic disease of this person. | xref |
| contactPerson | - | A person acting as a channel for communication between groups or on behalf of a group. | string |
| contactEmail | - | Email address of the contact person or organization | email |
| alternativeIdentifiers | - | A backup sequence of characters used to identify an entity. | string |
| firstVisitDate | - | The date for the first patient visit. | date |
| belongsWithTwin | - | Either of two offspring born from the same pregnancy. | bool |
| fetalStatus | - | Any tissue from a fetus. | bool |
| consanguinity | - | Genetic relatedness between individuals who are descendants of at least one common ancestor. | bool |
| belongsToStudy | - | Reference to the study or studies in which this person participates. | mref |
| belongsToCohort | - | A group of individuals, identified by a common characteristic. | mref |
| belongsToDataRelease | - | The act of making data or other structured information accessible to the public or to the user group of a database. | mref |
| recordMetadata | - | metadata is data that provides information about data. | compound |
| comments | - | A written explanation, observation or criticism added to textual material. | text |
| dateRecordCreated | - | The date on which the activity or entity is created. | datetime |
| recordCreatedBy | - | Indicates the person or authoritative body who brought the item into existence. | string |
| dateRecordUpdated | - | The date (and time) on which report was updated after it had been submitted. | datetime |
| wasUpdatedBy | - | An entity which is updated by another entity or an agent. | string |

### Entity: umdm_studies

A detailed examination, analysis, or critical inspection of one or multiple subjects designed to discover facts.

| Name | Label | Description | Data Type |
|:---- |:-----|:-----------|:---------|
| studyID&#8251; | - | A unique proper name or character sequence that identifies this particular study. | string |
| studyAcronym | - | The non-unique initials or abbreviated name used for identification. | string |
| studyName | - | A name that designates this study. | string |
| inclusionCriteria | - | The conditions which, if met, make an person eligible for participation in this study. | mref |
| principleInvestigator | - | An investigator who is responsible for all aspects of the conduct of a study. | string |
| contactPerson | - | Name of study contact. | string |
| contactEmail | - | A text string identifier for a location to which e-mail for the study contact can be delivered. | email |
| studyDescription | - | A plan specification comprised of protocols (which may specify how and what kinds of data will be gathered) that are executed as part of this study. | text |
| studyStartDate | - | The date on which this study began. | date |
| studyCompletionDate | - | The date on which the concluding information for this study is completed. Usually, this is when the last subject has a final visit, or the main analysis has finished, or any other protocol-defined completion date. | date |
| currentStudyStatus | - | The status of a study or trial. | mref |
| numberOfSubjectsEnrolled | - | An integer specifying the quantity of study subjects enrolled in the study at the current time. | int |
| samplesCollected | - | An integer specifying the quantity of samples collected at the current time. | int |
| belongsToDataRelease | - | The act of making data or other structured information accessible to the public or to the user group of a database. | mref |
| recordMetadata | - | metadata is data that provides information about data. | compound |
| comments | - | A written explanation, observation or criticism added to textual material. | text |
| dateRecordCreated | - | The date on which the activity or entity is created. | datetime |
| recordCreatedBy | - | Indicates the person or authoritative body who brought the item into existence. | string |
| dateRecordUpdated | - | The date (and time) on which report was updated after it had been submitted. | datetime |
| wasUpdatedBy | - | An entity which is updated by another entity or an agent. | string |

### Entity: umdm_consent

Consent given by a patient to a surgical or medical procedure or participation in a study, examination or analysis after achieving an understanding of the relevant medical facts and the risks involved.

| Name | Label | Description | Data Type |
|:---- |:-----|:-----------|:---------|
| consentID&#8251; | - | A unique proper name or character sequence that identifies this particular signed individual consent. | string |
| belongsToSubject | - | An individual who is the subject of personal data, persons to whom data refers, and from whom data are collected, processed, and stored. | xref |
| collectedBy | - | Indicates the person, group, or institution who performed the collection act. | string |
| signingDate | - | A date specification that designates when this individual consent form was signed. | date |
| validUntil | - | End date of the validity of this individual consent. | date |
| consentWithdrawn | - | An indication that the consent to participate in the study or one or more segments of the study has been revoked. | bool |
| dataUsePermission | - | A data item that is used to indicate consent permissions for datasets and/or materials, and relates to the purposes for which datasets and/or material might be used. | mref |
| dataUseModifiers | - | Data use modifiers indicate additional conditions for use. For instance, a dataset is restricted to investigations into specific diseases or performed at specific geographical locations. | mref |
| dataUseSpecification | - | Further specification of applied data use permissions and modifiers. For example, a list of countries in case of geographic restrictions or a list of diseases when restricted to disease-specific research. | text |
| allowIncidentalFindingRecontact | - | A planned process for a subject agrees not to be informed about any incidental finding. | bool |
| allowMatchmaker | - | Permission is given for MatchMaking | bool |
| allowRecontacting | - | The procedure of recontacting the patient for specified reasons. This means the patient agrees to be re-identifiable under those circumstances. | bool |
| belongsToDataRelease | - | The act of making data or other structured information accessible to the public or to the user group of a database. | mref |
| recordMetadata | - | metadata is data that provides information about data. | compound |
| comments | - | A written explanation, observation or criticism added to textual material. | text |
| dateRecordCreated | - | The date on which the activity or entity is created. | datetime |
| recordCreatedBy | - | Indicates the person or authoritative body who brought the item into existence. | string |
| dateRecordUpdated | - | The date (and time) on which report was updated after it had been submitted. | datetime |
| wasUpdatedBy | - | An entity which is updated by another entity or an agent. | string |

### Entity: umdm_clinical

Findings and circumstances relating to the examination and treatment of a patient.

| Name | Label | Description | Data Type |
|:---- |:-----|:-----------|:---------|
| clinicalID&#8251; | - | A unique proper name or character sequence that identifies this particular clinical examination. | string |
| belongsToSubject | - | An individual who is the subject of personal data, persons to whom data refers, and from whom data are collected, processed, and stored. | xref |
| affectedStatus | - | Individuals in a pedigree who exhibit the specific phenotype under study. | bool |
| dateOfDiagnosis | - | The date on which a diagnosis of disease was made. | date |
| ageAtDiagnosis | - | The age (in years), measured from some defined time point (e.g. birth) at which a patient is diagnosed with a disease. | decimal |
| ageOfOnset | - | Age (in years) of onset of clinical manifestations related to the disease of the patient. | decimal |
| observedPhenotype | - | The outward appearance of the individual. In medical context, these are often the symptoms caused by a disease. | mref |
| unobservedPhenotype | - | Phenotypes or symptoms that were looked for but not observed, which may help in differential diagnosis or establish incomplete penetrance. | mref |
| provisionalPhenotype | - | The test or procedure was successfully performed, but the results are borderline and can neither be declared positive / negative nor detected / not detected according to the current established criteria. | mref |
| clinicalDiagnosis | - | A diagnosis made from a study of the signs and symptoms of a disease. | mref |
| molecularDiagnosis | - | Gene affected by pathogenic variation that is causal for disease of the patient. | mref |
| molecularDiagnosisOther | - | Causal variant in HGVS notation with optional classification or free text explaining any other molecular mechanisms involved. | text |
| statusOfDiagnosis | - | A condition or state at a particular time. | xref |
| dateDiagnosisConfirmed | - | The particular day, month and year an event has happened or will happen. | date |
| belongsToSample | - | Name or other identifier of an entry from a biosample database. | mref |
| belongsToDataRelease | - | The act of making data or other structured information accessible to the public or to the user group of a database. | mref |
| recordMetadata | - | metadata is data that provides information about data. | compound |
| comments | - | A written explanation, observation or criticism added to textual material. | text |
| dateRecordCreated | - | The date on which the activity or entity is created. | datetime |
| recordCreatedBy | - | Indicates the person or authoritative body who brought the item into existence. | string |
| dateRecordUpdated | - | The date (and time) on which report was updated after it had been submitted. | datetime |
| wasUpdatedBy | - | An entity which is updated by another entity or an agent. | string |

### Entity: umdm_samples

A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a material) to be used for testing, analysis, inspection, investigation, demonstration, or trial use.

| Name | Label | Description | Data Type |
|:---- |:-----|:-----------|:---------|
| sampleID&#8251; | - | Name or other identifier of an entry from a biosample database. | string |
| belongsToSubject | - | An individual who is the subject of personal data, persons to whom data refers, and from whom data are collected, processed, and stored. | xref |
| belongsToRequest | - | A sequence of letters, numbers, or other characters that specifically identifies a particular order. | string |
| dateOfRequest | - | The date on which the activity or entity was ordered. | date |
| reasonForSampling | - | The explanation for why a test, measurement, or assessment is executed. | mref |
| samplingDate | - | The date that a sample was collected or obtained. | date |
| samplingTimestamp | - | Date and time at which this material was collected. | datetime |
| samplingProtocol | - | The procedure whereby this material was sampled for an analysis. | mref |
| samplingProtocolDeviation | - | A variation from processes or procedures defined in the sampling protocol. Deviations usually do not preclude the overall evaluability of subject data for either efficacy or safety, and are often acknowledged and accepted in advance by the sponsor. | text |
| reasonForSamplingProtocolDeviation | - | The rationale for why a deviation from the sampling protocol has occurred. | text |
| biospecimenType | - | The type of material taken from a biological entity for testing, diagnostic, propagation, treatment or research purposes. | xref |
| anatomicalSource | - | Biological entity that constitutes the structural organization of an individual member of a biological species from which this material was taken. | xref |
| pathologicalState | - | The pathological state of the tissue from which this material was derived. | xref |
| biospecimenUsability | - | An indication as to whether a biospecimen is suitable for testing purposes. | bool |
| alternativeIdentifiers | - | A backup sequence of characters used to identify an entity. | string |
| belongsToDataRelease | - | The act of making data or other structured information accessible to the public or to the user group of a database. | mref |
| recordMetadata | - | metadata is data that provides information about data. | compound |
| comments | - | A written explanation, observation or criticism added to textual material. | text |
| dateRecordCreated | - | The date on which the activity or entity is created. | datetime |
| recordCreatedBy | - | Indicates the person or authoritative body who brought the item into existence. | string |
| dateRecordUpdated | - | The date (and time) on which report was updated after it had been submitted. | datetime |
| wasUpdatedBy | - | An entity which is updated by another entity or an agent. | string |

### Entity: umdm_samplePreparation

A sample preparation for a nucleic acids sequencing assay.

| Name | Label | Description | Data Type |
|:---- |:-----|:-----------|:---------|
| sampleID&#8251; | - | A unique proper name or character sequence that identifies this particular sample preparation. | string |
| belongsToSample | - | Name or other identifier of an entry from a biosample database. | xref |
| belongsToLabProcedure | - | Any procedure that involves testing or manipulating a sample of blood, urine, or other body substance in a laboratory setting. | xref |
| belongsToRequest | - | A sequence of letters, numbers, or other characters that specifically identifies a particular order. | string |
| inputAmount | - | Amount of input material in nanogram (ng). | int |
| libraryPreparationKit | - | Pre-filled, ready-to-use reagent cartridges intented to improve chemistry, cluster density and read length as well as improve quality (Q) scores for this sample. Reagent components are encoded to interact with the sequencing system to validate compatibility with user-defined applications. | xref |
| pcrFree | - | Indicates whether a polymerase chain reaction (PCR) was used to prepare this sample. PCR is a method for amplifying a DNA base sequence using multiple rounds of heat denaturation of the DNA and annealing of oligonucleotide primers complementary to flanking regions in the presence of a heat-stable polymerase. | bool |
| targetEnrichmentKit | - | Indicates which target enrichment kit was used to prepare this sample. Target enrichment is a pre-sequencing DNA preparation step where DNA sequences are either directly amplified (amplicon or multiplex PCR-based) or captured (hybrid capture-based) in order to only focus on specific regions of a genome or DNA sample. | xref |
| umisPresent | - | Indicates whether any unique molecular identifiers (UMIs) are present. An UMI barcode is a short nucleotide sequence that is used to identify reads originating from an individual mRNA molecule. | bool |
| intendedInsertSize | - | In paired-end sequencing, the DNA between the adapter sequences is the insert. The length of this sequence is known as the insert size, not to be confused with the inner distance between reads. So, fragment length equals read adapter length (2x) plus insert size, and insert size equals read lenght (2x) plus inner distance. | int |
| intendedReadLength | - | The number of nucleotides intended to be ordered from each side of a nucleic acid fragment obtained after the completion of a sequencing process. | int |
| barcode | - | A machine-readable representation of information in a visual format on a surface. | string |
| belongsToBatch | - | A quantity of people or things treated or regarded as a group, especially when subdivided from a larger group. | string |
| belongsToDataRelease | - | The act of making data or other structured information accessible to the public or to the user group of a database. | mref |
| recordMetadata | - | metadata is data that provides information about data. | compound |
| comments | - | A written explanation, observation or criticism added to textual material. | text |
| dateRecordCreated | - | The date on which the activity or entity is created. | datetime |
| recordCreatedBy | - | Indicates the person or authoritative body who brought the item into existence. | string |
| dateRecordUpdated | - | The date (and time) on which report was updated after it had been submitted. | datetime |
| wasUpdatedBy | - | An entity which is updated by another entity or an agent. | string |

### Entity: umdm_sequencing

The determination of complete (typically nucleotide) sequences, including those of genomes (full genome sequencing, de novo sequencing and resequencing), amplicons and transcriptomes.

| Name | Label | Description | Data Type |
|:---- |:-----|:-----------|:---------|
| sequencingID&#8251; | - | A unique proper name or character sequence that identifies this particular nucleic acid sequencing assay. | string |
| belongsToLabProcedure | - | Any procedure that involves testing or manipulating a sample of blood, urine, or other body substance in a laboratory setting. | xref |
| belongsToSamplePreparation | - | A unique proper name or character sequence that identifies this particular sample preparation. | xref |
| reasonForSequencing | - | A rationale for executing a plan of action. | xref |
| sequencingDate | - | Date on which this sequencing assay was performed. | date |
| sequencingFacilityOrganization | - | An organization that provides sequence determination service | xref |
| sequencingPlatform | - | The used sequencing platform (i.e. brand, name of a company that produces sequencer equipment). | xref |
| sequencingInstrumentModel | - | The used product name and model number of a manufacturer's genomic (dna) sequencer. | xref |
| sequencingMethod | - | Method used to determine the order of bases in a nucleic acid sequence. | xref |
| averageReadDepth | - | The average number of times a particular locus (site, nucleotide, amplicon, region) was sequenced. | int |
| observedReadLength | - | The number of nucleotides successfully ordered from each side of a nucleic acid fragment obtained after the completion of a sequencing process. | int |
| observedInsertSize | - | In paired-end sequencing, the DNA between the adapter sequences is the insert. The length of this sequence is known as the insert size, not to be confused with the inner distance between reads. So, fragment length equals read adapter length (2x) plus insert size, and insert size equals read lenght (2x) plus inner distance. | int |
| percentageQ30 | - | Percentage of reads with a Phred quality score over 30, which indicates less than a 1/1000 chance that the base was called incorrectly. | decimal |
| percentageTR20 | - | Percentage of the target sequence on which 20 or more unique reads were successfully mapped. | decimal |
| otherQualityMetrics | - | Other NGS quality control metrics, including but not limited to (i) sequencer metrics such as yield, error rate, density (K/mm2), cluster PF (%) and phas/prephas (%), (ii) alignment metrics such as QM insert size, GC content, QM duplicated reads (%), QM error rate, uniformity/evenness of coverage and maternal cell contamination, and (iii) variant call metrics such as number of SNVs/CNVs/SVs called, number of missense/nonsense variants, common variants (%), unique variants (%), gender match and trio inheritance check. | text |
| referenceGenomeUsed | - | The specific build of the human genome used as reference for sequence alignment and variant calling. | xref |
| belongsToDataRelease | - | The act of making data or other structured information accessible to the public or to the user group of a database. | mref |
| recordMetadata | - | metadata is data that provides information about data. | compound |
| comments | - | A written explanation, observation or criticism added to textual material. | text |
| dateRecordCreated | - | The date on which the activity or entity is created. | datetime |
| recordCreatedBy | - | Indicates the person or authoritative body who brought the item into existence. | string |
| dateRecordUpdated | - | The date (and time) on which report was updated after it had been submitted. | datetime |
| wasUpdatedBy | - | An entity which is updated by another entity or an agent. | string |

### Entity: umdm_files

A set of related records (either written or electronic) kept together.

| Name | Label | Description | Data Type |
|:---- |:-----|:-----------|:---------|
| filename&#8251; | - | The literal identifier for an electronic file. | string |
| producedBySequencing | - | A unique proper name or character sequence that identifies this particular nucleic acid sequencing assay. | mref |
| belongsToSubject | - | An individual who is the subject of personal data, persons to whom data refers, and from whom data are collected, processed, and stored. | xref |
| belongsToStudy | - | Reference to the study or studies in which this person participates. | mref |
| belongsToCohort | - | A group of individuals, identified by a common characteristic. | mref |
| server | - | A computer which provides some service for other computers connected to it via a network. | string |
| filePath | - | The specification of a node (file or directory) in a hierarchical file system, usually specified by listing the nodes top-down. | string |
| fileFormat | - | The format of an electronic file. | string |
| fileSize | - | The size of an electronic file in bytes. | int |
| md5Checksum | - | A 32-character hexadecimal number that is computed on a file. | string |
| fileStatus | - | The condition for an electronic file relative to the current data or file processing step. | xref |
| dateFileCreated | - | The date a digital resource was created. | date |
| alternativeFileIdentifiers | - | A backup sequence of characters used to identify an entity. | string |
| belongsToDataRelease | - | The act of making data or other structured information accessible to the public or to the user group of a database. | mref |
| recordMetadata | - | metadata is data that provides information about data. | compound |
| comments | - | A written explanation, observation or criticism added to textual material. | text |
| dateRecordCreated | - | The date on which the activity or entity is created. | datetime |
| recordCreatedBy | - | Indicates the person or authoritative body who brought the item into existence. | string |
| dateRecordUpdated | - | The date (and time) on which report was updated after it had been submitted. | datetime |
| wasUpdatedBy | - | An entity which is updated by another entity or an agent. | string |

### Entity: umdm_cohorts

A group of individuals, identified by a common characteristic.

| Name | Label | Description | Data Type |
|:---- |:-----|:-----------|:---------|
| cohortID&#8251; | - | One or more characters used to identify, name, or characterize the nature, properties, or contents of a thing. | string |
| acronym | - | The non-unique initials or abbreviated name used for identification. | string |
| name | - | The words or language units by which a thing is known. | string |
| description | - | The description of the characteristics that define a cohort. | text |
| principleInvestigator | - | The principle investigator or responsible person for this study. | string |
| contactPerson | - | A person acting as a channel for communication between groups or on behalf of a group. | string |
| contactEmail | - | An email address for the purpose of contacting the study contact person. | email |
| sizeOfCohort | - | A subset of a larger population, selected for investigation to draw conclusions or make estimates about the larger population. | int |
| recordMetadata | - | metadata is data that provides information about data. | compound |
| comments | - | A written explanation, observation or criticism added to textual material. | text |
| dateRecordCreated | - | The date on which the activity or entity is created. | datetime |
| recordCreatedBy | - | Indicates the person or authoritative body who brought the item into existence. | string |
| dateRecordUpdated | - | The date (and time) on which report was updated after it had been submitted. | datetime |
| wasUpdatedBy | - | An entity which is updated by another entity or an agent. | string |

### Entity: umdm_labProcedures

Any procedure that involves testing or manipulating a sample of blood, urine, or other body substance in a laboratory setting.

| Name | Label | Description | Data Type |
|:---- |:-----|:-----------|:---------|
| code&#8251; | - | A character or string that represents the short code name of the laboratory test. | string |
| test | - | A character or string that represents the full name of the laboratory assessment. | string |
| description | - | A written or verbal account, representation, statement, or explanation of something | text |
| category | - | A classification of the laboratory test. | string |
| subcategory | - | A sub-division of the laboratory test classification. | string |
| geneList | - | A data set of the names or identifiers of genes that are the outcome of an analysis or have been put together for the purpose of an analysis. | text |

### Entity: umdm_organizations

Organization information standardized to the Research Organization Registry (ROR)

| Name | Label | Description | Data Type |
|:---- |:-----|:-----------|:---------|
| value&#8251; | - | The information contained in a data field. It may represent a numeric quantity, a textual characterization, a date or time measurement, or some other state, depending on the nature of the attribute. | string |
| description | - | A written or verbal account, representation, statement, or explanation of something | text |
| codesystem | - | A systematized collection of concepts that define corresponding codes. | string |
| code | - | A symbol or combination of symbols which is assigned to the members of a collection. | string |
| iri | - | A unique symbol that establishes identity of the resource. | hyperlink |

### Entity: umdm_releases

The act of making data or other structured information accessible to the public or to the user group of a database.

| Name | Label | Description | Data Type |
|:---- |:-----|:-----------|:---------|
| id&#8251; | - | One or more characters used to identify, name, or characterize the nature, properties, or contents of a thing. | string |
| name | - | The words or language units by which a thing is known. | string |
| description | - | A written or verbal account, representation, statement, or explanation of something. | text |
| date | - | A date of database submission refers to the moment in time in which some information was submitted/received to a database system. | date |
| createdBy | - | Indicates the person or authoritative body who brought the item into existence. | string |
| numberOfEntriesAdded | - | Combined or joined to increase in size or quantity or scope. | int |
| dataSource | - | The person or authoritative body who provided the information. | string |
| releaseComments | - | A notation regarding the decisions, and/or clarification of any information pertaining to data management. | text |

### Entity: umdm_samplingProtocols

Describes the procedure whereby biological samples for an experiment are sourced.

| Name | Label | Description | Data Type |
|:---- |:-----|:-----------|:---------|
| id&#8251; | - | One or more characters used to identify, name, or characterize the nature, properties, or contents of a thing. | string |
| name | - | The words or language units by which a thing is known. | string |
| description | - | A written or verbal account, representation, statement, or explanation of something. | text |
| version | - | A form or variant of a type or original; one of a sequence of copies of a program, each incorporating new modifications. | string |
| iri | - | A unique symbol that establishes identity of the resource. | hyperlink |

### Entity: umdm_lookups_attributeTemplateDefault

attribute template where value is the primary key

| Name | Label | Description | Data Type |
|:---- |:-----|:-----------|:---------|
| value&#8251; | - | The information contained in a data field. It may represent a numeric quantity, a textual characterization, a date or time measurement, or some other state, depending on the nature of the attribute. | string |
| description | - | A written or verbal account, representation, statement, or explanation of something | text |
| codesystem | - | A systematized collection of concepts that define corresponding codes. | string |
| code | - | A symbol or combination of symbols which is assigned to the members of a collection. | string |
| iri | - | A unique symbol that establishes identity of the resource. | hyperlink |

### Entity: umdm_lookups_attributeTemplateCode

attribute template where code is the primary key

| Name | Label | Description | Data Type |
|:---- |:-----|:-----------|:---------|
| value | - | The information contained in a data field. It may represent a numeric quantity, a textual characterization, a date or time measurement, or some other state, depending on the nature of the attribute. | string |
| description | - | A written or verbal account, representation, statement, or explanation of something | text |
| codesystem | - | A systematized collection of concepts that define corresponding codes. | string |
| code&#8251; | - | A symbol or combination of symbols which is assigned to the members of a collection. | string |
| iri | - | A unique symbol that establishes identity of the resource. | hyperlink |

Note: The symbol &#8251; denotes attributes that are primary keys

