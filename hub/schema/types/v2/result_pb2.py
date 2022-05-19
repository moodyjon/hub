# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: result.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='result.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z$github.com/lbryio/hub/protobuf/go/pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cresult.proto\x12\x02pb\"\x97\x01\n\x07Outputs\x12\x18\n\x04txos\x18\x01 \x03(\x0b\x32\n.pb.Output\x12\x1e\n\nextra_txos\x18\x02 \x03(\x0b\x32\n.pb.Output\x12\r\n\x05total\x18\x03 \x01(\r\x12\x0e\n\x06offset\x18\x04 \x01(\r\x12\x1c\n\x07\x62locked\x18\x05 \x03(\x0b\x32\x0b.pb.Blocked\x12\x15\n\rblocked_total\x18\x06 \x01(\r\"{\n\x06Output\x12\x0f\n\x07tx_hash\x18\x01 \x01(\x0c\x12\x0c\n\x04nout\x18\x02 \x01(\r\x12\x0e\n\x06height\x18\x03 \x01(\r\x12\x1e\n\x05\x63laim\x18\x07 \x01(\x0b\x32\r.pb.ClaimMetaH\x00\x12\x1a\n\x05\x65rror\x18\x0f \x01(\x0b\x32\t.pb.ErrorH\x00\x42\x06\n\x04meta\"\xe6\x02\n\tClaimMeta\x12\x1b\n\x07\x63hannel\x18\x01 \x01(\x0b\x32\n.pb.Output\x12\x1a\n\x06repost\x18\x02 \x01(\x0b\x32\n.pb.Output\x12\x11\n\tshort_url\x18\x03 \x01(\t\x12\x15\n\rcanonical_url\x18\x04 \x01(\t\x12\x16\n\x0eis_controlling\x18\x05 \x01(\x08\x12\x18\n\x10take_over_height\x18\x06 \x01(\r\x12\x17\n\x0f\x63reation_height\x18\x07 \x01(\r\x12\x19\n\x11\x61\x63tivation_height\x18\x08 \x01(\r\x12\x19\n\x11\x65xpiration_height\x18\t \x01(\r\x12\x19\n\x11\x63laims_in_channel\x18\n \x01(\r\x12\x10\n\x08reposted\x18\x0b \x01(\r\x12\x18\n\x10\x65\x66\x66\x65\x63tive_amount\x18\x14 \x01(\x04\x12\x16\n\x0esupport_amount\x18\x15 \x01(\x04\x12\x16\n\x0etrending_score\x18\x16 \x01(\x01\"\x94\x01\n\x05\x45rror\x12\x1c\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x0e.pb.Error.Code\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x1c\n\x07\x62locked\x18\x03 \x01(\x0b\x32\x0b.pb.Blocked\"A\n\x04\x43ode\x12\x10\n\x0cUNKNOWN_CODE\x10\x00\x12\r\n\tNOT_FOUND\x10\x01\x12\x0b\n\x07INVALID\x10\x02\x12\x0b\n\x07\x42LOCKED\x10\x03\"5\n\x07\x42locked\x12\r\n\x05\x63ount\x18\x01 \x01(\r\x12\x1b\n\x07\x63hannel\x18\x02 \x01(\x0b\x32\n.pb.OutputB&Z$github.com/lbryio/hub/protobuf/go/pbb\x06proto3'
)



_ERROR_CODE = _descriptor.EnumDescriptor(
  name='Code',
  full_name='pb.Error.Code',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_CODE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BLOCKED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=744,
  serialized_end=809,
)
_sym_db.RegisterEnumDescriptor(_ERROR_CODE)


_OUTPUTS = _descriptor.Descriptor(
  name='Outputs',
  full_name='pb.Outputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='txos', full_name='pb.Outputs.txos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extra_txos', full_name='pb.Outputs.extra_txos', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total', full_name='pb.Outputs.total', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='pb.Outputs.offset', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='blocked', full_name='pb.Outputs.blocked', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='blocked_total', full_name='pb.Outputs.blocked_total', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=172,
)


_OUTPUT = _descriptor.Descriptor(
  name='Output',
  full_name='pb.Output',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_hash', full_name='pb.Output.tx_hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nout', full_name='pb.Output.nout', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='pb.Output.height', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='claim', full_name='pb.Output.claim', index=3,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='pb.Output.error', index=4,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='meta', full_name='pb.Output.meta',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=174,
  serialized_end=297,
)


