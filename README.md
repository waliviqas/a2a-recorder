# a2a-recorder

**Records what your AI agents say to each other.**

If you've ever built a multi-agent app and wondered *"wait, what did they actually say?"*...that's what this is for.

When two agents talk to each other, it's a black box. You don't know if they hallucinated, agreed on something wrong, or talked each other into a bad decision, and the more tasks you trust them to do, the more that matters. You can't trust what you can't see.

`a2a-recorder` saves every message between your agents so you can actually look at what they said and trace backs the steps as to why they made the decision that they did.

Open-source. Alpha. Works with CrewAI today. More frameworks coming.

---

## Install

```bash
pip install a2a-recorder[crewai]
```

## Use it

Add one line to your CrewAI code:

```python
from recorder import Recorder

Recorder.start(crew)       # that's it — recording starts automatically

crew.kickoff()              # runs normally
```

After the run, every agent message is saved to `recordings.db` — a SQLite database any app can read.

## What you get

A SQLite database with **one row per message.** Every message has the same fields no matter which framework you used — so your recordings stay consistent even when you switch from CrewAI to AutoGen later.

| from_agent | to_agent | content | turn | protocol |
|---|---|---|---|---|
| researcher | crew | "found 3 sources" | 1 | crewai |
| writer | crew | "drafted intro" | 2 | crewai |
| editor | crew | "polished it" | 3 | crewai |

## Roadmap

- [x] CrewAI
- [ ] AutoGen
- [ ] LangGraph
- [ ] Plain Python (no framework)
- [ ] Network recording (A2A protocol)
- [ ] Optional dashboard
- [ ] EU AI Act compliance mode

Want a specific one sooner? Open an issue.

## Status

Alpha. Don't use in production yet. Feedback wanted.

## License

MIT.
