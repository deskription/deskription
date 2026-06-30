# ResourceTable

`ResourceTable` defines the columns a UI renders when listing resources of a kind —
the equivalent of what `kubectl get` prints, but declarative and extensible.

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
    - name: Status
      type: status
      path: status.phase
    - name: Ready
      width: short
      type: conditions
    - name: Restarts
      type: sum
      width: short
      path: status.containerStatuses.*.restartCount
    - name: Owner
      type: owners
      path: metadata.ownerReferences
    - name: Memory
      type: memory
      width: short
    - name: CPU
      type: cpu
      width: short
    - name: Created
      type: datetime
      path: metadata.creationTimestamp
```

## Spec

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `selector` | object | yes | The resource kind this table applies to, see [Selectors](concepts.md#selectors) |
| `columns` | array | yes | The columns, in render order |

### Column

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | yes | Column header. Also the merge key, see [Merging](concepts.md#merging) |
| `path` | string | no | [JSONPath](concepts.md#paths) to the value. May be omitted for [well-known names](concepts.md#well-known-names) |
| `type` | string | no | Cell renderer, defaults to `string`. See below |
| `width` | string | no | Width hint: `short`, `default` (the default), or `wide` |

## Column types

| Type | Renders |
| --- | --- |
| `string` | The raw value as text (default) |
| `status` | A status badge with an icon/color for the phase value |
| `conditions` | A ready summary derived from the resource's conditions, e.g. `2/2` |
| `sum` | The numeric sum of all values the path yields |
| `owners` | Links to the resources in an `ownerReferences` list |
| `memory` | Current memory usage of the workload (from the metrics API) |
| `cpu` | Current CPU usage of the workload (from the metrics API) |
| `datetime` | A timestamp, typically rendered as relative time |

Renderers that cannot provide a type (e.g. no metrics API available) should omit the
column or render it empty, never fail.

## Schema

[`schema/resourcetable.schema.json`](../schema/resourcetable.schema.json)
