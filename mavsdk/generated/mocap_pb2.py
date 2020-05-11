# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mocap.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mocap.proto',
  package='mavsdk.rpc.mocap',
  syntax='proto3',
  serialized_options=b'\n\017io.mavsdk.mocapB\nMocapProto',
  serialized_pb=b'\n\x0bmocap.proto\x12\x10mavsdk.rpc.mocap\x1a\x14mavsdk_options.proto\"n\n SetVisionPositionEstimateRequest\x12J\n\x18vision_position_estimate\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.mocap.VisionPositionEstimate\"X\n!SetVisionPositionEstimateResponse\x12\x33\n\x0cmocap_result\x18\x01 \x01(\x0b\x32\x1d.mavsdk.rpc.mocap.MocapResult\"k\n\x1fSetAttitudePositionMocapRequest\x12H\n\x17\x61ttitude_position_mocap\x18\x01 \x01(\x0b\x32\'.mavsdk.rpc.mocap.AttitudePositionMocap\"W\n SetAttitudePositionMocapResponse\x12\x33\n\x0cmocap_result\x18\x01 \x01(\x0b\x32\x1d.mavsdk.rpc.mocap.MocapResult\"B\n\x12SetOdometryRequest\x12,\n\x08odometry\x18\x01 \x01(\x0b\x32\x1a.mavsdk.rpc.mocap.Odometry\"J\n\x13SetOdometryResponse\x12\x33\n\x0cmocap_result\x18\x01 \x01(\x0b\x32\x1d.mavsdk.rpc.mocap.MocapResult\"5\n\x0cPositionBody\x12\x0b\n\x03x_m\x18\x01 \x01(\x02\x12\x0b\n\x03y_m\x18\x02 \x01(\x02\x12\x0b\n\x03z_m\x18\x03 \x01(\x02\"A\n\tAngleBody\x12\x10\n\x08roll_rad\x18\x01 \x01(\x02\x12\x11\n\tpitch_rad\x18\x02 \x01(\x02\x12\x0f\n\x07yaw_rad\x18\x03 \x01(\x02\"8\n\tSpeedBody\x12\r\n\x05x_m_s\x18\x01 \x01(\x02\x12\r\n\x05y_m_s\x18\x02 \x01(\x02\x12\r\n\x05z_m_s\x18\x03 \x01(\x02\"Q\n\x13\x41ngularVelocityBody\x12\x12\n\nroll_rad_s\x18\x01 \x01(\x02\x12\x13\n\x0bpitch_rad_s\x18\x02 \x01(\x02\x12\x11\n\tyaw_rad_s\x18\x03 \x01(\x02\"\'\n\nCovariance\x12\x19\n\x11\x63ovariance_matrix\x18\x01 \x03(\x02\"8\n\nQuaternion\x12\t\n\x01w\x18\x01 \x01(\x02\x12\t\n\x01x\x18\x02 \x01(\x02\x12\t\n\x01y\x18\x03 \x01(\x02\x12\t\n\x01z\x18\x04 \x01(\x02\"\xca\x01\n\x16VisionPositionEstimate\x12\x11\n\ttime_usec\x18\x01 \x01(\x04\x12\x35\n\rposition_body\x18\x02 \x01(\x0b\x32\x1e.mavsdk.rpc.mocap.PositionBody\x12/\n\nangle_body\x18\x03 \x01(\x0b\x32\x1b.mavsdk.rpc.mocap.AngleBody\x12\x35\n\x0fpose_covariance\x18\x04 \x01(\x0b\x32\x1c.mavsdk.rpc.mocap.Covariance\"\xc1\x01\n\x15\x41ttitudePositionMocap\x12\x11\n\ttime_usec\x18\x01 \x01(\x04\x12\'\n\x01q\x18\x02 \x01(\x0b\x32\x1c.mavsdk.rpc.mocap.Quaternion\x12\x35\n\rposition_body\x18\x03 \x01(\x0b\x32\x1e.mavsdk.rpc.mocap.PositionBody\x12\x35\n\x0fpose_covariance\x18\x04 \x01(\x0b\x32\x1c.mavsdk.rpc.mocap.Covariance\"\xdb\x03\n\x08Odometry\x12\x11\n\ttime_usec\x18\x01 \x01(\x04\x12\x35\n\x08\x66rame_id\x18\x02 \x01(\x0e\x32#.mavsdk.rpc.mocap.Odometry.MavFrame\x12\x35\n\rposition_body\x18\x03 \x01(\x0b\x32\x1e.mavsdk.rpc.mocap.PositionBody\x12\'\n\x01q\x18\x04 \x01(\x0b\x32\x1c.mavsdk.rpc.mocap.Quaternion\x12/\n\nspeed_body\x18\x05 \x01(\x0b\x32\x1b.mavsdk.rpc.mocap.SpeedBody\x12\x44\n\x15\x61ngular_velocity_body\x18\x06 \x01(\x0b\x32%.mavsdk.rpc.mocap.AngularVelocityBody\x12\x35\n\x0fpose_covariance\x18\x07 \x01(\x0b\x32\x1c.mavsdk.rpc.mocap.Covariance\x12\x39\n\x13velocity_covariance\x18\x08 \x01(\x0b\x32\x1c.mavsdk.rpc.mocap.Covariance\"<\n\x08MavFrame\x12\x17\n\x13MAV_FRAME_MOCAP_NED\x10\x00\x12\x17\n\x13MAV_FRAME_LOCAL_FRD\x10\x01\"\xde\x01\n\x0bMocapResult\x12\x34\n\x06result\x18\x01 \x01(\x0e\x32$.mavsdk.rpc.mocap.MocapResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\x84\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x02\x12\x1b\n\x17RESULT_CONNECTION_ERROR\x10\x03\x12\x1f\n\x1bRESULT_INVALID_REQUEST_DATA\x10\x04\x32\x87\x03\n\x0cMocapService\x12\x8a\x01\n\x19SetVisionPositionEstimate\x12\x32.mavsdk.rpc.mocap.SetVisionPositionEstimateRequest\x1a\x33.mavsdk.rpc.mocap.SetVisionPositionEstimateResponse\"\x04\x80\xb5\x18\x01\x12\x87\x01\n\x18SetAttitudePositionMocap\x12\x31.mavsdk.rpc.mocap.SetAttitudePositionMocapRequest\x1a\x32.mavsdk.rpc.mocap.SetAttitudePositionMocapResponse\"\x04\x80\xb5\x18\x01\x12`\n\x0bSetOdometry\x12$.mavsdk.rpc.mocap.SetOdometryRequest\x1a%.mavsdk.rpc.mocap.SetOdometryResponse\"\x04\x80\xb5\x18\x01\x42\x1d\n\x0fio.mavsdk.mocapB\nMocapProtob\x06proto3'
  ,
  dependencies=[mavsdk__options__pb2.DESCRIPTOR,])



