# Python stubs generated by omniidl from trafficConditioningProfile.idl
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

# #include "transmissionParameters.idl"
import transmissionParameters_idl
_0_transmissionParameters = omniORB.openModule("transmissionParameters")
_0_transmissionParameters__POA = omniORB.openModule("transmissionParameters__POA")

# #include "terminationPoint.idl"
import terminationPoint_idl
_0_terminationPoint = omniORB.openModule("terminationPoint")
_0_terminationPoint__POA = omniORB.openModule("terminationPoint__POA")

# #include "common.idl"
import common_idl
_0_common = omniORB.openModule("common")
_0_common__POA = omniORB.openModule("common__POA")

# #include "subnetworkConnection.idl"
import subnetworkConnection_idl
_0_subnetworkConnection = omniORB.openModule("subnetworkConnection")
_0_subnetworkConnection__POA = omniORB.openModule("subnetworkConnection__POA")

# #include "performance.idl"
import performance_idl
_0_performance = omniORB.openModule("performance")
_0_performance__POA = omniORB.openModule("performance__POA")

# #include "flowDomainFragment.idl"
import flowDomainFragment_idl
_0_flowDomainFragment = omniORB.openModule("flowDomainFragment")
_0_flowDomainFragment__POA = omniORB.openModule("flowDomainFragment__POA")

# #include "topologicalLink.idl"
import topologicalLink_idl
_0_topologicalLink = omniORB.openModule("topologicalLink")
_0_topologicalLink__POA = omniORB.openModule("topologicalLink__POA")

# #include "flowDomain.idl"
import flowDomain_idl
_0_flowDomain = omniORB.openModule("flowDomain")
_0_flowDomain__POA = omniORB.openModule("flowDomain__POA")

# #include "transmissionDescriptor.idl"
import transmissionDescriptor_idl
_0_transmissionDescriptor = omniORB.openModule("transmissionDescriptor")
_0_transmissionDescriptor__POA = omniORB.openModule("transmissionDescriptor__POA")

#
# Start of module "trafficConditioningProfile"
#
__name__ = "trafficConditioningProfile"
_0_trafficConditioningProfile = omniORB.openModule("trafficConditioningProfile", r"trafficConditioningProfile.idl")
_0_trafficConditioningProfile__POA = omniORB.openModule("trafficConditioningProfile__POA", r"trafficConditioningProfile.idl")


# struct TCProfile_T
_0_trafficConditioningProfile.TCProfile_T = omniORB.newEmptyClass()
class TCProfile_T (omniORB.StructBase):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/trafficConditioningProfile/TCProfile_T:1.0"

    def __init__(self, name, userLabel, nativeEMSName, owner, defaultProfile, transmissionParams, additionalInfo):
        self.name = name
        self.userLabel = userLabel
        self.nativeEMSName = nativeEMSName
        self.owner = owner
        self.defaultProfile = defaultProfile
        self.transmissionParams = transmissionParams
        self.additionalInfo = additionalInfo

_0_trafficConditioningProfile.TCProfile_T = TCProfile_T
_0_trafficConditioningProfile._d_TCProfile_T  = (omniORB.tcInternal.tv_struct, TCProfile_T, TCProfile_T._NP_RepositoryId, "TCProfile_T", "name", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], "userLabel", (omniORB.tcInternal.tv_string,0), "nativeEMSName", (omniORB.tcInternal.tv_string,0), "owner", (omniORB.tcInternal.tv_string,0), "defaultProfile", omniORB.tcInternal.tv_boolean, "transmissionParams", omniORB.typeMapping["IDL:mtnm.tmforum.org/transmissionParameters/LayeredParameterList_T:1.0"], "additionalInfo", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"])
_0_trafficConditioningProfile._tc_TCProfile_T = omniORB.tcInternal.createTypeCode(_0_trafficConditioningProfile._d_TCProfile_T)
omniORB.registerType(TCProfile_T._NP_RepositoryId, _0_trafficConditioningProfile._d_TCProfile_T, _0_trafficConditioningProfile._tc_TCProfile_T)
del TCProfile_T

