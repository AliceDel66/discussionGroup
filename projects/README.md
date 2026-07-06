# projects — 项目归档目录

本目录存放**按项目隔离**的全部规划文档。每个产品/功能方向拥有**独立大文件夹**，内含完整 spec、plan、架构、商业分析与讨论记录。

---

## 为什么用项目文件夹

- 一个仓库可并行管理多个产品，互不混杂
- Codex 只需进入单个项目目录即可拿到全部上下文
- 项目 README 作为该产品的**唯一入口索引**

---

## 项目列表

| 项目 | 目录 | 状态 | 等级 | 说明 |
|------|------|------|------|------|
| RepPilot 医药代表智能助手 | [pharma-rep-agent](./pharma-rep-agent/) | 有结论 | L2 | H5 + Web 双端 Agent，面向医药代表 |

> 新建项目时在此追加一行，并创建 `projects/<project-slug>/README.md`。

---

## 新建项目流程（Cursor Agent 必遵）

1. 确定 **project-slug**（英文小写 + 连字符，如 `pharma-rep-agent`）
2. 创建目录：

```
projects/<project-slug>/
├── README.md          # 必填：项目入口索引
├── ideas/             # 讨论记录
├── product/           # spec.md 或 specs/
├── plans/             # plan.md
├── tech/              # architecture.md
├── business/          # 可选
├── research/          # 可选
├── decisions/         # ADR
├── questions/         # 开放问题
└── archive/           # 已废弃文档
```

3. 编写 `projects/<project-slug>/README.md`（见 agent.md 模板）
4. 更新**本文件**「项目列表」表
5. 更新**根目录** `README.md`「项目索引」表

---

## 与根目录的关系

| 位置 | 用途 |
|------|------|
| `/agent.md` | 全局 Agent 操作规范 |
| `/README.md` | 仓库总览 + 项目索引 |
| `/projects/<slug>/` | **所有产品文档的实际存放位置** |

根目录不再直接存放 `product/`、`plans/` 等业务文档（已废弃该扁平结构）。
