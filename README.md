# Deskription

## Definitions

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
  * Autoscaling
    * HorizontalPodAutoscalers
  * policy
    * PodDisruptionBudget
  * storage
    * StorageClass
    * VolumeSnapshot
    * VolumeSnapshotClass
    * VolumeSnapshotContent
* [Operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)
  * CatalogSources
  * ClusterServiceVersions
  * Subscriptions
  * PackageManifests
* [OpenShift](https://docs.openshift.com/)
  * apps
    * DeploymentConfigs
  * autoscaling
    * MachineAutoscaler
  * build
    * Builds
    * BuildRuns
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
    * Service
    * Revision
    * Route
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

## Resource types:

* Workload (Pods, Deployments, etc.)
* Storage (PV, PVC, etc.)
* RBAC (Users, Groups, ServiceAccounts, etc.)
* CI/CD (Workflows like Builds, Pipelines, etc.)
* Compute (Nodes, etc.)
* Network
* Operator (Packages, Subscriptions, etc.)
