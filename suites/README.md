# Suites

All evaluation prompts live under `suites/`.

- `suites/coding.md`: general coding + reasoning + instruction-following.
- `suites/agentic.md`: planning/debug/orchestration scenarios.
- `suites/infrasec.md`: DevOps/SRE/Security Engineering scenarios.
- `suites/sysadmin.md`: SysAdmin tasks by seniority (junior/middle/senior).

Run a suite with:

```bash
python tools/run.py --suite coding --provider print
```
