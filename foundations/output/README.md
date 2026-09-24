# output/ — What its output must look like

**Question this folder answers:** what shape must this agent's artefact take, in a form specific enough to be checked?

**Maintained by:** Platform Engineering · **Propagation:** mandatory · **Tier:** A — ships complete

One schema per artefact of the Loop. Each states its required fields, its field-level acceptance rules, who may write it, who may close it, and what makes it invalid.

Where a standard can be checked deterministically, it should be. A check agent is for what a rule cannot express.

---

**Status: not yet written.** This folder is declared and empty. The framework holds that a Stream which has not settled these questions is not running a governed system — so an empty folder here is a statement about this repository, not a permission. See [`../../MINIMUM.md`](../../MINIMUM.md) for what must be in place before a Stream runs agents unattended, and [`../escalation/`](../escalation/) for the one declaration published complete.

Framework reference: *Agent Foundations → What Must Be Declared Before an Agent Runs*.
