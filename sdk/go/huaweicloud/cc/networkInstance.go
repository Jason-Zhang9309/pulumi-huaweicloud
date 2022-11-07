// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cc

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages a network instance resource within HuaweiCloud.
//
// Load VPCs or virtual gateways to the cloud connection. If you load virtual gateways, your on-premises data center
// can access multiple VPCs to build a hybrid cloud.
//
// Each network instance can be loaded onto only one cloud connection.
//
// ## Import
//
// The network instance can be imported using the `id`, e.g.
//
// ```sh
//
//	$ pulumi import huaweicloud:Cc/networkInstance:NetworkInstance test 0ce123456a00f2591fabc00385ff1234
//
// ```
type NetworkInstance struct {
	pulumi.CustomResourceState

	// List of routes advertised by the VPC or virtual gateway.
	Cidrs pulumi.StringArrayOutput `pulumi:"cidrs"`
	// Cloud connection ID.
	CloudConnectionId pulumi.StringOutput `pulumi:"cloudConnectionId"`
	// The description about the network instance.\
	// The description can contain a maximum of 255 characters.
	Description pulumi.StringOutput `pulumi:"description"`
	// Account ID.
	DomainId pulumi.StringOutput `pulumi:"domainId"`
	// Account ID of the VPC or virtual gateway.
	InstanceDomainId pulumi.StringOutput `pulumi:"instanceDomainId"`
	// ID of the VPC or virtual gateway to be loaded to the cloud connection.
	InstanceId pulumi.StringOutput `pulumi:"instanceId"`
	// The network instance name.\
	// The name can contain 1 to 64 characters, only letters, Chinese characters, digits, hyphens (-),
	// underscores (_) and dots (.).
	Name pulumi.StringOutput `pulumi:"name"`
	// Project ID of the VPC or virtual gateway.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
	// Specifies the region in which to create the resource.
	// If omitted, the provider-level region will be used. Changing this parameter will create a new resource.
	Region pulumi.StringOutput `pulumi:"region"`
	// Region ID of the VPC or virtual gateway.
	RegionId pulumi.StringOutput `pulumi:"regionId"`
	// Network instance status.\
	// The options are as follows:
	// + **ACTIVE**: The network instance is available.
	Status pulumi.StringOutput `pulumi:"status"`
	// Type of the network instance to be loaded to the cloud connection.\
	// The options are as follows:
	// + **vpc**: Virtual Private Cloud.
	// + **vgw**: virtual gateway.
	Type pulumi.StringOutput `pulumi:"type"`
}

