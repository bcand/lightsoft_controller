import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA


# Python stubs generated by omniidl from globaldefs.idl
# DO NOT EDIT THIS FILE!



_omnipy.checkVersion(4,2, __file__, 1)

try:
    property
except NameError:
    def property(*args):
        return None


#
# Start of module "globaldefs"
#
__name__ = "globaldefs"
_0_globaldefs = omniORB.openModule("globaldefs", r"globaldefs.idl")
_0_globaldefs__POA = omniORB.openModule("globaldefs__POA", r"globaldefs.idl")


# struct NameAndStringValue_T
_0_globaldefs.NameAndStringValue_T = omniORB.newEmptyClass()
class NameAndStringValue_T (omniORB.StructBase):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/globaldefs/NameAndStringValue_T:1.0"

    def __init__(self, name, value):
        self.name = name
        self.value = value

_0_globaldefs.NameAndStringValue_T = NameAndStringValue_T
_0_globaldefs._d_NameAndStringValue_T  = (omniORB.tcInternal.tv_struct, NameAndStringValue_T, NameAndStringValue_T._NP_RepositoryId, "NameAndStringValue_T", "name", (omniORB.tcInternal.tv_string,0), "value", (omniORB.tcInternal.tv_string,0))
_0_globaldefs._tc_NameAndStringValue_T = omniORB.tcInternal.createTypeCode(_0_globaldefs._d_NameAndStringValue_T)
omniORB.registerType(NameAndStringValue_T._NP_RepositoryId, _0_globaldefs._d_NameAndStringValue_T, _0_globaldefs._tc_NameAndStringValue_T)

# typedef ... NVSList_T
class NVSList_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"
    def __init__(self, *args, **kw):
        self = []
        for count, thing in enumerate(args):
            print '{0}'.format(thing)
            self.append(thing)
_0_globaldefs.NVSList_T = NVSList_T
_0_globaldefs._d_NVSList_T  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NameAndStringValue_T:1.0"], 0)
_0_globaldefs._ad_NVSList_T = (omniORB.tcInternal.tv_alias, NVSList_T._NP_RepositoryId, "NVSList_T", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NameAndStringValue_T:1.0"], 0))
_0_globaldefs._tc_NVSList_T = omniORB.tcInternal.createTypeCode(_0_globaldefs._ad_NVSList_T)
omniORB.registerType(NVSList_T._NP_RepositoryId, _0_globaldefs._ad_NVSList_T, _0_globaldefs._tc_NVSList_T)

# typedef ... NamingAttributes_T
class NamingAttributes_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"
    def __init__(self, *args, **kw):
        if args:

            self = args

_0_globaldefs.NamingAttributes_T = NamingAttributes_T
_0_globaldefs._d_NamingAttributes_T  = omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"]
_0_globaldefs._ad_NamingAttributes_T = (omniORB.tcInternal.tv_alias, NamingAttributes_T._NP_RepositoryId, "NamingAttributes_T", omniORB.typeCodeMapping["IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"]._d)
_0_globaldefs._tc_NamingAttributes_T = omniORB.tcInternal.createTypeCode(_0_globaldefs._ad_NamingAttributes_T)
omniORB.registerType(NamingAttributes_T._NP_RepositoryId, _0_globaldefs._ad_NamingAttributes_T, _0_globaldefs._tc_NamingAttributes_T)

# typedef ... NamingAttributesList_T
class NamingAttributesList_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/globaldefs/NamingAttributesList_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_globaldefs.NamingAttributesList_T = NamingAttributesList_T
_0_globaldefs._d_NamingAttributesList_T  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], 0)
_0_globaldefs._ad_NamingAttributesList_T = (omniORB.tcInternal.tv_alias, NamingAttributesList_T._NP_RepositoryId, "NamingAttributesList_T", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], 0))
_0_globaldefs._tc_NamingAttributesList_T = omniORB.tcInternal.createTypeCode(_0_globaldefs._ad_NamingAttributesList_T)
omniORB.registerType(NamingAttributesList_T._NP_RepositoryId, _0_globaldefs._ad_NamingAttributesList_T, _0_globaldefs._tc_NamingAttributesList_T)
del NamingAttributesList_T

# typedef ... Time_T
class Time_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/globaldefs/Time_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_globaldefs.Time_T = Time_T
_0_globaldefs._d_Time_T  = (omniORB.tcInternal.tv_string,0)
_0_globaldefs._ad_Time_T = (omniORB.tcInternal.tv_alias, Time_T._NP_RepositoryId, "Time_T", (omniORB.tcInternal.tv_string,0))
_0_globaldefs._tc_Time_T = omniORB.tcInternal.createTypeCode(_0_globaldefs._ad_Time_T)
omniORB.registerType(Time_T._NP_RepositoryId, _0_globaldefs._ad_Time_T, _0_globaldefs._tc_Time_T)
del Time_T

