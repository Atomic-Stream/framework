# access/ — What it may reach, and with what rights

**Question this folder answers:** which systems and data may this agent connect to, and may it read, write, or administer each?

**Maintained by:** Platform Engineering · **Propagation:** mandatory · **Tier:** B — scaffold

Reach and rights are separate questions and are declared separately. An agent that can read a repository and one that can write to it are not the same agent, and a single permission list that conflates them will be read permissively.

Credentials are the one thing excluded from this repository: held in the organisation's secret store, injected at runtime, short-lived, and revocable without changing any declaration.

---

**Status: not yet written.** This folder is declared and empty. The framework holds that a Stream which has not settled these questions is not running a governed system — so an empty folder here is a statement about this repository, not a permission. See [`../../MINIMUM.md`](../../MINIMUM.md) for what must be in place before a Stream runs agents unattended, and [`../escalation/`](../escalation/) for the one declaration published complete.

Framework reference: *Agent Foundations → What Must Be Declared Before an Agent Runs*.
