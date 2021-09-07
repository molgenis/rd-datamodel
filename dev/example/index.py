#'////////////////////////////////////////////////////////////////////////////
#' FILE: index.py
#' AUTHOR: David Ruvolo
#' CREATED: 2021-09-07
#' MODIFIED: 2021-09-07
#' PURPOSE: test conversion
#' STATUS: in.progress
#' PACKAGES: NA
#' COMMENTS: NA
#'////////////////////////////////////////////////////////////////////////////

from src.convert.convert import Convert
c = Convert(file = 'dev/example/birddata.yml')
c.convert()
# c.write(format = 'xlsx', outDir = 'dev/example/model/')
c.write_schema(path = 'dev/example/model/birddata_schema.md')


data = [
    {'id': 'aaa', 'value': 124},
    {'id': 'bbb', 'value': 163, 'type': 'xyz'},
    {'id': 'ccc', 'value': 163},
] 