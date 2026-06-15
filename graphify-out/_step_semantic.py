import json
from pathlib import Path

# Semantic extraction for document files in VCliv0 project
# Based on manual analysis of all document files

nodes = [
    # Core concepts
    {"id": "openspec_framework", "label": "OpenSpec Framework", "file_type": "concept", "source_file": "sunto.txt", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "spec_driven", "label": "Spec-Driven Development", "file_type": "concept", "source_file": "sunto.txt", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "change_lifecycle", "label": "Change Lifecycle", "file_type": "concept", "source_file": "sunto.txt", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "cli_openspec", "label": "OpenSpec CLI", "file_type": "concept", "source_file": "sunto.txt", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "agent_skills", "label": "Agent Skills System", "file_type": "concept", "source_file": "sunto.txt", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "workspace_guard", "label": "Workspace Guard", "file_type": "concept", "source_file": "sunto.txt", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "delta_specs", "label": "Delta Specs", "file_type": "concept", "source_file": "sunto.txt", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},

    # Task tracker change concepts
    {"id": "add_task_tracker", "label": "Add Task Tracker Change", "file_type": "concept", "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/proposal.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "task_tracker_capability", "label": "Task Tracker Capability", "file_type": "concept", "source_file": "openspec/specs/task-tracker/spec.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "task_storage_capability", "label": "Task Storage Capability", "file_type": "concept", "source_file": "openspec/specs/task-storage/spec.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "atomic_write", "label": "Atomic Write Pattern", "file_type": "concept", "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/design.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "json_storage", "label": "JSON File Storage", "file_type": "rationale", "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/design.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "layering_pattern", "label": "Service/Repository Layering", "file_type": "concept", "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/design.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "cli_task", "label": "Task CLI", "file_type": "concept", "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/tasks.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},

    # Skills (named skills in the system)
    {"id": "skill_openspec_propose", "label": "Skill: OpenSpec Propose", "file_type": "skill", "source_file": ".agent/skills/openspec-propose/SKILL.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "skill_openspec_apply", "label": "Skill: OpenSpec Apply Change", "file_type": "skill", "source_file": ".agent/skills/openspec-apply-change/SKILL.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "skill_openspec_explore", "label": "Skill: OpenSpec Explore", "file_type": "skill", "source_file": ".agent/skills/openspec-explore/SKILL.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "skill_openspec_archive", "label": "Skill: OpenSpec Archive Change", "file_type": "skill", "source_file": ".agent/skills/openspec-archive-change/SKILL.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "skill_openspec_sync", "label": "Skill: OpenSpec Sync Specs", "file_type": "skill", "source_file": ".agent/skills/openspec-sync-specs/SKILL.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},

    # Workflows (slash commands)
    {"id": "workflow_opsx_propose", "label": "Workflow: /opsx:propose", "file_type": "document", "source_file": ".agent/workflows/opsx-propose.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "workflow_opsx_apply", "label": "Workflow: /opsx:apply", "file_type": "document", "source_file": ".agent/workflows/opsx-apply.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "workflow_opsx_explore", "label": "Workflow: /opsx:explore", "file_type": "document", "source_file": ".agent/workflows/opsx-explore.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "workflow_opsx_archive", "label": "Workflow: /opsx:archive", "file_type": "document", "source_file": ".agent/workflows/opsx-archive.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "workflow_opsx_sync", "label": "Workflow: /opsx:sync", "file_type": "document", "source_file": ".agent/workflows/opsx-sync.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},

    # Artifacts concepts
    {"id": "artifact_proposal", "label": "Proposal Artifact", "file_type": "concept", "source_file": "sunto.txt", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "artifact_design", "label": "Design Artifact", "file_type": "concept", "source_file": "sunto.txt", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "artifact_specs", "label": "Specs Artifact", "file_type": "concept", "source_file": "sunto.txt", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "artifact_tasks", "label": "Tasks Artifact", "file_type": "concept", "source_file": "sunto.txt", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},

    # Change archive instance
    {"id": "archive_proposal", "label": "Archive Proposal", "file_type": "document", "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/proposal.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "archive_design", "label": "Archive Design", "file_type": "document", "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/design.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "archive_tasks", "label": "Archive Tasks", "file_type": "document", "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/tasks.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "archive_delta_spec_task_storage", "label": "Archive Delta Spec: Task Storage", "file_type": "document", "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/specs/task-storage/spec.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
    {"id": "archive_delta_spec_task_tracker", "label": "Archive Delta Spec: Task Tracker", "file_type": "document", "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/specs/task-tracker/spec.md", "source_location": None, "source_url": None, "captured_at": None, "author": None, "contributor": None},
]

edges = [
    # Framework hierarchy
    {"source": "openspec_framework", "target": "spec_driven", "relation": "conceptually_related_to", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "sunto.txt", "source_location": None, "weight": 1.0},
    {"source": "change_lifecycle", "target": "openspec_framework", "relation": "conceptually_related_to", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "sunto.txt", "source_location": None, "weight": 1.0},

    # CLI commands reference framework
    {"source": "cli_openspec", "target": "openspec_framework", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "sunto.txt", "source_location": None, "weight": 1.0},

    # Skills mapped to lifecycle phases
    {"source": "skill_openspec_explore", "target": "change_lifecycle", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": ".agent/skills/openspec-explore/SKILL.md", "source_location": None, "weight": 1.0},
    {"source": "skill_openspec_propose", "target": "change_lifecycle", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": ".agent/skills/openspec-propose/SKILL.md", "source_location": None, "weight": 1.0},
    {"source": "skill_openspec_apply", "target": "change_lifecycle", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": ".agent/skills/openspec-apply-change/SKILL.md", "source_location": None, "weight": 1.0},
    {"source": "skill_openspec_sync", "target": "change_lifecycle", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": ".agent/skills/openspec-sync-specs/SKILL.md", "source_location": None, "weight": 1.0},
    {"source": "skill_openspec_archive", "target": "change_lifecycle", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": ".agent/skills/openspec-archive-change/SKILL.md", "source_location": None, "weight": 1.0},

    # Workflows → Skills (workflows reference/trigger skills)
    {"source": "workflow_opsx_propose", "target": "skill_openspec_propose", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": ".agent/workflows/opsx-propose.md", "source_location": None, "weight": 1.0},
    {"source": "workflow_opsx_apply", "target": "skill_openspec_apply", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": ".agent/workflows/opsx-apply.md", "source_location": None, "weight": 1.0},
    {"source": "workflow_opsx_explore", "target": "skill_openspec_explore", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": ".agent/workflows/opsx-explore.md", "source_location": None, "weight": 1.0},
    {"source": "workflow_opsx_archive", "target": "skill_openspec_archive", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": ".agent/workflows/opsx-archive.md", "source_location": None, "weight": 1.0},
    {"source": "workflow_opsx_sync", "target": "skill_openspec_sync", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": ".agent/workflows/opsx-sync.md", "source_location": None, "weight": 1.0},

    # Artifact types
    {"source": "artifact_proposal", "target": "skill_openspec_propose", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "sunto.txt", "source_location": None, "weight": 1.0},
    {"source": "artifact_design", "target": "skill_openspec_propose", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "sunto.txt", "source_location": None, "weight": 1.0},
    {"source": "artifact_specs", "target": "skill_openspec_propose", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "sunto.txt", "source_location": None, "weight": 1.0},
    {"source": "artifact_tasks", "target": "skill_openspec_propose", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "sunto.txt", "source_location": None, "weight": 1.0},

    # Workspace guard
    {"source": "workspace_guard", "target": "openspec_framework", "relation": "conceptually_related_to", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "sunto.txt", "source_location": None, "weight": 1.0},
    {"source": "workspace_guard", "target": "skill_openspec_apply", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": ".agent/skills/openspec-apply-change/SKILL.md", "source_location": None, "weight": 1.0},

    # Delta specs
    {"source": "delta_specs", "target": "spec_driven", "relation": "conceptually_related_to", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "sunto.txt", "source_location": None, "weight": 1.0},

    # Change instance → concepts
    {"source": "add_task_tracker", "target": "change_lifecycle", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/proposal.md", "source_location": None, "weight": 1.0},
    {"source": "add_task_tracker", "target": "task_tracker_capability", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/proposal.md", "source_location": None, "weight": 1.0},
    {"source": "add_task_tracker", "target": "task_storage_capability", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/proposal.md", "source_location": None, "weight": 1.0},

    # Design decisions
    {"source": "atomic_write", "target": "task_storage_capability", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/design.md", "source_location": None, "weight": 1.0},
    {"source": "json_storage", "target": "task_storage_capability", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/design.md", "source_location": None, "weight": 1.0},
    {"source": "layering_pattern", "target": "task_storage_capability", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/design.md", "source_location": None, "weight": 1.0},
    {"source": "layering_pattern", "target": "task_tracker_capability", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/design.md", "source_location": None, "weight": 1.0},
    {"source": "cli_task", "target": "task_tracker_capability", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/tasks.md", "source_location": None, "weight": 1.0},
    {"source": "cli_task", "target": "cli_openspec", "relation": "conceptually_related_to", "confidence": "INFERRED", "confidence_score": 0.85, "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/tasks.md", "source_location": None, "weight": 1.0},

    # Archive files → their instances
    {"source": "archive_proposal", "target": "artifact_proposal", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/proposal.md", "source_location": None, "weight": 1.0},
    {"source": "archive_design", "target": "artifact_design", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/design.md", "source_location": None, "weight": 1.0},
    {"source": "archive_tasks", "target": "artifact_tasks", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/tasks.md", "source_location": None, "weight": 1.0},
    {"source": "archive_delta_spec_task_storage", "target": "delta_specs", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/specs/task-storage/spec.md", "source_location": None, "weight": 1.0},
    {"source": "archive_delta_spec_task_tracker", "target": "delta_specs", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/specs/task-tracker/spec.md", "source_location": None, "weight": 1.0},

    # Main specs → archive specs (semantic similarity: same content, one is delta, other is main)
    {"source": "task_storage_capability", "target": "archive_delta_spec_task_storage", "relation": "semantically_similar_to", "confidence": "INFERRED", "confidence_score": 0.95, "source_file": "openspec/specs/task-storage/spec.md", "source_location": None, "weight": 1.0},
    {"source": "task_tracker_capability", "target": "archive_delta_spec_task_tracker", "relation": "semantically_similar_to", "confidence": "INFERRED", "confidence_score": 0.95, "source_file": "openspec/specs/task-tracker/spec.md", "source_location": None, "weight": 1.0},
]

hyperedges = [
    {
        "id": "change_lifecycle_phases",
        "label": "Change Lifecycle Phases",
        "nodes": [
            "skill_openspec_explore",
            "skill_openspec_propose",
            "skill_openspec_apply",
            "skill_openspec_sync",
            "skill_openspec_archive"
        ],
        "relation": "form",
        "confidence": "EXTRACTED",
        "confidence_score": 1.0,
        "source_file": "sunto.txt"
    },
    {
        "id": "change_artifacts",
        "label": "Change Artifacts",
        "nodes": [
            "artifact_proposal",
            "artifact_design",
            "artifact_specs",
            "artifact_tasks"
        ],
        "relation": "form",
        "confidence": "EXTRACTED",
        "confidence_score": 1.0,
        "source_file": "sunto.txt"
    },
    {
        "id": "task_tracker_components",
        "label": "Task Tracker Components",
        "nodes": [
            "task_tracker_capability",
            "task_storage_capability",
            "atomic_write",
            "layering_pattern",
            "cli_task"
        ],
        "relation": "form",
        "confidence": "EXTRACTED",
        "confidence_score": 1.0,
        "source_file": "openspec/changes/archive/2026-06-04-add-task-tracker/design.md"
    }
]

output = {
    "nodes": nodes,
    "edges": edges,
    "hyperedges": hyperedges,
    "input_tokens": 0,
    "output_tokens": 0
}

Path('graphify-out/.graphify_semantic.json').write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding='utf-8')
print(f'Semantic: {len(nodes)} nodes, {len(edges)} edges, {len(hyperedges)} hyperedges')
