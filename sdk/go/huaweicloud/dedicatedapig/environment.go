// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dedicatedapig

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages an APIG environment resource within HuaweiCloud.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/huaweicloud/pulumi-huaweicloud/sdk/go/huaweicloud/DedicatedApig"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			cfg := config.New(ctx, "")
//			instanceId := cfg.RequireObject("instanceId")
//			environmentName := cfg.RequireObject("environmentName")
//			description := cfg.RequireObject("description")
//			_, err := DedicatedApig.NewEnvironment(ctx, "test", &DedicatedApig.EnvironmentArgs{
//				InstanceId:  pulumi.Any(instanceId),
//				Description: pulumi.Any(description),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// Environments can be imported using their `id` and the ID of the APIG instance to which the environment belongs, separated by a slash, e.g.
//
// ```sh
//
//	$ pulumi import huaweicloud:DedicatedApig/environment:Environment test <instance ID>/<id>
//
// ```
type Environment struct {
	pulumi.CustomResourceState

	// Time when the APIG environment was created, in RFC-3339 format.
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// Specifies the description about the API environment. The description contain a
	// maximum of 255 characters and the angle brackets (< and >) are not allowed. Chinese characters must be in UTF-8 or
	// Unicode format.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Specifies an ID of the APIG dedicated instance to which the API
	// environment belongs to. Changing this will create a new APIG environment resource.
	InstanceId pulumi.StringOutput `pulumi:"instanceId"`
	// Specifies the name of the API environment. The API environment name consists of 3 to 64
	// characters, starting with a letter. Only letters, digits and underscores (_) are allowed.
	Name pulumi.StringOutput `pulumi:"name"`
	// Specifies the region in which to create the APIG environment resource. If
	// omitted, the provider-level region will be used. Changing this will create a new APIG environment resource.
	Region pulumi.StringOutput `pulumi:"region"`
}

