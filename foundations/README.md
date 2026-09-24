# Agent Foundations

*The groundwork the framework rests on: what is declared, how it is governed, and when an agent must stop.*

The Loop describes agents doing the work of every step while humans decide between them. Foundations is what has to be in place for that arrangement to hold.

Foundations is the agent's **harness**: everything around the model that makes it an agent. Without one, an agent works neither effectively nor safely. The harness is the framework's infrastructure and its governance at once. It is not produced by the work; it is the ground the work stands on — a set of declarations, held in version control, that determine what agents may do at all.

Where the artefacts of the Loop accumulate as delivery proceeds, these are settled beforehand and change rarely. **An artefact records what happened; a declaration determines what is permitted to happen.**

## The six questions

An agent works without supervision between one human decision and the next. That is only tolerable when six things have been settled in advance and written where the agent reads them at execution time.

| | Question | Folder | Maintained by | Propagation |
|---|---|---|---|---|
| 1 | What it is | [`identity/`](identity/) | Platform Engineering | mandatory |
| 2 | What it may reach, and with what rights | [`access/`](access/) | Platform Engineering | mandatory |
| 3 | What it knows | [`knowledge/`](knowledge/) | Stream Orchestrator | reviewed |
| 4 | What it must not do | [`boundaries/`](boundaries/) | System Architect | mandatory |
| 5 | When it must stop and ask | [`escalation/`](escalation/) | System Architect | mandatory |
| 6 | What its output must look like | [`output/`](output/) | Platform Engineering | mandatory |

The folders are arranged one per question, in the order asked. Their contents will change as tooling does; the questions will not.

The order in which agents run is **not** declared here. Sequencing is authored per Build by the Pilot Developer in the Agent Briefs, because dependencies differ for every change.

## Propagation

A change to a declaration is a change to how every agent in every Stream behaves. Pushing it carelessly is closer to a production deployment than to a document edit.

| Class | Applies to | Propagation |
|---|---|---|
| **Mandatory** | Compliance, security, supply-chain, regulatory obligation. | Applied immediately. No Stream may decline. |
| **Reviewed** | Presentation standards, outcome context. | Raised as a change request. Merges automatically after a defined review window. |
| **Proposed** | New capabilities, workflow changes, strategic shifts. | Requires acceptance. Declines are recorded with reason. |

## Credentials

Credentials are the one thing excluded from this repository: held in the organisation's secret store, injected at runtime, short-lived, and revocable without changing any declaration.
