# Deskription

Deskription is a project for Kubernetes that defines how UIs should render Kubernetes
resources. Instead of hard-coding a table and a detail view for every resource kind,
a UI (console, dashboard, IDE plugin, CLI) reads **Deskription custom resources** that
describe how *other* resources should be displayed — and renders any kind, including
custom resources, from that description.

The definitions are themselves Kubernetes resources (API group `deskription.io`,
version `v1alpha1`), so they can be bundled with a UI as defaults *and* applied to a
cluster to extend or update the rendering at any time, without changing the UI:

| Kind | Purpose |
| --- | --- |
| `Resource` | Classifies a resource kind into a category (Workload, Storage, …) |
| `ResourceTable` | Columns a UI renders when listing resources of a kind |
| `ResourceDetails` | Fields a UI renders on the detail view of a single resource |

```yaml
apiVersion: deskription.io/v1alpha1
kind: ResourceTable
metadata:
  name: kubernetes-apps-v1-deployment
spec:
  selector:
    apiGroup: apps
    apiVersion: v1
    kind: Deployment
  columns:
    - name: Name
      path: metadata.name
    - name: Created
      type: datetime
      path: metadata.creationTimestamp
```

Definitions that match the same resource kind are merged: columns and fields override
by `name` or are appended, so an extension can add a single column without restating
the whole table.

## Documentation

* [Documentation](docs/README.md) — concepts, consumption model, and the full spec of
  all kinds
* [`schema/`](schema/) — JSON schemas for editor completion and validation
* [`definitions/`](definitions/) — the bundled default definitions, organized as
  `<distribution>/<group>/<version>/<Kind>.yaml`

Validate the definitions against the schemas with:

```sh
python3 scripts/validate.py
```

## Resource types

Every kind is classified by a `Resource` definition. The type is an open enum; known
values:

* `Workload` — Pods, Deployments, Jobs, Knative services, etc.
* `Storage` — PersistentVolumes, PersistentVolumeClaims, StorageClasses, etc.
* `Data` — ConfigMaps, Secrets
* `RBAC` — Users, Groups, ServiceAccounts, etc.
* `CICD` — workflows like Builds, Pipelines, ImageStreams, etc.
* `Compute` — Nodes, Machines, MachineConfigs, etc.
* `Network` — Services, Routes, Ingresses, etc.
* `Operators` — PackageManifests, Subscriptions, CatalogSources, etc.

## Bundled definitions

* **Kubernetes** ([Docs](https://kubernetes.io/docs/))
  * core
    * Nodes
    * Pods
    * PersistentVolumes
    * PersistentVolumeClaims
    * ReplicationControllers
    * ConfigMaps
    * Secrets
    * ServiceAccounts
  * batch
    * Jobs
    * CronJobs
  * apps
    * DaemonSets
    * Deployments
    * ReplicaSets
    * StatefulSets
  * autoscaling
    * HorizontalPodAutoscalers
  * policy
    * PodDisruptionBudgets
  * storage
    * StorageClasses
    * VolumeSnapshots
    * VolumeSnapshotClasses
    * VolumeSnapshotContents
* [Operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)
  * CatalogSources
  * ClusterServiceVersions
  * Subscriptions
  * PackageManifests
* [OpenShift](https://docs.openshift.com/)
  * apps
    * DeploymentConfigs
  * autoscaling
    * MachineAutoscalers
  * build
    * Builds
    * BuildConfigs
  * image
    * ImageStreams
    * ImageStreamTags
  * machine
    * Machines
    * MachineHealthChecks
    * MachineSets
  * machineconfiguration
    * MachineConfigs
    * MachineConfigPools
  * user
    * Users
    * Groups
* [Knative](https://knative.dev/)
  * [serving](https://knative.dev/docs/serving/)
    * Services
    * Revisions
    * Routes
* [Tekton](https://tekton.dev/)
  * core
    * Pipelines
    * PipelineRuns
    * ClusterTasks
    * Tasks
    * TaskRuns
* [Shipwright](https://shipwright.io/)
  * core
    * Builds
    * BuildRuns