# struct TCProfileCreateData_T
_0_trafficConditioningProfile.TCProfileCreateData_T = omniORB.newEmptyClass()
class TCProfileCreateData_T (omniORB.StructBase):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/trafficConditioningProfile/TCProfileCreateData_T:1.0"

    def __init__(self, userLabel, forceUniqueness, owner, transmissionParams, additionalCreationInfo):
        self.userLabel = userLabel
        self.forceUniqueness = forceUniqueness
        self.owner = owner
        self.transmissionParams = transmissionParams
        self.additionalCreationInfo = additionalCreationInfo

_0_trafficConditioningProfile.TCProfileCreateData_T = TCProfileCreateData_T
_0_trafficConditioningProfile._d_TCProfileCreateData_T  = (omniORB.tcInternal.tv_struct, TCProfileCreateData_T, TCProfileCreateData_T._NP_RepositoryId, "TCProfileCreateData_T", "userLabel", (omniORB.tcInternal.tv_string,0), "forceUniqueness", omniORB.tcInternal.tv_boolean, "owner", (omniORB.tcInternal.tv_string,0), "transmissionParams", omniORB.typeMapping["IDL:mtnm.tmforum.org/transmissionParameters/LayeredParameterList_T:1.0"], "additionalCreationInfo", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"])
_0_trafficConditioningProfile._tc_TCProfileCreateData_T = omniORB.tcInternal.createTypeCode(_0_trafficConditioningProfile._d_TCProfileCreateData_T)
omniORB.registerType(TCProfileCreateData_T._NP_RepositoryId, _0_trafficConditioningProfile._d_TCProfileCreateData_T, _0_trafficConditioningProfile._tc_TCProfileCreateData_T)
del TCProfileCreateData_T

# typedef ... TCProfileList_T
class TCProfileList_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/trafficConditioningProfile/TCProfileList_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_trafficConditioningProfile.TCProfileList_T = TCProfileList_T
_0_trafficConditioningProfile._d_TCProfileList_T  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/trafficConditioningProfile/TCProfile_T:1.0"], 0)
_0_trafficConditioningProfile._ad_TCProfileList_T = (omniORB.tcInternal.tv_alias, TCProfileList_T._NP_RepositoryId, "TCProfileList_T", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/trafficConditioningProfile/TCProfile_T:1.0"], 0))
_0_trafficConditioningProfile._tc_TCProfileList_T = omniORB.tcInternal.createTypeCode(_0_trafficConditioningProfile._ad_TCProfileList_T)
omniORB.registerType(TCProfileList_T._NP_RepositoryId, _0_trafficConditioningProfile._ad_TCProfileList_T, _0_trafficConditioningProfile._tc_TCProfileList_T)
del TCProfileList_T

# interface TCProfileIterator_I
_0_trafficConditioningProfile._d_TCProfileIterator_I = (omniORB.tcInternal.tv_objref, "IDL:mtnm.tmforum.org/trafficConditioningProfile/TCProfileIterator_I:1.0", "TCProfileIterator_I")
omniORB.typeMapping["IDL:mtnm.tmforum.org/trafficConditioningProfile/TCProfileIterator_I:1.0"] = _0_trafficConditioningProfile._d_TCProfileIterator_I
_0_trafficConditioningProfile.TCProfileIterator_I = omniORB.newEmptyClass()
class TCProfileIterator_I :
    _NP_RepositoryId = _0_trafficConditioningProfile._d_TCProfileIterator_I[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_trafficConditioningProfile.TCProfileIterator_I = TCProfileIterator_I
_0_trafficConditioningProfile._tc_TCProfileIterator_I = omniORB.tcInternal.createTypeCode(_0_trafficConditioningProfile._d_TCProfileIterator_I)
omniORB.registerType(TCProfileIterator_I._NP_RepositoryId, _0_trafficConditioningProfile._d_TCProfileIterator_I, _0_trafficConditioningProfile._tc_TCProfileIterator_I)

# TCProfileIterator_I operations and attributes
TCProfileIterator_I._d_next_n = ((omniORB.tcInternal.tv_ulong, ), (omniORB.tcInternal.tv_boolean, omniORB.typeMapping["IDL:mtnm.tmforum.org/trafficConditioningProfile/TCProfileList_T:1.0"]), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
TCProfileIterator_I._d_getLength = ((), (omniORB.tcInternal.tv_ulong, ), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
TCProfileIterator_I._d_destroy = ((), (), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})

# TCProfileIterator_I object reference
class _objref_TCProfileIterator_I (CORBA.Object):
    _NP_RepositoryId = TCProfileIterator_I._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def next_n(self, *args):
        return self._obj.invoke("next_n", _0_trafficConditioningProfile.TCProfileIterator_I._d_next_n, args)

    def getLength(self, *args):
        return self._obj.invoke("getLength", _0_trafficConditioningProfile.TCProfileIterator_I._d_getLength, args)

    def destroy(self, *args):
        return self._obj.invoke("destroy", _0_trafficConditioningProfile.TCProfileIterator_I._d_destroy, args)

omniORB.registerObjref(TCProfileIterator_I._NP_RepositoryId, _objref_TCProfileIterator_I)
_0_trafficConditioningProfile._objref_TCProfileIterator_I = _objref_TCProfileIterator_I
del TCProfileIterator_I, _objref_TCProfileIterator_I

# TCProfileIterator_I skeleton
__name__ = "trafficConditioningProfile__POA"
class TCProfileIterator_I (PortableServer.Servant):
    _NP_RepositoryId = _0_trafficConditioningProfile.TCProfileIterator_I._NP_RepositoryId


    _omni_op_d = {"next_n": _0_trafficConditioningProfile.TCProfileIterator_I._d_next_n, "getLength": _0_trafficConditioningProfile.TCProfileIterator_I._d_getLength, "destroy": _0_trafficConditioningProfile.TCProfileIterator_I._d_destroy}

TCProfileIterator_I._omni_skeleton = TCProfileIterator_I
_0_trafficConditioningProfile__POA.TCProfileIterator_I = TCProfileIterator_I
omniORB.registerSkeleton(TCProfileIterator_I._NP_RepositoryId, TCProfileIterator_I)
del TCProfileIterator_I
__name__ = "trafficConditioningProfile"

# interface TCProfileMgr_I
_0_trafficConditioningProfile._d_TCProfileMgr_I = (omniORB.tcInternal.tv_objref, "IDL:mtnm.tmforum.org/trafficConditioningProfile/TCProfileMgr_I:1.0", "TCProfileMgr_I")
omniORB.typeMapping["IDL:mtnm.tmforum.org/trafficConditioningProfile/TCProfileMgr_I:1.0"] = _0_trafficConditioningProfile._d_TCProfileMgr_I
_0_trafficConditioningProfile.TCProfileMgr_I = omniORB.newEmptyClass()
class TCProfileMgr_I (_0_common.Common_I):
    _NP_RepositoryId = _0_trafficConditioningProfile._d_TCProfileMgr_I[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_trafficConditioningProfile.TCProfileMgr_I = TCProfileMgr_I
_0_trafficConditioningProfile._tc_TCProfileMgr_I = omniORB.tcInternal.createTypeCode(_0_trafficConditioningProfile._d_TCProfileMgr_I)
omniORB.registerType(TCProfileMgr_I._NP_RepositoryId, _0_trafficConditioningProfile._d_TCProfileMgr_I, _0_trafficConditioningProfile._tc_TCProfileMgr_I)

# TCProfileMgr_I operations and attributes
TCProfileMgr_I._d_getAllTCProfiles = ((omniORB.tcInternal.tv_ulong, ), (omniORB.typeMapping["IDL:mtnm.tmforum.org/trafficConditioningProfile/TCProfileList_T:1.0"], omniORB.typeMapping["IDL:mtnm.tmforum.org/trafficConditioningProfile/TCProfileIterator_I:1.0"]), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
TCProfileMgr_I._d_getTCProfile = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], ), (omniORB.typeMapping["IDL:mtnm.tmforum.org/trafficConditioningProfile/TCProfile_T:1.0"], ), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
TCProfileMgr_I._d_getTCProfileAssociatedTPs = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], omniORB.tcInternal.tv_ulong), (omniORB.typeMapping["IDL:mtnm.tmforum.org/terminationPoint/TerminationPointList_T:1.0"], omniORB.typeMapping["IDL:mtnm.tmforum.org/terminationPoint/TerminationPointIterator_I:1.0"]), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
TCProfileMgr_I._d_createTCProfile = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/trafficConditioningProfile/TCProfileCreateData_T:1.0"], ), (omniORB.typeMapping["IDL:mtnm.tmforum.org/trafficConditioningProfile/TCProfile_T:1.0"], ), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
TCProfileMgr_I._d_deleteTCProfile = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], ), (), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
TCProfileMgr_I._d_modifyTCProfile = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], omniORB.typeMapping["IDL:mtnm.tmforum.org/trafficConditioningProfile/TCProfileCreateData_T:1.0"], omniORB.typeMapping["IDL:mtnm.tmforum.org/subnetworkConnection/TPDataList_T:1.0"]), (omniORB.typeMapping["IDL:mtnm.tmforum.org/subnetworkConnection/TPDataList_T:1.0"], omniORB.typeMapping["IDL:mtnm.tmforum.org/trafficConditioningProfile/TCProfile_T:1.0"], (omniORB.tcInternal.tv_string,0)), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})

