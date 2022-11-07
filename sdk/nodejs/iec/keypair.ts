// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a keypair resource within HuaweiCloud IEC.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as huaweicloud from "@pulumi/huaweicloud";
 *
 * const testKeypair = new huaweicloud.Iec.Keypair("test_keypair", {});
 * ```
 *
 * ## Import
 *
 * Keypairs can be imported using the `name`, e.g.
 *
 * ```sh
 *  $ pulumi import huaweicloud:Iec/keypair:Keypair test_keypair iec-keypair-demo
 * ```
 */
export class Keypair extends pulumi.CustomResource {
    /**
     * Get an existing Keypair resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: KeypairState, opts?: pulumi.CustomResourceOptions): Keypair {
        return new Keypair(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'huaweicloud:Iec/keypair:Keypair';

    /**
     * Returns true if the given object is an instance of Keypair.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Keypair {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Keypair.__pulumiType;
    }

    /**
     * The finger of iec keypair. The value contains a encoding type(SHA256) and a string of 43 characters.
     */
    public /*out*/ readonly fingerprint!: pulumi.Output<string>;
    /**
     * Specifies a unique name for the keypair. This parameter can contain a maximum of
     * 64 characters, which may consist of letters, digits, underscores (_), and hyphens (-). Changing this parameter creates
     * a new keypair resource.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Specifies a pregenerated OpenSSH-formatted public key. Changing this
     * parameter creates a new keypair resource.
     */
    public readonly publicKey!: pulumi.Output<string>;
    public readonly region!: pulumi.Output<string>;

    /**
     * Create a Keypair resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: KeypairArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: KeypairArgs | KeypairState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as KeypairState | undefined;
            resourceInputs["fingerprint"] = state ? state.fingerprint : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["publicKey"] = state ? state.publicKey : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
        } else {
            const args = argsOrState as KeypairArgs | undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["publicKey"] = args ? args.publicKey : undefined;
            resourceInputs["region"] = args ? args.region : undefined;
            resourceInputs["fingerprint"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Keypair.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Keypair resources.
 */
export interface KeypairState {
    /**
     * The finger of iec keypair. The value contains a encoding type(SHA256) and a string of 43 characters.
     */
    fingerprint?: pulumi.Input<string>;
    /**
     * Specifies a unique name for the keypair. This parameter can contain a maximum of
     * 64 characters, which may consist of letters, digits, underscores (_), and hyphens (-). Changing this parameter creates
     * a new keypair resource.
     */
    name?: pulumi.Input<string>;
    /**
     * Specifies a pregenerated OpenSSH-formatted public key. Changing this
     * parameter creates a new keypair resource.
     */
    publicKey?: pulumi.Input<string>;
    region?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Keypair resource.
 */
export interface KeypairArgs {
    /**
     * Specifies a unique name for the keypair. This parameter can contain a maximum of
     * 64 characters, which may consist of letters, digits, underscores (_), and hyphens (-). Changing this parameter creates
     * a new keypair resource.
     */
    name?: pulumi.Input<string>;
    /**
     * Specifies a pregenerated OpenSSH-formatted public key. Changing this
     * parameter creates a new keypair resource.
     */
    publicKey?: pulumi.Input<string>;
    region?: pulumi.Input<string>;
}