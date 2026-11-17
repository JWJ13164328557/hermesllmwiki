#!/usr/bin/env python3
"""PlantSciKB 流水线存活告警。

背景：调度器寄生在 WSL 内的 hermes-gateway 进程；WSL 空闲约 60s 即整机 poweroff，
若无人使用 WSL，08:00 任务根本不会触发。此脚本用「最后一份 summary.json 的年龄」
作为客观存活证据，超过阈值就推送飞书，避免再次静默停摆。

退出码：0=健康；1=已告警；2=告警发送失败
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime, timedelta

BASE = os.environ.get("KB_BASE", "/mnt/g/hermes_obsidian/hermes")
LOG_DIR = os.path.join(BASE, "logs", "pipeline")
STATE = os.path.join(LOG_DIR, ".health_alert_state.json")
HERMES_PY = "/home/jiwj/miniconda3/envs/hermes/bin/python3"
DEFAULT_TARGET = "feishu:oc_2f31de60dc8655fe4454b1283fcd8b3f"


def newest_summary():
    best, best_m = None, -1.0
    try:
        runs = os.listdir(LOG_DIR)
    except OSError:
        return None, None
    for name in runs:
        f = os.path.join(LOG_DIR, name, "summary.json")
        if not os.path.isfile(f):
            continue
        m = os.path.getmtime(f)
        if m > best_m:
            best, best_m = f, m
    if not best:
        return None, None
    try:
        with open(best, encoding="utf-8") as fh:
            return best, json.load(fh)
    except Exception:
        return best, None


def human_age(seconds):
    days, rem = divmod(int(seconds), 86400)
    hours, rem = divmod(rem, 3600)
    mins = rem // 60
    parts = []
    if days:
        parts.append(str(days) + " 天")
    if hours or days:
        parts.append(str(hours) + " 小时")
    parts.append(str(mins) + " 分")
    return " ".join(parts)


def send(text, target, dry_run):
    if dry_run:
        print("[dry-run] would send to " + target)
        print(text)
        return True
    cmd = [HERMES_PY, "-m", "hermes_cli.main", "send", "--to", target, text]
    try:
        r = subprocess.run(cmd, cwd="/home/jiwj/.hermes",
                           capture_output=True, text=True, timeout=120)
    except Exception as exc:
        print("[health] send exception: " + str(exc), file=sys.stderr)
        return False
    if r.returncode != 0:
        print("[health] send failed rc=" + str(r.returncode), file=sys.stderr)
        print((r.stderr or "")[:800], file=sys.stderr)
        return False
    print("[health] alert sent")
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-age-hours", type=float, default=36.0)
    ap.add_argument("--target", default=DEFAULT_TARGET)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true", help="忽略当日去重，强制发送")
    args = ap.parse_args()

    now = time.time()
    path, summary = newest_summary()
    if path is None:
        age = None
        last = "无任何 summary.json"
    else:
        age = now - os.path.getmtime(path)
        last = datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m-%d %H:%M")

    healthy = age is not None and age <= args.max_age_hours * 3600
    if healthy:
        print("[health] OK — 最近一次成功运行 " + last + "（" + human_age(age) + " 前）")
        return 0

    today = datetime.now().strftime("%Y-%m-%d")
    if not args.force and os.path.isfile(STATE):
        try:
            with open(STATE, encoding="utf-8") as fh:
                if json.load(fh).get("last_alert_day") == today:
                    print("[health] 今日已告警过，跳过")
                    return 1
        except Exception:
            pass

    lines = ["[PlantSciKB 告警] 每日文献流水线疑似停摆"]
    if age is None:
        lines.append("- 最近成功运行：" + last)
    else:
        lines.append("- 最近成功运行：" + last + "（" + human_age(age) + " 前，阈值 "
                     + str(int(args.max_age_hours)) + " 小时）")
        lines.append("- 产物：" + path)

    if summary:
        deg = summary.get("degraded") or []
        fail = summary.get("failures") or []
        lines.append("- 上次新增论文页：" + str(summary.get("new_pages", "?")))
        lines.append("- 上次全文获取：" + str(summary.get("fulltext_acquired", "?"))
                     + "/" + str(summary.get("pdf_candidates", "?")))
        if deg:
            lines.append("- 上次降级项 " + str(len(deg)) + " 条："
                         + "；".join(str(x)[:60] for x in deg[:3]))
        if fail:
            lines.append("- 上次失败阶段：" + ", ".join(map(str, fail[:5])))

    try:
        du = shutil.disk_usage("/mnt/g")
        lines.append("- G: 剩余 %.1f GB（已用 %.0f%%）" % (du.free / 1024.0 ** 3, du.used * 100.0 / du.total))
    except Exception:
        pass

    lines.append("- 排查：wsl.exe -d Ubuntu -- uptime ；schtasks /query /tn Hermes-PlantSciKB-Daily /v /fo list"
                 " ；日志目录 " + LOG_DIR)
    text = "\n".join(lines)
    print(text)

    ok = send(text, args.target, args.dry_run)
    if ok:
        if not args.dry_run:
            try:
                with open(STATE, "w", encoding="utf-8") as fh:
                    json.dump({"last_alert_day": today,
                               "alerted_at": datetime.now().isoformat()}, fh)
            except Exception:
                pass
        return 1
    return 2


if __name__ == "__main__":
    sys.exit(main())
