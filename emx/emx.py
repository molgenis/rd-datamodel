#'////////////////////////////////////////////////////////////////////////////
#' FILE: emx.py
#' AUTHOR: David Ruvolo
#' CREATED: 2021-10-19
#' MODIFIED: 2021-10-11
#' PURPOSE: compile and build EMX files
#' STATUS: working; ongoing
#' PACKAGES: emxconvert
#' COMMENTS: NA
#'////////////////////////////////////////////////////////////////////////////

# pip install yamlemxconvert
import yamlemxconvert

#//////////////////////////////////////

# ~ 1 ~
# BUILD EMX1 MODEL
# render model for EMX v1 Molgenis instances

# build: main data model
urdm = yamlemxconvert.Convert(
    files = [
        'emx/src/urdm_emx1.yaml',
        'emx/src/urdm_lookups_emx1.yaml'
    ]
)

urdm.convert()
# urdm.packages
# urdm.entities
# urdm.attributes

urdm.write('urdm', format = 'xlsx', outDir = 'emx/dist/')
urdm.write_schema('emx/schemas/urdm_schema.md')


# ~ a ~
# build: user management module
usersModule = yamlemxconvert.Convert(files = ['emx/src/module_approved_users.yaml'])
usersModule.convert()
usersModule.write('users', format = 'xlsx', outDir = 'emx/dist/')
usersModule.write_schema('emx/schemas/users_module_schema.md')

# ~ b ~
# build: jobs module
jobsModule = yamlemxconvert.Convert(
    files = [
        'emx/src/module_jobs.yaml',
        'emx/src/module_jobs_results.yaml'
    ]
)
jobsModule.convert()
jobsModule.write('jobs', format = 'xlsx', outDir = 'emx/dist')
jobsModule.write_schema('emx/schemas/jobs_module_schema.md')