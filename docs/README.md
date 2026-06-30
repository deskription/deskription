# Deskription documentation

Deskription is a Kubernetes-native way to describe how UIs should render Kubernetes
resources. Instead of hard-coding tables and detail views per resource kind, a UI reads
Deskription definitions — themselves Kubernetes resources — and renders any kind,
including custom resources, from that description.

## Contents

* [Concepts](concepts.md) — how definitions are consumed, selectors, merging,
  paths, and well-known names
* [Resource](resource.md) — classifying a resource kind
* [ResourceTable](resource-table.md) — columns for list views
* [ResourceDetails](resource-details.md) — fields for detail views
* [Roadmap](roadmap.md) — planned kinds and spec extensions

## Quick example

A single YAML file usually contains all three definitions for one resource kind,
separated by `---`:

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
---
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
---
apiVersion: deskription.io/v1alpha1
kind: ResourceDetails
metadata:
  name: kubernetes-apps-v1-deployment
spec:
  selector:
    apiGroup: apps
    apiVersion: v1
    kind: Deployment
  fields:
    - name: Name
    - name: Namespace
    - name: Labels
      path: metadata.labels
```

## Validation

JSON schemas for all kinds live in [`schema/`](../schema/). Validate the bundled
definitions with:

```sh
python3 scripts/validate.py
```

To get completion and validation in VS Code (with the YAML extension), add to your
settings:

```json
"yaml.schemas": {
  "./schema/deskription.schema.json": "definitions/**/*.yaml"
}
```
