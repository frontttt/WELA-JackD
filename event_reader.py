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

event_id = 4624

print(EVENT_TYPES.get(event_id, "Unknown Event"))