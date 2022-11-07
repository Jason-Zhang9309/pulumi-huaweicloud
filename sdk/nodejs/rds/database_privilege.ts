// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Manages RDS Mysql database privilege resource within HuaweiCloud.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as huaweicloud from "@pulumi/huaweicloud";
 *
 * const config = new pulumi.Config();
 * const instanceId = config.requireObject("instanceId");
 * const dbName = config.requireObject("dbName");
 * const userName1 = config.requireObject("userName1");
 * const userName2 = config.requireObject("userName2");
 * const test = new huaweicloud.rds.Database_privilege("test", {
 *     instanceId: instanceId,
 *     dbName: dbName,
 *     users: [
 *         {
 *             name: userName1,
 *             readonly: true,
 *         },
 *         {
 *             name: userName2,
 *             readonly: false,
 *         },
 *     ],
 * });
 * ```
 *
 * ## Import
 *
 * RDS database privilege can be imported using the `instance id` and `database name`, e.g.
 *
 * ```sh
 *  $ pulumi import huaweicloud:Rds/database_privilege:Database_privilege test instance_id/database_name
 * ```
 */
export class Database_privilege extends pulumi.CustomResource {
    /**
     * Get an existing Database_privilege resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: Database_privilegeState, opts?: pulumi.CustomResourceOptions): Database_privilege {
        return new Database_privilege(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'huaweicloud:Rds/database_privilege:Database_privilege';

    /**
     * Returns true if the given object is an instance of Database_privilege.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Database_privilege {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Database_privilege.__pulumiType;
    }

    /**
     * Specifies the database name. Changing this creates a new resource.
     */
    public readonly dbName!: pulumi.Output<string>;
    /**
     * Specifies the RDS instance ID. Changing this will create a new resource.
     */
    public readonly instanceId!: pulumi.Output<string>;
    /**
     * The region in which to create the RDS database privilege resource. If omitted,
     * the provider-level region will be used. Changing this creates a new resource.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * Specifies the account that associated with the database. This parameter supports
     * a maximum of 50 elements. Structure is documented below. Changing this creates a new resource.
     */
    public readonly users!: pulumi.Output<outputs.Rds.Database_privilegeUser[]>;

    /**
     * Create a Database_privilege resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: Database_privilegeArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: Database_privilegeArgs | Database_privilegeState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as Database_privilegeState | undefined;
            resourceInputs["dbName"] = state ? state.dbName : undefined;
            resourceInputs["instanceId"] = state ? state.instanceId : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["users"] = state ? state.users : undefined;
        } else {
            const args = argsOrState as Database_privilegeArgs | undefined;
            if ((!args || args.dbName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dbName'");
            }
            if ((!args || args.instanceId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceId'");
            }
            if ((!args || args.users === undefined) && !opts.urn) {
                throw new Error("Missing required property 'users'");
            }
            resourceInputs["dbName"] = args ? args.dbName : undefined;
            resourceInputs["instanceId"] = args ? args.instanceId : undefined;
            resourceInputs["region"] = args ? args.region : undefined;
            resourceInputs["users"] = args ? args.users : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Database_privilege.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Database_privilege resources.
 */
export interface Database_privilegeState {
    /**
     * Specifies the database name. Changing this creates a new resource.
     */
    dbName?: pulumi.Input<string>;
    /**
     * Specifies the RDS instance ID. Changing this will create a new resource.
     */
    instanceId?: pulumi.Input<string>;
    /**
     * The region in which to create the RDS database privilege resource. If omitted,
     * the provider-level region will be used. Changing this creates a new resource.
     */
    region?: pulumi.Input<string>;
    /**
     * Specifies the account that associated with the database. This parameter supports
     * a maximum of 50 elements. Structure is documented below. Changing this creates a new resource.
     */
    users?: pulumi.Input<pulumi.Input<inputs.Rds.Database_privilegeUser>[]>;
}

/**
 * The set of arguments for constructing a Database_privilege resource.
 */
export interface Database_privilegeArgs {
    /**
     * Specifies the database name. Changing this creates a new resource.
     */
    dbName: pulumi.Input<string>;
    /**
     * Specifies the RDS instance ID. Changing this will create a new resource.
     */
    instanceId: pulumi.Input<string>;
    /**
     * The region in which to create the RDS database privilege resource. If omitted,
     * the provider-level region will be used. Changing this creates a new resource.
     */
    region?: pulumi.Input<string>;
    /**
     * Specifies the account that associated with the database. This parameter supports
     * a maximum of 50 elements. Structure is documented below. Changing this creates a new resource.
     */
    users: pulumi.Input<pulumi.Input<inputs.Rds.Database_privilegeUser>[]>;
}