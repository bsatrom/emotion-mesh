# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: local-detector/streaming/assets/messages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='local-detector/streaming/assets/messages.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n.local-detector/streaming/assets/messages.proto\"\x89\x01\n\x0bServerBound\x12(\n\x0estream_control\x18\x01 \x01(\x0b\x32\x0e.StreamControlH\x00\x12&\n\rframe_capture\x18\x02 \x01(\x0b\x32\r.FrameCaptureH\x00\x12\x1d\n\x08response\x18\x03 \x01(\x0b\x32\t.ResponseH\x00\x42\t\n\x07message\" \n\rStreamControl\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\"\x1f\n\x0c\x46rameCapture\x12\x0f\n\x07overlay\x18\x01 \x01(\x08\"\x9c\x02\n\x0b\x43lientBound\x12\x17\n\x05start\x18\x01 \x01(\x0b\x32\x06.StartH\x00\x12\x15\n\x04stop\x18\x02 \x01(\x0b\x32\x05.StopH\x00\x12\x17\n\x05video\x18\x03 \x01(\x0b\x32\x06.VideoH\x00\x12\x1b\n\x07overlay\x18\x04 \x01(\x0b\x32\x08.OverlayH\x00\x12+\n\x0f\x64\x65tectionResult\x18\x05 \x01(\x0b\x32\x10.DetectionResultH\x00\x12\x17\n\x05reset\x18\x06 \x01(\x0b\x32\x06.ResetH\x00\x12!\n\nprocessing\x18\x07 \x01(\x0b\x32\x0b.ProcessingH\x00\x12\x1d\n\x08response\x18\x08 \x01(\x0b\x32\t.ResponseH\x00\x12\x14\n\x0ctimestamp_us\x18\n \x01(\x04\x42\t\n\x07message\"&\n\x05Start\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\"\x06\n\x04Stop\"\x15\n\x05Video\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\x16\n\x07Overlay\x12\x0b\n\x03svg\x18\x01 \x01(\t\";\n\x0f\x44\x65tectionResult\x12\x11\n\timagePath\x18\x01 \x01(\t\x12\x15\n\remotionResult\x18\x02 \x01(\t\"\x07\n\x05Reset\"\x0c\n\nProcessing\"\x1b\n\x08Response\x12\x0f\n\x07\x63orrect\x18\x01 \x01(\x08\x62\x06proto3')
)




_SERVERBOUND = _descriptor.Descriptor(
  name='ServerBound',
  full_name='ServerBound',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream_control', full_name='ServerBound.stream_control', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame_capture', full_name='ServerBound.frame_capture', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='ServerBound.response', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
      name='message', full_name='ServerBound.message',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=51,
  serialized_end=188,
)


_STREAMCONTROL = _descriptor.Descriptor(
  name='StreamControl',
  full_name='StreamControl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='StreamControl.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=190,
  serialized_end=222,
)


_FRAMECAPTURE = _descriptor.Descriptor(
  name='FrameCapture',
  full_name='FrameCapture',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='overlay', full_name='FrameCapture.overlay', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=224,
  serialized_end=255,
)


_CLIENTBOUND = _descriptor.Descriptor(
  name='ClientBound',
  full_name='ClientBound',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='ClientBound.start', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='ClientBound.stop', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='video', full_name='ClientBound.video', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='overlay', full_name='ClientBound.overlay', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detectionResult', full_name='ClientBound.detectionResult', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reset', full_name='ClientBound.reset', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processing', full_name='ClientBound.processing', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='ClientBound.response', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_us', full_name='ClientBound.timestamp_us', index=8,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
      name='message', full_name='ClientBound.message',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=258,
  serialized_end=542,
)


_START = _descriptor.Descriptor(
  name='Start',
  full_name='Start',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='Start.width', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='Start.height', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=544,
  serialized_end=582,
)


_STOP = _descriptor.Descriptor(
  name='Stop',
  full_name='Stop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=584,
  serialized_end=590,
)


_VIDEO = _descriptor.Descriptor(
  name='Video',
  full_name='Video',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='Video.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=592,
  serialized_end=613,
)


_OVERLAY = _descriptor.Descriptor(
  name='Overlay',
  full_name='Overlay',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='svg', full_name='Overlay.svg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=615,
  serialized_end=637,
)


_DETECTIONRESULT = _descriptor.Descriptor(
  name='DetectionResult',
  full_name='DetectionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='imagePath', full_name='DetectionResult.imagePath', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='emotionResult', full_name='DetectionResult.emotionResult', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=639,
  serialized_end=698,
)


