# Python stubs generated by omniidl from notifications.idl
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

# #include "OMGidl/CosNotification.idl"
import CosNotification_idl
_0_CosNotification = omniORB.openModule("CosNotification")
_0_CosNotification__POA = omniORB.openModule("CosNotification__POA")

# #include "transmissionParameters.idl"
import transmissionParameters_idl
_0_transmissionParameters = omniORB.openModule("transmissionParameters")
_0_transmissionParameters__POA = omniORB.openModule("transmissionParameters__POA")

# #include "common.idl"
import common_idl
_0_common = omniORB.openModule("common")
_0_common__POA = omniORB.openModule("common__POA")

# #include "performance.idl"
import performance_idl
_0_performance = omniORB.openModule("performance")
_0_performance__POA = omniORB.openModule("performance__POA")

#
# Start of module "notifications"
#
__name__ = "notifications"
_0_notifications = omniORB.openModule("notifications", r"notifications.idl")
_0_notifications__POA = omniORB.openModule("notifications__POA", r"notifications.idl")


# enum ObjectType_T
_0_notifications.OT_EMS = omniORB.EnumItem("OT_EMS", 0)
_0_notifications.OT_MANAGED_ELEMENT = omniORB.EnumItem("OT_MANAGED_ELEMENT", 1)
_0_notifications.OT_MULTILAYER_SUBNETWORK = omniORB.EnumItem("OT_MULTILAYER_SUBNETWORK", 2)
_0_notifications.OT_TOPOLOGICAL_LINK = omniORB.EnumItem("OT_TOPOLOGICAL_LINK", 3)
_0_notifications.OT_SUBNETWORK_CONNECTION = omniORB.EnumItem("OT_SUBNETWORK_CONNECTION", 4)
_0_notifications.OT_PHYSICAL_TERMINATION_POINT = omniORB.EnumItem("OT_PHYSICAL_TERMINATION_POINT", 5)
_0_notifications.OT_CONNECTION_TERMINATION_POINT = omniORB.EnumItem("OT_CONNECTION_TERMINATION_POINT", 6)
_0_notifications.OT_TERMINATION_POINT_POOL = omniORB.EnumItem("OT_TERMINATION_POINT_POOL", 7)
_0_notifications.OT_EQUIPMENT_HOLDER = omniORB.EnumItem("OT_EQUIPMENT_HOLDER", 8)
_0_notifications.OT_EQUIPMENT = omniORB.EnumItem("OT_EQUIPMENT", 9)
_0_notifications.OT_PROTECTION_GROUP = omniORB.EnumItem("OT_PROTECTION_GROUP", 10)
_0_notifications.OT_TRAFFIC_DESCRIPTOR = omniORB.EnumItem("OT_TRAFFIC_DESCRIPTOR", 11)
_0_notifications.OT_AID = omniORB.EnumItem("OT_AID", 12)
_0_notifications.ObjectType_T = omniORB.Enum("IDL:mtnm.tmforum.org/notifications/ObjectType_T:1.0", (_0_notifications.OT_EMS, _0_notifications.OT_MANAGED_ELEMENT, _0_notifications.OT_MULTILAYER_SUBNETWORK, _0_notifications.OT_TOPOLOGICAL_LINK, _0_notifications.OT_SUBNETWORK_CONNECTION, _0_notifications.OT_PHYSICAL_TERMINATION_POINT, _0_notifications.OT_CONNECTION_TERMINATION_POINT, _0_notifications.OT_TERMINATION_POINT_POOL, _0_notifications.OT_EQUIPMENT_HOLDER, _0_notifications.OT_EQUIPMENT, _0_notifications.OT_PROTECTION_GROUP, _0_notifications.OT_TRAFFIC_DESCRIPTOR, _0_notifications.OT_AID,))

_0_notifications._d_ObjectType_T  = (omniORB.tcInternal.tv_enum, _0_notifications.ObjectType_T._NP_RepositoryId, "ObjectType_T", _0_notifications.ObjectType_T._items)
_0_notifications._tc_ObjectType_T = omniORB.tcInternal.createTypeCode(_0_notifications._d_ObjectType_T)
omniORB.registerType(_0_notifications.ObjectType_T._NP_RepositoryId, _0_notifications._d_ObjectType_T, _0_notifications._tc_ObjectType_T)