_ODOMETRY_MAVFRAME = _descriptor.EnumDescriptor(
  name='MavFrame',
  full_name='mavsdk.rpc.mocap.Odometry.MavFrame',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MAV_FRAME_MOCAP_NED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAV_FRAME_LOCAL_FRD', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1778,
  serialized_end=1838,
)
_sym_db.RegisterEnumDescriptor(_ODOMETRY_MAVFRAME)

_MOCAPRESULT_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mavsdk.rpc.mocap.MocapResult.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESULT_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_NO_SYSTEM', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_CONNECTION_ERROR', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_INVALID_REQUEST_DATA', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1931,
  serialized_end=2063,
)
_sym_db.RegisterEnumDescriptor(_MOCAPRESULT_RESULT)


_SETVISIONPOSITIONESTIMATEREQUEST = _descriptor.Descriptor(
  name='SetVisionPositionEstimateRequest',
  full_name='mavsdk.rpc.mocap.SetVisionPositionEstimateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vision_position_estimate', full_name='mavsdk.rpc.mocap.SetVisionPositionEstimateRequest.vision_position_estimate', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=55,
  serialized_end=165,
)


_SETVISIONPOSITIONESTIMATERESPONSE = _descriptor.Descriptor(
  name='SetVisionPositionEstimateResponse',
  full_name='mavsdk.rpc.mocap.SetVisionPositionEstimateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mocap_result', full_name='mavsdk.rpc.mocap.SetVisionPositionEstimateResponse.mocap_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=167,
  serialized_end=255,
)


_SETATTITUDEPOSITIONMOCAPREQUEST = _descriptor.Descriptor(
  name='SetAttitudePositionMocapRequest',
  full_name='mavsdk.rpc.mocap.SetAttitudePositionMocapRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attitude_position_mocap', full_name='mavsdk.rpc.mocap.SetAttitudePositionMocapRequest.attitude_position_mocap', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=257,
  serialized_end=364,
)


