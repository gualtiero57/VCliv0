// graphify OpenCode plugin
// Auto-builds the knowledge graph in background on project load + injects reminder.
import { existsSync } from "fs";
import { join } from "path";
import { spawn, execSync } from "child_process";

const graphifyBin = () => {
  try {
    const r = execSync("where graphify", { encoding: "utf8", timeout: 3000 });
    return r.trim().split("\n")[0];
  } catch {
    return null;
  }
};

let _graphifyPath = null;

export const GraphifyPlugin = async ({ directory }) => {
  let reminded = false;
  let built = false;
  let failed = false;

  const graphifyOut = join(directory, "graphify-out");
  if (!_graphifyPath) _graphifyPath = graphifyBin();

  const buildGraph = () => {
    if (built || failed || !_graphifyPath) return;
    built = true;
    const child = spawn(_graphifyPath, ["update", "."], {
      cwd: directory,
      stdio: "ignore",
      detached: true,
      windowsHide: true,
    });
    child.on("error", () => { failed = true; });
    child.unref();
  };

  const graphReady = () => existsSync(join(graphifyOut, "graph.json"));

  // Lancia graphify subito al caricamento del progetto
  buildGraph();

  return {
    "tool.execute.before": async (input, output) => {
      if (reminded || !graphReady()) return;

      if (input.tool === "bash") {
        output.args.command = `echo "[graphify] Run 'graphify query \"<question>\"' or read GRAPH_REPORT.md." ; ${output.args.command}`;
        reminded = true;
      }
    },
  };
};
