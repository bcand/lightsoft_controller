# Python stubs generated by omniidl from guiCutThrough.idl
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
# Start of module "guiCutThrough"
#
__name__ = "guiCutThrough"
_0_guiCutThrough = omniORB.openModule("guiCutThrough", r"guiCutThrough.idl")
_0_guiCutThrough__POA = omniORB.openModule("guiCutThrough__POA", r"guiCutThrough.idl")


# enum ServerLaunchCapability_T
_0_guiCutThrough.CLIENT_LAUNCH_ONLY = omniORB.EnumItem("CLIENT_LAUNCH_ONLY", 0)
_0_guiCutThrough.SERVER_LAUNCH_CAPABLE = omniORB.EnumItem("SERVER_LAUNCH_CAPABLE", 1)
_0_guiCutThrough.ServerLaunchCapability_T = omniORB.Enum("IDL:mtnm.tmforum.org/guiCutThrough/ServerLaunchCapability_T:1.0", (_0_guiCutThrough.CLIENT_LAUNCH_ONLY, _0_guiCutThrough.SERVER_LAUNCH_CAPABLE,))

_0_guiCutThrough._d_ServerLaunchCapability_T  = (omniORB.tcInternal.tv_enum, _0_guiCutThrough.ServerLaunchCapability_T._NP_RepositoryId, "ServerLaunchCapability_T", _0_guiCutThrough.ServerLaunchCapability_T._items)
_0_guiCutThrough._tc_ServerLaunchCapability_T = omniORB.tcInternal.createTypeCode(_0_guiCutThrough._d_ServerLaunchCapability_T)
omniORB.registerType(_0_guiCutThrough.ServerLaunchCapability_T._NP_RepositoryId, _0_guiCutThrough._d_ServerLaunchCapability_T, _0_guiCutThrough._tc_ServerLaunchCapability_T)

# struct GuiCutThroughData_T
_0_guiCutThrough.GuiCutThroughData_T = omniORB.newEmptyClass()
class GuiCutThroughData_T (omniORB.StructBase):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/guiCutThrough/GuiCutThroughData_T:1.0"

    def __init__(self, gctScope, gctContext, gctCommand, additionalInfo):
        self.gctScope = gctScope
        self.gctContext = gctContext
        self.gctCommand = gctCommand
        self.additionalInfo = additionalInfo

