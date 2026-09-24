# identity/ — What it is

**Question this folder answers:** what is this agent — its role, its instructions, and the limits on how it behaves?

**Maintained by:** Platform Engineering · **Propagation:** mandatory · **Tier:** B — scaffold

One file per agent template. Each declares only what differs from its base: `access`, `boundaries`, `escalation` and `output` are inherited by reference, never copied. An agent file that restates the shared escalation policy is a file that will drift from it.

A template is a versioned configuration file and performs no work. An agent is a running instance of one, executing a single brief and producing a single artefact.

---

**Status: not yet written.** This folder is declared and empty. The framework holds that a Stream which has not settled these questions is not running a governed system — so an empty folder here is a statement about this repository, not a permission. See [`../../MINIMUM.md`](../../MINIMUM.md) for what must be in place before a Stream runs agents unattended, and [`../escalation/`](../escalation/) for the one declaration published complete.

Framework reference: *Agent Foundations → What Must Be Declared Before an Agent Runs*.
