#!/usr/bin/env python3
"""Export Magic Patterns artifact JSON dumps into RepPilot monorepo folders."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path("/Users/yaocheng/Desktop/nexus/reppilot")

EXPORTS = {
    "h5": {
        "json": Path(
            "/Users/yaocheng/.cursor/projects/Users-yaocheng-Desktop-nexus-discussionGroup/agent-tools/23181aca-d523-4090-a589-809015530f78.txt"
        ),
        "package_name": "@reppilot/h5",
        "description": "RepPilot H5 用户端（移动浏览器/PWA）",
        "port": 5173,
    },
    "web": {
        "json": Path(
            "/Users/yaocheng/.cursor/projects/Users-yaocheng-Desktop-nexus-discussionGroup/agent-tools/98dcb26c-d6e0-4057-9baf-2535b6aad4e9.txt"
        ),
        "package_name": "@reppilot/web",
        "description": "RepPilot Web 用户端（桌面浏览器）",
        "port": 5174,
    },
    "admin": {
        "json": Path(
            "/Users/yaocheng/.cursor/projects/Users-yaocheng-Desktop-nexus-discussionGroup/agent-tools/373606c0-998a-4777-9aea-b498464c8816.txt"
        ),
        "package_name": "@reppilot/admin",
        "description": "RepPilot Admin 后台（admin.reppilot.com）",
        "port": 5175,
    },
}

VITE_CONFIG = """import {{ defineConfig }} from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({{
  plugins: [react()],
  server: {{
    port: {port},
    host: true,
  }},
}})
"""

INDEX_HTML = """<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title}</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/index.tsx"></script>
  </body>
</html>
"""

TSCONFIG = """{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": false,
    "noUnusedParameters": false
  },
  "include": ["src"]
}
"""

POSTCSS = """export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
"""

GITIGNORE = """node_modules/
dist/
.DS_Store
*.local
.env
.env.*
"""

README_TEMPLATE = """# {title}

{description}