_0_guiCutThrough.GuiCutThroughData_T = GuiCutThroughData_T
_0_guiCutThrough._d_GuiCutThroughData_T  = (omniORB.tcInternal.tv_struct, GuiCutThroughData_T, GuiCutThroughData_T._NP_RepositoryId, "GuiCutThroughData_T", "gctScope", (omniORB.tcInternal.tv_string,0), "gctContext", (omniORB.tcInternal.tv_string,0), "gctCommand", (omniORB.tcInternal.tv_string,0), "additionalInfo", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"])
_0_guiCutThrough._tc_GuiCutThroughData_T = omniORB.tcInternal.createTypeCode(_0_guiCutThrough._d_GuiCutThroughData_T)
omniORB.registerType(GuiCutThroughData_T._NP_RepositoryId, _0_guiCutThrough._d_GuiCutThroughData_T, _0_guiCutThrough._tc_GuiCutThroughData_T)
del GuiCutThroughData_T

# typedef ... GuiCutThroughDataList_T
class GuiCutThroughDataList_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/guiCutThrough/GuiCutThroughDataList_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_guiCutThrough.GuiCutThroughDataList_T = GuiCutThroughDataList_T
_0_guiCutThrough._d_GuiCutThroughDataList_T  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/guiCutThrough/GuiCutThroughData_T:1.0"], 0)
_0_guiCutThrough._ad_GuiCutThroughDataList_T = (omniORB.tcInternal.tv_alias, GuiCutThroughDataList_T._NP_RepositoryId, "GuiCutThroughDataList_T", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/guiCutThrough/GuiCutThroughData_T:1.0"], 0))
_0_guiCutThrough._tc_GuiCutThroughDataList_T = omniORB.tcInternal.createTypeCode(_0_guiCutThrough._ad_GuiCutThroughDataList_T)
omniORB.registerType(GuiCutThroughDataList_T._NP_RepositoryId, _0_guiCutThrough._ad_GuiCutThroughDataList_T, _0_guiCutThrough._tc_GuiCutThroughDataList_T)
del GuiCutThroughDataList_T

# struct GCTProfileInfo_T
_0_guiCutThrough.GCTProfileInfo_T = omniORB.newEmptyClass()
class GCTProfileInfo_T (omniORB.StructBase):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/guiCutThrough/GCTProfileInfo_T:1.0"

    def __init__(self, serverLaunchCapability, gctHostname, emsGctPlatform, guiCutThroughDataList):
        self.serverLaunchCapability = serverLaunchCapability
        self.gctHostname = gctHostname
        self.emsGctPlatform = emsGctPlatform
        self.guiCutThroughDataList = guiCutThroughDataList

_0_guiCutThrough.GCTProfileInfo_T = GCTProfileInfo_T
_0_guiCutThrough._d_GCTProfileInfo_T  = (omniORB.tcInternal.tv_struct, GCTProfileInfo_T, GCTProfileInfo_T._NP_RepositoryId, "GCTProfileInfo_T", "serverLaunchCapability", omniORB.typeMapping["IDL:mtnm.tmforum.org/guiCutThrough/ServerLaunchCapability_T:1.0"], "gctHostname", (omniORB.tcInternal.tv_string,0), "emsGctPlatform", (omniORB.tcInternal.tv_string,0), "guiCutThroughDataList", omniORB.typeMapping["IDL:mtnm.tmforum.org/guiCutThrough/GuiCutThroughDataList_T:1.0"])
_0_guiCutThrough._tc_GCTProfileInfo_T = omniORB.tcInternal.createTypeCode(_0_guiCutThrough._d_GCTProfileInfo_T)
omniORB.registerType(GCTProfileInfo_T._NP_RepositoryId, _0_guiCutThrough._d_GCTProfileInfo_T, _0_guiCutThrough._tc_GCTProfileInfo_T)
del GCTProfileInfo_T

# interface GuiCutThroughMgr_I
_0_guiCutThrough._d_GuiCutThroughMgr_I = (omniORB.tcInternal.tv_objref, "IDL:mtnm.tmforum.org/guiCutThrough/GuiCutThroughMgr_I:1.0", "GuiCutThroughMgr_I")
omniORB.typeMapping["IDL:mtnm.tmforum.org/guiCutThrough/GuiCutThroughMgr_I:1.0"] = _0_guiCutThrough._d_GuiCutThroughMgr_I
_0_guiCutThrough.GuiCutThroughMgr_I = omniORB.newEmptyClass()
class GuiCutThroughMgr_I (_0_common.Common_I):
    _NP_RepositoryId = _0_guiCutThrough._d_GuiCutThroughMgr_I[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_guiCutThrough.GuiCutThroughMgr_I = GuiCutThroughMgr_I
_0_guiCutThrough._tc_GuiCutThroughMgr_I = omniORB.tcInternal.createTypeCode(_0_guiCutThrough._d_GuiCutThroughMgr_I)
omniORB.registerType(GuiCutThroughMgr_I._NP_RepositoryId, _0_guiCutThrough._d_GuiCutThroughMgr_I, _0_guiCutThrough._tc_GuiCutThroughMgr_I)

# GuiCutThroughMgr_I operations and attributes
GuiCutThroughMgr_I._d_getGCTProfileInfo = ((), (omniORB.typeMapping["IDL:mtnm.tmforum.org/guiCutThrough/GCTProfileInfo_T:1.0"], ), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
GuiCutThroughMgr_I._d_launchGCT = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], (omniORB.tcInternal.tv_string,0), omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"], (omniORB.tcInternal.tv_string,0), omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"]), (omniORB.tcInternal.tv_boolean, omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"]), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
GuiCutThroughMgr_I._d_destroyGCT = (((omniORB.tcInternal.tv_string,0), ), (), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})

# GuiCutThroughMgr_I object reference
class _objref_GuiCutThroughMgr_I (_0_common._objref_Common_I):
    _NP_RepositoryId = GuiCutThroughMgr_I._NP_RepositoryId

    def __init__(self, obj):
        _0_common._objref_Common_I.__init__(self, obj)

    def getGCTProfileInfo(self, *args):
        return self._obj.invoke("getGCTProfileInfo", _0_guiCutThrough.GuiCutThroughMgr_I._d_getGCTProfileInfo, args)

    def launchGCT(self, *args):
        return self._obj.invoke("launchGCT", _0_guiCutThrough.GuiCutThroughMgr_I._d_launchGCT, args)

    def destroyGCT(self, *args):
        return self._obj.invoke("destroyGCT", _0_guiCutThrough.GuiCutThroughMgr_I._d_destroyGCT, args)

omniORB.registerObjref(GuiCutThroughMgr_I._NP_RepositoryId, _objref_GuiCutThroughMgr_I)
_0_guiCutThrough._objref_GuiCutThroughMgr_I = _objref_GuiCutThroughMgr_I
del GuiCutThroughMgr_I, _objref_GuiCutThroughMgr_I

# GuiCutThroughMgr_I skeleton
__name__ = "guiCutThrough__POA"
class GuiCutThroughMgr_I (_0_common__POA.Common_I):
    _NP_RepositoryId = _0_guiCutThrough.GuiCutThroughMgr_I._NP_RepositoryId


    _omni_op_d = {"getGCTProfileInfo": _0_guiCutThrough.GuiCutThroughMgr_I._d_getGCTProfileInfo, "launchGCT": _0_guiCutThrough.GuiCutThroughMgr_I._d_launchGCT, "destroyGCT": _0_guiCutThrough.GuiCutThroughMgr_I._d_destroyGCT}
    _omni_op_d.update(_0_common__POA.Common_I._omni_op_d)

GuiCutThroughMgr_I._omni_skeleton = GuiCutThroughMgr_I
_0_guiCutThrough__POA.GuiCutThroughMgr_I = GuiCutThroughMgr_I
omniORB.registerSkeleton(GuiCutThroughMgr_I._NP_RepositoryId, GuiCutThroughMgr_I)
del GuiCutThroughMgr_I
__name__ = "guiCutThrough"

#
# End of module "guiCutThrough"
#
__name__ = "guiCutThrough_idl"

_exported_modules = ( "guiCutThrough", )

# The end.
