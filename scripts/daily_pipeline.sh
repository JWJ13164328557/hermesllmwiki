#!/usr/bin/env bash
# PlantSciKB 每日文献流水线 —— 唯一的 shell 入口
#
# 用法:
#   scripts/daily_pipeline.sh [任意 daily_full_pipeline.py 参数]
#
# 示例:
#   scripts/daily_pipeline.sh --dry-run            # 只看阶段计划
#   scripts/daily_pipeline.sh --check              # 只做预检
#   scripts/daily_pipeline.sh --only phase3_pubmed --no-git
#   scripts/daily_pipeline.sh --resume             # 断点续跑当日
#   KB_BASE=/path/to/your/kb scripts/daily_pipeline.sh
#
# 约定:
#   * KB_BASE 指定知识库根；未设置时回落到本仓库根目录。
#   * 退出码直接透传 daily_full_pipeline.py:
#       0 成功 / 1 必需阶段失败 / 2 参数或预检失败 / 3 已有实例在运行
#   * 不使用 "echo EXIT_CODE=$?"。旧写法会让 cron 永远看到成功，
#     因此此处改为经 tee 记录日志后取 PIPESTATUS[0] 作为真实退出码。

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# 知识库根目录：KB_BASE > APP_DIR > 仓库根
KB_BASE="${KB_BASE:-${APP_DIR:-${REPO_ROOT}}}"
export KB_BASE
export APP_DIR="${KB_BASE}"          # 兼容仍读取 APP_DIR 的旧脚本

# cron 环境几乎为空：证书、编码、缓冲都要显式声明。
# 证书按「当前 conda/venv 自带 → 系统 CA」顺序探测，不写死任何个人路径。
if [ -z "${SSL_CERT_FILE:-}" ]; then
  for cand in "${CONDA_PREFIX:-/nonexistent}/ssl/cert.pem" /etc/ssl/certs/ca-certificates.crt; do
    if [ -f "${cand}" ]; then
      export SSL_CERT_FILE="${cand}"
      break
    fi
  done
fi
if [ -f /etc/ssl/certs/ca-certificates.crt ]; then
  export CURL_CA_BUNDLE="${CURL_CA_BUNDLE:-/etc/ssl/certs/ca-certificates.crt}"
  export REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-${CURL_CA_BUNDLE}}"
fi
export PYTHONIOENCODING="${PYTHONIOENCODING:-utf-8}"
export PYTHONUNBUFFERED=1

PYTHON_BIN="${PYTHON_BIN:-python3}"
LOG_DIR="${KB_BASE}/logs/pipeline"
mkdir -p "${LOG_DIR}"

# 日志轮转：每天一个文件，只保留最近 ${KB_LOG_KEEP} 个（默认 30）。
# 旧实现是单个 4.7 MB 的 daily_cron.log 从不轮转，最后写到磁盘都没人看。
KB_LOG_KEEP="${KB_LOG_KEEP:-30}"
if [ "${KB_LOG_KEEP}" -gt 0 ]; then
  # shellcheck disable=SC2012
  ls -1t "${LOG_DIR}"/cron_*.log 2>/dev/null | tail -n +$((KB_LOG_KEEP + 1)) | while read -r old; do
    rm -f -- "${old}"
  done
fi

LOG_FILE="${LOG_DIR}/cron_$(date +%Y-%m-%d_%H%M%S).log"

cd "${REPO_ROOT}" || exit 2

echo "[daily_pipeline] KB_BASE=${KB_BASE}" | tee -a "${LOG_FILE}"
echo "[daily_pipeline] python=${PYTHON_BIN} -> $(command -v "${PYTHON_BIN}" || echo 'not found')" \
  | tee -a "${LOG_FILE}"

"${PYTHON_BIN}" -u "${SCRIPT_DIR}/daily_full_pipeline.py" "$@" 2>&1 | tee -a "${LOG_FILE}"
CODE="${PIPESTATUS[0]}"

echo "[daily_pipeline] exit=${CODE}" | tee -a "${LOG_FILE}"
exit "${CODE}"