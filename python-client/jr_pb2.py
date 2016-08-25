# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jr.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='jr.proto',
  package='JRService',
  syntax='proto3',
  serialized_pb=_b('\n\x08jr.proto\x12\tJRService\"\x16\n\x08SingerId\x12\n\n\x02id\x18\x01 \x01(\x05\"\"\n\x06Singer\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"C\n\x04Song\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12!\n\x06singer\x18\x03 \x01(\x0b\x32\x11.JRService.Singer\"*\n\x08SongList\x12\x1e\n\x05songs\x18\x01 \x03(\x0b\x32\x0f.JRService.Song2z\n\tJRService\x12\x37\n\tListSongs\x12\x13.JRService.SingerId\x1a\x13.JRService.SongList\"\x00\x12\x34\n\x08GetSongs\x12\x13.JRService.SingerId\x1a\x0f.JRService.Song\"\x00\x30\x01\x42\x1d\n\x10\x63om.jr.JRServiceB\x07JRProtoP\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SINGERID = _descriptor.Descriptor(
  name='SingerId',
  full_name='JRService.SingerId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='JRService.SingerId.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=45,
)


_SINGER = _descriptor.Descriptor(
  name='Singer',
  full_name='JRService.Singer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='JRService.Singer.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='JRService.Singer.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=81,
)


_SONG = _descriptor.Descriptor(
  name='Song',
  full_name='JRService.Song',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='JRService.Song.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='JRService.Song.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='singer', full_name='JRService.Song.singer', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=150,
)


_SONGLIST = _descriptor.Descriptor(
  name='SongList',
  full_name='JRService.SongList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='songs', full_name='JRService.SongList.songs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=194,
)

_SONG.fields_by_name['singer'].message_type = _SINGER
_SONGLIST.fields_by_name['songs'].message_type = _SONG
DESCRIPTOR.message_types_by_name['SingerId'] = _SINGERID
DESCRIPTOR.message_types_by_name['Singer'] = _SINGER
DESCRIPTOR.message_types_by_name['Song'] = _SONG
DESCRIPTOR.message_types_by_name['SongList'] = _SONGLIST

SingerId = _reflection.GeneratedProtocolMessageType('SingerId', (_message.Message,), dict(
  DESCRIPTOR = _SINGERID,
  __module__ = 'jr_pb2'
  # @@protoc_insertion_point(class_scope:JRService.SingerId)
  ))
_sym_db.RegisterMessage(SingerId)

Singer = _reflection.GeneratedProtocolMessageType('Singer', (_message.Message,), dict(
  DESCRIPTOR = _SINGER,
  __module__ = 'jr_pb2'
  # @@protoc_insertion_point(class_scope:JRService.Singer)
  ))
_sym_db.RegisterMessage(Singer)

Song = _reflection.GeneratedProtocolMessageType('Song', (_message.Message,), dict(
  DESCRIPTOR = _SONG,
  __module__ = 'jr_pb2'
  # @@protoc_insertion_point(class_scope:JRService.Song)
  ))
_sym_db.RegisterMessage(Song)

SongList = _reflection.GeneratedProtocolMessageType('SongList', (_message.Message,), dict(
  DESCRIPTOR = _SONGLIST,
  __module__ = 'jr_pb2'
  # @@protoc_insertion_point(class_scope:JRService.SongList)
  ))
_sym_db.RegisterMessage(SongList)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\020com.jr.JRServiceB\007JRProtoP\001'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class JRServiceStub(object):
  """service definition
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListSongs = channel.unary_unary(
        '/JRService.JRService/ListSongs',
        request_serializer=SingerId.SerializeToString,
        response_deserializer=SongList.FromString,
        )
    self.GetSongs = channel.unary_stream(
        '/JRService.JRService/GetSongs',
        request_serializer=SingerId.SerializeToString,
        response_deserializer=Song.FromString,
        )


class JRServiceServicer(object):
  """service definition
  """

  def ListSongs(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSongs(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_JRServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListSongs': grpc.unary_unary_rpc_method_handler(
          servicer.ListSongs,
          request_deserializer=SingerId.FromString,
          response_serializer=SongList.SerializeToString,
      ),
      'GetSongs': grpc.unary_stream_rpc_method_handler(
          servicer.GetSongs,
          request_deserializer=SingerId.FromString,
          response_serializer=Song.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'JRService.JRService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaJRServiceServicer(object):
  """service definition
  """
  def ListSongs(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def GetSongs(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaJRServiceStub(object):
  """service definition
  """
  def ListSongs(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  ListSongs.future = None
  def GetSongs(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()


def beta_create_JRService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('JRService.JRService', 'GetSongs'): SingerId.FromString,
    ('JRService.JRService', 'ListSongs'): SingerId.FromString,
  }
  response_serializers = {
    ('JRService.JRService', 'GetSongs'): Song.SerializeToString,
    ('JRService.JRService', 'ListSongs'): SongList.SerializeToString,
  }
  method_implementations = {
    ('JRService.JRService', 'GetSongs'): face_utilities.unary_stream_inline(servicer.GetSongs),
    ('JRService.JRService', 'ListSongs'): face_utilities.unary_unary_inline(servicer.ListSongs),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_JRService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('JRService.JRService', 'GetSongs'): SingerId.SerializeToString,
    ('JRService.JRService', 'ListSongs'): SingerId.SerializeToString,
  }
  response_deserializers = {
    ('JRService.JRService', 'GetSongs'): Song.FromString,
    ('JRService.JRService', 'ListSongs'): SongList.FromString,
  }
  cardinalities = {
    'GetSongs': cardinality.Cardinality.UNARY_STREAM,
    'ListSongs': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'JRService.JRService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)