# enum ConnectionDirection_T
_0_globaldefs.CD_UNI = omniORB.EnumItem("CD_UNI", 0)
_0_globaldefs.CD_BI = omniORB.EnumItem("CD_BI", 1)
_0_globaldefs.ConnectionDirection_T = omniORB.Enum("IDL:mtnm.tmforum.org/globaldefs/ConnectionDirection_T:1.0", (_0_globaldefs.CD_UNI, _0_globaldefs.CD_BI,))

_0_globaldefs._d_ConnectionDirection_T  = (omniORB.tcInternal.tv_enum, _0_globaldefs.ConnectionDirection_T._NP_RepositoryId, "ConnectionDirection_T", _0_globaldefs.ConnectionDirection_T._items)
_0_globaldefs._tc_ConnectionDirection_T = omniORB.tcInternal.createTypeCode(_0_globaldefs._d_ConnectionDirection_T)
omniORB.registerType(_0_globaldefs.ConnectionDirection_T._NP_RepositoryId, _0_globaldefs._d_ConnectionDirection_T, _0_globaldefs._tc_ConnectionDirection_T)

# enum ExceptionType_T
_0_globaldefs.EXCPT_NOT_IMPLEMENTED = omniORB.EnumItem("EXCPT_NOT_IMPLEMENTED", 0)
_0_globaldefs.EXCPT_INTERNAL_ERROR = omniORB.EnumItem("EXCPT_INTERNAL_ERROR", 1)
_0_globaldefs.EXCPT_INVALID_INPUT = omniORB.EnumItem("EXCPT_INVALID_INPUT", 2)
_0_globaldefs.EXCPT_OBJECT_IN_USE = omniORB.EnumItem("EXCPT_OBJECT_IN_USE", 3)
_0_globaldefs.EXCPT_TP_INVALID_ENDPOINT = omniORB.EnumItem("EXCPT_TP_INVALID_ENDPOINT", 4)
_0_globaldefs.EXCPT_ENTITY_NOT_FOUND = omniORB.EnumItem("EXCPT_ENTITY_NOT_FOUND", 5)
_0_globaldefs.EXCPT_TIMESLOT_IN_USE = omniORB.EnumItem("EXCPT_TIMESLOT_IN_USE", 6)
_0_globaldefs.EXCPT_PROTECTION_EFFORT_NOT_MET = omniORB.EnumItem("EXCPT_PROTECTION_EFFORT_NOT_MET", 7)
_0_globaldefs.EXCPT_NOT_IN_VALID_STATE = omniORB.EnumItem("EXCPT_NOT_IN_VALID_STATE", 8)
_0_globaldefs.EXCPT_UNABLE_TO_COMPLY = omniORB.EnumItem("EXCPT_UNABLE_TO_COMPLY", 9)
_0_globaldefs.EXCPT_NE_COMM_LOSS = omniORB.EnumItem("EXCPT_NE_COMM_LOSS", 10)
_0_globaldefs.EXCPT_CAPACITY_EXCEEDED = omniORB.EnumItem("EXCPT_CAPACITY_EXCEEDED", 11)
_0_globaldefs.EXCPT_ACCESS_DENIED = omniORB.EnumItem("EXCPT_ACCESS_DENIED", 12)
_0_globaldefs.EXCPT_TOO_MANY_OPEN_ITERATORS = omniORB.EnumItem("EXCPT_TOO_MANY_OPEN_ITERATORS", 13)
_0_globaldefs.EXCPT_UNSUPPORTED_ROUTING_CONSTRAINTS = omniORB.EnumItem("EXCPT_UNSUPPORTED_ROUTING_CONSTRAINTS", 14)
_0_globaldefs.EXCPT_USERLABEL_IN_USE = omniORB.EnumItem("EXCPT_USERLABEL_IN_USE", 15)
_0_globaldefs.ExceptionType_T = omniORB.Enum("IDL:mtnm.tmforum.org/globaldefs/ExceptionType_T:1.0", (_0_globaldefs.EXCPT_NOT_IMPLEMENTED, _0_globaldefs.EXCPT_INTERNAL_ERROR, _0_globaldefs.EXCPT_INVALID_INPUT, _0_globaldefs.EXCPT_OBJECT_IN_USE, _0_globaldefs.EXCPT_TP_INVALID_ENDPOINT, _0_globaldefs.EXCPT_ENTITY_NOT_FOUND, _0_globaldefs.EXCPT_TIMESLOT_IN_USE, _0_globaldefs.EXCPT_PROTECTION_EFFORT_NOT_MET, _0_globaldefs.EXCPT_NOT_IN_VALID_STATE, _0_globaldefs.EXCPT_UNABLE_TO_COMPLY, _0_globaldefs.EXCPT_NE_COMM_LOSS, _0_globaldefs.EXCPT_CAPACITY_EXCEEDED, _0_globaldefs.EXCPT_ACCESS_DENIED, _0_globaldefs.EXCPT_TOO_MANY_OPEN_ITERATORS, _0_globaldefs.EXCPT_UNSUPPORTED_ROUTING_CONSTRAINTS, _0_globaldefs.EXCPT_USERLABEL_IN_USE,))

