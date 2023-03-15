import synack

h = synack.Handler()

notifications = h.notifications.get_unread_count()
h.alerts.slack(notifications)
