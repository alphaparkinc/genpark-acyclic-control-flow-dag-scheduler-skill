import sys
import json
from client import DAGListScheduler

sched = DAGListScheduler()

def handle_call(name, arguments):
    if name == "schedule":
        nodes = arguments["nodes"]
        edges = [tuple(e) for e in arguments["edges"]]
        return {"order": sched.schedule(edges, nodes)}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
