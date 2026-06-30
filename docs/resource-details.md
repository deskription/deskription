# ResourceDetails

`ResourceDetails` defines the fields a UI renders on the detail view of a single
resource — the equivalent of `kubectl describe`, but declarative and extensible.

```yaml
apiVersion: deskription.io/v1alpha1
kind: ResourceDetails
metadata:
  name: kubernetes-core-v1-pod
spec:
  selector:
    apiGroup: core
    apiVersion: v1
    kind: Pod
  fields:
    - name: Name
    - name: Namespace
    - name: Labels
    - name: Annotations
    - name: Created at
    - name: Owner
    - name: Status
    - name: Containers
      type: table
      table:
        columns:
          - name: Name
          - name: Image
          - name: State
          - name: Restarts
          - name: Started
          - name: Finished
```

## Spec

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `selector` | object | yes | The resource kind these details apply to, see [Selectors](concepts.md#selectors) |
| `fields` | array | yes | The fields, in render order |

### Field

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | yes | Field label. Also the merge key, see [Merging](concepts.md#merging) |
| `path` | string | no | [JSONPath](concepts.md#paths) to the value. May be omitted for [well-known names](concepts.md#well-known-names) |
| `type` | string | no | Value renderer, defaults to `string`. All [column types](resource-table.md#column-types) plus `table` |
| `table` | object | when `type: table` | Nested table definition |
| `table.columns` | array | yes | Columns of the nested table; same shape as [ResourceTable columns](resource-table.md#column) |

## Nested tables

A field with `type: table` renders a list that belongs to the resource — for example
the containers of a Pod — as an embedded table. The field's `path` selects the list;
each entry becomes a row, and the nested columns' paths are evaluated **relative to the
row item** (e.g. `image` for a container), not to the resource root.

## Schema

[`schema/resourcedetails.schema.json`](../schema/resourcedetails.schema.json)