// NewEnvironment registers a new resource with the given unique name, arguments, and options.
func NewEnvironment(ctx *pulumi.Context,
	name string, args *EnvironmentArgs, opts ...pulumi.ResourceOption) (*Environment, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.InstanceId == nil {
		return nil, errors.New("invalid value for required argument 'InstanceId'")
	}
	var resource Environment
	err := ctx.RegisterResource("huaweicloud:DedicatedApig/environment:Environment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEnvironment gets an existing Environment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEnvironment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EnvironmentState, opts ...pulumi.ResourceOption) (*Environment, error) {
	var resource Environment
	err := ctx.ReadResource("huaweicloud:DedicatedApig/environment:Environment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Environment resources.
type environmentState struct {
	// Time when the APIG environment was created, in RFC-3339 format.
	CreateTime *string `pulumi:"createTime"`
	// Specifies the description about the API environment. The description contain a
	// maximum of 255 characters and the angle brackets (< and >) are not allowed. Chinese characters must be in UTF-8 or
	// Unicode format.
	Description *string `pulumi:"description"`
	// Specifies an ID of the APIG dedicated instance to which the API
	// environment belongs to. Changing this will create a new APIG environment resource.
	InstanceId *string `pulumi:"instanceId"`
	// Specifies the name of the API environment. The API environment name consists of 3 to 64
	// characters, starting with a letter. Only letters, digits and underscores (_) are allowed.
	Name *string `pulumi:"name"`
	// Specifies the region in which to create the APIG environment resource. If
	// omitted, the provider-level region will be used. Changing this will create a new APIG environment resource.
	Region *string `pulumi:"region"`
}

type EnvironmentState struct {
	// Time when the APIG environment was created, in RFC-3339 format.
	CreateTime pulumi.StringPtrInput
	// Specifies the description about the API environment. The description contain a
	// maximum of 255 characters and the angle brackets (< and >) are not allowed. Chinese characters must be in UTF-8 or
	// Unicode format.
	Description pulumi.StringPtrInput
	// Specifies an ID of the APIG dedicated instance to which the API
	// environment belongs to. Changing this will create a new APIG environment resource.
	InstanceId pulumi.StringPtrInput
	// Specifies the name of the API environment. The API environment name consists of 3 to 64
	// characters, starting with a letter. Only letters, digits and underscores (_) are allowed.
	Name pulumi.StringPtrInput
	// Specifies the region in which to create the APIG environment resource. If
	// omitted, the provider-level region will be used. Changing this will create a new APIG environment resource.
	Region pulumi.StringPtrInput
}

func (EnvironmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*environmentState)(nil)).Elem()
}

type environmentArgs struct {
	// Specifies the description about the API environment. The description contain a
	// maximum of 255 characters and the angle brackets (< and >) are not allowed. Chinese characters must be in UTF-8 or
	// Unicode format.
	Description *string `pulumi:"description"`
	// Specifies an ID of the APIG dedicated instance to which the API
	// environment belongs to. Changing this will create a new APIG environment resource.
	InstanceId string `pulumi:"instanceId"`
	// Specifies the name of the API environment. The API environment name consists of 3 to 64
	// characters, starting with a letter. Only letters, digits and underscores (_) are allowed.
	Name *string `pulumi:"name"`
	// Specifies the region in which to create the APIG environment resource. If
	// omitted, the provider-level region will be used. Changing this will create a new APIG environment resource.
	Region *string `pulumi:"region"`
}

// The set of arguments for constructing a Environment resource.
type EnvironmentArgs struct {
	// Specifies the description about the API environment. The description contain a
	// maximum of 255 characters and the angle brackets (< and >) are not allowed. Chinese characters must be in UTF-8 or
	// Unicode format.
	Description pulumi.StringPtrInput
	// Specifies an ID of the APIG dedicated instance to which the API
	// environment belongs to. Changing this will create a new APIG environment resource.
	InstanceId pulumi.StringInput
	// Specifies the name of the API environment. The API environment name consists of 3 to 64
	// characters, starting with a letter. Only letters, digits and underscores (_) are allowed.
	Name pulumi.StringPtrInput
	// Specifies the region in which to create the APIG environment resource. If
	// omitted, the provider-level region will be used. Changing this will create a new APIG environment resource.
	Region pulumi.StringPtrInput
}

func (EnvironmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*environmentArgs)(nil)).Elem()
}

type EnvironmentInput interface {
	pulumi.Input

	ToEnvironmentOutput() EnvironmentOutput
	ToEnvironmentOutputWithContext(ctx context.Context) EnvironmentOutput
}

func (*Environment) ElementType() reflect.Type {
	return reflect.TypeOf((**Environment)(nil)).Elem()
}

func (i *Environment) ToEnvironmentOutput() EnvironmentOutput {
	return i.ToEnvironmentOutputWithContext(context.Background())
}

func (i *Environment) ToEnvironmentOutputWithContext(ctx context.Context) EnvironmentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EnvironmentOutput)
}

// EnvironmentArrayInput is an input type that accepts EnvironmentArray and EnvironmentArrayOutput values.
// You can construct a concrete instance of `EnvironmentArrayInput` via:
//
//	EnvironmentArray{ EnvironmentArgs{...} }
type EnvironmentArrayInput interface {
	pulumi.Input

	ToEnvironmentArrayOutput() EnvironmentArrayOutput
	ToEnvironmentArrayOutputWithContext(context.Context) EnvironmentArrayOutput
}

type EnvironmentArray []EnvironmentInput

func (EnvironmentArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Environment)(nil)).Elem()
}

func (i EnvironmentArray) ToEnvironmentArrayOutput() EnvironmentArrayOutput {
	return i.ToEnvironmentArrayOutputWithContext(context.Background())
}

func (i EnvironmentArray) ToEnvironmentArrayOutputWithContext(ctx context.Context) EnvironmentArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EnvironmentArrayOutput)
}

// EnvironmentMapInput is an input type that accepts EnvironmentMap and EnvironmentMapOutput values.
// You can construct a concrete instance of `EnvironmentMapInput` via:
//
//	EnvironmentMap{ "key": EnvironmentArgs{...} }
type EnvironmentMapInput interface {
	pulumi.Input

	ToEnvironmentMapOutput() EnvironmentMapOutput
	ToEnvironmentMapOutputWithContext(context.Context) EnvironmentMapOutput
}

