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

SEVERITY_TYPES = {
       0: "[NONE]",
       1: "[LOW]",
       2: "[MEDIUM]",
       3: "[HIGH]"
}

def event_analyze(events):
    results = {
        "successful_logins": 0,
        "failed_logins": 0,
        "alerts": []
    }

    for event_id in events:
        if event_id == 4624:
                results["successful_logins"] += 1
        elif event_id == 4625:
                results["failed_logins"] += 1
        elif event_id == 4634:
                results["alerts"].append(EVENT_TYPES[4634] + " " + SEVERITY_TYPES[0])
        elif event_id == 4648:
                results["alerts"].append(EVENT_TYPES[4648] + " " + SEVERITY_TYPES[1])
        elif event_id == 4672:
                results["alerts"].append(EVENT_TYPES[4672] + " " + SEVERITY_TYPES[2])
        elif event_id == 4688:
                results["alerts"].append(EVENT_TYPES[4688] + " " + SEVERITY_TYPES[3])
        elif event_id == 4720:
                results["alerts"].append(EVENT_TYPES[4720] + " " + SEVERITY_TYPES[1])
        elif event_id == 4726:
                results["alerts"].append(EVENT_TYPES[4726] + " " + SEVERITY_TYPES[1])
        elif event_id == 4732:
                results["alerts"].append(EVENT_TYPES[4732] + " " + SEVERITY_TYPES[3])
        elif event_id == 7045:
                results["alerts"].append(EVENT_TYPES[7045] + " " + SEVERITY_TYPES[0])

    return results
            
