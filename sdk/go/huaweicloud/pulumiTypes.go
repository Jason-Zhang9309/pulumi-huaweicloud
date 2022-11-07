// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package huaweicloud

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type ProviderAssumeRole struct {
	AgencyName string `pulumi:"agencyName"`
	DomainName string `pulumi:"domainName"`
}

// ProviderAssumeRoleInput is an input type that accepts ProviderAssumeRoleArgs and ProviderAssumeRoleOutput values.
// You can construct a concrete instance of `ProviderAssumeRoleInput` via:
//
//	ProviderAssumeRoleArgs{...}
type ProviderAssumeRoleInput interface {
	pulumi.Input

	ToProviderAssumeRoleOutput() ProviderAssumeRoleOutput
	ToProviderAssumeRoleOutputWithContext(context.Context) ProviderAssumeRoleOutput
}

type ProviderAssumeRoleArgs struct {
	AgencyName pulumi.StringInput `pulumi:"agencyName"`
	DomainName pulumi.StringInput `pulumi:"domainName"`
}

func (ProviderAssumeRoleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ProviderAssumeRole)(nil)).Elem()
}

func (i ProviderAssumeRoleArgs) ToProviderAssumeRoleOutput() ProviderAssumeRoleOutput {
	return i.ToProviderAssumeRoleOutputWithContext(context.Background())
}

func (i ProviderAssumeRoleArgs) ToProviderAssumeRoleOutputWithContext(ctx context.Context) ProviderAssumeRoleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProviderAssumeRoleOutput)
}

func (i ProviderAssumeRoleArgs) ToProviderAssumeRolePtrOutput() ProviderAssumeRolePtrOutput {
	return i.ToProviderAssumeRolePtrOutputWithContext(context.Background())
}

func (i ProviderAssumeRoleArgs) ToProviderAssumeRolePtrOutputWithContext(ctx context.Context) ProviderAssumeRolePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProviderAssumeRoleOutput).ToProviderAssumeRolePtrOutputWithContext(ctx)
}

// ProviderAssumeRolePtrInput is an input type that accepts ProviderAssumeRoleArgs, ProviderAssumeRolePtr and ProviderAssumeRolePtrOutput values.
// You can construct a concrete instance of `ProviderAssumeRolePtrInput` via:
//
//	        ProviderAssumeRoleArgs{...}
//
//	or:
//
//	        nil
type ProviderAssumeRolePtrInput interface {
	pulumi.Input

	ToProviderAssumeRolePtrOutput() ProviderAssumeRolePtrOutput
	ToProviderAssumeRolePtrOutputWithContext(context.Context) ProviderAssumeRolePtrOutput
}

type providerAssumeRolePtrType ProviderAssumeRoleArgs

func ProviderAssumeRolePtr(v *ProviderAssumeRoleArgs) ProviderAssumeRolePtrInput {
	return (*providerAssumeRolePtrType)(v)
}

func (*providerAssumeRolePtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**ProviderAssumeRole)(nil)).Elem()
}

func (i *providerAssumeRolePtrType) ToProviderAssumeRolePtrOutput() ProviderAssumeRolePtrOutput {
	return i.ToProviderAssumeRolePtrOutputWithContext(context.Background())
}

func (i *providerAssumeRolePtrType) ToProviderAssumeRolePtrOutputWithContext(ctx context.Context) ProviderAssumeRolePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProviderAssumeRolePtrOutput)
}

type ProviderAssumeRoleOutput struct{ *pulumi.OutputState }

func (ProviderAssumeRoleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ProviderAssumeRole)(nil)).Elem()
}

func (o ProviderAssumeRoleOutput) ToProviderAssumeRoleOutput() ProviderAssumeRoleOutput {
	return o
}

func (o ProviderAssumeRoleOutput) ToProviderAssumeRoleOutputWithContext(ctx context.Context) ProviderAssumeRoleOutput {
	return o
}

func (o ProviderAssumeRoleOutput) ToProviderAssumeRolePtrOutput() ProviderAssumeRolePtrOutput {
	return o.ToProviderAssumeRolePtrOutputWithContext(context.Background())
}

func (o ProviderAssumeRoleOutput) ToProviderAssumeRolePtrOutputWithContext(ctx context.Context) ProviderAssumeRolePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v ProviderAssumeRole) *ProviderAssumeRole {
		return &v
	}).(ProviderAssumeRolePtrOutput)
}

func (o ProviderAssumeRoleOutput) AgencyName() pulumi.StringOutput {
	return o.ApplyT(func(v ProviderAssumeRole) string { return v.AgencyName }).(pulumi.StringOutput)
}

func (o ProviderAssumeRoleOutput) DomainName() pulumi.StringOutput {
	return o.ApplyT(func(v ProviderAssumeRole) string { return v.DomainName }).(pulumi.StringOutput)
}

type ProviderAssumeRolePtrOutput struct{ *pulumi.OutputState }

func (ProviderAssumeRolePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ProviderAssumeRole)(nil)).Elem()
}

func (o ProviderAssumeRolePtrOutput) ToProviderAssumeRolePtrOutput() ProviderAssumeRolePtrOutput {
	return o
}

func (o ProviderAssumeRolePtrOutput) ToProviderAssumeRolePtrOutputWithContext(ctx context.Context) ProviderAssumeRolePtrOutput {
	return o
}

func (o ProviderAssumeRolePtrOutput) Elem() ProviderAssumeRoleOutput {
	return o.ApplyT(func(v *ProviderAssumeRole) ProviderAssumeRole {
		if v != nil {
			return *v
		}
		var ret ProviderAssumeRole
		return ret
	}).(ProviderAssumeRoleOutput)
}

func (o ProviderAssumeRolePtrOutput) AgencyName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ProviderAssumeRole) *string {
		if v == nil {
			return nil
		}
		return &v.AgencyName
	}).(pulumi.StringPtrOutput)
}

func (o ProviderAssumeRolePtrOutput) DomainName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ProviderAssumeRole) *string {
		if v == nil {
			return nil
		}
		return &v.DomainName
	}).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ProviderAssumeRoleInput)(nil)).Elem(), ProviderAssumeRoleArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ProviderAssumeRolePtrInput)(nil)).Elem(), ProviderAssumeRoleArgs{})
	pulumi.RegisterOutputType(ProviderAssumeRoleOutput{})
	pulumi.RegisterOutputType(ProviderAssumeRolePtrOutput{})
}