type EnvironmentMap map[string]EnvironmentInput

func (EnvironmentMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Environment)(nil)).Elem()
}

func (i EnvironmentMap) ToEnvironmentMapOutput() EnvironmentMapOutput {
	return i.ToEnvironmentMapOutputWithContext(context.Background())
}

func (i EnvironmentMap) ToEnvironmentMapOutputWithContext(ctx context.Context) EnvironmentMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EnvironmentMapOutput)
}

type EnvironmentOutput struct{ *pulumi.OutputState }

func (EnvironmentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Environment)(nil)).Elem()
}

func (o EnvironmentOutput) ToEnvironmentOutput() EnvironmentOutput {
	return o
}

func (o EnvironmentOutput) ToEnvironmentOutputWithContext(ctx context.Context) EnvironmentOutput {
	return o
}

// Time when the APIG environment was created, in RFC-3339 format.
func (o EnvironmentOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Environment) pulumi.StringOutput { return v.CreateTime }).(pulumi.StringOutput)
}

// Specifies the description about the API environment. The description contain a
// maximum of 255 characters and the angle brackets (< and >) are not allowed. Chinese characters must be in UTF-8 or
// Unicode format.
func (o EnvironmentOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Environment) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// Specifies an ID of the APIG dedicated instance to which the API
// environment belongs to. Changing this will create a new APIG environment resource.
func (o EnvironmentOutput) InstanceId() pulumi.StringOutput {
	return o.ApplyT(func(v *Environment) pulumi.StringOutput { return v.InstanceId }).(pulumi.StringOutput)
}

// Specifies the name of the API environment. The API environment name consists of 3 to 64
// characters, starting with a letter. Only letters, digits and underscores (_) are allowed.
func (o EnvironmentOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Environment) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Specifies the region in which to create the APIG environment resource. If
// omitted, the provider-level region will be used. Changing this will create a new APIG environment resource.
func (o EnvironmentOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v *Environment) pulumi.StringOutput { return v.Region }).(pulumi.StringOutput)
}

type EnvironmentArrayOutput struct{ *pulumi.OutputState }

func (EnvironmentArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Environment)(nil)).Elem()
}

func (o EnvironmentArrayOutput) ToEnvironmentArrayOutput() EnvironmentArrayOutput {
	return o
}

func (o EnvironmentArrayOutput) ToEnvironmentArrayOutputWithContext(ctx context.Context) EnvironmentArrayOutput {
	return o
}

func (o EnvironmentArrayOutput) Index(i pulumi.IntInput) EnvironmentOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Environment {
		return vs[0].([]*Environment)[vs[1].(int)]
	}).(EnvironmentOutput)
}

type EnvironmentMapOutput struct{ *pulumi.OutputState }

func (EnvironmentMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Environment)(nil)).Elem()
}

func (o EnvironmentMapOutput) ToEnvironmentMapOutput() EnvironmentMapOutput {
	return o
}

func (o EnvironmentMapOutput) ToEnvironmentMapOutputWithContext(ctx context.Context) EnvironmentMapOutput {
	return o
}

func (o EnvironmentMapOutput) MapIndex(k pulumi.StringInput) EnvironmentOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Environment {
		return vs[0].(map[string]*Environment)[vs[1].(string)]
	}).(EnvironmentOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*EnvironmentInput)(nil)).Elem(), &Environment{})
	pulumi.RegisterInputType(reflect.TypeOf((*EnvironmentArrayInput)(nil)).Elem(), EnvironmentArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*EnvironmentMapInput)(nil)).Elem(), EnvironmentMap{})
	pulumi.RegisterOutputType(EnvironmentOutput{})
	pulumi.RegisterOutputType(EnvironmentArrayOutput{})
	pulumi.RegisterOutputType(EnvironmentMapOutput{})
}