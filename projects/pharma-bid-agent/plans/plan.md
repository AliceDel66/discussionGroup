# Codex 任务规划：BidPilot 多模式招标工作台

- **对应 Spec**：[`../product/spec.md`](../product/spec.md)
- **技术架构**：[`../tech/architecture.md`](../tech/architecture.md)
- **项目索引**：[`../README.md`](../README.md)
- **日期**：2026-07-06
- **版本**：v0.1（Web SaaS，A 药品集采 + B 供应商 + C 药企合作标）
- **状态**：部分可开发（Phase 1 可启动；待用户确认项见 Spec §10）
- **目标代码仓库**：（待用户补充）

---

## 前置条件

- [ ] 域名 + HTTPS 已就绪
- [ ] LLM API Key 与 Embedding 环境可用
- [ ] 对象存储（OSS/MinIO）可用
- [ ] 至少 1 套 **药品集采** 样本（招标 PDF + 脱敏标书）用于联调
- [ ] 至少 1 套 **药企合作标** 样本（指南 + 含商务章脱敏方案）
- [ ] 高校行业库数据协议进度明确（可先租户库试点）
- [ ] Word 导出模板初版（技术标/商务标/合作标各 1）

---

## 安全约束（Codex 必须遵守）

- **未审阅通过（status ≠ approved）禁止导出正式稿**；仅允许带水印 preview
- AI **禁止**输出真实报价金额、降幅、费率、资质编号；ComplianceFilter 强制 `{{待填写}}`
- RAG 检索 SQL **必须**带 `mode = project.mode`；禁止跨租户
- 用户数据按 `tenant_id` 严格隔离；Admin 独立鉴权
- 不在代码/日志中硬编码 API Key
- 上传文件 MIME 白名单；病毒扫描可选
- **禁止实现**：Office/Cursor 插件、H5/小程序、电子投标 CA、跨模式混检、B 采购方发标、AI 自动填资质业绩

---

## Phase 1 — Web SaaS MVP（6–8 周）

### Sprint 1：基础架构 + 项目骨架（Week 1）

| ID | 任务 | 输入 | 输出 | 验收标准 | 依赖 |
|----|------|------|------|----------|------|
| T1 | 初始化 monorepo | architecture §9 | `backend/` + `frontend/` | 本地 docker-compose 可启动 | — |
| T2 | DB migration | Spec §7 | Alembic 全部表 | Project/Document/Matrix/Outline/Draft/Review/KnowledgeDoc | T1 |
| T3 | 认证 + 多租户 | JWT | register/login/refresh + tenant_id | 注册登录；数据 tenant 隔离 | T1, T2 |
| T4 | Project CRUD API | mode, category, tags | POST/GET/PATCH /projects | 创建 A/B/C 项目；A 固定 category=drug_procurement | T3 |
| T5 | Web 骨架 | Spec §8 页面清单 | 侧边栏布局 + 路由 | 项目列表/新建/详情壳可导航 | T3 |
| T6 | Workflow 状态机 | architecture §4 | state_machine + status API | 状态按 Spec 流转；非法跳转拒绝 | T4 |

### Sprint 2：文档解析 + Skill Pack A/C（Week 2–3）

| ID | 任务 | 输入 | 输出 | 验收标准 | 依赖 |
|----|------|------|------|----------|------|
| T7 | 文件上传 API | PDF/docx | OSS + Document 记录 | 50MB 限制；返回 document_id | T4 |
| T8 | 文本提取 + OCR 降级 | T7 | parser service | 文本层优先；扫描件走 OCR | T7 |
| T9 | SkillPack 基类 + Router | architecture §5 | base.py + router | mode 路由到正确 Pack | T8 |
| T10 | A 药品集采 Pack | parse_schema_drug | ParsedRequirement | 输出：品种/废标/技术商务/报价格式 Tab | T9 |
| T11 | C 合作标 Pack | parse_schema_collab | ParsedRequirement | 输出：指标/预算/商务报价/IP Tab | T9 |
| T12 | B 供应商 Pack | 共用 A 引擎 | SupplierBidPack | 复用流水线；RFP 字段映射 | T10 |
| T13 | 解析 Celery Job | T8–T12 | async parse task | 202 异步；完成后 status=parsed | T12 |
| T14 | Web 解析结果页 | T13 | 分 Tab 展示 + 加载态 | 轮询/SSE 解析进度 | T5, T13 |

### Sprint 3：响应矩阵 + 相似检索（Week 3–4）

| ID | 任务 | 输入 | 输出 | 验收标准 | 依赖 |
|----|------|------|------|----------|------|
| T15 | Matrix 生成服务 | ParsedRequirement + Pack | ResponseMatrix rows | A：含技术/商务列；C：含章节类型列 | T13 |
| T16 | Matrix API + 编辑 | PATCH rows | GET/PATCH /matrix | 增删改行；Excel 导出 | T15 |
| T17 | Web 可编辑矩阵 | T16 | EditableMatrix 组件 | 大数据量表格流畅；导出按钮 | T16, T5 |
| T18 | KnowledgeDoc 模型 + Admin 入库 | 脱敏样本 | /admin/knowledge | mode/tags/chunks 入库 | T2 |
| T19 | pgvector 索引 + 检索 | mode 硬过滤 | /similar-cases | 仅同 mode；Top-K + snippet | T18 |
| T20 | Web 相似案例页 | T19 | 卡片列表 + 参考段落 | 点击可查看引用 | T19, T5 |

