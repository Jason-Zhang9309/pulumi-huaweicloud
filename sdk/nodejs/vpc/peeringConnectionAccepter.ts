// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

export class PeeringConnectionAccepter extends pulumi.CustomResource {
    /**
     * Get an existing PeeringConnectionAccepter resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PeeringConnectionAccepterState, opts?: pulumi.CustomResourceOptions): PeeringConnectionAccepter {
        return new PeeringConnectionAccepter(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'huaweicloud:Vpc/peeringConnectionAccepter:PeeringConnectionAccepter';

    /**
     * Returns true if the given object is an instance of PeeringConnectionAccepter.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PeeringConnectionAccepter {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PeeringConnectionAccepter.__pulumiType;
    }

    /**
     * - Whether or not to accept the peering request. Defaults to `false`.
     */
    public readonly accept!: pulumi.Output<boolean | undefined>;
    /**
     * The VPC peering connection name.
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * The Tenant Id of the accepter tenant.
     */
    public /*out*/ readonly peerTenantId!: pulumi.Output<string>;
    /**
     * The VPC ID of the accepter tenant.
     */
    public /*out*/ readonly peerVpcId!: pulumi.Output<string>;
    /**
     * The region in which to create the vpc peering connection accepter. If omitted,
     * the provider-level region will be used. Changing this creates a new VPC peering connection accepter resource.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * The VPC peering connection status.
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * The ID of requester VPC involved in a VPC peering connection.
     */
    public /*out*/ readonly vpcId!: pulumi.Output<string>;
    /**
     * - The VPC Peering Connection ID to manage. Changing this
     * creates a new VPC peering connection accepter.
     */
    public readonly vpcPeeringConnectionId!: pulumi.Output<string>;

    /**
     * Create a PeeringConnectionAccepter resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PeeringConnectionAccepterArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PeeringConnectionAccepterArgs | PeeringConnectionAccepterState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as PeeringConnectionAccepterState | undefined;
            resourceInputs["accept"] = state ? state.accept : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["peerTenantId"] = state ? state.peerTenantId : undefined;
            resourceInputs["peerVpcId"] = state ? state.peerVpcId : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["status"] = state ? state.status : undefined;
            resourceInputs["vpcId"] = state ? state.vpcId : undefined;
            resourceInputs["vpcPeeringConnectionId"] = state ? state.vpcPeeringConnectionId : undefined;
        } else {
            const args = argsOrState as PeeringConnectionAccepterArgs | undefined;
            if ((!args || args.vpcPeeringConnectionId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'vpcPeeringConnectionId'");
            }
            resourceInputs["accept"] = args ? args.accept : undefined;
            resourceInputs["region"] = args ? args.region : undefined;
            resourceInputs["vpcPeeringConnectionId"] = args ? args.vpcPeeringConnectionId : undefined;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["peerTenantId"] = undefined /*out*/;
            resourceInputs["peerVpcId"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["vpcId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(PeeringConnectionAccepter.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering PeeringConnectionAccepter resources.
 */
export interface PeeringConnectionAccepterState {
    /**
     * - Whether or not to accept the peering request. Defaults to `false`.
     */
    accept?: pulumi.Input<boolean>;
    /**
     * The VPC peering connection name.
     */
    name?: pulumi.Input<string>;
    /**
     * The Tenant Id of the accepter tenant.
     */
    peerTenantId?: pulumi.Input<string>;
    /**
     * The VPC ID of the accepter tenant.
     */
    peerVpcId?: pulumi.Input<string>;
    /**
     * The region in which to create the vpc peering connection accepter. If omitted,
     * the provider-level region will be used. Changing this creates a new VPC peering connection accepter resource.
     */
    region?: pulumi.Input<string>;
    /**
     * The VPC peering connection status.
     */
    status?: pulumi.Input<string>;
    /**
     * The ID of requester VPC involved in a VPC peering connection.
     */
    vpcId?: pulumi.Input<string>;
    /**
     * - The VPC Peering Connection ID to manage. Changing this
     * creates a new VPC peering connection accepter.
     */
    vpcPeeringConnectionId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a PeeringConnectionAccepter resource.
 */
export interface PeeringConnectionAccepterArgs {
    /**
     * - Whether or not to accept the peering request. Defaults to `false`.
     */
    accept?: pulumi.Input<boolean>;
    /**
     * The region in which to create the vpc peering connection accepter. If omitted,
     * the provider-level region will be used. Changing this creates a new VPC peering connection accepter resource.
     */
    region?: pulumi.Input<string>;
    /**
     * - The VPC Peering Connection ID to manage. Changing this
     * creates a new VPC peering connection accepter.
     */
    vpcPeeringConnectionId: pulumi.Input<string>;
}