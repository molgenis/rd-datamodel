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


from emxconvert.convert import Convert

# data model
c = Convert(files = ['emx/src/model.yaml'])
c.convert()
c.write('rdmodel', format = 'xlsx', outDir = 'emx/dist/')
c.write_schema('emx/dist/rdmodel_schema.md')


# user management module
usersModule = Convert(files = ['emx/src/module_approved_users.yaml'])
usersModule.convert()
usersModule.write('users', format = 'xlsx', outDir = 'emx/dist/')