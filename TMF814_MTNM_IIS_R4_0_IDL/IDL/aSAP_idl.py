# Python stubs generated by omniidl from aSAP.idl
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


# #include "globaldefs.idl"
import globaldefs_idl
_0_globaldefs = omniORB.openModule("globaldefs")
_0_globaldefs__POA = omniORB.openModule("globaldefs__POA")

#
# Start of module "aSAP"
#
__name__ = "aSAP"
_0_aSAP = omniORB.openModule("aSAP", r"aSAP.idl")
_0_aSAP__POA = omniORB.openModule("aSAP__POA", r"aSAP.idl")


# enum AssignedSeverity_T
_0_aSAP.AS_INDETERMINATE = omniORB.EnumItem("AS_INDETERMINATE", 0)
_0_aSAP.AS_CRITICAL = omniORB.EnumItem("AS_CRITICAL", 1)
_0_aSAP.AS_MAJOR = omniORB.EnumItem("AS_MAJOR", 2)
_0_aSAP.AS_MINOR = omniORB.EnumItem("AS_MINOR", 3)
_0_aSAP.AS_WARNING = omniORB.EnumItem("AS_WARNING", 4)
_0_aSAP.AS_NONALARMED = omniORB.EnumItem("AS_NONALARMED", 5)
_0_aSAP.AS_FREE_CHOICE = omniORB.EnumItem("AS_FREE_CHOICE", 6)
_0_aSAP.AssignedSeverity_T = omniORB.Enum("IDL:mtnm.tmforum.org/aSAP/AssignedSeverity_T:1.0", (_0_aSAP.AS_INDETERMINATE, _0_aSAP.AS_CRITICAL, _0_aSAP.AS_MAJOR, _0_aSAP.AS_MINOR, _0_aSAP.AS_WARNING, _0_aSAP.AS_NONALARMED, _0_aSAP.AS_FREE_CHOICE,))

_0_aSAP._d_AssignedSeverity_T  = (omniORB.tcInternal.tv_enum, _0_aSAP.AssignedSeverity_T._NP_RepositoryId, "AssignedSeverity_T", _0_aSAP.AssignedSeverity_T._items)
_0_aSAP._tc_AssignedSeverity_T = omniORB.tcInternal.createTypeCode(_0_aSAP._d_AssignedSeverity_T)
omniORB.registerType(_0_aSAP.AssignedSeverity_T._NP_RepositoryId, _0_aSAP._d_AssignedSeverity_T, _0_aSAP._tc_AssignedSeverity_T)

# struct AlarmSeverityAssignment_T
_0_aSAP.AlarmSeverityAssignment_T = omniORB.newEmptyClass()
class AlarmSeverityAssignment_T (omniORB.StructBase):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/aSAP/AlarmSeverityAssignment_T:1.0"

    def __init__(self, probableCause, probableCauseQualifier, nativeProbableCause, serviceAffecting, serviceNonAffecting, serviceIndependentOrUnknown):
        self.probableCause = probableCause
        self.probableCauseQualifier = probableCauseQualifier
        self.nativeProbableCause = nativeProbableCause
        self.serviceAffecting = serviceAffecting
        self.serviceNonAffecting = serviceNonAffecting
        self.serviceIndependentOrUnknown = serviceIndependentOrUnknown

_0_aSAP.AlarmSeverityAssignment_T = AlarmSeverityAssignment_T
_0_aSAP._d_AlarmSeverityAssignment_T  = (omniORB.tcInternal.tv_struct, AlarmSeverityAssignment_T, AlarmSeverityAssignment_T._NP_RepositoryId, "AlarmSeverityAssignment_T", "probableCause", (omniORB.tcInternal.tv_string,0), "probableCauseQualifier", (omniORB.tcInternal.tv_string,0), "nativeProbableCause", (omniORB.tcInternal.tv_string,0), "serviceAffecting", omniORB.typeMapping["IDL:mtnm.tmforum.org/aSAP/AssignedSeverity_T:1.0"], "serviceNonAffecting", omniORB.typeMapping["IDL:mtnm.tmforum.org/aSAP/AssignedSeverity_T:1.0"], "serviceIndependentOrUnknown", omniORB.typeMapping["IDL:mtnm.tmforum.org/aSAP/AssignedSeverity_T:1.0"])
_0_aSAP._tc_AlarmSeverityAssignment_T = omniORB.tcInternal.createTypeCode(_0_aSAP._d_AlarmSeverityAssignment_T)
omniORB.registerType(AlarmSeverityAssignment_T._NP_RepositoryId, _0_aSAP._d_AlarmSeverityAssignment_T, _0_aSAP._tc_AlarmSeverityAssignment_T)
del AlarmSeverityAssignment_T

