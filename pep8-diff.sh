#!/usr/bin/env bash

LINE_LENGTH=100

# Obtain the path to the work directory
RELATIVE_SOURCE_PATH=`dirname ${BASH_SOURCE[@]}`
SOURCE_PATH=`readlink -f ${RELATIVE_SOURCE_PATH}`


TMP_FILE=`mktemp`

autopep8 --max-line-length ${LINE_LENGTH} --diff -aaa -r ${SOURCE_PATH}/sim_jop/ >> ${TMP_FILE}
autopep8 --max-line-length ${LINE_LENGTH} --diff -aaa -r ${SOURCE_PATH}/sim_jop/railway/ >> ${TMP_FILE}

autopep8 --max-line-length ${LINE_LENGTH} --diff -aaa ${SOURCE_PATH}/setup.py >> ${TMP_FILE}


if [ -s ${TMP_FILE} ]
then
    cat ${TMP_FILE}
    rm -f ${TMP_FILE}
    exit 1
else
    rm -f ${TMP_FILE}
    exit 0
fi
