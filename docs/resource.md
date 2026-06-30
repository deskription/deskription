# Resource

`Resource` classifies a Kubernetes resource kind into a category. UIs use the category
to group kinds in navigation, search filters, and overview pages.

```yaml
apiVersion: deskription.io/v1alpha1
kind: Resource
metadata:
  name: kubernetes-apps-v1-deployment
spec:
  selector:
    apiGroup: apps
    apiVersion: v1
    kind: Deployment
  type: Workload
```

## Spec

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `selector` | object | yes | The resource kind this definition applies to, see [Selectors](concepts.md#selectors) |
| `selector.apiGroup` | string | yes | API group; `core` or `""` for the core group |
| `selector.apiVersion` | string | yes | API version, e.g. `v1` |
| `selector.kind` | string | yes | Kind, e.g. `Deployment` |
| `type` | string | yes | Category of the resource kind |

## Types

`type` is an **open enum**: any string is allowed, so new categories never require a
spec change. UIs should treat unknown values as their own category. The known values
are:

| Type | Used for |
| --- | --- |
| `Workload` | Pods, Deployments, Jobs, Knative services, … |
| `Storage` | PersistentVolumes, PersistentVolumeClaims, StorageClasses, VolumeSnapshots, … |
| `Data` | ConfigMaps, Secrets |
| `RBAC` | Users, Groups, ServiceAccounts, … |
| `CICD` | Workflows like Builds, Pipelines, ImageStreams, … |
| `Compute` | Nodes, Machines, MachineSets, MachineConfigs, … |
| `Network` | Services, Routes, Ingresses, … |
| `Operators` | PackageManifests, Subscriptions, CatalogSources, ClusterServiceVersions, … |

If several `Resource` definitions match the same selector, the last one loaded wins
(see [Merging](concepts.md#merging)).

## Schema

[`schema/resource.schema.json`](../schema/resource.schema.json)
