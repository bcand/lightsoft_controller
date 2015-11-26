# Python stubs generated by omniidl from protection.idl
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

#
# Start of module "protection"
#
__name__ = "protection"
_0_protection = omniORB.openModule("protection", r"protection.idl")
_0_protection__POA = omniORB.openModule("protection__POA", r"protection.idl")


# enum ProtectionSchemeState_T
_0_protection.PSS_UNKNOWN = omniORB.EnumItem("PSS_UNKNOWN", 0)
_0_protection.PSS_AUTOMATIC = omniORB.EnumItem("PSS_AUTOMATIC", 1)
_0_protection.PSS_FORCED_OR_LOCKED_OUT = omniORB.EnumItem("PSS_FORCED_OR_LOCKED_OUT", 2)
_0_protection.ProtectionSchemeState_T = omniORB.Enum("IDL:mtnm.tmforum.org/protection/ProtectionSchemeState_T:1.0", (_0_protection.PSS_UNKNOWN, _0_protection.PSS_AUTOMATIC, _0_protection.PSS_FORCED_OR_LOCKED_OUT,))

_0_protection._d_ProtectionSchemeState_T  = (omniORB.tcInternal.tv_enum, _0_protection.ProtectionSchemeState_T._NP_RepositoryId, "ProtectionSchemeState_T", _0_protection.ProtectionSchemeState_T._items)
_0_protection._tc_ProtectionSchemeState_T = omniORB.tcInternal.createTypeCode(_0_protection._d_ProtectionSchemeState_T)
omniORB.registerType(_0_protection.ProtectionSchemeState_T._NP_RepositoryId, _0_protection._d_ProtectionSchemeState_T, _0_protection._tc_ProtectionSchemeState_T)

# enum ProtectionType_T
_0_protection.PT_MSP_APS = omniORB.EnumItem("PT_MSP_APS", 0)
_0_protection.PT_SNCP = omniORB.EnumItem("PT_SNCP", 1)
_0_protection.ProtectionType_T = omniORB.Enum("IDL:mtnm.tmforum.org/protection/ProtectionType_T:1.0", (_0_protection.PT_MSP_APS, _0_protection.PT_SNCP,))

_0_protection._d_ProtectionType_T  = (omniORB.tcInternal.tv_enum, _0_protection.ProtectionType_T._NP_RepositoryId, "ProtectionType_T", _0_protection.ProtectionType_T._items)
_0_protection._tc_ProtectionType_T = omniORB.tcInternal.createTypeCode(_0_protection._d_ProtectionType_T)
omniORB.registerType(_0_protection.ProtectionType_T._NP_RepositoryId, _0_protection._d_ProtectionType_T, _0_protection._tc_ProtectionType_T)

# enum SwitchReason_T
_0_protection.SR_NA = omniORB.EnumItem("SR_NA", 0)
_0_protection.SR_RESTORED = omniORB.EnumItem("SR_RESTORED", 1)
_0_protection.SR_SIGNAL_FAIL = omniORB.EnumItem("SR_SIGNAL_FAIL", 2)
_0_protection.SR_SIGNAL_MISMATCH = omniORB.EnumItem("SR_SIGNAL_MISMATCH", 3)
_0_protection.SR_SIGNAL_DEGRADE = omniORB.EnumItem("SR_SIGNAL_DEGRADE", 4)
_0_protection.SR_AUTOMATIC_SWITCH = omniORB.EnumItem("SR_AUTOMATIC_SWITCH", 5)
_0_protection.SR_MANUAL = omniORB.EnumItem("SR_MANUAL", 6)
_0_protection.SwitchReason_T = omniORB.Enum("IDL:mtnm.tmforum.org/protection/SwitchReason_T:1.0", (_0_protection.SR_NA, _0_protection.SR_RESTORED, _0_protection.SR_SIGNAL_FAIL, _0_protection.SR_SIGNAL_MISMATCH, _0_protection.SR_SIGNAL_DEGRADE, _0_protection.SR_AUTOMATIC_SWITCH, _0_protection.SR_MANUAL,))

_0_protection._d_SwitchReason_T  = (omniORB.tcInternal.tv_enum, _0_protection.SwitchReason_T._NP_RepositoryId, "SwitchReason_T", _0_protection.SwitchReason_T._items)
_0_protection._tc_SwitchReason_T = omniORB.tcInternal.createTypeCode(_0_protection._d_SwitchReason_T)
omniORB.registerType(_0_protection.SwitchReason_T._NP_RepositoryId, _0_protection._d_SwitchReason_T, _0_protection._tc_SwitchReason_T)

