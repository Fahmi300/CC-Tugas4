#!/bin/sh

. /app/backend/venv/bin/activate
python3 /app/backend/app.py &

cd /app/frontend
npm run dev