// NewNetworkInstance registers a new resource with the given unique name, arguments, and options.
func NewNetworkInstance(ctx *pulumi.Context,
	name string, args *NetworkInstanceArgs, opts ...pulumi.ResourceOption) (*NetworkInstance, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Cidrs == nil {
		return nil, errors.New("invalid value for required argument 'Cidrs'")
	}
	if args.CloudConnectionId == nil {
		return nil, errors.New("invalid value for required argument 'CloudConnectionId'")
	}
	if args.InstanceId == nil {
		return nil, errors.New("invalid value for required argument 'InstanceId'")
	}
	if args.ProjectId == nil {
		return nil, errors.New("invalid value for required argument 'ProjectId'")
	}
	if args.RegionId == nil {
		return nil, errors.New("invalid value for required argument 'RegionId'")
	}
	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	var resource NetworkInstance
	err := ctx.RegisterResource("huaweicloud:Cc/networkInstance:NetworkInstance", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNetworkInstance gets an existing NetworkInstance resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNetworkInstance(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NetworkInstanceState, opts ...pulumi.ResourceOption) (*NetworkInstance, error) {
	var resource NetworkInstance
	err := ctx.ReadResource("huaweicloud:Cc/networkInstance:NetworkInstance", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering NetworkInstance resources.
type networkInstanceState struct {
	// List of routes advertised by the VPC or virtual gateway.
	Cidrs []string `pulumi:"cidrs"`
	// Cloud connection ID.
	CloudConnectionId *string `pulumi:"cloudConnectionId"`
	// The description about the network instance.\
	// The description can contain a maximum of 255 characters.
	Description *string `pulumi:"description"`
	// Account ID.
	DomainId *string `pulumi:"domainId"`
	// Account ID of the VPC or virtual gateway.
	InstanceDomainId *string `pulumi:"instanceDomainId"`
	// ID of the VPC or virtual gateway to be loaded to the cloud connection.
	InstanceId *string `pulumi:"instanceId"`
	// The network instance name.\
	// The name can contain 1 to 64 characters, only letters, Chinese characters, digits, hyphens (-),
	// underscores (_) and dots (.).
	Name *string `pulumi:"name"`
	// Project ID of the VPC or virtual gateway.
	ProjectId *string `pulumi:"projectId"`
	// Specifies the region in which to create the resource.
	// If omitted, the provider-level region will be used. Changing this parameter will create a new resource.
	Region *string `pulumi:"region"`
	// Region ID of the VPC or virtual gateway.
	RegionId *string `pulumi:"regionId"`
	// Network instance status.\
	// The options are as follows:
	// + **ACTIVE**: The network instance is available.
	Status *string `pulumi:"status"`
	// Type of the network instance to be loaded to the cloud connection.\
	// The options are as follows:
	// + **vpc**: Virtual Private Cloud.
	// + **vgw**: virtual gateway.
	Type *string `pulumi:"type"`
}

type NetworkInstanceState struct {
	// List of routes advertised by the VPC or virtual gateway.
	Cidrs pulumi.StringArrayInput
	// Cloud connection ID.
	CloudConnectionId pulumi.StringPtrInput
	// The description about the network instance.\
	// The description can contain a maximum of 255 characters.
	Description pulumi.StringPtrInput
	// Account ID.
	DomainId pulumi.StringPtrInput
	// Account ID of the VPC or virtual gateway.
	InstanceDomainId pulumi.StringPtrInput
	// ID of the VPC or virtual gateway to be loaded to the cloud connection.
	InstanceId pulumi.StringPtrInput
	// The network instance name.\
	// The name can contain 1 to 64 characters, only letters, Chinese characters, digits, hyphens (-),
	// underscores (_) and dots (.).
	Name pulumi.StringPtrInput
	// Project ID of the VPC or virtual gateway.
	ProjectId pulumi.StringPtrInput
	// Specifies the region in which to create the resource.
	// If omitted, the provider-level region will be used. Changing this parameter will create a new resource.
	Region pulumi.StringPtrInput
	// Region ID of the VPC or virtual gateway.
	RegionId pulumi.StringPtrInput
	// Network instance status.\
	// The options are as follows:
	// + **ACTIVE**: The network instance is available.
	Status pulumi.StringPtrInput
	// Type of the network instance to be loaded to the cloud connection.\
	// The options are as follows:
	// + **vpc**: Virtual Private Cloud.
	// + **vgw**: virtual gateway.
	Type pulumi.StringPtrInput
}

func (NetworkInstanceState) ElementType() reflect.Type {
	return reflect.TypeOf((*networkInstanceState)(nil)).Elem()
}

type networkInstanceArgs struct {
	// List of routes advertised by the VPC or virtual gateway.
	Cidrs []string `pulumi:"cidrs"`
	// Cloud connection ID.
	CloudConnectionId string `pulumi:"cloudConnectionId"`
	// The description about the network instance.\
	// The description can contain a maximum of 255 characters.
	Description *string `pulumi:"description"`
	// Account ID of the VPC or virtual gateway.
	InstanceDomainId *string `pulumi:"instanceDomainId"`
	// ID of the VPC or virtual gateway to be loaded to the cloud connection.
	InstanceId string `pulumi:"instanceId"`
	// The network instance name.\
	// The name can contain 1 to 64 characters, only letters, Chinese characters, digits, hyphens (-),
	// underscores (_) and dots (.).
	Name *string `pulumi:"name"`
	// Project ID of the VPC or virtual gateway.
	ProjectId string `pulumi:"projectId"`
	// Specifies the region in which to create the resource.
	// If omitted, the provider-level region will be used. Changing this parameter will create a new resource.
	Region *string `pulumi:"region"`
	// Region ID of the VPC or virtual gateway.
	RegionId string `pulumi:"regionId"`
	// Type of the network instance to be loaded to the cloud connection.\
	// The options are as follows:
	// + **vpc**: Virtual Private Cloud.
	// + **vgw**: virtual gateway.
	Type string `pulumi:"type"`
}

// The set of arguments for constructing a NetworkInstance resource.
type NetworkInstanceArgs struct {
	// List of routes advertised by the VPC or virtual gateway.
	Cidrs pulumi.StringArrayInput
	// Cloud connection ID.
	CloudConnectionId pulumi.StringInput
	// The description about the network instance.\
	// The description can contain a maximum of 255 characters.
	Description pulumi.StringPtrInput
	// Account ID of the VPC or virtual gateway.
	InstanceDomainId pulumi.StringPtrInput
	// ID of the VPC or virtual gateway to be loaded to the cloud connection.
	InstanceId pulumi.StringInput
	// The network instance name.\
	// The name can contain 1 to 64 characters, only letters, Chinese characters, digits, hyphens (-),
	// underscores (_) and dots (.).
	Name pulumi.StringPtrInput
	// Project ID of the VPC or virtual gateway.
	ProjectId pulumi.StringInput
	// Specifies the region in which to create the resource.
	// If omitted, the provider-level region will be used. Changing this parameter will create a new resource.
	Region pulumi.StringPtrInput
	// Region ID of the VPC or virtual gateway.
	RegionId pulumi.StringInput
	// Type of the network instance to be loaded to the cloud connection.\
	// The options are as follows:
	// + **vpc**: Virtual Private Cloud.
	// + **vgw**: virtual gateway.
	Type pulumi.StringInput
}

func (NetworkInstanceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*networkInstanceArgs)(nil)).Elem()
}

type NetworkInstanceInput interface {
	pulumi.Input

	ToNetworkInstanceOutput() NetworkInstanceOutput
	ToNetworkInstanceOutputWithContext(ctx context.Context) NetworkInstanceOutput
}

func (*NetworkInstance) ElementType() reflect.Type {
	return reflect.TypeOf((**NetworkInstance)(nil)).Elem()
}

func (i *NetworkInstance) ToNetworkInstanceOutput() NetworkInstanceOutput {
	return i.ToNetworkInstanceOutputWithContext(context.Background())
}

func (i *NetworkInstance) ToNetworkInstanceOutputWithContext(ctx context.Context) NetworkInstanceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkInstanceOutput)
}