# typedef ... ESwitchReason_T
class ESwitchReason_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/protection/ESwitchReason_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_protection.ESwitchReason_T = ESwitchReason_T
_0_protection._d_ESwitchReason_T  = (omniORB.tcInternal.tv_string,0)
_0_protection._ad_ESwitchReason_T = (omniORB.tcInternal.tv_alias, ESwitchReason_T._NP_RepositoryId, "ESwitchReason_T", (omniORB.tcInternal.tv_string,0))
_0_protection._tc_ESwitchReason_T = omniORB.tcInternal.createTypeCode(_0_protection._ad_ESwitchReason_T)
omniORB.registerType(ESwitchReason_T._NP_RepositoryId, _0_protection._ad_ESwitchReason_T, _0_protection._tc_ESwitchReason_T)
del ESwitchReason_T

# enum ProtectionCommand_T
_0_protection.PC_CLEAR = omniORB.EnumItem("PC_CLEAR", 0)
_0_protection.PC_LOCKOUT = omniORB.EnumItem("PC_LOCKOUT", 1)
_0_protection.PC_FORCED_SWITCH = omniORB.EnumItem("PC_FORCED_SWITCH", 2)
_0_protection.PC_MANUAL_SWITCH = omniORB.EnumItem("PC_MANUAL_SWITCH", 3)
_0_protection.PC_EXERCISER = omniORB.EnumItem("PC_EXERCISER", 4)
_0_protection.ProtectionCommand_T = omniORB.Enum("IDL:mtnm.tmforum.org/protection/ProtectionCommand_T:1.0", (_0_protection.PC_CLEAR, _0_protection.PC_LOCKOUT, _0_protection.PC_FORCED_SWITCH, _0_protection.PC_MANUAL_SWITCH, _0_protection.PC_EXERCISER,))

_0_protection._d_ProtectionCommand_T  = (omniORB.tcInternal.tv_enum, _0_protection.ProtectionCommand_T._NP_RepositoryId, "ProtectionCommand_T", _0_protection.ProtectionCommand_T._items)
_0_protection._tc_ProtectionCommand_T = omniORB.tcInternal.createTypeCode(_0_protection._d_ProtectionCommand_T)
omniORB.registerType(_0_protection.ProtectionCommand_T._NP_RepositoryId, _0_protection._d_ProtectionCommand_T, _0_protection._tc_ProtectionCommand_T)

# enum ProtectionGroupType_T
_0_protection.PGT_MSP_1_PLUS_1 = omniORB.EnumItem("PGT_MSP_1_PLUS_1", 0)
_0_protection.PGT_MSP_1_FOR_N = omniORB.EnumItem("PGT_MSP_1_FOR_N", 1)
_0_protection.PGT_2_FIBER_BLSR = omniORB.EnumItem("PGT_2_FIBER_BLSR", 2)
_0_protection.PGT_4_FIBER_BLSR = omniORB.EnumItem("PGT_4_FIBER_BLSR", 3)
_0_protection.ProtectionGroupType_T = omniORB.Enum("IDL:mtnm.tmforum.org/protection/ProtectionGroupType_T:1.0", (_0_protection.PGT_MSP_1_PLUS_1, _0_protection.PGT_MSP_1_FOR_N, _0_protection.PGT_2_FIBER_BLSR, _0_protection.PGT_4_FIBER_BLSR,))

_0_protection._d_ProtectionGroupType_T  = (omniORB.tcInternal.tv_enum, _0_protection.ProtectionGroupType_T._NP_RepositoryId, "ProtectionGroupType_T", _0_protection.ProtectionGroupType_T._items)
_0_protection._tc_ProtectionGroupType_T = omniORB.tcInternal.createTypeCode(_0_protection._d_ProtectionGroupType_T)
omniORB.registerType(_0_protection.ProtectionGroupType_T._NP_RepositoryId, _0_protection._d_ProtectionGroupType_T, _0_protection._tc_ProtectionGroupType_T)

