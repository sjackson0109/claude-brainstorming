# Installation Guide — Brainstorming Skill for Claude Code

This guide covers how to install the Brainstorming Skill in [Claude Code](https://claude.ai/claude-code). The skill provides an intelligent brainstorming orchestrator with 150 specialised domain expertise skills covering technical, business, design, innovation, cybersecurity, and strategic domains.

---

## What Are Claude Code Plugins?

Plugins let you extend Claude Code with custom functionality that can be shared across projects and teams. A plugin can contain skills (instructions Claude follows automatically), commands (slash commands you invoke), agents, hooks, and MCP servers. Once installed, a plugin is available in every Claude Code session on that machine.

A **marketplace** is a catalogue of plugins hosted in a Git repository. You add a marketplace once, then install any plugin it lists by name.

---

## Prerequisites

- [Claude Code](https://claude.ai/claude-code) installed (`claude --version` to confirm)
- Git installed and accessible on your PATH
- An active Claude subscription or API key configured

---

## 1. Add the Marketplace

Register the Brainstorming Skills marketplace with a single command. You only need to do this once per machine.

```shell
/plugin marketplace add sjackson0109/claude-brainstorming
```

Claude Code will clone the repository, read the `.claude-plugin/marketplace.json` catalogue, and register it locally as `brainstorming-skills`. You can confirm it was added with:

```shell
/plugin marketplace list
```

---

## 2. Install the Brainstorming Skill

Once the marketplace is registered, install the skill:

```shell
/plugin install brainstorming@brainstorming-skills
```

The plugin is installed to a local cache (`~/.claude/plugins/cache`) and activates immediately in new Claude Code sessions.

---

## 3. Team Setup — Auto-Install via Project Settings

For teams, you can pre-wire the marketplace into your project so every developer gets the skill automatically when they open the project in Claude Code — no manual install step required.

Add the following to your project's `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "brainstorming-skills": {
      "source": {
        "source": "github",
        "repo": "sjackson0109/claude-brainstorming"
      }
    }
  },
  "enabledPlugins": {
    "brainstorming@brainstorming-skills": true
  }
}
```

Commit this file to your repository. The next time a team member trusts the project folder in Claude Code, the marketplace and plugin will be registered automatically.

---

## 4. Manual Installation (Alternative)

If you prefer not to use the marketplace, you can install the skill manually:

1. Clone the repository:
   ```shell
   git clone https://github.com/sjackson0109/claude-brainstorming.git
   ```

2. In Claude, navigate to **Settings → Skills** and import the `brainstorming.skill` file from the cloned repository.

3. Alternatively, reference the skill directory directly from your project's Claude settings.

---

## Using the Skill

Once installed, simply start a conversation with Claude and use natural language:

**Simple domain request:**
> "Use your Brainstorming skill to support me with technical user interface design."

**Multi-domain request:**
> "Help me brainstorm a digital transformation strategy that includes cybersecurity considerations and change management."

**Strategic analysis:**
> "I need to develop a competitive analysis framework for entering a new market."

The orchestrator automatically detects the relevant domains and reads the appropriate specialised reference skills.

---

## Keeping the Skill Up to Date

When this repository is updated with new skill content or improvements, refresh your local copy:

```shell
/plugin marketplace update brainstorming-skills
```

To update the installed plugin:

```shell
/plugin update brainstorming@brainstorming-skills
```

---

## Uninstalling

To remove the plugin:

```shell
/plugin uninstall brainstorming@brainstorming-skills
```

To remove the marketplace entirely:

```shell
/plugin marketplace remove brainstorming-skills
```

---

## Domain Coverage

The Brainstorming Skill covers **150 specialised domains** across 16 categories:

| Category | Skills | Examples |
|---|---|---|
| Technical & Engineering | 16 | API design, cloud migration, software architecture |
| Cybersecurity & Offensive Security | 37 | Penetration testing, red team ops, compliance |
| Business Strategy & Commercial | 15 | Strategic planning, market entry, M&A analysis |
| Product & Innovation | 10 | Product development, lean startup, design thinking |
| Design & User Experience | 7 | UI/UX design, user research, human-centred design |
| Financial Strategy & Pricing | 5 | Pricing strategies, financial modelling |
| Operations & Process Optimisation | 8 | Operational excellence, supply chain, quality |
| Organisational Development & People | 13 | Change management, talent, cultural transformation |
| Analytics & Data-Driven Decision Making | 13 | Forecasting, hypothesis testing, decision tracking |
| Sustainability & Environment | 5 | Sustainability frameworks, green technology |
| Crisis Management & Strategic Challenges | 4 | Crisis response, red team challenges |
| Facilitation & Communication | 3 | Workshop facilitation, writing |
| Knowledge & Learning Systems | 5 | Knowledge management, cross-domain analysis |
| Advanced Thinking & Analysis | 6 | Systems thinking, biomimetic strategy |
| Productivity & Personal Effectiveness | 1 | Time management |
| Digital Strategy & E-commerce | 2 | Digital strategy, e-commerce growth |

---

## Troubleshooting

**Marketplace not found after adding**
Run `/plugin marketplace list` to confirm it was registered. If it's missing, check that your Git credentials allow access and retry.

**Plugin installation fails**
Verify you have network access to GitHub and that your Git version is current. You can also clone the repo manually to test: `git clone https://github.com/sjackson0109/claude-brainstorming.git`

**Skill not activating in sessions**
Restart Claude Code after installing the plugin. Skills activate in new sessions, not mid-session.

**Git timeout on slow connections**
Increase the timeout via environment variable before running Claude Code:
```bash
export CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS=300000
```

For additional help, [open an issue](https://github.com/sjackson0109/claude-brainstorming/issues) on the repository.

---

## See Also

- [Claude Code documentation](https://claude.ai/claude-code)
- [Plugin marketplace docs](https://code.claude.com/docs/en/plugin-marketplaces)
- [Full Documentation](docs/index.md) — user guide, quick reference, prompt examples
- [GitHub Pages Site](https://sjackson0109.github.io/claude-brainstorming/) — landing page and interactive walkthrough
- [GitHub Repository](https://github.com/sjackson0109/claude-brainstorming)
