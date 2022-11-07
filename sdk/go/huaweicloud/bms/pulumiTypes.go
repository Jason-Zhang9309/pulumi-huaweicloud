// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package bms

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type InstanceDataDisk struct {
	// Specifies the data disk size, in GB. The value ranges form 10 to 32768. Changing
	// this creates a new instance.
	Size int `pulumi:"size"`
	// Specifies the BMS data disk type, which must be one of available disk types,
	// contains of *SSD*, *GPSSD* and *SAS*. Changing this creates a new instance.
	Type string `pulumi:"type"`
}

// InstanceDataDiskInput is an input type that accepts InstanceDataDiskArgs and InstanceDataDiskOutput values.
// You can construct a concrete instance of `InstanceDataDiskInput` via:
//
//	InstanceDataDiskArgs{...}
type InstanceDataDiskInput interface {
	pulumi.Input

	ToInstanceDataDiskOutput() InstanceDataDiskOutput
	ToInstanceDataDiskOutputWithContext(context.Context) InstanceDataDiskOutput
}

type InstanceDataDiskArgs struct {
	// Specifies the data disk size, in GB. The value ranges form 10 to 32768. Changing
	// this creates a new instance.
	Size pulumi.IntInput `pulumi:"size"`
	// Specifies the BMS data disk type, which must be one of available disk types,
	// contains of *SSD*, *GPSSD* and *SAS*. Changing this creates a new instance.
	Type pulumi.StringInput `pulumi:"type"`
}

func (InstanceDataDiskArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*InstanceDataDisk)(nil)).Elem()
}

func (i InstanceDataDiskArgs) ToInstanceDataDiskOutput() InstanceDataDiskOutput {
	return i.ToInstanceDataDiskOutputWithContext(context.Background())
}

func (i InstanceDataDiskArgs) ToInstanceDataDiskOutputWithContext(ctx context.Context) InstanceDataDiskOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceDataDiskOutput)
}

// InstanceDataDiskArrayInput is an input type that accepts InstanceDataDiskArray and InstanceDataDiskArrayOutput values.
// You can construct a concrete instance of `InstanceDataDiskArrayInput` via:
//
//	InstanceDataDiskArray{ InstanceDataDiskArgs{...} }
type InstanceDataDiskArrayInput interface {
	pulumi.Input

	ToInstanceDataDiskArrayOutput() InstanceDataDiskArrayOutput
	ToInstanceDataDiskArrayOutputWithContext(context.Context) InstanceDataDiskArrayOutput
}

type InstanceDataDiskArray []InstanceDataDiskInput

func (InstanceDataDiskArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]InstanceDataDisk)(nil)).Elem()
}

func (i InstanceDataDiskArray) ToInstanceDataDiskArrayOutput() InstanceDataDiskArrayOutput {
	return i.ToInstanceDataDiskArrayOutputWithContext(context.Background())
}

func (i InstanceDataDiskArray) ToInstanceDataDiskArrayOutputWithContext(ctx context.Context) InstanceDataDiskArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceDataDiskArrayOutput)
}

type InstanceDataDiskOutput struct{ *pulumi.OutputState }

func (InstanceDataDiskOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*InstanceDataDisk)(nil)).Elem()
}

func (o InstanceDataDiskOutput) ToInstanceDataDiskOutput() InstanceDataDiskOutput {
	return o
}

func (o InstanceDataDiskOutput) ToInstanceDataDiskOutputWithContext(ctx context.Context) InstanceDataDiskOutput {
	return o
}

// Specifies the data disk size, in GB. The value ranges form 10 to 32768. Changing
// this creates a new instance.
func (o InstanceDataDiskOutput) Size() pulumi.IntOutput {
	return o.ApplyT(func(v InstanceDataDisk) int { return v.Size }).(pulumi.IntOutput)
}

// Specifies the BMS data disk type, which must be one of available disk types,
// contains of *SSD*, *GPSSD* and *SAS*. Changing this creates a new instance.
func (o InstanceDataDiskOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v InstanceDataDisk) string { return v.Type }).(pulumi.StringOutput)
}

type InstanceDataDiskArrayOutput struct{ *pulumi.OutputState }

