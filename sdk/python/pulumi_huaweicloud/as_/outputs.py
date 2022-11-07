# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'BandwidthPolicyScalingPolicyAction',
    'BandwidthPolicyScheduledPolicy',
    'ConfigurationInstanceConfig',
    'ConfigurationInstanceConfigDisk',
    'ConfigurationInstanceConfigPersonality',
    'ConfigurationInstanceConfigPublicIp',
    'ConfigurationInstanceConfigPublicIpEip',
    'ConfigurationInstanceConfigPublicIpEipBandwidth',
    'GroupLbaasListener',
    'GroupNetwork',
    'GroupSecurityGroup',
    'PolicyScalingPolicyAction',
    'PolicyScheduledPolicy',
]

@pulumi.output_type
class BandwidthPolicyScalingPolicyAction(dict):
    def __init__(__self__, *,
                 limits: Optional[int] = None,
                 operation: Optional[str] = None,
                 size: Optional[int] = None):
        """
        :param int limits: Specifies the operation restrictions.
               - If operation is not SET, this parameter takes effect and the unit is Mbit/s.
               - If operation is set to ADD, this parameter indicates the maximum bandwidth allowed.
               - If operation is set to REDUCE, this parameter indicates the minimum bandwidth allowed.
        :param str operation: Specifies the operation to be performed. The default operation is ADD.
               The options are as follows:
               - **ADD**: indicates adding the bandwidth size.
               - **REDUCE**: indicates reducing the bandwidth size.
               - **SET**: indicates setting the bandwidth size to a specified value.
        :param int size: Specifies the bandwidth (Mbit/s).
               The value is an integer from 1 to 2000. The default value is 1.
        """
        if limits is not None:
            pulumi.set(__self__, "limits", limits)
        if operation is not None:
            pulumi.set(__self__, "operation", operation)
        if size is not None:
            pulumi.set(__self__, "size", size)

    @property
    @pulumi.getter
    def limits(self) -> Optional[int]:
        """
        Specifies the operation restrictions.
        - If operation is not SET, this parameter takes effect and the unit is Mbit/s.
        - If operation is set to ADD, this parameter indicates the maximum bandwidth allowed.
        - If operation is set to REDUCE, this parameter indicates the minimum bandwidth allowed.
        """
        return pulumi.get(self, "limits")

    @property
    @pulumi.getter
    def operation(self) -> Optional[str]:
        """
        Specifies the operation to be performed. The default operation is ADD.
        The options are as follows:
        - **ADD**: indicates adding the bandwidth size.
        - **REDUCE**: indicates reducing the bandwidth size.
        - **SET**: indicates setting the bandwidth size to a specified value.
        """
        return pulumi.get(self, "operation")

    @property
    @pulumi.getter
    def size(self) -> Optional[int]:
        """
        Specifies the bandwidth (Mbit/s).
        The value is an integer from 1 to 2000. The default value is 1.
        """
        return pulumi.get(self, "size")