_RESET = _descriptor.Descriptor(
  name='Reset',
  full_name='Reset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=700,
  serialized_end=707,
)


_PROCESSING = _descriptor.Descriptor(
  name='Processing',
  full_name='Processing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=709,
  serialized_end=721,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='correct', full_name='Response.correct', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=723,
  serialized_end=750,
)

_SERVERBOUND.fields_by_name['stream_control'].message_type = _STREAMCONTROL
_SERVERBOUND.fields_by_name['frame_capture'].message_type = _FRAMECAPTURE
_SERVERBOUND.fields_by_name['response'].message_type = _RESPONSE
_SERVERBOUND.oneofs_by_name['message'].fields.append(
  _SERVERBOUND.fields_by_name['stream_control'])
_SERVERBOUND.fields_by_name['stream_control'].containing_oneof = _SERVERBOUND.oneofs_by_name['message']
_SERVERBOUND.oneofs_by_name['message'].fields.append(
  _SERVERBOUND.fields_by_name['frame_capture'])
_SERVERBOUND.fields_by_name['frame_capture'].containing_oneof = _SERVERBOUND.oneofs_by_name['message']
_SERVERBOUND.oneofs_by_name['message'].fields.append(
  _SERVERBOUND.fields_by_name['response'])
_SERVERBOUND.fields_by_name['response'].containing_oneof = _SERVERBOUND.oneofs_by_name['message']
_CLIENTBOUND.fields_by_name['start'].message_type = _START
_CLIENTBOUND.fields_by_name['stop'].message_type = _STOP
_CLIENTBOUND.fields_by_name['video'].message_type = _VIDEO
_CLIENTBOUND.fields_by_name['overlay'].message_type = _OVERLAY
_CLIENTBOUND.fields_by_name['detectionResult'].message_type = _DETECTIONRESULT
_CLIENTBOUND.fields_by_name['reset'].message_type = _RESET
_CLIENTBOUND.fields_by_name['processing'].message_type = _PROCESSING
_CLIENTBOUND.fields_by_name['response'].message_type = _RESPONSE
_CLIENTBOUND.oneofs_by_name['message'].fields.append(
  _CLIENTBOUND.fields_by_name['start'])
_CLIENTBOUND.fields_by_name['start'].containing_oneof = _CLIENTBOUND.oneofs_by_name['message']
_CLIENTBOUND.oneofs_by_name['message'].fields.append(
  _CLIENTBOUND.fields_by_name['stop'])
_CLIENTBOUND.fields_by_name['stop'].containing_oneof = _CLIENTBOUND.oneofs_by_name['message']
_CLIENTBOUND.oneofs_by_name['message'].fields.append(
  _CLIENTBOUND.fields_by_name['video'])
_CLIENTBOUND.fields_by_name['video'].containing_oneof = _CLIENTBOUND.oneofs_by_name['message']
_CLIENTBOUND.oneofs_by_name['message'].fields.append(
  _CLIENTBOUND.fields_by_name['overlay'])
_CLIENTBOUND.fields_by_name['overlay'].containing_oneof = _CLIENTBOUND.oneofs_by_name['message']
_CLIENTBOUND.oneofs_by_name['message'].fields.append(
  _CLIENTBOUND.fields_by_name['detectionResult'])
_CLIENTBOUND.fields_by_name['detectionResult'].containing_oneof = _CLIENTBOUND.oneofs_by_name['message']
_CLIENTBOUND.oneofs_by_name['message'].fields.append(
  _CLIENTBOUND.fields_by_name['reset'])
_CLIENTBOUND.fields_by_name['reset'].containing_oneof = _CLIENTBOUND.oneofs_by_name['message']
_CLIENTBOUND.oneofs_by_name['message'].fields.append(
  _CLIENTBOUND.fields_by_name['processing'])
_CLIENTBOUND.fields_by_name['processing'].containing_oneof = _CLIENTBOUND.oneofs_by_name['message']
_CLIENTBOUND.oneofs_by_name['message'].fields.append(
  _CLIENTBOUND.fields_by_name['response'])
