# Codex 任务规划：曜承 HR Agent

- **对应 Spec**：[`../product/spec.md`](../product/spec.md)
- **项目索引**：[`../README.md`](../README.md)
- **日期**：2026-07-06
- **版本**：一期 v1.0 工程完结 + release gate 补证切片
- **状态**：一期 **工程 PASS**；release gate **可启动**；二期 **待排期**
- **目标代码仓库**：`/Users/yaocheng/Desktop/nexus/Ai/hr—agent/hr-agent-app`
- **工程状态板权威**：`../Ai/hr—agent/doc/current/loop/STATE.md`（代码仓库内）

---

## 前置条件（release gate 切片）

- [x] 一期 T1–T14 工程任务闭合
- [x] SM1–SM9 小微极简模式闭合
- [x] BI1–BI8 BOSS 收简历助手闭合（mock/offline）
- [ ] 真实 WeCom staging 凭据与可信域名就绪
- [ ] 真实 webhook receiver URL 就绪
- [ ] `samples/pilot/` 真实/脱敏样本 manifest 填充
- [ ] LLM 正式网关可用于 5×3 矩阵

---

## 安全约束（Codex 必须遵守）

- **一期零 SMTP**：不得引入 smtplib / sendmail / 任何发信依赖
- **IMAP 只读**：mail-poller 不得修改邮箱状态（除已设计标记）
- **共享内核不直连企微**：pipeline / worker 不得 import wecom 模块
- **日志/审计脱敏**：禁止输出联系方式、简历原文、授权码、API Key
- **webhook SSRF**：生产拒绝内网/链路本地地址
- **BOSS 红线**：禁止 greet / batch-view / search / 生产 mock 绑定
- **RBAC 服务端强制**：越权必须 403 + 审计
- **AI 结论声明**：前端页脚保留人工复核声明
- **禁止实现（一期）**：开放注册、多租户、RAG、ATS 爬虫、自动淘汰/录用

---

## Phase 1 — 一期工程（已完成 ✅）

> 状态来源：`doc/current/loop/STATE.md` + `docs/phase1-completion-report.md`

### Sprint 0：双版本地基 T1–T6

| ID | 任务 | 状态 | 证据 |
|----|------|------|------|
| T1 | edition 开关、路由挂载、env 模板 | ✅ done | caea46f |
| T2 | Alembic、schema、source 中性化 | ✅ done | 3 migrations |
| T3 | AuthProvider、本地登录、改密、锁定 | ✅ done | test_auth.py |
| T4 | 上传越权、RBAC、质量补课 | ✅ done | test_upload_security.py |
| T5 | NotificationChannel 三通道 | ✅ done | notify.py |
| T6 | 前端 edition、登录页、通知铃铛 | ✅ done | /login, NotificationBell |

### Sprint 1–2：候选人域 + 邮箱 T7–T11

| ID | 任务 | 状态 | 证据 |
|----|------|------|------|
| T7 | 候选人列表/详情/复核/assign-job | ✅ done | c05b02b |
| T8 | mailbox-ingest、Mail Classifier | ✅ done | 6ed3441 |
| T9 | 用户管理 P0 | ✅ done | /admin/users |
| T10 | webhook 告警与集成中心 | ✅ done | /integrations |
| T11 | 面试、日报、审计 | ✅ done | a2dd772 |

### Sprint 3–4：质量 + 交付 T12–T15

| ID | 任务 | 状态 | 证据 |
|----|------|------|------|
| T12 | 安全与红线回归 | ✅ done | test_security_redlines.py |
| T13 | CI 完整版、回归样本集 | ✅ done | 20 简历 + 15 邮件 |
| T14 | 打包部署与手册 | ✅ done | docker-compose + docs |
| T15 | 试点验收 | ⚠️ partial | 工程 PASS / release HOLD |

### 扩展：小微极简模式 SM1–SM9

| ID | 任务 | 状态 |
|----|------|------|
| SM1 | org_mode 后端底座 | ✅ done |
| SM2 | 老板三键决策 | ✅ done |
| SM3 | 通知 simple preset | ✅ done |
| SM4 | 开箱三步向导 | ✅ done |
| SM5 | 老板评估卡 one_line_verdict | ✅ done |
| SM6 | 轻量面试记录 | ✅ done |
| SM7 | 导航折叠与升级向导 | ✅ done |
| SM8 | 四组合 CI matrix | ✅ done |
| SM9 | 小微交付文档 | ✅ done |

### 扩展：BOSS 收简历助手 BI1–BI8

| ID | 任务 | 状态 |
|----|------|------|
| BI1 | 数据模型 + 租户开关 | ✅ done |
| BI2 | 账号绑定、同步、轮询 | ✅ done |
| BI3 | 会话分拣 + 列表 API | ✅ done |
| BI4 | 求简历执行 + 批量审计 | ✅ done |
| BI5 | BOSS 待处理页与导航 | ✅ done |
| BI6 | 首页摘要 + 设置 + 详情链路 | ✅ done |
| BI7 | 邮箱入站 ↔ BOSS 关联 | ✅ done |
| BI8 | 测试、红线、交付文档 | ✅ done |

