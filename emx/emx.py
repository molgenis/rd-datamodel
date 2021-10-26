#'////////////////////////////////////////////////////////////////////////////
#' FILE: emx.py
#' AUTHOR: David Ruvolo
#' CREATED: 2021-10-19
#' MODIFIED: 2021-10-21
#' PURPOSE: compile and build EMX files
#' STATUS: working; ongoing
#' PACKAGES: emxconvert
#' COMMENTS: NA
#'////////////////////////////////////////////////////////////////////////////


import yamlemxconvert


#//////////////////////////////////////

# ~ 1 ~
# BUILD EMX1 MODEL
# render model for EMX v1 Molgenis instances

# build: main data model
c = yamlemxconvert.Convert(files = ['emx/src/model_emx_v1.yaml'])
c.convert()

c.write('rdmodel', format = 'xlsx', outDir = 'emx/dist/')
c.write_schema('emx/schemas/rdmodel_schema.md')

c.convert(priorityNameKey = 'rd3')
c.packages
c.entities
c.attributes


# build: user management module
usersModule = yamlemxconvert.Convert(files = ['emx/src/module_approved_users.yaml'])
usersModule.convert()
usersModule.write('users', format = 'xlsx', outDir = 'emx/dist/')
usersModule.write_schema('emx/schemas/users_module_schema.md')