# typedef ... AlarmSeverityAssignmentList_T
class AlarmSeverityAssignmentList_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/aSAP/AlarmSeverityAssignmentList_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_aSAP.AlarmSeverityAssignmentList_T = AlarmSeverityAssignmentList_T
_0_aSAP._d_AlarmSeverityAssignmentList_T  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/aSAP/AlarmSeverityAssignment_T:1.0"], 0)
_0_aSAP._ad_AlarmSeverityAssignmentList_T = (omniORB.tcInternal.tv_alias, AlarmSeverityAssignmentList_T._NP_RepositoryId, "AlarmSeverityAssignmentList_T", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/aSAP/AlarmSeverityAssignment_T:1.0"], 0))
_0_aSAP._tc_AlarmSeverityAssignmentList_T = omniORB.tcInternal.createTypeCode(_0_aSAP._ad_AlarmSeverityAssignmentList_T)
omniORB.registerType(AlarmSeverityAssignmentList_T._NP_RepositoryId, _0_aSAP._ad_AlarmSeverityAssignmentList_T, _0_aSAP._tc_AlarmSeverityAssignmentList_T)
del AlarmSeverityAssignmentList_T

# struct ASAP_T
_0_aSAP.ASAP_T = omniORB.newEmptyClass()
class ASAP_T (omniORB.StructBase):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/aSAP/ASAP_T:1.0"

    def __init__(self, name, userLabel, nativeEMSName, owner, notModifiable, alarmSeverityAssignmentList, additionalInfo):
        self.name = name
        self.userLabel = userLabel
        self.nativeEMSName = nativeEMSName
        self.owner = owner
        self.notModifiable = notModifiable
        self.alarmSeverityAssignmentList = alarmSeverityAssignmentList
        self.additionalInfo = additionalInfo

_0_aSAP.ASAP_T = ASAP_T
_0_aSAP._d_ASAP_T  = (omniORB.tcInternal.tv_struct, ASAP_T, ASAP_T._NP_RepositoryId, "ASAP_T", "name", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], "userLabel", (omniORB.tcInternal.tv_string,0), "nativeEMSName", (omniORB.tcInternal.tv_string,0), "owner", (omniORB.tcInternal.tv_string,0), "notModifiable", omniORB.tcInternal.tv_boolean, "alarmSeverityAssignmentList", omniORB.typeMapping["IDL:mtnm.tmforum.org/aSAP/AlarmSeverityAssignmentList_T:1.0"], "additionalInfo", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"])
_0_aSAP._tc_ASAP_T = omniORB.tcInternal.createTypeCode(_0_aSAP._d_ASAP_T)
omniORB.registerType(ASAP_T._NP_RepositoryId, _0_aSAP._d_ASAP_T, _0_aSAP._tc_ASAP_T)
del ASAP_T

# typedef ... ASAPList_T
class ASAPList_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/aSAP/ASAPList_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_aSAP.ASAPList_T = ASAPList_T
_0_aSAP._d_ASAPList_T  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/aSAP/ASAP_T:1.0"], 0)
_0_aSAP._ad_ASAPList_T = (omniORB.tcInternal.tv_alias, ASAPList_T._NP_RepositoryId, "ASAPList_T", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/aSAP/ASAP_T:1.0"], 0))
_0_aSAP._tc_ASAPList_T = omniORB.tcInternal.createTypeCode(_0_aSAP._ad_ASAPList_T)
omniORB.registerType(ASAPList_T._NP_RepositoryId, _0_aSAP._ad_ASAPList_T, _0_aSAP._tc_ASAPList_T)
del ASAPList_T

# struct ASAPCreateModifyData_T
_0_aSAP.ASAPCreateModifyData_T = omniORB.newEmptyClass()
class ASAPCreateModifyData_T (omniORB.StructBase):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/aSAP/ASAPCreateModifyData_T:1.0"

    def __init__(self, userLabel, forceUniqueness, owner, alarmSeverityAssignmentList, additionalInfo):
        self.userLabel = userLabel
        self.forceUniqueness = forceUniqueness
        self.owner = owner
        self.alarmSeverityAssignmentList = alarmSeverityAssignmentList
        self.additionalInfo = additionalInfo

_0_aSAP.ASAPCreateModifyData_T = ASAPCreateModifyData_T
_0_aSAP._d_ASAPCreateModifyData_T  = (omniORB.tcInternal.tv_struct, ASAPCreateModifyData_T, ASAPCreateModifyData_T._NP_RepositoryId, "ASAPCreateModifyData_T", "userLabel", (omniORB.tcInternal.tv_string,0), "forceUniqueness", omniORB.tcInternal.tv_boolean, "owner", (omniORB.tcInternal.tv_string,0), "alarmSeverityAssignmentList", omniORB.typeMapping["IDL:mtnm.tmforum.org/aSAP/AlarmSeverityAssignmentList_T:1.0"], "additionalInfo", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"])
_0_aSAP._tc_ASAPCreateModifyData_T = omniORB.tcInternal.createTypeCode(_0_aSAP._d_ASAPCreateModifyData_T)
omniORB.registerType(ASAPCreateModifyData_T._NP_RepositoryId, _0_aSAP._d_ASAPCreateModifyData_T, _0_aSAP._tc_ASAPCreateModifyData_T)
del ASAPCreateModifyData_T

# interface ASAPIterator_I
_0_aSAP._d_ASAPIterator_I = (omniORB.tcInternal.tv_objref, "IDL:mtnm.tmforum.org/aSAP/ASAPIterator_I:1.0", "ASAPIterator_I")
omniORB.typeMapping["IDL:mtnm.tmforum.org/aSAP/ASAPIterator_I:1.0"] = _0_aSAP._d_ASAPIterator_I
_0_aSAP.ASAPIterator_I = omniORB.newEmptyClass()
class ASAPIterator_I :
    _NP_RepositoryId = _0_aSAP._d_ASAPIterator_I[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_aSAP.ASAPIterator_I = ASAPIterator_I
_0_aSAP._tc_ASAPIterator_I = omniORB.tcInternal.createTypeCode(_0_aSAP._d_ASAPIterator_I)
omniORB.registerType(ASAPIterator_I._NP_RepositoryId, _0_aSAP._d_ASAPIterator_I, _0_aSAP._tc_ASAPIterator_I)

# ASAPIterator_I operations and attributes
ASAPIterator_I._d_next_n = ((omniORB.tcInternal.tv_ulong, ), (omniORB.tcInternal.tv_boolean, omniORB.typeMapping["IDL:mtnm.tmforum.org/aSAP/ASAPList_T:1.0"]), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
ASAPIterator_I._d_getLength = ((), (omniORB.tcInternal.tv_ulong, ), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
ASAPIterator_I._d_destroy = ((), (), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})

# ASAPIterator_I object reference
class _objref_ASAPIterator_I (CORBA.Object):
    _NP_RepositoryId = ASAPIterator_I._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def next_n(self, *args):
        return self._obj.invoke("next_n", _0_aSAP.ASAPIterator_I._d_next_n, args)

    def getLength(self, *args):
        return self._obj.invoke("getLength", _0_aSAP.ASAPIterator_I._d_getLength, args)

    def destroy(self, *args):
        return self._obj.invoke("destroy", _0_aSAP.ASAPIterator_I._d_destroy, args)

omniORB.registerObjref(ASAPIterator_I._NP_RepositoryId, _objref_ASAPIterator_I)
_0_aSAP._objref_ASAPIterator_I = _objref_ASAPIterator_I
del ASAPIterator_I, _objref_ASAPIterator_I

# ASAPIterator_I skeleton
__name__ = "aSAP__POA"
class ASAPIterator_I (PortableServer.Servant):
    _NP_RepositoryId = _0_aSAP.ASAPIterator_I._NP_RepositoryId


    _omni_op_d = {"next_n": _0_aSAP.ASAPIterator_I._d_next_n, "getLength": _0_aSAP.ASAPIterator_I._d_getLength, "destroy": _0_aSAP.ASAPIterator_I._d_destroy}

ASAPIterator_I._omni_skeleton = ASAPIterator_I
_0_aSAP__POA.ASAPIterator_I = ASAPIterator_I
omniORB.registerSkeleton(ASAPIterator_I._NP_RepositoryId, ASAPIterator_I)
del ASAPIterator_I
__name__ = "aSAP"

#
# End of module "aSAP"
#
__name__ = "aSAP_idl"

_exported_modules = ( "aSAP", )

# The end.