# typedef ... EProtectionGroupType_T
class EProtectionGroupType_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/protection/EProtectionGroupType_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_protection.EProtectionGroupType_T = EProtectionGroupType_T
_0_protection._d_EProtectionGroupType_T  = (omniORB.tcInternal.tv_string,0)
_0_protection._ad_EProtectionGroupType_T = (omniORB.tcInternal.tv_alias, EProtectionGroupType_T._NP_RepositoryId, "EProtectionGroupType_T", (omniORB.tcInternal.tv_string,0))
_0_protection._tc_EProtectionGroupType_T = omniORB.tcInternal.createTypeCode(_0_protection._ad_EProtectionGroupType_T)
omniORB.registerType(EProtectionGroupType_T._NP_RepositoryId, _0_protection._ad_EProtectionGroupType_T, _0_protection._tc_EProtectionGroupType_T)
del EProtectionGroupType_T

# enum ReversionMode_T
_0_protection.RM_UNKNOWN = omniORB.EnumItem("RM_UNKNOWN", 0)
_0_protection.RM_NON_REVERTIVE = omniORB.EnumItem("RM_NON_REVERTIVE", 1)
_0_protection.RM_REVERTIVE = omniORB.EnumItem("RM_REVERTIVE", 2)
_0_protection.ReversionMode_T = omniORB.Enum("IDL:mtnm.tmforum.org/protection/ReversionMode_T:1.0", (_0_protection.RM_UNKNOWN, _0_protection.RM_NON_REVERTIVE, _0_protection.RM_REVERTIVE,))

_0_protection._d_ReversionMode_T  = (omniORB.tcInternal.tv_enum, _0_protection.ReversionMode_T._NP_RepositoryId, "ReversionMode_T", _0_protection.ReversionMode_T._items)
_0_protection._tc_ReversionMode_T = omniORB.tcInternal.createTypeCode(_0_protection._d_ReversionMode_T)
omniORB.registerType(_0_protection.ReversionMode_T._NP_RepositoryId, _0_protection._d_ReversionMode_T, _0_protection._tc_ReversionMode_T)

# struct ProtectionGroup_T
_0_protection.ProtectionGroup_T = omniORB.newEmptyClass()
class ProtectionGroup_T (omniORB.StructBase):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/protection/ProtectionGroup_T:1.0"

    def __init__(self, name, userLabel, nativeEMSName, owner, protectionGroupType, protectionSchemeState, reversionMode, rate, pgpTPList, pgpParameters, additionalInfo):
        self.name = name
        self.userLabel = userLabel
        self.nativeEMSName = nativeEMSName
        self.owner = owner
        self.protectionGroupType = protectionGroupType
        self.protectionSchemeState = protectionSchemeState
        self.reversionMode = reversionMode
        self.rate = rate
        self.pgpTPList = pgpTPList
        self.pgpParameters = pgpParameters
        self.additionalInfo = additionalInfo

_0_protection.ProtectionGroup_T = ProtectionGroup_T
_0_protection._d_ProtectionGroup_T  = (omniORB.tcInternal.tv_struct, ProtectionGroup_T, ProtectionGroup_T._NP_RepositoryId, "ProtectionGroup_T", "name", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], "userLabel", (omniORB.tcInternal.tv_string,0), "nativeEMSName", (omniORB.tcInternal.tv_string,0), "owner", (omniORB.tcInternal.tv_string,0), "protectionGroupType", omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/ProtectionGroupType_T:1.0"], "protectionSchemeState", omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/ProtectionSchemeState_T:1.0"], "reversionMode", omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/ReversionMode_T:1.0"], "rate", omniORB.typeMapping["IDL:mtnm.tmforum.org/transmissionParameters/LayerRate_T:1.0"], "pgpTPList", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributesList_T:1.0"], "pgpParameters", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"], "additionalInfo", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"])
_0_protection._tc_ProtectionGroup_T = omniORB.tcInternal.createTypeCode(_0_protection._d_ProtectionGroup_T)
omniORB.registerType(ProtectionGroup_T._NP_RepositoryId, _0_protection._d_ProtectionGroup_T, _0_protection._tc_ProtectionGroup_T)
del ProtectionGroup_T

