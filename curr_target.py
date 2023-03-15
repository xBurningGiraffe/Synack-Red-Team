import time
import synack

h = synack.Handler()

# Check connected target
curr_target = h.targets.get_connected()
print(f"Currently connected to {curr_target}")