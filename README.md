# Python Sidecars for Tianshu

Python HTTP 服务集合，为 [Tianshu](https://github.com/tianshu-ai/tianshu) 提供本地 AI 能力。

## 服务

### decision/ — 决策模型服务

基于 Clef/Laya 的快速决策模型，用于 worker 路由、意图分类等。

- 端口：8710
- API：`POST /v1/systemone`（Jev/SystemOne 兼容）
- 模型：Clef-flash (9B) / Clef (27B) / Laya

```bash
cd decision
bash install.sh    # 安装依赖 + 下载模型
bash start.sh      # 前台启动
bash start.sh --background  # 后台启动
```

### tts/ — 语音合成服务

基于 Qwen3-TTS 的本地语音合成。

- 端口：50000
- API：`POST /tts`
- 后端：MLX (Apple Silicon) / PyTorch (Linux GPU/CPU)

```bash
cd tts
bash install.sh    # 安装依赖 + 下载模型
bash start.sh      # 前台启动
bash start.sh --background  # 后台启动
```

## 部署

每个服务独立 venv，互不影响：

| 服务 | venv 路径 | 模型路径 |
|---|---|---|
| decision | `~/.tianshu/clef-decision-venv` | `~/.tianshu/clef-models` |
| tts | `~/.tianshu/qwen-tts-venv` | HuggingFace cache |

## License

Apache-2.0