### Sprint 4：大纲 + 章节起草（Week 4–5）

| ID | 任务 | 输入 | 输出 | 验收标准 | 依赖 |
|----|------|------|------|----------|------|
| T21 | Outline 推荐 | 矩阵 + 检索 + 模板 | /outline/recommend | A：技术+商务分册；C：含商务/报价章 | T16, T19 |
| T22 | Outline API + 树形编辑 | sections[] | GET/PATCH /outline | 增删改章节顺序 | T21 |
| T23 | Web 大纲树 | T22 | OutlineTree 组件 | 从案例插入章节 | T22, T5 |
| T24 | Draft 生成 Job | outline + citations | SectionDraft | 每段带 citations；数值占位符 | T22 |
| T25 | ComplianceFilter | LLM 输出 | 过滤金额/资质 | 违规字段 → `{{待填写}}` | T24 |
| T26 | Web 章节编辑器 | T24 | 双栏：正文 + 引用侧栏 | C 模式 Phase 1 必须可用 | T24, T5 |
| T27 | A 模式章节起草 | T24 | 可选 Sprint 4 末或 Sprint 5 | 至少 C 完整；A 可先大纲 | T24 |

### Sprint 5：合规扫描 + 审阅 + 导出（Week 5–6）

| ID | 任务 | 输入 | 输出 | 验收标准 | 依赖 |
|----|------|------|------|----------|------|
| T28 | Compliance 扫描 | matrix + drafts + pack rules | /compliance/scan | A：废标+报价表；C：商务章缺项 | T16, T24 |
| T29 | Review API | approve/reject | /review | 未 approved 拦截正式导出 | T28 |
| T30 | Word 导出 | docxtpl + 水印 | /export | approved 后 Word；未审阅仅 preview | T29 |
| T31 | Excel 矩阵导出 | openpyxl | 随 /export 打包 | 矩阵与 Word 一致 | T16, T30 |
| T32 | Web 审阅页 | T29 | 通过/退回 + 意见 | 退回回到 drafting | T29, T5 |
| T33 | Web 导出页 | T30 | 下载 + 占位符警告 | 有水印 preview 与正式稿区分 | T30, T5 |

### Sprint 6：联调 + 三模式验收（Week 6–8）

| ID | 任务 | 输入 | 输出 | 验收标准 | 依赖 |
|----|------|------|------|----------|------|
| T34 | 端到端 A 药品集采 | 真实样本 | 演示项目 | 解析→矩阵→大纲→（可选起草）→审阅→导出 | T1–T33 |
| T35 | 端到端 B 供应商 | RFP 样本 | 演示项目 | 共用 A 引擎全流程 | T34 |
| T36 | 端到端 C 合作标 | 含商务章样本 | 演示项目 | 含商务/报价章；数值占位 | T34 |
| T37 | Admin 知识库批量导入 | 高校样本 | seed 脚本 | ≥10 条分 mode 样本可检索 | T18 |
| T38 | 部署文档 + CI | docker-compose | README deploy |  staging 可访问 | T1 |

---

## 建议执行顺序

```mermaid
flowchart LR
    T1 --> T2 --> T3 --> T4 --> T5 --> T6
    T6 --> T7 --> T8 --> T9 --> T10
    T10 --> T11 --> T12 --> T13 --> T14
    T14 --> T15 --> T16 --> T17 --> T18 --> T19 --> T20
    T20 --> T21 --> T22 --> T23 --> T24 --> T25 --> T26
    T26 --> T28 --> T29 --> T30 --> T31 --> T32 --> T33
    T33 --> T34 --> T35 --> T36 --> T37 --> T38
```

---

## Out of Scope（Codex 勿做）

- Cursor / Word / Office 插件
- H5、微信小程序
- B 模式采购方发标
- 器械/服务集采（A 模式扩展）
- 跨 mode 检索
- 电子投标平台对接、CA 锁
- AI 自动填写报价金额、资质、业绩
- 与 RepPilot 代码级集成

---

## 完成后自检

- [ ] A 药品集采：解析含品种/商务报价格式；矩阵分技术/商务
- [ ] B 供应商：全流程跑通，索引 mode=B
- [ ] C 合作标：大纲含商务/报价章；起草带引用；数值占位
- [ ] 未 approved 无法下载正式 Word
- [ ] RAG 检索不会返回其他 mode/tenant 数据
- [ ] ComplianceFilter 拦截金额/资质自动输出

---

## 回传 Cursor

Codex 完成后应更新：本 plan 任务勾选状态，并在 `product/spec.md` 注明「已实现 / 偏差说明」。同步更新项目 `README.md` 状态。
