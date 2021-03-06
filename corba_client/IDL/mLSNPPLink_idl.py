# Python stubs generated by omniidl from mLSNPPLink.idl
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

# #include "common.idl"
import common_idl
_0_common = omniORB.openModule("common")
_0_common__POA = omniORB.openModule("common__POA")

# #include "terminationPoint.idl"
import terminationPoint_idl
_0_terminationPoint = omniORB.openModule("terminationPoint")
_0_terminationPoint__POA = omniORB.openModule("terminationPoint__POA")

# #include "mLSNPP.idl"
import mLSNPP_idl
_0_mLSNPP = omniORB.openModule("mLSNPP")
_0_mLSNPP__POA = omniORB.openModule("mLSNPP__POA")

#
# Start of module "mLSNPPLink"
#
__name__ = "mLSNPPLink"
_0_mLSNPPLink = omniORB.openModule("mLSNPPLink", r"mLSNPPLink.idl")
_0_mLSNPPLink__POA = omniORB.openModule("mLSNPPLink__POA", r"mLSNPPLink.idl")


# typedef ... SignallingProtocol_T
class SignallingProtocol_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/mLSNPPLink/SignallingProtocol_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_mLSNPPLink.SignallingProtocol_T = SignallingProtocol_T
_0_mLSNPPLink._d_SignallingProtocol_T  = (omniORB.tcInternal.tv_string,0)
_0_mLSNPPLink._ad_SignallingProtocol_T = (omniORB.tcInternal.tv_alias, SignallingProtocol_T._NP_RepositoryId, "SignallingProtocol_T", (omniORB.tcInternal.tv_string,0))
_0_mLSNPPLink._tc_SignallingProtocol_T = omniORB.tcInternal.createTypeCode(_0_mLSNPPLink._ad_SignallingProtocol_T)
omniORB.registerType(SignallingProtocol_T._NP_RepositoryId, _0_mLSNPPLink._ad_SignallingProtocol_T, _0_mLSNPPLink._tc_SignallingProtocol_T)
del SignallingProtocol_T

# struct SNPPLink_T
_0_mLSNPPLink.SNPPLink_T = omniORB.newEmptyClass()
class SNPPLink_T (omniORB.StructBase):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/mLSNPPLink/SNPPLink_T:1.0"

    def __init__(self, SNPPLinkId, aEnd, zEnd):
        self.SNPPLinkId = SNPPLinkId
        self.aEnd = aEnd
        self.zEnd = zEnd

_0_mLSNPPLink.SNPPLink_T = SNPPLink_T
_0_mLSNPPLink._d_SNPPLink_T  = (omniORB.tcInternal.tv_struct, SNPPLink_T, SNPPLink_T._NP_RepositoryId, "SNPPLink_T", "SNPPLinkId", (omniORB.tcInternal.tv_string,0), "aEnd", omniORB.typeMapping["IDL:mtnm.tmforum.org/mLSNPP/SNPP_T:1.0"], "zEnd", omniORB.typeMapping["IDL:mtnm.tmforum.org/mLSNPP/SNPP_T:1.0"])
_0_mLSNPPLink._tc_SNPPLink_T = omniORB.tcInternal.createTypeCode(_0_mLSNPPLink._d_SNPPLink_T)
omniORB.registerType(SNPPLink_T._NP_RepositoryId, _0_mLSNPPLink._d_SNPPLink_T, _0_mLSNPPLink._tc_SNPPLink_T)
del SNPPLink_T

