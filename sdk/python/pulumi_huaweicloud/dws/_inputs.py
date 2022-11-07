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
    'ClusterEndpointArgs',
    'ClusterPublicEndpointArgs',
    'ClusterPublicIpArgs',
]

@pulumi.input_type
class ClusterEndpointArgs:
    def __init__(__self__, *,
                 connect_info: Optional[pulumi.Input[str]] = None,
                 jdbc_url: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] connect_info: (Optional, String) Private network connection information.
        :param pulumi.Input[str] jdbc_url: (Optional, String)
               JDBC URL. The following is the default format:
               jdbc:postgresql://< public_connect_info>/<YOUR_DATABASE_NAME>
        """
        if connect_info is not None:
            pulumi.set(__self__, "connect_info", connect_info)
        if jdbc_url is not None:
            pulumi.set(__self__, "jdbc_url", jdbc_url)

    @property
    @pulumi.getter(name="connectInfo")
    def connect_info(self) -> Optional[pulumi.Input[str]]:
        """
        (Optional, String) Private network connection information.
        """
        return pulumi.get(self, "connect_info")

    @connect_info.setter
    def connect_info(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connect_info", value)

    @property
    @pulumi.getter(name="jdbcUrl")
    def jdbc_url(self) -> Optional[pulumi.Input[str]]:
        """
        (Optional, String)
        JDBC URL. The following is the default format:
        jdbc:postgresql://< public_connect_info>/<YOUR_DATABASE_NAME>
        """
        return pulumi.get(self, "jdbc_url")

    @jdbc_url.setter
    def jdbc_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "jdbc_url", value)


@pulumi.input_type
class ClusterPublicEndpointArgs:
    def __init__(__self__, *,
                 jdbc_url: Optional[pulumi.Input[str]] = None,
                 public_connect_info: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] jdbc_url: (Optional, String)
               JDBC URL. The following is the default format:
               jdbc:postgresql://< public_connect_info>/<YOUR_DATABASE_NAME>
        :param pulumi.Input[str] public_connect_info: (Optional, String)
               Public network connection information.
        """
        if jdbc_url is not None:
            pulumi.set(__self__, "jdbc_url", jdbc_url)
        if public_connect_info is not None:
            pulumi.set(__self__, "public_connect_info", public_connect_info)

    @property
    @pulumi.getter(name="jdbcUrl")
    def jdbc_url(self) -> Optional[pulumi.Input[str]]:
        """
        (Optional, String)
        JDBC URL. The following is the default format:
        jdbc:postgresql://< public_connect_info>/<YOUR_DATABASE_NAME>
        """
        return pulumi.get(self, "jdbc_url")

    @jdbc_url.setter
    def jdbc_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "jdbc_url", value)

    @property
    @pulumi.getter(name="publicConnectInfo")
    def public_connect_info(self) -> Optional[pulumi.Input[str]]:
        """
        (Optional, String)
        Public network connection information.
        """
        return pulumi.get(self, "public_connect_info")

    @public_connect_info.setter
    def public_connect_info(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_connect_info", value)


@pulumi.input_type
class ClusterPublicIpArgs:
    def __init__(__self__, *,
                 eip_id: Optional[pulumi.Input[str]] = None,
                 public_bind_type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] eip_id: EIP ID.
        :param pulumi.Input[str] public_bind_type: Binding type of an EIP. The value can be either of the following:
               auto_assign not_use bind_existing The default value is not_use.
        """
        if eip_id is not None:
            pulumi.set(__self__, "eip_id", eip_id)
        if public_bind_type is not None:
            pulumi.set(__self__, "public_bind_type", public_bind_type)

    @property
    @pulumi.getter(name="eipId")
    def eip_id(self) -> Optional[pulumi.Input[str]]:
        """
        EIP ID.
        """
        return pulumi.get(self, "eip_id")

    @eip_id.setter
    def eip_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "eip_id", value)

    @property
    @pulumi.getter(name="publicBindType")
    def public_bind_type(self) -> Optional[pulumi.Input[str]]:
        """
        Binding type of an EIP. The value can be either of the following:
        auto_assign not_use bind_existing The default value is not_use.
        """
        return pulumi.get(self, "public_bind_type")

    @public_bind_type.setter
    def public_bind_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_bind_type", value)

