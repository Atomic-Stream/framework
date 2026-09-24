# The Minimum Viable Stream

*What has to be true on day one. Everything else is added as the Stream grows.*

A Stream does not begin at full size. The smallest arrangement that practises the Atomic Stream is **one Atomic Pair** — one Product Owner and one Pilot Developer — with the Stream Orchestrator and System Architect accountabilities held by named people who may hold other roles.

That arrangement is a Stream if, and only if, these five things are in place from the first day.

---

### 1. A validation gate before any production code

No production code is written against an unvalidated hypothesis. A Proof of Concept — a working prototype, evidence from exposure to real customers, and a stated threshold that would confirm or reject the hypothesis — is brought to a decision before anything is built.

At minimum size the Product Council is two people: the Orchestrator and the Architect accountabilities, whoever holds them. Two voters, neither able to overrule the other, and no agent participating. Disagreement resolves as No-Go and the proposal returns for revision.

*Why this one first: it is the central rule of the framework. A Stream without it is a team using agents quickly.*

### 2. One accountable human per artefact, named

Not a role. Not a team. A person, written down, for every artefact the Stream produces. Agents produce and agents check; no agent closes a decision and no agent is accountable for an outcome.

### 3. The six declarations in version control

`identity/`, `access/`, `knowledge/`, `boundaries/`, `escalation/`, `output/` — held in the same repository as the code, loaded by agents at execution time, changed through review.

At day one these are thin. Thin and written beats complete and verbal. What matters is that the route exists: a rule that lives in someone's head cannot be versioned, reviewed, or inherited by a successor.

### 4. An escalation policy

The conditions that require an agent to halt rather than exercise judgement, and the named person each condition is raised to.

This is the one declaration that ships complete in this repository — see [`foundations/escalation/`](foundations/escalation/). It requires no editing beyond filling in names and deputies in `routing.md`. There is no reason for a Stream to start without it.

### 5. A Feedback Pack that is closed with a decision

After release, signal is gathered and closed with one of three documented decisions: open a new Intent, update an open Intent, or close without action with a stated reason. Never closed by an agent, never closed without a decision.

*Signal that is observed but not decided upon is indistinguishable from signal that was never gathered.*

---

## What is not required on day one

- **The Hydra Model.** Job-sharing is the recommended mechanism for recoverability, not a requirement. The minimum is a documented State of the Union with a named successor, so that every accountability is recoverable by someone else within a working day.
- **Five to eight Pairs.** That is the shape of a mature Stream, not its starting point.
- **A full agent roster.** Start with the agents the first Intent actually needs. Every step of the Loop must have both a worker and a check; how many of each is a matter of the work.
- **Platform Engineering as a separate function.** At minimum size the Architect accountability covers it. The function separates when there is more than one Stream to serve.
- **Tooling of any particular kind.** The framework requires version control, review, and an open route to propose change. It does not require a particular product.

---

## How to tell it has stopped being a Stream

Three readings, from the framework's own measures:

- **A discard rate near zero.** The gate is approving whatever reaches it. Validation has become a stage rather than a gate.
- **A Feedback Pack queue that grows.** Signal is gathered and not decided upon. The loop is open and release has become the end of the process rather than its middle.
- **Escalations raised and not answered.** Agents are stopping as instructed and nobody is resolving what stopped them, so the pressure to proceed regardless becomes irresistible.

An organisation adopting this shape to reduce headcount while keeping its existing tempo, approval structures and reporting expectations will get the concentration of load without the compensating reduction in coordination — which is a worse position than the one it started from.