# typedef ... SNPPLinkList_T
class SNPPLinkList_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/mLSNPPLink/SNPPLinkList_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_mLSNPPLink.SNPPLinkList_T = SNPPLinkList_T
_0_mLSNPPLink._d_SNPPLinkList_T  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/mLSNPPLink/SNPPLink_T:1.0"], 0)
_0_mLSNPPLink._ad_SNPPLinkList_T = (omniORB.tcInternal.tv_alias, SNPPLinkList_T._NP_RepositoryId, "SNPPLinkList_T", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/mLSNPPLink/SNPPLink_T:1.0"], 0))
_0_mLSNPPLink._tc_SNPPLinkList_T = omniORB.tcInternal.createTypeCode(_0_mLSNPPLink._ad_SNPPLinkList_T)
omniORB.registerType(SNPPLinkList_T._NP_RepositoryId, _0_mLSNPPLink._ad_SNPPLinkList_T, _0_mLSNPPLink._tc_SNPPLinkList_T)
del SNPPLinkList_T

# struct LayeredSNPPLink_T
_0_mLSNPPLink.LayeredSNPPLink_T = omniORB.newEmptyClass()
class LayeredSNPPLink_T (omniORB.StructBase):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/mLSNPPLink/LayeredSNPPLink_T:1.0"

    def __init__(self, layerRate, sNPPLinkList):
        self.layerRate = layerRate
        self.sNPPLinkList = sNPPLinkList

_0_mLSNPPLink.LayeredSNPPLink_T = LayeredSNPPLink_T
_0_mLSNPPLink._d_LayeredSNPPLink_T  = (omniORB.tcInternal.tv_struct, LayeredSNPPLink_T, LayeredSNPPLink_T._NP_RepositoryId, "LayeredSNPPLink_T", "layerRate", omniORB.typeMapping["IDL:mtnm.tmforum.org/transmissionParameters/LayerRate_T:1.0"], "sNPPLinkList", omniORB.typeMapping["IDL:mtnm.tmforum.org/mLSNPPLink/SNPPLinkList_T:1.0"])
_0_mLSNPPLink._tc_LayeredSNPPLink_T = omniORB.tcInternal.createTypeCode(_0_mLSNPPLink._d_LayeredSNPPLink_T)
omniORB.registerType(LayeredSNPPLink_T._NP_RepositoryId, _0_mLSNPPLink._d_LayeredSNPPLink_T, _0_mLSNPPLink._tc_LayeredSNPPLink_T)
del LayeredSNPPLink_T

# typedef ... LayeredSNPPLinkList_T
class LayeredSNPPLinkList_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/mLSNPPLink/LayeredSNPPLinkList_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_mLSNPPLink.LayeredSNPPLinkList_T = LayeredSNPPLinkList_T
_0_mLSNPPLink._d_LayeredSNPPLinkList_T  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/mLSNPPLink/LayeredSNPPLink_T:1.0"], 0)
_0_mLSNPPLink._ad_LayeredSNPPLinkList_T = (omniORB.tcInternal.tv_alias, LayeredSNPPLinkList_T._NP_RepositoryId, "LayeredSNPPLinkList_T", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/mLSNPPLink/LayeredSNPPLink_T:1.0"], 0))
_0_mLSNPPLink._tc_LayeredSNPPLinkList_T = omniORB.tcInternal.createTypeCode(_0_mLSNPPLink._ad_LayeredSNPPLinkList_T)
omniORB.registerType(LayeredSNPPLinkList_T._NP_RepositoryId, _0_mLSNPPLink._ad_LayeredSNPPLinkList_T, _0_mLSNPPLink._tc_LayeredSNPPLinkList_T)
del LayeredSNPPLinkList_T

# typedef ... InterfaceType_T
class InterfaceType_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/mLSNPPLink/InterfaceType_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_mLSNPPLink.InterfaceType_T = InterfaceType_T
_0_mLSNPPLink._d_InterfaceType_T  = (omniORB.tcInternal.tv_string,0)
_0_mLSNPPLink._ad_InterfaceType_T = (omniORB.tcInternal.tv_alias, InterfaceType_T._NP_RepositoryId, "InterfaceType_T", (omniORB.tcInternal.tv_string,0))
_0_mLSNPPLink._tc_InterfaceType_T = omniORB.tcInternal.createTypeCode(_0_mLSNPPLink._ad_InterfaceType_T)
omniORB.registerType(InterfaceType_T._NP_RepositoryId, _0_mLSNPPLink._ad_InterfaceType_T, _0_mLSNPPLink._tc_InterfaceType_T)
del InterfaceType_T

# typedef ... Capacity_T
class Capacity_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/mLSNPPLink/Capacity_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_mLSNPPLink.Capacity_T = Capacity_T
_0_mLSNPPLink._d_Capacity_T  = (omniORB.tcInternal.tv_string,0)
_0_mLSNPPLink._ad_Capacity_T = (omniORB.tcInternal.tv_alias, Capacity_T._NP_RepositoryId, "Capacity_T", (omniORB.tcInternal.tv_string,0))
_0_mLSNPPLink._tc_Capacity_T = omniORB.tcInternal.createTypeCode(_0_mLSNPPLink._ad_Capacity_T)
omniORB.registerType(Capacity_T._NP_RepositoryId, _0_mLSNPPLink._ad_Capacity_T, _0_mLSNPPLink._tc_Capacity_T)
del Capacity_T

# struct LayeredCapacity_T
_0_mLSNPPLink.LayeredCapacity_T = omniORB.newEmptyClass()
class LayeredCapacity_T (omniORB.StructBase):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/mLSNPPLink/LayeredCapacity_T:1.0"

    def __init__(self, layerRate, capacity):
        self.layerRate = layerRate
        self.capacity = capacity

_0_mLSNPPLink.LayeredCapacity_T = LayeredCapacity_T
_0_mLSNPPLink._d_LayeredCapacity_T  = (omniORB.tcInternal.tv_struct, LayeredCapacity_T, LayeredCapacity_T._NP_RepositoryId, "LayeredCapacity_T", "layerRate", omniORB.typeMapping["IDL:mtnm.tmforum.org/transmissionParameters/LayerRate_T:1.0"], "capacity", omniORB.typeMapping["IDL:mtnm.tmforum.org/mLSNPPLink/Capacity_T:1.0"])
_0_mLSNPPLink._tc_LayeredCapacity_T = omniORB.tcInternal.createTypeCode(_0_mLSNPPLink._d_LayeredCapacity_T)
omniORB.registerType(LayeredCapacity_T._NP_RepositoryId, _0_mLSNPPLink._d_LayeredCapacity_T, _0_mLSNPPLink._tc_LayeredCapacity_T)
del LayeredCapacity_T

# typedef ... AvailableCapacity_T
class AvailableCapacity_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/mLSNPPLink/AvailableCapacity_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_mLSNPPLink.AvailableCapacity_T = AvailableCapacity_T
_0_mLSNPPLink._d_AvailableCapacity_T  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/mLSNPPLink/LayeredCapacity_T:1.0"], 0)
_0_mLSNPPLink._ad_AvailableCapacity_T = (omniORB.tcInternal.tv_alias, AvailableCapacity_T._NP_RepositoryId, "AvailableCapacity_T", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/mLSNPPLink/LayeredCapacity_T:1.0"], 0))
_0_mLSNPPLink._tc_AvailableCapacity_T = omniORB.tcInternal.createTypeCode(_0_mLSNPPLink._ad_AvailableCapacity_T)
omniORB.registerType(AvailableCapacity_T._NP_RepositoryId, _0_mLSNPPLink._ad_AvailableCapacity_T, _0_mLSNPPLink._tc_AvailableCapacity_T)
del AvailableCapacity_T

# struct MultiLayerSNPPLink_T
_0_mLSNPPLink.MultiLayerSNPPLink_T = omniORB.newEmptyClass()
class MultiLayerSNPPLink_T (omniORB.StructBase):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/mLSNPPLink/MultiLayerSNPPLink_T:1.0"

    def __init__(self, name, userLabel, nativeEMSName, owner, direction, aMLRAName, zMLRAName, aTNAName, zTNAName, aTNAGroupName, zTNAGroupName, sNPPLinkList, interfaceType, signallingParameters, signallingControllerIdentifier, signallingProtocol, signallingEnabled, cost, discovered, availability, linkSRG, additionalInfo):
        self.name = name
        self.userLabel = userLabel
        self.nativeEMSName = nativeEMSName
        self.owner = owner
        self.direction = direction
        self.aMLRAName = aMLRAName
        self.zMLRAName = zMLRAName
        self.aTNAName = aTNAName
        self.zTNAName = zTNAName
        self.aTNAGroupName = aTNAGroupName
        self.zTNAGroupName = zTNAGroupName
        self.sNPPLinkList = sNPPLinkList
        self.interfaceType = interfaceType
        self.signallingParameters = signallingParameters
        self.signallingControllerIdentifier = signallingControllerIdentifier
        self.signallingProtocol = signallingProtocol
        self.signallingEnabled = signallingEnabled
        self.cost = cost
        self.discovered = discovered
        self.availability = availability
        self.linkSRG = linkSRG
        self.additionalInfo = additionalInfo

_0_mLSNPPLink.MultiLayerSNPPLink_T = MultiLayerSNPPLink_T
_0_mLSNPPLink._d_MultiLayerSNPPLink_T  = (omniORB.tcInternal.tv_struct, MultiLayerSNPPLink_T, MultiLayerSNPPLink_T._NP_RepositoryId, "MultiLayerSNPPLink_T", "name", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], "userLabel", (omniORB.tcInternal.tv_string,0), "nativeEMSName", (omniORB.tcInternal.tv_string,0), "owner", (omniORB.tcInternal.tv_string,0), "direction", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/ConnectionDirection_T:1.0"], "aMLRAName", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], "zMLRAName", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], "aTNAName", (omniORB.tcInternal.tv_string,0), "zTNAName", (omniORB.tcInternal.tv_string,0), "aTNAGroupName", (omniORB.tcInternal.tv_string,0), "zTNAGroupName", (omniORB.tcInternal.tv_string,0), "sNPPLinkList", omniORB.typeMapping["IDL:mtnm.tmforum.org/mLSNPPLink/LayeredSNPPLinkList_T:1.0"], "interfaceType", omniORB.typeMapping["IDL:mtnm.tmforum.org/mLSNPPLink/InterfaceType_T:1.0"], "signallingParameters", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"], "signallingControllerIdentifier", (omniORB.tcInternal.tv_string,0), "signallingProtocol", omniORB.typeMapping["IDL:mtnm.tmforum.org/mLSNPPLink/SignallingProtocol_T:1.0"], "signallingEnabled", omniORB.tcInternal.tv_boolean, "cost", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"], "discovered", omniORB.tcInternal.tv_boolean, "availability", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"], "linkSRG", (omniORB.tcInternal.tv_string,0), "additionalInfo", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"])
_0_mLSNPPLink._tc_MultiLayerSNPPLink_T = omniORB.tcInternal.createTypeCode(_0_mLSNPPLink._d_MultiLayerSNPPLink_T)
omniORB.registerType(MultiLayerSNPPLink_T._NP_RepositoryId, _0_mLSNPPLink._d_MultiLayerSNPPLink_T, _0_mLSNPPLink._tc_MultiLayerSNPPLink_T)
del MultiLayerSNPPLink_T

# typedef ... MLSNPPLinkList_T
class MLSNPPLinkList_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/mLSNPPLink/MLSNPPLinkList_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_mLSNPPLink.MLSNPPLinkList_T = MLSNPPLinkList_T
_0_mLSNPPLink._d_MLSNPPLinkList_T  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/mLSNPPLink/MultiLayerSNPPLink_T:1.0"], 0)
_0_mLSNPPLink._ad_MLSNPPLinkList_T = (omniORB.tcInternal.tv_alias, MLSNPPLinkList_T._NP_RepositoryId, "MLSNPPLinkList_T", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/mLSNPPLink/MultiLayerSNPPLink_T:1.0"], 0))
_0_mLSNPPLink._tc_MLSNPPLinkList_T = omniORB.tcInternal.createTypeCode(_0_mLSNPPLink._ad_MLSNPPLinkList_T)
omniORB.registerType(MLSNPPLinkList_T._NP_RepositoryId, _0_mLSNPPLink._ad_MLSNPPLinkList_T, _0_mLSNPPLink._tc_MLSNPPLinkList_T)
del MLSNPPLinkList_T

# interface MLSNPPLinkIterator_I
_0_mLSNPPLink._d_MLSNPPLinkIterator_I = (omniORB.tcInternal.tv_objref, "IDL:mtnm.tmforum.org/mLSNPPLink/MLSNPPLinkIterator_I:1.0", "MLSNPPLinkIterator_I")
omniORB.typeMapping["IDL:mtnm.tmforum.org/mLSNPPLink/MLSNPPLinkIterator_I:1.0"] = _0_mLSNPPLink._d_MLSNPPLinkIterator_I
_0_mLSNPPLink.MLSNPPLinkIterator_I = omniORB.newEmptyClass()
class MLSNPPLinkIterator_I :
    _NP_RepositoryId = _0_mLSNPPLink._d_MLSNPPLinkIterator_I[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_mLSNPPLink.MLSNPPLinkIterator_I = MLSNPPLinkIterator_I
_0_mLSNPPLink._tc_MLSNPPLinkIterator_I = omniORB.tcInternal.createTypeCode(_0_mLSNPPLink._d_MLSNPPLinkIterator_I)
omniORB.registerType(MLSNPPLinkIterator_I._NP_RepositoryId, _0_mLSNPPLink._d_MLSNPPLinkIterator_I, _0_mLSNPPLink._tc_MLSNPPLinkIterator_I)

# MLSNPPLinkIterator_I operations and attributes
MLSNPPLinkIterator_I._d_next_n = ((omniORB.tcInternal.tv_ulong, ), (omniORB.tcInternal.tv_boolean, omniORB.typeMapping["IDL:mtnm.tmforum.org/mLSNPPLink/MLSNPPLinkList_T:1.0"]), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
MLSNPPLinkIterator_I._d_getLength = ((), (omniORB.tcInternal.tv_ulong, ), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
MLSNPPLinkIterator_I._d_destroy = ((), (), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})

# MLSNPPLinkIterator_I object reference
class _objref_MLSNPPLinkIterator_I (CORBA.Object):
    _NP_RepositoryId = MLSNPPLinkIterator_I._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def next_n(self, *args):
        return self._obj.invoke("next_n", _0_mLSNPPLink.MLSNPPLinkIterator_I._d_next_n, args)

    def getLength(self, *args):
        return self._obj.invoke("getLength", _0_mLSNPPLink.MLSNPPLinkIterator_I._d_getLength, args)

    def destroy(self, *args):
        return self._obj.invoke("destroy", _0_mLSNPPLink.MLSNPPLinkIterator_I._d_destroy, args)

omniORB.registerObjref(MLSNPPLinkIterator_I._NP_RepositoryId, _objref_MLSNPPLinkIterator_I)
_0_mLSNPPLink._objref_MLSNPPLinkIterator_I = _objref_MLSNPPLinkIterator_I
del MLSNPPLinkIterator_I, _objref_MLSNPPLinkIterator_I

# MLSNPPLinkIterator_I skeleton
__name__ = "mLSNPPLink__POA"
class MLSNPPLinkIterator_I (PortableServer.Servant):
    _NP_RepositoryId = _0_mLSNPPLink.MLSNPPLinkIterator_I._NP_RepositoryId


    _omni_op_d = {"next_n": _0_mLSNPPLink.MLSNPPLinkIterator_I._d_next_n, "getLength": _0_mLSNPPLink.MLSNPPLinkIterator_I._d_getLength, "destroy": _0_mLSNPPLink.MLSNPPLinkIterator_I._d_destroy}

MLSNPPLinkIterator_I._omni_skeleton = MLSNPPLinkIterator_I
_0_mLSNPPLink__POA.MLSNPPLinkIterator_I = MLSNPPLinkIterator_I
omniORB.registerSkeleton(MLSNPPLinkIterator_I._NP_RepositoryId, MLSNPPLinkIterator_I)
del MLSNPPLinkIterator_I
__name__ = "mLSNPPLink"

# interface MLSNPPLinkMgr_I
_0_mLSNPPLink._d_MLSNPPLinkMgr_I = (omniORB.tcInternal.tv_objref, "IDL:mtnm.tmforum.org/mLSNPPLink/MLSNPPLinkMgr_I:1.0", "MLSNPPLinkMgr_I")
omniORB.typeMapping["IDL:mtnm.tmforum.org/mLSNPPLink/MLSNPPLinkMgr_I:1.0"] = _0_mLSNPPLink._d_MLSNPPLinkMgr_I
_0_mLSNPPLink.MLSNPPLinkMgr_I = omniORB.newEmptyClass()
class MLSNPPLinkMgr_I (_0_common.Common_I):
    _NP_RepositoryId = _0_mLSNPPLink._d_MLSNPPLinkMgr_I[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_mLSNPPLink.MLSNPPLinkMgr_I = MLSNPPLinkMgr_I
_0_mLSNPPLink._tc_MLSNPPLinkMgr_I = omniORB.tcInternal.createTypeCode(_0_mLSNPPLink._d_MLSNPPLinkMgr_I)
omniORB.registerType(MLSNPPLinkMgr_I._NP_RepositoryId, _0_mLSNPPLink._d_MLSNPPLinkMgr_I, _0_mLSNPPLink._tc_MLSNPPLinkMgr_I)

# MLSNPPLinkMgr_I operations and attributes
MLSNPPLinkMgr_I._d_getAvailableCapacity = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], omniORB.typeMapping["IDL:mtnm.tmforum.org/transmissionParameters/LayerRate_T:1.0"]), (omniORB.typeMapping["IDL:mtnm.tmforum.org/mLSNPPLink/AvailableCapacity_T:1.0"], ), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
MLSNPPLinkMgr_I._d_assignSignallingController = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], (omniORB.tcInternal.tv_string,0)), (), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
MLSNPPLinkMgr_I._d_deassignSignallingController = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], ), (), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
MLSNPPLinkMgr_I._d_setSignallingProtocolAndParameters = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], omniORB.typeMapping["IDL:mtnm.tmforum.org/mLSNPPLink/SignallingProtocol_T:1.0"], omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"]), (), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
MLSNPPLinkMgr_I._d_setTNANameForMLSNPPLinkEnd = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], omniORB.typeMapping["IDL:mtnm.tmforum.org/mLSNPP/SNPTNADataList_T:1.0"], omniORB.typeMapping["IDL:mtnm.tmforum.org/mLSNPP/SNPPTNAPairList_T:1.0"], (omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0)), (omniORB.typeMapping["IDL:mtnm.tmforum.org/mLSNPPLink/MultiLayerSNPPLink_T:1.0"], ), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
MLSNPPLinkMgr_I._d_modifySignallingProtocolParameters = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"]), (omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"], ), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
MLSNPPLinkMgr_I._d_enableSignalling = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], ), (), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
MLSNPPLinkMgr_I._d_disableSignalling = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], ), (), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})

