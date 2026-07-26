# 일본어 LLM 위키

일상에서 발견한 일본어 **단어·관용어**를 구조화하고 상호연결해, 시간이 지날수록 풍부해지는 개인 학습 지식베이스로 축적하는 Obsidian 볼트다.

**LLM 위키 패턴**으로 운영한다 — 관리자는 소스를 모으고 질문하며, **위키의 모든 페이지는 LLM(Claude)이 쓰고 유지한다.** 관리자는 한자에 약하므로 요미가나와 한국 한자 대응을 특히 신경 쓴다.

> 📌 이 파일(README)은 사람이 읽는 개요다. **정확한 스키마·운영 규칙의 정본은 [`CLAUDE.md`](CLAUDE.md)** 이며, 충돌 시 CLAUDE.md를 따른다.

---

## 무엇이 어디에 있나

```
raw/            원본 수집 (날짜별 파일, 불변 소스) — 관리자가 직접 적음
wiki/
  voca/         단어 페이지 (개당 1파일, 예: 袖.md)
  expression/   관용어 페이지 (개당 1파일, 예: 油を売る.md)
MOC/
  주제별/       주제로 묶은 Map of Content (의류, 감정 …)
  품사별/       품사로 묶은 Map of Content (명사, 동사 …)
train/          복습·테스트 산출물 (review.md=오전 복습, train.md=저녁 테스트)
templates/      페이지 템플릿
.claude/skills/ LLM 운영 스킬 (ingest, review)
index.md        위키 전체 카탈로그
log.md          작업 이력 (시간순)
CLAUDE.md       스키마 & 운영 규칙 (정본)
```

3계층 원칙: **raw/** = 소스 오브 트루스(LLM은 읽기만), **wiki·MOC·train** = LLM 산출물, **CLAUDE.md** = 규칙.

---

## 워크플로

### 1. 수집 → 인제스트
`raw/YYYY-MM-DD.md`에 그날 발견한 단어·관용어를 `## vocabulary` / `## expression`로 적어둔다. 그 뒤 **`/ingest <날짜>`** 를 실행하면 LLM이 각 항목을 위키 페이지로 승격한다 — 템플릿에 맞춰 요미가나·한국 한자·예문 3개·상위개념 링크·주제 태그를 채우고, MOC·index·log까지 갱신한다.

### 2. 질의 (Query)
위키에 대해 물어보면 LLM이 `index.md`를 먼저 읽고 관련 페이지를 인용해 답한다. 가치 있는 답변(비교표·정리)은 새 위키 페이지로 파일링된다.

### 3. 린트 (Lint)
"린트"를 요청하면 위키 건강 검진 — 페이지 간 모순, 요미가나·한자 오류, 고아 페이지, 누락된 상호참조·MOC 등록 등을 점검한다.

### 4. 복습 (Review)
하루 단위 복습 루틴:

- **오전**: **`/review`** 실행 → `wiki/voca`의 `last_seen`(마지막 복습일)을 읽어 가장 오래되거나 미복습인 단어 **10개를 랜덤 추출**해 `train/review.md`에 담는다. 이 파일로 복습한다.
- **저녁**: `train/train.md`(전일 오전에 복습했던 10개)로 테스트한다.
- `/review`를 실행하면 직전 `review.md`가 `train.md`로 이월되면서 세대가 한 칸씩 밀린다. **review 스킬은 wiki를 읽기만 한다.**

각 단어·관용어 페이지 **맨 아래에는 복습완료 버튼**이 있다. 페이지를 열어 복습한 뒤 누르면 `last_seen`이 오늘 날짜로, `복습횟수`가 +1로 갱신된다.

---

## Obsidian 플러그인 (복습완료 버튼용)

복습완료 버튼은 [Meta Bind](https://www.moritzjung.dev/obsidian-meta-bind-plugin-docs/) 로 동작한다. 아래를 설정해야 버튼이 작동한다:

1. **Meta Bind** + **JS Engine** 커뮤니티 플러그인 설치·활성화
2. Meta Bind 설정에서 **JavaScript(JS evaluation) 활성화**
3. Meta Bind **날짜 포맷 = `YYYY-MM-DD`** (복습 추출 정렬과 맞추기 위함)

---

## 관리자 프로필

프로그래머 / JLPT N3 / 일상 회화 가능 / 한자 약함. 그래서 모든 페이지에 **요미가나**와 **한국 한자 대응**(예: `袖 — 소매 수`)을 빠짐없이 채운다.
