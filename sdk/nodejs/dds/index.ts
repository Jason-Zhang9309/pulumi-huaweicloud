// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./databaseRole";
export * from "./databaseUser";
export * from "./getFlavors";
export * from "./instance";

// Import resources to register:
import { DatabaseRole } from "./databaseRole";
import { DatabaseUser } from "./databaseUser";
import { Instance } from "./instance";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "huaweicloud:Dds/databaseRole:DatabaseRole":
                return new DatabaseRole(name, <any>undefined, { urn })
            case "huaweicloud:Dds/databaseUser:DatabaseUser":
                return new DatabaseUser(name, <any>undefined, { urn })
            case "huaweicloud:Dds/instance:Instance":
                return new Instance(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("huaweicloud", "Dds/databaseRole", _module)
pulumi.runtime.registerResourceModule("huaweicloud", "Dds/databaseUser", _module)
pulumi.runtime.registerResourceModule("huaweicloud", "Dds/instance", _module)