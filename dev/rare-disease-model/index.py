#'////////////////////////////////////////////////////////////////////////////
#' FILE: index.py
#' AUTHOR: David Ruvolo
#' CREATED: 2021-09-15
#' MODIFIED: 2021-09-15
#' PURPOSE: compile EMX for `model.yml`
#' STATUS: in.progress
#' PACKAGES: convert
#' COMMENTS: NA
#'////////////////////////////////////////////////////////////////////////////


from src.convert.convert import Convert
c = Convert(files = ['emx/model.yml'])
c.convert(priorityNameKey = 'name-cosas')
c.write_schema(path = 'dev/rare-disease-model/model/rd_schema.md')

# c.convert()
c.packages
c.entities
c.attributes
c.data

c.write(name = 'rdModel', format = 'xlsx', outDir = 'dev/rare-disease-model/model/')