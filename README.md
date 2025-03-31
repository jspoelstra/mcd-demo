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

### Set Environment variables

Set the following environment variables. Get the values from Azure AI Foundry where the models are deployed:

```bash
export AZURE_OPENAI_API_KEY=<your_azure_openai_api_key>
export AZURE_OPENAI_ENDPOINT=<your_azure_openai_endpoint>
```

Optionally, you can set the following environment variables to configure the MCP servers:

```bash
export MCP_MATH_URI=http://<server-uri>:5001/sse
```

> **Note**: You can also set these variables in a `.env` file in the root directory of the project.

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
