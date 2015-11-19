# Python stubs generated by omniidl from DsEventLogAdmin.idl
# DO NOT EDIT THIS FILE!

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA


_omnipy.checkVersion(4,2, __file__, 1)

try:
    property
except NameError:
    def property(*args):
        return None


# #include "CosEventComm.idl"
import CosEventComm_idl
_0_CosEventComm = omniORB.openModule("CosEventComm")
_0_CosEventComm__POA = omniORB.openModule("CosEventComm__POA")

# #include "CosEventChannelAdmin.idl"
import CosEventChannelAdmin_idl
_0_CosEventChannelAdmin = omniORB.openModule("CosEventChannelAdmin")
_0_CosEventChannelAdmin__POA = omniORB.openModule("CosEventChannelAdmin__POA")

# #include "TimeBase.idl"
import TimeBase_idl
_0_TimeBase = omniORB.openModule("TimeBase")
_0_TimeBase__POA = omniORB.openModule("TimeBase__POA")

# #include "DsLogAdmin.idl"
import DsLogAdmin_idl
_0_DsLogAdmin = omniORB.openModule("DsLogAdmin")
_0_DsLogAdmin__POA = omniORB.openModule("DsLogAdmin__POA")

#
# Start of module "DsEventLogAdmin"
#
__name__ = "DsEventLogAdmin"
_0_DsEventLogAdmin = omniORB.openModule("DsEventLogAdmin", r"DsEventLogAdmin.idl")
_0_DsEventLogAdmin__POA = omniORB.openModule("DsEventLogAdmin__POA", r"DsEventLogAdmin.idl")