// NetworkInstanceArrayInput is an input type that accepts NetworkInstanceArray and NetworkInstanceArrayOutput values.
// You can construct a concrete instance of `NetworkInstanceArrayInput` via:
//
//	NetworkInstanceArray{ NetworkInstanceArgs{...} }
type NetworkInstanceArrayInput interface {
	pulumi.Input

	ToNetworkInstanceArrayOutput() NetworkInstanceArrayOutput
	ToNetworkInstanceArrayOutputWithContext(context.Context) NetworkInstanceArrayOutput
}

type NetworkInstanceArray []NetworkInstanceInput

func (NetworkInstanceArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*NetworkInstance)(nil)).Elem()
}

func (i NetworkInstanceArray) ToNetworkInstanceArrayOutput() NetworkInstanceArrayOutput {
	return i.ToNetworkInstanceArrayOutputWithContext(context.Background())
}

func (i NetworkInstanceArray) ToNetworkInstanceArrayOutputWithContext(ctx context.Context) NetworkInstanceArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkInstanceArrayOutput)
}

// NetworkInstanceMapInput is an input type that accepts NetworkInstanceMap and NetworkInstanceMapOutput values.
// You can construct a concrete instance of `NetworkInstanceMapInput` via:
//
//	NetworkInstanceMap{ "key": NetworkInstanceArgs{...} }
type NetworkInstanceMapInput interface {
	pulumi.Input

	ToNetworkInstanceMapOutput() NetworkInstanceMapOutput
	ToNetworkInstanceMapOutputWithContext(context.Context) NetworkInstanceMapOutput
}

type NetworkInstanceMap map[string]NetworkInstanceInput

func (NetworkInstanceMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*NetworkInstance)(nil)).Elem()
}

func (i NetworkInstanceMap) ToNetworkInstanceMapOutput() NetworkInstanceMapOutput {
	return i.ToNetworkInstanceMapOutputWithContext(context.Background())
}

func (i NetworkInstanceMap) ToNetworkInstanceMapOutputWithContext(ctx context.Context) NetworkInstanceMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkInstanceMapOutput)
}

type NetworkInstanceOutput struct{ *pulumi.OutputState }

func (NetworkInstanceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**NetworkInstance)(nil)).Elem()
}

func (o NetworkInstanceOutput) ToNetworkInstanceOutput() NetworkInstanceOutput {
	return o
}

func (o NetworkInstanceOutput) ToNetworkInstanceOutputWithContext(ctx context.Context) NetworkInstanceOutput {
	return o
}