# typedef ... ObjectTypeQualifier_T
class ObjectTypeQualifier_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/notifications/ObjectTypeQualifier_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_notifications.ObjectTypeQualifier_T = ObjectTypeQualifier_T
_0_notifications._d_ObjectTypeQualifier_T  = (omniORB.tcInternal.tv_string,0)
_0_notifications._ad_ObjectTypeQualifier_T = (omniORB.tcInternal.tv_alias, ObjectTypeQualifier_T._NP_RepositoryId, "ObjectTypeQualifier_T", (omniORB.tcInternal.tv_string,0))
_0_notifications._tc_ObjectTypeQualifier_T = omniORB.tcInternal.createTypeCode(_0_notifications._ad_ObjectTypeQualifier_T)
omniORB.registerType(ObjectTypeQualifier_T._NP_RepositoryId, _0_notifications._ad_ObjectTypeQualifier_T, _0_notifications._tc_ObjectTypeQualifier_T)
del ObjectTypeQualifier_T

# enum PerceivedSeverity_T
_0_notifications.PS_INDETERMINATE = omniORB.EnumItem("PS_INDETERMINATE", 0)
_0_notifications.PS_CRITICAL = omniORB.EnumItem("PS_CRITICAL", 1)
_0_notifications.PS_MAJOR = omniORB.EnumItem("PS_MAJOR", 2)
_0_notifications.PS_MINOR = omniORB.EnumItem("PS_MINOR", 3)
_0_notifications.PS_WARNING = omniORB.EnumItem("PS_WARNING", 4)
_0_notifications.PS_CLEARED = omniORB.EnumItem("PS_CLEARED", 5)
_0_notifications.PerceivedSeverity_T = omniORB.Enum("IDL:mtnm.tmforum.org/notifications/PerceivedSeverity_T:1.0", (_0_notifications.PS_INDETERMINATE, _0_notifications.PS_CRITICAL, _0_notifications.PS_MAJOR, _0_notifications.PS_MINOR, _0_notifications.PS_WARNING, _0_notifications.PS_CLEARED,))

_0_notifications._d_PerceivedSeverity_T  = (omniORB.tcInternal.tv_enum, _0_notifications.PerceivedSeverity_T._NP_RepositoryId, "PerceivedSeverity_T", _0_notifications.PerceivedSeverity_T._items)
_0_notifications._tc_PerceivedSeverity_T = omniORB.tcInternal.createTypeCode(_0_notifications._d_PerceivedSeverity_T)
omniORB.registerType(_0_notifications.PerceivedSeverity_T._NP_RepositoryId, _0_notifications._d_PerceivedSeverity_T, _0_notifications._tc_PerceivedSeverity_T)

# enum AcknowledgeIndication_T
_0_notifications.AI_EVENT_ACKNOWLEDGED = omniORB.EnumItem("AI_EVENT_ACKNOWLEDGED", 0)
_0_notifications.AI_EVENT_UNACKNOWLEDGED = omniORB.EnumItem("AI_EVENT_UNACKNOWLEDGED", 1)
_0_notifications.AI_NA = omniORB.EnumItem("AI_NA", 2)
_0_notifications.AcknowledgeIndication_T = omniORB.Enum("IDL:mtnm.tmforum.org/notifications/AcknowledgeIndication_T:1.0", (_0_notifications.AI_EVENT_ACKNOWLEDGED, _0_notifications.AI_EVENT_UNACKNOWLEDGED, _0_notifications.AI_NA,))

_0_notifications._d_AcknowledgeIndication_T  = (omniORB.tcInternal.tv_enum, _0_notifications.AcknowledgeIndication_T._NP_RepositoryId, "AcknowledgeIndication_T", _0_notifications.AcknowledgeIndication_T._items)
_0_notifications._tc_AcknowledgeIndication_T = omniORB.tcInternal.createTypeCode(_0_notifications._d_AcknowledgeIndication_T)
omniORB.registerType(_0_notifications.AcknowledgeIndication_T._NP_RepositoryId, _0_notifications._d_AcknowledgeIndication_T, _0_notifications._tc_AcknowledgeIndication_T)

