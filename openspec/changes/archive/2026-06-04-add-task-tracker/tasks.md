## 1. Project scaffold

- [ ] 1.1 Create `package.json` with name, version, and a `task` script that runs `node bin/task.js`
- [ ] 1.2 Create `src/` and `bin/` directories
- [ ] 1.3 Add a `.gitignore` entry for `.agent/data/`

## 2. Domain model and storage

- [ ] 2.1 Implement `src/task-tracker/task.js` with `Task` factory and `TaskStatus` enum (`todo`, `done`)
- [ ] 2.2 Implement `src/task-tracker/json-repository.js` with `load()`, `save(tasks)`, and corruption-recovery logic per `task-storage` spec
- [ ] 2.3 Implement `src/task-tracker/service.js` with `addTask`, `listTasks`, `completeTask`, `deleteTask` delegating to a repository passed in the constructor

## 3. CLI entrypoint

- [ ] 3.1 Implement `bin/task.js` that parses `process.argv` and dispatches `add | list | done | rm` to the service
- [ ] 3.2 Print exit code 0 on success, non-zero on validation/not-found errors
- [ ] 3.3 Format list output with `[ ]` / `[x]` prefixes and aligned columns

## 4. Manual verification

- [ ] 4.1 Run `node bin/task.js add "Buy milk"` and confirm a task is created and listed
- [ ] 4.2 Run `node bin/task.js done <id>` and confirm the task shows `[x]`
- [ ] 4.3 Run `node bin/task.js rm <id>` and confirm the task disappears
- [ ] 4.4 Corrupt `.agent/data/tasks.json` manually and confirm the loader backs it up and returns an empty list

## 5. Archive

- [ ] 5.1 Run `openspec archive add-task-tracker` to move the change into `changes/archive/` and lift specs into `openspec/specs/`
