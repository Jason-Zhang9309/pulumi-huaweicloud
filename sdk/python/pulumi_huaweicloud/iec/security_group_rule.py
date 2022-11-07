# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SecurityGroupRuleArgs', 'SecurityGroupRule']

@pulumi.input_type
class SecurityGroupRuleArgs:
    def __init__(__self__, *,
                 direction: pulumi.Input[str],
                 protocol: pulumi.Input[str],
                 security_group_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 ethertype: Optional[pulumi.Input[str]] = None,
                 port_range_max: Optional[pulumi.Input[int]] = None,
                 port_range_min: Optional[pulumi.Input[int]] = None,
                 remote_group_id: Optional[pulumi.Input[str]] = None,
                 remote_ip_prefix: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SecurityGroupRule resource.
        :param pulumi.Input[str] direction: Specifies the direction of the rule, valid values are **ingress** or
               **egress**. Changing this parameter creates a new security group rule resource.
        :param pulumi.Input[str] protocol: Specifies the layer 4 protocol type, valid values are following. The valid
               values are: **tcp**, **udp**, **icmp** and **gre**. Changing this parameter creates a new security group rule
               resource.
        :param pulumi.Input[str] security_group_id: Specifies the security group id the rule should belong to. Changing
               this parameter creates a new security group rule resource.
        :param pulumi.Input[str] description: Specifies a description of the security group rule. Changing this
               parameter creates a new security group rule resource.
        :param pulumi.Input[str] ethertype: Specifies the layer 3 protocol type, valid values are **IPv4**(IPv4 is
               default) or **IPv6**. Changing this parameter creates a new security group rule resource.
        :param pulumi.Input[int] port_range_max: Specifies the higher part of the allowed port range, valid integer value
               needs to be between 1 and 65535. Changing this parameter creates a new security group rule resource.
        :param pulumi.Input[int] port_range_min: Specifies the lower part of the allowed port range, valid integer value
               needs to be between 1 and 65535. Changing this parameter creates a new security group rule resource.
        :param pulumi.Input[str] remote_group_id: Specifies the remote group id, the value needs to be an ID of a
               security group. This parameter and remote_ip_prefix are alternative. Changing this parameter creates a new security
               group rule resource.
        :param pulumi.Input[str] remote_ip_prefix: Specifies the remote CIDR, the value to be a valid CIDR (i.e.
               192.168.0.0/16). This parameter and remote_group_id are alternative. Changing this parameter creates a new security
               group rule resource.
        """
        pulumi.set(__self__, "direction", direction)
        pulumi.set(__self__, "protocol", protocol)
        pulumi.set(__self__, "security_group_id", security_group_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if ethertype is not None:
            pulumi.set(__self__, "ethertype", ethertype)
        if port_range_max is not None:
            pulumi.set(__self__, "port_range_max", port_range_max)
        if port_range_min is not None:
            pulumi.set(__self__, "port_range_min", port_range_min)
        if remote_group_id is not None:
            pulumi.set(__self__, "remote_group_id", remote_group_id)
        if remote_ip_prefix is not None:
            pulumi.set(__self__, "remote_ip_prefix", remote_ip_prefix)

    @property
    @pulumi.getter
    def direction(self) -> pulumi.Input[str]:
        """
        Specifies the direction of the rule, valid values are **ingress** or
        **egress**. Changing this parameter creates a new security group rule resource.
        """
        return pulumi.get(self, "direction")

    @direction.setter
    def direction(self, value: pulumi.Input[str]):
        pulumi.set(self, "direction", value)

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[str]:
        """
        Specifies the layer 4 protocol type, valid values are following. The valid
        values are: **tcp**, **udp**, **icmp** and **gre**. Changing this parameter creates a new security group rule
        resource.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: pulumi.Input[str]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> pulumi.Input[str]:
        """
        Specifies the security group id the rule should belong to. Changing
        this parameter creates a new security group rule resource.
        """
        return pulumi.get(self, "security_group_id")

    @security_group_id.setter
    def security_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "security_group_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies a description of the security group rule. Changing this
        parameter creates a new security group rule resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def ethertype(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the layer 3 protocol type, valid values are **IPv4**(IPv4 is
        default) or **IPv6**. Changing this parameter creates a new security group rule resource.
        """
        return pulumi.get(self, "ethertype")

    @ethertype.setter
    def ethertype(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ethertype", value)

    @property
    @pulumi.getter(name="portRangeMax")
    def port_range_max(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the higher part of the allowed port range, valid integer value
        needs to be between 1 and 65535. Changing this parameter creates a new security group rule resource.
        """
        return pulumi.get(self, "port_range_max")

    @port_range_max.setter
    def port_range_max(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port_range_max", value)

    @property
    @pulumi.getter(name="portRangeMin")
    def port_range_min(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the lower part of the allowed port range, valid integer value
        needs to be between 1 and 65535. Changing this parameter creates a new security group rule resource.
        """
        return pulumi.get(self, "port_range_min")

    @port_range_min.setter
    def port_range_min(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port_range_min", value)

    @property
    @pulumi.getter(name="remoteGroupId")
    def remote_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the remote group id, the value needs to be an ID of a
        security group. This parameter and remote_ip_prefix are alternative. Changing this parameter creates a new security
        group rule resource.
        """
        return pulumi.get(self, "remote_group_id")

    @remote_group_id.setter
    def remote_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remote_group_id", value)

    @property
    @pulumi.getter(name="remoteIpPrefix")
    def remote_ip_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the remote CIDR, the value to be a valid CIDR (i.e.
        192.168.0.0/16). This parameter and remote_group_id are alternative. Changing this parameter creates a new security
        group rule resource.
        """
        return pulumi.get(self, "remote_ip_prefix")

    @remote_ip_prefix.setter
    def remote_ip_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remote_ip_prefix", value)


@pulumi.input_type
class _SecurityGroupRuleState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 direction: Optional[pulumi.Input[str]] = None,
                 ethertype: Optional[pulumi.Input[str]] = None,
                 port_range_max: Optional[pulumi.Input[int]] = None,
                 port_range_min: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 remote_group_id: Optional[pulumi.Input[str]] = None,
                 remote_ip_prefix: Optional[pulumi.Input[str]] = None,
                 security_group_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SecurityGroupRule resources.
        :param pulumi.Input[str] description: Specifies a description of the security group rule. Changing this
               parameter creates a new security group rule resource.
        :param pulumi.Input[str] direction: Specifies the direction of the rule, valid values are **ingress** or
               **egress**. Changing this parameter creates a new security group rule resource.
        :param pulumi.Input[str] ethertype: Specifies the layer 3 protocol type, valid values are **IPv4**(IPv4 is
               default) or **IPv6**. Changing this parameter creates a new security group rule resource.
        :param pulumi.Input[int] port_range_max: Specifies the higher part of the allowed port range, valid integer value
               needs to be between 1 and 65535. Changing this parameter creates a new security group rule resource.
        :param pulumi.Input[int] port_range_min: Specifies the lower part of the allowed port range, valid integer value
               needs to be between 1 and 65535. Changing this parameter creates a new security group rule resource.
        :param pulumi.Input[str] protocol: Specifies the layer 4 protocol type, valid values are following. The valid
               values are: **tcp**, **udp**, **icmp** and **gre**. Changing this parameter creates a new security group rule
               resource.
        :param pulumi.Input[str] remote_group_id: Specifies the remote group id, the value needs to be an ID of a
               security group. This parameter and remote_ip_prefix are alternative. Changing this parameter creates a new security
               group rule resource.
        :param pulumi.Input[str] remote_ip_prefix: Specifies the remote CIDR, the value to be a valid CIDR (i.e.
               192.168.0.0/16). This parameter and remote_group_id are alternative. Changing this parameter creates a new security
               group rule resource.
        :param pulumi.Input[str] security_group_id: Specifies the security group id the rule should belong to. Changing
               this parameter creates a new security group rule resource.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if direction is not None:
            pulumi.set(__self__, "direction", direction)
        if ethertype is not None:
            pulumi.set(__self__, "ethertype", ethertype)
        if port_range_max is not None:
            pulumi.set(__self__, "port_range_max", port_range_max)
        if port_range_min is not None:
            pulumi.set(__self__, "port_range_min", port_range_min)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if remote_group_id is not None:
            pulumi.set(__self__, "remote_group_id", remote_group_id)
        if remote_ip_prefix is not None:
            pulumi.set(__self__, "remote_ip_prefix", remote_ip_prefix)
        if security_group_id is not None:
            pulumi.set(__self__, "security_group_id", security_group_id)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies a description of the security group rule. Changing this
        parameter creates a new security group rule resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def direction(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the direction of the rule, valid values are **ingress** or
        **egress**. Changing this parameter creates a new security group rule resource.
        """
        return pulumi.get(self, "direction")

    @direction.setter
    def direction(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "direction", value)

    @property
    @pulumi.getter
    def ethertype(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the layer 3 protocol type, valid values are **IPv4**(IPv4 is
        default) or **IPv6**. Changing this parameter creates a new security group rule resource.
        """
        return pulumi.get(self, "ethertype")

    @ethertype.setter
    def ethertype(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ethertype", value)

    @property
    @pulumi.getter(name="portRangeMax")
    def port_range_max(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the higher part of the allowed port range, valid integer value
        needs to be between 1 and 65535. Changing this parameter creates a new security group rule resource.
        """
        return pulumi.get(self, "port_range_max")

    @port_range_max.setter
    def port_range_max(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port_range_max", value)

    @property
    @pulumi.getter(name="portRangeMin")
    def port_range_min(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the lower part of the allowed port range, valid integer value
        needs to be between 1 and 65535. Changing this parameter creates a new security group rule resource.
        """
        return pulumi.get(self, "port_range_min")

    @port_range_min.setter
    def port_range_min(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port_range_min", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the layer 4 protocol type, valid values are following. The valid
        values are: **tcp**, **udp**, **icmp** and **gre**. Changing this parameter creates a new security group rule
        resource.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter(name="remoteGroupId")
    def remote_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the remote group id, the value needs to be an ID of a
        security group. This parameter and remote_ip_prefix are alternative. Changing this parameter creates a new security
        group rule resource.
        """
        return pulumi.get(self, "remote_group_id")

    @remote_group_id.setter
    def remote_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remote_group_id", value)

    @property
    @pulumi.getter(name="remoteIpPrefix")
    def remote_ip_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the remote CIDR, the value to be a valid CIDR (i.e.
        192.168.0.0/16). This parameter and remote_group_id are alternative. Changing this parameter creates a new security
        group rule resource.
        """
        return pulumi.get(self, "remote_ip_prefix")

    @remote_ip_prefix.setter
    def remote_ip_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remote_ip_prefix", value)

    @property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the security group id the rule should belong to. Changing
        this parameter creates a new security group rule resource.
        """
        return pulumi.get(self, "security_group_id")

    @security_group_id.setter
    def security_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_group_id", value)


class SecurityGroupRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 direction: Optional[pulumi.Input[str]] = None,
                 ethertype: Optional[pulumi.Input[str]] = None,
                 port_range_max: Optional[pulumi.Input[int]] = None,
                 port_range_min: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 remote_group_id: Optional[pulumi.Input[str]] = None,
                 remote_ip_prefix: Optional[pulumi.Input[str]] = None,
                 security_group_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a IEC security group rule resource within HuaweiCloud.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_huaweicloud as huaweicloud

        secgroup_rule_test = huaweicloud.iec.SecurityGroupRule("secgroupRuleTest",
            direction="ingress",
            port_range_min=22,
            port_range_max=22,
            ethertype="IPv4",
            protocol="tcp",
            security_group_id=var["iec_security_group_id"],
            remote_ip_prefix="0.0.0.0/0")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Specifies a description of the security group rule. Changing this
               parameter creates a new security group rule resource.
        :param pulumi.Input[str] direction: Specifies the direction of the rule, valid values are **ingress** or
               **egress**. Changing this parameter creates a new security group rule resource.
        :param pulumi.Input[str] ethertype: Specifies the layer 3 protocol type, valid values are **IPv4**(IPv4 is
               default) or **IPv6**. Changing this parameter creates a new security group rule resource.
        :param pulumi.Input[int] port_range_max: Specifies the higher part of the allowed port range, valid integer value
               needs to be between 1 and 65535. Changing this parameter creates a new security group rule resource.
        :param pulumi.Input[int] port_range_min: Specifies the lower part of the allowed port range, valid integer value
               needs to be between 1 and 65535. Changing this parameter creates a new security group rule resource.
        :param pulumi.Input[str] protocol: Specifies the layer 4 protocol type, valid values are following. The valid
               values are: **tcp**, **udp**, **icmp** and **gre**. Changing this parameter creates a new security group rule
               resource.
        :param pulumi.Input[str] remote_group_id: Specifies the remote group id, the value needs to be an ID of a
               security group. This parameter and remote_ip_prefix are alternative. Changing this parameter creates a new security
               group rule resource.
        :param pulumi.Input[str] remote_ip_prefix: Specifies the remote CIDR, the value to be a valid CIDR (i.e.
               192.168.0.0/16). This parameter and remote_group_id are alternative. Changing this parameter creates a new security
               group rule resource.
        :param pulumi.Input[str] security_group_id: Specifies the security group id the rule should belong to. Changing
               this parameter creates a new security group rule resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecurityGroupRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a IEC security group rule resource within HuaweiCloud.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_huaweicloud as huaweicloud

        secgroup_rule_test = huaweicloud.iec.SecurityGroupRule("secgroupRuleTest",
            direction="ingress",
            port_range_min=22,
            port_range_max=22,
            ethertype="IPv4",
            protocol="tcp",
            security_group_id=var["iec_security_group_id"],
            remote_ip_prefix="0.0.0.0/0")
        ```

        :param str resource_name: The name of the resource.
        :param SecurityGroupRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecurityGroupRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 direction: Optional[pulumi.Input[str]] = None,
                 ethertype: Optional[pulumi.Input[str]] = None,
                 port_range_max: Optional[pulumi.Input[int]] = None,
                 port_range_min: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 remote_group_id: Optional[pulumi.Input[str]] = None,
                 remote_ip_prefix: Optional[pulumi.Input[str]] = None,
                 security_group_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SecurityGroupRuleArgs.__new__(SecurityGroupRuleArgs)

            __props__.__dict__["description"] = description
            if direction is None and not opts.urn:
                raise TypeError("Missing required property 'direction'")
            __props__.__dict__["direction"] = direction
            __props__.__dict__["ethertype"] = ethertype
            __props__.__dict__["port_range_max"] = port_range_max
            __props__.__dict__["port_range_min"] = port_range_min
            if protocol is None and not opts.urn:
                raise TypeError("Missing required property 'protocol'")
            __props__.__dict__["protocol"] = protocol
            __props__.__dict__["remote_group_id"] = remote_group_id
            __props__.__dict__["remote_ip_prefix"] = remote_ip_prefix
            if security_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'security_group_id'")
            __props__.__dict__["security_group_id"] = security_group_id
        super(SecurityGroupRule, __self__).__init__(
            'huaweicloud:Iec/securityGroupRule:SecurityGroupRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            direction: Optional[pulumi.Input[str]] = None,
            ethertype: Optional[pulumi.Input[str]] = None,
            port_range_max: Optional[pulumi.Input[int]] = None,
            port_range_min: Optional[pulumi.Input[int]] = None,
            protocol: Optional[pulumi.Input[str]] = None,
            remote_group_id: Optional[pulumi.Input[str]] = None,
            remote_ip_prefix: Optional[pulumi.Input[str]] = None,
            security_group_id: Optional[pulumi.Input[str]] = None) -> 'SecurityGroupRule':
        """
        Get an existing SecurityGroupRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Specifies a description of the security group rule. Changing this
               parameter creates a new security group rule resource.
        :param pulumi.Input[str] direction: Specifies the direction of the rule, valid values are **ingress** or
               **egress**. Changing this parameter creates a new security group rule resource.
        :param pulumi.Input[str] ethertype: Specifies the layer 3 protocol type, valid values are **IPv4**(IPv4 is
               default) or **IPv6**. Changing this parameter creates a new security group rule resource.
        :param pulumi.Input[int] port_range_max: Specifies the higher part of the allowed port range, valid integer value
               needs to be between 1 and 65535. Changing this parameter creates a new security group rule resource.
        :param pulumi.Input[int] port_range_min: Specifies the lower part of the allowed port range, valid integer value
               needs to be between 1 and 65535. Changing this parameter creates a new security group rule resource.
        :param pulumi.Input[str] protocol: Specifies the layer 4 protocol type, valid values are following. The valid
               values are: **tcp**, **udp**, **icmp** and **gre**. Changing this parameter creates a new security group rule
               resource.
        :param pulumi.Input[str] remote_group_id: Specifies the remote group id, the value needs to be an ID of a
               security group. This parameter and remote_ip_prefix are alternative. Changing this parameter creates a new security
               group rule resource.
        :param pulumi.Input[str] remote_ip_prefix: Specifies the remote CIDR, the value to be a valid CIDR (i.e.
               192.168.0.0/16). This parameter and remote_group_id are alternative. Changing this parameter creates a new security
               group rule resource.
        :param pulumi.Input[str] security_group_id: Specifies the security group id the rule should belong to. Changing
               this parameter creates a new security group rule resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SecurityGroupRuleState.__new__(_SecurityGroupRuleState)

        __props__.__dict__["description"] = description
        __props__.__dict__["direction"] = direction
        __props__.__dict__["ethertype"] = ethertype
        __props__.__dict__["port_range_max"] = port_range_max
        __props__.__dict__["port_range_min"] = port_range_min
        __props__.__dict__["protocol"] = protocol
        __props__.__dict__["remote_group_id"] = remote_group_id
        __props__.__dict__["remote_ip_prefix"] = remote_ip_prefix
        __props__.__dict__["security_group_id"] = security_group_id
        return SecurityGroupRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies a description of the security group rule. Changing this
        parameter creates a new security group rule resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def direction(self) -> pulumi.Output[str]:
        """
        Specifies the direction of the rule, valid values are **ingress** or
        **egress**. Changing this parameter creates a new security group rule resource.
        """
        return pulumi.get(self, "direction")

    @property
    @pulumi.getter
    def ethertype(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the layer 3 protocol type, valid values are **IPv4**(IPv4 is
        default) or **IPv6**. Changing this parameter creates a new security group rule resource.
        """
        return pulumi.get(self, "ethertype")

    @property
    @pulumi.getter(name="portRangeMax")
    def port_range_max(self) -> pulumi.Output[Optional[int]]:
        """
        Specifies the higher part of the allowed port range, valid integer value
        needs to be between 1 and 65535. Changing this parameter creates a new security group rule resource.
        """
        return pulumi.get(self, "port_range_max")

    @property
    @pulumi.getter(name="portRangeMin")
    def port_range_min(self) -> pulumi.Output[Optional[int]]:
        """
        Specifies the lower part of the allowed port range, valid integer value
        needs to be between 1 and 65535. Changing this parameter creates a new security group rule resource.
        """
        return pulumi.get(self, "port_range_min")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[str]:
        """
        Specifies the layer 4 protocol type, valid values are following. The valid
        values are: **tcp**, **udp**, **icmp** and **gre**. Changing this parameter creates a new security group rule
        resource.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="remoteGroupId")
    def remote_group_id(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the remote group id, the value needs to be an ID of a
        security group. This parameter and remote_ip_prefix are alternative. Changing this parameter creates a new security
        group rule resource.
        """
        return pulumi.get(self, "remote_group_id")

    @property
    @pulumi.getter(name="remoteIpPrefix")
    def remote_ip_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the remote CIDR, the value to be a valid CIDR (i.e.
        192.168.0.0/16). This parameter and remote_group_id are alternative. Changing this parameter creates a new security
        group rule resource.
        """
        return pulumi.get(self, "remote_ip_prefix")

    @property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> pulumi.Output[str]:
        """
        Specifies the security group id the rule should belong to. Changing
        this parameter creates a new security group rule resource.
        """
        return pulumi.get(self, "security_group_id")
