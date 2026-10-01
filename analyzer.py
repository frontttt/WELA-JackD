import event_reader

EVENT_TYPES = {
    4624: "Successful Logon",
    4625: "Failed Logon",
    4634: "Logoff",
    4648: "Logon using explicit credentials",
    4672: "Special privileges assigned",
    4688: "New process created",
    4720: "User account created",
    4726: "User account deleted",
    4732: "Account added to security-enabled local group",
    7045: "New Windows service installed"
}

def event_analyze(events):
    results = {
        "successful_logins": 0,
        "failed_logins": 0,
        "alerts": []
    }

    event_id = events
    if event_id == 4624:
        results["successful_logins"] += 1
    elif event_id == 4625:
        results["failed_logins"] += 1

    print(f"Succesful Logins: {results["successful_logins"]}")
    print(f"Failed Logins: {results["failed_logins"]}")
    print(f"Alerts: {results["alerts"]}")

    return results
            