# MLSNPPLinkMgr_I object reference
class _objref_MLSNPPLinkMgr_I (_0_common._objref_Common_I):
    _NP_RepositoryId = MLSNPPLinkMgr_I._NP_RepositoryId

    def __init__(self, obj):
        _0_common._objref_Common_I.__init__(self, obj)

    def getAvailableCapacity(self, *args):
        return self._obj.invoke("getAvailableCapacity", _0_mLSNPPLink.MLSNPPLinkMgr_I._d_getAvailableCapacity, args)

    def assignSignallingController(self, *args):
        return self._obj.invoke("assignSignallingController", _0_mLSNPPLink.MLSNPPLinkMgr_I._d_assignSignallingController, args)

    def deassignSignallingController(self, *args):
        return self._obj.invoke("deassignSignallingController", _0_mLSNPPLink.MLSNPPLinkMgr_I._d_deassignSignallingController, args)

    def setSignallingProtocolAndParameters(self, *args):
        return self._obj.invoke("setSignallingProtocolAndParameters", _0_mLSNPPLink.MLSNPPLinkMgr_I._d_setSignallingProtocolAndParameters, args)

    def setTNANameForMLSNPPLinkEnd(self, *args):
        return self._obj.invoke("setTNANameForMLSNPPLinkEnd", _0_mLSNPPLink.MLSNPPLinkMgr_I._d_setTNANameForMLSNPPLinkEnd, args)

    def modifySignallingProtocolParameters(self, *args):
        return self._obj.invoke("modifySignallingProtocolParameters", _0_mLSNPPLink.MLSNPPLinkMgr_I._d_modifySignallingProtocolParameters, args)

    def enableSignalling(self, *args):
        return self._obj.invoke("enableSignalling", _0_mLSNPPLink.MLSNPPLinkMgr_I._d_enableSignalling, args)

    def disableSignalling(self, *args):
        return self._obj.invoke("disableSignalling", _0_mLSNPPLink.MLSNPPLinkMgr_I._d_disableSignalling, args)

