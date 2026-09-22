# QX-icons

> 面向 **Quantumult X** 的自用图标仓库，同时兼容 Clash Verge / Mihomo 等支持远程图标 URL 的客户端。

[![Sync QX icons](https://github.com/chenran71ran-oss/QX-icons/actions/workflows/sync-icons.yml/badge.svg)](https://github.com/chenran71ran-oss/QX-icons/actions/workflows/sync-icons.yml)

本仓库的目标不是单纯收集图片，而是把不同来源的图标统一整理成 **Quantumult X 可直接引用的稳定格式**：

- App 图标：从 Apple App Store 官方 artwork 自动同步；
- QX 策略组：生成 108×108、RGBA、透明圆形 PNG；
- QX 节点资源 / 订阅：单独生成 144×144、单色透明模板 PNG；
- 国家 / 通用图标：镜像到本仓库，避免配置运行时依赖多个第三方地址；
- 自定义订阅品牌图标：良心云、海獭、月兔、DMIT、RN-VPS。

---

## 目录结构

```text
QX-icons/
├─ .github/
│  └─ workflows/
│     └─ sync-icons.yml
├─ icons/
│  ├─ apps/                 # App Store 原始 artwork（JPG）
│  ├─ subscriptions/        # 自定义订阅品牌源图
│  ├─ utility/              # 国家 / 通用 / 功能图标源图
│  └─ qx/
│     ├─ apps/              # QX 策略组 App 图标：108×108 圆形透明 PNG
│     ├─ subscriptions/     # QX 策略组使用的订阅品牌彩色圆形 PNG
│     ├─ proxy/             # QX [server_remote] 专用单色模板 PNG
│     └─ utility/           # QX 国家 / 通用图标：108×108 PNG
└─ README.md
```

### 目录用途

| 目录 | 用途 | 推荐场景 |
|---|---|---|
| `icons/apps/` | App Store 官方原始 artwork | Clash / 其他支持 JPG 的客户端 |
| `icons/qx/apps/` | 圆形透明 App 图标 | Quantumult X `[policy]` |
| `icons/qx/subscriptions/` | 彩色圆形订阅品牌图标 | QX 策略组中展示机场 / VPS 品牌 |
| `icons/qx/proxy/` | 单色透明模板图标 | Quantumult X `[server_remote]` |
| `icons/qx/utility/` | 国家、自动选择、全局、加密货币等 | QX 通用策略组 |

---

## Quantumult X 图标规则

Quantumult X 的 **策略组图标** 与 **节点资源 / 订阅图标** 不是同一种渲染方式。

### 1. 策略组 `[policy]`

建议使用：

- PNG；
- 108×108；
- RGBA；
- 圆形主体；
- 圆外透明。

示例：

```ini
static=ChatGPT, DMIT-美国-自动, RN｜联通优化, DIRECT, img-url=https://raw.githubusercontent.com/chenran71ran-oss/QX-icons/main/icons/qx/apps/ChatGPT-circle-v2.png
```

常用 App 图标：

| App | 预览 | RAW |
|---|---:|---|
| ChatGPT | <img src="./icons/qx/apps/ChatGPT-circle-v2.png" width="42"> | `icons/qx/apps/ChatGPT-circle-v2.png` |
| Claude | <img src="./icons/qx/apps/Claude-circle-v2.png" width="42"> | `icons/qx/apps/Claude-circle-v2.png` |
| Gemini | <img src="./icons/qx/apps/Gemini-circle-v2.png" width="42"> | `icons/qx/apps/Gemini-circle-v2.png` |
| Google | <img src="./icons/qx/apps/Google-circle-v2.png" width="42"> | `icons/qx/apps/Google-circle-v2.png` |
| Emby | <img src="./icons/qx/apps/Emby-circle-v2.png" width="42"> | `icons/qx/apps/Emby-circle-v2.png` |
| Speedtest | <img src="./icons/qx/apps/Speedtest-circle-v2.png" width="42"> | `icons/qx/apps/Speedtest-circle-v2.png` |
| X | <img src="./icons/qx/apps/X-circle-v2.png" width="42"> | `icons/qx/apps/X-circle-v2.png` |
| Telegram | <img src="./icons/qx/apps/Telegram-circle-v2.png" width="42"> | `icons/qx/apps/Telegram-circle-v2.png` |
| Instagram | <img src="./icons/qx/apps/Instagram-circle-v2.png" width="42"> | `icons/qx/apps/Instagram-circle-v2.png` |

### 2. 节点资源 / 订阅 `[server_remote]`

QX 的 PROXY / 节点资源区域会把图标按**模板 / mask**方式渲染，因此不适合直接放彩色 App 风格图标。

本仓库为这一场景单独维护：

```text
icons/qx/proxy/
├─ Liangxin.png
├─ Haita.png
├─ Yuetutu.png
├─ DMIT.png
└─ RN-VPS.png
```

这些文件为：

- 144×144 PNG；
- 白色图形；
- 透明背景；
- 由 QX 自动按界面颜色着色。

示例：

```ini
https://example.com/subscription, tag=DMIT, img-url=https://raw.githubusercontent.com/chenran71ran-oss/QX-icons/main/icons/qx/proxy/DMIT.png, update-interval=86400, enabled=true
```

### 当前订阅图标

| 订阅 | QX 节点资源图标 |
|---|---:|
| 良心云 | <img src="./icons/qx/proxy/Liangxin.png" width="42"> |
| 海獭 | <img src="./icons/qx/proxy/Haita.png" width="42"> |
| 月兔 | <img src="./icons/qx/proxy/Yuetutu.png" width="42"> |
| DMIT | <img src="./icons/qx/proxy/DMIT.png" width="42"> |
| RN-VPS | <img src="./icons/qx/proxy/RN-VPS.png" width="42"> |

---

## RAW 地址

Quantumult X 推荐直接使用 GitHub RAW：

```text
https://raw.githubusercontent.com/chenran71ran-oss/QX-icons/main/<文件路径>
```

例如：

```text
https://raw.githubusercontent.com/chenran71ran-oss/QX-icons/main/icons/qx/apps/Gemini-circle-v2.png

https://raw.githubusercontent.com/chenran71ran-oss/QX-icons/main/icons/qx/proxy/RN-VPS.png
```

也可以使用 jsDelivr：

```text
https://cdn.jsdelivr.net/gh/chenran71ran-oss/QX-icons@main/<文件路径>
```

但对 Quantumult X 来说，本仓库当前配置优先使用 **`raw.githubusercontent.com`**，主要是为了减少 CDN 缓存导致的图标更新延迟。

---

## Clash Verge / Mihomo

Clash / Mihomo 的策略组可以直接使用 `icon:`：

```yaml
proxy-groups:
  - name: ChatGPT
    type: select
    icon: https://raw.githubusercontent.com/chenran71ran-oss/QX-icons/main/icons/apps/ChatGPT.jpg
    proxies:
      - DIRECT
```

如果希望 Clash 与 QX 视觉一致，也可以直接使用：

```text
icons/qx/apps/ChatGPT-circle-v2.png
```

> `proxy-providers` 本身通常不使用与 QX `[server_remote]` 相同的订阅图标机制；本仓库的 `icons/qx/proxy/` 主要针对 Quantumult X。

---

## 自动同步

仓库通过：

```text
.github/workflows/sync-icons.yml
```

自动维护图标。

当前 Workflow 支持：

- 手动运行 `workflow_dispatch`；
- 每周一自动运行；
- 修改 Workflow 后自动运行；
- 自动提交更新后的图标与元数据。

计划任务：

```text
17 3 * * 1
```

即每周一 **03:17 UTC** 执行。

### App Store 图标

以下 App 通过 Apple iTunes Lookup API 获取当前 artwork：

- ChatGPT
- Claude
- Gemini
- Google
- X
- Telegram
- Instagram
- Reddit
- GitHub
- TikTok
- Emby
- Speedtest
- Netflix

源图保存在：

```text
icons/apps/
```

同步元数据保存在：

```text
icons/apps/appstore-meta.json
```

随后 Workflow 会自动生成 QX 适配版本：

```text
icons/qx/apps/
```

### 国家 / 通用图标

国家、全局、自动选择、加密货币等通用图标会先镜像到本仓库，再生成 QX 版本，因此实际配置不必直接依赖多个第三方仓库。

---

## 自定义订阅图标的更新方式

如果要更换良心云、海獭、月兔、DMIT 或 RN-VPS 的品牌图：

1. 替换 `icons/subscriptions/` 下对应源图；
2. 手动运行 **Sync QX icons**；
3. Workflow 会重新生成：
   - `icons/qx/subscriptions/` 彩色圆形版本；
   - `icons/qx/proxy/` QX 节点资源模板版本。

> `icons/qx/` 下多数文件属于自动生成产物，不建议手工逐个修改，否则下一次 Workflow 运行时可能被覆盖。

---

## QX 图片缓存

Quantumult X 会缓存已加载的远程图标。

如果 GitHub 中的图片已经更新，但 QX 仍显示旧图：

1. 在 Quantumult X 中删除图片缓存；
2. 完全退出 Quantumult X；
3. 重新打开；
4. 必要时重新载入配置 / 更新资源。

对需要强制绕过旧缓存的策略图标，本仓库保留了类似：

```text
ChatGPT-circle-v2.png
Gemini-circle-v2.png
RN-VPS-circle-v2.png
```

这样的版本化文件名。

---

## 图标来源与说明

- App 图标：通过 Apple iTunes Lookup API 获取当前 App Store artwork；
- 国家 / 通用图标：部分来自或镜像自 [Oasisic-Icons](https://github.com/Hawaiine/Oasisic-Icons)；
- Profile / 部分辅助图标：来自 [Orz-3/mini](https://github.com/Orz-3/mini)、[FoKit/Scripts](https://github.com/FoKit/Scripts)；
- 良心云、海獭、月兔、DMIT、RN-VPS：本仓库自定义订阅图标。

本仓库仅用于个人配置、图标整理与客户端适配。各 App、品牌名称、商标及原始 artwork 的权利归其各自权利人所有。

---

## 维护建议

- QX 策略组优先使用 `icons/qx/apps/` 和 `icons/qx/utility/`；
- QX 节点资源订阅必须优先使用 `icons/qx/proxy/`；
- Clash 可直接使用 `icons/apps/` 原始 artwork；
- 修改源图后通过 Workflow 重新生成，不建议手工维护派生文件；
- 配置中优先使用固定、区分大小写的英文文件名。

---

## Repository

https://github.com/chenran71ran-oss/QX-icons
