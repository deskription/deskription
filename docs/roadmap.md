# Roadmap

The `v1alpha1` API covers classification (`Resource`), list views (`ResourceTable`),
and detail views (`ResourceDetails`). The following extensions are planned but not yet
specified — names and shapes may change.

## Spec extensions

* **Selector wildcards.** Allow omitting selector fields to match more broadly, e.g.
  one definition covering both `v1alpha1` and `v1beta1` of a kind, or all kinds of an
  API group. `v1alpha1` requires exact matches.
* **Explicit ordering on merge.** Today merged columns/fields override by `name` or are
  appended at the end. An optional weight or before/after anchor would let extensions
  control placement.
* **Localizable names.** Column and field names are currently display strings; a future
  version may separate a stable key from the displayed (translatable) label.

## Planned kinds

* **ResourceActions** — actions a UI offers for a resource kind (restart rollout,
  trigger a pipeline, scale), including which standard actions (edit, delete) apply.
* **ResourceNavigation** — how kinds appear in menus and how resources link to related
  resources (e.g. PipelineRun → Pipeline, Pod → owning Deployment).
* **ResourceStatus** — a declarative mapping from a resource's status/conditions to a
  summarized status badge, instead of relying on renderer-side heuristics for
  `type: status` and `type: conditions`.

## Known gaps in the bundled definitions

The definitions in [`definitions/`](../definitions/) are drafts:

* Many columns/fields reference values only by name without a `path` and beyond the
  [well-known names](concepts.md#well-known-names) are not resolvable yet.
* Some tables were copied from the Pod table and reference Pod-only paths (e.g.
  `status.containerStatuses` on Deployments); they need per-kind review.
* Cluster-scoped kinds (Nodes, PersistentVolumes, StorageClasses, Users, …) still list
  a `Namespace` column.
