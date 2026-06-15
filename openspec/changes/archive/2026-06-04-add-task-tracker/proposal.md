## Why

Il progetto non dispone di alcun sistema per tracciare i task. Serve un modo semplice e locale per creare, elencare, completare e rimuovere task, con stato persistente, così da poter gestire il lavoro direttamente dalla riga di comando senza dipendenze esterne.

## What Changes

- Aggiunta di una capability `task-tracker` che permette di creare, elencare, completare e cancellare task.
- Persistenza su file JSON locale in `.agent/data/tasks.json`.
- Esposizione di un'interfaccia a riga di comando (`task`) per interagire con i task.
- Definizione di una capability `task-storage` che incapsula le operazioni di lettura/scrittura su disco, riutilizzabile e testabile in isolamento.

## Capabilities

### New Capabilities
- `task-tracker`: gestione del ciclo di vita dei task (create, list, complete, delete) e relativi scenari d'uso.
- `task-storage`: persistenza dei task su file JSON con garanzie di atomicità e concorrenza di base.

### Modified Capabilities
- (nessuna)

## Impact

- Nuovo entrypoint CLI: `bin/task` (o script equivalente).
- Nuovo modulo libreria: `src/task-tracker/` con classi/pure functions per domain logic e storage.
- Nuovo file di stato: `.agent/data/tasks.json` (ignorato da VCS).
- Nessuna dipendenza esterna oltre a Node.js (se implementato in TS/JS) o stdlib (se in Python).
- Nessun impatto su API esistenti: il progetto è attualmente vuoto.