_SETATTITUDEPOSITIONMOCAPRESPONSE = _descriptor.Descriptor(
  name='SetAttitudePositionMocapResponse',
  full_name='mavsdk.rpc.mocap.SetAttitudePositionMocapResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mocap_result', full_name='mavsdk.rpc.mocap.SetAttitudePositionMocapResponse.mocap_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=366,
  serialized_end=453,
)


_SETODOMETRYREQUEST = _descriptor.Descriptor(
  name='SetOdometryRequest',
  full_name='mavsdk.rpc.mocap.SetOdometryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='odometry', full_name='mavsdk.rpc.mocap.SetOdometryRequest.odometry', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=455,
  serialized_end=521,
)


_SETODOMETRYRESPONSE = _descriptor.Descriptor(
  name='SetOdometryResponse',
  full_name='mavsdk.rpc.mocap.SetOdometryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mocap_result', full_name='mavsdk.rpc.mocap.SetOdometryResponse.mocap_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=523,
  serialized_end=597,
)


_POSITIONBODY = _descriptor.Descriptor(
  name='PositionBody',
  full_name='mavsdk.rpc.mocap.PositionBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x_m', full_name='mavsdk.rpc.mocap.PositionBody.x_m', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y_m', full_name='mavsdk.rpc.mocap.PositionBody.y_m', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z_m', full_name='mavsdk.rpc.mocap.PositionBody.z_m', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=599,
  serialized_end=652,
)


_ANGLEBODY = _descriptor.Descriptor(
  name='AngleBody',
  full_name='mavsdk.rpc.mocap.AngleBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roll_rad', full_name='mavsdk.rpc.mocap.AngleBody.roll_rad', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pitch_rad', full_name='mavsdk.rpc.mocap.AngleBody.pitch_rad', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yaw_rad', full_name='mavsdk.rpc.mocap.AngleBody.yaw_rad', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=654,
  serialized_end=719,
)


_SPEEDBODY = _descriptor.Descriptor(
  name='SpeedBody',
  full_name='mavsdk.rpc.mocap.SpeedBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x_m_s', full_name='mavsdk.rpc.mocap.SpeedBody.x_m_s', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y_m_s', full_name='mavsdk.rpc.mocap.SpeedBody.y_m_s', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z_m_s', full_name='mavsdk.rpc.mocap.SpeedBody.z_m_s', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=721,
  serialized_end=777,
)


_ANGULARVELOCITYBODY = _descriptor.Descriptor(
  name='AngularVelocityBody',
  full_name='mavsdk.rpc.mocap.AngularVelocityBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roll_rad_s', full_name='mavsdk.rpc.mocap.AngularVelocityBody.roll_rad_s', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pitch_rad_s', full_name='mavsdk.rpc.mocap.AngularVelocityBody.pitch_rad_s', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yaw_rad_s', full_name='mavsdk.rpc.mocap.AngularVelocityBody.yaw_rad_s', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=779,
  serialized_end=860,
)


_COVARIANCE = _descriptor.Descriptor(
  name='Covariance',
  full_name='mavsdk.rpc.mocap.Covariance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='covariance_matrix', full_name='mavsdk.rpc.mocap.Covariance.covariance_matrix', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=862,
  serialized_end=901,
)


_QUATERNION = _descriptor.Descriptor(
  name='Quaternion',
  full_name='mavsdk.rpc.mocap.Quaternion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='w', full_name='mavsdk.rpc.mocap.Quaternion.w', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='mavsdk.rpc.mocap.Quaternion.x', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='mavsdk.rpc.mocap.Quaternion.y', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='mavsdk.rpc.mocap.Quaternion.z', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=903,
  serialized_end=959,
)


_VISIONPOSITIONESTIMATE = _descriptor.Descriptor(
  name='VisionPositionEstimate',
  full_name='mavsdk.rpc.mocap.VisionPositionEstimate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_usec', full_name='mavsdk.rpc.mocap.VisionPositionEstimate.time_usec', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position_body', full_name='mavsdk.rpc.mocap.VisionPositionEstimate.position_body', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angle_body', full_name='mavsdk.rpc.mocap.VisionPositionEstimate.angle_body', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pose_covariance', full_name='mavsdk.rpc.mocap.VisionPositionEstimate.pose_covariance', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=962,
  serialized_end=1164,
)


