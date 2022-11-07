// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Manages an IoTDA product within HuaweiCloud.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as huaweicloud from "@pulumi/huaweicloud";
 *
 * const config = new pulumi.Config();
 * const productName = config.requireObject("productName");
 * const space = new huaweicloud.iotda.Space("space", {});
 * const test = new huaweicloud.iotda.Product("test", {
 *     deviceType: "WaterMeter",
 *     protocol: "MQTT",
 *     spaceId: huaweicloud_iotda_space.test.id,
 *     dataType: "json",
 *     manufacturerName: "demo_manufacturer_name",
 *     industry: "demo_industry",
 *     services: [{
 *         id: "service_1",
 *         type: "serv_type",
 *         properties: [
 *             {
 *                 name: "p_1",
 *                 type: "int",
 *                 min: "3",
 *                 max: "666",
 *                 description: "desc",
 *                 method: "RW",
 *             },
 *             {
 *                 name: "p_2",
 *                 type: "string",
 *                 maxLength: 20,
 *                 enumLists: [
 *                     "1",
 *                     "E",
 *                 ],
 *                 method: "R",
 *             },
 *             {
 *                 name: "p_3",
 *                 type: "string",
 *                 method: "W",
 *                 maxLength: 200,
 *             },
 *             {
 *                 name: "p_4",
 *                 type: "decimal",
 *                 method: "W",
 *                 min: "3.1",
 *                 max: "666.99",
 *             },
 *         ],
 *         commands: [{
 *             name: "cmd_1",
 *             paras: [{
 *                 name: "cmd_p_1",
 *                 type: "int",
 *                 description: "desc",
 *                 min: "1",
 *                 max: "33",
 *             }],
 *             responses: [{
 *                 name: "cmd_r_1",
 *                 type: "int",
 *                 description: "desc",
 *                 min: "1",
 *                 max: "22",
 *             }],
 *         }],
 *     }],
 * });
 * ```
 *
 * ## Import
 *
 * Products can be imported using the `id`, e.g.
 *
 * ```sh
 *  $ pulumi import huaweicloud:IoTDA/product:Product test 10022532f4f94f26b01daa1e424853e1
 * ```
 */
export class Product extends pulumi.CustomResource {
    /**
     * Get an existing Product resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProductState, opts?: pulumi.CustomResourceOptions): Product {
        return new Product(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'huaweicloud:IoTDA/product:Product';

    /**
     * Returns true if the given object is an instance of Product.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Product {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Product.__pulumiType;
    }

    /**
     * Specifies the type of data.
     * The valid values are **json** and **binary**.
     */
    public readonly dataType!: pulumi.Output<string>;
    /**
     * Specifies the description of the parameter. The description contains a maximum of
     * 128 characters. Only letters, Chinese characters, digits, hyphens (-), underscores (_) and the following specail
     * characters are allowed: `?'#().,&%@!`.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Specifies the device type. The device type contains a maximum of 32 characters.
     * Only letters, Chinese characters, digits, hyphens (-), underscores (_) and the following specail characters
     * are allowed: `?'#().,&%@!`. Example: StreetLight, GasMeter, or WaterMeter.
     */
    public readonly deviceType!: pulumi.Output<string>;
    /**
     * Specifies the industry which the device belongs to. The industry contains a maximum of
     * 64 characters. Only letters, Chinese characters, digits, hyphens (-), underscores (_) and
     * the following specail characters are allowed: `?'#().,&%@!`.
     */
    public readonly industry!: pulumi.Output<string>;
    /**
     * Specifies the manufacturer name. The name contains a maximum of 32 characters.
     * Only letters, Chinese characters, digits, hyphens (-), underscores (_) and the following specail
     * characters are allowed: `?'#().,&%@!`.
     */
    public readonly manufacturerName!: pulumi.Output<string>;
    /**
     * Specifies the name of the parameter. The name contains a maximum of 64 characters.
     * Only letters, Chinese characters, digits, hyphens (-), underscores (_) and the following specail characters are
     * allowed: `?'#().,&%@!`.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Specifies the product ID. The product ID contains a maximum of 32
     * characters. Only letters, digits, hyphens (-) and underscores (_) are allowed. If omitted, the platform will
     * automatically allocate a product ID. Changing this parameter will create a new resource.
     */
    public readonly productId!: pulumi.Output<string>;
    /**
     * Specifies the protocal.
     * The valid values are **MQTT**, **CoAP**, **HTTP**, **HTTPS**, **Modbus**, **ONVIF**, **OPC-UA**, **OPC-DA**, **Other**.
     */
    public readonly protocol!: pulumi.Output<string>;
    /**
     * Specifies the region in which to create the IoTDA product resource.
     * If omitted, the provider-level region will be used. Changing this parameter will create a new resource.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * Specifies the list of services.
     * The services structure is documented below.
     */
    public readonly services!: pulumi.Output<outputs.IoTDA.ProductService[]>;
    /**
     * Specifies the resource space ID which the product belongs to. If omitted,
     * the product will belong to the default resource space. Changing this parameter will create a new resource.
     */
    public readonly spaceId!: pulumi.Output<string>;

    /**
     * Create a Product resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ProductArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ProductArgs | ProductState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ProductState | undefined;
            resourceInputs["dataType"] = state ? state.dataType : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["deviceType"] = state ? state.deviceType : undefined;
            resourceInputs["industry"] = state ? state.industry : undefined;
            resourceInputs["manufacturerName"] = state ? state.manufacturerName : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["productId"] = state ? state.productId : undefined;
            resourceInputs["protocol"] = state ? state.protocol : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["services"] = state ? state.services : undefined;
            resourceInputs["spaceId"] = state ? state.spaceId : undefined;
        } else {
            const args = argsOrState as ProductArgs | undefined;
            if ((!args || args.dataType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dataType'");
            }
            if ((!args || args.deviceType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'deviceType'");
            }
            if ((!args || args.protocol === undefined) && !opts.urn) {
                throw new Error("Missing required property 'protocol'");
            }
            if ((!args || args.services === undefined) && !opts.urn) {
                throw new Error("Missing required property 'services'");
            }
            resourceInputs["dataType"] = args ? args.dataType : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["deviceType"] = args ? args.deviceType : undefined;
            resourceInputs["industry"] = args ? args.industry : undefined;
            resourceInputs["manufacturerName"] = args ? args.manufacturerName : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["productId"] = args ? args.productId : undefined;
            resourceInputs["protocol"] = args ? args.protocol : undefined;
            resourceInputs["region"] = args ? args.region : undefined;
            resourceInputs["services"] = args ? args.services : undefined;
            resourceInputs["spaceId"] = args ? args.spaceId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Product.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Product resources.
 */