func (InstanceDataDiskArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]InstanceDataDisk)(nil)).Elem()
}

func (o InstanceDataDiskArrayOutput) ToInstanceDataDiskArrayOutput() InstanceDataDiskArrayOutput {
	return o
}

func (o InstanceDataDiskArrayOutput) ToInstanceDataDiskArrayOutputWithContext(ctx context.Context) InstanceDataDiskArrayOutput {
	return o
}

func (o InstanceDataDiskArrayOutput) Index(i pulumi.IntInput) InstanceDataDiskOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) InstanceDataDisk {
		return vs[0].([]InstanceDataDisk)[vs[1].(int)]
	}).(InstanceDataDiskOutput)
}

type InstanceNic struct {
	// Specifies a fixed IPv4 address to be used on this network. Changing this
	// creates a new instance.
	IpAddress  *string `pulumi:"ipAddress"`
	MacAddress *string `pulumi:"macAddress"`
	PortId     *string `pulumi:"portId"`
	// Specifies the ID of subnet to attach to the instance. Changing this creates
	// a new instance.
	SubnetId string `pulumi:"subnetId"`
}

// InstanceNicInput is an input type that accepts InstanceNicArgs and InstanceNicOutput values.
// You can construct a concrete instance of `InstanceNicInput` via:
//
//	InstanceNicArgs{...}
type InstanceNicInput interface {
	pulumi.Input

	ToInstanceNicOutput() InstanceNicOutput
	ToInstanceNicOutputWithContext(context.Context) InstanceNicOutput
}

type InstanceNicArgs struct {
	// Specifies a fixed IPv4 address to be used on this network. Changing this
	// creates a new instance.
	IpAddress  pulumi.StringPtrInput `pulumi:"ipAddress"`
	MacAddress pulumi.StringPtrInput `pulumi:"macAddress"`
	PortId     pulumi.StringPtrInput `pulumi:"portId"`
	// Specifies the ID of subnet to attach to the instance. Changing this creates
	// a new instance.
	SubnetId pulumi.StringInput `pulumi:"subnetId"`
}

func (InstanceNicArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*InstanceNic)(nil)).Elem()
}

func (i InstanceNicArgs) ToInstanceNicOutput() InstanceNicOutput {
	return i.ToInstanceNicOutputWithContext(context.Background())
}

func (i InstanceNicArgs) ToInstanceNicOutputWithContext(ctx context.Context) InstanceNicOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceNicOutput)
}

// InstanceNicArrayInput is an input type that accepts InstanceNicArray and InstanceNicArrayOutput values.
// You can construct a concrete instance of `InstanceNicArrayInput` via:
//
//	InstanceNicArray{ InstanceNicArgs{...} }
type InstanceNicArrayInput interface {
	pulumi.Input

	ToInstanceNicArrayOutput() InstanceNicArrayOutput
	ToInstanceNicArrayOutputWithContext(context.Context) InstanceNicArrayOutput
}

type InstanceNicArray []InstanceNicInput

func (InstanceNicArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]InstanceNic)(nil)).Elem()
}

func (i InstanceNicArray) ToInstanceNicArrayOutput() InstanceNicArrayOutput {
	return i.ToInstanceNicArrayOutputWithContext(context.Background())
}

func (i InstanceNicArray) ToInstanceNicArrayOutputWithContext(ctx context.Context) InstanceNicArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceNicArrayOutput)
}

type InstanceNicOutput struct{ *pulumi.OutputState }

func (InstanceNicOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*InstanceNic)(nil)).Elem()
}

func (o InstanceNicOutput) ToInstanceNicOutput() InstanceNicOutput {
	return o
}

func (o InstanceNicOutput) ToInstanceNicOutputWithContext(ctx context.Context) InstanceNicOutput {
	return o
}

// Specifies a fixed IPv4 address to be used on this network. Changing this
// creates a new instance.
func (o InstanceNicOutput) IpAddress() pulumi.StringPtrOutput {
	return o.ApplyT(func(v InstanceNic) *string { return v.IpAddress }).(pulumi.StringPtrOutput)
}

func (o InstanceNicOutput) MacAddress() pulumi.StringPtrOutput {
	return o.ApplyT(func(v InstanceNic) *string { return v.MacAddress }).(pulumi.StringPtrOutput)
}

