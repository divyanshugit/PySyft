# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/store/dataset.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)
from syft.proto.core.store import (
    store_object_pb2 as proto_dot_core_dot_store_dot_store__object__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/core/store/dataset.proto",
    package="syft.core.store",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1eproto/core/store/dataset.proto\x12\x0fsyft.core.store\x1a%proto/core/common/common_object.proto\x1a#proto/core/store/store_object.proto"\xe2\x01\n\x07\x44\x61taset\x12!\n\x02id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12\x10\n\x08obj_type\x18\x02 \x01(\t\x12\x1a\n\x12schematic_qualname\x18\x03 \x01(\t\x12-\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32\x1f.syft.core.store.StorableObject\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x0c\n\x04tags\x18\x06 \x03(\t\x12\x18\n\x10read_permissions\x18\x07 \x01(\x0c\x12\x1a\n\x12search_permissions\x18\x08 \x01(\x0c\x62\x06proto3',
    dependencies=[
        proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,
        proto_dot_core_dot_store_dot_store__object__pb2.DESCRIPTOR,
    ],
)


_DATASET = _descriptor.Descriptor(
    name="Dataset",
    full_name="syft.core.store.Dataset",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="syft.core.store.Dataset.id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="obj_type",
            full_name="syft.core.store.Dataset.obj_type",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="schematic_qualname",
            full_name="syft.core.store.Dataset.schematic_qualname",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="data",
            full_name="syft.core.store.Dataset.data",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="syft.core.store.Dataset.description",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="tags",
            full_name="syft.core.store.Dataset.tags",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="read_permissions",
            full_name="syft.core.store.Dataset.read_permissions",
            index=6,
            number=7,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="search_permissions",
            full_name="syft.core.store.Dataset.search_permissions",
            index=7,
            number=8,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=128,
    serialized_end=354,
)

_DATASET.fields_by_name[
    "id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_DATASET.fields_by_name[
    "data"
].message_type = proto_dot_core_dot_store_dot_store__object__pb2._STORABLEOBJECT
DESCRIPTOR.message_types_by_name["Dataset"] = _DATASET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Dataset = _reflection.GeneratedProtocolMessageType(
    "Dataset",
    (_message.Message,),
    {
        "DESCRIPTOR": _DATASET,
        "__module__": "proto.core.store.dataset_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.store.Dataset)
    },
)
_sym_db.RegisterMessage(Dataset)


# @@protoc_insertion_point(module_scope)
