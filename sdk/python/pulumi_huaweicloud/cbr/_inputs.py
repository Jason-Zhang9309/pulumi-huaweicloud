# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'PolicyBackupCycleArgs',
    'PolicyLongTermRetentionArgs',
    'VaultResourceArgs',
    'GetVaultsVaultArgs',
    'GetVaultsVaultResourceArgs',
]

@pulumi.input_type
class PolicyBackupCycleArgs:
    def __init__(__self__, *,
                 execution_times: pulumi.Input[Sequence[pulumi.Input[str]]],
                 days: Optional[pulumi.Input[str]] = None,
                 interval: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] execution_times: Specifies the backup time. Automated backups will be triggered at the backup
               time. The current time is in the UTC format (HH:MM). The minutes in the list must be set to **00** and the hours
               cannot be repeated. In the replication policy, you are advised to set one time point for one day.
        :param pulumi.Input[str] days: Specifies the weekly backup day of backup schedule. It supports seven days a week (MO, TU,
               WE, TH, FR, SA, SU) and this parameter is separated by a comma (,) without spaces, between date and date during the
               configuration.
        :param pulumi.Input[int] interval: Specifies the interval (in days) of backup schedule. The value range is `1` to `30`. This
               parameter and `days` are alternative.
        """
        pulumi.set(__self__, "execution_times", execution_times)
        if days is not None:
            pulumi.set(__self__, "days", days)
        if interval is not None:
            pulumi.set(__self__, "interval", interval)

    @property
    @pulumi.getter(name="executionTimes")
    def execution_times(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Specifies the backup time. Automated backups will be triggered at the backup
        time. The current time is in the UTC format (HH:MM). The minutes in the list must be set to **00** and the hours
        cannot be repeated. In the replication policy, you are advised to set one time point for one day.
        """
        return pulumi.get(self, "execution_times")

    @execution_times.setter
    def execution_times(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "execution_times", value)

    @property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the weekly backup day of backup schedule. It supports seven days a week (MO, TU,
        WE, TH, FR, SA, SU) and this parameter is separated by a comma (,) without spaces, between date and date during the
        configuration.
        """
        return pulumi.get(self, "days")

    @days.setter
    def days(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "days", value)

    @property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the interval (in days) of backup schedule. The value range is `1` to `30`. This
        parameter and `days` are alternative.
        """
        return pulumi.get(self, "interval")

    @interval.setter
    def interval(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "interval", value)


