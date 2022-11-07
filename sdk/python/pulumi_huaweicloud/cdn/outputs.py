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
    'DomainCacheSettings',
    'DomainCacheSettingsRule',
    'DomainConfigs',
    'DomainConfigsCacheUrlParameterFilter',
    'DomainConfigsCompress',
    'DomainConfigsForceRedirect',
    'DomainConfigsHttpResponseHeader',
    'DomainConfigsHttpsSettings',
    'DomainConfigsRetrievalRequestHeader',
    'DomainConfigsUrlSigning',
    'DomainSource',
]

@pulumi.output_type
class DomainCacheSettings(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "followOrigin":
            suggest = "follow_origin"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DomainCacheSettings. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DomainCacheSettings.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DomainCacheSettings.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 follow_origin: Optional[bool] = None,
                 rules: Optional[Sequence['outputs.DomainCacheSettingsRule']] = None):
        """
        :param bool follow_origin: Specifies whether to enable origin cache control.
        :param Sequence['DomainCacheSettingsRuleArgs'] rules: Specifies the cache rules, which overwrite the previous rule configurations.
               Blank rules are reset to default rules. The object structure is documented below.
        """
        if follow_origin is not None:
            pulumi.set(__self__, "follow_origin", follow_origin)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)

    @property
    @pulumi.getter(name="followOrigin")
    def follow_origin(self) -> Optional[bool]:
        """
        Specifies whether to enable origin cache control.
        """
        return pulumi.get(self, "follow_origin")

    @property
    @pulumi.getter
    def rules(self) -> Optional[Sequence['outputs.DomainCacheSettingsRule']]:
        """
        Specifies the cache rules, which overwrite the previous rule configurations.
        Blank rules are reset to default rules. The object structure is documented below.
        """
        return pulumi.get(self, "rules")


@pulumi.output_type
class DomainCacheSettingsRule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ruleType":
            suggest = "rule_type"
        elif key == "ttlType":
            suggest = "ttl_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DomainCacheSettingsRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DomainCacheSettingsRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DomainCacheSettingsRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 rule_type: int,
                 content: Optional[str] = None,
                 priority: Optional[int] = None,
                 ttl: Optional[int] = None,
                 ttl_type: Optional[int] = None):
        """
        :param int rule_type: Specifies the rule type. Possible value are:
               **0**: All types of files are matched. It is the default value.
               **1**: Files are matched based on their suffixes.
               **2**: Files are matched based on their directories.
               **3**: Files are matched based on their full paths.
        :param str content: Specifies the content that matches `rule_type`. If `rule_type` is set to **0**,
               this parameter is empty. If `rule_type` is set to **1**, the value of this parameter is a list of file name
               extensions. A file name extension starts with a period (.). File name extensions are separated by semicolons (;),
               for example, .jpg;.zip;.exe. If `rule_type` is set to **2**, the value of this parameter is a list of directories.
               A directory starts with a slash (/). Directories are separated by semicolons (;), for example,
               /test/folder01;/test/folder02.
        :param int priority: Specifies the priority weight of this rule. The default value is 1.
               A larger value indicates a higher priority. The value ranges from 1 to 100. The weight values must be unique.
        :param int ttl: Specifies the cache age. The maximum cache age is 365 days.
        :param int ttl_type: Specifies the unit of the cache age. Possible values: **1** (second), **2** (minute),
               **3** (hour), and **4** (day).
        """
        pulumi.set(__self__, "rule_type", rule_type)
        if content is not None:
            pulumi.set(__self__, "content", content)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)
        if ttl_type is not None:
            pulumi.set(__self__, "ttl_type", ttl_type)

    @property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> int:
        """
        Specifies the rule type. Possible value are:
        **0**: All types of files are matched. It is the default value.
        **1**: Files are matched based on their suffixes.
        **2**: Files are matched based on their directories.
        **3**: Files are matched based on their full paths.
        """
        return pulumi.get(self, "rule_type")

    @property
    @pulumi.getter
    def content(self) -> Optional[str]:
        """
        Specifies the content that matches `rule_type`. If `rule_type` is set to **0**,
        this parameter is empty. If `rule_type` is set to **1**, the value of this parameter is a list of file name
        extensions. A file name extension starts with a period (.). File name extensions are separated by semicolons (;),
        for example, .jpg;.zip;.exe. If `rule_type` is set to **2**, the value of this parameter is a list of directories.
        A directory starts with a slash (/). Directories are separated by semicolons (;), for example,
        /test/folder01;/test/folder02.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter
    def priority(self) -> Optional[int]:
        """
        Specifies the priority weight of this rule. The default value is 1.
        A larger value indicates a higher priority. The value ranges from 1 to 100. The weight values must be unique.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def ttl(self) -> Optional[int]:
        """
        Specifies the cache age. The maximum cache age is 365 days.
        """
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter(name="ttlType")
    def ttl_type(self) -> Optional[int]:
        """
        Specifies the unit of the cache age. Possible values: **1** (second), **2** (minute),
        **3** (hour), and **4** (day).
        """
        return pulumi.get(self, "ttl_type")


