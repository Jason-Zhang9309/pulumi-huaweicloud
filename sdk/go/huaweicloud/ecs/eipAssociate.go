// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ecs

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// * Associates the **IPv4** address of an ECS instance to a specified EIP.
// * Associates the **IPv6** address of an ECS instance to a specified **Shared** Bandwidth.
//
// ## Example Usage
//
// ## Import
//
// This resource can be imported using the related `eip address` or `bandwidth_id`, `instance_id` and `fixed_ip`, separated by slashes, e.g.
//
// ```sh
//
//	$ pulumi import huaweicloud:Ecs/eipAssociate:EipAssociate bind <eip address or bandwidth_id>/<instance_id>/<fixed_ip>
//
// ```
type EipAssociate struct {
	pulumi.CustomResourceState

	// Specifies the **shared** bandwidth ID to associate.
	// It's **mandatory** when you want to associate the ECS instance with a specified shared bandwidth.
	// Changing this creates a new resource.
	BandwidthId pulumi.StringPtrOutput `pulumi:"bandwidthId"`
	// Specifies the private IP address to direct traffic to. It's **mandatory**
	// and must be a valid IPv6 address when you want to associate the ECS instance with a specified shared bandwidth.
	// Changing this creates a new resource.
	FixedIp pulumi.StringOutput `pulumi:"fixedIp"`
	// Specifies the ID of ECS instance to associated with.
	// Changing this creates a new resource.
	InstanceId pulumi.StringOutput `pulumi:"instanceId"`
	// The port ID of the ECS instance that associated with.
	PortId pulumi.StringOutput `pulumi:"portId"`
	// Specifies the EIP address to associate. It's **mandatory**
	// when you want to associate the ECS instance with an EIP. Changing this creates a new resource.
	PublicIp pulumi.StringPtrOutput `pulumi:"publicIp"`
	// Specifies the region in which to create the associated resource.
	// If omitted, the provider-level region will be used. Changing this creates a new resource.
	Region pulumi.StringOutput `pulumi:"region"`
}

