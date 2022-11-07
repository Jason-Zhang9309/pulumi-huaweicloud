// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./dependency";
export * from "./function";
export * from "./getDependencies";
export * from "./trigger";

// Import resources to register:
import { Dependency } from "./dependency";
import { Function } from "./function";
import { Trigger } from "./trigger";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "huaweicloud:FunctionGraph/dependency:Dependency":
                return new Dependency(name, <any>undefined, { urn })
            case "huaweicloud:FunctionGraph/function:Function":
                return new Function(name, <any>undefined, { urn })
            case "huaweicloud:FunctionGraph/trigger:Trigger":
                return new Trigger(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("huaweicloud", "FunctionGraph/dependency", _module)
pulumi.runtime.registerResourceModule("huaweicloud", "FunctionGraph/function", _module)
pulumi.runtime.registerResourceModule("huaweicloud", "FunctionGraph/trigger", _module)