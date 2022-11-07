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
    'GetNamespacesNamespaceResult',
    'GetNamespacesNamespaceNetworkResult',
    'GetNamespacesNamespaceNetworkVpcResult',
]

@pulumi.output_type
class GetNamespacesNamespaceResult(dict):
    def __init__(__self__, *,
                 auto_expend_enabled: bool,
                 container_network_enabled: bool,
                 created_at: str,
                 enterprise_project_id: str,
                 id: str,
                 name: str,
                 networks: Sequence['outputs.GetNamespacesNamespaceNetworkResult'],
                 rbac_enabled: bool,
                 recycling_interval: int,
                 status: str,
                 type: str,
                 warmup_pool_size: int):
        """
        :param bool auto_expend_enabled: Whether elastic scheduling is enabled.
        :param bool container_network_enabled: Whether container network is enabled.
        :param str created_at: The time when the namespace was created in UTC format, such as **2021-09-27T01:30:39Z**.
        :param str enterprise_project_id: Specifies the enterprise project ID in UUID format.
        :param str id: The VPC ID in UUID format.
        :param str name: Specifies th name of the specified CCI namespace.
               This parameter can contain a maximum of 63 characters, which may consist of lowercase letters, digits and hyphens,
               and must start and end with lowercase letters and digits.
        :param Sequence['GetNamespacesNamespaceNetworkArgs'] networks: The network information of the CCI namespace. The structure is documented below.
        :param bool rbac_enabled: Whether Role-based access control is enabled.
               After the RBAC permission is enabled, the user's use of resources under the namespace will be controlled by the RBAC
               permission.
        :param int recycling_interval: The IP address recycling interval in hour.
               The idle IP resources from the elastic expansion of the IP resource pool can be recycled within this time.
        :param str status: The CCI namespace status.
        :param str type: Specifies the CCI namespace type.
               The valid values are **general-computing** and **gpu-accelerated**.
        :param int warmup_pool_size: The size of IP pool to warm-up.
        """
        pulumi.set(__self__, "auto_expend_enabled", auto_expend_enabled)
        pulumi.set(__self__, "container_network_enabled", container_network_enabled)
        pulumi.set(__self__, "created_at", created_at)
        pulumi.set(__self__, "enterprise_project_id", enterprise_project_id)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "networks", networks)
        pulumi.set(__self__, "rbac_enabled", rbac_enabled)
        pulumi.set(__self__, "recycling_interval", recycling_interval)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "warmup_pool_size", warmup_pool_size)

    @property
    @pulumi.getter(name="autoExpendEnabled")
    def auto_expend_enabled(self) -> bool:
        """
        Whether elastic scheduling is enabled.
        """
        return pulumi.get(self, "auto_expend_enabled")

    @property
    @pulumi.getter(name="containerNetworkEnabled")
    def container_network_enabled(self) -> bool:
        """
        Whether container network is enabled.
        """
        return pulumi.get(self, "container_network_enabled")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The time when the namespace was created in UTC format, such as **2021-09-27T01:30:39Z**.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="enterpriseProjectId")
    def enterprise_project_id(self) -> str:
        """
        Specifies the enterprise project ID in UUID format.
        """
        return pulumi.get(self, "enterprise_project_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The VPC ID in UUID format.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Specifies th name of the specified CCI namespace.
        This parameter can contain a maximum of 63 characters, which may consist of lowercase letters, digits and hyphens,
        and must start and end with lowercase letters and digits.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def networks(self) -> Sequence['outputs.GetNamespacesNamespaceNetworkResult']:
        """
        The network information of the CCI namespace. The structure is documented below.
        """
        return pulumi.get(self, "networks")

    @property
    @pulumi.getter(name="rbacEnabled")
    def rbac_enabled(self) -> bool:
        """
        Whether Role-based access control is enabled.
        After the RBAC permission is enabled, the user's use of resources under the namespace will be controlled by the RBAC
        permission.
        """
        return pulumi.get(self, "rbac_enabled")

    @property
    @pulumi.getter(name="recyclingInterval")
    def recycling_interval(self) -> int:
        """
        The IP address recycling interval in hour.
        The idle IP resources from the elastic expansion of the IP resource pool can be recycled within this time.
        """
        return pulumi.get(self, "recycling_interval")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The CCI namespace status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Specifies the CCI namespace type.
        The valid values are **general-computing** and **gpu-accelerated**.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="warmupPoolSize")
    def warmup_pool_size(self) -> int:
        """
        The size of IP pool to warm-up.
        """
        return pulumi.get(self, "warmup_pool_size")


@pulumi.output_type
class GetNamespacesNamespaceNetworkResult(dict):
    def __init__(__self__, *,
                 name: str,
                 security_group_id: str,
                 vpcs: Sequence['outputs.GetNamespacesNamespaceNetworkVpcResult']):
        """
        :param str name: Specifies th name of the specified CCI namespace.
               This parameter can contain a maximum of 63 characters, which may consist of lowercase letters, digits and hyphens,
               and must start and end with lowercase letters and digits.
        :param str security_group_id: The default security group ID in UUID format.
        :param Sequence['GetNamespacesNamespaceNetworkVpcArgs'] vpcs: The network information of the VPC under the CCI network. The structure is documented below.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "security_group_id", security_group_id)
        pulumi.set(__self__, "vpcs", vpcs)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Specifies th name of the specified CCI namespace.
        This parameter can contain a maximum of 63 characters, which may consist of lowercase letters, digits and hyphens,
        and must start and end with lowercase letters and digits.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> str:
        """
        The default security group ID in UUID format.
        """
        return pulumi.get(self, "security_group_id")

    @property
    @pulumi.getter
    def vpcs(self) -> Sequence['outputs.GetNamespacesNamespaceNetworkVpcResult']:
        """
        The network information of the VPC under the CCI network. The structure is documented below.
        """
        return pulumi.get(self, "vpcs")


@pulumi.output_type
class GetNamespacesNamespaceNetworkVpcResult(dict):
    def __init__(__self__, *,
                 id: str,
                 network_id: str,
                 subnet_cidr: str,
                 subnet_id: str):
        """
        :param str id: The VPC ID in UUID format.
        :param str network_id: The network ID of the VPC subnet in UUID format.
        :param str subnet_cidr: The subnet CIDR block.
        :param str subnet_id: The VPC subnet ID in UUID format.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "network_id", network_id)
        pulumi.set(__self__, "subnet_cidr", subnet_cidr)
        pulumi.set(__self__, "subnet_id", subnet_id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The VPC ID in UUID format.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> str:
        """
        The network ID of the VPC subnet in UUID format.
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter(name="subnetCidr")
    def subnet_cidr(self) -> str:
        """
        The subnet CIDR block.
        """
        return pulumi.get(self, "subnet_cidr")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        The VPC subnet ID in UUID format.
        """
        return pulumi.get(self, "subnet_id")

