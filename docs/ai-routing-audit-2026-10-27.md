# AI 官方 App / Bot 分流核对准备

核查日期：2026-10-27（Asia/Shanghai）。本次只更新图标与公开资料记录，尚未修改任何用户代理配置；覆盖结论以随后提供的最新版 QX / Clash 配置为准。

## 产品与域名证据

| 拟用策略 | 官方产品 / Agent | 已核实的域名或连接范围 | 后续核对重点 |
|---|---|---|---|
| Muse | Meta 的 Muse from Meta；独立 App、Web、WhatsApp 入口 | `muse.ai`，含官方 `introducing.muse.ai`、`security.muse.ai` | 官方说明 App / Web 客户端直连专用 VM，但未公布完整客户端网络白名单。VM、附件、认证依赖需结合连接日志核实；不能将全部 Facebook / Instagram CDN 并入 Muse。 |
| Manus | Manus、Manus Studio，以及官方独立 Agent App **Cue by Manus** | `manus.im`；官网资源使用 `files.manuscdn.com`；官网链接到 `open.manus.ai`；官方 Cue 入口为 `cue.im` | 基础候选为 `manus.im`、`manuscdn.com`、精确主机 `open.manus.ai`、`cue.im`。Cue 的其他后端 / 附件域名仍待日志确认。App 共用基础设施不代表一定共用全部域名。 |
| Grok | Grok App / Web，以及独立 **Grok Bot** | Grok：`grok.com`、`x.ai`；官方统一登录文档另列 `accounts.spacex.ai`、`grokusercontent.com`。Grok Bot：`cursor.sh`、`cursor-cdn.com`、`cursorapi.com`、`cursorvm.com`，安装更新涉及 `cursor.com`、`downloads.cursor.com` | Bot 的聊天与云电脑不只使用 Grok 品牌域名。Cursor 域名也供 Cursor 编辑器使用，域名分流会同时影响两者；合并到 Grok 前要明确这项影响。官方已预告 10 月 30 日登录域名迁移，保留旧登录与新增登录的核对。 |
| ChatGPT | ChatGPT App / Web、**Dots**；同时核对 Codex / Work | Dots 由 ChatGPT 提供，并非必须另装一个 Dots App。官方网络说明列 `chatgpt.com`、`openai.com`、`oaistatic.com`、`oaiusercontent.com`、`oaistatsig.com`；精确依赖包括 `cdn.openaimerge.com`、`cdn.platform.openai.com` 和若干 WorkOS 主机。WebSocket 为 `ws.chatgpt.com` / `chatgpt.com` | 不能仅凭已经有 ChatGPT 策略组就认定登录、文件、实时消息、语音全覆盖。除直接规则外，还要检查远程 OpenAI 规则集及优先级。共享登录 / 客服 / 支付域名须按具体主机核对，不直接代理整个第三方平台。 |
| Claude | Claude App / Web、Code、Cowork，以及独立 **Claude Duet** | 官方 Duet 页面明确：独立 iOS / Android App；电脑端在 `claude.ai` 使用。官方产品页面为 `claude.com`，静态资源使用 `assets.claude.com` | 若已有 `claude.ai` 域名后缀规则，Duet Web 入口会命中；若已有 `DOMAIN-KEYWORD,claude`，也会匹配含 Claude 的域名。仍需核对原规则、远程列表和 App 实际附件 / 云电脑依赖，不能据官网入口断言 App 完整覆盖。 |

`DOMAIN-SUFFIX,cursorvm.com`（Clash）/ `host-suffix, cursorvm.com`（QX）可匹配多层子域，不能照抄企业网关的“单层通配符”语义。

## 不混淆客户端与云端出站

- 手机 / 电脑的分流只影响本机连接。Agent 在远程 VM 上访问第三方站点，不会自动继承手机的 VPN 出口。
- WhatsApp 中的 Muse、Telegram / LINE 中的 Manus Bot，消息传输先走对应通信平台。普通域名规则不能只识别同一通信平台里的某一个 Bot 对话。
- 不把整个 Apple、Google、Facebook、Cloudflare、Amazon S3、Azure 或 LiveKit 公共域名并入某个 AI；有共享依赖时先核实具体主机。
- 本轮没有安装 / 登录 App，也没有抓取私人连接日志，因此这里是带来源的核对清单，不是已通过播放、语音、附件或 VM 实测的最终规则集。

## 图标路径

Muse、Manus、Grok、Cue、GrokBot 都来自 Apple 官方 Lookup 接口，并核对固定 App ID 与 bundle ID；详见 `icons/apps/ai-appstore-meta.json`。

- Clash：`icons/apps/<Name>.png`，512×512，实际 PNG 编码。
- QX：`icons/qx/apps/<Name>-circle-v2.png`，108×108 RGBA，圆形主体、圆外透明。
- 原始兼容路径：`icons/apps/<Name>.jpg`。
- Dots 暂使用既有 ChatGPT 图标；Claude Duet 暂使用既有 Claude 图标，不伪造独立官方标识。

## 下一轮配置核对

收到最新版后，检查直接规则与远程规则集、重叠和先后顺序、DNS / 附件 / WebSocket / 语音 / 登录的连接范围；新增 Muse、Manus、Grok 三组，Bot 先按所属品牌归组。若遇到共享域名冲突，再单独处理。保留用户现有节点候选和排序，不借本次修改调整其他业务策略。

## 公开来源

- Meta 官方发布（包含 Muse 主域与 WhatsApp 入口）：https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/
- Muse 官方架构（客户端直连 VM）：https://security.muse.ai/
- Manus 官方发布（Cue 与 cue.im 链接）：https://www.manus.im/blog/introducing-manus-2-0
- Manus 官方下载页面（manuscdn / API 链接）：https://www.manus.im/download
- Grok Bot 官方客户端网络要求：https://docs.x.ai/grok-bot/proxies
- 官方统一登录域名与迁移日期：https://docs.x.ai/x-subscription/sign-in-domains
- OpenAI 官方网络要求：https://help.openai.com/en/articles/9247338-network-recommendations-for-chatgpt-errors-on-web-and-apps
- OpenAI Dots 说明：https://help.openai.com/en/articles/20001554-manage-dots-in-chatgpt-workspaces
- Claude Duet 官方产品页：https://claude.com/product/claude-duet
- Apple 官方 App 元数据接口：`https://itunes.apple.com/lookup?id=<trackId>&country=us`