# typedef ... ProtectionGroupList_T
class ProtectionGroupList_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/protection/ProtectionGroupList_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_protection.ProtectionGroupList_T = ProtectionGroupList_T
_0_protection._d_ProtectionGroupList_T  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/ProtectionGroup_T:1.0"], 0)
_0_protection._ad_ProtectionGroupList_T = (omniORB.tcInternal.tv_alias, ProtectionGroupList_T._NP_RepositoryId, "ProtectionGroupList_T", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/ProtectionGroup_T:1.0"], 0))
_0_protection._tc_ProtectionGroupList_T = omniORB.tcInternal.createTypeCode(_0_protection._ad_ProtectionGroupList_T)
omniORB.registerType(ProtectionGroupList_T._NP_RepositoryId, _0_protection._ad_ProtectionGroupList_T, _0_protection._tc_ProtectionGroupList_T)
del ProtectionGroupList_T

# struct EProtectionGroup_T
_0_protection.EProtectionGroup_T = omniORB.newEmptyClass()
class EProtectionGroup_T (omniORB.StructBase):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/protection/EProtectionGroup_T:1.0"

    def __init__(self, name, userLabel, nativeEMSName, owner, eProtectionGroupType, protectionSchemeState, reversionMode, protectedList, protectingList, ePgpParameters, additionalInfo):
        self.name = name
        self.userLabel = userLabel
        self.nativeEMSName = nativeEMSName
        self.owner = owner
        self.eProtectionGroupType = eProtectionGroupType
        self.protectionSchemeState = protectionSchemeState
        self.reversionMode = reversionMode
        self.protectedList = protectedList
        self.protectingList = protectingList
        self.ePgpParameters = ePgpParameters
        self.additionalInfo = additionalInfo

_0_protection.EProtectionGroup_T = EProtectionGroup_T
_0_protection._d_EProtectionGroup_T  = (omniORB.tcInternal.tv_struct, EProtectionGroup_T, EProtectionGroup_T._NP_RepositoryId, "EProtectionGroup_T", "name", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], "userLabel", (omniORB.tcInternal.tv_string,0), "nativeEMSName", (omniORB.tcInternal.tv_string,0), "owner", (omniORB.tcInternal.tv_string,0), "eProtectionGroupType", omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/EProtectionGroupType_T:1.0"], "protectionSchemeState", omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/ProtectionSchemeState_T:1.0"], "reversionMode", omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/ReversionMode_T:1.0"], "protectedList", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributesList_T:1.0"], "protectingList", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributesList_T:1.0"], "ePgpParameters", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"], "additionalInfo", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"])
_0_protection._tc_EProtectionGroup_T = omniORB.tcInternal.createTypeCode(_0_protection._d_EProtectionGroup_T)
omniORB.registerType(EProtectionGroup_T._NP_RepositoryId, _0_protection._d_EProtectionGroup_T, _0_protection._tc_EProtectionGroup_T)
del EProtectionGroup_T

# typedef ... EProtectionGroupList_T
class EProtectionGroupList_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/protection/EProtectionGroupList_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_protection.EProtectionGroupList_T = EProtectionGroupList_T
_0_protection._d_EProtectionGroupList_T  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/EProtectionGroup_T:1.0"], 0)
_0_protection._ad_EProtectionGroupList_T = (omniORB.tcInternal.tv_alias, EProtectionGroupList_T._NP_RepositoryId, "EProtectionGroupList_T", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/EProtectionGroup_T:1.0"], 0))
_0_protection._tc_EProtectionGroupList_T = omniORB.tcInternal.createTypeCode(_0_protection._ad_EProtectionGroupList_T)
omniORB.registerType(EProtectionGroupList_T._NP_RepositoryId, _0_protection._ad_EProtectionGroupList_T, _0_protection._tc_EProtectionGroupList_T)
del EProtectionGroupList_T

# struct SwitchData_T
_0_protection.SwitchData_T = omniORB.newEmptyClass()
class SwitchData_T (omniORB.StructBase):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/protection/SwitchData_T:1.0"

    def __init__(self, protectionType, switchReason, layerRate, groupName, protectedTP, switchToTP, additionalInfo):
        self.protectionType = protectionType
        self.switchReason = switchReason
        self.layerRate = layerRate
        self.groupName = groupName
        self.protectedTP = protectedTP
        self.switchToTP = switchToTP
        self.additionalInfo = additionalInfo

_0_protection.SwitchData_T = SwitchData_T
_0_protection._d_SwitchData_T  = (omniORB.tcInternal.tv_struct, SwitchData_T, SwitchData_T._NP_RepositoryId, "SwitchData_T", "protectionType", omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/ProtectionType_T:1.0"], "switchReason", omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/SwitchReason_T:1.0"], "layerRate", omniORB.typeMapping["IDL:mtnm.tmforum.org/transmissionParameters/LayerRate_T:1.0"], "groupName", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], "protectedTP", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], "switchToTP", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], "additionalInfo", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"])
_0_protection._tc_SwitchData_T = omniORB.tcInternal.createTypeCode(_0_protection._d_SwitchData_T)
omniORB.registerType(SwitchData_T._NP_RepositoryId, _0_protection._d_SwitchData_T, _0_protection._tc_SwitchData_T)
del SwitchData_T