_CLIENTBOUND.fields_by_name['response'].containing_oneof = _CLIENTBOUND.oneofs_by_name['message']
DESCRIPTOR.message_types_by_name['ServerBound'] = _SERVERBOUND
DESCRIPTOR.message_types_by_name['StreamControl'] = _STREAMCONTROL
DESCRIPTOR.message_types_by_name['FrameCapture'] = _FRAMECAPTURE
DESCRIPTOR.message_types_by_name['ClientBound'] = _CLIENTBOUND
DESCRIPTOR.message_types_by_name['Start'] = _START
DESCRIPTOR.message_types_by_name['Stop'] = _STOP
DESCRIPTOR.message_types_by_name['Video'] = _VIDEO
DESCRIPTOR.message_types_by_name['Overlay'] = _OVERLAY
DESCRIPTOR.message_types_by_name['DetectionResult'] = _DETECTIONRESULT
DESCRIPTOR.message_types_by_name['Reset'] = _RESET
DESCRIPTOR.message_types_by_name['Processing'] = _PROCESSING
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServerBound = _reflection.GeneratedProtocolMessageType('ServerBound', (_message.Message,), {
  'DESCRIPTOR' : _SERVERBOUND,
  '__module__' : 'local_detector.streaming.assets.messages_pb2'
  # @@protoc_insertion_point(class_scope:ServerBound)
  })
_sym_db.RegisterMessage(ServerBound)

StreamControl = _reflection.GeneratedProtocolMessageType('StreamControl', (_message.Message,), {
  'DESCRIPTOR' : _STREAMCONTROL,
  '__module__' : 'local_detector.streaming.assets.messages_pb2'
  # @@protoc_insertion_point(class_scope:StreamControl)
  })
_sym_db.RegisterMessage(StreamControl)

FrameCapture = _reflection.GeneratedProtocolMessageType('FrameCapture', (_message.Message,), {
  'DESCRIPTOR' : _FRAMECAPTURE,
  '__module__' : 'local_detector.streaming.assets.messages_pb2'
  # @@protoc_insertion_point(class_scope:FrameCapture)
  })
_sym_db.RegisterMessage(FrameCapture)

ClientBound = _reflection.GeneratedProtocolMessageType('ClientBound', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTBOUND,
  '__module__' : 'local_detector.streaming.assets.messages_pb2'
  # @@protoc_insertion_point(class_scope:ClientBound)
  })
_sym_db.RegisterMessage(ClientBound)

Start = _reflection.GeneratedProtocolMessageType('Start', (_message.Message,), {
  'DESCRIPTOR' : _START,
  '__module__' : 'local_detector.streaming.assets.messages_pb2'
  # @@protoc_insertion_point(class_scope:Start)
  })
_sym_db.RegisterMessage(Start)

Stop = _reflection.GeneratedProtocolMessageType('Stop', (_message.Message,), {
  'DESCRIPTOR' : _STOP,
  '__module__' : 'local_detector.streaming.assets.messages_pb2'
  # @@protoc_insertion_point(class_scope:Stop)
  })
_sym_db.RegisterMessage(Stop)

Video = _reflection.GeneratedProtocolMessageType('Video', (_message.Message,), {
  'DESCRIPTOR' : _VIDEO,
  '__module__' : 'local_detector.streaming.assets.messages_pb2'
  # @@protoc_insertion_point(class_scope:Video)
  })
_sym_db.RegisterMessage(Video)

Overlay = _reflection.GeneratedProtocolMessageType('Overlay', (_message.Message,), {
  'DESCRIPTOR' : _OVERLAY,
  '__module__' : 'local_detector.streaming.assets.messages_pb2'
  # @@protoc_insertion_point(class_scope:Overlay)
  })
_sym_db.RegisterMessage(Overlay)

DetectionResult = _reflection.GeneratedProtocolMessageType('DetectionResult', (_message.Message,), {
  'DESCRIPTOR' : _DETECTIONRESULT,
  '__module__' : 'local_detector.streaming.assets.messages_pb2'
  # @@protoc_insertion_point(class_scope:DetectionResult)
  })
_sym_db.RegisterMessage(DetectionResult)

Reset = _reflection.GeneratedProtocolMessageType('Reset', (_message.Message,), {
  'DESCRIPTOR' : _RESET,
  '__module__' : 'local_detector.streaming.assets.messages_pb2'
  # @@protoc_insertion_point(class_scope:Reset)
  })
_sym_db.RegisterMessage(Reset)

Processing = _reflection.GeneratedProtocolMessageType('Processing', (_message.Message,), {
  'DESCRIPTOR' : _PROCESSING,
  '__module__' : 'local_detector.streaming.assets.messages_pb2'
  # @@protoc_insertion_point(class_scope:Processing)
  })
_sym_db.RegisterMessage(Processing)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'local_detector.streaming.assets.messages_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  })
_sym_db.RegisterMessage(Response)


# @@protoc_insertion_point(module_scope)
