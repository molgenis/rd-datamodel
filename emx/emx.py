#'////////////////////////////////////////////////////////////////////////////
#' FILE: emx.py
#' AUTHOR: David Ruvolo
#' CREATED: 2021-10-19
#' MODIFIED: 2021-10-19
#' PURPOSE: compile and build EMX files
#' STATUS: in.progress
#' PACKAGES: emxconvert
#' COMMENTS: NA
#'////////////////////////////////////////////////////////////////////////////


from emxconvert.convert import Convert

c = Convert(files = ['emx/src/model.yaml'])
c.convert()
c.write('rdmodel', format = 'xlsx', outDir = 'emx/dist/')
c.write_schema('emx/dist/rdmodel_schema.md')