export interface ProductState {
    /**
     * Specifies the type of data.
     * The valid values are **json** and **binary**.
     */
    dataType?: pulumi.Input<string>;
    /**
     * Specifies the description of the parameter. The description contains a maximum of
     * 128 characters. Only letters, Chinese characters, digits, hyphens (-), underscores (_) and the following specail
     * characters are allowed: `?'#().,&%@!`.
     */
    description?: pulumi.Input<string>;
    /**
     * Specifies the device type. The device type contains a maximum of 32 characters.
     * Only letters, Chinese characters, digits, hyphens (-), underscores (_) and the following specail characters
     * are allowed: `?'#().,&%@!`. Example: StreetLight, GasMeter, or WaterMeter.
     */
    deviceType?: pulumi.Input<string>;
    /**
     * Specifies the industry which the device belongs to. The industry contains a maximum of
     * 64 characters. Only letters, Chinese characters, digits, hyphens (-), underscores (_) and
     * the following specail characters are allowed: `?'#().,&%@!`.
     */
    industry?: pulumi.Input<string>;
    /**
     * Specifies the manufacturer name. The name contains a maximum of 32 characters.
     * Only letters, Chinese characters, digits, hyphens (-), underscores (_) and the following specail
     * characters are allowed: `?'#().,&%@!`.
     */
    manufacturerName?: pulumi.Input<string>;
    /**
     * Specifies the name of the parameter. The name contains a maximum of 64 characters.
     * Only letters, Chinese characters, digits, hyphens (-), underscores (_) and the following specail characters are
     * allowed: `?'#().,&%@!`.
     */
    name?: pulumi.Input<string>;
    /**
     * Specifies the product ID. The product ID contains a maximum of 32
     * characters. Only letters, digits, hyphens (-) and underscores (_) are allowed. If omitted, the platform will
     * automatically allocate a product ID. Changing this parameter will create a new resource.
     */
    productId?: pulumi.Input<string>;
    /**
     * Specifies the protocal.
     * The valid values are **MQTT**, **CoAP**, **HTTP**, **HTTPS**, **Modbus**, **ONVIF**, **OPC-UA**, **OPC-DA**, **Other**.
     */
    protocol?: pulumi.Input<string>;
    /**
     * Specifies the region in which to create the IoTDA product resource.
     * If omitted, the provider-level region will be used. Changing this parameter will create a new resource.
     */
    region?: pulumi.Input<string>;
    /**
     * Specifies the list of services.
     * The services structure is documented below.
     */
    services?: pulumi.Input<pulumi.Input<inputs.IoTDA.ProductService>[]>;
    /**
     * Specifies the resource space ID which the product belongs to. If omitted,
     * the product will belong to the default resource space. Changing this parameter will create a new resource.
     */
    spaceId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Product resource.
 */
export interface ProductArgs {
    /**
     * Specifies the type of data.
     * The valid values are **json** and **binary**.
     */
    dataType: pulumi.Input<string>;
    /**
     * Specifies the description of the parameter. The description contains a maximum of
     * 128 characters. Only letters, Chinese characters, digits, hyphens (-), underscores (_) and the following specail
     * characters are allowed: `?'#().,&%@!`.
     */
    description?: pulumi.Input<string>;
    /**
     * Specifies the device type. The device type contains a maximum of 32 characters.
     * Only letters, Chinese characters, digits, hyphens (-), underscores (_) and the following specail characters
     * are allowed: `?'#().,&%@!`. Example: StreetLight, GasMeter, or WaterMeter.
     */
    deviceType: pulumi.Input<string>;
    /**
     * Specifies the industry which the device belongs to. The industry contains a maximum of
     * 64 characters. Only letters, Chinese characters, digits, hyphens (-), underscores (_) and
     * the following specail characters are allowed: `?'#().,&%@!`.
     */
    industry?: pulumi.Input<string>;
    /**
     * Specifies the manufacturer name. The name contains a maximum of 32 characters.
     * Only letters, Chinese characters, digits, hyphens (-), underscores (_) and the following specail
     * characters are allowed: `?'#().,&%@!`.
     */
    manufacturerName?: pulumi.Input<string>;
    /**
     * Specifies the name of the parameter. The name contains a maximum of 64 characters.
     * Only letters, Chinese characters, digits, hyphens (-), underscores (_) and the following specail characters are
     * allowed: `?'#().,&%@!`.
     */
    name?: pulumi.Input<string>;
    /**
     * Specifies the product ID. The product ID contains a maximum of 32
     * characters. Only letters, digits, hyphens (-) and underscores (_) are allowed. If omitted, the platform will
     * automatically allocate a product ID. Changing this parameter will create a new resource.
     */
    productId?: pulumi.Input<string>;
    /**
     * Specifies the protocal.
     * The valid values are **MQTT**, **CoAP**, **HTTP**, **HTTPS**, **Modbus**, **ONVIF**, **OPC-UA**, **OPC-DA**, **Other**.
     */
    protocol: pulumi.Input<string>;
    /**
     * Specifies the region in which to create the IoTDA product resource.
     * If omitted, the provider-level region will be used. Changing this parameter will create a new resource.
     */
    region?: pulumi.Input<string>;
    /**
     * Specifies the list of services.
     * The services structure is documented below.
     */
    services: pulumi.Input<pulumi.Input<inputs.IoTDA.ProductService>[]>;
    /**
     * Specifies the resource space ID which the product belongs to. If omitted,
     * the product will belong to the default resource space. Changing this parameter will create a new resource.
     */
    spaceId?: pulumi.Input<string>;
}