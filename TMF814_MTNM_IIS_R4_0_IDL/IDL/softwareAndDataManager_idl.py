# Python stubs generated by omniidl from softwareAndDataManager.idl
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

# #include "common.idl"
import common_idl
_0_common = omniORB.openModule("common")
_0_common__POA = omniORB.openModule("common__POA")

#
# Start of module "softwareAndDataManager"
#
__name__ = "softwareAndDataManager"
_0_softwareAndDataManager = omniORB.openModule("softwareAndDataManager", r"softwareAndDataManager.idl")
_0_softwareAndDataManager__POA = omniORB.openModule("softwareAndDataManager__POA", r"softwareAndDataManager.idl")


# struct BackupId_T
_0_softwareAndDataManager.BackupId_T = omniORB.newEmptyClass()
class BackupId_T (omniORB.StructBase):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/softwareAndDataManager/BackupId_T:1.0"

    def __init__(self, meName, backupTime):
        self.meName = meName
        self.backupTime = backupTime

_0_softwareAndDataManager.BackupId_T = BackupId_T
_0_softwareAndDataManager._d_BackupId_T  = (omniORB.tcInternal.tv_struct, BackupId_T, BackupId_T._NP_RepositoryId, "BackupId_T", "meName", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], "backupTime", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/Time_T:1.0"])
_0_softwareAndDataManager._tc_BackupId_T = omniORB.tcInternal.createTypeCode(_0_softwareAndDataManager._d_BackupId_T)
omniORB.registerType(BackupId_T._NP_RepositoryId, _0_softwareAndDataManager._d_BackupId_T, _0_softwareAndDataManager._tc_BackupId_T)
del BackupId_T