// List of routes advertised by the VPC or virtual gateway.
func (o NetworkInstanceOutput) Cidrs() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *NetworkInstance) pulumi.StringArrayOutput { return v.Cidrs }).(pulumi.StringArrayOutput)
}

// Cloud connection ID.
func (o NetworkInstanceOutput) CloudConnectionId() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkInstance) pulumi.StringOutput { return v.CloudConnectionId }).(pulumi.StringOutput)
}

// The description about the network instance.\
// The description can contain a maximum of 255 characters.
func (o NetworkInstanceOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkInstance) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// Account ID.
func (o NetworkInstanceOutput) DomainId() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkInstance) pulumi.StringOutput { return v.DomainId }).(pulumi.StringOutput)
}

// Account ID of the VPC or virtual gateway.
func (o NetworkInstanceOutput) InstanceDomainId() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkInstance) pulumi.StringOutput { return v.InstanceDomainId }).(pulumi.StringOutput)
}

// ID of the VPC or virtual gateway to be loaded to the cloud connection.
func (o NetworkInstanceOutput) InstanceId() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkInstance) pulumi.StringOutput { return v.InstanceId }).(pulumi.StringOutput)
}

// The network instance name.\
// The name can contain 1 to 64 characters, only letters, Chinese characters, digits, hyphens (-),
// underscores (_) and dots (.).
func (o NetworkInstanceOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkInstance) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Project ID of the VPC or virtual gateway.
func (o NetworkInstanceOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkInstance) pulumi.StringOutput { return v.ProjectId }).(pulumi.StringOutput)
}

// Specifies the region in which to create the resource.
// If omitted, the provider-level region will be used. Changing this parameter will create a new resource.
func (o NetworkInstanceOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkInstance) pulumi.StringOutput { return v.Region }).(pulumi.StringOutput)
}

// Region ID of the VPC or virtual gateway.
func (o NetworkInstanceOutput) RegionId() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkInstance) pulumi.StringOutput { return v.RegionId }).(pulumi.StringOutput)
}

// Network instance status.\
// The options are as follows:
// + **ACTIVE**: The network instance is available.
func (o NetworkInstanceOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkInstance) pulumi.StringOutput { return v.Status }).(pulumi.StringOutput)
}

// Type of the network instance to be loaded to the cloud connection.\
// The options are as follows:
// + **vpc**: Virtual Private Cloud.
// + **vgw**: virtual gateway.
func (o NetworkInstanceOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkInstance) pulumi.StringOutput { return v.Type }).(pulumi.StringOutput)
}

type NetworkInstanceArrayOutput struct{ *pulumi.OutputState }

func (NetworkInstanceArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*NetworkInstance)(nil)).Elem()
}

func (o NetworkInstanceArrayOutput) ToNetworkInstanceArrayOutput() NetworkInstanceArrayOutput {
	return o
}

func (o NetworkInstanceArrayOutput) ToNetworkInstanceArrayOutputWithContext(ctx context.Context) NetworkInstanceArrayOutput {
	return o
}

func (o NetworkInstanceArrayOutput) Index(i pulumi.IntInput) NetworkInstanceOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *NetworkInstance {
		return vs[0].([]*NetworkInstance)[vs[1].(int)]
	}).(NetworkInstanceOutput)
}

type NetworkInstanceMapOutput struct{ *pulumi.OutputState }

func (NetworkInstanceMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*NetworkInstance)(nil)).Elem()
}

func (o NetworkInstanceMapOutput) ToNetworkInstanceMapOutput() NetworkInstanceMapOutput {
	return o
}

func (o NetworkInstanceMapOutput) ToNetworkInstanceMapOutputWithContext(ctx context.Context) NetworkInstanceMapOutput {
	return o
}

func (o NetworkInstanceMapOutput) MapIndex(k pulumi.StringInput) NetworkInstanceOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *NetworkInstance {
		return vs[0].(map[string]*NetworkInstance)[vs[1].(string)]
	}).(NetworkInstanceOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkInstanceInput)(nil)).Elem(), &NetworkInstance{})
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkInstanceArrayInput)(nil)).Elem(), NetworkInstanceArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkInstanceMapInput)(nil)).Elem(), NetworkInstanceMap{})
	pulumi.RegisterOutputType(NetworkInstanceOutput{})
	pulumi.RegisterOutputType(NetworkInstanceArrayOutput{})
	pulumi.RegisterOutputType(NetworkInstanceMapOutput{})
}