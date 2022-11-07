// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./ptrrecord";
export * from "./recordset";
export * from "./zone";

// Import resources to register:
import { Ptrrecord } from "./ptrrecord";
import { Recordset } from "./recordset";
import { Zone } from "./zone";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "huaweicloud:Dns/ptrrecord:Ptrrecord":
                return new Ptrrecord(name, <any>undefined, { urn })
            case "huaweicloud:Dns/recordset:Recordset":
                return new Recordset(name, <any>undefined, { urn })
            case "huaweicloud:Dns/zone:Zone":
                return new Zone(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("huaweicloud", "Dns/ptrrecord", _module)
pulumi.runtime.registerResourceModule("huaweicloud", "Dns/recordset", _module)
pulumi.runtime.registerResourceModule("huaweicloud", "Dns/zone", _module)