@pulumi.output_type
class BandwidthPolicyScheduledPolicy(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "launchTime":
            suggest = "launch_time"
        elif key == "endTime":
            suggest = "end_time"
        elif key == "recurrenceType":
            suggest = "recurrence_type"
        elif key == "recurrenceValue":
            suggest = "recurrence_value"
        elif key == "startTime":
            suggest = "start_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BandwidthPolicyScheduledPolicy. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BandwidthPolicyScheduledPolicy.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BandwidthPolicyScheduledPolicy.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 launch_time: str,
                 end_time: Optional[str] = None,
                 recurrence_type: Optional[str] = None,
                 recurrence_value: Optional[str] = None,
                 start_time: Optional[str] = None):
        """
        :param str launch_time: Specifies the time when the scaling action is triggered.
               The time format complies with UTC.
               - If scaling_policy_type is set to SCHEDULED, the time format is YYYY-MM-DDThh:mmZ.
               - If scaling_policy_type is set to RECURRENCE, the time format is hh:mm.
        :param str end_time: Specifies the end time of the scaling action triggered periodically.
               The time format complies with UTC. This parameter is mandatory when scaling_policy_type is set to RECURRENCE.
               When the scaling action is triggered periodically, the end time cannot be earlier than the current and start time.
               The time format is YYYY-MM-DDThh:mmZ.
        :param str recurrence_type: Specifies the periodic triggering type.
               This parameter is mandatory when scaling_policy_type is set to RECURRENCE. The options are as follows:
               - **Daily**: indicates that the scaling action is triggered once a day.
               - **Weekly**: indicates that the scaling action is triggered once a week.
               - **Monthly**: indicates that the scaling action is triggered once a month.
        :param str recurrence_value: Specifies the day when a periodic scaling action is triggered.
               This parameter is mandatory when scaling_policy_type is set to RECURRENCE.
               - If recurrence_type is set to Daily, the value is null, indicating that the scaling action is triggered once a day.
               - If recurrence_type is set to Weekly, the value ranges from 1 (Sunday) to 7 (Saturday).
               The digits refer to dates in each week and separated by a comma, such as 1,3,5.
               - If recurrence_type is set to Monthly, the value ranges from 1 to 31.
               The digits refer to the dates in each month and separated by a comma, such as 1,10,13,28.
        :param str start_time: Specifies the start time of the scaling action triggered periodically.
               The time format complies with UTC. The default value is the local time.
               The time format is YYYY-MM-DDThh:mmZ.
        """
        pulumi.set(__self__, "launch_time", launch_time)
        if end_time is not None:
            pulumi.set(__self__, "end_time", end_time)
        if recurrence_type is not None:
            pulumi.set(__self__, "recurrence_type", recurrence_type)
        if recurrence_value is not None:
            pulumi.set(__self__, "recurrence_value", recurrence_value)
        if start_time is not None:
            pulumi.set(__self__, "start_time", start_time)

    @property
    @pulumi.getter(name="launchTime")
    def launch_time(self) -> str:
        """
        Specifies the time when the scaling action is triggered.
        The time format complies with UTC.
        - If scaling_policy_type is set to SCHEDULED, the time format is YYYY-MM-DDThh:mmZ.
        - If scaling_policy_type is set to RECURRENCE, the time format is hh:mm.
        """
        return pulumi.get(self, "launch_time")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[str]:
        """
        Specifies the end time of the scaling action triggered periodically.
        The time format complies with UTC. This parameter is mandatory when scaling_policy_type is set to RECURRENCE.
        When the scaling action is triggered periodically, the end time cannot be earlier than the current and start time.
        The time format is YYYY-MM-DDThh:mmZ.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="recurrenceType")
    def recurrence_type(self) -> Optional[str]:
        """
        Specifies the periodic triggering type.
        This parameter is mandatory when scaling_policy_type is set to RECURRENCE. The options are as follows:
        - **Daily**: indicates that the scaling action is triggered once a day.
        - **Weekly**: indicates that the scaling action is triggered once a week.
        - **Monthly**: indicates that the scaling action is triggered once a month.
        """
        return pulumi.get(self, "recurrence_type")

    @property
    @pulumi.getter(name="recurrenceValue")
    def recurrence_value(self) -> Optional[str]:
        """
        Specifies the day when a periodic scaling action is triggered.
        This parameter is mandatory when scaling_policy_type is set to RECURRENCE.
        - If recurrence_type is set to Daily, the value is null, indicating that the scaling action is triggered once a day.
        - If recurrence_type is set to Weekly, the value ranges from 1 (Sunday) to 7 (Saturday).
        The digits refer to dates in each week and separated by a comma, such as 1,3,5.
        - If recurrence_type is set to Monthly, the value ranges from 1 to 31.
        The digits refer to the dates in each month and separated by a comma, such as 1,10,13,28.
        """
        return pulumi.get(self, "recurrence_value")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[str]:
        """
        Specifies the start time of the scaling action triggered periodically.
        The time format complies with UTC. The default value is the local time.
        The time format is YYYY-MM-DDThh:mmZ.
        """
        return pulumi.get(self, "start_time")


@pulumi.output_type
class ConfigurationInstanceConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "keyName":
            suggest = "key_name"
        elif key == "instanceId":
            suggest = "instance_id"
        elif key == "publicIp":
            suggest = "public_ip"
        elif key == "userData":
            suggest = "user_data"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigurationInstanceConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigurationInstanceConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigurationInstanceConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 key_name: str,
                 disks: Optional[Sequence['outputs.ConfigurationInstanceConfigDisk']] = None,
                 flavor: Optional[str] = None,
                 image: Optional[str] = None,
                 instance_id: Optional[str] = None,
                 metadata: Optional[Mapping[str, str]] = None,
                 personalities: Optional[Sequence['outputs.ConfigurationInstanceConfigPersonality']] = None,
                 public_ip: Optional['outputs.ConfigurationInstanceConfigPublicIp'] = None,
                 user_data: Optional[str] = None):
        """
        :param str key_name: Specifies the name of the SSH key pair used to log in to the instance.
               Changing this will create a new resource.
        :param Sequence['ConfigurationInstanceConfigDiskArgs'] disks: Specifies the disk group information. System disks are mandatory and
               data disks are optional. The object structure is documented below.
               Changing this will create a new resource.
        :param str flavor: Specifies the ECS flavor name. A maximum of 10 flavors can be selected.
               Use a comma (,) to separate multiple flavor names. Changing this will create a new resource.
        :param str image: Specifies the ECS image ID. Changing this will create a new resource.
        :param str instance_id: Specifies the ECS instance ID when using its specification
               as the template to create AS configurations. In this case, `flavor`, `image`, and `disk` arguments do not take effect.
               If this argument is not specified, `flavor`, `image`, and `disk` arguments are mandatory.
               Changing this will create a new resource.
        :param Mapping[str, str] metadata: Specifies the key/value pairs to make available from within the instance.
               Changing this will create a new resource.
        :param Sequence['ConfigurationInstanceConfigPersonalityArgs'] personalities: Specifies the customize personality of an instance by defining one or
               more files and their contents. The object structure is documented below.
               Changing this will create a new resource.
        :param 'ConfigurationInstanceConfigPublicIpArgs' public_ip: Specifies the EIP of the ECS instance.
               The object structure is documented below.
               Changing this will create a new resource.
        :param str user_data: Specifies the user data to provide when launching the instance.
               The file content must be encoded with Base64. Changing this will create a new resource.
        """
        pulumi.set(__self__, "key_name", key_name)
        if disks is not None:
            pulumi.set(__self__, "disks", disks)
        if flavor is not None:
            pulumi.set(__self__, "flavor", flavor)
        if image is not None:
            pulumi.set(__self__, "image", image)
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if personalities is not None:
            pulumi.set(__self__, "personalities", personalities)
        if public_ip is not None:
            pulumi.set(__self__, "public_ip", public_ip)
        if user_data is not None:
            pulumi.set(__self__, "user_data", user_data)

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> str:
        """
        Specifies the name of the SSH key pair used to log in to the instance.
        Changing this will create a new resource.
        """
        return pulumi.get(self, "key_name")

    @property
    @pulumi.getter
    def disks(self) -> Optional[Sequence['outputs.ConfigurationInstanceConfigDisk']]:
        """
        Specifies the disk group information. System disks are mandatory and
        data disks are optional. The object structure is documented below.
        Changing this will create a new resource.
        """
        return pulumi.get(self, "disks")

    @property
    @pulumi.getter
    def flavor(self) -> Optional[str]:
        """
        Specifies the ECS flavor name. A maximum of 10 flavors can be selected.
        Use a comma (,) to separate multiple flavor names. Changing this will create a new resource.
        """
        return pulumi.get(self, "flavor")

    @property
    @pulumi.getter
    def image(self) -> Optional[str]:
        """
        Specifies the ECS image ID. Changing this will create a new resource.
        """
        return pulumi.get(self, "image")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[str]:
        """
        Specifies the ECS instance ID when using its specification
        as the template to create AS configurations. In this case, `flavor`, `image`, and `disk` arguments do not take effect.
        If this argument is not specified, `flavor`, `image`, and `disk` arguments are mandatory.
        Changing this will create a new resource.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, str]]:
        """
        Specifies the key/value pairs to make available from within the instance.
        Changing this will create a new resource.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def personalities(self) -> Optional[Sequence['outputs.ConfigurationInstanceConfigPersonality']]:
        """
        Specifies the customize personality of an instance by defining one or
        more files and their contents. The object structure is documented below.
        Changing this will create a new resource.
        """
        return pulumi.get(self, "personalities")

    @property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> Optional['outputs.ConfigurationInstanceConfigPublicIp']:
        """
        Specifies the EIP of the ECS instance.
        The object structure is documented below.
        Changing this will create a new resource.
        """
        return pulumi.get(self, "public_ip")

    @property
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[str]:
        """
        Specifies the user data to provide when launching the instance.
        The file content must be encoded with Base64. Changing this will create a new resource.
        """
        return pulumi.get(self, "user_data")


@pulumi.output_type
class ConfigurationInstanceConfigDisk(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "diskType":
            suggest = "disk_type"
        elif key == "volumeType":
            suggest = "volume_type"
        elif key == "kmsId":
            suggest = "kms_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigurationInstanceConfigDisk. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigurationInstanceConfigDisk.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigurationInstanceConfigDisk.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 disk_type: str,
                 size: int,
                 volume_type: str,
                 kms_id: Optional[str] = None):
        """
        :param str disk_type: Specifies whether the disk is a system disk or a data disk.
               Option **DATA** indicates a data disk, option **SYS** indicates a system disk.
               Changing this will create a new resource.
        :param int size: Specifies the bandwidth (Mbit/s). The value range for bandwidth billed by bandwidth
               is 1 to 2000 and that for bandwidth billed by traffic is 1 to 300.
               Changing this creates a new resource.
        :param str volume_type: Specifies the disk type. Changing this will create a new resource.
               Available options are:
               + `SAS`: high I/O disk type.
               + `SSD`: ultra-high I/O disk type.
               + `GPSSD`: general purpose SSD disk type.
        :param str kms_id: Specifies the encryption KMS ID of the **DATA** disk.
               Changing this will create a new resource.
        """
        pulumi.set(__self__, "disk_type", disk_type)
        pulumi.set(__self__, "size", size)
        pulumi.set(__self__, "volume_type", volume_type)
        if kms_id is not None:
            pulumi.set(__self__, "kms_id", kms_id)

    @property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> str:
        """
        Specifies whether the disk is a system disk or a data disk.
        Option **DATA** indicates a data disk, option **SYS** indicates a system disk.
        Changing this will create a new resource.
        """
        return pulumi.get(self, "disk_type")

    @property
    @pulumi.getter
    def size(self) -> int:
        """
        Specifies the bandwidth (Mbit/s). The value range for bandwidth billed by bandwidth
        is 1 to 2000 and that for bandwidth billed by traffic is 1 to 300.
        Changing this creates a new resource.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> str:
        """
        Specifies the disk type. Changing this will create a new resource.
        Available options are:
        + `SAS`: high I/O disk type.
        + `SSD`: ultra-high I/O disk type.
        + `GPSSD`: general purpose SSD disk type.
        """
        return pulumi.get(self, "volume_type")

    @property
    @pulumi.getter(name="kmsId")
    def kms_id(self) -> Optional[str]:
        """
        Specifies the encryption KMS ID of the **DATA** disk.
        Changing this will create a new resource.
        """
        return pulumi.get(self, "kms_id")


