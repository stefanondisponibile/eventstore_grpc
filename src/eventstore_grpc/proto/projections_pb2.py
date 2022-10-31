# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: projections.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2

from eventstore_grpc.proto import shared_pb2 as shared__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x11projections.proto\x12\x1e\x65vent_store.client.projections\x1a\x1cgoogle/protobuf/struct.proto\x1a\x0cshared.proto"\xb3\x03\n\tCreateReq\x12\x42\n\x07options\x18\x01 \x01(\x0b\x32\x31.event_store.client.projections.CreateReq.Options\x1a\xe1\x02\n\x07Options\x12-\n\x08one_time\x18\x01 \x01(\x0b\x32\x19.event_store.client.EmptyH\x00\x12P\n\ttransient\x18\x02 \x01(\x0b\x32;.event_store.client.projections.CreateReq.Options.TransientH\x00\x12R\n\ncontinuous\x18\x03 \x01(\x0b\x32<.event_store.client.projections.CreateReq.Options.ContinuousH\x00\x12\r\n\x05query\x18\x04 \x01(\t\x1a\x19\n\tTransient\x12\x0c\n\x04name\x18\x01 \x01(\t\x1aO\n\nContinuous\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x65mit_enabled\x18\x02 \x01(\x08\x12\x1d\n\x15track_emitted_streams\x18\x03 \x01(\x08\x42\x06\n\x04mode"\x0c\n\nCreateResp"\xd5\x01\n\tUpdateReq\x12\x42\n\x07options\x18\x01 \x01(\x0b\x32\x31.event_store.client.projections.UpdateReq.Options\x1a\x83\x01\n\x07Options\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05query\x18\x02 \x01(\t\x12\x16\n\x0c\x65mit_enabled\x18\x03 \x01(\x08H\x00\x12\x34\n\x0fno_emit_options\x18\x04 \x01(\x0b\x32\x19.event_store.client.EmptyH\x00\x42\r\n\x0b\x65mit_option"\x0c\n\nUpdateResp"\xc7\x01\n\tDeleteReq\x12\x42\n\x07options\x18\x01 \x01(\x0b\x32\x31.event_store.client.projections.DeleteReq.Options\x1av\n\x07Options\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1e\n\x16\x64\x65lete_emitted_streams\x18\x02 \x01(\x08\x12\x1b\n\x13\x64\x65lete_state_stream\x18\x03 \x01(\x08\x12 \n\x18\x64\x65lete_checkpoint_stream\x18\x04 \x01(\x08"\x0c\n\nDeleteResp"\xb5\x02\n\rStatisticsReq\x12\x46\n\x07options\x18\x01 \x01(\x0b\x32\x35.event_store.client.projections.StatisticsReq.Options\x1a\xdb\x01\n\x07Options\x12\x0e\n\x04name\x18\x01 \x01(\tH\x00\x12(\n\x03\x61ll\x18\x02 \x01(\x0b\x32\x19.event_store.client.EmptyH\x00\x12.\n\ttransient\x18\x03 \x01(\x0b\x32\x19.event_store.client.EmptyH\x00\x12/\n\ncontinuous\x18\x04 \x01(\x0b\x32\x19.event_store.client.EmptyH\x00\x12-\n\x08one_time\x18\x05 \x01(\x0b\x32\x19.event_store.client.EmptyH\x00\x42\x06\n\x04mode"\xb0\x04\n\x0eStatisticsResp\x12G\n\x07\x64\x65tails\x18\x01 \x01(\x0b\x32\x36.event_store.client.projections.StatisticsResp.Details\x1a\xd4\x03\n\x07\x44\x65tails\x12\x1a\n\x12\x63oreProcessingTime\x18\x01 \x01(\x03\x12\x0f\n\x07version\x18\x02 \x01(\x03\x12\r\n\x05\x65poch\x18\x03 \x01(\x03\x12\x15\n\reffectiveName\x18\x04 \x01(\t\x12\x18\n\x10writesInProgress\x18\x05 \x01(\x05\x12\x17\n\x0freadsInProgress\x18\x06 \x01(\x05\x12\x18\n\x10partitionsCached\x18\x07 \x01(\x05\x12\x0e\n\x06status\x18\x08 \x01(\t\x12\x13\n\x0bstateReason\x18\t \x01(\t\x12\x0c\n\x04name\x18\n \x01(\t\x12\x0c\n\x04mode\x18\x0b \x01(\t\x12\x10\n\x08position\x18\x0c \x01(\t\x12\x10\n\x08progress\x18\r \x01(\x02\x12\x16\n\x0elastCheckpoint\x18\x0e \x01(\t\x12#\n\x1b\x65ventsProcessedAfterRestart\x18\x0f \x01(\x03\x12\x18\n\x10\x63heckpointStatus\x18\x10 \x01(\t\x12\x16\n\x0e\x62ufferedEvents\x18\x11 \x01(\x03\x12*\n"writePendingEventsBeforeCheckpoint\x18\x12 \x01(\x05\x12)\n!writePendingEventsAfterCheckpoint\x18\x13 \x01(\x05"y\n\x08StateReq\x12\x41\n\x07options\x18\x01 \x01(\x0b\x32\x30.event_store.client.projections.StateReq.Options\x1a*\n\x07Options\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tpartition\x18\x02 \x01(\t"2\n\tStateResp\x12%\n\x05state\x18\x01 \x01(\x0b\x32\x16.google.protobuf.Value"{\n\tResultReq\x12\x42\n\x07options\x18\x01 \x01(\x0b\x32\x31.event_store.client.projections.ResultReq.Options\x1a*\n\x07Options\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tpartition\x18\x02 \x01(\t"4\n\nResultResp\x12&\n\x06result\x18\x01 \x01(\x0b\x32\x16.google.protobuf.Value"\x80\x01\n\x08ResetReq\x12\x41\n\x07options\x18\x01 \x01(\x0b\x32\x30.event_store.client.projections.ResetReq.Options\x1a\x31\n\x07Options\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10write_checkpoint\x18\x02 \x01(\x08"\x0b\n\tResetResp"h\n\tEnableReq\x12\x42\n\x07options\x18\x01 \x01(\x0b\x32\x31.event_store.client.projections.EnableReq.Options\x1a\x17\n\x07Options\x12\x0c\n\x04name\x18\x01 \x01(\t"\x0c\n\nEnableResp"\x84\x01\n\nDisableReq\x12\x43\n\x07options\x18\x01 \x01(\x0b\x32\x32.event_store.client.projections.DisableReq.Options\x1a\x31\n\x07Options\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10write_checkpoint\x18\x02 \x01(\x08"\r\n\x0b\x44isableResp2\xcb\x07\n\x0bProjections\x12_\n\x06\x43reate\x12).event_store.client.projections.CreateReq\x1a*.event_store.client.projections.CreateResp\x12_\n\x06Update\x12).event_store.client.projections.UpdateReq\x1a*.event_store.client.projections.UpdateResp\x12_\n\x06\x44\x65lete\x12).event_store.client.projections.DeleteReq\x1a*.event_store.client.projections.DeleteResp\x12m\n\nStatistics\x12-.event_store.client.projections.StatisticsReq\x1a..event_store.client.projections.StatisticsResp0\x01\x12\x62\n\x07\x44isable\x12*.event_store.client.projections.DisableReq\x1a+.event_store.client.projections.DisableResp\x12_\n\x06\x45nable\x12).event_store.client.projections.EnableReq\x1a*.event_store.client.projections.EnableResp\x12\\\n\x05Reset\x12(.event_store.client.projections.ResetReq\x1a).event_store.client.projections.ResetResp\x12\\\n\x05State\x12(.event_store.client.projections.StateReq\x1a).event_store.client.projections.StateResp\x12_\n\x06Result\x12).event_store.client.projections.ResultReq\x1a*.event_store.client.projections.ResultResp\x12H\n\x10RestartSubsystem\x12\x19.event_store.client.Empty\x1a\x19.event_store.client.EmptyB+\n)com.eventstore.dbclient.proto.projectionsb\x06proto3'
)


_CREATEREQ = DESCRIPTOR.message_types_by_name["CreateReq"]
_CREATEREQ_OPTIONS = _CREATEREQ.nested_types_by_name["Options"]
_CREATEREQ_OPTIONS_TRANSIENT = _CREATEREQ_OPTIONS.nested_types_by_name["Transient"]
_CREATEREQ_OPTIONS_CONTINUOUS = _CREATEREQ_OPTIONS.nested_types_by_name["Continuous"]
_CREATERESP = DESCRIPTOR.message_types_by_name["CreateResp"]
_UPDATEREQ = DESCRIPTOR.message_types_by_name["UpdateReq"]
_UPDATEREQ_OPTIONS = _UPDATEREQ.nested_types_by_name["Options"]
_UPDATERESP = DESCRIPTOR.message_types_by_name["UpdateResp"]
_DELETEREQ = DESCRIPTOR.message_types_by_name["DeleteReq"]
_DELETEREQ_OPTIONS = _DELETEREQ.nested_types_by_name["Options"]
_DELETERESP = DESCRIPTOR.message_types_by_name["DeleteResp"]
_STATISTICSREQ = DESCRIPTOR.message_types_by_name["StatisticsReq"]
_STATISTICSREQ_OPTIONS = _STATISTICSREQ.nested_types_by_name["Options"]
_STATISTICSRESP = DESCRIPTOR.message_types_by_name["StatisticsResp"]
_STATISTICSRESP_DETAILS = _STATISTICSRESP.nested_types_by_name["Details"]
_STATEREQ = DESCRIPTOR.message_types_by_name["StateReq"]
_STATEREQ_OPTIONS = _STATEREQ.nested_types_by_name["Options"]
_STATERESP = DESCRIPTOR.message_types_by_name["StateResp"]
_RESULTREQ = DESCRIPTOR.message_types_by_name["ResultReq"]
_RESULTREQ_OPTIONS = _RESULTREQ.nested_types_by_name["Options"]
_RESULTRESP = DESCRIPTOR.message_types_by_name["ResultResp"]
_RESETREQ = DESCRIPTOR.message_types_by_name["ResetReq"]
_RESETREQ_OPTIONS = _RESETREQ.nested_types_by_name["Options"]
_RESETRESP = DESCRIPTOR.message_types_by_name["ResetResp"]
_ENABLEREQ = DESCRIPTOR.message_types_by_name["EnableReq"]
_ENABLEREQ_OPTIONS = _ENABLEREQ.nested_types_by_name["Options"]
_ENABLERESP = DESCRIPTOR.message_types_by_name["EnableResp"]
_DISABLEREQ = DESCRIPTOR.message_types_by_name["DisableReq"]
_DISABLEREQ_OPTIONS = _DISABLEREQ.nested_types_by_name["Options"]
_DISABLERESP = DESCRIPTOR.message_types_by_name["DisableResp"]
CreateReq = _reflection.GeneratedProtocolMessageType(
    "CreateReq",
    (_message.Message,),
    {
        "Options": _reflection.GeneratedProtocolMessageType(
            "Options",
            (_message.Message,),
            {
                "Transient": _reflection.GeneratedProtocolMessageType(
                    "Transient",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _CREATEREQ_OPTIONS_TRANSIENT,
                        "__module__": "projections_pb2"
                        # @@protoc_insertion_point(class_scope:event_store.client.projections.CreateReq.Options.Transient)
                    },
                ),
                "Continuous": _reflection.GeneratedProtocolMessageType(
                    "Continuous",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _CREATEREQ_OPTIONS_CONTINUOUS,
                        "__module__": "projections_pb2"
                        # @@protoc_insertion_point(class_scope:event_store.client.projections.CreateReq.Options.Continuous)
                    },
                ),
                "DESCRIPTOR": _CREATEREQ_OPTIONS,
                "__module__": "projections_pb2"
                # @@protoc_insertion_point(class_scope:event_store.client.projections.CreateReq.Options)
            },
        ),
        "DESCRIPTOR": _CREATEREQ,
        "__module__": "projections_pb2"
        # @@protoc_insertion_point(class_scope:event_store.client.projections.CreateReq)
    },
)
_sym_db.RegisterMessage(CreateReq)
_sym_db.RegisterMessage(CreateReq.Options)
_sym_db.RegisterMessage(CreateReq.Options.Transient)
_sym_db.RegisterMessage(CreateReq.Options.Continuous)

CreateResp = _reflection.GeneratedProtocolMessageType(
    "CreateResp",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATERESP,
        "__module__": "projections_pb2"
        # @@protoc_insertion_point(class_scope:event_store.client.projections.CreateResp)
    },
)
_sym_db.RegisterMessage(CreateResp)

UpdateReq = _reflection.GeneratedProtocolMessageType(
    "UpdateReq",
    (_message.Message,),
    {
        "Options": _reflection.GeneratedProtocolMessageType(
            "Options",
            (_message.Message,),
            {
                "DESCRIPTOR": _UPDATEREQ_OPTIONS,
                "__module__": "projections_pb2"
                # @@protoc_insertion_point(class_scope:event_store.client.projections.UpdateReq.Options)
            },
        ),
        "DESCRIPTOR": _UPDATEREQ,
        "__module__": "projections_pb2"
        # @@protoc_insertion_point(class_scope:event_store.client.projections.UpdateReq)
    },
)
_sym_db.RegisterMessage(UpdateReq)
_sym_db.RegisterMessage(UpdateReq.Options)

UpdateResp = _reflection.GeneratedProtocolMessageType(
    "UpdateResp",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATERESP,
        "__module__": "projections_pb2"
        # @@protoc_insertion_point(class_scope:event_store.client.projections.UpdateResp)
    },
)
_sym_db.RegisterMessage(UpdateResp)

DeleteReq = _reflection.GeneratedProtocolMessageType(
    "DeleteReq",
    (_message.Message,),
    {
        "Options": _reflection.GeneratedProtocolMessageType(
            "Options",
            (_message.Message,),
            {
                "DESCRIPTOR": _DELETEREQ_OPTIONS,
                "__module__": "projections_pb2"
                # @@protoc_insertion_point(class_scope:event_store.client.projections.DeleteReq.Options)
            },
        ),
        "DESCRIPTOR": _DELETEREQ,
        "__module__": "projections_pb2"
        # @@protoc_insertion_point(class_scope:event_store.client.projections.DeleteReq)
    },
)
_sym_db.RegisterMessage(DeleteReq)
_sym_db.RegisterMessage(DeleteReq.Options)

DeleteResp = _reflection.GeneratedProtocolMessageType(
    "DeleteResp",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETERESP,
        "__module__": "projections_pb2"
        # @@protoc_insertion_point(class_scope:event_store.client.projections.DeleteResp)
    },
)
_sym_db.RegisterMessage(DeleteResp)

StatisticsReq = _reflection.GeneratedProtocolMessageType(
    "StatisticsReq",
    (_message.Message,),
    {
        "Options": _reflection.GeneratedProtocolMessageType(
            "Options",
            (_message.Message,),
            {
                "DESCRIPTOR": _STATISTICSREQ_OPTIONS,
                "__module__": "projections_pb2"
                # @@protoc_insertion_point(class_scope:event_store.client.projections.StatisticsReq.Options)
            },
        ),
        "DESCRIPTOR": _STATISTICSREQ,
        "__module__": "projections_pb2"
        # @@protoc_insertion_point(class_scope:event_store.client.projections.StatisticsReq)
    },
)
_sym_db.RegisterMessage(StatisticsReq)
_sym_db.RegisterMessage(StatisticsReq.Options)

StatisticsResp = _reflection.GeneratedProtocolMessageType(
    "StatisticsResp",
    (_message.Message,),
    {
        "Details": _reflection.GeneratedProtocolMessageType(
            "Details",
            (_message.Message,),
            {
                "DESCRIPTOR": _STATISTICSRESP_DETAILS,
                "__module__": "projections_pb2"
                # @@protoc_insertion_point(class_scope:event_store.client.projections.StatisticsResp.Details)
            },
        ),
        "DESCRIPTOR": _STATISTICSRESP,
        "__module__": "projections_pb2"
        # @@protoc_insertion_point(class_scope:event_store.client.projections.StatisticsResp)
    },
)
_sym_db.RegisterMessage(StatisticsResp)
_sym_db.RegisterMessage(StatisticsResp.Details)

StateReq = _reflection.GeneratedProtocolMessageType(
    "StateReq",
    (_message.Message,),
    {
        "Options": _reflection.GeneratedProtocolMessageType(
            "Options",
            (_message.Message,),
            {
                "DESCRIPTOR": _STATEREQ_OPTIONS,
                "__module__": "projections_pb2"
                # @@protoc_insertion_point(class_scope:event_store.client.projections.StateReq.Options)
            },
        ),
        "DESCRIPTOR": _STATEREQ,
        "__module__": "projections_pb2"
        # @@protoc_insertion_point(class_scope:event_store.client.projections.StateReq)
    },
)
_sym_db.RegisterMessage(StateReq)
_sym_db.RegisterMessage(StateReq.Options)

StateResp = _reflection.GeneratedProtocolMessageType(
    "StateResp",
    (_message.Message,),
    {
        "DESCRIPTOR": _STATERESP,
        "__module__": "projections_pb2"
        # @@protoc_insertion_point(class_scope:event_store.client.projections.StateResp)
    },
)
_sym_db.RegisterMessage(StateResp)

ResultReq = _reflection.GeneratedProtocolMessageType(
    "ResultReq",
    (_message.Message,),
    {
        "Options": _reflection.GeneratedProtocolMessageType(
            "Options",
            (_message.Message,),
            {
                "DESCRIPTOR": _RESULTREQ_OPTIONS,
                "__module__": "projections_pb2"
                # @@protoc_insertion_point(class_scope:event_store.client.projections.ResultReq.Options)
            },
        ),
        "DESCRIPTOR": _RESULTREQ,
        "__module__": "projections_pb2"
        # @@protoc_insertion_point(class_scope:event_store.client.projections.ResultReq)
    },
)
_sym_db.RegisterMessage(ResultReq)
_sym_db.RegisterMessage(ResultReq.Options)

ResultResp = _reflection.GeneratedProtocolMessageType(
    "ResultResp",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESULTRESP,
        "__module__": "projections_pb2"
        # @@protoc_insertion_point(class_scope:event_store.client.projections.ResultResp)
    },
)
_sym_db.RegisterMessage(ResultResp)

ResetReq = _reflection.GeneratedProtocolMessageType(
    "ResetReq",
    (_message.Message,),
    {
        "Options": _reflection.GeneratedProtocolMessageType(
            "Options",
            (_message.Message,),
            {
                "DESCRIPTOR": _RESETREQ_OPTIONS,
                "__module__": "projections_pb2"
                # @@protoc_insertion_point(class_scope:event_store.client.projections.ResetReq.Options)
            },
        ),
        "DESCRIPTOR": _RESETREQ,
        "__module__": "projections_pb2"
        # @@protoc_insertion_point(class_scope:event_store.client.projections.ResetReq)
    },
)
_sym_db.RegisterMessage(ResetReq)
_sym_db.RegisterMessage(ResetReq.Options)

ResetResp = _reflection.GeneratedProtocolMessageType(
    "ResetResp",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESETRESP,
        "__module__": "projections_pb2"
        # @@protoc_insertion_point(class_scope:event_store.client.projections.ResetResp)
    },
)
_sym_db.RegisterMessage(ResetResp)

EnableReq = _reflection.GeneratedProtocolMessageType(
    "EnableReq",
    (_message.Message,),
    {
        "Options": _reflection.GeneratedProtocolMessageType(
            "Options",
            (_message.Message,),
            {
                "DESCRIPTOR": _ENABLEREQ_OPTIONS,
                "__module__": "projections_pb2"
                # @@protoc_insertion_point(class_scope:event_store.client.projections.EnableReq.Options)
            },
        ),
        "DESCRIPTOR": _ENABLEREQ,
        "__module__": "projections_pb2"
        # @@protoc_insertion_point(class_scope:event_store.client.projections.EnableReq)
    },
)
_sym_db.RegisterMessage(EnableReq)
_sym_db.RegisterMessage(EnableReq.Options)

EnableResp = _reflection.GeneratedProtocolMessageType(
    "EnableResp",
    (_message.Message,),
    {
        "DESCRIPTOR": _ENABLERESP,
        "__module__": "projections_pb2"
        # @@protoc_insertion_point(class_scope:event_store.client.projections.EnableResp)
    },
)
_sym_db.RegisterMessage(EnableResp)

DisableReq = _reflection.GeneratedProtocolMessageType(
    "DisableReq",
    (_message.Message,),
    {
        "Options": _reflection.GeneratedProtocolMessageType(
            "Options",
            (_message.Message,),
            {
                "DESCRIPTOR": _DISABLEREQ_OPTIONS,
                "__module__": "projections_pb2"
                # @@protoc_insertion_point(class_scope:event_store.client.projections.DisableReq.Options)
            },
        ),
        "DESCRIPTOR": _DISABLEREQ,
        "__module__": "projections_pb2"
        # @@protoc_insertion_point(class_scope:event_store.client.projections.DisableReq)
    },
)
_sym_db.RegisterMessage(DisableReq)
_sym_db.RegisterMessage(DisableReq.Options)

DisableResp = _reflection.GeneratedProtocolMessageType(
    "DisableResp",
    (_message.Message,),
    {
        "DESCRIPTOR": _DISABLERESP,
        "__module__": "projections_pb2"
        # @@protoc_insertion_point(class_scope:event_store.client.projections.DisableResp)
    },
)
_sym_db.RegisterMessage(DisableResp)

_PROJECTIONS = DESCRIPTOR.services_by_name["Projections"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n)com.eventstore.dbclient.proto.projections"
    _CREATEREQ._serialized_start = 98
    _CREATEREQ._serialized_end = 533
    _CREATEREQ_OPTIONS._serialized_start = 180
    _CREATEREQ_OPTIONS._serialized_end = 533
    _CREATEREQ_OPTIONS_TRANSIENT._serialized_start = 419
    _CREATEREQ_OPTIONS_TRANSIENT._serialized_end = 444
    _CREATEREQ_OPTIONS_CONTINUOUS._serialized_start = 446
    _CREATEREQ_OPTIONS_CONTINUOUS._serialized_end = 525
    _CREATERESP._serialized_start = 535
    _CREATERESP._serialized_end = 547
    _UPDATEREQ._serialized_start = 550
    _UPDATEREQ._serialized_end = 763
    _UPDATEREQ_OPTIONS._serialized_start = 632
    _UPDATEREQ_OPTIONS._serialized_end = 763
    _UPDATERESP._serialized_start = 765
    _UPDATERESP._serialized_end = 777
    _DELETEREQ._serialized_start = 780
    _DELETEREQ._serialized_end = 979
    _DELETEREQ_OPTIONS._serialized_start = 861
    _DELETEREQ_OPTIONS._serialized_end = 979
    _DELETERESP._serialized_start = 981
    _DELETERESP._serialized_end = 993
    _STATISTICSREQ._serialized_start = 996
    _STATISTICSREQ._serialized_end = 1305
    _STATISTICSREQ_OPTIONS._serialized_start = 1086
    _STATISTICSREQ_OPTIONS._serialized_end = 1305
    _STATISTICSRESP._serialized_start = 1308
    _STATISTICSRESP._serialized_end = 1868
    _STATISTICSRESP_DETAILS._serialized_start = 1400
    _STATISTICSRESP_DETAILS._serialized_end = 1868
    _STATEREQ._serialized_start = 1870
    _STATEREQ._serialized_end = 1991
    _STATEREQ_OPTIONS._serialized_start = 1949
    _STATEREQ_OPTIONS._serialized_end = 1991
    _STATERESP._serialized_start = 1993
    _STATERESP._serialized_end = 2043
    _RESULTREQ._serialized_start = 2045
    _RESULTREQ._serialized_end = 2168
    _RESULTREQ_OPTIONS._serialized_start = 1949
    _RESULTREQ_OPTIONS._serialized_end = 1991
    _RESULTRESP._serialized_start = 2170
    _RESULTRESP._serialized_end = 2222
    _RESETREQ._serialized_start = 2225
    _RESETREQ._serialized_end = 2353
    _RESETREQ_OPTIONS._serialized_start = 2304
    _RESETREQ_OPTIONS._serialized_end = 2353
    _RESETRESP._serialized_start = 2355
    _RESETRESP._serialized_end = 2366
    _ENABLEREQ._serialized_start = 2368
    _ENABLEREQ._serialized_end = 2472
    _ENABLEREQ_OPTIONS._serialized_start = 632
    _ENABLEREQ_OPTIONS._serialized_end = 655
    _ENABLERESP._serialized_start = 2474
    _ENABLERESP._serialized_end = 2486
    _DISABLEREQ._serialized_start = 2489
    _DISABLEREQ._serialized_end = 2621
    _DISABLEREQ_OPTIONS._serialized_start = 2304
    _DISABLEREQ_OPTIONS._serialized_end = 2353
    _DISABLERESP._serialized_start = 2623
    _DISABLERESP._serialized_end = 2636
    _PROJECTIONS._serialized_start = 2639
    _PROJECTIONS._serialized_end = 3610
# @@protoc_insertion_point(module_scope)