@pulumi.output_type
class DomainConfigs(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "cacheUrlParameterFilter":
            suggest = "cache_url_parameter_filter"
        elif key == "forceRedirect":
            suggest = "force_redirect"
        elif key == "httpResponseHeaders":
            suggest = "http_response_headers"
        elif key == "httpsSettings":
            suggest = "https_settings"
        elif key == "ipv6Enable":
            suggest = "ipv6_enable"
        elif key == "originProtocol":
            suggest = "origin_protocol"
        elif key == "rangeBasedRetrievalEnabled":
            suggest = "range_based_retrieval_enabled"
        elif key == "retrievalRequestHeaders":
            suggest = "retrieval_request_headers"
        elif key == "urlSigning":
            suggest = "url_signing"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DomainConfigs. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DomainConfigs.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DomainConfigs.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cache_url_parameter_filter: Optional['outputs.DomainConfigsCacheUrlParameterFilter'] = None,
                 compress: Optional['outputs.DomainConfigsCompress'] = None,
                 force_redirect: Optional['outputs.DomainConfigsForceRedirect'] = None,
                 http_response_headers: Optional[Sequence['outputs.DomainConfigsHttpResponseHeader']] = None,
                 https_settings: Optional['outputs.DomainConfigsHttpsSettings'] = None,
                 ipv6_enable: Optional[bool] = None,
                 origin_protocol: Optional[str] = None,
                 range_based_retrieval_enabled: Optional[bool] = None,
                 retrieval_request_headers: Optional[Sequence['outputs.DomainConfigsRetrievalRequestHeader']] = None,
                 url_signing: Optional['outputs.DomainConfigsUrlSigning'] = None):
        """
        :param 'DomainConfigsCacheUrlParameterFilterArgs' cache_url_parameter_filter: Specifies the settings for caching URL parameters.
               The object structure is documented below.
        :param 'DomainConfigsCompressArgs' compress: Specifies the smart compression. The object structure
               is documented below.
        :param 'DomainConfigsForceRedirectArgs' force_redirect: Specifies the force redirect.
               The object structure is documented below.
        :param Sequence['DomainConfigsHttpResponseHeaderArgs'] http_response_headers: Specifies the HTTP response header settings.
               The object structure is documented below.
        :param 'DomainConfigsHttpsSettingsArgs' https_settings: Specifies the certificate configuration. The object
               structure is documented below.
        :param bool ipv6_enable: Specifies whether to enable IPv6.
        :param str origin_protocol: Specifies the content retrieval protocol. Possible values:
               + **follow**: same as user requests.
               + **http**: HTTP, which is the default value.
               + **https**: HTTPS.
        :param bool range_based_retrieval_enabled: Specifies whether to enable range-based retrieval.
        :param Sequence['DomainConfigsRetrievalRequestHeaderArgs'] retrieval_request_headers: Specifies the retrieval request header settings.
               The object structure is documented below.
        :param 'DomainConfigsUrlSigningArgs' url_signing: Specifies the URL signing.
               The object structure is documented below.
        """
        if cache_url_parameter_filter is not None:
            pulumi.set(__self__, "cache_url_parameter_filter", cache_url_parameter_filter)
        if compress is not None:
            pulumi.set(__self__, "compress", compress)
        if force_redirect is not None:
            pulumi.set(__self__, "force_redirect", force_redirect)
        if http_response_headers is not None:
            pulumi.set(__self__, "http_response_headers", http_response_headers)
        if https_settings is not None:
            pulumi.set(__self__, "https_settings", https_settings)
        if ipv6_enable is not None:
            pulumi.set(__self__, "ipv6_enable", ipv6_enable)
        if origin_protocol is not None:
            pulumi.set(__self__, "origin_protocol", origin_protocol)
        if range_based_retrieval_enabled is not None:
            pulumi.set(__self__, "range_based_retrieval_enabled", range_based_retrieval_enabled)
        if retrieval_request_headers is not None:
            pulumi.set(__self__, "retrieval_request_headers", retrieval_request_headers)
        if url_signing is not None:
            pulumi.set(__self__, "url_signing", url_signing)

    @property
    @pulumi.getter(name="cacheUrlParameterFilter")
    def cache_url_parameter_filter(self) -> Optional['outputs.DomainConfigsCacheUrlParameterFilter']:
        """
        Specifies the settings for caching URL parameters.
        The object structure is documented below.
        """
        return pulumi.get(self, "cache_url_parameter_filter")

    @property
    @pulumi.getter
    def compress(self) -> Optional['outputs.DomainConfigsCompress']:
        """
        Specifies the smart compression. The object structure
        is documented below.
        """
        return pulumi.get(self, "compress")

    @property
    @pulumi.getter(name="forceRedirect")
    def force_redirect(self) -> Optional['outputs.DomainConfigsForceRedirect']:
        """
        Specifies the force redirect.
        The object structure is documented below.
        """
        return pulumi.get(self, "force_redirect")

    @property
    @pulumi.getter(name="httpResponseHeaders")
    def http_response_headers(self) -> Optional[Sequence['outputs.DomainConfigsHttpResponseHeader']]:
        """
        Specifies the HTTP response header settings.
        The object structure is documented below.
        """
        return pulumi.get(self, "http_response_headers")

    @property
    @pulumi.getter(name="httpsSettings")
    def https_settings(self) -> Optional['outputs.DomainConfigsHttpsSettings']:
        """
        Specifies the certificate configuration. The object
        structure is documented below.
        """
        return pulumi.get(self, "https_settings")

    @property
    @pulumi.getter(name="ipv6Enable")
    def ipv6_enable(self) -> Optional[bool]:
        """
        Specifies whether to enable IPv6.
        """
        return pulumi.get(self, "ipv6_enable")

    @property
    @pulumi.getter(name="originProtocol")
    def origin_protocol(self) -> Optional[str]:
        """
        Specifies the content retrieval protocol. Possible values:
        + **follow**: same as user requests.
        + **http**: HTTP, which is the default value.
        + **https**: HTTPS.
        """
        return pulumi.get(self, "origin_protocol")

    @property
    @pulumi.getter(name="rangeBasedRetrievalEnabled")
    def range_based_retrieval_enabled(self) -> Optional[bool]:
        """
        Specifies whether to enable range-based retrieval.
        """
        return pulumi.get(self, "range_based_retrieval_enabled")

    @property
    @pulumi.getter(name="retrievalRequestHeaders")
    def retrieval_request_headers(self) -> Optional[Sequence['outputs.DomainConfigsRetrievalRequestHeader']]:
        """
        Specifies the retrieval request header settings.
        The object structure is documented below.
        """
        return pulumi.get(self, "retrieval_request_headers")

    @property
    @pulumi.getter(name="urlSigning")
    def url_signing(self) -> Optional['outputs.DomainConfigsUrlSigning']:
        """
        Specifies the URL signing.
        The object structure is documented below.
        """
        return pulumi.get(self, "url_signing")


