#!/usr/bin/env bash
# Arranca uvicorn, espera /api/health, ejecuta el comando dado y apaga el servidor.
PORT=${PORT:-8000}
PYTHONPATH=. python3 -m uvicorn backend.app.main:app --port $PORT --log-level warning &
PID=$!
for i in $(seq 1 120); do curl -sf localhost:$PORT/api/health >/dev/null && break; sleep 1; done
"$@"; RC=$?
kill $PID; wait $PID 2>/dev/null
exit $RC
