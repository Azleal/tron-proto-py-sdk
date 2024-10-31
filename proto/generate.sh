#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status.

# Directory containing all proto files (relative to the script's location)
PROTO_DIR=.

# Output directory for generated Python code
OUT_DIR=../

# Ensure the output directory exists
mkdir -p "$OUT_DIR"

# Set the include path to the parent directory (current directory)
INCLUDE_PATHS="-I=. -I=$HOME/protobuf/include"

# Find all .proto files within PROTO_DIR and its subdirectories
PROTO_FILES=$(find "$PROTO_DIR" -type f -name "*.proto")

PROTO_FILES="tron/proto/api/api.proto tron/proto/core/*.proto tron/proto/core/contract/*.proto"
echo "Generating Python sources for the following .proto files:"
echo "$PROTO_FILES"
echo "Using include paths:"
echo "$INCLUDE_PATHS"

# Run protoc with the specified include paths and proto files
python -m grpc_tools.protoc $INCLUDE_PATHS --python_out="$OUT_DIR"  --grpc_python_out="$OUT_DIR" $PROTO_FILES

# (Optional) Add __init__.py files to make directories into Python packages
find "$OUT_DIR" -type d -exec touch {}/__init__.py \;

echo "Python source files generated successfully in '$OUT_DIR'."