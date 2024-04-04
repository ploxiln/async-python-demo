#!/bin/sh
exec uvicorn --host=0.0.0.0 --port=${PORT:-4000} --workers=1 app:app
