#!/bin/bash

. ${OPENSHIFT_DATA_DIR}env.sh

cd ${OPENSHIFT_REPO_DIR}l4c_db
python manage.py loadcclmessages
