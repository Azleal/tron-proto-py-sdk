# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: tron/proto/core/Discover.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'tron/proto/core/Discover.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1etron/proto/core/Discover.proto\x12\x08protocol\"9\n\x08\x45ndpoint\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x0e\n\x06nodeId\x18\x03 \x01(\x0c\"s\n\x0bPingMessage\x12 \n\x04\x66rom\x18\x01 \x01(\x0b\x32\x12.protocol.Endpoint\x12\x1e\n\x02to\x18\x02 \x01(\x0b\x32\x12.protocol.Endpoint\x12\x0f\n\x07version\x18\x03 \x01(\x05\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\"P\n\x0bPongMessage\x12 \n\x04\x66rom\x18\x01 \x01(\x0b\x32\x12.protocol.Endpoint\x12\x0c\n\x04\x65\x63ho\x18\x02 \x01(\x05\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\"W\n\x0e\x46indNeighbours\x12 \n\x04\x66rom\x18\x01 \x01(\x0b\x32\x12.protocol.Endpoint\x12\x10\n\x08targetId\x18\x02 \x01(\x0c\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\"i\n\nNeighbours\x12 \n\x04\x66rom\x18\x01 \x01(\x0b\x32\x12.protocol.Endpoint\x12&\n\nneighbours\x18\x02 \x03(\x0b\x32\x12.protocol.Endpoint\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\"/\n\rBackupMessage\x12\x0c\n\x04\x66lag\x18\x01 \x01(\x08\x12\x10\n\x08priority\x18\x02 \x01(\x05\x42\x46\n\x0forg.tron.protosB\x08\x44iscoverZ)github.com/tronprotocol/grpc-gateway/coreb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tron.proto.core.Discover_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017org.tron.protosB\010DiscoverZ)github.com/tronprotocol/grpc-gateway/core'
  _globals['_ENDPOINT']._serialized_start=44
  _globals['_ENDPOINT']._serialized_end=101
  _globals['_PINGMESSAGE']._serialized_start=103
  _globals['_PINGMESSAGE']._serialized_end=218
  _globals['_PONGMESSAGE']._serialized_start=220
  _globals['_PONGMESSAGE']._serialized_end=300
  _globals['_FINDNEIGHBOURS']._serialized_start=302
  _globals['_FINDNEIGHBOURS']._serialized_end=389
  _globals['_NEIGHBOURS']._serialized_start=391
  _globals['_NEIGHBOURS']._serialized_end=496
  _globals['_BACKUPMESSAGE']._serialized_start=498
  _globals['_BACKUPMESSAGE']._serialized_end=545
# @@protoc_insertion_point(module_scope)
