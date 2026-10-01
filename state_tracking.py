def track_state():
    state = {
        "done": False,
        "stage": 0,
        "status": None
    }

    max_iters = 10

    for i in range(max_iters):
        state["stage"] += 1
        print(f"Iteration {state['stage']}")

        print("Observe")
        print("Decide")
        print("Act")

        if state["stage"] == 3:
            state["done"] = True
            state["status"] = "success"
            return state

    state["done"] = True
    state["status"] = "failure"
    return state

result = track_state()
print(result)