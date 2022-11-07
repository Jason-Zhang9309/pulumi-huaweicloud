# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['RecordCallbackArgs', 'RecordCallback']

@pulumi.input_type
class RecordCallbackArgs:
    def __init__(__self__, *,
                 domain_name: pulumi.Input[str],
                 types: pulumi.Input[Sequence[pulumi.Input[str]]],
                 url: pulumi.Input[str],
                 region: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RecordCallback resource.
        :param pulumi.Input[str] domain_name: Specifies the ingest domain name.
               Changing this parameter will create a new resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] types: Specifies the types of recording notifications. The options are as follows:
               + **RECORD_NEW_FILE_START**: Recording started.
               + **RECORD_FILE_COMPLETE**: Recording file generated.
               + **RECORD_OVER**: Recording completed.
               + **RECORD_FAILED**: Recording failed.
        :param pulumi.Input[str] url: Specifies the callback URL for sending recording notifications, which must start with
               `http://` or `https://`, and cannot contain message headers or parameters.
        :param pulumi.Input[str] region: Specifies the region in which to create the resource.
               If omitted, the provider-level region will be used. Changing this parameter will create a new resource.
        """
        pulumi.set(__self__, "domain_name", domain_name)
        pulumi.set(__self__, "types", types)
        pulumi.set(__self__, "url", url)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        Specifies the ingest domain name.
        Changing this parameter will create a new resource.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter
    def types(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Specifies the types of recording notifications. The options are as follows:
        + **RECORD_NEW_FILE_START**: Recording started.
        + **RECORD_FILE_COMPLETE**: Recording file generated.
        + **RECORD_OVER**: Recording completed.
        + **RECORD_FAILED**: Recording failed.
        """
        return pulumi.get(self, "types")

    @types.setter
    def types(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "types", value)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        Specifies the callback URL for sending recording notifications, which must start with
        `http://` or `https://`, and cannot contain message headers or parameters.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the region in which to create the resource.
        If omitted, the provider-level region will be used. Changing this parameter will create a new resource.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


