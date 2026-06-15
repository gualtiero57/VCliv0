## Context

Il progetto è attualmente vuoto e non dispone di alcun meccanismo di gestione task. L'obiettivo della change `add-task-tracker` è introdurre un sistema minimale, locale e scriptabile, capace di tracciare task come oggetti con stato (todo / done) e di persisterli su disco. Lo storage è centralizzato in un unico file JSON, sufficiente per uso single-user single-machine.

Vincoli:
- Nessuna dipendenza esterna oltre a Node.js e la sua stdlib.
- Deve funzionare su Windows (la shell di lavoro è PowerShell 5.1).
- Lo storage deve essere atomico per evitare corruzione in caso di crash.
- Deve essere testabile in isolamento (storage separato dalla logica di dominio).

## Goals / Non-Goals

**Goals:**
- Definire un modello dati `Task` con campi `id`, `title`, `status`, `createdAt`, `completedAt`.
- Esporre operazioni CRUD con effetti collaterali confinati al layer storage.
- Offrire un entrypoint CLI per creare, listare, completare e cancellare task.
- Persistenza atomica tramite scrittura su file temporaneo + `rename`.
- Locking single-process via `fs.openSync` con flag `wx` sul file `.lock`.

**Non-Goals:**
- Multi-utente o sincronizzazione cloud.
- Date di scadenza, priorità, tag, sotto-task.
- Notifiche o hook.
- Concorrenza tra processi simultanei (oltre un best-effort tramite lock file).

## Decisions

- **Stack: Node.js (CommonJS) con TypeScript-free plain JS** per minimizzare toolchain e mantenere il sample focalizzato sul design, non sul build system. Un `package.json` con uno script `task` che usa `node bin/task.js` è sufficiente.
  - *Alternative considered*: TypeScript — scartato per il sample; aggiungerebbe complessità di build.
  - *Alternative considered*: Python — scartato perché l'utente lavora in ambiente Windows PowerShell dove Node è onnipresente.

- **Storage: file JSON in `.agent/data/tasks.json`**. Formato scelto per leggibilità umana e zero-config.
  - *Alternative considered*: SQLite — overkill per il caso d'uso single-user e richiede native binding.
  - *Alternative considered*: YAML — più verboso e dipendenza `js-yaml`.

- **Atomic write**: scrittura su `<file>.tmp` seguita da `fs.renameSync` atomico sul filesystem (POSIX guarantee; su NTFS `MoveFileEx` con replace è sufficiente).
  - *Alternative considered*: write-then-fsync manuale — più complesso, non necessario per il sample.

- **Layering**: separazione netta tra `TaskService` (logica di dominio, pura) e `JsonTaskRepository` (I/O). Il servizio riceve il repository via costruttore (dependency injection leggera), così da poter testare con un `InMemoryTaskRepository`.

- **ID generation**: `crypto.randomUUID()` (built-in in Node ≥ 14.17). Niente dipendenze esterne.
  - *Alternative considered*: contatore monotono in file — più complesso e non necessario.

- **CLI parsing**: nessuna libreria. Si ispezionano `process.argv` direttamente, accettando comandi `add`, `list`, `done <id>`, `rm <id>`. Lo split è banale e mantiene il sample leggibile.
  - *Alternative considered*: `commander` o `yargs` — overkill per 4 comandi.

## Risks / Trade-offs

- **Corruzione del file JSON in caso di crash a metà scrittura** → mitigato da atomic rename; in caso di JSON malformato all'avvio, il loader fa un backup `tasks.json.bak` e riparte da una lista vuota.
- **Concorrenza tra processi** non gestita correttamente su Windows (lock file semantics sono diverse) → mitigato da best-effort `.lock` e documentato come limitazione nota.
- **Nessuna migrazione schema** → il modello `Task` è versionato implicitamente; futuri cambi dovranno aggiungere un campo `schemaVersion`.
- **Single point of failure: il file `.agent/data/tasks.json`** → non è un problema per uso locale single-user, ma è documentato.

## Migration Plan

Non applicabile: il progetto parte da zero. L'unica "migration" è la creazione iniziale di `.agent/data/` al primo utilizzo, gestita lazy dal repository.

## Open Questions

- Vogliamo aggiungere un comando `clear` per svuotare la lista (anche dei task done)?
- Serve una flag `--json` su `list` per output machine-readable?
- Vogliamo supportare un `--file` per cambiare il path dello storage (utile per i test)?