_ATTITUDEPOSITIONMOCAP = _descriptor.Descriptor(
  name='AttitudePositionMocap',
  full_name='mavsdk.rpc.mocap.AttitudePositionMocap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_usec', full_name='mavsdk.rpc.mocap.AttitudePositionMocap.time_usec', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='q', full_name='mavsdk.rpc.mocap.AttitudePositionMocap.q', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position_body', full_name='mavsdk.rpc.mocap.AttitudePositionMocap.position_body', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pose_covariance', full_name='mavsdk.rpc.mocap.AttitudePositionMocap.pose_covariance', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=1167,
  serialized_end=1360,
)


_ODOMETRY = _descriptor.Descriptor(
  name='Odometry',
  full_name='mavsdk.rpc.mocap.Odometry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_usec', full_name='mavsdk.rpc.mocap.Odometry.time_usec', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame_id', full_name='mavsdk.rpc.mocap.Odometry.frame_id', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position_body', full_name='mavsdk.rpc.mocap.Odometry.position_body', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='q', full_name='mavsdk.rpc.mocap.Odometry.q', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speed_body', full_name='mavsdk.rpc.mocap.Odometry.speed_body', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular_velocity_body', full_name='mavsdk.rpc.mocap.Odometry.angular_velocity_body', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pose_covariance', full_name='mavsdk.rpc.mocap.Odometry.pose_covariance', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velocity_covariance', full_name='mavsdk.rpc.mocap.Odometry.velocity_covariance', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ODOMETRY_MAVFRAME,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1363,
  serialized_end=1838,
)


_MOCAPRESULT = _descriptor.Descriptor(
  name='MocapResult',
  full_name='mavsdk.rpc.mocap.MocapResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mavsdk.rpc.mocap.MocapResult.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result_str', full_name='mavsdk.rpc.mocap.MocapResult.result_str', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MOCAPRESULT_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1841,
  serialized_end=2063,
)

_SETVISIONPOSITIONESTIMATEREQUEST.fields_by_name['vision_position_estimate'].message_type = _VISIONPOSITIONESTIMATE
_SETVISIONPOSITIONESTIMATERESPONSE.fields_by_name['mocap_result'].message_type = _MOCAPRESULT
_SETATTITUDEPOSITIONMOCAPREQUEST.fields_by_name['attitude_position_mocap'].message_type = _ATTITUDEPOSITIONMOCAP
_SETATTITUDEPOSITIONMOCAPRESPONSE.fields_by_name['mocap_result'].message_type = _MOCAPRESULT
_SETODOMETRYREQUEST.fields_by_name['odometry'].message_type = _ODOMETRY
_SETODOMETRYRESPONSE.fields_by_name['mocap_result'].message_type = _MOCAPRESULT
_VISIONPOSITIONESTIMATE.fields_by_name['position_body'].message_type = _POSITIONBODY
_VISIONPOSITIONESTIMATE.fields_by_name['angle_body'].message_type = _ANGLEBODY
_VISIONPOSITIONESTIMATE.fields_by_name['pose_covariance'].message_type = _COVARIANCE
_ATTITUDEPOSITIONMOCAP.fields_by_name['q'].message_type = _QUATERNION
_ATTITUDEPOSITIONMOCAP.fields_by_name['position_body'].message_type = _POSITIONBODY
_ATTITUDEPOSITIONMOCAP.fields_by_name['pose_covariance'].message_type = _COVARIANCE
_ODOMETRY.fields_by_name['frame_id'].enum_type = _ODOMETRY_MAVFRAME
_ODOMETRY.fields_by_name['position_body'].message_type = _POSITIONBODY
_ODOMETRY.fields_by_name['q'].message_type = _QUATERNION
_ODOMETRY.fields_by_name['speed_body'].message_type = _SPEEDBODY
_ODOMETRY.fields_by_name['angular_velocity_body'].message_type = _ANGULARVELOCITYBODY
_ODOMETRY.fields_by_name['pose_covariance'].message_type = _COVARIANCE
_ODOMETRY.fields_by_name['velocity_covariance'].message_type = _COVARIANCE
_ODOMETRY_MAVFRAME.containing_type = _ODOMETRY
_MOCAPRESULT.fields_by_name['result'].enum_type = _MOCAPRESULT_RESULT
_MOCAPRESULT_RESULT.containing_type = _MOCAPRESULT
DESCRIPTOR.message_types_by_name['SetVisionPositionEstimateRequest'] = _SETVISIONPOSITIONESTIMATEREQUEST
DESCRIPTOR.message_types_by_name['SetVisionPositionEstimateResponse'] = _SETVISIONPOSITIONESTIMATERESPONSE
DESCRIPTOR.message_types_by_name['SetAttitudePositionMocapRequest'] = _SETATTITUDEPOSITIONMOCAPREQUEST
DESCRIPTOR.message_types_by_name['SetAttitudePositionMocapResponse'] = _SETATTITUDEPOSITIONMOCAPRESPONSE
DESCRIPTOR.message_types_by_name['SetOdometryRequest'] = _SETODOMETRYREQUEST
DESCRIPTOR.message_types_by_name['SetOdometryResponse'] = _SETODOMETRYRESPONSE
DESCRIPTOR.message_types_by_name['PositionBody'] = _POSITIONBODY
DESCRIPTOR.message_types_by_name['AngleBody'] = _ANGLEBODY
DESCRIPTOR.message_types_by_name['SpeedBody'] = _SPEEDBODY
DESCRIPTOR.message_types_by_name['AngularVelocityBody'] = _ANGULARVELOCITYBODY
DESCRIPTOR.message_types_by_name['Covariance'] = _COVARIANCE
DESCRIPTOR.message_types_by_name['Quaternion'] = _QUATERNION
DESCRIPTOR.message_types_by_name['VisionPositionEstimate'] = _VISIONPOSITIONESTIMATE
DESCRIPTOR.message_types_by_name['AttitudePositionMocap'] = _ATTITUDEPOSITIONMOCAP
DESCRIPTOR.message_types_by_name['Odometry'] = _ODOMETRY
DESCRIPTOR.message_types_by_name['MocapResult'] = _MOCAPRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetVisionPositionEstimateRequest = _reflection.GeneratedProtocolMessageType('SetVisionPositionEstimateRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETVISIONPOSITIONESTIMATEREQUEST,
  '__module__' : 'mocap_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mocap.SetVisionPositionEstimateRequest)
  })