omniORB.registerObjref(MLSNPPLinkMgr_I._NP_RepositoryId, _objref_MLSNPPLinkMgr_I)
_0_mLSNPPLink._objref_MLSNPPLinkMgr_I = _objref_MLSNPPLinkMgr_I
del MLSNPPLinkMgr_I, _objref_MLSNPPLinkMgr_I

# MLSNPPLinkMgr_I skeleton
__name__ = "mLSNPPLink__POA"
class MLSNPPLinkMgr_I (_0_common__POA.Common_I):
    _NP_RepositoryId = _0_mLSNPPLink.MLSNPPLinkMgr_I._NP_RepositoryId


    _omni_op_d = {"getAvailableCapacity": _0_mLSNPPLink.MLSNPPLinkMgr_I._d_getAvailableCapacity, "assignSignallingController": _0_mLSNPPLink.MLSNPPLinkMgr_I._d_assignSignallingController, "deassignSignallingController": _0_mLSNPPLink.MLSNPPLinkMgr_I._d_deassignSignallingController, "setSignallingProtocolAndParameters": _0_mLSNPPLink.MLSNPPLinkMgr_I._d_setSignallingProtocolAndParameters, "setTNANameForMLSNPPLinkEnd": _0_mLSNPPLink.MLSNPPLinkMgr_I._d_setTNANameForMLSNPPLinkEnd, "modifySignallingProtocolParameters": _0_mLSNPPLink.MLSNPPLinkMgr_I._d_modifySignallingProtocolParameters, "enableSignalling": _0_mLSNPPLink.MLSNPPLinkMgr_I._d_enableSignalling, "disableSignalling": _0_mLSNPPLink.MLSNPPLinkMgr_I._d_disableSignalling}
    _omni_op_d.update(_0_common__POA.Common_I._omni_op_d)

MLSNPPLinkMgr_I._omni_skeleton = MLSNPPLinkMgr_I
_0_mLSNPPLink__POA.MLSNPPLinkMgr_I = MLSNPPLinkMgr_I
omniORB.registerSkeleton(MLSNPPLinkMgr_I._NP_RepositoryId, MLSNPPLinkMgr_I)
del MLSNPPLinkMgr_I
__name__ = "mLSNPPLink"

#
# End of module "mLSNPPLink"
#
__name__ = "mLSNPPLink_idl"

_exported_modules = ( "mLSNPPLink", )

# The end.
