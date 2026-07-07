# BidPilot — 医药行业多模式招标智能工作台

面向 **医院/集采应标（A）**、**供应商应标（B）**、**药企合作标（C）** 三类场景的统一招标 Intelligence 工作台。用户按项目自选模式；A 与 B（供应商侧）共用应标引擎；C 首发文档类型为 **药企合作标**。

---

## 项目状态

| 项 | 值 |
|----|-----|
| **Slug** | `pharma-bid-agent` |
| **版本** | v0.2 |
| **等级** | L3（可开发包） |
| **状态** | 部分可开发（Phase 1 Web SaaS 可启动） |
| **工作名** | BidPilot / 标策助手 |
| **交付形态** | **Web SaaS**（桌面浏览器） |
| **代码仓库** | （待补充，非本仓库） |

---

## 已确认决策

| 决策 | 结论 |
|------|------|
| 产品形态 | Workflow 为主 + 模式化 Skill Pack + 薄层编排 Agent |
| 模式覆盖 | A / B / C 全支持，用户新建项目时自选 |
| B 模式 Phase 1 | **仅供应商应标**，与 A **共用应标引擎** |
| B 模式 Phase 2 | 采购方发标（RFP 生成、评分表） |
| C 模式首发文档 | **药企合作标**（产学研/研发合作/联合项目应标），**含商务/报价章** |
| A 模式首发品类 | **药品集采**（国采/省采；Phase 1 不做器械/服务） |
| 高风险边界 | 不自动填资质业绩；AI 输出必须带引用；强制人工审阅后导出 |
| Phase 1 交付 | **Web SaaS**（不做插件/H5/小程序） |

---

## 文档索引

| 文档 | 路径 | 说明 |
|------|------|------|
| **产品 Spec** | [product/spec.md](./product/spec.md) | 三模式定义、流程图、MVP 范围、安全边界 |
| **开发 Plan** | [plans/plan.md](./plans/plan.md) | Codex 任务拆解（38 项）、验收标准 |
| **技术架构** | [tech/architecture.md](./tech/architecture.md) | Web SaaS 架构、Workflow、Skill Pack、API |
| **高校合作一页纸** | [business/university-partnership-one-pager.md](./business/university-partnership-one-pager.md) | 对外产学研合作草案 |
| **讨论记录** | [ideas/2026-07-06-pharma-bid-agent.md](./ideas/2026-07-06-pharma-bid-agent.md) | 需求演进与决策脉络 |
| **开放问题** | [questions/open-questions.md](./questions/open-questions.md) | 待对齐项 |

---

## MVP 功能一览（Phase 1）

| 模式 | Phase 1 深度 | 核心能力 |
|------|--------------|----------|
| **A** 药品集采应标 | 深 | 集采文件解析 + 废标清单 + 技术/商务响应矩阵 + 历史检索 + 大纲 |
| **B** 供应商应标 | 中（共用 A 引擎） | 同 A 流水线，RFP 解析 + 供应商响应模板 |
| **C** 药企合作标 | 中偏深 | 指标映射 + **技术方案 + 商务/报价章** 大纲 + 章节初稿 |
| **B** 采购方发标 | 不做 | Phase 2 |

**Phase 1 不做**：一键完整可提交标书、自动承诺资质业绩、跨模式混检、B 采购方发标。

---

## 目录结构

```
pharma-bid-agent/
├── README.md                 # 本文件（项目入口）
├── product/
│   └── spec.md               # L2 产品规格
├── ideas/
│   └── 2026-07-06-....md     # 讨论记录
├── questions/
│   └── open-questions.md     # 开放问题
├── plans/
│   └── plan.md               # L3 Codex 任务规划
├── tech/
│   └── architecture.md       # Web SaaS 技术架构
├── business/
│   └── university-partnership-one-pager.md  # 高校合作一页纸
├── decisions/                # ADR
└── archive/
```

---

## 与 RepPilot 关系

| 产品 | 阶段 | 用户 |
|------|------|------|
| **BidPilot**（本项目） | 进院前：招标/合作应标 | 招投标部、标书顾问、产学研办 |
| **RepPilot** | 进院后：代表日常 | 医药代表 |

长期叙事：BidPilot（中标/合作）→ RepPilot（推广拜访）医药商业链路。

---

## 给 Codex 的快速上手

1. 打开 [plans/plan.md](./plans/plan.md)，确认前置条件
2. 阅读 [product/spec.md](./product/spec.md) 理解范围与禁止项
3. 参照 [tech/architecture.md](./tech/architecture.md) 落地 Web SaaS
4. 按 Plan 任务 ID 顺序实现，完成后回传勾选状态

---

## 待确认项

- [ ] 产品正式名称
- [x] ~~A 模式首发品类~~ → **药品集采**
- [x] ~~Phase 1 交付形态~~ → **Web SaaS**
- [ ] 高校历史数据规模、脱敏规则与商用授权
- [ ] 目标代码仓库路径

---

## 讨论记录索引

| 日期 | 主题 | 路径 |
|------|------|------|
| 2026-07-06 | 多模式招标工作台方向讨论 | [ideas/2026-07-06-pharma-bid-agent.md](./ideas/2026-07-06-pharma-bid-agent.md) |
