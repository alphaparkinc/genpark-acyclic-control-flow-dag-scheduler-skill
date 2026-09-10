import collections

class DAGListScheduler:
    """
    Critical-Path Acyclic Instruction List Scheduler.
    Schedules basic block instruction DAG to minimize pipeline stall cycles.
    """
    def __init__(self, latencies=None):
        self.latencies = latencies or {"MUL": 3, "ADD": 1, "LOAD": 2, "STORE": 1}

    def schedule(self, dag_edges, nodes):
        in_degree = {n: 0 for n in nodes}
        adj = collections.defaultdict(list)
        for u, v in dag_edges:
            adj[u].append(v)
            in_degree[v] += 1

        ready = [n for n in nodes if in_degree[n] == 0]
        schedule_order = []

        while ready:
            ready.sort(key=lambda n: self.latencies.get(n.split()[0], 1), reverse=True)
            chosen = ready.pop(0)
            schedule_order.append(chosen)

            for v in adj[chosen]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    ready.append(v)

        return schedule_order
