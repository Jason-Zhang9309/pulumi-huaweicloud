// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./getVolumes";
export * from "./snapshot";
export * from "./volume";

// Import resources to register:
import { Snapshot } from "./snapshot";
import { Volume } from "./volume";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "huaweicloud:Evs/snapshot:Snapshot":
                return new Snapshot(name, <any>undefined, { urn })
            case "huaweicloud:Evs/volume:Volume":
                return new Volume(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("huaweicloud", "Evs/snapshot", _module)
pulumi.runtime.registerResourceModule("huaweicloud", "Evs/volume", _module)