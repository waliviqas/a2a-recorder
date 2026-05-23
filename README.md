# a2a-recorder

**Records what your AI agents say to each other.**

If you've ever built a multi-agent app and wondered *"wait, what did they actually say?"* — that's what this is for.

When two agents talk to each other, it's a black box. You don't know if they hallucinated, agreed on something wrong, or talked each other into a bad decision — and the more you trust them to do, the more that matters. You can't trust what you can't see.

`a2a-recorder` saves every message between your agents so you can actually look at what they said — and decide whether to trust them.

Open-source. Alpha. Works with CrewAI today. More frameworks coming.

---

## Install

```bash
pip install a2a-recorder[crewai]
```

## Use it

Add 3 lines to your CrewAI code:

```python
from recorder.storage import JSONLStorage
from recorder.adapters.crewai import CrewAIAdapter

storage = JSONLStorage("recordings.jsonl")   # 1. where to save
adapter = CrewAIAdapter(storage)             # 2. set up the recorder
adapter.wrap(crew)                           # 3. plug it into your crew

crew.kickoff()                               # run normally — recording happens automatically
```

That's it. After your crew runs, open `recordings.jsonl` and you'll see every message your agents sent each other.

## What you get

A text file with **one message per line.** Like this:

```
{"from_agent": "researcher", "content": "found 3 sources", "turn": 1, ...}
{"from_agent": "writer",     "content": "drafted intro",   "turn": 2, ...}
{"from_agent": "editor",     "content": "polished it",     "turn": 3, ...}
```

Every message has the same fields no matter which framework you used. That's the point — your recordings stay consistent even when you switch from CrewAI to AutoGen later.

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