# typedef ... BackupIdList_T
class BackupIdList_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/softwareAndDataManager/BackupIdList_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_softwareAndDataManager.BackupIdList_T = BackupIdList_T
_0_softwareAndDataManager._d_BackupIdList_T  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/softwareAndDataManager/BackupId_T:1.0"], 0)
_0_softwareAndDataManager._ad_BackupIdList_T = (omniORB.tcInternal.tv_alias, BackupIdList_T._NP_RepositoryId, "BackupIdList_T", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/softwareAndDataManager/BackupId_T:1.0"], 0))
_0_softwareAndDataManager._tc_BackupIdList_T = omniORB.tcInternal.createTypeCode(_0_softwareAndDataManager._ad_BackupIdList_T)
omniORB.registerType(BackupIdList_T._NP_RepositoryId, _0_softwareAndDataManager._ad_BackupIdList_T, _0_softwareAndDataManager._tc_BackupIdList_T)
del BackupIdList_T

# enum Current_OperationStatus_T
_0_softwareAndDataManager.COS_Idle = omniORB.EnumItem("COS_Idle", 0)
_0_softwareAndDataManager.COS_Pending = omniORB.EnumItem("COS_Pending", 1)
_0_softwareAndDataManager.COS_InProgress = omniORB.EnumItem("COS_InProgress", 2)
_0_softwareAndDataManager.COS_Completed = omniORB.EnumItem("COS_Completed", 3)
_0_softwareAndDataManager.COS_Aborted = omniORB.EnumItem("COS_Aborted", 4)
_0_softwareAndDataManager.Current_OperationStatus_T = omniORB.Enum("IDL:mtnm.tmforum.org/softwareAndDataManager/Current_OperationStatus_T:1.0", (_0_softwareAndDataManager.COS_Idle, _0_softwareAndDataManager.COS_Pending, _0_softwareAndDataManager.COS_InProgress, _0_softwareAndDataManager.COS_Completed, _0_softwareAndDataManager.COS_Aborted,))

_0_softwareAndDataManager._d_Current_OperationStatus_T  = (omniORB.tcInternal.tv_enum, _0_softwareAndDataManager.Current_OperationStatus_T._NP_RepositoryId, "Current_OperationStatus_T", _0_softwareAndDataManager.Current_OperationStatus_T._items)
_0_softwareAndDataManager._tc_Current_OperationStatus_T = omniORB.tcInternal.createTypeCode(_0_softwareAndDataManager._d_Current_OperationStatus_T)
omniORB.registerType(_0_softwareAndDataManager.Current_OperationStatus_T._NP_RepositoryId, _0_softwareAndDataManager._d_Current_OperationStatus_T, _0_softwareAndDataManager._tc_Current_OperationStatus_T)

# struct BackupStatus_T
_0_softwareAndDataManager.BackupStatus_T = omniORB.newEmptyClass()
class BackupStatus_T (omniORB.StructBase):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/softwareAndDataManager/BackupStatus_T:1.0"

    def __init__(self, opStatus, failureReason):
        self.opStatus = opStatus
        self.failureReason = failureReason

_0_softwareAndDataManager.BackupStatus_T = BackupStatus_T
_0_softwareAndDataManager._d_BackupStatus_T  = (omniORB.tcInternal.tv_struct, BackupStatus_T, BackupStatus_T._NP_RepositoryId, "BackupStatus_T", "opStatus", omniORB.typeMapping["IDL:mtnm.tmforum.org/softwareAndDataManager/Current_OperationStatus_T:1.0"], "failureReason", (omniORB.tcInternal.tv_string,0))
_0_softwareAndDataManager._tc_BackupStatus_T = omniORB.tcInternal.createTypeCode(_0_softwareAndDataManager._d_BackupStatus_T)
omniORB.registerType(BackupStatus_T._NP_RepositoryId, _0_softwareAndDataManager._d_BackupStatus_T, _0_softwareAndDataManager._tc_BackupStatus_T)
del BackupStatus_T

# interface BackupIdIterator_I
_0_softwareAndDataManager._d_BackupIdIterator_I = (omniORB.tcInternal.tv_objref, "IDL:mtnm.tmforum.org/softwareAndDataManager/BackupIdIterator_I:1.0", "BackupIdIterator_I")
omniORB.typeMapping["IDL:mtnm.tmforum.org/softwareAndDataManager/BackupIdIterator_I:1.0"] = _0_softwareAndDataManager._d_BackupIdIterator_I
_0_softwareAndDataManager.BackupIdIterator_I = omniORB.newEmptyClass()
class BackupIdIterator_I :
    _NP_RepositoryId = _0_softwareAndDataManager._d_BackupIdIterator_I[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_softwareAndDataManager.BackupIdIterator_I = BackupIdIterator_I
_0_softwareAndDataManager._tc_BackupIdIterator_I = omniORB.tcInternal.createTypeCode(_0_softwareAndDataManager._d_BackupIdIterator_I)
omniORB.registerType(BackupIdIterator_I._NP_RepositoryId, _0_softwareAndDataManager._d_BackupIdIterator_I, _0_softwareAndDataManager._tc_BackupIdIterator_I)

# BackupIdIterator_I operations and attributes
BackupIdIterator_I._d_next_n = ((omniORB.tcInternal.tv_ulong, ), (omniORB.tcInternal.tv_boolean, omniORB.typeMapping["IDL:mtnm.tmforum.org/softwareAndDataManager/BackupIdList_T:1.0"]), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
BackupIdIterator_I._d_getLength = ((), (omniORB.tcInternal.tv_ulong, ), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
BackupIdIterator_I._d_destroy = ((), (), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})

# BackupIdIterator_I object reference
class _objref_BackupIdIterator_I (CORBA.Object):
    _NP_RepositoryId = BackupIdIterator_I._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def next_n(self, *args):
        return self._obj.invoke("next_n", _0_softwareAndDataManager.BackupIdIterator_I._d_next_n, args)

    def getLength(self, *args):
        return self._obj.invoke("getLength", _0_softwareAndDataManager.BackupIdIterator_I._d_getLength, args)

    def destroy(self, *args):
        return self._obj.invoke("destroy", _0_softwareAndDataManager.BackupIdIterator_I._d_destroy, args)

omniORB.registerObjref(BackupIdIterator_I._NP_RepositoryId, _objref_BackupIdIterator_I)
_0_softwareAndDataManager._objref_BackupIdIterator_I = _objref_BackupIdIterator_I
del BackupIdIterator_I, _objref_BackupIdIterator_I

# BackupIdIterator_I skeleton
__name__ = "softwareAndDataManager__POA"
class BackupIdIterator_I (PortableServer.Servant):
    _NP_RepositoryId = _0_softwareAndDataManager.BackupIdIterator_I._NP_RepositoryId


    _omni_op_d = {"next_n": _0_softwareAndDataManager.BackupIdIterator_I._d_next_n, "getLength": _0_softwareAndDataManager.BackupIdIterator_I._d_getLength, "destroy": _0_softwareAndDataManager.BackupIdIterator_I._d_destroy}

BackupIdIterator_I._omni_skeleton = BackupIdIterator_I
_0_softwareAndDataManager__POA.BackupIdIterator_I = BackupIdIterator_I
omniORB.registerSkeleton(BackupIdIterator_I._NP_RepositoryId, BackupIdIterator_I)
del BackupIdIterator_I
__name__ = "softwareAndDataManager"

# interface SoftwareAndDataMgr_I
_0_softwareAndDataManager._d_SoftwareAndDataMgr_I = (omniORB.tcInternal.tv_objref, "IDL:mtnm.tmforum.org/softwareAndDataManager/SoftwareAndDataMgr_I:1.0", "SoftwareAndDataMgr_I")
omniORB.typeMapping["IDL:mtnm.tmforum.org/softwareAndDataManager/SoftwareAndDataMgr_I:1.0"] = _0_softwareAndDataManager._d_SoftwareAndDataMgr_I
_0_softwareAndDataManager.SoftwareAndDataMgr_I = omniORB.newEmptyClass()
class SoftwareAndDataMgr_I (_0_common.Common_I):
    _NP_RepositoryId = _0_softwareAndDataManager._d_SoftwareAndDataMgr_I[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_softwareAndDataManager.SoftwareAndDataMgr_I = SoftwareAndDataMgr_I
_0_softwareAndDataManager._tc_SoftwareAndDataMgr_I = omniORB.tcInternal.createTypeCode(_0_softwareAndDataManager._d_SoftwareAndDataMgr_I)
omniORB.registerType(SoftwareAndDataMgr_I._NP_RepositoryId, _0_softwareAndDataManager._d_SoftwareAndDataMgr_I, _0_softwareAndDataManager._tc_SoftwareAndDataMgr_I)

# SoftwareAndDataMgr_I operations and attributes
SoftwareAndDataMgr_I._d_backupME = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], ), (), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
SoftwareAndDataMgr_I._d_getMEBackupStatus = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], ), (omniORB.typeMapping["IDL:mtnm.tmforum.org/softwareAndDataManager/BackupStatus_T:1.0"], ), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
SoftwareAndDataMgr_I._d_abortMEBackup = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], ), (), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
SoftwareAndDataMgr_I._d_getBackupList = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributesList_T:1.0"], omniORB.tcInternal.tv_ulong), (omniORB.typeMapping["IDL:mtnm.tmforum.org/softwareAndDataManager/BackupIdList_T:1.0"], omniORB.typeMapping["IDL:mtnm.tmforum.org/softwareAndDataManager/BackupIdIterator_I:1.0"]), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})

