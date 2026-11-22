#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
if [[ -z "${DATABASE_URL:-}" ]]; then
  echo "DATABASE_URL não definida; verificação de conectividade e migrações não pode ser executada." >&2
  exit 2
fi
pnpm install --frozen-lockfile
pnpm build
python3 -m compileall -q backend/app backend/migrations
(
  cd backend
  python3 -m pip install -r requirements.txt
  alembic upgrade head
)
echo "Build frontend e migrações concluídos. Confirma /health/db depois do deploy."