@pulumi.output_type
class ConfigurationInstanceConfigPersonality(dict):
    def __init__(__self__, *,
                 content: str,
                 path: str):
        """
        :param str path: Specifies the path of the injected file. Changing this creates a new resource.
        """
        pulumi.set(__self__, "content", content)
        pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter
    def content(self) -> str:
        return pulumi.get(self, "content")

    @property
    @pulumi.getter
    def path(self) -> str:
        """
        Specifies the path of the injected file. Changing this creates a new resource.
        """
        return pulumi.get(self, "path")


@pulumi.output_type
class ConfigurationInstanceConfigPublicIp(dict):
    def __init__(__self__, *,
                 eip: 'outputs.ConfigurationInstanceConfigPublicIpEip'):
        """
        :param 'ConfigurationInstanceConfigPublicIpEipArgs' eip: Specifies the EIP configuration that will be automatically assigned to the instance.
               The object structure is documented below. Changing this will create a new resource.
        """
        pulumi.set(__self__, "eip", eip)

    @property
    @pulumi.getter
    def eip(self) -> 'outputs.ConfigurationInstanceConfigPublicIpEip':
        """
        Specifies the EIP configuration that will be automatically assigned to the instance.
        The object structure is documented below. Changing this will create a new resource.
        """
        return pulumi.get(self, "eip")


