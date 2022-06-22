#!/bin/bash

set -e
set -o pipefail

PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

SRC_DIR=protos
DST_DIR=src/eventstore_grpc/proto
CLIENT_API=ClientAPI
GRPC=Grpc
TMP_DIR=.new_protos

mkdir -p $TMP_DIR
rm -rf $TMP_DIR/*

python -m grpc_tools.protoc \
    --proto_path=$SRC_DIR/$CLIENT_API \
    --python_out=$TMP_DIR \
    --grpc_python_out=$TMP_DIR protos/$CLIENT_API/ClientMessageDtos.proto

python -m grpc_tools.protoc \
    --proto_path=$SRC_DIR/$GRPC \
    --python_out=$TMP_DIR \
    --grpc_python_out=$TMP_DIR protos/$GRPC/*.proto

sed -i 's/^import \(.\+\) as/from eventstore_grpc.proto import \1 as/' $TMP_DIR/*.py

mkdir .protos.backup
mv $DST_DIR .protos.backup
mv $TMP_DIR $DST_DIR
rm -rf .protos.backup

