// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Use this data source to get the available of HuaweiCloud IEC sites.
 *
 * ## Example Usage
 * ### Basic IEC Sites
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as huaweicloud from "@pulumi/huaweicloud";
 *
 * const iecSites = pulumi.output(huaweicloud.Iec.getSites());
 * ```
 */
export function getSites(args?: GetSitesArgs, opts?: pulumi.InvokeOptions): Promise<GetSitesResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("huaweicloud:Iec/getSites:getSites", {
        "area": args.area,
        "city": args.city,
        "province": args.province,
        "region": args.region,
    }, opts);
}

/**
 * A collection of arguments for invoking getSites.
 */
export interface GetSitesArgs {
    /**
     * Specifies the area of the IEC sites located.
     */
    area?: string;
    /**
     * Specifies the city of the IEC sites located.
     */
    city?: string;
    /**
     * Specifies the province of the IEC sites located.
     */
    province?: string;
    region?: string;
}

/**
 * A collection of values returned by getSites.
 */
export interface GetSitesResult {
    /**
     * The area of the IEC service site located.
     */
    readonly area?: string;
    /**
     * The city of the IEC service site located.
     */
    readonly city?: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The province of the IEC service site located.
     */
    readonly province?: string;
    readonly region: string;
    /**
     * An array of one or more IEC service sites. The sites object structure is documented below.
     */
    readonly sites: outputs.Iec.GetSitesSite[];
}

export function getSitesOutput(args?: GetSitesOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetSitesResult> {
    return pulumi.output(args).apply(a => getSites(a, opts))
}

/**
 * A collection of arguments for invoking getSites.
 */
export interface GetSitesOutputArgs {
    /**
     * Specifies the area of the IEC sites located.
     */
    area?: pulumi.Input<string>;
    /**
     * Specifies the city of the IEC sites located.
     */
    city?: pulumi.Input<string>;
    /**
     * Specifies the province of the IEC sites located.
     */
    province?: pulumi.Input<string>;
    region?: pulumi.Input<string>;
}