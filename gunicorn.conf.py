# Gunicorn configuration file for Render deployment
# This file is automatically loaded by Gunicorn when starting up.

import os

# Bind to 0.0.0.0 and the port specified by Render (default to 8000)
bind = f"0.0.0.0:{os.environ.get('PORT', '8000')}"

# Use the Uvicorn ASGI worker class so that Gunicorn can run the FastAPI ASGI app
worker_class = "uvicorn.workers.UvicornWorker"

# Adjust timeout for LLM agent processing
timeout = 120

# Number of worker processes
workers = int(os.environ.get("WEB_CONCURRENCY", 2))