func (o InstanceNicOutput) PortId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v InstanceNic) *string { return v.PortId }).(pulumi.StringPtrOutput)
}

// Specifies the ID of subnet to attach to the instance. Changing this creates
// a new instance.
func (o InstanceNicOutput) SubnetId() pulumi.StringOutput {
	return o.ApplyT(func(v InstanceNic) string { return v.SubnetId }).(pulumi.StringOutput)
}

type InstanceNicArrayOutput struct{ *pulumi.OutputState }

func (InstanceNicArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]InstanceNic)(nil)).Elem()
}

func (o InstanceNicArrayOutput) ToInstanceNicArrayOutput() InstanceNicArrayOutput {
	return o
}

func (o InstanceNicArrayOutput) ToInstanceNicArrayOutputWithContext(ctx context.Context) InstanceNicArrayOutput {
	return o
}

func (o InstanceNicArrayOutput) Index(i pulumi.IntInput) InstanceNicOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) InstanceNic {
		return vs[0].([]InstanceNic)[vs[1].(int)]
	}).(InstanceNicOutput)
}

type GetFlavorsFlavor struct {
	// Specifies the CPU architecture of the BMS flavor.
	// The value can be x8664 and aarch64, defaults to **x86_64**.
	CpuArch string `pulumi:"cpuArch"`
	// The id or name of the BMS flavor.
	Id string `pulumi:"id"`
	// Specifies the memory size(GB) in the BMS flavor.
	Memory int `pulumi:"memory"`
	// The operation status of the BMS flavor in an each AZs.
	Operation string `pulumi:"operation"`
	// Specifies the number of vCPUs in the BMS flavor.
	Vcpus int `pulumi:"vcpus"`
}

// GetFlavorsFlavorInput is an input type that accepts GetFlavorsFlavorArgs and GetFlavorsFlavorOutput values.
// You can construct a concrete instance of `GetFlavorsFlavorInput` via:
//
//	GetFlavorsFlavorArgs{...}
type GetFlavorsFlavorInput interface {
	pulumi.Input

	ToGetFlavorsFlavorOutput() GetFlavorsFlavorOutput
	ToGetFlavorsFlavorOutputWithContext(context.Context) GetFlavorsFlavorOutput
}

type GetFlavorsFlavorArgs struct {
	// Specifies the CPU architecture of the BMS flavor.
	// The value can be x8664 and aarch64, defaults to **x86_64**.
	CpuArch pulumi.StringInput `pulumi:"cpuArch"`
	// The id or name of the BMS flavor.
	Id pulumi.StringInput `pulumi:"id"`
	// Specifies the memory size(GB) in the BMS flavor.
	Memory pulumi.IntInput `pulumi:"memory"`
	// The operation status of the BMS flavor in an each AZs.
	Operation pulumi.StringInput `pulumi:"operation"`
	// Specifies the number of vCPUs in the BMS flavor.
	Vcpus pulumi.IntInput `pulumi:"vcpus"`
}

func (GetFlavorsFlavorArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetFlavorsFlavor)(nil)).Elem()
}

func (i GetFlavorsFlavorArgs) ToGetFlavorsFlavorOutput() GetFlavorsFlavorOutput {
	return i.ToGetFlavorsFlavorOutputWithContext(context.Background())
}

func (i GetFlavorsFlavorArgs) ToGetFlavorsFlavorOutputWithContext(ctx context.Context) GetFlavorsFlavorOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetFlavorsFlavorOutput)
}

// GetFlavorsFlavorArrayInput is an input type that accepts GetFlavorsFlavorArray and GetFlavorsFlavorArrayOutput values.
// You can construct a concrete instance of `GetFlavorsFlavorArrayInput` via:
//
//	GetFlavorsFlavorArray{ GetFlavorsFlavorArgs{...} }
type GetFlavorsFlavorArrayInput interface {
	pulumi.Input

	ToGetFlavorsFlavorArrayOutput() GetFlavorsFlavorArrayOutput
	ToGetFlavorsFlavorArrayOutputWithContext(context.Context) GetFlavorsFlavorArrayOutput
}

type GetFlavorsFlavorArray []GetFlavorsFlavorInput

