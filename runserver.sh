#!/bin/sh

export OPENSHIFT_DIY_IP=0.0.0.0
export OPENSHIFT_DIY_PORT=8000
export OPENSHIFT_REPO_DIR="`dirname $0`/"
export OPENSHIFT_DATA_DIR=${OPENSHIFT_REPO_DIR}../dev-data/
export OPENSHIFT_DIY_LOG_DIR=${OPENSHIFT_DATA_DIR}

uwsgi \
    --ini ${OPENSHIFT_REPO_DIR}uwsgi/uwsgi-common.ini \
    --ini ${OPENSHIFT_REPO_DIR}uwsgi/uwsgi-development.ini
