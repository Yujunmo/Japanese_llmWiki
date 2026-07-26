---
기록일자: 2026-07-26
last_seen:          # 복습 시 갱신 (YYYY-MM-DD), 승격 시엔 공백
복습횟수: 0          # 복습완료 버튼 누를 때마다 +1, 승격 시 0
tags:              # 출처를 포함 (예: [요루시카])
---

# 관용어 (후리가나)

(3~4줄 이내 설명 — 의미 + 유래/뉘앙스)

## 후리가나


## 예문
1.  — 
2.  — 
3.  — 

## 포함 단어 풀이
- 단어（요미） — 뜻 (JLPT 레벨)

```meta-bind-button
label: ✅ 복습완료 (오늘로)
style: primary
actions:
  - type: updateMetadata
    bindTarget: last_seen
    evaluate: true
    value: "moment().format('YYYY-MM-DD')"
  - type: updateMetadata
    bindTarget: 복습횟수
    evaluate: true
    value: "(x ?? 0) + 1"
```
마지막 복습: `VIEW[{last_seen}]` · 복습 `VIEW[{복습횟수}]`회