@pulumi.input_type
class _RecordCallbackState:
    def __init__(__self__, *,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering RecordCallback resources.
        :param pulumi.Input[str] domain_name: Specifies the ingest domain name.
               Changing this parameter will create a new resource.
        :param pulumi.Input[str] region: Specifies the region in which to create the resource.
               If omitted, the provider-level region will be used. Changing this parameter will create a new resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] types: Specifies the types of recording notifications. The options are as follows:
               + **RECORD_NEW_FILE_START**: Recording started.
               + **RECORD_FILE_COMPLETE**: Recording file generated.
               + **RECORD_OVER**: Recording completed.
               + **RECORD_FAILED**: Recording failed.
        :param pulumi.Input[str] url: Specifies the callback URL for sending recording notifications, which must start with
               `http://` or `https://`, and cannot contain message headers or parameters.
        """
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if types is not None:
            pulumi.set(__self__, "types", types)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the ingest domain name.
        Changing this parameter will create a new resource.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the region in which to create the resource.
        If omitted, the provider-level region will be used. Changing this parameter will create a new resource.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies the types of recording notifications. The options are as follows:
        + **RECORD_NEW_FILE_START**: Recording started.
        + **RECORD_FILE_COMPLETE**: Recording file generated.
        + **RECORD_OVER**: Recording completed.
        + **RECORD_FAILED**: Recording failed.
        """
        return pulumi.get(self, "types")

    @types.setter
    def types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "types", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the callback URL for sending recording notifications, which must start with
        `http://` or `https://`, and cannot contain message headers or parameters.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class RecordCallback(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a callback configuration within HuaweiCloud Live.

        > Only one callback configuration can be created for an ingestion domain name.

        ## Example Usage
        ### Create a callback configuration for an ingest domain name

        ```python
        import pulumi
        import pulumi_huaweicloud as huaweicloud

        config = pulumi.Config()
        ingest_domain_name = config.require_object("ingestDomainName")
        ingest_domain = huaweicloud.live.Domain("ingestDomain", type="push")
        callback = huaweicloud.live.RecordCallback("callback",
            domain_name=ingest_domain_name,
            url="http://mycallback.com.cn/record_notify",
            types=["RECORD_NEW_FILE_START"])
        ```

        ## Import

        Callback configurations can be imported using the `id`, e.g.

        ```sh
         $ pulumi import huaweicloud:Live/recordCallback:RecordCallback test 55534eaa-533a-419d-9b40-ec427ea7195a
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_name: Specifies the ingest domain name.
               Changing this parameter will create a new resource.
        :param pulumi.Input[str] region: Specifies the region in which to create the resource.
               If omitted, the provider-level region will be used. Changing this parameter will create a new resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] types: Specifies the types of recording notifications. The options are as follows:
               + **RECORD_NEW_FILE_START**: Recording started.
               + **RECORD_FILE_COMPLETE**: Recording file generated.
               + **RECORD_OVER**: Recording completed.
               + **RECORD_FAILED**: Recording failed.
        :param pulumi.Input[str] url: Specifies the callback URL for sending recording notifications, which must start with
               `http://` or `https://`, and cannot contain message headers or parameters.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RecordCallbackArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a callback configuration within HuaweiCloud Live.

        > Only one callback configuration can be created for an ingestion domain name.

        ## Example Usage
        ### Create a callback configuration for an ingest domain name

        ```python
        import pulumi
        import pulumi_huaweicloud as huaweicloud

        config = pulumi.Config()
        ingest_domain_name = config.require_object("ingestDomainName")
        ingest_domain = huaweicloud.live.Domain("ingestDomain", type="push")
        callback = huaweicloud.live.RecordCallback("callback",
            domain_name=ingest_domain_name,
            url="http://mycallback.com.cn/record_notify",
            types=["RECORD_NEW_FILE_START"])
        ```

        ## Import

        Callback configurations can be imported using the `id`, e.g.

        ```sh
         $ pulumi import huaweicloud:Live/recordCallback:RecordCallback test 55534eaa-533a-419d-9b40-ec427ea7195a
        ```

        :param str resource_name: The name of the resource.
        :param RecordCallbackArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RecordCallbackArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RecordCallbackArgs.__new__(RecordCallbackArgs)

            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            __props__.__dict__["region"] = region
            if types is None and not opts.urn:
                raise TypeError("Missing required property 'types'")
            __props__.__dict__["types"] = types
            if url is None and not opts.urn:
                raise TypeError("Missing required property 'url'")
            __props__.__dict__["url"] = url
        super(RecordCallback, __self__).__init__(
            'huaweicloud:Live/recordCallback:RecordCallback',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            domain_name: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'RecordCallback':
        """
        Get an existing RecordCallback resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_name: Specifies the ingest domain name.
               Changing this parameter will create a new resource.
        :param pulumi.Input[str] region: Specifies the region in which to create the resource.
               If omitted, the provider-level region will be used. Changing this parameter will create a new resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] types: Specifies the types of recording notifications. The options are as follows:
               + **RECORD_NEW_FILE_START**: Recording started.
               + **RECORD_FILE_COMPLETE**: Recording file generated.
               + **RECORD_OVER**: Recording completed.
               + **RECORD_FAILED**: Recording failed.
        :param pulumi.Input[str] url: Specifies the callback URL for sending recording notifications, which must start with
               `http://` or `https://`, and cannot contain message headers or parameters.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RecordCallbackState.__new__(_RecordCallbackState)

        __props__.__dict__["domain_name"] = domain_name
        __props__.__dict__["region"] = region
        __props__.__dict__["types"] = types
        __props__.__dict__["url"] = url
        return RecordCallback(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        Specifies the ingest domain name.
        Changing this parameter will create a new resource.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        Specifies the region in which to create the resource.
        If omitted, the provider-level region will be used. Changing this parameter will create a new resource.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def types(self) -> pulumi.Output[Sequence[str]]:
        """
        Specifies the types of recording notifications. The options are as follows:
        + **RECORD_NEW_FILE_START**: Recording started.
        + **RECORD_FILE_COMPLETE**: Recording file generated.
        + **RECORD_OVER**: Recording completed.
        + **RECORD_FAILED**: Recording failed.
        """
        return pulumi.get(self, "types")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        Specifies the callback URL for sending recording notifications, which must start with
        `http://` or `https://`, and cannot contain message headers or parameters.
        """
        return pulumi.get(self, "url")
