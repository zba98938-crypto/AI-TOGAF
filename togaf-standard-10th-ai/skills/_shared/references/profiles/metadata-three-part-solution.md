# 元数据业务需求与IT方案三要素

`profile_id`: metadata-three-part-solution；`artifact_id`: metadata-repository-design；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G234 §4.3；G234/fig4-4。

## 构图与定义状态

表示族：`metadata-map`；输出：`diagram`。规范版本：2.3。

{
  "id": "metadata-three-part-solution",
  "version": "2.3",
  "source_verified": false,
  "layout_notes": "按已核查的来源结构参数化；参考图与业务实例的验收分别进行。",
  "structure": "solution",
  "source_assets": [
    {
      "path": "reviews/source-template-bases/G234-fig4-4-p25-0.png",
      "figure_id": "G234/fig4-4",
      "pdf_page": 25,
      "sha256": "5d9b7c920c1ee780291118ac0c3601a47dc2919e9c1d04c937216664d020497c",
      "source_version": "G234e.pdf",
      "source_pdf_sha256": "34a1c590f938bf915182fe5bbe00d1d68f9a3e948697b5500ce7c5a9494f77e7",
      "verification_scope": "actual image opened; structural layout and readable labels compared; tiny embedded screenshots excluded"
    }
  ],
  "structure_basis": "实际打开英文PDF第25页：上下两层、下层三要素与两个+号、一条整体向上支撑箭头、四类关注图例。上方部门可替换，源图未规定部门/关注点数量映射。",
  "verification_limit": "组件内产品界面截图是说明素材，不声称逐字复刻；模板结构和完整例另验收。",
  "concern_legend": [
    {
      "label": "质量",
      "color": "#9dc666"
    },
    {
      "label": "文档化",
      "color": "#fff3b0"
    },
    {
      "label": "安全／隐私／合规",
      "color": "#edb6c0"
    },
    {
      "label": "治理",
      "color": "#7acbd3"
    }
  ]
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：visual_container, requirement, metadata_solution_component。关系类型：visually_contains, supports_metadata_requirement, g234:supports-requirements。

```json
{
  "entities": {
    "visual_container": [
      "definition"
    ],
    "requirement": [
      "statement",
      "concerns",
      "concern_mapping_basis"
    ],
    "metadata_solution_component": [
      "definition"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 对象、关系、必要属性均可追溯并得到表达
- 参考内容不自动成为项目事实；未知项保持显式
- 源图支撑关系从整个IT方案指向整个业务需求
- 下层三要素用+表示组合，不是流程
- 四类关注图例齐全且不当成人员数量
- 虚构项目关系与来源整体支撑关系分别展示
- 来源错图继续保留和登记

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构业务案例；采用来源结构及术语，不代表真实实施或批准。",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "虚构社区服务机构的访谈、记录和项目约定"
    }
  ],
  "entities": [
    {
      "id": "metadata-needs",
      "type": "visual_container",
      "name": "业务需求",
      "attributes": {
        "definition": "由业务社区及质量、文档、安全隐私合规、治理关注共同确定",
        "g234:slot": "requirements"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-solution",
      "type": "visual_container",
      "name": "元数据管理IT方案",
      "attributes": {
        "definition": "技术功能集、数据模型、流程三部分协同构成方案",
        "g234:slot": "solution"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-need-ops",
      "type": "requirement",
      "name": "社区服务运营",
      "attributes": {
        "statement": "预约术语一致，变更后下游字典可追溯",
        "concerns": [
          "质量",
          "文档化",
          "安全／隐私／合规",
          "治理"
        ],
        "concern_mapping_basis": "虚构案例的共同关注；不是源图部门与颜色的一一对应"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-need-finance",
      "type": "requirement",
      "name": "补贴财务",
      "attributes": {
        "statement": "补贴字段与业务规则匹配，报表能回溯定义",
        "concerns": [
          "质量",
          "文档化",
          "安全／隐私／合规",
          "治理"
        ],
        "concern_mapping_basis": "虚构案例的共同关注；不是源图部门与颜色的一一对应"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-need-privacy",
      "type": "requirement",
      "name": "数据保护",
      "attributes": {
        "statement": "个人数据使用目的、保留规则、访问与变更职责明确",
        "concerns": [
          "质量",
          "文档化",
          "安全／隐私／合规",
          "治理"
        ],
        "concern_mapping_basis": "虚构案例的共同关注；不是源图部门与颜色的一一对应"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-tech",
      "type": "metadata_solution_component",
      "name": "1. 技术",
      "attributes": {
        "definition": "术语目录、字典连接器与权限/版本服务"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-data-model",
      "type": "metadata_solution_component",
      "name": "2. 数据模型",
      "attributes": {
        "definition": "术语→业务元素→数据字段及处理活动关联，标识和值域明确定义"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-process",
      "type": "metadata_solution_component",
      "name": "3. 流程与工作流",
      "attributes": {
        "definition": "管家提交→所有者评审→发布；隐私变更由数据保护角色参与"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "group-metadata-need-ops",
      "type": "visually_contains",
      "source": "metadata-needs",
      "target": "metadata-need-ops",
      "label": "业务需求分组",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "group-metadata-need-finance",
      "type": "visually_contains",
      "source": "metadata-needs",
      "target": "metadata-need-finance",
      "label": "业务需求分组",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "group-metadata-need-privacy",
      "type": "visually_contains",
      "source": "metadata-needs",
      "target": "metadata-need-privacy",
      "label": "业务需求分组",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "solution-metadata-tech",
      "type": "visually_contains",
      "source": "metadata-solution",
      "target": "metadata-tech",
      "label": "方案的并列组成，不是执行步骤",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "supports-metadata-tech",
      "type": "supports_metadata_requirement",
      "source": "metadata-tech",
      "target": "metadata-need-finance",
      "label": "虚构项目设计支撑，待实现验证",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "definition_origin": "fictional-project-design; not a relation asserted by source figure"
      }
    },
    {
      "id": "solution-metadata-data-model",
      "type": "visually_contains",
      "source": "metadata-solution",
      "target": "metadata-data-model",
      "label": "方案的并列组成，不是执行步骤",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "supports-metadata-data-model",
      "type": "supports_metadata_requirement",
      "source": "metadata-data-model",
      "target": "metadata-need-ops",
      "label": "虚构项目设计支撑，待实现验证",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "definition_origin": "fictional-project-design; not a relation asserted by source figure"
      }
    },
    {
      "id": "solution-metadata-process",
      "type": "visually_contains",
      "source": "metadata-solution",
      "target": "metadata-process",
      "label": "方案的并列组成，不是执行步骤",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "supports-metadata-process",
      "type": "supports_metadata_requirement",
      "source": "metadata-process",
      "target": "metadata-need-privacy",
      "label": "虚构项目设计支撑，待实现验证",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "definition_origin": "fictional-project-design; not a relation asserted by source figure"
      }
    },
    {
      "id": "solution-supports-business",
      "type": "g234:supports-requirements",
      "source": "metadata-solution",
      "target": "metadata-needs",
      "label": "三个要素共同构成的IT方案支撑业务需求",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "definition_origin": "source-structure-G234-fig4-4",
        "scope": "whole-solution-to-whole-requirements; not three one-to-one mappings"
      }
    }
  ],
  "view": {
    "id": "v-metadata-three-part-solution",
    "artifact_id": "metadata-repository-design",
    "profile_id": "metadata-three-part-solution",
    "title": "元数据业务需求与IT方案三要素",
    "entity_ids": [
      "metadata-needs",
      "metadata-solution",
      "metadata-need-ops",
      "metadata-need-finance",
      "metadata-need-privacy",
      "metadata-tech",
      "metadata-data-model",
      "metadata-process"
    ],
    "relationship_ids": [
      "group-metadata-need-ops",
      "group-metadata-need-finance",
      "group-metadata-need-privacy",
      "solution-metadata-tech",
      "supports-metadata-tech",
      "solution-metadata-data-model",
      "supports-metadata-data-model",
      "solution-metadata-process",
      "supports-metadata-process",
      "solution-supports-business"
    ],
    "analysis": "原料：三个业务社区要求质量、定义与隐私可追溯。先分出需求范围和技术/模型/流程；三者共同支撑业务需求。源图只规定整体支撑，案例另列三条待验证的组成到具体需求关系。",
    "legend": "四类关注：质量（绿）、文档化（浅黄）、安全／隐私／合规（粉）、治理（青）；色块不是人员数量。+ 表示三要素共同具备，不是步骤；箭头从IT方案指向业务需求；项目设计关系另列。"
  },
  "extensions": {
    "relationship_types": {
      "g234:supports-requirements": {
        "source_types": [
          "visual_container"
        ],
        "target_types": [
          "visual_container"
        ],
        "meaning": "G234图4-4整体元数据IT方案支撑业务需求范围；不是特定组件到部门的一一映射"
      }
    }
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile metadata-three-part-solution --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile metadata-three-part-solution --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