# typedef ... SwitchDataList_T
class SwitchDataList_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/protection/SwitchDataList_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_protection.SwitchDataList_T = SwitchDataList_T
_0_protection._d_SwitchDataList_T  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/SwitchData_T:1.0"], 0)
_0_protection._ad_SwitchDataList_T = (omniORB.tcInternal.tv_alias, SwitchDataList_T._NP_RepositoryId, "SwitchDataList_T", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/SwitchData_T:1.0"], 0))
_0_protection._tc_SwitchDataList_T = omniORB.tcInternal.createTypeCode(_0_protection._ad_SwitchDataList_T)
omniORB.registerType(SwitchDataList_T._NP_RepositoryId, _0_protection._ad_SwitchDataList_T, _0_protection._tc_SwitchDataList_T)
del SwitchDataList_T

# struct ESwitchData_T
_0_protection.ESwitchData_T = omniORB.newEmptyClass()
class ESwitchData_T (omniORB.StructBase):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/protection/ESwitchData_T:1.0"

    def __init__(self, eProtectionGroupType, eSwitchReason, ePGPName, protectedE, switchToE, additionalInfo):
        self.eProtectionGroupType = eProtectionGroupType
        self.eSwitchReason = eSwitchReason
        self.ePGPName = ePGPName
        self.protectedE = protectedE
        self.switchToE = switchToE
        self.additionalInfo = additionalInfo

_0_protection.ESwitchData_T = ESwitchData_T
_0_protection._d_ESwitchData_T  = (omniORB.tcInternal.tv_struct, ESwitchData_T, ESwitchData_T._NP_RepositoryId, "ESwitchData_T", "eProtectionGroupType", omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/EProtectionGroupType_T:1.0"], "eSwitchReason", omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/ESwitchReason_T:1.0"], "ePGPName", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], "protectedE", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], "switchToE", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], "additionalInfo", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NVSList_T:1.0"])
_0_protection._tc_ESwitchData_T = omniORB.tcInternal.createTypeCode(_0_protection._d_ESwitchData_T)
omniORB.registerType(ESwitchData_T._NP_RepositoryId, _0_protection._d_ESwitchData_T, _0_protection._tc_ESwitchData_T)
del ESwitchData_T

