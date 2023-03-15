import time
import json
import synack


h = synack.Handler()


# Register new targets
unreg_targets = h.targets.get_unregistered()

if unreg_targets:
    registered_targets = h.targets.set_unregistered([unreg_targets[0]])
    reg_payload = {
        "text": f"Newly registered targets: {registered_targets}"
    }
    h.alerts.slack(reg_payload)
else:
    print(f"No unregistered targets found")
