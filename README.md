# Infographic GPTs

This repository contains automatically generated prompt files for a variety of marketing roles. Each prompt is exactly 8,000 characters long and can be found in the `marketing_agents` directory.

Use `guide.html` for an interactive way to explore each prompt. Open the file in a browser and expand any role to load its full text on demand.

## Generating Agents

Scripts in the `scripts` folder recreate the agent prompts:

```bash
python3 scripts/generate_marketing_agents.py
```

This will populate the `marketing_agents` directory with 50 agent files.
