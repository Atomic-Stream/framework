# The Atomic Stream: Executable Governance 

This repository contains the foundational declarations required to run an Atomic Stream. It provides the exact structure for agent identity, architectural boundaries, and escalation policies so that agentic teams can operate safely without continuous human supervision.

## Phase 1: Doctrine & Assignment
Before executing any scripts, the organization must establish the human container.
* Read the Atomic Stream Framework Guide.
* Formally appoint the Stream Orchestrator, System Architect, and Platform Engineer.

## Phase 2: Bootstrapping the Stream
This repository acts as a centralized rulebook, initialized via a guided setup.
* Clone this repository to your local environment.
* Run `python scripts/bootstrap_stream.py`.
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