# TCProfileMgr_I object reference
class _objref_TCProfileMgr_I (_0_common._objref_Common_I):
    _NP_RepositoryId = TCProfileMgr_I._NP_RepositoryId

    def __init__(self, obj):
        _0_common._objref_Common_I.__init__(self, obj)

    def getAllTCProfiles(self, *args):
        return self._obj.invoke("getAllTCProfiles", _0_trafficConditioningProfile.TCProfileMgr_I._d_getAllTCProfiles, args)

    def getTCProfile(self, *args):
        return self._obj.invoke("getTCProfile", _0_trafficConditioningProfile.TCProfileMgr_I._d_getTCProfile, args)

    def getTCProfileAssociatedTPs(self, *args):
        return self._obj.invoke("getTCProfileAssociatedTPs", _0_trafficConditioningProfile.TCProfileMgr_I._d_getTCProfileAssociatedTPs, args)

    def createTCProfile(self, *args):
        return self._obj.invoke("createTCProfile", _0_trafficConditioningProfile.TCProfileMgr_I._d_createTCProfile, args)

    def deleteTCProfile(self, *args):
        return self._obj.invoke("deleteTCProfile", _0_trafficConditioningProfile.TCProfileMgr_I._d_deleteTCProfile, args)

    def modifyTCProfile(self, *args):
        return self._obj.invoke("modifyTCProfile", _0_trafficConditioningProfile.TCProfileMgr_I._d_modifyTCProfile, args)