---

## Phase RG — Release Gate 补证（当前推荐切片）

> 入口：`hr-agent-app/docs/pilot-evidence-runbook.md`
> 目标：闭合 T15 release gate，决策是否打 `phase1-v2.0-dual` tag

| ID | 任务 | 输入 | 输出 | 验收标准 | 依赖 |
|----|------|------|------|----------|------|
| RG1 | 真实/脱敏 pilot 样本包 | 30 简历 + 20 邮件 | `samples/pilot/manifest.json` | 人工标签签收；privacy 审查通过 | 用户提供样本 |
| RG2 | pilot 证据脚本聚合 | RG1 manifest | `samples/pilot/evidence.json` | `pilot_sample_evidence.py` gate 通过 | RG1 |
| RG3 | LLM 5×3 评测矩阵 | 5 脱敏简历 × 3 轮 | `docs/phase1-m0-validation.md` | schema pass、分数漂移 ≤10、耗时/成本记录 | LLM 网关 |
| RG4 | 真实 WeCom staging | CorpID/Secret/域名/回调 | staging 截图/遮挡证据 | 免登 + textcard + 深链全链路 | 企微后台 |
| RG5 | 真实 webhook receiver | ALERT_WEBHOOK_URL | test send 成功日志 | payload 零候选人信息；HMAC 验证 | 外网 endpoint |
| RG6 | 真实邮箱 E2E P95 | 受控 BOSS 投递 + 非招聘邮件 | 时间戳证据 | mail-poller → DB P95 ≤ 7min | 真实 IMAP |
| RG7 | 公网 HTTPS 复验 | 域名 + Nginx + 证书 | healthz 200 | api/web 公网可达 | 运维 |
| RG8 | CI 口径对齐 | Python 3.12 / Node 20 | CI 绿色 | 与本地 3.14/24 差异消除 | RG1–RG6 |
| RG9 | tag 决策复盘 | RG1–RG8 证据 | 更新 phase1-completion-report | 决策 GO/HOLD + tag 说明 | 全部 |

### RG 执行顺序

```
RG1 → RG2 → RG3（可与 RG4–RG6 并行）
RG4、RG5、RG6 可并行
RG7 依赖部署环境
RG9 最后
```

---

## Phase 2 — 产品增强（概要，未排期）

> 来源：PRD v1.1 §3.3 二期归属 + v0.2 AgentMail PRD 愿景
> **启动前需用户确认优先级**

### 2.1 出站邮件与沟通（P0 候选）

| ID | 任务 | 验收标准 |
|----|------|----------|
| P2-1 | 邮件模板 CRUD + 预览 | HR 可编辑邀约/拒信模板 |
| P2-2 | 两阶段确认发送 | Agent 草稿 → 人工确认 → SMTP 发送 |
| P2-3 | 退信/回复归档 | delivery log + 候选人时间线 |
| P2-4 | DKIM/SPF 部署指南 | 送达率基线文档 |

### 2.2 评估增强

| ID | 任务 | 验收标准 |
|----|------|----------|
| P2-5 | 企业 RAG 岗位知识包 | 评估卡引用内部 JD/标准文档 |
| P2-6 | 历史校准 / 评分漂移监控 | 管理员看板 |
| P2-7 | 真实性分析（轻量） | 风险 flag，不进自动决策 |

### 2.3 渠道与集成

| ID | 任务 | 验收标准 |
|----|------|----------|
| P2-8 | AgentMail / webhook 邮箱 provider | 与 IMAP 并列 adapter |
| P2-9 | 多招聘邮箱分岗位 | 绑定 N 邮箱 |
| P2-10 | ATS 官方集成调研 | ADR + PoC |

### 2.4 平台化（Phase 7 前置）

| ID | 任务 | 验收标准 |
|----|------|----------|
| P2-11 | 开放注册 + 邀请流 | 单租户扩展 |
| P2-12 | SSO/OIDC 适配器 | AuthProvider 第三实现 |
| P2-13 | 多租户 SaaS 数据隔离 | tenant_id 全链路 |

---

## Phase 3 — 对外服务包（Future）

| 方向 | 说明 |
|------|------|
| 曜承 AI 招聘初筛服务包 | 面向创业 CEO / 中小老板 |
| 按岗位/按量计费 | 需 Phase 2 出站 + 多租户 |
| 行业模板库 | 医疗 AI / 企服 / 外包等岗位 |

---

## 验收清单（release gate 全绿条件）

参照 `hr-agent-app/docs/phase1-completion-report.md` §9：

- [ ] RG1 真实/脱敏样本人工签收
- [ ] RG3 LLM 5×3 矩阵归档
- [ ] RG4 真实 WeCom 全链路
- [ ] RG5 真实 webhook test send
- [ ] RG6 真实邮箱 E2E P95
- [ ] RG7 公网 HTTPS
- [ ] RG9 tag 决策 = GO

---

## 变更日志

| 版本 | 日期 | 变更 |
|------|------|------|
| v0.1 | 2026-07-06 | 从 hr—agent 工程状态建档；一期任务标记完成；新增 RG 切片与 Phase 2 概要 |