@pulumi.output_type
class ConfigurationInstanceConfigPublicIpEip(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ipType":
            suggest = "ip_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigurationInstanceConfigPublicIpEip. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigurationInstanceConfigPublicIpEip.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigurationInstanceConfigPublicIpEip.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 bandwidth: 'outputs.ConfigurationInstanceConfigPublicIpEipBandwidth',
                 ip_type: str):
        """
        :param 'ConfigurationInstanceConfigPublicIpEipBandwidthArgs' bandwidth: Specifies the bandwidth information. The object structure is documented below.
               Changing this will create a new resource.
        :param str ip_type: Specifies the EIP type. Possible values are **5_bgp** (dynamic BGP)
               and **5_sbgp** (static BGP). Changing this will create a new resource.
        """
        pulumi.set(__self__, "bandwidth", bandwidth)
        pulumi.set(__self__, "ip_type", ip_type)

    @property
    @pulumi.getter
    def bandwidth(self) -> 'outputs.ConfigurationInstanceConfigPublicIpEipBandwidth':
        """
        Specifies the bandwidth information. The object structure is documented below.
        Changing this will create a new resource.
        """
        return pulumi.get(self, "bandwidth")

    @property
    @pulumi.getter(name="ipType")
    def ip_type(self) -> str:
        """
        Specifies the EIP type. Possible values are **5_bgp** (dynamic BGP)
        and **5_sbgp** (static BGP). Changing this will create a new resource.
        """
        return pulumi.get(self, "ip_type")


