# mcd-demo
Testing creation of simple MCD servers and integrating with LangChain agent

## Prerequisites

### Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Running the agent

### Start the MCP servers
You have to start all three MCP servers before starting the agent. Each server listens on a separate port. You can start them in separate terminals or run them in the background. To run in the background, do the following:

```bash
python weather_server.py &
python math_server.py &
python telemetry_server.py &
```

### Start the agent
```bash
python agent.py
```

## Killing the MCP servers

```bash
pkill -9 -f weather_server.py
pkill -9 -f math_server.py
pkill -9 -f telemetry_server.py
```
