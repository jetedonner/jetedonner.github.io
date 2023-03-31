---
layout: post
title:  "Unreal Engine - Snippets"
author: dave
date:   2023-03-31 22:13:04 +0200
categories: UnrealEngine Snippets
tags: [UnrealEngine, Snippets]
published: true
---

![UE code snippets on blueprintue.com](../../assets/img/projects/ue/UE-Code-Snippets-On-blueprintue_com.png){: width="444" height="462" }
_UE Code snippets on blueprintue.com_


# Unreal Engine Snippets
This page shows some - maybe - usefull code and Blueprint snippets for the Unreal Engine
- [_Unreal Engine Snippets on blueprintue.com by DaVe_](https://blueprintue.com/profile/jetedonner/){:target="_blank" rel="noopener"}

## Portal Helper-Functions
This functions can help you with the calcualtions needed for teleporting Actors like Characters or Bullets through Teleportation-Portals. The snippets are hosted on [blueprintue.com](https://blueprintue.com/profile/jetedonner/){:target="_blank" rel="noopener"} and created by me with the help of [wiki.unrealengine.com](https://michaeljcole.github.io/wiki.unrealengine.com/Simple_Portals/#Overview){:target="_blank" rel="noopener"}

### PortalConvertDirection
This UE5.1 Blueprint Function is meant for Portal pairs to convert a input direction from the current portal to the traget portal.

<iframe src="https://blueprintue.com/render/schzg-gp/" scrolling="no" width="100%" height="640" allowfullscreen></iframe>

- [PortalConvertDirection on blueprintue.com](https://blueprintue.com/blueprint/schzg-gp/){:target="_blank" rel="noopener"}

#### PortalConvertDirection - C++ Sourcecode

```c++
FVector UPortalFunctionLibrary::PortalConvertDirection(ATeleporterPortalBaseActor* CurrentPortal, ATeleporterPortalBaseActor* TargetPortal, FVector PrevDirection)
{
    FTransform CurrentActorTransform = CurrentPortal->GetActorTransform();
	FTransform TargetActorTransform = TargetPortal->GetActorTransform();


    FVector InversedTransformDirection = UKismetMathLibrary::InverseTransformDirection(CurrentActorTransform, PrevDirection);
    FVector MirroredDirection = UKismetMathLibrary::MirrorVectorByNormal(UKismetMathLibrary::MirrorVectorByNormal(InversedTransformDirection, FVector(1, 0, 0)), FVector(0, 1, 0));
    return UKismetMathLibrary::TransformDirection(TargetActorTransform, MirroredDirection);
}
```


### PortalConvertLocation
This UE5.1 Blueprint Function is meant for Portal pairs to convert a input location from the current portal to the traget portal.

<iframe src="https://blueprintue.com/render/px7---nm/" scrolling="no" width="100%" height="640" allowfullscreen></iframe>

- [PortalConvertLocation on blueprintue.com](https://blueprintue.com/blueprint/px7---nm/){:target="_blank" rel="noopener"}

#### PortalConvertLocation - C++ Sourcecode

```c++
FVector UPortalFunctionLibrary::PortalConvertLocation(ATeleporterPortalBaseActor* CurrentPortal, ATeleporterPortalBaseActor* TargetPortal, FVector PrevLocation)
{
    FTransform CurrentActorTransform = CurrentPortal->GetActorTransform();
	FTransform TargetActorTransform = TargetPortal->GetActorTransform();

    FTransform NewTransform = FTransform(CurrentActorTransform.GetRotation(), CurrentActorTransform.GetTranslation(), FVector(CurrentActorTransform.GetTranslation().X * -1, CurrentActorTransform.GetTranslation().Y * -1, CurrentActorTransform.GetTranslation().Z));

    FVector InversedTransformLocation = UKismetMathLibrary::InverseTransformLocation(NewTransform, PrevLocation);
    return UKismetMathLibrary::TransformLocation(TargetActorTransform, InversedTransformLocation);
}
```


### PortalConvertMirroredLocation
This UE5.1 Blueprint Function is meant for Portal pairs to convert a input location from the current portal mirrored to the traget portal.

<iframe src="https://blueprintue.com/render/py9v4574/" scrolling="no" width="100%" height="640" allowfullscreen></iframe>

- [PortalConvertMirroredLocation on blueprintue.com](https://blueprintue.com/blueprint/py9v4574/){:target="_blank" rel="noopener"}

#### PortalConvertMirroredLocation - C++ Sourcecode

```c++
FVector UPortalFunctionLibrary::PortalConvertLocationMirrored(ATeleporterPortalBaseActor* CurrentPortal, ATeleporterPortalBaseActor* TargetPortal, FVector PrevLocation)
{
    FTransform CurrentActorTransform = CurrentPortal->GetActorTransform();
	FTransform TargetActorTransform = TargetPortal->GetActorTransform();

    FTransform NewTransform = FTransform(CurrentActorTransform.GetRotation(), CurrentActorTransform.GetTranslation(), FVector(CurrentActorTransform.GetTranslation().X, CurrentActorTransform.GetTranslation().Y * -1, CurrentActorTransform.GetTranslation().Z));
    FVector InversedTransformLocation = UKismetMathLibrary::InverseTransformLocation(NewTransform, PrevLocation);

    return UKismetMathLibrary::TransformLocation(TargetActorTransform, InversedTransformLocation);
}
```


### PortalConvertRotation
This UE5.1 Blueprint Function is meant for Portal pairs to convert a input rotation from the current portal to the traget portal.

<iframe src="https://blueprintue.com/render/rbaz1sm6/" scrolling="no" width="100%" height="640" allowfullscreen></iframe>

- [PortalConvertRotation on blueprintue.com](https://blueprintue.com/blueprint/rbaz1sm6/){:target="_blank" rel="noopener"}

#### PortalConvertRotation - C++ Sourcecode

```c++
FRotator UPortalFunctionLibrary::PortalConvertRotation(ATeleporterPortalBaseActor* CurrentPortal, ATeleporterPortalBaseActor* TargetPortal, FRotator PrevRotation)
{
    FVector X;
    FVector Y;
    FVector Z;

    UKismetMathLibrary::GetAxes(PrevRotation, X, Y, Z);

    FVector DirX = UPortalFunctionLibrary::PortalConvertDirection(CurrentPortal, TargetPortal, X);
    FVector DirY = UPortalFunctionLibrary::PortalConvertDirection(CurrentPortal, TargetPortal, Y);
    
    return UKismetMathLibrary::MakeRotFromXY(X, Y);
}
```


### PortalConvertVelocity
This UE5.1 Blueprint Function is meant for Portal pairs to convert a input velocity from the current portal to the traget portal.

<iframe src="https://blueprintue.com/render/i44d0_gg/" scrolling="no" width="100%" height="640" allowfullscreen></iframe>

- [PortalConvertVelocity on blueprintue.com](https://blueprintue.com/blueprint/i44d0_gg/){:target="_blank" rel="noopener"}

#### PortalConvertVelocity - C++ Sourcecode

```c++
FVector UPortalFunctionLibrary::PortalConvertVelocity(ATeleporterPortalBaseActor* CurrentPortal, ATeleporterPortalBaseActor* TargetPortal, FVector PrevVelocity)
{
    PrevVelocity.Normalize();
    FVector VelocityDir = UPortalFunctionLibrary::PortalConvertDirection(CurrentPortal, TargetPortal, PrevVelocity);
    return VelocityDir * PrevVelocity.Length();
}
```