@pulumi.output_type
class ConfigurationInstanceConfigPublicIpEipBandwidth(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "chargingMode":
            suggest = "charging_mode"
        elif key == "shareType":
            suggest = "share_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigurationInstanceConfigPublicIpEipBandwidth. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigurationInstanceConfigPublicIpEipBandwidth.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigurationInstanceConfigPublicIpEipBandwidth.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 charging_mode: str,
                 share_type: str,
                 size: int):
        """
        :param str charging_mode: Specifies whether the bandwidth is billed by traffic or by bandwidth
               size. The value can be **traffic** or **bandwidth**. Changing this creates a new resource.
        :param str share_type: Specifies the bandwidth sharing type. The system only supports
               **PER** (indicates exclusive bandwidth). Changing this will create a new resource.
        :param int size: Specifies the bandwidth (Mbit/s). The value range for bandwidth billed by bandwidth
               is 1 to 2000 and that for bandwidth billed by traffic is 1 to 300.
               Changing this creates a new resource.
        """
        pulumi.set(__self__, "charging_mode", charging_mode)
        pulumi.set(__self__, "share_type", share_type)
        pulumi.set(__self__, "size", size)

    @property
    @pulumi.getter(name="chargingMode")
    def charging_mode(self) -> str:
        """
        Specifies whether the bandwidth is billed by traffic or by bandwidth
        size. The value can be **traffic** or **bandwidth**. Changing this creates a new resource.
        """
        return pulumi.get(self, "charging_mode")

    @property
    @pulumi.getter(name="shareType")
    def share_type(self) -> str:
        """
        Specifies the bandwidth sharing type. The system only supports
        **PER** (indicates exclusive bandwidth). Changing this will create a new resource.
        """
        return pulumi.get(self, "share_type")

    @property
    @pulumi.getter
    def size(self) -> int:
        """
        Specifies the bandwidth (Mbit/s). The value range for bandwidth billed by bandwidth
        is 1 to 2000 and that for bandwidth billed by traffic is 1 to 300.
        Changing this creates a new resource.
        """
        return pulumi.get(self, "size")


