# Clef Sidecar

Lightweight HTTP server that wraps Clef/Clef-flash decision models, exposing a Jev/SystemOne-compatible `/v1/systemone` API.

Designed to run alongside [Tianshu](https://github.com/tianshu-ai/tianshu) as a decision model backend for the `decision` plugin.

## Quick Start

```bash
# Create venv and install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Download model (first time only)
python3 download_model.py

# Start server
python3 server.py --port 8710
```

## API

### POST /v1/systemone

Jev/SystemOne-compatible decision endpoint.

```bash
curl -X POST http://127.0.0.1:8710/v1/systemone \
  -H "Content-Type: application/json" \
  -d '{
    "model": "clef-flash",
    "state": "帮我写一个 Python 脚本",
    "questions": {
      "route": {
        "type": "choice",
        "instructions": "Which worker should handle this?",
        "criteria": {
          "coder": "Code generation and debugging",
          "researcher": "Web search and research",
          "main": "General conversation"
        }
      }
    }
  }'
```

### GET /health

Health check endpoint.

## Models

| Model | Size | Latency (MPS) | Accuracy |
|---|---|---|---|
| Clef-flash (9B) | ~18GB | ~220ms | Excellent |
| Clef (27B) | ~54GB | ~500ms | Best |
| Laya (~1B) | ~1.5GB | ~47ms | Good (70%) |

## Configuration

| Env | Default | Description |
|---|---|---|
| `CLEF_MODEL_DIR` | auto-detect | Path to model directory |
| `CLEF_PORT` | 8710 | Server port |
| `CLEF_DEVICE` | auto (mps > cuda > cpu) | Torch device |
| `CLEF_MODEL` | clef-flash | Model to load |

## Deployment

### macOS (launchd)

```bash
# Install as a service
cp com.tianshu.clef-sidecar.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.tianshu.clef-sidecar.plist
```

### Linux (systemd)

```bash
sudo cp clef-sidecar.service /etc/systemd/system/
sudo systemctl enable --now clef-sidecar
```

### Docker

```bash
docker build -t clef-sidecar .
docker run -p 8710:8710 --gpus all clef-sidecar
```

## License

Apache-2.0
