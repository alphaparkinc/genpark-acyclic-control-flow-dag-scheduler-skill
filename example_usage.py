from client import DAGListScheduler

def main():
    print("=== Testing Acyclic DAG Instruction List Scheduler ===")
    sched = DAGListScheduler()

    nodes = ["LOAD r1", "MUL r2", "ADD r3"]
    edges = [("LOAD r1", "ADD r3"), ("MUL r2", "ADD r3")]

    order = sched.schedule(edges, nodes)
    print("Optimal scheduled order:", order)
    assert order[0] == "MUL r2"
    assert order[-1] == "ADD r3"
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