_sym_db.RegisterMessage(SetVisionPositionEstimateRequest)

SetVisionPositionEstimateResponse = _reflection.GeneratedProtocolMessageType('SetVisionPositionEstimateResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETVISIONPOSITIONESTIMATERESPONSE,
  '__module__' : 'mocap_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mocap.SetVisionPositionEstimateResponse)
  })
_sym_db.RegisterMessage(SetVisionPositionEstimateResponse)

SetAttitudePositionMocapRequest = _reflection.GeneratedProtocolMessageType('SetAttitudePositionMocapRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETATTITUDEPOSITIONMOCAPREQUEST,
  '__module__' : 'mocap_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mocap.SetAttitudePositionMocapRequest)
  })
_sym_db.RegisterMessage(SetAttitudePositionMocapRequest)

SetAttitudePositionMocapResponse = _reflection.GeneratedProtocolMessageType('SetAttitudePositionMocapResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETATTITUDEPOSITIONMOCAPRESPONSE,
  '__module__' : 'mocap_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mocap.SetAttitudePositionMocapResponse)
  })
_sym_db.RegisterMessage(SetAttitudePositionMocapResponse)

SetOdometryRequest = _reflection.GeneratedProtocolMessageType('SetOdometryRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETODOMETRYREQUEST,
  '__module__' : 'mocap_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mocap.SetOdometryRequest)
  })
_sym_db.RegisterMessage(SetOdometryRequest)

SetOdometryResponse = _reflection.GeneratedProtocolMessageType('SetOdometryResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETODOMETRYRESPONSE,
  '__module__' : 'mocap_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mocap.SetOdometryResponse)
  })
_sym_db.RegisterMessage(SetOdometryResponse)

PositionBody = _reflection.GeneratedProtocolMessageType('PositionBody', (_message.Message,), {
  'DESCRIPTOR' : _POSITIONBODY,
  '__module__' : 'mocap_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mocap.PositionBody)
  })
_sym_db.RegisterMessage(PositionBody)