# typedef ... ESwitchDataList_T
class ESwitchDataList_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/protection/ESwitchDataList_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_protection.ESwitchDataList_T = ESwitchDataList_T
_0_protection._d_ESwitchDataList_T  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/ESwitchData_T:1.0"], 0)
_0_protection._ad_ESwitchDataList_T = (omniORB.tcInternal.tv_alias, ESwitchDataList_T._NP_RepositoryId, "ESwitchDataList_T", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/ESwitchData_T:1.0"], 0))
_0_protection._tc_ESwitchDataList_T = omniORB.tcInternal.createTypeCode(_0_protection._ad_ESwitchDataList_T)
omniORB.registerType(ESwitchDataList_T._NP_RepositoryId, _0_protection._ad_ESwitchDataList_T, _0_protection._tc_ESwitchDataList_T)
del ESwitchDataList_T

# interface ProtectionGroupIterator_I
_0_protection._d_ProtectionGroupIterator_I = (omniORB.tcInternal.tv_objref, "IDL:mtnm.tmforum.org/protection/ProtectionGroupIterator_I:1.0", "ProtectionGroupIterator_I")
omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/ProtectionGroupIterator_I:1.0"] = _0_protection._d_ProtectionGroupIterator_I
_0_protection.ProtectionGroupIterator_I = omniORB.newEmptyClass()
class ProtectionGroupIterator_I :
    _NP_RepositoryId = _0_protection._d_ProtectionGroupIterator_I[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_protection.ProtectionGroupIterator_I = ProtectionGroupIterator_I
_0_protection._tc_ProtectionGroupIterator_I = omniORB.tcInternal.createTypeCode(_0_protection._d_ProtectionGroupIterator_I)
omniORB.registerType(ProtectionGroupIterator_I._NP_RepositoryId, _0_protection._d_ProtectionGroupIterator_I, _0_protection._tc_ProtectionGroupIterator_I)

# ProtectionGroupIterator_I operations and attributes
ProtectionGroupIterator_I._d_next_n = ((omniORB.tcInternal.tv_ulong, ), (omniORB.tcInternal.tv_boolean, omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/ProtectionGroupList_T:1.0"]), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
ProtectionGroupIterator_I._d_getLength = ((), (omniORB.tcInternal.tv_ulong, ), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
ProtectionGroupIterator_I._d_destroy = ((), (), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})

# ProtectionGroupIterator_I object reference
class _objref_ProtectionGroupIterator_I (CORBA.Object):
    _NP_RepositoryId = ProtectionGroupIterator_I._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def next_n(self, *args):
        return self._obj.invoke("next_n", _0_protection.ProtectionGroupIterator_I._d_next_n, args)

    def getLength(self, *args):
        return self._obj.invoke("getLength", _0_protection.ProtectionGroupIterator_I._d_getLength, args)

    def destroy(self, *args):
        return self._obj.invoke("destroy", _0_protection.ProtectionGroupIterator_I._d_destroy, args)

omniORB.registerObjref(ProtectionGroupIterator_I._NP_RepositoryId, _objref_ProtectionGroupIterator_I)
_0_protection._objref_ProtectionGroupIterator_I = _objref_ProtectionGroupIterator_I
del ProtectionGroupIterator_I, _objref_ProtectionGroupIterator_I

# ProtectionGroupIterator_I skeleton
__name__ = "protection__POA"
class ProtectionGroupIterator_I (PortableServer.Servant):
    _NP_RepositoryId = _0_protection.ProtectionGroupIterator_I._NP_RepositoryId


    _omni_op_d = {"next_n": _0_protection.ProtectionGroupIterator_I._d_next_n, "getLength": _0_protection.ProtectionGroupIterator_I._d_getLength, "destroy": _0_protection.ProtectionGroupIterator_I._d_destroy}

ProtectionGroupIterator_I._omni_skeleton = ProtectionGroupIterator_I
_0_protection__POA.ProtectionGroupIterator_I = ProtectionGroupIterator_I
omniORB.registerSkeleton(ProtectionGroupIterator_I._NP_RepositoryId, ProtectionGroupIterator_I)
del ProtectionGroupIterator_I
__name__ = "protection"

# interface EProtectionGroupIterator_I
_0_protection._d_EProtectionGroupIterator_I = (omniORB.tcInternal.tv_objref, "IDL:mtnm.tmforum.org/protection/EProtectionGroupIterator_I:1.0", "EProtectionGroupIterator_I")
omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/EProtectionGroupIterator_I:1.0"] = _0_protection._d_EProtectionGroupIterator_I
_0_protection.EProtectionGroupIterator_I = omniORB.newEmptyClass()
class EProtectionGroupIterator_I :
    _NP_RepositoryId = _0_protection._d_EProtectionGroupIterator_I[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_protection.EProtectionGroupIterator_I = EProtectionGroupIterator_I
_0_protection._tc_EProtectionGroupIterator_I = omniORB.tcInternal.createTypeCode(_0_protection._d_EProtectionGroupIterator_I)
omniORB.registerType(EProtectionGroupIterator_I._NP_RepositoryId, _0_protection._d_EProtectionGroupIterator_I, _0_protection._tc_EProtectionGroupIterator_I)

# EProtectionGroupIterator_I operations and attributes
EProtectionGroupIterator_I._d_next_n = ((omniORB.tcInternal.tv_ulong, ), (omniORB.tcInternal.tv_boolean, omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/EProtectionGroupList_T:1.0"]), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
EProtectionGroupIterator_I._d_getLength = ((), (omniORB.tcInternal.tv_ulong, ), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
EProtectionGroupIterator_I._d_destroy = ((), (), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})

# EProtectionGroupIterator_I object reference
class _objref_EProtectionGroupIterator_I (CORBA.Object):
    _NP_RepositoryId = EProtectionGroupIterator_I._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def next_n(self, *args):
        return self._obj.invoke("next_n", _0_protection.EProtectionGroupIterator_I._d_next_n, args)

    def getLength(self, *args):
        return self._obj.invoke("getLength", _0_protection.EProtectionGroupIterator_I._d_getLength, args)

    def destroy(self, *args):
        return self._obj.invoke("destroy", _0_protection.EProtectionGroupIterator_I._d_destroy, args)

omniORB.registerObjref(EProtectionGroupIterator_I._NP_RepositoryId, _objref_EProtectionGroupIterator_I)
_0_protection._objref_EProtectionGroupIterator_I = _objref_EProtectionGroupIterator_I
del EProtectionGroupIterator_I, _objref_EProtectionGroupIterator_I

# EProtectionGroupIterator_I skeleton
__name__ = "protection__POA"
class EProtectionGroupIterator_I (PortableServer.Servant):
    _NP_RepositoryId = _0_protection.EProtectionGroupIterator_I._NP_RepositoryId


    _omni_op_d = {"next_n": _0_protection.EProtectionGroupIterator_I._d_next_n, "getLength": _0_protection.EProtectionGroupIterator_I._d_getLength, "destroy": _0_protection.EProtectionGroupIterator_I._d_destroy}

EProtectionGroupIterator_I._omni_skeleton = EProtectionGroupIterator_I
_0_protection__POA.EProtectionGroupIterator_I = EProtectionGroupIterator_I
omniORB.registerSkeleton(EProtectionGroupIterator_I._NP_RepositoryId, EProtectionGroupIterator_I)
del EProtectionGroupIterator_I
__name__ = "protection"

# interface ProtectionMgr_I
_0_protection._d_ProtectionMgr_I = (omniORB.tcInternal.tv_objref, "IDL:mtnm.tmforum.org/protection/ProtectionMgr_I:1.0", "ProtectionMgr_I")
omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/ProtectionMgr_I:1.0"] = _0_protection._d_ProtectionMgr_I
_0_protection.ProtectionMgr_I = omniORB.newEmptyClass()
class ProtectionMgr_I (_0_common.Common_I):
    _NP_RepositoryId = _0_protection._d_ProtectionMgr_I[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_protection.ProtectionMgr_I = ProtectionMgr_I
_0_protection._tc_ProtectionMgr_I = omniORB.tcInternal.createTypeCode(_0_protection._d_ProtectionMgr_I)
omniORB.registerType(ProtectionMgr_I._NP_RepositoryId, _0_protection._d_ProtectionMgr_I, _0_protection._tc_ProtectionMgr_I)

# ProtectionMgr_I operations and attributes
ProtectionMgr_I._d_getAllProtectionGroups = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], omniORB.tcInternal.tv_ulong), (omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/ProtectionGroupList_T:1.0"], omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/ProtectionGroupIterator_I:1.0"]), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
ProtectionMgr_I._d_getAllEProtectionGroups = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], omniORB.tcInternal.tv_ulong), (omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/EProtectionGroupList_T:1.0"], omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/EProtectionGroupIterator_I:1.0"]), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
ProtectionMgr_I._d_getProtectionGroup = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], ), (omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/ProtectionGroup_T:1.0"], ), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
ProtectionMgr_I._d_getEProtectionGroup = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], ), (omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/EProtectionGroup_T:1.0"], ), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
ProtectionMgr_I._d_getAllNUTTPNames = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], omniORB.tcInternal.tv_ulong), (omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributesList_T:1.0"], omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributesIterator_I:1.0"]), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
ProtectionMgr_I._d_getAllPreemptibleTPNames = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], omniORB.tcInternal.tv_ulong), (omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributesList_T:1.0"], omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributesIterator_I:1.0"]), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
ProtectionMgr_I._d_getAllProtectedTPNames = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], omniORB.tcInternal.tv_ulong), (omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributesList_T:1.0"], omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributesIterator_I:1.0"]), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
ProtectionMgr_I._d_retrieveSwitchData = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], ), (omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/SwitchDataList_T:1.0"], ), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
ProtectionMgr_I._d_retrieveESwitchData = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], ), (omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/ESwitchDataList_T:1.0"], ), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
ProtectionMgr_I._d_performProtectionCommand = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/ProtectionCommand_T:1.0"], omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"]), (omniORB.typeMapping["IDL:mtnm.tmforum.org/protection/SwitchData_T:1.0"], ), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
ProtectionMgr_I._d_getContainingPGNames = ((omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], ), (omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributesList_T:1.0"], ), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})

# ProtectionMgr_I object reference
class _objref_ProtectionMgr_I (_0_common._objref_Common_I):
    _NP_RepositoryId = ProtectionMgr_I._NP_RepositoryId

    def __init__(self, obj):
        _0_common._objref_Common_I.__init__(self, obj)

    def getAllProtectionGroups(self, *args):
        return self._obj.invoke("getAllProtectionGroups", _0_protection.ProtectionMgr_I._d_getAllProtectionGroups, args)

    def getAllEProtectionGroups(self, *args):
        return self._obj.invoke("getAllEProtectionGroups", _0_protection.ProtectionMgr_I._d_getAllEProtectionGroups, args)

    def getProtectionGroup(self, *args):
        return self._obj.invoke("getProtectionGroup", _0_protection.ProtectionMgr_I._d_getProtectionGroup, args)

    def getEProtectionGroup(self, *args):
        return self._obj.invoke("getEProtectionGroup", _0_protection.ProtectionMgr_I._d_getEProtectionGroup, args)

    def getAllNUTTPNames(self, *args):
        return self._obj.invoke("getAllNUTTPNames", _0_protection.ProtectionMgr_I._d_getAllNUTTPNames, args)

    def getAllPreemptibleTPNames(self, *args):
        return self._obj.invoke("getAllPreemptibleTPNames", _0_protection.ProtectionMgr_I._d_getAllPreemptibleTPNames, args)

    def getAllProtectedTPNames(self, *args):
        return self._obj.invoke("getAllProtectedTPNames", _0_protection.ProtectionMgr_I._d_getAllProtectedTPNames, args)

    def retrieveSwitchData(self, *args):
        return self._obj.invoke("retrieveSwitchData", _0_protection.ProtectionMgr_I._d_retrieveSwitchData, args)

    def retrieveESwitchData(self, *args):
        return self._obj.invoke("retrieveESwitchData", _0_protection.ProtectionMgr_I._d_retrieveESwitchData, args)

    def performProtectionCommand(self, *args):
        return self._obj.invoke("performProtectionCommand", _0_protection.ProtectionMgr_I._d_performProtectionCommand, args)

    def getContainingPGNames(self, *args):
        return self._obj.invoke("getContainingPGNames", _0_protection.ProtectionMgr_I._d_getContainingPGNames, args)

omniORB.registerObjref(ProtectionMgr_I._NP_RepositoryId, _objref_ProtectionMgr_I)
_0_protection._objref_ProtectionMgr_I = _objref_ProtectionMgr_I
del ProtectionMgr_I, _objref_ProtectionMgr_I

# ProtectionMgr_I skeleton
__name__ = "protection__POA"
class ProtectionMgr_I (_0_common__POA.Common_I):
    _NP_RepositoryId = _0_protection.ProtectionMgr_I._NP_RepositoryId


    _omni_op_d = {"getAllProtectionGroups": _0_protection.ProtectionMgr_I._d_getAllProtectionGroups, "getAllEProtectionGroups": _0_protection.ProtectionMgr_I._d_getAllEProtectionGroups, "getProtectionGroup": _0_protection.ProtectionMgr_I._d_getProtectionGroup, "getEProtectionGroup": _0_protection.ProtectionMgr_I._d_getEProtectionGroup, "getAllNUTTPNames": _0_protection.ProtectionMgr_I._d_getAllNUTTPNames, "getAllPreemptibleTPNames": _0_protection.ProtectionMgr_I._d_getAllPreemptibleTPNames, "getAllProtectedTPNames": _0_protection.ProtectionMgr_I._d_getAllProtectedTPNames, "retrieveSwitchData": _0_protection.ProtectionMgr_I._d_retrieveSwitchData, "retrieveESwitchData": _0_protection.ProtectionMgr_I._d_retrieveESwitchData, "performProtectionCommand": _0_protection.ProtectionMgr_I._d_performProtectionCommand, "getContainingPGNames": _0_protection.ProtectionMgr_I._d_getContainingPGNames}
    _omni_op_d.update(_0_common__POA.Common_I._omni_op_d)

ProtectionMgr_I._omni_skeleton = ProtectionMgr_I
_0_protection__POA.ProtectionMgr_I = ProtectionMgr_I
omniORB.registerSkeleton(ProtectionMgr_I._NP_RepositoryId, ProtectionMgr_I)
del ProtectionMgr_I
__name__ = "protection"

#
# End of module "protection"
#
__name__ = "protection_idl"

_exported_modules = ( "protection", )

# The end.
