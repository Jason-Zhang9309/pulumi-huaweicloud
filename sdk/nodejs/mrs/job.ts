// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manage a job resource within HuaweiCloud MRS.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as huaweicloud from "@pulumi/huaweicloud";
 *
 * const config = new pulumi.Config();
 * const clusterId = config.requireObject("clusterId");
 * const jobName = config.requireObject("jobName");
 * const programPath = config.requireObject("programPath");
 * const accessKey = config.requireObject("accessKey");
 * const secretKey = config.requireObject("secretKey");
 * const test = new huaweicloud.mrs.Job("test", {
 *     clusterId: clusterId,
 *     type: "SparkSubmit",
 *     programPath: programPath,
 *     parameters: `${accessKey} ${secretKey} 1 obs://obs-demo-analysis/input obs://obs-demo-analysis/output`,
 *     programParameters: {
 *         "--class": "com.huawei.bigdata.spark.examples.DriverBehavior",
 *     },
 * });
 * ```
 *
 * ## Import
 *
 * MapReduce jobs can be imported using their `id` and the IDs of the MapReduce cluster to which the job belongs, separated by a slash, e.g.
 *
 * ```sh
 *  $ pulumi import huaweicloud:Mrs/job:Job test <cluster_id>/<id>
 * ```
 */
export class Job extends pulumi.CustomResource {
    /**
     * Get an existing Job resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: JobState, opts?: pulumi.CustomResourceOptions): Job {
        return new Job(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'huaweicloud:Mrs/job:Job';

    /**
     * Returns true if the given object is an instance of Job.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Job {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Job.__pulumiType;
    }

    /**
     * Specifies an ID of the MapReduce cluster to which the job belongs to.
     * Changing this will create a new MapReduce job resource.
     */
    public readonly clusterId!: pulumi.Output<string>;
    /**
     * The completion time of the MapReduce job.
     */
    public /*out*/ readonly finishTime!: pulumi.Output<string>;
    /**
     * Specifies the name of the MapReduce job. The name can contain 1 to 64
     * characters, which may consist of letters, digits, underscores (_) and hyphens (-). Changing this will create a new
     * MapReduce job resource.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Specifies the parameters for the MapReduce job. Add an at sign (@) before
     * each parameter can prevent the parameters being saved in plaintext format. Each parameters are separated with spaces.
     * This parameter can be set when `type` is **Flink**, **MapReduce** or **SparkSubmit**. Changing this will create a new
     * MapReduce job resource.
     */
    public readonly parameters!: pulumi.Output<string | undefined>;
    /**
     * Specifies the the key/value pairs of the program parameters, such as
     * thread, memory, and vCPUs, are used to optimize resource usage and improve job execution performance. This parameter
     * can be set when `type` is **Flink**, **SparkSubmit**, **SparkSql**, **SparkScript**, **HiveSql** or
     * **HiveScript**. Refer to the documents for each type of support key-values.
     * Changing this will create a new MapReduce job resource.
     */
    public readonly programParameters!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * Specifies the .jar package path or .py file path for program execution.
     * The parameter must meet the following requirements:
     * + Contains a maximum of 1023 characters, excluding special characters such as `;|&><'$`.
     * + The address cannot be empty or full of spaces.
     * + The program support OBS or DHFS to storage program file or package. For OBS, starts with (OBS:) **obs://** and end
     * with **.jar** or **.py**. For DHFS, starts with (DHFS:) **&#47;user**.
     */
    public readonly programPath!: pulumi.Output<string | undefined>;
    /**
     * Specifies the region in which to create the MapReduce job resource. If
     * omitted, the provider-level region will be used. Changing this will create a new MapReduce job resource.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * Specifies the key/value pairs used to modify service configuration.
     * Parameter configurations of services are available on the Service Configuration tab page of MapReduce Manager.
     * Changing this will create a new MapReduce job resource.
     */
    public readonly serviceParameters!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * Specifies the SQL command or file path. Only required if `type` is **HiveSql**
     * or **SparkSql**. Changing this will create a new MapReduce job resource.
     */
    public readonly sql!: pulumi.Output<string | undefined>;
    /**
     * The creation time of the MapReduce job.
     */
    public /*out*/ readonly startTime!: pulumi.Output<string>;
    /**
     * Status of the MapReduce job.
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * The submission time of the MapReduce job.
     */
    public /*out*/ readonly submitTime!: pulumi.Output<string>;
    public readonly type!: pulumi.Output<string>;

    /**
     * Create a Job resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: JobArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: JobArgs | JobState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as JobState | undefined;
            resourceInputs["clusterId"] = state ? state.clusterId : undefined;
            resourceInputs["finishTime"] = state ? state.finishTime : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["parameters"] = state ? state.parameters : undefined;
            resourceInputs["programParameters"] = state ? state.programParameters : undefined;
            resourceInputs["programPath"] = state ? state.programPath : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["serviceParameters"] = state ? state.serviceParameters : undefined;
            resourceInputs["sql"] = state ? state.sql : undefined;
            resourceInputs["startTime"] = state ? state.startTime : undefined;
            resourceInputs["status"] = state ? state.status : undefined;
            resourceInputs["submitTime"] = state ? state.submitTime : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
        } else {
            const args = argsOrState as JobArgs | undefined;
            if ((!args || args.clusterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clusterId'");
            }
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            resourceInputs["clusterId"] = args ? args.clusterId : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["parameters"] = args ? args.parameters : undefined;
            resourceInputs["programParameters"] = args ? args.programParameters : undefined;
            resourceInputs["programPath"] = args ? args.programPath : undefined;
            resourceInputs["region"] = args ? args.region : undefined;
            resourceInputs["serviceParameters"] = args ? args.serviceParameters : undefined;
            resourceInputs["sql"] = args ? args.sql : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["finishTime"] = undefined /*out*/;
            resourceInputs["startTime"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["submitTime"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Job.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Job resources.
 */
export interface JobState {
    /**
     * Specifies an ID of the MapReduce cluster to which the job belongs to.
     * Changing this will create a new MapReduce job resource.
     */
    clusterId?: pulumi.Input<string>;
    /**
     * The completion time of the MapReduce job.
     */
    finishTime?: pulumi.Input<string>;
    /**
     * Specifies the name of the MapReduce job. The name can contain 1 to 64
     * characters, which may consist of letters, digits, underscores (_) and hyphens (-). Changing this will create a new
     * MapReduce job resource.
     */
    name?: pulumi.Input<string>;
    /**
     * Specifies the parameters for the MapReduce job. Add an at sign (@) before
     * each parameter can prevent the parameters being saved in plaintext format. Each parameters are separated with spaces.
     * This parameter can be set when `type` is **Flink**, **MapReduce** or **SparkSubmit**. Changing this will create a new
     * MapReduce job resource.
     */
    parameters?: pulumi.Input<string>;
    /**
     * Specifies the the key/value pairs of the program parameters, such as
     * thread, memory, and vCPUs, are used to optimize resource usage and improve job execution performance. This parameter
     * can be set when `type` is **Flink**, **SparkSubmit**, **SparkSql**, **SparkScript**, **HiveSql** or
     * **HiveScript**. Refer to the documents for each type of support key-values.
     * Changing this will create a new MapReduce job resource.
     */
    programParameters?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Specifies the .jar package path or .py file path for program execution.
     * The parameter must meet the following requirements:
     * + Contains a maximum of 1023 characters, excluding special characters such as `;|&><'$`.
     * + The address cannot be empty or full of spaces.
     * + The program support OBS or DHFS to storage program file or package. For OBS, starts with (OBS:) **obs://** and end
     * with **.jar** or **.py**. For DHFS, starts with (DHFS:) **&#47;user**.
     */
    programPath?: pulumi.Input<string>;
    /**
     * Specifies the region in which to create the MapReduce job resource. If
     * omitted, the provider-level region will be used. Changing this will create a new MapReduce job resource.
     */
    region?: pulumi.Input<string>;
    /**
     * Specifies the key/value pairs used to modify service configuration.
     * Parameter configurations of services are available on the Service Configuration tab page of MapReduce Manager.
     * Changing this will create a new MapReduce job resource.
     */
    serviceParameters?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Specifies the SQL command or file path. Only required if `type` is **HiveSql**
     * or **SparkSql**. Changing this will create a new MapReduce job resource.
     */
    sql?: pulumi.Input<string>;
    /**
     * The creation time of the MapReduce job.
     */
    startTime?: pulumi.Input<string>;
    /**
     * Status of the MapReduce job.
     */
    status?: pulumi.Input<string>;
    /**
     * The submission time of the MapReduce job.
     */
    submitTime?: pulumi.Input<string>;
    type?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Job resource.
 */
export interface JobArgs {
    /**
     * Specifies an ID of the MapReduce cluster to which the job belongs to.
     * Changing this will create a new MapReduce job resource.
     */
    clusterId: pulumi.Input<string>;
    /**
     * Specifies the name of the MapReduce job. The name can contain 1 to 64
     * characters, which may consist of letters, digits, underscores (_) and hyphens (-). Changing this will create a new
     * MapReduce job resource.
     */
    name?: pulumi.Input<string>;
    /**
     * Specifies the parameters for the MapReduce job. Add an at sign (@) before
     * each parameter can prevent the parameters being saved in plaintext format. Each parameters are separated with spaces.
     * This parameter can be set when `type` is **Flink**, **MapReduce** or **SparkSubmit**. Changing this will create a new
     * MapReduce job resource.
     */
    parameters?: pulumi.Input<string>;
    /**
     * Specifies the the key/value pairs of the program parameters, such as
     * thread, memory, and vCPUs, are used to optimize resource usage and improve job execution performance. This parameter
     * can be set when `type` is **Flink**, **SparkSubmit**, **SparkSql**, **SparkScript**, **HiveSql** or
     * **HiveScript**. Refer to the documents for each type of support key-values.
     * Changing this will create a new MapReduce job resource.
     */
    programParameters?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Specifies the .jar package path or .py file path for program execution.
     * The parameter must meet the following requirements:
     * + Contains a maximum of 1023 characters, excluding special characters such as `;|&><'$`.
     * + The address cannot be empty or full of spaces.
     * + The program support OBS or DHFS to storage program file or package. For OBS, starts with (OBS:) **obs://** and end
     * with **.jar** or **.py**. For DHFS, starts with (DHFS:) **&#47;user**.
     */
    programPath?: pulumi.Input<string>;
    /**
     * Specifies the region in which to create the MapReduce job resource. If
     * omitted, the provider-level region will be used. Changing this will create a new MapReduce job resource.
     */
    region?: pulumi.Input<string>;
    /**
     * Specifies the key/value pairs used to modify service configuration.
     * Parameter configurations of services are available on the Service Configuration tab page of MapReduce Manager.
     * Changing this will create a new MapReduce job resource.
     */
    serviceParameters?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Specifies the SQL command or file path. Only required if `type` is **HiveSql**
     * or **SparkSql**. Changing this will create a new MapReduce job resource.
     */
    sql?: pulumi.Input<string>;
    type: pulumi.Input<string>;
}