AngleBody = _reflection.GeneratedProtocolMessageType('AngleBody', (_message.Message,), {
  'DESCRIPTOR' : _ANGLEBODY,
  '__module__' : 'mocap_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mocap.AngleBody)
  })
_sym_db.RegisterMessage(AngleBody)

SpeedBody = _reflection.GeneratedProtocolMessageType('SpeedBody', (_message.Message,), {
  'DESCRIPTOR' : _SPEEDBODY,
  '__module__' : 'mocap_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mocap.SpeedBody)
  })
_sym_db.RegisterMessage(SpeedBody)

AngularVelocityBody = _reflection.GeneratedProtocolMessageType('AngularVelocityBody', (_message.Message,), {
  'DESCRIPTOR' : _ANGULARVELOCITYBODY,
  '__module__' : 'mocap_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mocap.AngularVelocityBody)
  })
_sym_db.RegisterMessage(AngularVelocityBody)

Covariance = _reflection.GeneratedProtocolMessageType('Covariance', (_message.Message,), {
  'DESCRIPTOR' : _COVARIANCE,
  '__module__' : 'mocap_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mocap.Covariance)
  })
_sym_db.RegisterMessage(Covariance)

Quaternion = _reflection.GeneratedProtocolMessageType('Quaternion', (_message.Message,), {
  'DESCRIPTOR' : _QUATERNION,
  '__module__' : 'mocap_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mocap.Quaternion)
  })
_sym_db.RegisterMessage(Quaternion)

VisionPositionEstimate = _reflection.GeneratedProtocolMessageType('VisionPositionEstimate', (_message.Message,), {
  'DESCRIPTOR' : _VISIONPOSITIONESTIMATE,
  '__module__' : 'mocap_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mocap.VisionPositionEstimate)
  })
_sym_db.RegisterMessage(VisionPositionEstimate)

AttitudePositionMocap = _reflection.GeneratedProtocolMessageType('AttitudePositionMocap', (_message.Message,), {
  'DESCRIPTOR' : _ATTITUDEPOSITIONMOCAP,
  '__module__' : 'mocap_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mocap.AttitudePositionMocap)
  })
_sym_db.RegisterMessage(AttitudePositionMocap)

Odometry = _reflection.GeneratedProtocolMessageType('Odometry', (_message.Message,), {
  'DESCRIPTOR' : _ODOMETRY,
  '__module__' : 'mocap_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mocap.Odometry)
  })
_sym_db.RegisterMessage(Odometry)

MocapResult = _reflection.GeneratedProtocolMessageType('MocapResult', (_message.Message,), {
  'DESCRIPTOR' : _MOCAPRESULT,
  '__module__' : 'mocap_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mocap.MocapResult)
  })
_sym_db.RegisterMessage(MocapResult)


DESCRIPTOR._options = None

_MOCAPSERVICE = _descriptor.ServiceDescriptor(
  name='MocapService',
  full_name='mavsdk.rpc.mocap.MocapService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=2066,
  serialized_end=2457,
  methods=[
  _descriptor.MethodDescriptor(
    name='SetVisionPositionEstimate',
    full_name='mavsdk.rpc.mocap.MocapService.SetVisionPositionEstimate',
    index=0,
    containing_service=None,
    input_type=_SETVISIONPOSITIONESTIMATEREQUEST,
    output_type=_SETVISIONPOSITIONESTIMATERESPONSE,
    serialized_options=b'\200\265\030\001',
  ),
  _descriptor.MethodDescriptor(
    name='SetAttitudePositionMocap',
    full_name='mavsdk.rpc.mocap.MocapService.SetAttitudePositionMocap',
    index=1,
    containing_service=None,
    input_type=_SETATTITUDEPOSITIONMOCAPREQUEST,
    output_type=_SETATTITUDEPOSITIONMOCAPRESPONSE,
    serialized_options=b'\200\265\030\001',
  ),
  _descriptor.MethodDescriptor(
    name='SetOdometry',
    full_name='mavsdk.rpc.mocap.MocapService.SetOdometry',
    index=2,
    containing_service=None,
    input_type=_SETODOMETRYREQUEST,
    output_type=_SETODOMETRYRESPONSE,
    serialized_options=b'\200\265\030\001',
  ),
])
_sym_db.RegisterServiceDescriptor(_MOCAPSERVICE)

DESCRIPTOR.services_by_name['MocapService'] = _MOCAPSERVICE

# @@protoc_insertion_point(module_scope)