func (GetFlavorsFlavorArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetFlavorsFlavor)(nil)).Elem()
}

func (i GetFlavorsFlavorArray) ToGetFlavorsFlavorArrayOutput() GetFlavorsFlavorArrayOutput {
	return i.ToGetFlavorsFlavorArrayOutputWithContext(context.Background())
}

func (i GetFlavorsFlavorArray) ToGetFlavorsFlavorArrayOutputWithContext(ctx context.Context) GetFlavorsFlavorArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetFlavorsFlavorArrayOutput)
}

type GetFlavorsFlavorOutput struct{ *pulumi.OutputState }

func (GetFlavorsFlavorOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetFlavorsFlavor)(nil)).Elem()
}

func (o GetFlavorsFlavorOutput) ToGetFlavorsFlavorOutput() GetFlavorsFlavorOutput {
	return o
}

func (o GetFlavorsFlavorOutput) ToGetFlavorsFlavorOutputWithContext(ctx context.Context) GetFlavorsFlavorOutput {
	return o
}

// Specifies the CPU architecture of the BMS flavor.
// The value can be x8664 and aarch64, defaults to **x86_64**.
func (o GetFlavorsFlavorOutput) CpuArch() pulumi.StringOutput {
	return o.ApplyT(func(v GetFlavorsFlavor) string { return v.CpuArch }).(pulumi.StringOutput)
}

// The id or name of the BMS flavor.
func (o GetFlavorsFlavorOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetFlavorsFlavor) string { return v.Id }).(pulumi.StringOutput)
}

// Specifies the memory size(GB) in the BMS flavor.
func (o GetFlavorsFlavorOutput) Memory() pulumi.IntOutput {
	return o.ApplyT(func(v GetFlavorsFlavor) int { return v.Memory }).(pulumi.IntOutput)
}

// The operation status of the BMS flavor in an each AZs.
func (o GetFlavorsFlavorOutput) Operation() pulumi.StringOutput {
	return o.ApplyT(func(v GetFlavorsFlavor) string { return v.Operation }).(pulumi.StringOutput)
}

// Specifies the number of vCPUs in the BMS flavor.
func (o GetFlavorsFlavorOutput) Vcpus() pulumi.IntOutput {
	return o.ApplyT(func(v GetFlavorsFlavor) int { return v.Vcpus }).(pulumi.IntOutput)
}

type GetFlavorsFlavorArrayOutput struct{ *pulumi.OutputState }

func (GetFlavorsFlavorArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetFlavorsFlavor)(nil)).Elem()
}

func (o GetFlavorsFlavorArrayOutput) ToGetFlavorsFlavorArrayOutput() GetFlavorsFlavorArrayOutput {
	return o
}

func (o GetFlavorsFlavorArrayOutput) ToGetFlavorsFlavorArrayOutputWithContext(ctx context.Context) GetFlavorsFlavorArrayOutput {
	return o
}

func (o GetFlavorsFlavorArrayOutput) Index(i pulumi.IntInput) GetFlavorsFlavorOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) GetFlavorsFlavor {
		return vs[0].([]GetFlavorsFlavor)[vs[1].(int)]
	}).(GetFlavorsFlavorOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*InstanceDataDiskInput)(nil)).Elem(), InstanceDataDiskArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*InstanceDataDiskArrayInput)(nil)).Elem(), InstanceDataDiskArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*InstanceNicInput)(nil)).Elem(), InstanceNicArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*InstanceNicArrayInput)(nil)).Elem(), InstanceNicArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetFlavorsFlavorInput)(nil)).Elem(), GetFlavorsFlavorArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetFlavorsFlavorArrayInput)(nil)).Elem(), GetFlavorsFlavorArray{})
	pulumi.RegisterOutputType(InstanceDataDiskOutput{})
	pulumi.RegisterOutputType(InstanceDataDiskArrayOutput{})
	pulumi.RegisterOutputType(InstanceNicOutput{})
	pulumi.RegisterOutputType(InstanceNicArrayOutput{})
	pulumi.RegisterOutputType(GetFlavorsFlavorOutput{})
	pulumi.RegisterOutputType(GetFlavorsFlavorArrayOutput{})
}