@pulumi.input_type
class PolicyLongTermRetentionArgs:
    def __init__(__self__, *,
                 daily: Optional[pulumi.Input[int]] = None,
                 monthly: Optional[pulumi.Input[int]] = None,
                 weekly: Optional[pulumi.Input[int]] = None,
                 yearly: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[int] daily: - Specifies the latest backup of each day is saved in the long term.
        :param pulumi.Input[int] monthly: - Specifies the latest backup of each month is saved in the long term.
        :param pulumi.Input[int] weekly: - Specifies the latest backup of each week is saved in the long term.
        :param pulumi.Input[int] yearly: - Specifies the latest backup of each year is saved in the long term.
        """
        if daily is not None:
            pulumi.set(__self__, "daily", daily)
        if monthly is not None:
            pulumi.set(__self__, "monthly", monthly)
        if weekly is not None:
            pulumi.set(__self__, "weekly", weekly)
        if yearly is not None:
            pulumi.set(__self__, "yearly", yearly)

    @property
    @pulumi.getter
    def daily(self) -> Optional[pulumi.Input[int]]:
        """
        - Specifies the latest backup of each day is saved in the long term.
        """
        return pulumi.get(self, "daily")

    @daily.setter
    def daily(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "daily", value)

    @property
    @pulumi.getter
    def monthly(self) -> Optional[pulumi.Input[int]]:
        """
        - Specifies the latest backup of each month is saved in the long term.
        """
        return pulumi.get(self, "monthly")

    @monthly.setter
    def monthly(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "monthly", value)

    @property
    @pulumi.getter
    def weekly(self) -> Optional[pulumi.Input[int]]:
        """
        - Specifies the latest backup of each week is saved in the long term.
        """
        return pulumi.get(self, "weekly")

    @weekly.setter
    def weekly(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "weekly", value)

    @property
    @pulumi.getter
    def yearly(self) -> Optional[pulumi.Input[int]]:
        """
        - Specifies the latest backup of each year is saved in the long term.
        """
        return pulumi.get(self, "yearly")

    @yearly.setter
    def yearly(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "yearly", value)


@pulumi.input_type
class VaultResourceArgs:
    def __init__(__self__, *,
                 excludes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 includes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 server_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] excludes: Specifies the array of disk IDs which will be excluded in the backup.
               Only **server** vault support this parameter.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] includes: Specifies the array of disk or SFS file system IDs which will be included in the backup.
               Only **disk** and **turbo** vault support this parameter.
        :param pulumi.Input[str] server_id: Specifies the ID of the ECS instance to be backed up.
        """
        if excludes is not None:
            pulumi.set(__self__, "excludes", excludes)
        if includes is not None:
            pulumi.set(__self__, "includes", includes)
        if server_id is not None:
            pulumi.set(__self__, "server_id", server_id)

    @property
    @pulumi.getter
    def excludes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies the array of disk IDs which will be excluded in the backup.
        Only **server** vault support this parameter.
        """
        return pulumi.get(self, "excludes")

    @excludes.setter
    def excludes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "excludes", value)

    @property
    @pulumi.getter
    def includes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies the array of disk or SFS file system IDs which will be included in the backup.
        Only **disk** and **turbo** vault support this parameter.
        """
        return pulumi.get(self, "includes")

    @includes.setter
    def includes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "includes", value)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the ID of the ECS instance to be backed up.
        """
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_id", value)


@pulumi.input_type
class GetVaultsVaultArgs:
    def __init__(__self__, *,
                 allocated: float,
                 auto_expand_enabled: bool,
                 consistent_level: str,
                 enterprise_project_id: str,
                 id: str,
                 name: str,
                 policy_id: str,
                 protection_type: str,
                 resources: Sequence['GetVaultsVaultResourceArgs'],
                 size: int,
                 spec_code: str,
                 status: str,
                 storage: str,
                 tags: Mapping[str, str],
                 type: str,
                 used: float):
        """
        :param float allocated: The allocated capacity of the vault, in GB.
        :param bool auto_expand_enabled: Specifies whether to enable automatic expansion of the backup protection
               type vault. Default to **false**.
        :param str consistent_level: Specifies the backup specifications.
               The valid values are as follows:
               + **[crash_consistent](https://support.huaweicloud.com/intl/en-us/usermanual-cbr/cbr_03_0109.html)**
               + **[app_consistent](https://support.huaweicloud.com/intl/en-us/usermanual-cbr/cbr_03_0109.html)**
        :param str enterprise_project_id: Specifies a unique ID in UUID format of enterprise project.
        :param str id: The vault ID in UUID format.
        :param str name: Specifies a unique name of the CBR vault. This parameter can contain a maximum of 64
               characters, which may consist of letters, digits, underscores(_) and hyphens (-).
        :param str policy_id: Specifies a policy to associate with the CBR vault.
               The `policy_id` cannot be used with the vault of replicate protection type.
        :param str protection_type: Specifies the protection type of the CBR vault.
               The valid values are **backup** and **replication**. Vaults of type **disk** don't support **replication**.
        :param Sequence['GetVaultsVaultResourceArgs'] resources: An array of one or more resources to attach to the CBR vault.
               The object structure is documented below.
        :param int size: Specifies the vault sapacity, in GB. The valid value range is `1` to `10,485,760`.
        :param str spec_code: The specification code.
        :param str status: Specifies the CBR vault status, including **available**, **lock**, **frozen** and **error**.
        :param str storage: The name of the bucket for the vault.
        :param Mapping[str, str] tags: The key/value pairs to associate with the CBR vault.
        :param str type: Specifies the object type of the CBR vault. The vaild values are as follows:
               + **server** (Cloud Servers)
               + **disk** (EVS Disks)
               + **turbo** (SFS Turbo file systems)
        :param float used: The used capacity, in GB.
        """
        pulumi.set(__self__, "allocated", allocated)
        pulumi.set(__self__, "auto_expand_enabled", auto_expand_enabled)
        pulumi.set(__self__, "consistent_level", consistent_level)
        pulumi.set(__self__, "enterprise_project_id", enterprise_project_id)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "policy_id", policy_id)
        pulumi.set(__self__, "protection_type", protection_type)
        pulumi.set(__self__, "resources", resources)
        pulumi.set(__self__, "size", size)
        pulumi.set(__self__, "spec_code", spec_code)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "storage", storage)
        pulumi.set(__self__, "tags", tags)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "used", used)

    @property
    @pulumi.getter
    def allocated(self) -> float:
        """
        The allocated capacity of the vault, in GB.
        """
        return pulumi.get(self, "allocated")

    @allocated.setter
    def allocated(self, value: float):
        pulumi.set(self, "allocated", value)

    @property
    @pulumi.getter(name="autoExpandEnabled")
    def auto_expand_enabled(self) -> bool:
        """
        Specifies whether to enable automatic expansion of the backup protection
        type vault. Default to **false**.
        """
        return pulumi.get(self, "auto_expand_enabled")

    @auto_expand_enabled.setter
    def auto_expand_enabled(self, value: bool):
        pulumi.set(self, "auto_expand_enabled", value)

    @property
    @pulumi.getter(name="consistentLevel")
    def consistent_level(self) -> str:
        """
        Specifies the backup specifications.
        The valid values are as follows:
        + **[crash_consistent](https://support.huaweicloud.com/intl/en-us/usermanual-cbr/cbr_03_0109.html)**
        + **[app_consistent](https://support.huaweicloud.com/intl/en-us/usermanual-cbr/cbr_03_0109.html)**
        """
        return pulumi.get(self, "consistent_level")

    @consistent_level.setter
    def consistent_level(self, value: str):
        pulumi.set(self, "consistent_level", value)

    @property
    @pulumi.getter(name="enterpriseProjectId")
    def enterprise_project_id(self) -> str:
        """
        Specifies a unique ID in UUID format of enterprise project.
        """
        return pulumi.get(self, "enterprise_project_id")

    @enterprise_project_id.setter
    def enterprise_project_id(self, value: str):
        pulumi.set(self, "enterprise_project_id", value)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The vault ID in UUID format.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: str):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Specifies a unique name of the CBR vault. This parameter can contain a maximum of 64
        characters, which may consist of letters, digits, underscores(_) and hyphens (-).
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> str:
        """
        Specifies a policy to associate with the CBR vault.
        The `policy_id` cannot be used with the vault of replicate protection type.
        """
        return pulumi.get(self, "policy_id")

    @policy_id.setter
    def policy_id(self, value: str):
        pulumi.set(self, "policy_id", value)

    @property
    @pulumi.getter(name="protectionType")
    def protection_type(self) -> str:
        """
        Specifies the protection type of the CBR vault.
        The valid values are **backup** and **replication**. Vaults of type **disk** don't support **replication**.
        """
        return pulumi.get(self, "protection_type")

    @protection_type.setter
    def protection_type(self, value: str):
        pulumi.set(self, "protection_type", value)

    @property
    @pulumi.getter
    def resources(self) -> Sequence['GetVaultsVaultResourceArgs']:
        """
        An array of one or more resources to attach to the CBR vault.
        The object structure is documented below.
        """
        return pulumi.get(self, "resources")

    @resources.setter
    def resources(self, value: Sequence['GetVaultsVaultResourceArgs']):
        pulumi.set(self, "resources", value)

    @property
    @pulumi.getter
    def size(self) -> int:
        """
        Specifies the vault sapacity, in GB. The valid value range is `1` to `10,485,760`.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: int):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter(name="specCode")
    def spec_code(self) -> str:
        """
        The specification code.
        """
        return pulumi.get(self, "spec_code")

    @spec_code.setter
    def spec_code(self, value: str):
        pulumi.set(self, "spec_code", value)

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Specifies the CBR vault status, including **available**, **lock**, **frozen** and **error**.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: str):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def storage(self) -> str:
        """
        The name of the bucket for the vault.
        """
        return pulumi.get(self, "storage")

    @storage.setter
    def storage(self, value: str):
        pulumi.set(self, "storage", value)

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        The key/value pairs to associate with the CBR vault.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Mapping[str, str]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Specifies the object type of the CBR vault. The vaild values are as follows:
        + **server** (Cloud Servers)
        + **disk** (EVS Disks)
        + **turbo** (SFS Turbo file systems)
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: str):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def used(self) -> float:
        """
        The used capacity, in GB.
        """
        return pulumi.get(self, "used")

    @used.setter
    def used(self, value: float):
        pulumi.set(self, "used", value)


@pulumi.input_type
class GetVaultsVaultResourceArgs:
    def __init__(__self__, *,
                 excludes: Sequence[str],
                 includes: Sequence[str],
                 server_id: str):
        """
        :param Sequence[str] excludes: An array of disk IDs which will be excluded in the backup.
        :param Sequence[str] includes: An array of disk or SFS file system IDs which will be included in the backup.
        :param str server_id: The ID of the ECS instance to be backed up.
        """
        pulumi.set(__self__, "excludes", excludes)
        pulumi.set(__self__, "includes", includes)
        pulumi.set(__self__, "server_id", server_id)

    @property
    @pulumi.getter
    def excludes(self) -> Sequence[str]:
        """
        An array of disk IDs which will be excluded in the backup.
        """
        return pulumi.get(self, "excludes")

    @excludes.setter
    def excludes(self, value: Sequence[str]):
        pulumi.set(self, "excludes", value)

    @property
    @pulumi.getter
    def includes(self) -> Sequence[str]:
        """
        An array of disk or SFS file system IDs which will be included in the backup.
        """
        return pulumi.get(self, "includes")

    @includes.setter
    def includes(self, value: Sequence[str]):
        pulumi.set(self, "includes", value)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> str:
        """
        The ID of the ECS instance to be backed up.
        """
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: str):
        pulumi.set(self, "server_id", value)

