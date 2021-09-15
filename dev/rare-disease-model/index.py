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

# convert model
c = Convert(files = ['emx/model.yml'])


# priorityNameKey options
c.convert()
# c.convert(priorityNameKey = 'name-cosas')
# c.convert(priorityNameKey = 'name-rd3')

# print fields
c.packages
c.entities
c.attributes
c.data


# write model and schema
c.write(name = 'rdModel', format = 'csv', outDir = 'dev/rare-disease-model/model/')
c.write_schema(path = 'dev/rare-disease-model/model/rd_schema.md')