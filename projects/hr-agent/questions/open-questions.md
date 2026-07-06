# 开放问题与 Release Blockers

- **日期**：2026-07-06
- **状态**：一期工程完结；以下项阻塞正式 release / tag 决策
- **权威来源**：`hr-agent-app/docs/phase1-completion-report.md` §9

---

## P0 — Release Gate（阻塞 `phase1-v2.0-dual` tag）

| ID | 问题 | 阻塞原因 | 关闭条件 | 负责人 |
|----|------|----------|----------|--------|
| Q1 | 真实 WeCom staging | 企微版不能只靠路由 smoke 发布 | CorpID/Secret/AgentID/可信域名/callback/textcard 全链路通过，证据归档 | 待确认 |
| Q2 | 真实 webhook receiver | 告警外送成功率未证明 | `/integrations` 配置真实 endpoint，test send 成功，payload 零候选人信息 | 待确认 |
| Q3 | 真实邮箱端到端 P95 | 仅 offline 分类 + 历史 IMAP smoke | 受控 BOSS 投递进入 IMAP，`mail-poller → DB` P95 ≤ 7min | 待确认 |
| Q4 | LLM 5×3 矩阵 | T0 模型稳定性/耗时/成本未冻结 | 5 份脱敏简历 × 3 轮 → `docs/phase1-m0-validation.md` | 待确认 |
| Q5 | 真实/脱敏样本人工签收 | `samples/pilot` 当前为 synthetic | 替换或补充真实脱敏样本，人工标签 + 聚合报告 | 用户提供 |

---

## P1 — 环境与口径

| ID | 问题 | 说明 | 关闭条件 |
|----|------|------|----------|
| Q6 | 公网 HTTPS | 本机 compose 未证明公网 | 目标域名/Nginx/证书到位后复验 |
| Q7 | 本地 vs CI runtime 差异 | 本机 Python 3.14/Node 24；CI 固定 3.12/20 | CI 绿色或本地补跑 3.12/20 |
| Q8 | BOSS 真实 staging | BI1–BI8 仅 mock/offline | 受控真实 BOSS 账号演示（非爬取） |

---

## P2 — 技术债（不阻塞一期 tag）

| ID | 问题 | 说明 |
|----|------|------|
| Q9 | FastAPI `on_event` deprecation | 迁移 lifespan |
| Q10 | BOSS 邮件规则校准 | T0 真实 BOSS 样本未提供，规则仍用 example.yaml |
| Q11 | JWT test key warnings | 测试环境 SECRET_KEY 长度 |

---

## 产品待确认（Phase 2 排期前）

| ID | 问题 | 选项 | 影响 |
|----|------|------|------|
| Q12 | 二期首要优先级 | A. 出站邮件 B. RAG C. AgentMail adapter | Phase 2 WBS 排序 |
| Q13 | 对外服务包定价模型 | 按岗位 / 按量 / 订阅 | 商业 plan |
| Q14 | 多租户 SaaS 时间表 | Phase 7 原路线图 vs 提前 | 架构演进 |
| Q15 | AgentMail v0.2 与一期关系 | 独立 Phase vs 合并邮箱 adapter | spec 范围 |

---

## 已关闭（2026-07-06 P0 整改）

| 问题 | 修复提交 |
|------|----------|
| BI4 日上限跨天误重置 | 85503bb |
| 生产密钥与凭据加密 | 2c5512e |
| 候选人来源证据泄露 | 67ca9b7 |
| 告警 webhook SSRF | 9d69b39 |
| 上传页未提交授权记录 | 26c2b50 |
| 生产环境 BOSS mock 绑定 | fc24bfd |
| notify 内核顶层加载企微 | 527b57f |
| BOSS smoke 环境边界 | 38e8e1b |

---

## 下一步行动建议

1. 按 [plans/plan.md](../plans/plan.md) **Phase RG** 切片执行
2. 入口手册：`hr-agent-app/docs/pilot-evidence-runbook.md`
3. 样本填充：本地 `samples/pilot/manifest.json`（不进 git）
4. 全部 P0 闭合后召开 tag 决策（RG9）