_CLAIMMETA = _descriptor.Descriptor(
  name='ClaimMeta',
  full_name='pb.ClaimMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='pb.ClaimMeta.channel', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='repost', full_name='pb.ClaimMeta.repost', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='short_url', full_name='pb.ClaimMeta.short_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='canonical_url', full_name='pb.ClaimMeta.canonical_url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_controlling', full_name='pb.ClaimMeta.is_controlling', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='take_over_height', full_name='pb.ClaimMeta.take_over_height', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creation_height', full_name='pb.ClaimMeta.creation_height', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='activation_height', full_name='pb.ClaimMeta.activation_height', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expiration_height', full_name='pb.ClaimMeta.expiration_height', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='claims_in_channel', full_name='pb.ClaimMeta.claims_in_channel', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reposted', full_name='pb.ClaimMeta.reposted', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='effective_amount', full_name='pb.ClaimMeta.effective_amount', index=11,
      number=20, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='support_amount', full_name='pb.ClaimMeta.support_amount', index=12,
      number=21, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trending_score', full_name='pb.ClaimMeta.trending_score', index=13,
      number=22, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=300,
  serialized_end=658,
)


_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='pb.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pb.Error.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='pb.Error.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='blocked', full_name='pb.Error.blocked', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ERROR_CODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=661,
  serialized_end=809,
)


_BLOCKED = _descriptor.Descriptor(
  name='Blocked',
  full_name='pb.Blocked',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='pb.Blocked.count', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel', full_name='pb.Blocked.channel', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=811,
  serialized_end=864,
)

_OUTPUTS.fields_by_name['txos'].message_type = _OUTPUT
_OUTPUTS.fields_by_name['extra_txos'].message_type = _OUTPUT
_OUTPUTS.fields_by_name['blocked'].message_type = _BLOCKED
_OUTPUT.fields_by_name['claim'].message_type = _CLAIMMETA
_OUTPUT.fields_by_name['error'].message_type = _ERROR
_OUTPUT.oneofs_by_name['meta'].fields.append(
  _OUTPUT.fields_by_name['claim'])
_OUTPUT.fields_by_name['claim'].containing_oneof = _OUTPUT.oneofs_by_name['meta']
_OUTPUT.oneofs_by_name['meta'].fields.append(
  _OUTPUT.fields_by_name['error'])
_OUTPUT.fields_by_name['error'].containing_oneof = _OUTPUT.oneofs_by_name['meta']
_CLAIMMETA.fields_by_name['channel'].message_type = _OUTPUT
_CLAIMMETA.fields_by_name['repost'].message_type = _OUTPUT
_ERROR.fields_by_name['code'].enum_type = _ERROR_CODE
_ERROR.fields_by_name['blocked'].message_type = _BLOCKED
_ERROR_CODE.containing_type = _ERROR
_BLOCKED.fields_by_name['channel'].message_type = _OUTPUT
DESCRIPTOR.message_types_by_name['Outputs'] = _OUTPUTS
DESCRIPTOR.message_types_by_name['Output'] = _OUTPUT
DESCRIPTOR.message_types_by_name['ClaimMeta'] = _CLAIMMETA
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
DESCRIPTOR.message_types_by_name['Blocked'] = _BLOCKED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Outputs = _reflection.GeneratedProtocolMessageType('Outputs', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUTS,
  '__module__' : 'result_pb2'
  # @@protoc_insertion_point(class_scope:pb.Outputs)
  })
_sym_db.RegisterMessage(Outputs)

Output = _reflection.GeneratedProtocolMessageType('Output', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUT,
  '__module__' : 'result_pb2'
  # @@protoc_insertion_point(class_scope:pb.Output)
  })
_sym_db.RegisterMessage(Output)

ClaimMeta = _reflection.GeneratedProtocolMessageType('ClaimMeta', (_message.Message,), {
  'DESCRIPTOR' : _CLAIMMETA,
  '__module__' : 'result_pb2'
  # @@protoc_insertion_point(class_scope:pb.ClaimMeta)
  })
_sym_db.RegisterMessage(ClaimMeta)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {
  'DESCRIPTOR' : _ERROR,
  '__module__' : 'result_pb2'
  # @@protoc_insertion_point(class_scope:pb.Error)
  })
_sym_db.RegisterMessage(Error)

Blocked = _reflection.GeneratedProtocolMessageType('Blocked', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKED,
  '__module__' : 'result_pb2'
  # @@protoc_insertion_point(class_scope:pb.Blocked)
  })
_sym_db.RegisterMessage(Blocked)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)