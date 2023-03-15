#!/usr/bin/env python3

import time
import synack

h = synack.Handler(login=True)
print("Successfully logged into LP+")

known_missions = 0
print("Searching for missions...")

while True:
    time.sleep(30)
    curr_missions = h.missions.get_count()
    print(f"Currently {curr_missions} missions")
    if curr_missions and curr_missions > known_missions:
        print("New missions discovered")
        known_missions = curr_missions
        missions = h.missions.get_available()
        print(f"Available missions: {len(missions)}")
        for m in missions:
            time.sleep(1)
            outcome = h.missions.set_claimed(m)
            h.db.slack_url = 'https://hooks.slack.com/services/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'
            payload = {
                "text": "New missions claimed: {outcome}"
            }
            sani_payload = h.alerts.sanitize(payload)
            h.alerts.slack(sani_payload)
    elif curr_missions == 0:
        print("No current missions")
        known_missions = 0