# SoftwareAndDataMgr_I object reference
class _objref_SoftwareAndDataMgr_I (_0_common._objref_Common_I):
    _NP_RepositoryId = SoftwareAndDataMgr_I._NP_RepositoryId

    def __init__(self, obj):
        _0_common._objref_Common_I.__init__(self, obj)

    def backupME(self, *args):
        return self._obj.invoke("backupME", _0_softwareAndDataManager.SoftwareAndDataMgr_I._d_backupME, args)

    def getMEBackupStatus(self, *args):
        return self._obj.invoke("getMEBackupStatus", _0_softwareAndDataManager.SoftwareAndDataMgr_I._d_getMEBackupStatus, args)

    def abortMEBackup(self, *args):
        return self._obj.invoke("abortMEBackup", _0_softwareAndDataManager.SoftwareAndDataMgr_I._d_abortMEBackup, args)

    def getBackupList(self, *args):
        return self._obj.invoke("getBackupList", _0_softwareAndDataManager.SoftwareAndDataMgr_I._d_getBackupList, args)

omniORB.registerObjref(SoftwareAndDataMgr_I._NP_RepositoryId, _objref_SoftwareAndDataMgr_I)
_0_softwareAndDataManager._objref_SoftwareAndDataMgr_I = _objref_SoftwareAndDataMgr_I
del SoftwareAndDataMgr_I, _objref_SoftwareAndDataMgr_I

# SoftwareAndDataMgr_I skeleton
__name__ = "softwareAndDataManager__POA"
class SoftwareAndDataMgr_I (_0_common__POA.Common_I):
    _NP_RepositoryId = _0_softwareAndDataManager.SoftwareAndDataMgr_I._NP_RepositoryId


    _omni_op_d = {"backupME": _0_softwareAndDataManager.SoftwareAndDataMgr_I._d_backupME, "getMEBackupStatus": _0_softwareAndDataManager.SoftwareAndDataMgr_I._d_getMEBackupStatus, "abortMEBackup": _0_softwareAndDataManager.SoftwareAndDataMgr_I._d_abortMEBackup, "getBackupList": _0_softwareAndDataManager.SoftwareAndDataMgr_I._d_getBackupList}
    _omni_op_d.update(_0_common__POA.Common_I._omni_op_d)

SoftwareAndDataMgr_I._omni_skeleton = SoftwareAndDataMgr_I
_0_softwareAndDataManager__POA.SoftwareAndDataMgr_I = SoftwareAndDataMgr_I
omniORB.registerSkeleton(SoftwareAndDataMgr_I._NP_RepositoryId, SoftwareAndDataMgr_I)
del SoftwareAndDataMgr_I
__name__ = "softwareAndDataManager"

#
# End of module "softwareAndDataManager"
#
__name__ = "softwareAndDataManager_idl"

_exported_modules = ( "softwareAndDataManager", )

# The end.