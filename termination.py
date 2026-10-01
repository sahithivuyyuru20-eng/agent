def agent_loop(max_iters=10):
    state = {
        "done": False,
        "stage": "start"
    }

    for i in range(max_iters):
        # Observe
        state["stage"] = "observe"

        # Decide
        state["stage"] = "decide"

        # Act
        state["stage"] = "act"

        # Success → terminate
        if success_condition():
            state["done"] = True
            state["stage"] = "success"
            return "success", state

    # Max iterations → terminate with failure
    state["done"] = True
    state["stage"] = "failure"
    return "failure", state