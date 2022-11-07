// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Manages a database user resource within HuaweiCloud.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as huaweicloud from "@pulumi/huaweicloud";
 *
 * const config = new pulumi.Config();
 * const instanceId = config.requireObject("instanceId");
 * const userName = config.requireObject("userName");
 * const userPassword = config.requireObject("userPassword");
 * const ownedRoleName = config.requireObject("ownedRoleName");
 * const ownedRoleDbName = config.requireObject("ownedRoleDbName");
 * const test = new huaweicloud.dds.DatabaseUser("test", {
 *     instanceId: instanceId,
 *     password: userPassword,
 *     dbName: _var.db_name,
 *     roles: [{
 *         name: ownedRoleName,
 *         dbName: ownedRoleDbName,
 *     }],
 * });
 * ```
 *
 * ## Import
 *
 * Database users can be imported using their `id` (combination of `instance_id`, `db_name` and `name`), separated by a slash (/), e.g.
 *
 * ```sh
 *  $ pulumi import huaweicloud:Dds/databaseUser:DatabaseUser test &ltinstance_id&gt/&ltdb_name&gt/&ltname&gt
 * ```
 *
 *  Due to security reason, the imported state may not be identical to your resource definition (`password` parameter). It is generally recommended running `terraform plan` after importing a user resource. You can then decide if changes should be applied to the user, or the resource definition should be updated to align with the user. Also you can ignore changes as below. resource "huaweicloud_dds_database_user" "test" {
 *
 *  ...
 *
 *  lifecycle {
 *
 *  ignore_changes = [
 *
 *  password,
 *
 *  ]
 *
 *  } }
 */
export class DatabaseUser extends pulumi.CustomResource {
    /**
     * Get an existing DatabaseUser resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatabaseUserState, opts?: pulumi.CustomResourceOptions): DatabaseUser {
        return new DatabaseUser(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'huaweicloud:Dds/databaseUser:DatabaseUser';

    /**
     * Returns true if the given object is an instance of DatabaseUser.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DatabaseUser {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DatabaseUser.__pulumiType;
    }

    /**
     * Specifies the database name to which this owned role belongs.
     * Changing this parameter will create a new user.
     */
    public readonly dbName!: pulumi.Output<string>;
    /**
     * The list of database privileges owned by the current user, includes all privileges
     * inherited by owned roles. The object structure is documented below.
     */
    public /*out*/ readonly inheritedPrivileges!: pulumi.Output<outputs.Dds.DatabaseUserInheritedPrivilege[]>;
    /**
     * Specifies the DDS instance ID to which the user belongs.
     * Changing this parameter will create a new user.
     */
    public readonly instanceId!: pulumi.Output<string>;
    /**
     * Specifies the name of role owned by the current user.
     * The name can contain `1` to `64` characters, only letters, digits, underscores (_), hyphens (-) and dots (.) are
     * allowed. Changing this parameter will create a new user.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Specifies the user password.
     * The assword content must meet the following conditions:
     */
    public readonly password!: pulumi.Output<string>;
    /**
     * The list of database privileges owned by the current user.
     * The object structure is documented below.
     */
    public /*out*/ readonly privileges!: pulumi.Output<outputs.Dds.DatabaseUserPrivilege[]>;
    /**
     * Specifies the region where the DDS instance is located.
     * Changing this parameter will create a new user.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * Specifies the list of roles owned by the current user.
     * The object structure is documented below. Changing this parameter will create a new user.
     */
    public readonly roles!: pulumi.Output<outputs.Dds.DatabaseUserRole[]>;

    /**
     * Create a DatabaseUser resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DatabaseUserArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DatabaseUserArgs | DatabaseUserState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as DatabaseUserState | undefined;
            resourceInputs["dbName"] = state ? state.dbName : undefined;
            resourceInputs["inheritedPrivileges"] = state ? state.inheritedPrivileges : undefined;
            resourceInputs["instanceId"] = state ? state.instanceId : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["password"] = state ? state.password : undefined;
            resourceInputs["privileges"] = state ? state.privileges : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["roles"] = state ? state.roles : undefined;
        } else {
            const args = argsOrState as DatabaseUserArgs | undefined;
            if ((!args || args.dbName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dbName'");
            }
            if ((!args || args.instanceId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceId'");
            }
            if ((!args || args.password === undefined) && !opts.urn) {
                throw new Error("Missing required property 'password'");
            }
            if ((!args || args.roles === undefined) && !opts.urn) {
                throw new Error("Missing required property 'roles'");
            }
            resourceInputs["dbName"] = args ? args.dbName : undefined;
            resourceInputs["instanceId"] = args ? args.instanceId : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["password"] = args ? args.password : undefined;
            resourceInputs["region"] = args ? args.region : undefined;
            resourceInputs["roles"] = args ? args.roles : undefined;
            resourceInputs["inheritedPrivileges"] = undefined /*out*/;
            resourceInputs["privileges"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(DatabaseUser.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DatabaseUser resources.
 */
export interface DatabaseUserState {
    /**
     * Specifies the database name to which this owned role belongs.
     * Changing this parameter will create a new user.
     */
    dbName?: pulumi.Input<string>;
    /**
     * The list of database privileges owned by the current user, includes all privileges
     * inherited by owned roles. The object structure is documented below.
     */
    inheritedPrivileges?: pulumi.Input<pulumi.Input<inputs.Dds.DatabaseUserInheritedPrivilege>[]>;
    /**
     * Specifies the DDS instance ID to which the user belongs.
     * Changing this parameter will create a new user.
     */
    instanceId?: pulumi.Input<string>;
    /**
     * Specifies the name of role owned by the current user.
     * The name can contain `1` to `64` characters, only letters, digits, underscores (_), hyphens (-) and dots (.) are
     * allowed. Changing this parameter will create a new user.
     */
    name?: pulumi.Input<string>;
    /**
     * Specifies the user password.
     * The assword content must meet the following conditions:
     */
    password?: pulumi.Input<string>;
    /**
     * The list of database privileges owned by the current user.
     * The object structure is documented below.
     */
    privileges?: pulumi.Input<pulumi.Input<inputs.Dds.DatabaseUserPrivilege>[]>;
    /**
     * Specifies the region where the DDS instance is located.
     * Changing this parameter will create a new user.
     */
    region?: pulumi.Input<string>;
    /**
     * Specifies the list of roles owned by the current user.
     * The object structure is documented below. Changing this parameter will create a new user.
     */
    roles?: pulumi.Input<pulumi.Input<inputs.Dds.DatabaseUserRole>[]>;
}

/**
 * The set of arguments for constructing a DatabaseUser resource.
 */
export interface DatabaseUserArgs {
    /**
     * Specifies the database name to which this owned role belongs.
     * Changing this parameter will create a new user.
     */
    dbName: pulumi.Input<string>;
    /**
     * Specifies the DDS instance ID to which the user belongs.
     * Changing this parameter will create a new user.
     */
    instanceId: pulumi.Input<string>;
    /**
     * Specifies the name of role owned by the current user.
     * The name can contain `1` to `64` characters, only letters, digits, underscores (_), hyphens (-) and dots (.) are
     * allowed. Changing this parameter will create a new user.
     */
    name?: pulumi.Input<string>;
    /**
     * Specifies the user password.
     * The assword content must meet the following conditions:
     */
    password: pulumi.Input<string>;
    /**
     * Specifies the region where the DDS instance is located.
     * Changing this parameter will create a new user.
     */
    region?: pulumi.Input<string>;
    /**
     * Specifies the list of roles owned by the current user.
     * The object structure is documented below. Changing this parameter will create a new user.
     */
    roles: pulumi.Input<pulumi.Input<inputs.Dds.DatabaseUserRole>[]>;
}