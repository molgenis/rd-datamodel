#//////////////////////////////////////////////////////////////////////////////
# FILE: setup.sh
# CREATED: 2021-11-10
# MODIFIED: 2021-11-12
# PURPOSE: import URDM and assets into a new Molgenis instance
# COMMENTS: start by cloning this repository
#//////////////////////////////////////////////////////////////////////////////

# ~ 1 ~
# Install molgenis commander
# See github repo for the latest installation instructions and release notes
# https://github.com/molgenis/molgenis-tools-commander/wiki/Installation-guide
pip3 install --upgrade molgenis-commander

# run interactive config and set host (e.g., https://database.molgenis.org)
mcmd config set host

# ~ 2 ~
# Import URDM and assets
mcmd import -p emx/dist/urdm.xlsx
mcmd import -p emx/lookups/urdm_lookups_anatomicalSource.csv
mcmd import -p emx/lookups/urdm_lookups_ancestry.csv
mcmd import -p emx/lookups/urdm_lookups_biospecimenType.csv
mcmd import -p emx/lookups/urdm_lookups_country.csv
mcmd import -p emx/lookups/urdm_lookups_genomeAccessions.csv
mcmd import -p emx/lookups/urdm_lookups_genotypicSex.csv
mcmd import -p emx/lookups/urdm_lookups_inclusionStatus.csv
mcmd import -p emx/lookups/urdm_lookups_labIndication.csv
mcmd import -p emx/lookups/urdm_lookups_pathologicalState.csv
mcmd import -p emx/lookups/urdm_lookups_phenotype.csv
mcmd import -p emx/lookups/urdm_lookups_phenotypicSex.csv
mcmd import -p emx/lookups/urdm_lookups_sequencingMethods.csv
mcmd import -p emx/lookups/urdm_lookups_studyStatus.csv

# Optional: URDM modules
mcmd import -p emx/dist/jobs.xlsx   # module for tracking jobs
mcmd import -p emx/dist/users.xlsx  # module for user auditing


# Optional: create demo
mcmd import -p data/demo/urdm_demo.xlsx --as urdm
mcmd make --role ANONYMOUS urdm_VIEWER
mcmd give anonymous view sys_md