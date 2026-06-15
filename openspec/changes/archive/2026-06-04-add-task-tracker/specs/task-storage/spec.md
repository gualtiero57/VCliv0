## ADDED Requirements

### Requirement: Persist tasks atomically
The system SHALL persist tasks to `.agent/data/tasks.json` by writing to a temporary file in the same directory and renaming it over the target file.

#### Scenario: Successful save
- **WHEN** `JsonTaskRepository.save` is called with a non-empty task list
- **THEN** a file named `.agent/data/tasks.json.tmp` is written first
- **AND** it is atomically renamed to `.agent/data/tasks.json`
- **AND** no partial file is ever visible at the target path

#### Scenario: Crash mid-write
- **WHEN** the process is killed during the temp-file write phase
- **THEN** `.agent/data/tasks.json` either contains the previous valid content or is absent
- **AND** `.agent/data/tasks.json.tmp` may be left behind and is ignored on next load

### Requirement: Load tasks with corruption recovery
The system SHALL load tasks from `.agent/data/tasks.json`; if the file is missing, empty, or contains invalid JSON, the loader SHALL return an empty list and back up the bad file to `.agent/data/tasks.json.bak.<timestamp>`.

#### Scenario: Missing file
- **WHEN** the storage file does not exist
- **THEN** the loader returns an empty task list
- **AND** no backup is created

#### Scenario: Invalid JSON
- **WHEN** the storage file contains malformed JSON
- **THEN** the loader returns an empty task list
- **AND** the malformed file is moved to `.agent/data/tasks.json.bak.<timestamp>`

#### Scenario: Valid file
- **WHEN** the storage file contains a valid JSON array of tasks
- **THEN** the loader returns the parsed list

### Requirement: Lazy directory creation
The system SHALL create `.agent/data/` on first write if it does not exist.

#### Scenario: First write in a clean checkout
- **WHEN** `.agent/data/` does not exist and a save is performed
- **THEN** the directory is created with default permissions
- **AND** the save succeeds
