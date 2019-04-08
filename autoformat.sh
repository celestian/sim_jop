#!/usr/bin/env bash

LINE_LENGTH=80

# Obtain the path to the work directory
RELATIVE_SOURCE_PATH=`dirname ${BASH_SOURCE[@]}`
SOURCE_PATH=`readlink -f ${RELATIVE_SOURCE_PATH}`

# Removing of trailing spaces
# sed --in-place 's/[[:space:]]\+$//' `find ${SOURCE_PATH} -type f -name '*.md'`
# sed --in-place 's/[[:space:]]\+$//' `find ${SOURCE_PATH} -type f -name '*.feature'`

autopep8 --max-line-length ${LINE_LENGTH} -i -aaa -r ${SOURCE_PATH}/sim_doz/
autopep8 --max-line-length ${LINE_LENGTH} -i -aaa -r ${SOURCE_PATH}/sim_doz/railway

autopep8 --max-line-length ${LINE_LENGTH} -i -aaa ${SOURCE_PATH}/setup.py
