# Demo Video 01 Script

## Title

```text
AI Agent มีสมองอย่างเดียวไม่พอ — ต้องมี Rails, Brakes, Sensors, Quality
```

## Goal

Explain the Hermes + Nami Harness model and show the first working v0.0.1 runtime example.

## Target Length

```text
3-5 minutes
```

## Hook

```text
หลายคนสร้าง AI agent ให้คิดและทำงานแทนเราได้
แต่คำถามคือ ถ้ามันทำพลาด ใครเป็นคนเบรก?

นี่คือเหตุผลที่ผมแยก Hermes กับ Nami Harness ออกจากกัน
```

## Core Explanation

```text
Hermes คือสมอง
- คิด
- วางแผน
- เลือก tool
- delegate งาน
- เรียก worker

Nami Harness คือระบบควบคุม
- rails: ใครทำอะไรได้บ้าง
- brakes: เมื่อไหร่ต้องหยุด
- sensors: log และ audit trail
- quality: output ผ่านเกณฑ์หรือยัง
```

## Visual Flow

```text
User task
  -> Hermes plans
  -> Harness rails authorize
  -> Worker executes
  -> Harness quality validates
  -> Harness sensors record event
  -> Result ships
```

## Demo Steps

### Step 1 — Open Repository

Show:

```text
https://github.com/paopaonyapi-creator/nami-harness
```

Say:

```text
นี่คือ repo v0.0.1 ของ Nami Harness เป็น skeleton แรกสำหรับ Harness Engineering
```

### Step 2 — Show README Model

Say:

```text
ประโยคหลักคือ Hermes = brain และ Harness = rails, brakes, sensors, quality
```

### Step 3 — Show Runtime Example

File:

```text
examples/hermes_worker_guard.py
```

Say:

```text
ตัวอย่างนี้ wrap Hermes-style worker ด้วย HarnessRuntime
ก่อน worker จะทำงาน ต้องผ่าน policy และหลังทำงาน output ต้องผ่าน quality gate
```

### Step 4 — Run Example

Command:

```powershell
python examples\hermes_worker_guard.py
```

Expected output:

```text
Hermes processed: summarize the service health report
```

### Step 5 — Show Tests

Command:

```powershell
python -m pytest
```

Expected output:

```text
14 passed
```

## Key Talking Points

```text
1. Agentic systems need control planes, not just prompts.
2. Rails prevent unauthorized actions.
3. Brakes stop runaway or unsafe execution.
4. Sensors make behavior auditable.
5. Quality gates prevent bad output from shipping.
6. This is v0.0.1, intentionally small and easy to extend.
```

## CTA

```text
ถ้าสนใจแนวคิด Harness Engineering สำหรับ AI agents ดู repo ได้ที่:
https://github.com/paopaonyapi-creator/nami-harness

ผมจะต่อ v0.1 ด้วย rate limits, budget guard, sensor schema และ Hermes integration demo
```

## Short Version Script

```text
AI agent ไม่ควรมีแค่สมอง
มันต้องมีระบบควบคุมด้วย

Hermes คือสมองที่คิด วางแผน และสั่ง worker
Nami Harness คือราง เบรก เซนเซอร์ และระบบตรวจคุณภาพ

v0.0.1 ตอนนี้ปล่อยเป็น open-source แล้ว มี rails, brakes, sensors, quality และ runtime example

Repo อยู่ที่ github.com/paopaonyapi-creator/nami-harness
```

## Recording Checklist

```text
[ ] Open GitHub repo
[ ] Show README core model
[ ] Show runtime.py or example file
[ ] Run example
[ ] Run tests or show test result
[ ] End with repo URL
```
