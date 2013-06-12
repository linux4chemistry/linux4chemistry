#!/bin/bash

source ${OPENSHIFT_PYTHON_DIR}virtenv/bin/activate

cd ${OPENSHIFT_REPO_DIR}linux4chemistry
python manage.py loadmessages