# interface EventLog
_0_DsEventLogAdmin._d_EventLog = (omniORB.tcInternal.tv_objref, "IDL:omg.org/DsEventLogAdmin/EventLog:1.0", "EventLog")
omniORB.typeMapping["IDL:omg.org/DsEventLogAdmin/EventLog:1.0"] = _0_DsEventLogAdmin._d_EventLog
_0_DsEventLogAdmin.EventLog = omniORB.newEmptyClass()
class EventLog (_0_DsLogAdmin.Log, _0_CosEventChannelAdmin.EventChannel):
    _NP_RepositoryId = _0_DsEventLogAdmin._d_EventLog[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_DsEventLogAdmin.EventLog = EventLog
_0_DsEventLogAdmin._tc_EventLog = omniORB.tcInternal.createTypeCode(_0_DsEventLogAdmin._d_EventLog)
omniORB.registerType(EventLog._NP_RepositoryId, _0_DsEventLogAdmin._d_EventLog, _0_DsEventLogAdmin._tc_EventLog)

# EventLog object reference
class _objref_EventLog (_0_DsLogAdmin._objref_Log, _0_CosEventChannelAdmin._objref_EventChannel):
    _NP_RepositoryId = EventLog._NP_RepositoryId

    def __init__(self, obj):
        _0_DsLogAdmin._objref_Log.__init__(self, obj)
        _0_CosEventChannelAdmin._objref_EventChannel.__init__(self, obj)

omniORB.registerObjref(EventLog._NP_RepositoryId, _objref_EventLog)
_0_DsEventLogAdmin._objref_EventLog = _objref_EventLog
del EventLog, _objref_EventLog

# EventLog skeleton
__name__ = "DsEventLogAdmin__POA"
class EventLog (_0_DsLogAdmin__POA.Log, _0_CosEventChannelAdmin__POA.EventChannel):
    _NP_RepositoryId = _0_DsEventLogAdmin.EventLog._NP_RepositoryId


    _omni_op_d = {}
    _omni_op_d.update(_0_DsLogAdmin__POA.Log._omni_op_d)
    _omni_op_d.update(_0_CosEventChannelAdmin__POA.EventChannel._omni_op_d)

EventLog._omni_skeleton = EventLog
_0_DsEventLogAdmin__POA.EventLog = EventLog
omniORB.registerSkeleton(EventLog._NP_RepositoryId, EventLog)
del EventLog
__name__ = "DsEventLogAdmin"

# interface EventLogFactory
_0_DsEventLogAdmin._d_EventLogFactory = (omniORB.tcInternal.tv_objref, "IDL:omg.org/DsEventLogAdmin/EventLogFactory:1.0", "EventLogFactory")
omniORB.typeMapping["IDL:omg.org/DsEventLogAdmin/EventLogFactory:1.0"] = _0_DsEventLogAdmin._d_EventLogFactory
_0_DsEventLogAdmin.EventLogFactory = omniORB.newEmptyClass()
class EventLogFactory (_0_DsLogAdmin.LogMgr, _0_CosEventChannelAdmin.ConsumerAdmin):
    _NP_RepositoryId = _0_DsEventLogAdmin._d_EventLogFactory[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_DsEventLogAdmin.EventLogFactory = EventLogFactory
_0_DsEventLogAdmin._tc_EventLogFactory = omniORB.tcInternal.createTypeCode(_0_DsEventLogAdmin._d_EventLogFactory)
omniORB.registerType(EventLogFactory._NP_RepositoryId, _0_DsEventLogAdmin._d_EventLogFactory, _0_DsEventLogAdmin._tc_EventLogFactory)

# EventLogFactory operations and attributes
EventLogFactory._d_create = ((omniORB.typeMapping["IDL:omg.org/DsLogAdmin/LogFullActionType:1.0"], omniORB.tcInternal.tv_ulonglong, omniORB.typeMapping["IDL:omg.org/DsLogAdmin/CapacityAlarmThresholdList:1.0"]), (omniORB.typeMapping["IDL:omg.org/DsEventLogAdmin/EventLog:1.0"], omniORB.typeMapping["IDL:omg.org/DsLogAdmin/LogId:1.0"]), {_0_DsLogAdmin.InvalidLogFullAction._NP_RepositoryId: _0_DsLogAdmin._d_InvalidLogFullAction, _0_DsLogAdmin.InvalidThreshold._NP_RepositoryId: _0_DsLogAdmin._d_InvalidThreshold})
EventLogFactory._d_create_with_id = ((omniORB.typeMapping["IDL:omg.org/DsLogAdmin/LogId:1.0"], omniORB.typeMapping["IDL:omg.org/DsLogAdmin/LogFullActionType:1.0"], omniORB.tcInternal.tv_ulonglong, omniORB.typeMapping["IDL:omg.org/DsLogAdmin/CapacityAlarmThresholdList:1.0"]), (omniORB.typeMapping["IDL:omg.org/DsEventLogAdmin/EventLog:1.0"], ), {_0_DsLogAdmin.LogIdAlreadyExists._NP_RepositoryId: _0_DsLogAdmin._d_LogIdAlreadyExists, _0_DsLogAdmin.InvalidLogFullAction._NP_RepositoryId: _0_DsLogAdmin._d_InvalidLogFullAction, _0_DsLogAdmin.InvalidThreshold._NP_RepositoryId: _0_DsLogAdmin._d_InvalidThreshold})

# EventLogFactory object reference
class _objref_EventLogFactory (_0_DsLogAdmin._objref_LogMgr, _0_CosEventChannelAdmin._objref_ConsumerAdmin):
    _NP_RepositoryId = EventLogFactory._NP_RepositoryId

    def __init__(self, obj):
        _0_DsLogAdmin._objref_LogMgr.__init__(self, obj)
        _0_CosEventChannelAdmin._objref_ConsumerAdmin.__init__(self, obj)

    def create(self, *args):
        return self._obj.invoke("create", _0_DsEventLogAdmin.EventLogFactory._d_create, args)

    def create_with_id(self, *args):
        return self._obj.invoke("create_with_id", _0_DsEventLogAdmin.EventLogFactory._d_create_with_id, args)

omniORB.registerObjref(EventLogFactory._NP_RepositoryId, _objref_EventLogFactory)
_0_DsEventLogAdmin._objref_EventLogFactory = _objref_EventLogFactory
del EventLogFactory, _objref_EventLogFactory

# EventLogFactory skeleton
__name__ = "DsEventLogAdmin__POA"
class EventLogFactory (_0_DsLogAdmin__POA.LogMgr, _0_CosEventChannelAdmin__POA.ConsumerAdmin):
    _NP_RepositoryId = _0_DsEventLogAdmin.EventLogFactory._NP_RepositoryId


    _omni_op_d = {"create": _0_DsEventLogAdmin.EventLogFactory._d_create, "create_with_id": _0_DsEventLogAdmin.EventLogFactory._d_create_with_id}
    _omni_op_d.update(_0_DsLogAdmin__POA.LogMgr._omni_op_d)
    _omni_op_d.update(_0_CosEventChannelAdmin__POA.ConsumerAdmin._omni_op_d)

EventLogFactory._omni_skeleton = EventLogFactory
_0_DsEventLogAdmin__POA.EventLogFactory = EventLogFactory
omniORB.registerSkeleton(EventLogFactory._NP_RepositoryId, EventLogFactory)
del EventLogFactory
__name__ = "DsEventLogAdmin"

#
# End of module "DsEventLogAdmin"
#
__name__ = "DsEventLogAdmin_idl"

_exported_modules = ( "DsEventLogAdmin", )

# The end.