@pulumi.output_type
class DomainConfigsCacheUrlParameterFilter(dict):
    def __init__(__self__, *,
                 type: Optional[str] = None,
                 value: Optional[str] = None):
        """
        :param str type: Specifies the operation type for caching URL parameters. Posiible values are:
               **full_url**: cache all parameters
               **ignore_url_params**: ignore all parameters
               **del_args**: ignore specific URL parameters
               **reserve_args**: reserve specified URL parameters
        :param str value: Specifies the parameter values. Multiple values are separated by semicolons (;).
        """
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        Specifies the operation type for caching URL parameters. Posiible values are:
        **full_url**: cache all parameters
        **ignore_url_params**: ignore all parameters
        **del_args**: ignore specific URL parameters
        **reserve_args**: reserve specified URL parameters
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        Specifies the parameter values. Multiple values are separated by semicolons (;).
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class DomainConfigsCompress(dict):
    def __init__(__self__, *,
                 enabled: bool,
                 status: Optional[str] = None,
                 type: Optional[str] = None):
        """
        :param bool enabled: Specifies the whether to enable force redirect or smart compression.
        :param str type: Specifies the operation type for caching URL parameters. Posiible values are:
               **full_url**: cache all parameters
               **ignore_url_params**: ignore all parameters
               **del_args**: ignore specific URL parameters
               **reserve_args**: reserve specified URL parameters
        """
        pulumi.set(__self__, "enabled", enabled)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        Specifies the whether to enable force redirect or smart compression.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        Specifies the operation type for caching URL parameters. Posiible values are:
        **full_url**: cache all parameters
        **ignore_url_params**: ignore all parameters
        **del_args**: ignore specific URL parameters
        **reserve_args**: reserve specified URL parameters
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class DomainConfigsForceRedirect(dict):
    def __init__(__self__, *,
                 enabled: bool,
                 status: Optional[str] = None,
                 type: Optional[str] = None):
        """
        :param bool enabled: Specifies the whether to enable force redirect or smart compression.
        :param str type: Specifies the operation type for caching URL parameters. Posiible values are:
               **full_url**: cache all parameters
               **ignore_url_params**: ignore all parameters
               **del_args**: ignore specific URL parameters
               **reserve_args**: reserve specified URL parameters
        """
        pulumi.set(__self__, "enabled", enabled)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        Specifies the whether to enable force redirect or smart compression.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        Specifies the operation type for caching URL parameters. Posiible values are:
        **full_url**: cache all parameters
        **ignore_url_params**: ignore all parameters
        **del_args**: ignore specific URL parameters
        **reserve_args**: reserve specified URL parameters
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class DomainConfigsHttpResponseHeader(dict):
    def __init__(__self__, *,
                 action: str,
                 name: str,
                 value: Optional[str] = None):
        """
        :param str action: Specifies the operation type of request or response
        :param str name: Specifies the request or response header.
        :param str value: Specifies the parameter values. Multiple values are separated by semicolons (;).
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "name", name)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def action(self) -> str:
        """
        Specifies the operation type of request or response
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Specifies the request or response header.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        Specifies the parameter values. Multiple values are separated by semicolons (;).
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class DomainConfigsHttpsSettings(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "certificateBody":
            suggest = "certificate_body"
        elif key == "certificateName":
            suggest = "certificate_name"
        elif key == "certificateSource":
            suggest = "certificate_source"
        elif key == "http2Enabled":
            suggest = "http2_enabled"
        elif key == "http2Status":
            suggest = "http2_status"
        elif key == "httpsEnabled":
            suggest = "https_enabled"
        elif key == "httpsStatus":
            suggest = "https_status"
        elif key == "privateKey":
            suggest = "private_key"
        elif key == "tlsVersion":
            suggest = "tls_version"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DomainConfigsHttpsSettings. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DomainConfigsHttpsSettings.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DomainConfigsHttpsSettings.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 certificate_body: Optional[str] = None,
                 certificate_name: Optional[str] = None,
                 certificate_source: Optional[int] = None,
                 http2_enabled: Optional[bool] = None,
                 http2_status: Optional[str] = None,
                 https_enabled: Optional[bool] = None,
                 https_status: Optional[str] = None,
                 private_key: Optional[str] = None,
                 tls_version: Optional[str] = None):
        """
        :param str certificate_body: Specifies the content of the certificate used by the HTTPS protocol.
               This parameter is mandatory when a certificate is configured. The value is in PEM format.
        :param str certificate_name: Specifies the certificate name. The value contains 3 to 32 characters.
               This parameter is mandatory when a certificate is configured.
        :param int certificate_source: Specifies the certificate type. Possible values are:
               + **1**: Huawei-managed certificate.
               + **0**: your own certificate.
        :param bool http2_enabled: Specifies whether HTTP/2 is used.
        :param bool https_enabled: Specifies whether to enable HTTPS.
        :param str private_key: Specifies the private key used by the HTTPS protocol. This parameter is mandatory
               when a certificate is configured. The value is in PEM format.
        :param str tls_version: Specifies the transport Layer Security (TLS). Currently, **TLSv1.0**,
               **TLSv1.1**, **TLSv1.2**, and **TLSv1.3** are supported. By default, all versions are enabled. You can enable
               a single version or consecutive versions. To enable multiple versions, use commas (,) to separate versions,
               for example, **TLSv1.1,TLSv1.2**.
        """
        if certificate_body is not None:
            pulumi.set(__self__, "certificate_body", certificate_body)
        if certificate_name is not None:
            pulumi.set(__self__, "certificate_name", certificate_name)
        if certificate_source is not None:
            pulumi.set(__self__, "certificate_source", certificate_source)
        if http2_enabled is not None:
            pulumi.set(__self__, "http2_enabled", http2_enabled)
        if http2_status is not None:
            pulumi.set(__self__, "http2_status", http2_status)
        if https_enabled is not None:
            pulumi.set(__self__, "https_enabled", https_enabled)
        if https_status is not None:
            pulumi.set(__self__, "https_status", https_status)
        if private_key is not None:
            pulumi.set(__self__, "private_key", private_key)
        if tls_version is not None:
            pulumi.set(__self__, "tls_version", tls_version)

    @property
    @pulumi.getter(name="certificateBody")
    def certificate_body(self) -> Optional[str]:
        """
        Specifies the content of the certificate used by the HTTPS protocol.
        This parameter is mandatory when a certificate is configured. The value is in PEM format.
        """
        return pulumi.get(self, "certificate_body")

    @property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> Optional[str]:
        """
        Specifies the certificate name. The value contains 3 to 32 characters.
        This parameter is mandatory when a certificate is configured.
        """
        return pulumi.get(self, "certificate_name")

    @property
    @pulumi.getter(name="certificateSource")
    def certificate_source(self) -> Optional[int]:
        """
        Specifies the certificate type. Possible values are:
        + **1**: Huawei-managed certificate.
        + **0**: your own certificate.
        """
        return pulumi.get(self, "certificate_source")

    @property
    @pulumi.getter(name="http2Enabled")
    def http2_enabled(self) -> Optional[bool]:
        """
        Specifies whether HTTP/2 is used.
        """
        return pulumi.get(self, "http2_enabled")

    @property
    @pulumi.getter(name="http2Status")
    def http2_status(self) -> Optional[str]:
        return pulumi.get(self, "http2_status")

    @property
    @pulumi.getter(name="httpsEnabled")
    def https_enabled(self) -> Optional[bool]:
        """
        Specifies whether to enable HTTPS.
        """
        return pulumi.get(self, "https_enabled")

    @property
    @pulumi.getter(name="httpsStatus")
    def https_status(self) -> Optional[str]:
        return pulumi.get(self, "https_status")

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[str]:
        """
        Specifies the private key used by the HTTPS protocol. This parameter is mandatory
        when a certificate is configured. The value is in PEM format.
        """
        return pulumi.get(self, "private_key")

    @property
    @pulumi.getter(name="tlsVersion")
    def tls_version(self) -> Optional[str]:
        """
        Specifies the transport Layer Security (TLS). Currently, **TLSv1.0**,
        **TLSv1.1**, **TLSv1.2**, and **TLSv1.3** are supported. By default, all versions are enabled. You can enable
        a single version or consecutive versions. To enable multiple versions, use commas (,) to separate versions,
        for example, **TLSv1.1,TLSv1.2**.
        """
        return pulumi.get(self, "tls_version")