> UI 原型来自 [Magic Patterns](https://www.magicpatterns.com)，Editor ID: `{editor_id}`

## 开发

```bash
npm install
npm run dev
```

默认端口: **{port}**

## 说明

- 当前为 **Magic Patterns 导出原型**，含 mock 数据与本地 state 导航
- 生产化时需对接 FastAPI 后端、替换 mock 数据、接入真实鉴权
- 产品规格见 `docs/product/`（discussionGroup 仓库同步）

## Magic Patterns 来源

| 项 | 值 |
|----|-----|
| Editor | [{editor_url}]({editor_url}) |
| Artifact | `{artifact_note}` |
"""


def load_export(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data["files"]


def write_files(base: Path, files: list[dict]) -> None:
    src = base / "src"
    src.mkdir(parents=True, exist_ok=True)
    for item in files:
        rel = item["name"]
        if rel == "package.json":
            (base / "package.json").write_text(item["content"], encoding="utf-8")
            continue
        if rel == "tailwind.config.js":
            (base / "tailwind.config.js").write_text(item["content"], encoding="utf-8")
            continue
        target = src / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(item["content"], encoding="utf-8")


def patch_package_json(pkg_path: Path, meta: dict) -> None:
    pkg = json.loads(pkg_path.read_text(encoding="utf-8"))
    pkg["name"] = meta["package_name"]
    pkg["version"] = "0.1.0"
    pkg["type"] = "module"
    pkg["scripts"] = {
        "dev": "vite",
        "build": "vite build",
        "preview": "vite preview",
    }
    pkg.setdefault("devDependencies", {})
    pkg["devDependencies"].update(
        {
            "@types/react": "^18.3.12",
            "@types/react-dom": "^18.3.1",
            "@vitejs/plugin-react": "^4.3.4",
            "autoprefixer": "^10.4.20",
            "postcss": "^8.4.49",
            "tailwindcss": "^3.4.17",
            "typescript": "^5.7.2",
            "vite": "^6.0.3",
        }
    )
    pkg_path.write_text(json.dumps(pkg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def patch_tailwind(base: Path) -> None:
    cfg = base / "tailwind.config.js"
    if not cfg.exists():
        return
    text = cfg.read_text(encoding="utf-8")
    if "content:" not in text:
        text = text.replace(
            "export default {",
            "/** @type {import('tailwindcss').Config} */\nexport default {\n  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],",
            1,
        )
        cfg.write_text(text, encoding="utf-8")


def main() -> int:
    ROOT.mkdir(parents=True, exist_ok=True)

    editor_ids = {
        "h5": "8fhtf7e7nwwhyqedsfjyxq",
        "web": "fmym8gyxshrrcbyoulnjdu",
        "admin": "tqyr3td9fnwxd1aqhjnvj5",
    }

    for folder, meta in EXPORTS.items():
        base = ROOT / folder
        files = load_export(meta["json"])
        write_files(base, files)
        patch_package_json(base / "package.json", meta)
        patch_tailwind(base)

        (base / "vite.config.ts").write_text(
            VITE_CONFIG.format(port=meta["port"]), encoding="utf-8"
        )
        (base / "index.html").write_text(
            INDEX_HTML.format(title=meta["description"]), encoding="utf-8"
        )
        (base / "tsconfig.json").write_text(TSCONFIG, encoding="utf-8")
        (base / "postcss.config.js").write_text(POSTCSS, encoding="utf-8")
        (base / ".gitignore").write_text(GITIGNORE, encoding="utf-8")

        eid = editor_ids[folder]
        (base / "README.md").write_text(
            README_TEMPLATE.format(
                title=meta["description"],
                description=meta["description"],
                editor_id=eid,
                port=meta["port"],
                editor_url=f"https://www.magicpatterns.com/c/{eid}",
                artifact_note="见 Magic Patterns 编辑器版本历史",
            ),
            encoding="utf-8",
        )
        print(f"✓ {folder}: {len(files)} files")

    # Root README
    (ROOT / "README.md").write_text(
        """# RepPilot — 代码仓库

医药代表智能助手 RepPilot 前端 monorepo。产品规格与规划文档在 [discussionGroup](../discussionGroup/projects/pharma-rep-agent/)。

## 目录

| 目录 | 说明 | 域名 | 端口 |
|------|------|------|------|
| [`h5/`](./h5/) | 用户端 H5（移动浏览器/PWA） | m.reppilot.com | 5173 |
| [`web/`](./web/) | 用户端 Web（桌面浏览器） | app.reppilot.com | 5174 |
| [`admin/`](./admin/) | 后台 Admin | admin.reppilot.com | 5175 |

## 快速开始

```bash
cd h5 && npm install && npm run dev    # http://localhost:5173
cd web && npm install && npm run dev   # http://localhost:5174
cd admin && npm install && npm run dev # http://localhost:5175
```

## 设计风格

- **h5 / web**：Apple Health Warmth（温暖、关怀）
- **admin**：Ops Console · Review Clarity（运营效率、审核清晰）

## Magic Patterns 设计稿

| 端 | Editor |
|----|--------|
| H5 | [8fhtf7e7nwwhyqedsfjyxq](https://www.magicpatterns.com/c/8fhtf7e7nwwhyqedsfjyxq) |
| Web | [fmym8gyxshrrcbyoulnjdu](https://www.magicpatterns.com/c/fmym8gyxshrrcbyoulnjdu) |
| Admin | [tqyr3td9fnwxd1aqhjnvj5](https://www.magicpatterns.com/c/tqyr3td9fnwxd1aqhjnvj5) |

## 文档

- [用户端 Spec](../discussionGroup/projects/pharma-rep-agent/product/spec.md)
- [Admin Spec](../discussionGroup/projects/pharma-rep-agent/product/admin-spec.md)
- [开发 Plan](../discussionGroup/projects/pharma-rep-agent/plans/plan.md)
- [技术架构](../discussionGroup/projects/pharma-rep-agent/tech/architecture.md)
""",
        encoding="utf-8",
    )

    (ROOT / ".gitignore").write_text(GITIGNORE, encoding="utf-8")
    print(f"\nDone → {ROOT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
