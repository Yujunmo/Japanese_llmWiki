#!/usr/bin/env python3
"""PreToolUse 훅: raw/ 아래 파일 수정을 차단한다.

CLAUDE.md 3계층 원칙 — raw/는 불변 소스. 유일한 예외는 /ingest 마지막 단계의
`ingested: false -> true` 플래그 플립(단일 Edit) 뿐이다.
"""
import json
import os
import re
import sys


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # 파싱 실패 시 개입하지 않음

    tool = data.get("tool_name", "")
    ti = data.get("tool_input", {}) or {}
    path = ti.get("file_path") or ti.get("notebook_path")
    if not path:
        sys.exit(0)

    root = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or ""
    raw_dir = os.path.realpath(os.path.join(root, "raw"))
    target = os.path.realpath(path if os.path.isabs(path) else os.path.join(root, path))
    if not (target == raw_dir or target.startswith(raw_dir + os.sep)):
        sys.exit(0)  # raw/ 밖 -> 허용

    # 예외: ingested 플래그 플립(false -> true)만 허용
    if tool == "Edit":
        old = (ti.get("old_string") or "").strip()
        new = (ti.get("new_string") or "").strip()
        if re.fullmatch(r"ingested:\s*false", old) and re.fullmatch(r"ingested:\s*true", new):
            sys.exit(0)

    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": (
            "raw/는 불변 소스입니다 (CLAUDE.md 3계층 원칙). "
            "허용되는 유일한 변경은 /ingest의 ingested: false→true 플래그 플립뿐입니다."
        ),
    }}))
    sys.exit(0)


if __name__ == "__main__":
    main()
