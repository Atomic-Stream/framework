---
framework_layer: artefacts
maintained_by: Stream Orchestrator
impact_if_wrong: "The Scribe loses track of the initiative's state, leading to skipped governance gates, missed validations, and silent system failures."
change_process: "Requires pull request reviewed by Stream Orchestrator and Platform Engineering."
---

# Stream Ledger: [Initiative Name]

**Accountable Orchestrator:** [Name]
**Date Initiated:** [Timestamp]
**System of Record ID:** [Jira Epic ID / Linear Issue ID]

## Initiative Context
*Link to the overarching business goal this loop serves.*
* **Target Outcome:** [Brief description]

---

## The 6-Step Loop Checkpoints

*The Scribe monitors these checkpoints. An agent cannot proceed to the next step until the current step is marked complete and audited by an Artefact Checker.*

### [ ] Step 1: Initiative
- [ ] `Outcome Brief` created and logged.
- [ ] Artefact Checker validation: PASS.

### [ ] Step 2: Intent
- [ ] `Intent Brief` generated for specific feature/lever.
- [ ] Artefact Checker validation: PASS.

### [ ] Step 3: Proof of Concept
- [ ] Pilot Developer / Worker Agents execute research/prototype.
- [ ] `Evidence Pack` generated and logged.
- [ ] Artefact Checker validation: PASS.
- [ ] Product Council Go/No-Go decision captured by Scribe.

### [ ] Step 4: Build
- [ ] Code generated and logic map updated.
- [ ] `Build Record` generated.
- [ ] Code Checker validation: PASS (No boundary/security violations).

### [ ] Step 5: Release
- [ ] `Release Record` generated.
- [ ] Tier 3 Approver sign-off logged (if applicable).
- [ ] Code deployed behind feature flag.

### [ ] Step 6: Feedback
- [ ] Post-release telemetry and user data gathered.
- [ ] `Feedback Pack` generated.
- [ ] Evaluated against Step 1 Outcome target.

---

## Scribe Watchdog Triggers (Work in Progress)
*Below are the known events the Scribe must listen for during this Epic. We will expand this list as we draft the remaining artefacts.*

1. **Event:** Worker Agent POSTs an Evidence Pack. 
   **Action:** Scribe routes to Evidence Pack template, checks Step 3 box, triggers Artefact Checker.
2. **Event:** Artefact Checker POSTs a 'Fail' status.
   **Action:** Scribe pauses Epic progression, posts Escalation to Slack, awaits human unblock reply.
