# ////////////////////////////////////////////////////////////////////////////
# FILE: umdm_setup.sh
# AUTHOR: David Ruvolo
# CREATED: 2021-12-07
# MODIFIED: 2021-12-07
# PURPOSE: Setup script for the UMDM
# DEPENDENCIES: molgenis commander
# COMMENTS: NA
# ////////////////////////////////////////////////////////////////////////////

#
# Install the latest version of the Molgenis Commander from GitHub.
# https://github.com/molgenis/molgenis-tools-commander
#

# ~ 1 ~
# SET HOST
# Enter the URL of your Molgenis instance.
mcmd config set host

# ~ 2 ~
# IMPORT MODEL
# Using the molgenis commander, you can import the model and necessary files
# directly from GitHub.

mcmd import -u https://raw.githubusercontent.com/molgenis/rd-datamodel/main/emx/dist/umdm.xlsx
mcmd import -u https://raw.githubusercontent.com/molgenis/rd-datamodel/main/emx/lookups/umdm_lookups_anatomicalSource.csv
mcmd import -u https://raw.githubusercontent.com/molgenis/rd-datamodel/main/emx/lookups/umdm_lookups_ancestry.csv
mcmd import -u https://raw.githubusercontent.com/molgenis/rd-datamodel/main/emx/lookups/umdm_lookups_biospecimenType.csv
mcmd import -u https://raw.githubusercontent.com/molgenis/rd-datamodel/main/emx/lookups/umdm_lookups_country.csv
mcmd import -u https://raw.githubusercontent.com/molgenis/rd-datamodel/main/emx/lookups/umdm_lookups_dataUseModifiers.csv
mcmd import -u https://raw.githubusercontent.com/molgenis/rd-datamodel/main/emx/lookups/umdm_lookups_dataUsePermissions.csv
mcmd import -u https://raw.githubusercontent.com/molgenis/rd-datamodel/main/emx/lookups/umdm_lookups_diagnosisConfirmationStatuses.csv
mcmd import -u https://raw.githubusercontent.com/molgenis/rd-datamodel/main/emx/lookups/umdm_lookups_diseases.csv
mcmd import -u https://raw.githubusercontent.com/molgenis/rd-datamodel/main/emx/lookups/umdm_lookups_fileStatus.csv
mcmd import -u https://raw.githubusercontent.com/molgenis/rd-datamodel/main/emx/lookups/umdm_lookups_genomeAccessions.csv
mcmd import -u https://raw.githubusercontent.com/molgenis/rd-datamodel/main/emx/lookups/umdm_lookups_genotypicSex.csv
mcmd import -u https://raw.githubusercontent.com/molgenis/rd-datamodel/main/emx/lookups/umdm_lookups_inclusionCriteria.csv
mcmd import -u https://raw.githubusercontent.com/molgenis/rd-datamodel/main/emx/lookups/umdm_lookups_ngsKits.csv
mcmd import -u https://raw.githubusercontent.com/molgenis/rd-datamodel/main/emx/lookups/umdm_lookups_pathologicalState.csv
mcmd import -u https://raw.githubusercontent.com/molgenis/rd-datamodel/main/emx/lookups/umdm_lookups_phenotype.csv
mcmd import -u https://raw.githubusercontent.com/molgenis/rd-datamodel/main/emx/lookups/umdm_lookups_phenotypicSex.csv
mcmd import -u https://raw.githubusercontent.com/molgenis/rd-datamodel/main/emx/lookups/umdm_lookups_samplingReason.csv
mcmd import -u https://raw.githubusercontent.com/molgenis/rd-datamodel/main/emx/lookups/umdm_lookups_sequencingInstrumentModels.csv
mcmd import -u https://raw.githubusercontent.com/molgenis/rd-datamodel/main/emx/lookups/umdm_lookups_sequencingMethods.csv
mcmd import -u https://raw.githubusercontent.com/molgenis/rd-datamodel/main/emx/lookups/umdm_lookups_sequencingPlatform.csv
mcmd import -u https://raw.githubusercontent.com/molgenis/rd-datamodel/main/emx/lookups/umdm_lookups_studyStatus.csv
mcmd import -u https://raw.githubusercontent.com/molgenis/rd-datamodel/main/emx/lookups/umdm_lookups_subjectStatus.csv