omniORB.registerObjref(TCProfileMgr_I._NP_RepositoryId, _objref_TCProfileMgr_I)
_0_trafficConditioningProfile._objref_TCProfileMgr_I = _objref_TCProfileMgr_I
del TCProfileMgr_I, _objref_TCProfileMgr_I

# TCProfileMgr_I skeleton
__name__ = "trafficConditioningProfile__POA"
class TCProfileMgr_I (_0_common__POA.Common_I):
    _NP_RepositoryId = _0_trafficConditioningProfile.TCProfileMgr_I._NP_RepositoryId


    _omni_op_d = {"getAllTCProfiles": _0_trafficConditioningProfile.TCProfileMgr_I._d_getAllTCProfiles, "getTCProfile": _0_trafficConditioningProfile.TCProfileMgr_I._d_getTCProfile, "getTCProfileAssociatedTPs": _0_trafficConditioningProfile.TCProfileMgr_I._d_getTCProfileAssociatedTPs, "createTCProfile": _0_trafficConditioningProfile.TCProfileMgr_I._d_createTCProfile, "deleteTCProfile": _0_trafficConditioningProfile.TCProfileMgr_I._d_deleteTCProfile, "modifyTCProfile": _0_trafficConditioningProfile.TCProfileMgr_I._d_modifyTCProfile}
    _omni_op_d.update(_0_common__POA.Common_I._omni_op_d)

TCProfileMgr_I._omni_skeleton = TCProfileMgr_I
_0_trafficConditioningProfile__POA.TCProfileMgr_I = TCProfileMgr_I
omniORB.registerSkeleton(TCProfileMgr_I._NP_RepositoryId, TCProfileMgr_I)
del TCProfileMgr_I
__name__ = "trafficConditioningProfile"

#
# End of module "trafficConditioningProfile"
#
__name__ = "trafficConditioningProfile_idl"

_exported_modules = ( "trafficConditioningProfile", )

# The end.
