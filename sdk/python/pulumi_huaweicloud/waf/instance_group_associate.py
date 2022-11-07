# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['InstanceGroupAssociateArgs', 'InstanceGroupAssociate']

@pulumi.input_type
class InstanceGroupAssociateArgs:
    def __init__(__self__, *,
                 group_id: pulumi.Input[str],
                 load_balancers: pulumi.Input[Sequence[pulumi.Input[str]]],
                 region: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a InstanceGroupAssociate resource.
        """
        pulumi.set(__self__, "group_id", group_id)
        pulumi.set(__self__, "load_balancers", load_balancers)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="loadBalancers")
    def load_balancers(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "load_balancers")

    @load_balancers.setter
    def load_balancers(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "load_balancers", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


@pulumi.input_type
class _InstanceGroupAssociateState:
    def __init__(__self__, *,
                 group_id: Optional[pulumi.Input[str]] = None,
                 load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering InstanceGroupAssociate resources.
        """
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if load_balancers is not None:
            pulumi.set(__self__, "load_balancers", load_balancers)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="loadBalancers")
    def load_balancers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "load_balancers")

    @load_balancers.setter
    def load_balancers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "load_balancers", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


class InstanceGroupAssociate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a InstanceGroupAssociate resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstanceGroupAssociateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a InstanceGroupAssociate resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param InstanceGroupAssociateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceGroupAssociateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InstanceGroupAssociateArgs.__new__(InstanceGroupAssociateArgs)

            if group_id is None and not opts.urn:
                raise TypeError("Missing required property 'group_id'")
            __props__.__dict__["group_id"] = group_id
            if load_balancers is None and not opts.urn:
                raise TypeError("Missing required property 'load_balancers'")
            __props__.__dict__["load_balancers"] = load_balancers
            __props__.__dict__["region"] = region
        super(InstanceGroupAssociate, __self__).__init__(
            'huaweicloud:Waf/instanceGroupAssociate:InstanceGroupAssociate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            group_id: Optional[pulumi.Input[str]] = None,
            load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            region: Optional[pulumi.Input[str]] = None) -> 'InstanceGroupAssociate':
        """
        Get an existing InstanceGroupAssociate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InstanceGroupAssociateState.__new__(_InstanceGroupAssociateState)

        __props__.__dict__["group_id"] = group_id
        __props__.__dict__["load_balancers"] = load_balancers
        __props__.__dict__["region"] = region
        return InstanceGroupAssociate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter(name="loadBalancers")
    def load_balancers(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "load_balancers")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        return pulumi.get(self, "region")
