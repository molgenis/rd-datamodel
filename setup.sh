#//////////////////////////////////////////////////////////////////////////////
# FILE: setup.sh
# CREATED: 2021-11-10
# MODIFIED: 2022-02-02
# STATUS: stable
# PURPOSE: import URDM and assets into a new Molgenis instance
# COMMENTS: start by cloning this repository
#//////////////////////////////////////////////////////////////////////////////

# ~ 1 ~
# Install molgenis commander
# See github repo for the latest installation instructions and release notes
# https://github.com/molgenis/molgenis-tools-commander/wiki/Installation-guide
# pip3 install --upgrade molgenis-commander

# run interactive config and set host (e.g., https://database.molgenis.org)
# mcmd config set host

# ~ 2 ~
# Import URDM and assets

# <!--- start: listEmxFiles --->
mcmd import -p dist/umdm.xlsx
mcmd import -p dist/umdm_lookups_diagnosisConfirmationStatuses.csv
mcmd import -p dist/umdm_lookups_country.csv
mcmd import -p dist/umdm_lookups_genderIdentity.csv
mcmd import -p dist/umdm_lookups_inclusionCriteria.csv
mcmd import -p dist/umdm_lookups_sequencingMethods.csv
mcmd import -p dist/umdm_lookups_ancestry.csv
mcmd import -p dist/umdm_lookups_fileStatus.csv
mcmd import -p dist/umdm_lookups_samplingReason.csv
mcmd import -p dist/umdm_lookups_ngsKits.csv
mcmd import -p dist/umdm_lookups_sequencingPlatform.csv
mcmd import -p dist/umdm_lookups_phenotype.csv
mcmd import -p dist/umdm_lookups_dataUseModifiers.csv
mcmd import -p dist/umdm_lookups_subjectStatus.csv
mcmd import -p dist/umdm_lookups_studyStatus.csv
mcmd import -p dist/umdm_lookups_sequencingInstrumentModels.csv
mcmd import -p dist/umdm_lookups_pathologicalState.csv
mcmd import -p dist/umdm_lookups_genderAtBirth.csv
mcmd import -p dist/umdm_lookups_genomeAccessions.csv
mcmd import -p dist/umdm_lookups_diseases.csv
mcmd import -p dist/umdm_lookups_biospecimenType.csv
mcmd import -p dist/umdm_lookups_biospecimenUsability.csv
mcmd import -p dist/umdm_lookups_anatomicalSource.csv
mcmd import -p dist/umdm_lookups_dataUsePermissions.csv
mcmd import -p dist/umdm_lookups_genotypicSex.csv
# <!--- end: listEmxFiles --->


# Optional: create demo
# mcmd import -p data/demo/umdm_demo.xlsx --as umdm
# mcmd make --role ANONYMOUS umdm_VIEWER
# mcmd give anonymous view sys_md

# mcmd delete -p umdm # completing remove package

# Optional: URDM modules
# mcmd import -p dist/jobs.xlsx   # module for tracking jobs
# mcmd import -p dist/users.xlsx  # module for user auditing