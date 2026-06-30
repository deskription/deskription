# Concepts

## What Deskription is

Kubernetes UIs (consoles, dashboards, IDE plugins) traditionally hard-code how each
resource kind is listed and displayed. Every new CRD needs new UI code. Deskription
turns this into data: small Kubernetes resources that *describe* how other resources
should be rendered. A renderer that understands the three Deskription kinds can display
any resource kind — core Kubernetes, OpenShift, Tekton, Knative, Shipwright, operators,
or your own CRDs — and can be extended by simply adding more definitions.

All Deskription kinds live in the API group `deskription.io`, currently at version
`v1alpha1`:

| Kind | Purpose |
| --- | --- |
| [`Resource`](resource.md) | Classifies a resource kind into a category (Workload, Storage, …) |
| [`ResourceTable`](resource-table.md) | Columns a UI renders when listing resources of a kind |
| [`ResourceDetails`](resource-details.md) | Fields a UI renders on the detail view of a single resource |

## How definitions are consumed

Definitions are consumed in two ways, and both can be combined:

1. **Bundled defaults.** UIs ship the YAML files from this repository's
   [`definitions/`](../definitions/) folder as built-in configuration.
2. **Cluster resources.** With the Deskription CRDs installed, the same documents can
   be applied to a cluster. UIs read them at runtime, so cluster admins and operator
   authors can add or adjust rendering for their resources without changing the UI.

A UI first loads its bundled defaults and then merges in any definitions found on the
cluster (see [Merging](#merging)).

## Selectors

Every definition carries a `selector` that names the target resource kind:

```yaml
selector:
  apiGroup: apps
  apiVersion: v1
  kind: Deployment
```

* All three fields are required and matched exactly in `v1alpha1`. Wildcard matching
  (e.g. omitting `apiVersion` to cover all versions) is planned, see the
  [roadmap](roadmap.md).
* For the Kubernetes core API group, the literal `core` and the empty string `""` are
  equivalent; the bundled definitions use `core` for readability.

## Merging

More than one definition may match the same selector — for example a bundled default
and an extension applied to the cluster. Matching definitions are merged in the order
they are loaded (bundled defaults first, then cluster definitions):

* Columns and fields are identified by their `name`.
* An entry whose `name` already exists **overrides** the existing entry in place
  (keeping its position).
* An entry with a new `name` is **appended** at the end.

So an extension can add one column to the Deployment table, or replace just the
`Status` field of the Pod details, without restating the whole definition.

For `Resource`, the last loaded definition wins, since `type` is a single value.

## Paths

`path` selects the value to render from the resource's JSON representation. Paths are
[JSONPath](https://datatracker.ietf.org/doc/html/rfc9535) expressions; the leading `$.`
is optional. The bundled definitions use simple forms:

| Path | Meaning |
| --- | --- |
| `metadata.name` | Property access |
| `status.containerStatuses.*.restartCount` | Map over an array — one value per container |

When a path yields multiple values, the column/field `type` decides how they are
combined (e.g. `sum` adds them up).

Inside a nested table (see [ResourceDetails](resource-details.md)), column paths are
relative to the row item, not to the resource root.

## Well-known names

Columns and fields may omit `path`. A small set of names is *well known*: renderers
resolve them without a path, because the value either has a canonical location or needs
renderer logic (such as joining values or querying related resources):

| Name | Resolved from |
| --- | --- |
| `Name` | `metadata.name` |
| `Namespace` | `metadata.namespace` |
| `Labels` | `metadata.labels` |
| `Annotations` | `metadata.annotations` |
| `Created` / `Created at` | `metadata.creationTimestamp` |
| `Owner` | `metadata.ownerReferences` |
| `Status` | kind-specific status, typically `status.phase` or conditions |

Any other name without a `path` is not yet specified — the bundled definitions are
drafts and still contain such placeholders (e.g. `URL` on Knative services). Renderers
should render an empty value for names they cannot resolve, never fail.

## Naming convention

`metadata.name` of a definition follows
`<distribution>-<group>-<version>-<kind>`, all lowercase — for example
`kubernetes-apps-v1-deployment` or `tekton-core-v1-pipelinerun`. The three documents
for one resource kind share the same name (one per Deskription kind) and live in one
file at `definitions/<distribution>/<group>/<version>/<Kind>.yaml`.

## Validation

JSON schemas for all kinds are in [`schema/`](../schema/):

* `resource.schema.json`, `resourcetable.schema.json`, `resourcedetails.schema.json` —
  one schema per kind
* `deskription.schema.json` — matches any of the three; use it for multi-document
  YAML files and editor integration

`python3 scripts/validate.py` validates everything under `definitions/` against the
schemas.