@pulumi.output_type
class GroupLbaasListener(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "poolId":
            suggest = "pool_id"
        elif key == "protocolPort":
            suggest = "protocol_port"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GroupLbaasListener. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GroupLbaasListener.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GroupLbaasListener.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 pool_id: str,
                 protocol_port: int,
                 weight: Optional[int] = None):
        """
        :param str pool_id: Specifies the backend ECS group ID.
        :param int protocol_port: Specifies the backend protocol, which is the port on which a backend ECS listens for
               traffic. The number of the port ranges from 1 to 65535.
        :param int weight: Specifies the weight, which determines the portion of requests a backend ECS processes
               compared to other backend ECSs added to the same listener. The value of this parameter ranges from 0 to 100. The
               default value is 1.
        """
        pulumi.set(__self__, "pool_id", pool_id)
        pulumi.set(__self__, "protocol_port", protocol_port)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter(name="poolId")
    def pool_id(self) -> str:
        """
        Specifies the backend ECS group ID.
        """
        return pulumi.get(self, "pool_id")

    @property
    @pulumi.getter(name="protocolPort")
    def protocol_port(self) -> int:
        """
        Specifies the backend protocol, which is the port on which a backend ECS listens for
        traffic. The number of the port ranges from 1 to 65535.
        """
        return pulumi.get(self, "protocol_port")

    @property
    @pulumi.getter
    def weight(self) -> Optional[int]:
        """
        Specifies the weight, which determines the portion of requests a backend ECS processes
        compared to other backend ECSs added to the same listener. The value of this parameter ranges from 0 to 100. The
        default value is 1.
        """
        return pulumi.get(self, "weight")


@pulumi.output_type
class GroupNetwork(dict):
    def __init__(__self__, *,
                 id: str):
        """
        :param str id: The UUID of the security group.
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The UUID of the security group.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class GroupSecurityGroup(dict):
    def __init__(__self__, *,
                 id: str):
        """
        :param str id: The UUID of the security group.
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The UUID of the security group.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class PolicyScalingPolicyAction(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "instanceNumber":
            suggest = "instance_number"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PolicyScalingPolicyAction. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PolicyScalingPolicyAction.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PolicyScalingPolicyAction.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 instance_number: Optional[int] = None,
                 operation: Optional[str] = None):
        """
        :param int instance_number: The number of instances to be operated. The default number is 1.
        :param str operation: The operation to be performed. The options include `ADD` (default), `REMOVE`,
               and `SET`.
        """
        if instance_number is not None:
            pulumi.set(__self__, "instance_number", instance_number)
        if operation is not None:
            pulumi.set(__self__, "operation", operation)

    @property
    @pulumi.getter(name="instanceNumber")
    def instance_number(self) -> Optional[int]:
        """
        The number of instances to be operated. The default number is 1.
        """
        return pulumi.get(self, "instance_number")

    @property
    @pulumi.getter
    def operation(self) -> Optional[str]:
        """
        The operation to be performed. The options include `ADD` (default), `REMOVE`,
        and `SET`.
        """
        return pulumi.get(self, "operation")


