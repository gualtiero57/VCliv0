# Graph Report - .  (2026-06-08)

## Corpus Check
- Corpus is ~11,104 words - fits in a single context window. You may not need a graph.

## Summary
- 44 nodes · 43 edges · 9 communities (5 shown, 4 thin omitted)
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 3 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Task Tracker Change|Task Tracker Change]]
- [[_COMMUNITY_Proposal & Design Artifacts|Proposal & Design Artifacts]]
- [[_COMMUNITY_Change Lifecycle Workflows|Change Lifecycle Workflows]]
- [[_COMMUNITY_Core OpenSpec Framework|Core OpenSpec Framework]]
- [[_COMMUNITY_OpenCode Settings|OpenCode Settings]]
- [[_COMMUNITY_OpenCode Plugin Config|OpenCode Plugin Config]]
- [[_COMMUNITY_Package Dependencies|Package Dependencies]]
- [[_COMMUNITY_Agent Skills System|Agent Skills System]]

## God Nodes (most connected - your core abstractions)
1. `Change Lifecycle` - 7 edges
2. `Skill: OpenSpec Propose` - 6 edges
3. `Task Storage Capability` - 5 edges
4. `OpenSpec Framework` - 4 edges
5. `Task Tracker Capability` - 4 edges
6. `Delta Specs` - 3 edges
7. `Add Task Tracker Change` - 3 edges
8. `Skill: OpenSpec Apply Change` - 3 edges
9. `hooks` - 2 edges
10. `Spec-Driven Development` - 2 edges

## Surprising Connections (you probably didn't know these)
- `Add Task Tracker Change` --references--> `Change Lifecycle`  [EXTRACTED]
  openspec/changes/archive/2026-06-04-add-task-tracker/proposal.md → sunto.txt
- `Skill: OpenSpec Apply Change` --references--> `Change Lifecycle`  [EXTRACTED]
  .agent/skills/openspec-apply-change/SKILL.md → sunto.txt
- `Skill: OpenSpec Archive Change` --references--> `Change Lifecycle`  [EXTRACTED]
  .agent/skills/openspec-archive-change/SKILL.md → sunto.txt
- `Skill: OpenSpec Explore` --references--> `Change Lifecycle`  [EXTRACTED]
  .agent/skills/openspec-explore/SKILL.md → sunto.txt
- `Skill: OpenSpec Propose` --references--> `Change Lifecycle`  [EXTRACTED]
  .agent/skills/openspec-propose/SKILL.md → sunto.txt

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Change Lifecycle Phases** — skill_openspec_explore, skill_openspec_propose, skill_openspec_apply, skill_openspec_sync, skill_openspec_archive [EXTRACTED 1.00]
- **Change Artifacts** — artifact_proposal, artifact_design, artifact_specs, artifact_tasks [EXTRACTED 1.00]
- **Task Tracker Components** — task_tracker_capability, task_storage_capability, atomic_write, layering_pattern, cli_task [EXTRACTED 1.00]

## Communities (9 total, 4 thin omitted)

### Community 0 - "Task Tracker Change"
Cohesion: 0.28
Nodes (9): Add Task Tracker Change, Archive Delta Spec: Task Storage, Archive Delta Spec: Task Tracker, Atomic Write Pattern, Delta Specs, JSON File Storage, Service/Repository Layering, Task Storage Capability (+1 more)

### Community 1 - "Proposal & Design Artifacts"
Cohesion: 0.22
Nodes (9): Archive Design, Archive Proposal, Archive Tasks, Design Artifact, Proposal Artifact, Specs Artifact, Tasks Artifact, Skill: OpenSpec Propose (+1 more)

### Community 2 - "Change Lifecycle Workflows"
Cohesion: 0.29
Nodes (7): Change Lifecycle, Skill: OpenSpec Archive Change, Skill: OpenSpec Explore, Skill: OpenSpec Sync Specs, Workflow: /opsx:archive, Workflow: /opsx:explore, Workflow: /opsx:sync

### Community 3 - "Core OpenSpec Framework"
Cohesion: 0.29
Nodes (7): OpenSpec CLI, Task CLI, OpenSpec Framework, Skill: OpenSpec Apply Change, Spec-Driven Development, Workflow: /opsx:apply, Workspace Guard

## Knowledge Gaps
- **15 isolated node(s):** `PreToolUse`, `$schema`, `plugin`, `@opencode-ai/plugin`, `Agent Skills System` (+10 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Change Lifecycle` connect `Change Lifecycle Workflows` to `Task Tracker Change`, `Proposal & Design Artifacts`, `Core OpenSpec Framework`?**
  _High betweenness centrality (0.377) - this node is a cross-community bridge._
- **Why does `Skill: OpenSpec Propose` connect `Proposal & Design Artifacts` to `Change Lifecycle Workflows`?**
  _High betweenness centrality (0.231) - this node is a cross-community bridge._
- **Why does `Add Task Tracker Change` connect `Task Tracker Change` to `Change Lifecycle Workflows`?**
  _High betweenness centrality (0.166) - this node is a cross-community bridge._
- **What connects `PreToolUse`, `$schema`, `plugin` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._