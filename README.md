# GLD Platform

Streamlit app displaying GLD availability data from Databricks with AG Grid.

## Setup

```bash
uv sync
```

## Environment Variables

```
DATABRICKS_SERVER_HOSTNAME=<hostname>
DATABRICKS_HTTP_PATH=<http-path>
DATABRICKS_CLIENT_ID=<client-id>
DATABRICKS_CLIENT_SECRET=<client-secret>
```

## Run Locally

```bash
uv run streamlit run app.py
```

## Deploy to Posit Connect

```bash
rsconnect deploy streamlit -n <server-name> app.py
```