// NewEipAssociate registers a new resource with the given unique name, arguments, and options.
func NewEipAssociate(ctx *pulumi.Context,
	name string, args *EipAssociateArgs, opts ...pulumi.ResourceOption) (*EipAssociate, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.InstanceId == nil {
		return nil, errors.New("invalid value for required argument 'InstanceId'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource EipAssociate
	err := ctx.RegisterResource("huaweicloud:Ecs/eipAssociate:EipAssociate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEipAssociate gets an existing EipAssociate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEipAssociate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EipAssociateState, opts ...pulumi.ResourceOption) (*EipAssociate, error) {
	var resource EipAssociate
	err := ctx.ReadResource("huaweicloud:Ecs/eipAssociate:EipAssociate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering EipAssociate resources.
type eipAssociateState struct {
	// Specifies the **shared** bandwidth ID to associate.
	// It's **mandatory** when you want to associate the ECS instance with a specified shared bandwidth.
	// Changing this creates a new resource.
	BandwidthId *string `pulumi:"bandwidthId"`
	// Specifies the private IP address to direct traffic to. It's **mandatory**
	// and must be a valid IPv6 address when you want to associate the ECS instance with a specified shared bandwidth.
	// Changing this creates a new resource.
	FixedIp *string `pulumi:"fixedIp"`
	// Specifies the ID of ECS instance to associated with.
	// Changing this creates a new resource.
	InstanceId *string `pulumi:"instanceId"`
	// The port ID of the ECS instance that associated with.
	PortId *string `pulumi:"portId"`
	// Specifies the EIP address to associate. It's **mandatory**
	// when you want to associate the ECS instance with an EIP. Changing this creates a new resource.
	PublicIp *string `pulumi:"publicIp"`
	// Specifies the region in which to create the associated resource.
	// If omitted, the provider-level region will be used. Changing this creates a new resource.
	Region *string `pulumi:"region"`
}

type EipAssociateState struct {
	// Specifies the **shared** bandwidth ID to associate.
	// It's **mandatory** when you want to associate the ECS instance with a specified shared bandwidth.
	// Changing this creates a new resource.
	BandwidthId pulumi.StringPtrInput
	// Specifies the private IP address to direct traffic to. It's **mandatory**
	// and must be a valid IPv6 address when you want to associate the ECS instance with a specified shared bandwidth.
	// Changing this creates a new resource.
	FixedIp pulumi.StringPtrInput
	// Specifies the ID of ECS instance to associated with.
	// Changing this creates a new resource.
	InstanceId pulumi.StringPtrInput
	// The port ID of the ECS instance that associated with.
	PortId pulumi.StringPtrInput
	// Specifies the EIP address to associate. It's **mandatory**
	// when you want to associate the ECS instance with an EIP. Changing this creates a new resource.
	PublicIp pulumi.StringPtrInput
	// Specifies the region in which to create the associated resource.
	// If omitted, the provider-level region will be used. Changing this creates a new resource.
	Region pulumi.StringPtrInput
}

func (EipAssociateState) ElementType() reflect.Type {
	return reflect.TypeOf((*eipAssociateState)(nil)).Elem()
}

type eipAssociateArgs struct {
	// Specifies the **shared** bandwidth ID to associate.
	// It's **mandatory** when you want to associate the ECS instance with a specified shared bandwidth.
	// Changing this creates a new resource.
	BandwidthId *string `pulumi:"bandwidthId"`
	// Specifies the private IP address to direct traffic to. It's **mandatory**
	// and must be a valid IPv6 address when you want to associate the ECS instance with a specified shared bandwidth.
	// Changing this creates a new resource.
	FixedIp *string `pulumi:"fixedIp"`
	// Specifies the ID of ECS instance to associated with.
	// Changing this creates a new resource.
	InstanceId string `pulumi:"instanceId"`
	// Specifies the EIP address to associate. It's **mandatory**
	// when you want to associate the ECS instance with an EIP. Changing this creates a new resource.
	PublicIp *string `pulumi:"publicIp"`
	// Specifies the region in which to create the associated resource.
	// If omitted, the provider-level region will be used. Changing this creates a new resource.
	Region *string `pulumi:"region"`
}

// The set of arguments for constructing a EipAssociate resource.
type EipAssociateArgs struct {
	// Specifies the **shared** bandwidth ID to associate.
	// It's **mandatory** when you want to associate the ECS instance with a specified shared bandwidth.
	// Changing this creates a new resource.
	BandwidthId pulumi.StringPtrInput
	// Specifies the private IP address to direct traffic to. It's **mandatory**
	// and must be a valid IPv6 address when you want to associate the ECS instance with a specified shared bandwidth.
	// Changing this creates a new resource.
	FixedIp pulumi.StringPtrInput
	// Specifies the ID of ECS instance to associated with.
	// Changing this creates a new resource.
	InstanceId pulumi.StringInput
	// Specifies the EIP address to associate. It's **mandatory**
	// when you want to associate the ECS instance with an EIP. Changing this creates a new resource.
	PublicIp pulumi.StringPtrInput
	// Specifies the region in which to create the associated resource.
	// If omitted, the provider-level region will be used. Changing this creates a new resource.
	Region pulumi.StringPtrInput
}

func (EipAssociateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*eipAssociateArgs)(nil)).Elem()
}

type EipAssociateInput interface {
	pulumi.Input

	ToEipAssociateOutput() EipAssociateOutput
	ToEipAssociateOutputWithContext(ctx context.Context) EipAssociateOutput
}

func (*EipAssociate) ElementType() reflect.Type {
	return reflect.TypeOf((**EipAssociate)(nil)).Elem()
}

func (i *EipAssociate) ToEipAssociateOutput() EipAssociateOutput {
	return i.ToEipAssociateOutputWithContext(context.Background())
}

func (i *EipAssociate) ToEipAssociateOutputWithContext(ctx context.Context) EipAssociateOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EipAssociateOutput)
}

// EipAssociateArrayInput is an input type that accepts EipAssociateArray and EipAssociateArrayOutput values.
// You can construct a concrete instance of `EipAssociateArrayInput` via:
//
//	EipAssociateArray{ EipAssociateArgs{...} }
type EipAssociateArrayInput interface {
	pulumi.Input

	ToEipAssociateArrayOutput() EipAssociateArrayOutput
	ToEipAssociateArrayOutputWithContext(context.Context) EipAssociateArrayOutput
}

type EipAssociateArray []EipAssociateInput

func (EipAssociateArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*EipAssociate)(nil)).Elem()
}

func (i EipAssociateArray) ToEipAssociateArrayOutput() EipAssociateArrayOutput {
	return i.ToEipAssociateArrayOutputWithContext(context.Background())
}

func (i EipAssociateArray) ToEipAssociateArrayOutputWithContext(ctx context.Context) EipAssociateArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EipAssociateArrayOutput)
}

// EipAssociateMapInput is an input type that accepts EipAssociateMap and EipAssociateMapOutput values.
// You can construct a concrete instance of `EipAssociateMapInput` via:
//
//	EipAssociateMap{ "key": EipAssociateArgs{...} }
type EipAssociateMapInput interface {
	pulumi.Input

	ToEipAssociateMapOutput() EipAssociateMapOutput
	ToEipAssociateMapOutputWithContext(context.Context) EipAssociateMapOutput
}