# enum AlarmTypeQualifier_T
_0_notifications.ALARM = omniORB.EnumItem("ALARM", 0)
_0_notifications.TCA = omniORB.EnumItem("TCA", 1)
_0_notifications.AlarmTypeQualifier_T = omniORB.Enum("IDL:mtnm.tmforum.org/notifications/AlarmTypeQualifier_T:1.0", (_0_notifications.ALARM, _0_notifications.TCA,))

_0_notifications._d_AlarmTypeQualifier_T  = (omniORB.tcInternal.tv_enum, _0_notifications.AlarmTypeQualifier_T._NP_RepositoryId, "AlarmTypeQualifier_T", _0_notifications.AlarmTypeQualifier_T._items)
_0_notifications._tc_AlarmTypeQualifier_T = omniORB.tcInternal.createTypeCode(_0_notifications._d_AlarmTypeQualifier_T)
omniORB.registerType(_0_notifications.AlarmTypeQualifier_T._NP_RepositoryId, _0_notifications._d_AlarmTypeQualifier_T, _0_notifications._tc_AlarmTypeQualifier_T)

# typedef ... PerceivedSeverityList_T
class PerceivedSeverityList_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/notifications/PerceivedSeverityList_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_notifications.PerceivedSeverityList_T = PerceivedSeverityList_T
_0_notifications._d_PerceivedSeverityList_T  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/notifications/PerceivedSeverity_T:1.0"], 0)
_0_notifications._ad_PerceivedSeverityList_T = (omniORB.tcInternal.tv_alias, PerceivedSeverityList_T._NP_RepositoryId, "PerceivedSeverityList_T", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/notifications/PerceivedSeverity_T:1.0"], 0))
_0_notifications._tc_PerceivedSeverityList_T = omniORB.tcInternal.createTypeCode(_0_notifications._ad_PerceivedSeverityList_T)
omniORB.registerType(PerceivedSeverityList_T._NP_RepositoryId, _0_notifications._ad_PerceivedSeverityList_T, _0_notifications._tc_PerceivedSeverityList_T)
del PerceivedSeverityList_T

# enum ServiceAffecting_T
_0_notifications.SA_UNKNOWN = omniORB.EnumItem("SA_UNKNOWN", 0)
_0_notifications.SA_SERVICE_AFFECTING = omniORB.EnumItem("SA_SERVICE_AFFECTING", 1)
_0_notifications.SA_NON_SERVICE_AFFECTING = omniORB.EnumItem("SA_NON_SERVICE_AFFECTING", 2)
_0_notifications.ServiceAffecting_T = omniORB.Enum("IDL:mtnm.tmforum.org/notifications/ServiceAffecting_T:1.0", (_0_notifications.SA_UNKNOWN, _0_notifications.SA_SERVICE_AFFECTING, _0_notifications.SA_NON_SERVICE_AFFECTING,))

_0_notifications._d_ServiceAffecting_T  = (omniORB.tcInternal.tv_enum, _0_notifications.ServiceAffecting_T._NP_RepositoryId, "ServiceAffecting_T", _0_notifications.ServiceAffecting_T._items)
_0_notifications._tc_ServiceAffecting_T = omniORB.tcInternal.createTypeCode(_0_notifications._d_ServiceAffecting_T)
omniORB.registerType(_0_notifications.ServiceAffecting_T._NP_RepositoryId, _0_notifications._d_ServiceAffecting_T, _0_notifications._tc_ServiceAffecting_T)

# typedef ... ProbableCauseList_T
class ProbableCauseList_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/notifications/ProbableCauseList_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_notifications.ProbableCauseList_T = ProbableCauseList_T
_0_notifications._d_ProbableCauseList_T  = (omniORB.tcInternal.tv_sequence, (omniORB.tcInternal.tv_string,0), 0)
_0_notifications._ad_ProbableCauseList_T = (omniORB.tcInternal.tv_alias, ProbableCauseList_T._NP_RepositoryId, "ProbableCauseList_T", (omniORB.tcInternal.tv_sequence, (omniORB.tcInternal.tv_string,0), 0))
_0_notifications._tc_ProbableCauseList_T = omniORB.tcInternal.createTypeCode(_0_notifications._ad_ProbableCauseList_T)
omniORB.registerType(ProbableCauseList_T._NP_RepositoryId, _0_notifications._ad_ProbableCauseList_T, _0_notifications._tc_ProbableCauseList_T)
del ProbableCauseList_T

# struct NameAndAnyValue_T
_0_notifications.NameAndAnyValue_T = omniORB.newEmptyClass()
class NameAndAnyValue_T (omniORB.StructBase):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/notifications/NameAndAnyValue_T:1.0"

    def __init__(self, name, value):
        self.name = name
        self.value = value

_0_notifications.NameAndAnyValue_T = NameAndAnyValue_T
_0_notifications._d_NameAndAnyValue_T  = (omniORB.tcInternal.tv_struct, NameAndAnyValue_T, NameAndAnyValue_T._NP_RepositoryId, "NameAndAnyValue_T", "name", (omniORB.tcInternal.tv_string,0), "value", omniORB.tcInternal.tv_any)
_0_notifications._tc_NameAndAnyValue_T = omniORB.tcInternal.createTypeCode(_0_notifications._d_NameAndAnyValue_T)
omniORB.registerType(NameAndAnyValue_T._NP_RepositoryId, _0_notifications._d_NameAndAnyValue_T, _0_notifications._tc_NameAndAnyValue_T)
del NameAndAnyValue_T

# typedef ... NVList_T
class NVList_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/notifications/NVList_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_notifications.NVList_T = NVList_T
_0_notifications._d_NVList_T  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/notifications/NameAndAnyValue_T:1.0"], 0)
_0_notifications._ad_NVList_T = (omniORB.tcInternal.tv_alias, NVList_T._NP_RepositoryId, "NVList_T", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/notifications/NameAndAnyValue_T:1.0"], 0))
_0_notifications._tc_NVList_T = omniORB.tcInternal.createTypeCode(_0_notifications._ad_NVList_T)
omniORB.registerType(NVList_T._NP_RepositoryId, _0_notifications._ad_NVList_T, _0_notifications._tc_NVList_T)
del NVList_T

# enum FileTransferStatus_T
_0_notifications.FT_IN_PROGRESS = omniORB.EnumItem("FT_IN_PROGRESS", 0)
_0_notifications.FT_FAILED = omniORB.EnumItem("FT_FAILED", 1)
_0_notifications.FT_COMPLETED = omniORB.EnumItem("FT_COMPLETED", 2)
_0_notifications.FileTransferStatus_T = omniORB.Enum("IDL:mtnm.tmforum.org/notifications/FileTransferStatus_T:1.0", (_0_notifications.FT_IN_PROGRESS, _0_notifications.FT_FAILED, _0_notifications.FT_COMPLETED,))

_0_notifications._d_FileTransferStatus_T  = (omniORB.tcInternal.tv_enum, _0_notifications.FileTransferStatus_T._NP_RepositoryId, "FileTransferStatus_T", _0_notifications.FileTransferStatus_T._items)
_0_notifications._tc_FileTransferStatus_T = omniORB.tcInternal.createTypeCode(_0_notifications._d_FileTransferStatus_T)
omniORB.registerType(_0_notifications.FileTransferStatus_T._NP_RepositoryId, _0_notifications._d_FileTransferStatus_T, _0_notifications._tc_FileTransferStatus_T)

# typedef ... EventList_T
class EventList_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/notifications/EventList_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_notifications.EventList_T = EventList_T
_0_notifications._d_EventList_T  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosNotification/StructuredEvent:1.0"], 0)
_0_notifications._ad_EventList_T = (omniORB.tcInternal.tv_alias, EventList_T._NP_RepositoryId, "EventList_T", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosNotification/StructuredEvent:1.0"], 0))
_0_notifications._tc_EventList_T = omniORB.tcInternal.createTypeCode(_0_notifications._ad_EventList_T)
omniORB.registerType(EventList_T._NP_RepositoryId, _0_notifications._ad_EventList_T, _0_notifications._tc_EventList_T)
del EventList_T

# typedef ... SpecificProblem_T
class SpecificProblem_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/notifications/SpecificProblem_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_notifications.SpecificProblem_T = SpecificProblem_T
_0_notifications._d_SpecificProblem_T  = (omniORB.tcInternal.tv_string,0)
_0_notifications._ad_SpecificProblem_T = (omniORB.tcInternal.tv_alias, SpecificProblem_T._NP_RepositoryId, "SpecificProblem_T", (omniORB.tcInternal.tv_string,0))
_0_notifications._tc_SpecificProblem_T = omniORB.tcInternal.createTypeCode(_0_notifications._ad_SpecificProblem_T)
omniORB.registerType(SpecificProblem_T._NP_RepositoryId, _0_notifications._ad_SpecificProblem_T, _0_notifications._tc_SpecificProblem_T)
del SpecificProblem_T

# typedef ... SpecificProblemList_T
class SpecificProblemList_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/notifications/SpecificProblemList_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_notifications.SpecificProblemList_T = SpecificProblemList_T
_0_notifications._d_SpecificProblemList_T  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/notifications/SpecificProblem_T:1.0"], 0)
_0_notifications._ad_SpecificProblemList_T = (omniORB.tcInternal.tv_alias, SpecificProblemList_T._NP_RepositoryId, "SpecificProblemList_T", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/notifications/SpecificProblem_T:1.0"], 0))
_0_notifications._tc_SpecificProblemList_T = omniORB.tcInternal.createTypeCode(_0_notifications._ad_SpecificProblemList_T)
omniORB.registerType(SpecificProblemList_T._NP_RepositoryId, _0_notifications._ad_SpecificProblemList_T, _0_notifications._tc_SpecificProblemList_T)
del SpecificProblemList_T

# typedef ... NotifIDList_T
class NotifIDList_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/notifications/NotifIDList_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_notifications.NotifIDList_T = NotifIDList_T
_0_notifications._d_NotifIDList_T  = (omniORB.tcInternal.tv_sequence, (omniORB.tcInternal.tv_string,0), 0)
_0_notifications._ad_NotifIDList_T = (omniORB.tcInternal.tv_alias, NotifIDList_T._NP_RepositoryId, "NotifIDList_T", (omniORB.tcInternal.tv_sequence, (omniORB.tcInternal.tv_string,0), 0))
_0_notifications._tc_NotifIDList_T = omniORB.tcInternal.createTypeCode(_0_notifications._ad_NotifIDList_T)
omniORB.registerType(NotifIDList_T._NP_RepositoryId, _0_notifications._ad_NotifIDList_T, _0_notifications._tc_NotifIDList_T)
del NotifIDList_T

# struct CorrelatedNotifications_T
_0_notifications.CorrelatedNotifications_T = omniORB.newEmptyClass()
class CorrelatedNotifications_T (omniORB.StructBase):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/notifications/CorrelatedNotifications_T:1.0"

    def __init__(self, source, notifIDs):
        self.source = source
        self.notifIDs = notifIDs

_0_notifications.CorrelatedNotifications_T = CorrelatedNotifications_T
_0_notifications._d_CorrelatedNotifications_T  = (omniORB.tcInternal.tv_struct, CorrelatedNotifications_T, CorrelatedNotifications_T._NP_RepositoryId, "CorrelatedNotifications_T", "source", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], "notifIDs", omniORB.typeMapping["IDL:mtnm.tmforum.org/notifications/NotifIDList_T:1.0"])
_0_notifications._tc_CorrelatedNotifications_T = omniORB.tcInternal.createTypeCode(_0_notifications._d_CorrelatedNotifications_T)
omniORB.registerType(CorrelatedNotifications_T._NP_RepositoryId, _0_notifications._d_CorrelatedNotifications_T, _0_notifications._tc_CorrelatedNotifications_T)
del CorrelatedNotifications_T

# typedef ... CorrelatedNotificationList_T
class CorrelatedNotificationList_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/notifications/CorrelatedNotificationList_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_notifications.CorrelatedNotificationList_T = CorrelatedNotificationList_T
_0_notifications._d_CorrelatedNotificationList_T  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/notifications/CorrelatedNotifications_T:1.0"], 0)
_0_notifications._ad_CorrelatedNotificationList_T = (omniORB.tcInternal.tv_alias, CorrelatedNotificationList_T._NP_RepositoryId, "CorrelatedNotificationList_T", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/notifications/CorrelatedNotifications_T:1.0"], 0))
_0_notifications._tc_CorrelatedNotificationList_T = omniORB.tcInternal.createTypeCode(_0_notifications._ad_CorrelatedNotificationList_T)
omniORB.registerType(CorrelatedNotificationList_T._NP_RepositoryId, _0_notifications._ad_CorrelatedNotificationList_T, _0_notifications._tc_CorrelatedNotificationList_T)
del CorrelatedNotificationList_T

# typedef ... ProposedRepairAction_T
class ProposedRepairAction_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/notifications/ProposedRepairAction_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_notifications.ProposedRepairAction_T = ProposedRepairAction_T
_0_notifications._d_ProposedRepairAction_T  = (omniORB.tcInternal.tv_string,0)
_0_notifications._ad_ProposedRepairAction_T = (omniORB.tcInternal.tv_alias, ProposedRepairAction_T._NP_RepositoryId, "ProposedRepairAction_T", (omniORB.tcInternal.tv_string,0))
_0_notifications._tc_ProposedRepairAction_T = omniORB.tcInternal.createTypeCode(_0_notifications._ad_ProposedRepairAction_T)
omniORB.registerType(ProposedRepairAction_T._NP_RepositoryId, _0_notifications._ad_ProposedRepairAction_T, _0_notifications._tc_ProposedRepairAction_T)
del ProposedRepairAction_T

# typedef ... ProposedRepairActionList_T
class ProposedRepairActionList_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/notifications/ProposedRepairActionList_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_notifications.ProposedRepairActionList_T = ProposedRepairActionList_T
_0_notifications._d_ProposedRepairActionList_T  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/notifications/ProposedRepairAction_T:1.0"], 0)
_0_notifications._ad_ProposedRepairActionList_T = (omniORB.tcInternal.tv_alias, ProposedRepairActionList_T._NP_RepositoryId, "ProposedRepairActionList_T", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/notifications/ProposedRepairAction_T:1.0"], 0))
_0_notifications._tc_ProposedRepairActionList_T = omniORB.tcInternal.createTypeCode(_0_notifications._ad_ProposedRepairActionList_T)
omniORB.registerType(ProposedRepairActionList_T._NP_RepositoryId, _0_notifications._ad_ProposedRepairActionList_T, _0_notifications._tc_ProposedRepairActionList_T)
del ProposedRepairActionList_T

# struct AlarmId_T
_0_notifications.AlarmId_T = omniORB.newEmptyClass()
class AlarmId_T (omniORB.StructBase):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/notifications/AlarmId_T:1.0"

    def __init__(self, objectName, layerRate, probableCause, probableCauseQualifier):
        self.objectName = objectName
        self.layerRate = layerRate
        self.probableCause = probableCause
        self.probableCauseQualifier = probableCauseQualifier

_0_notifications.AlarmId_T = AlarmId_T
_0_notifications._d_AlarmId_T  = (omniORB.tcInternal.tv_struct, AlarmId_T, AlarmId_T._NP_RepositoryId, "AlarmId_T", "objectName", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], "layerRate", omniORB.typeMapping["IDL:mtnm.tmforum.org/transmissionParameters/LayerRate_T:1.0"], "probableCause", (omniORB.tcInternal.tv_string,0), "probableCauseQualifier", (omniORB.tcInternal.tv_string,0))
_0_notifications._tc_AlarmId_T = omniORB.tcInternal.createTypeCode(_0_notifications._d_AlarmId_T)
omniORB.registerType(AlarmId_T._NP_RepositoryId, _0_notifications._d_AlarmId_T, _0_notifications._tc_AlarmId_T)
del AlarmId_T

# struct TCAId_T
_0_notifications.TCAId_T = omniORB.newEmptyClass()
class TCAId_T (omniORB.StructBase):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/notifications/TCAId_T:1.0"

    def __init__(self, objectName, layerRate, pmParameterName, pmLocation, granularity):
        self.objectName = objectName
        self.layerRate = layerRate
        self.pmParameterName = pmParameterName
        self.pmLocation = pmLocation
        self.granularity = granularity

_0_notifications.TCAId_T = TCAId_T
_0_notifications._d_TCAId_T  = (omniORB.tcInternal.tv_struct, TCAId_T, TCAId_T._NP_RepositoryId, "TCAId_T", "objectName", omniORB.typeMapping["IDL:mtnm.tmforum.org/globaldefs/NamingAttributes_T:1.0"], "layerRate", omniORB.typeMapping["IDL:mtnm.tmforum.org/transmissionParameters/LayerRate_T:1.0"], "pmParameterName", omniORB.typeMapping["IDL:mtnm.tmforum.org/performance/PMParameterName_T:1.0"], "pmLocation", omniORB.typeMapping["IDL:mtnm.tmforum.org/performance/PMLocation_T:1.0"], "granularity", omniORB.typeMapping["IDL:mtnm.tmforum.org/performance/Granularity_T:1.0"])
_0_notifications._tc_TCAId_T = omniORB.tcInternal.createTypeCode(_0_notifications._d_TCAId_T)
omniORB.registerType(TCAId_T._NP_RepositoryId, _0_notifications._d_TCAId_T, _0_notifications._tc_TCAId_T)
del TCAId_T

# union AlarmOrTCAIdentifier_T
_0_notifications.AlarmOrTCAIdentifier_T = omniORB.newEmptyClass()
class AlarmOrTCAIdentifier_T (omniORB.Union):
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/notifications/AlarmOrTCAIdentifier_T:1.0"

_0_notifications.AlarmOrTCAIdentifier_T = AlarmOrTCAIdentifier_T

AlarmOrTCAIdentifier_T._m_to_d = {"alarmId": _0_notifications.ALARM, "tcaId": _0_notifications.TCA}
AlarmOrTCAIdentifier_T._d_to_m = {_0_notifications.ALARM: "alarmId", _0_notifications.TCA: "tcaId"}
AlarmOrTCAIdentifier_T._def_m  = None
AlarmOrTCAIdentifier_T._def_d  = None

_0_notifications._m_AlarmOrTCAIdentifier_T  = ((_0_notifications.ALARM, "alarmId", omniORB.typeMapping["IDL:mtnm.tmforum.org/notifications/AlarmId_T:1.0"]), (_0_notifications.TCA, "tcaId", omniORB.typeMapping["IDL:mtnm.tmforum.org/notifications/TCAId_T:1.0"]),)
_0_notifications._d_AlarmOrTCAIdentifier_T  = (omniORB.tcInternal.tv_union, AlarmOrTCAIdentifier_T, AlarmOrTCAIdentifier_T._NP_RepositoryId, "AlarmOrTCAIdentifier_T", omniORB.typeMapping["IDL:mtnm.tmforum.org/notifications/AlarmTypeQualifier_T:1.0"], -1, _0_notifications._m_AlarmOrTCAIdentifier_T, None, {_0_notifications.ALARM: _0_notifications._m_AlarmOrTCAIdentifier_T[0], _0_notifications.TCA: _0_notifications._m_AlarmOrTCAIdentifier_T[1]})
_0_notifications._tc_AlarmOrTCAIdentifier_T = omniORB.tcInternal.createTypeCode(_0_notifications._d_AlarmOrTCAIdentifier_T)
omniORB.registerType(AlarmOrTCAIdentifier_T._NP_RepositoryId, _0_notifications._d_AlarmOrTCAIdentifier_T, _0_notifications._tc_AlarmOrTCAIdentifier_T)
del AlarmOrTCAIdentifier_T

# typedef ... AlarmAndTCAIDList_T
class AlarmAndTCAIDList_T:
    _NP_RepositoryId = "IDL:mtnm.tmforum.org/notifications/AlarmAndTCAIDList_T:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_notifications.AlarmAndTCAIDList_T = AlarmAndTCAIDList_T
_0_notifications._d_AlarmAndTCAIDList_T  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/notifications/AlarmOrTCAIdentifier_T:1.0"], 0)
_0_notifications._ad_AlarmAndTCAIDList_T = (omniORB.tcInternal.tv_alias, AlarmAndTCAIDList_T._NP_RepositoryId, "AlarmAndTCAIDList_T", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:mtnm.tmforum.org/notifications/AlarmOrTCAIdentifier_T:1.0"], 0))
_0_notifications._tc_AlarmAndTCAIDList_T = omniORB.tcInternal.createTypeCode(_0_notifications._ad_AlarmAndTCAIDList_T)
omniORB.registerType(AlarmAndTCAIDList_T._NP_RepositoryId, _0_notifications._ad_AlarmAndTCAIDList_T, _0_notifications._tc_AlarmAndTCAIDList_T)
del AlarmAndTCAIDList_T

# interface EventIterator_I
_0_notifications._d_EventIterator_I = (omniORB.tcInternal.tv_objref, "IDL:mtnm.tmforum.org/notifications/EventIterator_I:1.0", "EventIterator_I")
omniORB.typeMapping["IDL:mtnm.tmforum.org/notifications/EventIterator_I:1.0"] = _0_notifications._d_EventIterator_I
_0_notifications.EventIterator_I = omniORB.newEmptyClass()
class EventIterator_I :
    _NP_RepositoryId = _0_notifications._d_EventIterator_I[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_notifications.EventIterator_I = EventIterator_I
_0_notifications._tc_EventIterator_I = omniORB.tcInternal.createTypeCode(_0_notifications._d_EventIterator_I)
omniORB.registerType(EventIterator_I._NP_RepositoryId, _0_notifications._d_EventIterator_I, _0_notifications._tc_EventIterator_I)

# EventIterator_I operations and attributes
EventIterator_I._d_next_n = ((omniORB.tcInternal.tv_ulong, ), (omniORB.tcInternal.tv_boolean, omniORB.typeMapping["IDL:mtnm.tmforum.org/notifications/EventList_T:1.0"]), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
EventIterator_I._d_getLength = ((), (omniORB.tcInternal.tv_ulong, ), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})
EventIterator_I._d_destroy = ((), (), {_0_globaldefs.ProcessingFailureException._NP_RepositoryId: _0_globaldefs._d_ProcessingFailureException})

# EventIterator_I object reference
class _objref_EventIterator_I (CORBA.Object):
    _NP_RepositoryId = EventIterator_I._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def next_n(self, *args):
        return self._obj.invoke("next_n", _0_notifications.EventIterator_I._d_next_n, args)

    def getLength(self, *args):
        return self._obj.invoke("getLength", _0_notifications.EventIterator_I._d_getLength, args)

    def destroy(self, *args):
        return self._obj.invoke("destroy", _0_notifications.EventIterator_I._d_destroy, args)

omniORB.registerObjref(EventIterator_I._NP_RepositoryId, _objref_EventIterator_I)
_0_notifications._objref_EventIterator_I = _objref_EventIterator_I
del EventIterator_I, _objref_EventIterator_I

# EventIterator_I skeleton
__name__ = "notifications__POA"
class EventIterator_I (PortableServer.Servant):
    _NP_RepositoryId = _0_notifications.EventIterator_I._NP_RepositoryId


    _omni_op_d = {"next_n": _0_notifications.EventIterator_I._d_next_n, "getLength": _0_notifications.EventIterator_I._d_getLength, "destroy": _0_notifications.EventIterator_I._d_destroy}

EventIterator_I._omni_skeleton = EventIterator_I
_0_notifications__POA.EventIterator_I = EventIterator_I
omniORB.registerSkeleton(EventIterator_I._NP_RepositoryId, EventIterator_I)
del EventIterator_I
__name__ = "notifications"

#
# End of module "notifications"
#
__name__ = "notifications_idl"

_exported_modules = ( "notifications", )

# The end.
