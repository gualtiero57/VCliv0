## ADDED Requirements

### Requirement: Create task
The system SHALL create a task with a non-empty `title`, a generated `id`, `status` set to `todo`, and a `createdAt` timestamp.

#### Scenario: Successful creation
- **WHEN** the user invokes `task add "Buy milk"`
- **THEN** a new task is persisted with `status = "todo"` and a unique `id`
- **AND** the CLI outputs the new task's `id`

#### Scenario: Empty title is rejected
- **WHEN** the user invokes `task add ""`
- **THEN** the system returns a non-zero exit code
- **AND** no task is persisted

### Requirement: List tasks
The system SHALL list all persisted tasks, ordered by `createdAt` ascending.

#### Scenario: Empty list
- **WHEN** no tasks exist and the user invokes `task list`
- **THEN** the CLI exits with code 0
- **AND** prints a header line and no task rows

#### Scenario: Mixed statuses
- **WHEN** tasks with `status` `todo` and `done` exist
- **THEN** all tasks are printed
- **AND** done tasks are visually distinguished (e.g. prefix `[x]` vs `[ ]`)

### Requirement: Complete task
The system SHALL mark a task as `done` and set `completedAt` to the current time.

#### Scenario: Complete existing task
- **WHEN** the user invokes `task done <id>` with a valid id
- **THEN** the task's `status` becomes `done`
- **AND** `completedAt` is set to the current timestamp

#### Scenario: Complete unknown id
- **WHEN** the user invokes `task done <id>` with an id that does not exist
- **THEN** the system returns a non-zero exit code
- **AND** prints a "task not found" error

#### Scenario: Complete an already-done task
- **WHEN** the user invokes `task done <id>` on a task with `status = "done"`
- **THEN** the system is idempotent: the task remains `done` and the CLI exits with code 0

### Requirement: Delete task
The system SHALL permanently remove a task by `id`.

#### Scenario: Delete existing task
- **WHEN** the user invokes `task rm <id>` with a valid id
- **THEN** the task is removed from storage
- **AND** a subsequent `task list` no longer includes it

#### Scenario: Delete unknown id
- **WHEN** the user invokes `task rm <id>` with an id that does not exist
- **THEN** the system returns a non-zero exit code
- **AND** no storage mutation occurs