type EipAssociateMap map[string]EipAssociateInput

func (EipAssociateMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*EipAssociate)(nil)).Elem()
}

func (i EipAssociateMap) ToEipAssociateMapOutput() EipAssociateMapOutput {
	return i.ToEipAssociateMapOutputWithContext(context.Background())
}

func (i EipAssociateMap) ToEipAssociateMapOutputWithContext(ctx context.Context) EipAssociateMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EipAssociateMapOutput)
}

type EipAssociateOutput struct{ *pulumi.OutputState }

func (EipAssociateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**EipAssociate)(nil)).Elem()
}

func (o EipAssociateOutput) ToEipAssociateOutput() EipAssociateOutput {
	return o
}

func (o EipAssociateOutput) ToEipAssociateOutputWithContext(ctx context.Context) EipAssociateOutput {
	return o
}

// Specifies the **shared** bandwidth ID to associate.
// It's **mandatory** when you want to associate the ECS instance with a specified shared bandwidth.
// Changing this creates a new resource.
func (o EipAssociateOutput) BandwidthId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *EipAssociate) pulumi.StringPtrOutput { return v.BandwidthId }).(pulumi.StringPtrOutput)
}

// Specifies the private IP address to direct traffic to. It's **mandatory**
// and must be a valid IPv6 address when you want to associate the ECS instance with a specified shared bandwidth.
// Changing this creates a new resource.
func (o EipAssociateOutput) FixedIp() pulumi.StringOutput {
	return o.ApplyT(func(v *EipAssociate) pulumi.StringOutput { return v.FixedIp }).(pulumi.StringOutput)
}

// Specifies the ID of ECS instance to associated with.
// Changing this creates a new resource.
func (o EipAssociateOutput) InstanceId() pulumi.StringOutput {
	return o.ApplyT(func(v *EipAssociate) pulumi.StringOutput { return v.InstanceId }).(pulumi.StringOutput)
}

// The port ID of the ECS instance that associated with.
func (o EipAssociateOutput) PortId() pulumi.StringOutput {
	return o.ApplyT(func(v *EipAssociate) pulumi.StringOutput { return v.PortId }).(pulumi.StringOutput)
}

// Specifies the EIP address to associate. It's **mandatory**
// when you want to associate the ECS instance with an EIP. Changing this creates a new resource.
func (o EipAssociateOutput) PublicIp() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *EipAssociate) pulumi.StringPtrOutput { return v.PublicIp }).(pulumi.StringPtrOutput)
}

// Specifies the region in which to create the associated resource.
// If omitted, the provider-level region will be used. Changing this creates a new resource.
func (o EipAssociateOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v *EipAssociate) pulumi.StringOutput { return v.Region }).(pulumi.StringOutput)
}

type EipAssociateArrayOutput struct{ *pulumi.OutputState }

func (EipAssociateArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*EipAssociate)(nil)).Elem()
}

func (o EipAssociateArrayOutput) ToEipAssociateArrayOutput() EipAssociateArrayOutput {
	return o
}

func (o EipAssociateArrayOutput) ToEipAssociateArrayOutputWithContext(ctx context.Context) EipAssociateArrayOutput {
	return o
}

func (o EipAssociateArrayOutput) Index(i pulumi.IntInput) EipAssociateOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *EipAssociate {
		return vs[0].([]*EipAssociate)[vs[1].(int)]
	}).(EipAssociateOutput)
}

type EipAssociateMapOutput struct{ *pulumi.OutputState }

func (EipAssociateMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*EipAssociate)(nil)).Elem()
}

func (o EipAssociateMapOutput) ToEipAssociateMapOutput() EipAssociateMapOutput {
	return o
}

func (o EipAssociateMapOutput) ToEipAssociateMapOutputWithContext(ctx context.Context) EipAssociateMapOutput {
	return o
}

func (o EipAssociateMapOutput) MapIndex(k pulumi.StringInput) EipAssociateOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *EipAssociate {
		return vs[0].(map[string]*EipAssociate)[vs[1].(string)]
	}).(EipAssociateOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*EipAssociateInput)(nil)).Elem(), &EipAssociate{})
	pulumi.RegisterInputType(reflect.TypeOf((*EipAssociateArrayInput)(nil)).Elem(), EipAssociateArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*EipAssociateMapInput)(nil)).Elem(), EipAssociateMap{})
	pulumi.RegisterOutputType(EipAssociateOutput{})
	pulumi.RegisterOutputType(EipAssociateArrayOutput{})
	pulumi.RegisterOutputType(EipAssociateMapOutput{})
}
