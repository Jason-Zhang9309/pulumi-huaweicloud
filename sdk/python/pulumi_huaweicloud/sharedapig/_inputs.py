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
    'ApiBackendParameterArgs',
    'ApiFunctionBackendArgs',
    'ApiHttpBackendArgs',
    'ApiMockBackendArgs',
    'ApiRequestParameterArgs',
]

@pulumi.input_type
class ApiBackendParameterArgs:
    def __init__(__self__, *,
                 location: pulumi.Input[str],
                 name: pulumi.Input[str],
                 value: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] location: Specifies the parameter location, which can be 'PATH', 'QUERY' or 'HEADER'.
        :param pulumi.Input[str] name: Specifies the parameter name. A parameter name consists of 1–32 characters, starting with
               a letter. Only letters, digits, periods (.), hyphens (-), and underscores (_) are allowed.
        :param pulumi.Input[str] value: Specifies the parameter value, which is a string of not more than 255 characters. The
               value varies depending on the parameter type:
               + 'REQUEST': parameter name in `request_parameter`
               + 'CONSTANT': real value of the parameter
               + 'SYSTEM': gateway parameter name
        :param pulumi.Input[str] description: Specifies the description of the parameter. The description cannot exceed 255
               characters.
        :param pulumi.Input[str] type: Specifies the parameter type, which can be 'REQUEST', 'CONSTANT', or 'SYSTEM'.
        """
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        Specifies the parameter location, which can be 'PATH', 'QUERY' or 'HEADER'.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Specifies the parameter name. A parameter name consists of 1–32 characters, starting with
        a letter. Only letters, digits, periods (.), hyphens (-), and underscores (_) are allowed.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        Specifies the parameter value, which is a string of not more than 255 characters. The
        value varies depending on the parameter type:
        + 'REQUEST': parameter name in `request_parameter`
        + 'CONSTANT': real value of the parameter
        + 'SYSTEM': gateway parameter name
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the description of the parameter. The description cannot exceed 255
        characters.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the parameter type, which can be 'REQUEST', 'CONSTANT', or 'SYSTEM'.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class ApiFunctionBackendArgs:
    def __init__(__self__, *,
                 function_urn: pulumi.Input[str],
                 invocation_type: pulumi.Input[str],
                 version: pulumi.Input[str],
                 timeout: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[str] function_urn: Specifies the function URN.
        :param pulumi.Input[str] invocation_type: Specifies the invocation mode, which can be 'async' or 'sync'.
        :param pulumi.Input[str] version: Specifies the function version.
        :param pulumi.Input[int] timeout: Timeout duration (in ms) for API Gateway to request for FunctionGraph. Defaults to 50000.
        """
        pulumi.set(__self__, "function_urn", function_urn)
        pulumi.set(__self__, "invocation_type", invocation_type)
        pulumi.set(__self__, "version", version)
        if timeout is not None:
            pulumi.set(__self__, "timeout", timeout)

    @property
    @pulumi.getter(name="functionUrn")
    def function_urn(self) -> pulumi.Input[str]:
        """
        Specifies the function URN.
        """
        return pulumi.get(self, "function_urn")

    @function_urn.setter
    def function_urn(self, value: pulumi.Input[str]):
        pulumi.set(self, "function_urn", value)

    @property
    @pulumi.getter(name="invocationType")
    def invocation_type(self) -> pulumi.Input[str]:
        """
        Specifies the invocation mode, which can be 'async' or 'sync'.
        """
        return pulumi.get(self, "invocation_type")

    @invocation_type.setter
    def invocation_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "invocation_type", value)

    @property
    @pulumi.getter
    def version(self) -> pulumi.Input[str]:
        """
        Specifies the function version.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: pulumi.Input[str]):
        pulumi.set(self, "version", value)

    @property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[int]]:
        """
        Timeout duration (in ms) for API Gateway to request for FunctionGraph. Defaults to 50000.
        """
        return pulumi.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout", value)


@pulumi.input_type
class ApiHttpBackendArgs:
    def __init__(__self__, *,
                 method: pulumi.Input[str],
                 protocol: pulumi.Input[str],
                 uri: pulumi.Input[str],
                 timeout: Optional[pulumi.Input[int]] = None,
                 url_domain: Optional[pulumi.Input[str]] = None,
                 vpc_channel: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] method: Specifies the backend request method, including 'GET','POST','PUT' and etc..
        :param pulumi.Input[str] protocol: Specifies the backend request protocol. The value can be 'HTTP' and 'HTTPS'.
        :param pulumi.Input[str] uri: Specifies the backend request path. The value must comply with URI specifications.
        :param pulumi.Input[int] timeout: Timeout duration (in ms) for API Gateway to request for the backend service. Defaults to
               50000.
        :param pulumi.Input[str] url_domain: Specifies the backend service address. An endpoint URL is in the format of
               "domain name (or IP address):port number", with up to 255 characters. This parameter and `vpc_channel` are
               alternative.
        :param pulumi.Input[str] vpc_channel: Specifies the VPC channel ID. This parameter and `url_domain` are alternative.
        """
        pulumi.set(__self__, "method", method)
        pulumi.set(__self__, "protocol", protocol)
        pulumi.set(__self__, "uri", uri)
        if timeout is not None:
            pulumi.set(__self__, "timeout", timeout)
        if url_domain is not None:
            pulumi.set(__self__, "url_domain", url_domain)
        if vpc_channel is not None:
            pulumi.set(__self__, "vpc_channel", vpc_channel)

    @property
    @pulumi.getter
    def method(self) -> pulumi.Input[str]:
        """
        Specifies the backend request method, including 'GET','POST','PUT' and etc..
        """
        return pulumi.get(self, "method")

    @method.setter
    def method(self, value: pulumi.Input[str]):
        pulumi.set(self, "method", value)

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[str]:
        """
        Specifies the backend request protocol. The value can be 'HTTP' and 'HTTPS'.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: pulumi.Input[str]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Input[str]:
        """
        Specifies the backend request path. The value must comply with URI specifications.
        """
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "uri", value)

    @property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[int]]:
        """
        Timeout duration (in ms) for API Gateway to request for the backend service. Defaults to
        50000.
        """
        return pulumi.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout", value)

    @property
    @pulumi.getter(name="urlDomain")
    def url_domain(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the backend service address. An endpoint URL is in the format of
        "domain name (or IP address):port number", with up to 255 characters. This parameter and `vpc_channel` are
        alternative.
        """
        return pulumi.get(self, "url_domain")

    @url_domain.setter
    def url_domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url_domain", value)

    @property
    @pulumi.getter(name="vpcChannel")
    def vpc_channel(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the VPC channel ID. This parameter and `url_domain` are alternative.
        """
        return pulumi.get(self, "vpc_channel")

    @vpc_channel.setter
    def vpc_channel(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_channel", value)


@pulumi.input_type
class ApiMockBackendArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 result_content: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] description: Specifies the description of the Mock backend. The description cannot exceed 255
               characters.
        :param pulumi.Input[str] result_content: Specifies the return result.
        :param pulumi.Input[str] version: Specifies the version of the Mock backend.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if result_content is not None:
            pulumi.set(__self__, "result_content", result_content)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the description of the Mock backend. The description cannot exceed 255
        characters.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="resultContent")
    def result_content(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the return result.
        """
        return pulumi.get(self, "result_content")

    @result_content.setter
    def result_content(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "result_content", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the version of the Mock backend.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


@pulumi.input_type
class ApiRequestParameterArgs:
    def __init__(__self__, *,
                 location: pulumi.Input[str],
                 name: pulumi.Input[str],
                 required: pulumi.Input[bool],
                 type: pulumi.Input[str],
                 default: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] location: Specifies the input parameter location, which can be 'PATH', 'QUERY' or 'HEADER'.
        :param pulumi.Input[str] name: Specifies the input parameter name. A parameter name consists of 1–32 characters, starting
               with a letter. Only letters, digits, periods (.), hyphens (-), and underscores (_) are allowed.
        :param pulumi.Input[bool] required: Specifies whether the parameter is mandatory or not.
        :param pulumi.Input[str] type: Specifies the input parameter type, which can be 'STRING' or 'NUMBER'.
        :param pulumi.Input[str] default: Specifies the default value when the parameter is optional.
        :param pulumi.Input[str] description: Specifies the description of the parameter. The description cannot exceed 255
               characters.
        """
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "required", required)
        pulumi.set(__self__, "type", type)
        if default is not None:
            pulumi.set(__self__, "default", default)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        Specifies the input parameter location, which can be 'PATH', 'QUERY' or 'HEADER'.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Specifies the input parameter name. A parameter name consists of 1–32 characters, starting
        with a letter. Only letters, digits, periods (.), hyphens (-), and underscores (_) are allowed.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def required(self) -> pulumi.Input[bool]:
        """
        Specifies whether the parameter is mandatory or not.
        """
        return pulumi.get(self, "required")

    @required.setter
    def required(self, value: pulumi.Input[bool]):
        pulumi.set(self, "required", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Specifies the input parameter type, which can be 'STRING' or 'NUMBER'.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def default(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the default value when the parameter is optional.
        """
        return pulumi.get(self, "default")

    @default.setter
    def default(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the description of the parameter. The description cannot exceed 255
        characters.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

