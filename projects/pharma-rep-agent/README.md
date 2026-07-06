# RepPilot — 医药代表智能助手

面向专科医药代表的 **Agent 工作助手**：专科晨报、重磅快讯、访前 Briefing、合规问答、访后记录。第一版客户端为 **H5 + Web 双端**（不含微信小程序）。

---

## 项目状态

| 项 | 值 |
|----|-----|
| **Slug** | `pharma-rep-agent` |
| **版本** | v0.2 |
| **等级** | L2（产品层有结论） |
| **状态** | 有结论，待确认项清零后可交 Codex |
| **客户端** | H5（移动浏览器/PWA）+ Web（桌面浏览器） |
| **目标用户** | 医药代表（MVP 首发 1 个专科，建议心内科） |
| **代码仓库** | （待补充，非本仓库） |

---

## 文档索引

| 文档 | 路径 | 说明 |
|------|------|------|
| **产品 Spec** | [product/spec.md](./product/spec.md) | 功能定义、流程图、数据模型、安全边界 |
| **开发 Plan** | [plans/plan.md](./plans/plan.md) | Codex 任务拆解（34 项）、验收标准 |
| **技术架构** | [tech/architecture.md](./tech/architecture.md) | 双端架构、选型、API、部署 |
| **商业分析** | [business/business.md](./business/business.md) | 市场、竞品、定价、GTM |
| **讨论记录** | [ideas/2026-07-06-pharma-rep-agent.md](./ideas/2026-07-06-pharma-rep-agent.md) | 需求演进与决策脉络 |

---

## MVP 功能一览

| 优先级 | 模块 |
|--------|------|
| P0 | 专科晨报 + 重磅快讯 |
| P0 | 访前 Briefing |
| P1 | 合规问答（RAG） |
| P1 | 访后语音/文字记录 |

**不做（v1）**：微信小程序、CRM 集成、处方分析、经理看板。

---

## 目录结构

```
pharma-rep-agent/
├── README.md                 # 本文件（项目入口）
├── product/
│   └── spec.md               # L2 产品规格
├── plans/
│   └── plan.md               # L3 Codex 任务规划
├── tech/
│   └── architecture.md       # 技术架构
├── business/
│   └── business.md           # 商业分析
├── ideas/
│   └── 2026-07-06-....md     # 讨论记录
├── decisions/                # ADR（暂无）
├── questions/                # 开放问题（暂无）
├── research/                 # 调研（暂无）
└── archive/                  # 废弃文档（暂无）
```

---

## 给 Codex 的快速上手

1. 打开 [plans/plan.md](./plans/plan.md)，确认状态与前置条件
2. 阅读 [product/spec.md](./product/spec.md) 理解范围与禁止项
3. 参照 [tech/architecture.md](./tech/architecture.md) 落地技术方案
4. 按 Plan 任务 ID 顺序实现，完成后回传勾选状态

---

## 待确认项

- [ ] 产品正式名称
- [ ] MVP 首发专科
- [ ] 注册方式（手机号 vs 邮箱）
- [ ] 目标代码仓库路径
- [ ] 域名 + HTTPS
- [ ] 首发产品资料 PDF 来源

---

## 讨论记录索引

| 日期 | 主题 | 路径 |
|------|------|------|
| 2026-07-06 | 医药代表 Agent 产品完整定义 | [ideas/2026-07-06-pharma-rep-agent.md](./ideas/2026-07-06-pharma-rep-agent.md) |

---

## 变更日志

| 版本 | 日期 | 变更 |
|------|------|------|
| v0.1 | 2026-07-06 | 初版 Spec / Plan / 架构 |
| v0.2 | 2026-07-06 | 客户端改为 H5 + Web，移除微信小程序 |
| v0.2 | 2026-07-06 | 迁入 `projects/pharma-rep-agent/` 项目文件夹 |
