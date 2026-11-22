#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
if ! command -v java >/dev/null || ! command -v javac >/dev/null; then echo "Instala JDK antes de gerar o APK." >&2; exit 2; fi
if [[ -z "${ANDROID_HOME:-${ANDROID_SDK_ROOT:-}}" ]]; then echo "Define ANDROID_HOME ou ANDROID_SDK_ROOT para um Android SDK instalado." >&2; exit 2; fi
cd "$ROOT"
pnpm install --frozen-lockfile
pnpm android:sync
cd frontend/android
./gradlew assembleDebug
printf 'APK gerado em: %s\n' "$ROOT/frontend/android/app/build/outputs/apk/debug/app-debug.apk"
