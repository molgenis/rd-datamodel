#'////////////////////////////////////////////////////////////////////////////
#' FILE: index.py
#' AUTHOR: David Ruvolo
#' CREATED: 2021-09-07
#' MODIFIED: 2021-09-14
#' PURPOSE: test conversion
#' STATUS: working
#' PACKAGES: NA
#' COMMENTS: NA
#'////////////////////////////////////////////////////////////////////////////

from src.convert.convert import Convert

# convert example files
c = Convert(files = ['dev/example/birddata.yml', 'dev/example/birddata_refs.yaml'])

# convert and view
c.convert(priorityNameKey = 'name-species')
c.packages
c.entities
c.attributes
c.data


# write files and schema
c.write(name = "birddata", format = 'xlsx', outDir = 'dev/example/model/')
c.write_schema(path = 'dev/example/model/birddata_schema.md')