@pulumi.output_type
class PolicyScheduledPolicy(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "launchTime":
            suggest = "launch_time"
        elif key == "endTime":
            suggest = "end_time"
        elif key == "recurrenceType":
            suggest = "recurrence_type"
        elif key == "recurrenceValue":
            suggest = "recurrence_value"
        elif key == "startTime":
            suggest = "start_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PolicyScheduledPolicy. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PolicyScheduledPolicy.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PolicyScheduledPolicy.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 launch_time: str,
                 end_time: Optional[str] = None,
                 recurrence_type: Optional[str] = None,
                 recurrence_value: Optional[str] = None,
                 start_time: Optional[str] = None):
        """
        :param str launch_time: The time when the scaling action is triggered.
               + If `scaling_policy_type` is set to `SCHEDULED`, the time format is YYYY-MM-DDThh:mmZ.
               + If `scaling_policy_type` is set to `RECURRENCE`, the time format is hh:mm.
        :param str end_time: The end time of the scaling action triggered periodically. The time format complies
               with UTC. This argument is mandatory when `scaling_policy_type`
               is set to `RECURRENCE`. The time format is YYYY-MM-DDThh:mmZ.
        :param str recurrence_type: The periodic triggering type. This argument is mandatory when
               `scaling_policy_type` is set to `RECURRENCE`. The options include `Daily`, `Weekly`, and `Monthly`.
        :param str recurrence_value: The frequency at which scaling actions are triggered.
        :param str start_time: The start time of the scaling action triggered periodically. The time format
               complies with UTC. The current time is used by default. The time format is YYYY-MM-DDThh:mmZ.
        """
        pulumi.set(__self__, "launch_time", launch_time)
        if end_time is not None:
            pulumi.set(__self__, "end_time", end_time)
        if recurrence_type is not None:
            pulumi.set(__self__, "recurrence_type", recurrence_type)
        if recurrence_value is not None:
            pulumi.set(__self__, "recurrence_value", recurrence_value)
        if start_time is not None:
            pulumi.set(__self__, "start_time", start_time)

    @property
    @pulumi.getter(name="launchTime")
    def launch_time(self) -> str:
        """
        The time when the scaling action is triggered.
        + If `scaling_policy_type` is set to `SCHEDULED`, the time format is YYYY-MM-DDThh:mmZ.
        + If `scaling_policy_type` is set to `RECURRENCE`, the time format is hh:mm.
        """
        return pulumi.get(self, "launch_time")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[str]:
        """
        The end time of the scaling action triggered periodically. The time format complies
        with UTC. This argument is mandatory when `scaling_policy_type`
        is set to `RECURRENCE`. The time format is YYYY-MM-DDThh:mmZ.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="recurrenceType")
    def recurrence_type(self) -> Optional[str]:
        """
        The periodic triggering type. This argument is mandatory when
        `scaling_policy_type` is set to `RECURRENCE`. The options include `Daily`, `Weekly`, and `Monthly`.
        """
        return pulumi.get(self, "recurrence_type")

    @property
    @pulumi.getter(name="recurrenceValue")
    def recurrence_value(self) -> Optional[str]:
        """
        The frequency at which scaling actions are triggered.
        """
        return pulumi.get(self, "recurrence_value")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[str]:
        """
        The start time of the scaling action triggered periodically. The time format
        complies with UTC. The current time is used by default. The time format is YYYY-MM-DDThh:mmZ.
        """
        return pulumi.get(self, "start_time")

