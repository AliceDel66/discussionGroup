# 曜承 HR Agent — 招聘初筛与面试辅助 Agent

面向 CEO / HR / 面试官的 **Agent 驱动招聘初筛助手**：双入口简历采集（手动上传 / 招聘邮箱 IMAP 入站 / BOSS 收简历助手）→ AI 解析评估 → 人工复核 → 面试辅助 → 招聘日报。一期交付 **双版本**（企业微信内部应用版 + 独立 Web 版）及 **小微极简模式**、**BOSS 收简历助手** 内置模块。

---

## 项目状态

| 项 | 值 |
|----|-----|
| **Slug** | `hr-agent` |
| **版本** | 一期 v1.0（工程完结）/ 产品总纲 v0.4 |
| **等级** | L3（一期可开发包已闭合；release gate 补证任务可交 Codex） |
| **状态** | 一期 **工程完结**；真实试点 **release gate HOLD** |
| **客户端** | 企微 H5 工作台 + 独立 Web（Next.js 响应式） |
| **目标用户** | 曜承内部试点；中小客户 CEO/HR（simple 模式）；已用企微的企业客户 |
| **代码仓库** | `/Users/yaocheng/Desktop/nexus/Ai/hr—agent/hr-agent-app` |
| **工程文档中心** | `/Users/yaocheng/Desktop/nexus/Ai/hr—agent/doc/` |
| **当前分支** | `feature/boss-inbox`（2026-07-06 工程完结快照） |

---

## 文档索引

| 文档 | 路径 | 说明 |
|------|------|------|
| **产品 Spec** | [product/spec.md](./product/spec.md) | 功能定义、流程图、双版本矩阵、安全边界 |
| **开发 Plan** | [plans/plan.md](./plans/plan.md) | 一期任务状态、release gate、二期路线图 |
| **技术架构** | [tech/architecture.md](./tech/architecture.md) | 共享内核 + 双适配层、选型、部署 |
| **讨论记录** | [ideas/2026-07-06-hr-agent.md](./ideas/2026-07-06-hr-agent.md) | 项目建档与一期结论脉络 |
| **开放问题** | [questions/open-questions.md](./questions/open-questions.md) | release blockers 与待确认项 |

### 代码仓库权威文档（不在本仓库重复）

| 文档 | 路径（相对 hr-agent-app） |
|------|---------------------------|
| 工程 README | `README.md` |
| 交付手册索引 | `docs/README.md` |
| 一期完结报告 | `docs/phase1-completion-report.md` |
| 双版本总体方案 | `../doc/current/plan/曜承_HR_Agent_一期_双版本总体方案_v1.0.md` |
| 一期 PRD 权威 | `../doc/current/product/曜承_HR_Agent_企业微信内部应用版_一期_PRD_v1.1.md` |
| 开发状态板 | `../doc/current/loop/STATE.md` |

---

## 一期能力一览

| 优先级 | 模块 | 状态 |
|--------|------|------|
| P0 | 双版本（wecom / standalone）+ edition 开关 | ✅ |
| P0 | 简历上传 → AI 评估卡 → 人工复核 | ✅ |
| P0 | 招聘邮箱 IMAP 入站 + Mail Classifier | ✅ |
| P0 | 面试安排 / 反馈 / 招聘日报 / 审计 | ✅ |
| P0 | 用户管理 / RBAC / 集成中心 webhook | ✅ |
| P1 | 小微极简模式（simple org_mode） | ✅ |
| P1 | BOSS 收简历助手（mock/offline） | ✅ |
| — | 真实试点 release gate | ⚠️ HOLD |

**一期不做**：SMTP 出站、向候选人发消息、开放注册、多租户 SaaS、RAG、BOSS 爬取/自动打招呼。

---

## 目录结构

```
hr-agent/
├── README.md                 # 本文件（项目入口）
├── product/
│   └── spec.md               # L2+ 产品规格
├── plans/
│   └── plan.md               # L3 任务规划（含 release gate + 二期概要）
├── tech/
│   └── architecture.md       # 技术架构
├── ideas/
│   └── 2026-07-06-hr-agent.md
├── questions/
│   └── open-questions.md     # release blockers
├── decisions/                # ADR（暂无）
├── business/                 # 商业分析（暂无，见 v0.2 PRD）
├── research/                 # 调研（暂无）
└── archive/                  # 废弃文档（暂无）
```

---

## 给 Codex 的快速上手

1. 阅读 [plans/plan.md](./plans/plan.md) — 确认当前切片（release gate 补证 vs 二期）
2. 阅读 [product/spec.md](./product/spec.md) 理解范围与禁止项
3. 参照 [tech/architecture.md](./tech/architecture.md) 与代码仓库 `hr-agent-app/README.md`
4. 开发在 **代码仓库** 进行，本仓库只更新 spec/plan 状态
5. 严格遵守 plan 中的 **安全约束** 与 **Out of Scope**

---

## 待确认项

- [ ] 真实 WeCom staging 环境与证据归档
- [ ] 真实 webhook receiver 联调
- [ ] 真实邮箱端到端 P95 ≤ 7min
- [ ] LLM 5×3 评测矩阵 → `docs/phase1-m0-validation.md`
- [ ] 30 份真实/脱敏简历 + 人工签收
- [ ] `phase1-v2.0-dual` tag 发布决策

详见 [questions/open-questions.md](./questions/open-questions.md)。

---

## 讨论记录索引

| 日期 | 主题 | 路径 |
|------|------|------|
| 2026-07-06 | HR Agent 项目建档与一期工程结论 | [ideas/2026-07-06-hr-agent.md](./ideas/2026-07-06-hr-agent.md) |

---

## 变更日志

| 版本 | 日期 | 变更 |
|------|------|------|
| v0.1 | 2026-07-06 | 从 hr—agent 代码仓库建档迁入 discussionGroup |
