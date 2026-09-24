# The Atomic Stream: Executable Governance 

This repository contains the foundational declarations required to run an Atomic Stream. It provides the exact structure for agent identity, architectural boundaries, and escalation policies so that agentic teams can operate safely without continuous human supervision.

## Phase 1: Doctrine & Assignment
Before executing any scripts, the organization must establish the human container.
* Read the Atomic Stream Framework Guide.
* Formally appoint the Stream Orchestrator, System Architect, and Platform Engineer.

## Phase 2: Bootstrapping the Stream
This repository acts as a centralized rulebook, initialized via a guided setup.
* Clone this repository to your local environment.
* Run `python onboarding/bootstrap_stream.py`.
* The System Architect, Orchestrator, and Platform Engineer must answer the script's prompts to define boundaries, domains, and access.
* The script generates the root `stream.yml` file; commit this to the `main` branch.

## Phase 3: The Connection Layer
Agents require an execution environment connected to this rulebook.
* Platform Engineering configures the execution environments (e.g., n8n, Claude Code).
* Inject necessary credentials (ticketing, version control, deployment) completely outside of this repository.
* Configure the Scribe service to route agent output directly to the Stream's system of record.

## Phase 4: Pair Instantiation
Pairs execute work in isolated environments by dynamically reading from this repository.
* The Stream Orchestrator assigns an Intent to a specific Pair.
* Pilot Developers trigger local worker agents using the provided Agent Brief templates
* Agents load rules from the `main` branch, execute the work, and halt if boundaries are crossed.

---

## What is in this repository

| | |
|---|---|
| [`guide/atomic-stream-v2.4.md`](guide/atomic-stream-v2.4.md) | The framework guide. Principles, accountabilities, the Loop, and the reasoning the rules rest on. |
| [`MINIMUM.md`](MINIMUM.md) | The five things that must be in place on day one for a Stream to be a Stream. |
| [`foundations/`](foundations/) | The six declarations that must be settled before an agent runs unattended, one folder per question. |
| [`artefacts/`](artefacts/) | Templates for the artefacts the Loop produces. |
| [`onboarding/`](onboarding/) | The guided setup that writes your `stream.yml`. |

New here? Read [`MINIMUM.md`](MINIMUM.md) first — it is the shortest complete answer to what it takes to start.

## State

This repository is published as it is written, and it is not complete.

Of the six declarations, [`escalation/`](foundations/escalation/) is the one that carries a working policy today. The remaining five state what belongs in them, who maintains them, and why they are not yet written. The framework holds that a Stream which has not settled all six questions is not running a governed system — so an empty folder here is a statement about this repository, not a permission.

The guide is **Version 2.4**, September 2026. It is under review with practitioners and CTOs and is not stable.

## Contributing

The framework argues that governance should be open to challenge by the people who operate under it, discussed against a specific diff rather than in the abstract. The same terms apply here.

Corrections, disagreements and proposals are welcome as issues or pull requests. A decline is recorded with its reason, not closed silently.

## Licence

Documentation and framework text: [CC BY 4.0](LICENSE) — share and adapt, including commercially, with attribution.
Code in `onboarding/`: MIT.
"The Atomic Stream" as a name is not licensed under either.

Written by Julia Waanders.