_0_globaldefs._d_ExceptionType_T  = (omniORB.tcInternal.tv_enum, _0_globaldefs.ExceptionType_T._NP_RepositoryId, "ExceptionType_T", _0_globaldefs.ExceptionType_T._items)
_0_globaldefs._tc_ExceptionType_T = omniORB.tcInternal.createTypeCode(_0_globaldefs._d_ExceptionType_T)
omniORB.registerType(_0_globaldefs.ExceptionType_T._NP_RepositoryId, _0_globaldefs._d_ExceptionType_T, _0_globaldefs._tc_ExceptionType_T)

# exception ProcessingFailureException
_0_globaldefs.ProcessingFailureException = omniORB.newEmptyClass()
class ProcessingFailureException (CORBA.UserException):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/globaldefs/ProcessingFailureException:1.0"

    def __init__(self, exceptionType, errorReason):
        CORBA.UserException.__init__(self, exceptionType, errorReason)
        self.exceptionType = exceptionType
        self.errorReason = errorReason

_0_globaldefs.ProcessingFailureException = ProcessingFailureException
_0_globaldefs._d_ProcessingFailureException  = (omniORB.tcInternal.tv_except, ProcessingFailureException, ProcessingFailureException._NP_RepositoryId, "ProcessingFailureException", "exceptionType", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/ExceptionType_T:1.0"], "errorReason", (omniORB.tcInternal.tv_string,0))
_0_globaldefs._tc_ProcessingFailureException = omniORB.tcInternal.createTypeCode(_0_globaldefs._d_ProcessingFailureException)
omniORB.registerType(ProcessingFailureException._NP_RepositoryId, _0_globaldefs._d_ProcessingFailureException, _0_globaldefs._tc_ProcessingFailureException)
del ProcessingFailureException

# interface NamingAttributesIterator_I
_0_globaldefs._d_NamingAttributesIterator_I = (omniORB.tcInternal.tv_objref, "IDL:mtnm.tmforum.org/globaldefs/NamingAttributesIterator_I:1.0", "NamingAttributesIterator_I")
omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributesIterator_I:1.0"] = _0_globaldefs._d_NamingAttributesIterator_I
_0_globaldefs.NamingAttributesIterator_I = omniORB.newEmptyClass()
class NamingAttributesIterator_I :
    _NP_RepositoryId = _0_globaldefs._d_NamingAttributesIterator_I[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_globaldefs.NamingAttributesIterator_I = NamingAttributesIterator_I
_0_globaldefs._tc_NamingAttributesIterator_I = omniORB.tcInternal.createTypeCode(_0_globaldefs._d_NamingAttributesIterator_I)
omniORB.registerType(NamingAttributesIterator_I._NP_RepositoryId, _0_globaldefs._d_NamingAttributesIterator_I, _0_globaldefs._tc_NamingAttributesIterator_I)

# NamingAttributesIterator_I operations and attributes
NamingAttributesIterator_I._d_next_n = ((omniORB.tcInternal.tv_ulong, ), (omniORB.tcInternal.tv_boolean, omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributesList_T:1.0"]), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
NamingAttributesIterator_I._d_getLength = ((), (omniORB.tcInternal.tv_ulong, ), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
NamingAttributesIterator_I._d_destroy = ((), (), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})

# NamingAttributesIterator_I object reference
class _objref_NamingAttributesIterator_I (CORBA.Object):
    _NP_RepositoryId = NamingAttributesIterator_I._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def next_n(self, *args):
        return self._obj.invoke("next_n", _0_globaldefs.NamingAttributesIterator_I._d_next_n, args)

    def getLength(self, *args):
        return self._obj.invoke("getLength", _0_globaldefs.NamingAttributesIterator_I._d_getLength, args)

    def destroy(self, *args):
        return self._obj.invoke("destroy", _0_globaldefs.NamingAttributesIterator_I._d_destroy, args)

omniORB.registerObjref(NamingAttributesIterator_I._NP_RepositoryId, _objref_NamingAttributesIterator_I)
_0_globaldefs._objref_NamingAttributesIterator_I = _objref_NamingAttributesIterator_I
del NamingAttributesIterator_I, _objref_NamingAttributesIterator_I

# NamingAttributesIterator_I skeleton
__name__ = "globaldefs__POA"
class NamingAttributesIterator_I (PortableServer.Servant):
    _NP_RepositoryId = _0_globaldefs.NamingAttributesIterator_I._NP_RepositoryId


    _omni_op_d = {"next_n": _0_globaldefs.NamingAttributesIterator_I._d_next_n, "getLength": _0_globaldefs.NamingAttributesIterator_I._d_getLength, "destroy": _0_globaldefs.NamingAttributesIterator_I._d_destroy}

NamingAttributesIterator_I._omni_skeleton = NamingAttributesIterator_I
_0_globaldefs__POA.NamingAttributesIterator_I = NamingAttributesIterator_I
omniORB.registerSkeleton(NamingAttributesIterator_I._NP_RepositoryId, NamingAttributesIterator_I)
del NamingAttributesIterator_I
__name__ = "globaldefs"

#
# End of module "globaldefs"
#
__name__ = "globaldefs_idl"

_exported_modules = ( "globaldefs", )

# The end.
