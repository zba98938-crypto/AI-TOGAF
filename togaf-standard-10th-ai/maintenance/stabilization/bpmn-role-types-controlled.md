# BPMN containment role types and controlled data DI rendering

This is a bounded successor to the Data/Compensation and Data DI groups. It
preserves their old audit/results bytes and addresses the MI role/type gap
retained under `output/bpmn-data-di-20261109/next-role-mapping-audit/`.

`bpmn_data_compensation._exchange_types` joins the **declared** official XSD
complex type names `t<ClassName>` to present CMOF classes. It maps 129 global
elements and all 21 class-valued local element declarations; each local role
is cross-checked against the matching owner CMOF composite property/type.
The role owner's actual class, including CMOF inheritance, determines whether
the local mapping applies. Local `ComplexBehaviorDefinition.event` consequently
means `ImplicitThrowEvent`, while the global `event` declaration means `Event`.
No XML tag capitalization or similar-name fallback is used. Primitive/QName
declarations remain values/references rather than constructed objects.

The official `MultiInstanceLoopCharacteristics.inputDataItem/outputDataItem`
roles are DataInput/DataOutput. Their inherited ItemAwareElement subject type,
collection and visibility checks now execute. MI items remain outside the
direct IOSpecification/Event set-membership loop. Expressions are preserved
and never executed. Optional `xsi:type` specialization is resolved through its
schema namespace and the source CMOF inheritance graph. Missing or conflicting
XSD/CMOF material yields an unusable material capability, not invented semantic
findings. Four exchange wrapper/text types without CMOF class counterparts are
reported in the mapping audit and are not guessed.

Sources remain the exact local official bytes:

- `BPMN20.cmof`: `72f5bf035da7bea80dc53131a22e6ba466789abd7437532e64abd3a7cff20139`.
- `Semantic.xsd`: `c4318842f7d2bbc262d7954c9452c501db16f0868eac0b8732ec5d7fb384d9a7`.
- Composite native IDs: `MultiInstanceLoopCharacteristics-inputDataItem` and
  `MultiInstanceLoopCharacteristics-outputDataItem`; declared XSD types are
  respectively `tDataInput` and `tDataOutput`.

The controlled worker now dispatches the controller-generated
`native-data-di` plan to the fixed `renderDataScene` function and checks the
native source hash. It records raw DI geometry, native plane order, common
symbols, optional data inventory, hidden native elements and notation
adaptations. The registered-session path checks, fixed two-field task schema,
resource/time/process cleanup checks and environment allowlist are reused
without modification. New independent tests exercise both real full and
partial owner views, Chinese fonts, screenshots, geometry and cleanup, plus
cross-session/absolute/symlink reads, protected input, imports, active
attributes, output-overwrite and executable-plan/command injection refusals.
All attack tasks must launch zero workers. No model sessions or budget changes
are involved.

Reproduce in this worktree with existing dependencies and an installed browser:

```sh
python3 -B tests/run_native_standard_evidence.py --out output/<new-empty-round> test_bpmn_role_types test_controlled_bpmn_data_render test_controlled_render test_bpmn_data_compensation test_bpmn_data_di test_bpmn_reference_semantics test_bpmn_design_time test_bpmn_render test_native_standard_cli
python3 -B tests/diagnose_controlled_bpmn_data.py --out output/<new-empty-admission>
```

Use `TOGAF_BROWSER_PATH` to select an existing installed executable. The
renderer does not install or download software. Role bindings are a separate
collision-checked delta, `bpmn-role-type-binding-additions.json`; they remain
partial even when bounded fixtures pass. Whole MI semantics, complete BPMN
design-time obligations, standard graphic scope completion, independent model
evaluation and human/organization approvals remain separate outstanding gates.