@pulumi.output_type
class DomainConfigsRetrievalRequestHeader(dict):
    def __init__(__self__, *,
                 action: str,
                 name: str,
                 value: Optional[str] = None):
        """
        :param str action: Specifies the operation type of request or response
        :param str name: Specifies the request or response header.
        :param str value: Specifies the parameter values. Multiple values are separated by semicolons (;).
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "name", name)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def action(self) -> str:
        """
        Specifies the operation type of request or response
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Specifies the request or response header.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        Specifies the parameter values. Multiple values are separated by semicolons (;).
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class DomainConfigsUrlSigning(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "expireTime":
            suggest = "expire_time"
        elif key == "timeFormat":
            suggest = "time_format"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DomainConfigsUrlSigning. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DomainConfigsUrlSigning.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DomainConfigsUrlSigning.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enabled: bool,
                 expire_time: Optional[int] = None,
                 key: Optional[str] = None,
                 status: Optional[str] = None,
                 time_format: Optional[str] = None,
                 type: Optional[str] = None):
        """
        :param bool enabled: Specifies the whether to enable force redirect or smart compression.
        :param int expire_time: Specifies the expiration time. The value ranges from **0** to **31536000**,
               in seconds.
        :param str key: Specifies the authentication key contains 6 to 32 characters, including letters and digits.
        :param str time_format: Specifies the time format. Possible values are:
               **dec**: Decimal, can be used in Method A, Method B and Method C2.
               **hex**: Hexadecimal, can be used in Method C1 and Method C2.
        :param str type: Specifies the operation type for caching URL parameters. Posiible values are:
               **full_url**: cache all parameters
               **ignore_url_params**: ignore all parameters
               **del_args**: ignore specific URL parameters
               **reserve_args**: reserve specified URL parameters
        """
        pulumi.set(__self__, "enabled", enabled)
        if expire_time is not None:
            pulumi.set(__self__, "expire_time", expire_time)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if time_format is not None:
            pulumi.set(__self__, "time_format", time_format)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        Specifies the whether to enable force redirect or smart compression.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[int]:
        """
        Specifies the expiration time. The value ranges from **0** to **31536000**,
        in seconds.
        """
        return pulumi.get(self, "expire_time")

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        """
        Specifies the authentication key contains 6 to 32 characters, including letters and digits.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="timeFormat")
    def time_format(self) -> Optional[str]:
        """
        Specifies the time format. Possible values are:
        **dec**: Decimal, can be used in Method A, Method B and Method C2.
        **hex**: Hexadecimal, can be used in Method C1 and Method C2.
        """
        return pulumi.get(self, "time_format")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        Specifies the operation type for caching URL parameters. Posiible values are:
        **full_url**: cache all parameters
        **ignore_url_params**: ignore all parameters
        **del_args**: ignore specific URL parameters
        **reserve_args**: reserve specified URL parameters
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class DomainSource(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "originType":
            suggest = "origin_type"
        elif key == "httpPort":
            suggest = "http_port"
        elif key == "httpsPort":
            suggest = "https_port"
        elif key == "obsWebHostingEnabled":
            suggest = "obs_web_hosting_enabled"
        elif key == "retrievalHost":
            suggest = "retrieval_host"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DomainSource. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DomainSource.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DomainSource.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 origin: str,
                 origin_type: str,
                 active: Optional[int] = None,
                 http_port: Optional[int] = None,
                 https_port: Optional[int] = None,
                 obs_web_hosting_enabled: Optional[bool] = None,
                 retrieval_host: Optional[str] = None):
        """
        :param str origin: The domain name or IP address of the origin server.
        :param str origin_type: The origin server type. The valid values are 'ipaddr', 'domain', and 'obs_bucket'.
        :param int active: Whether an origin server is active or standby (1: active; 0: standby). The default value is
               1.
        :param int http_port: Specifies the HTTP port. Default value: **80**.
        :param int https_port: Specifies the HTTPS port. Default value: **443**.
        :param bool obs_web_hosting_enabled: Whether to enable static website hosting for the OBS bucket.
               This parameter is mandatory when the `origin_type` is **obs_bucket**.
        :param str retrieval_host: Specifies the retrieval host. The default value is the acceleration domain name.
        """
        pulumi.set(__self__, "origin", origin)
        pulumi.set(__self__, "origin_type", origin_type)
        if active is not None:
            pulumi.set(__self__, "active", active)
        if http_port is not None:
            pulumi.set(__self__, "http_port", http_port)
        if https_port is not None:
            pulumi.set(__self__, "https_port", https_port)
        if obs_web_hosting_enabled is not None:
            pulumi.set(__self__, "obs_web_hosting_enabled", obs_web_hosting_enabled)
        if retrieval_host is not None:
            pulumi.set(__self__, "retrieval_host", retrieval_host)

    @property
    @pulumi.getter
    def origin(self) -> str:
        """
        The domain name or IP address of the origin server.
        """
        return pulumi.get(self, "origin")

    @property
    @pulumi.getter(name="originType")
    def origin_type(self) -> str:
        """
        The origin server type. The valid values are 'ipaddr', 'domain', and 'obs_bucket'.
        """
        return pulumi.get(self, "origin_type")

    @property
    @pulumi.getter
    def active(self) -> Optional[int]:
        """
        Whether an origin server is active or standby (1: active; 0: standby). The default value is
        1.
        """
        return pulumi.get(self, "active")

    @property
    @pulumi.getter(name="httpPort")
    def http_port(self) -> Optional[int]:
        """
        Specifies the HTTP port. Default value: **80**.
        """
        return pulumi.get(self, "http_port")

    @property
    @pulumi.getter(name="httpsPort")
    def https_port(self) -> Optional[int]:
        """
        Specifies the HTTPS port. Default value: **443**.
        """
        return pulumi.get(self, "https_port")

    @property
    @pulumi.getter(name="obsWebHostingEnabled")
    def obs_web_hosting_enabled(self) -> Optional[bool]:
        """
        Whether to enable static website hosting for the OBS bucket.
        This parameter is mandatory when the `origin_type` is **obs_bucket**.
        """
        return pulumi.get(self, "obs_web_hosting_enabled")

    @property
    @pulumi.getter(name="retrievalHost")
    def retrieval_host(self) -> Optional[str]:
        """
        Specifies the retrieval host. The default value is the acceleration domain name.
        """
        return pulumi.get(self, "retrieval_host")

