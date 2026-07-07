# RepPilot — 医药代表智能助手

面向专科医药代表的 **Agent 工作助手**：专科晨报、重磅快讯、访前 Briefing、合规问答、访后记录。第一版客户端为 **H5 + Web 双端**（不含微信小程序）。

---

## 项目状态

| 项 | 值 |
|----|-----|
| **Slug** | `pharma-rep-agent` |
| **版本** | v0.3 |
| **等级** | L2（产品层有结论） |
| **状态** | 前端工程化重构中（MP 原型仅 UI 参考）；后端 reppilot-api 暂缓 |
| **客户端** | H5 + Web + Admin（三端）；后端 **reppilot-api**（待建） |
| **目标用户** | 医药代表（MVP 首发 1 个专科，建议心内科） |
| **代码仓库** | 前端 [`reppilot`](https://github.com/AliceDel66/reppilot)（`h5/` · `web/` · `admin/` 原型）· 后端 `reppilot-api`（暂缓） |

---

## 文档索引

| 文档 | 路径 | 说明 |
|------|------|------|
| **产品 Spec** | [product/spec.md](./product/spec.md) | 用户端功能定义、流程图、数据模型、安全边界 |
| **Admin Spec** | [product/admin-spec.md](./product/admin-spec.md) | 后台管理端：审核、信息源、资料库、合规、角色权限 |
| **开发 Plan（后端）** | [plans/plan.md](./plans/plan.md) | API / Agent 审核 / DB（**暂缓**） |
| **开发 Plan（前端）** | [plans/frontend-plan.md](./plans/frontend-plan.md) | **Codex 优先**：工程化重构、设计系统、路由、Mock |
| **技术架构** | [tech/architecture.md](./tech/architecture.md) | 双端+Admin 架构、reppilot-api、Agent 审核、部署 |
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

## UI 设计稿（Magic Patterns）

| 端 | Editor ID | 编辑器 |
|----|-----------|--------|
| H5 用户端 | `8fhtf7e7nwwhyqedsfjyxq` | [打开](https://www.magicpatterns.com/c/8fhtf7e7nwwhyqedsfjyxq) |
| Web 用户端 | `fmym8gyxshrrcbyoulnjdu` | [打开](https://www.magicpatterns.com/c/fmym8gyxshrrcbyoulnjdu) |
| **Admin 后台** | `tqyr3td9fnwxd1aqhjnvj5` | [打开](https://www.magicpatterns.com/c/tqyr3td9fnwxd1aqhjnvj5) |

- 用户端风格：**Apple Health Warmth**（温暖、关怀）
- Admin 风格：**Ops Console · Review Clarity**（运营效率、审核清晰，与用户端区分）

---

## 目录结构

```
pharma-rep-agent/
├── README.md                 # 本文件（项目入口）
├── product/
│   ├── spec.md               # L2 用户端产品规格
│   └── admin-spec.md         # L2 Admin 后台规格
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
- [ ] 注册方式 → MVP **邮箱+密码**（手机号 OTP 预留）
- [x] 前端代码仓库 → [`reppilot`](../../../reppilot)（h5 / web / admin）
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
| v0.3 | 2026-07-07 | 新增 [`frontend-plan.md`](./plans/frontend-plan.md)：前端工程化重构（MP 仅 UI 参考） |
