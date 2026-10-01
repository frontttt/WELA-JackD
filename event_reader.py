import win32evtlog

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

def read_logs(log_type="System", max_records=10):
    server = 'localhost'
    hand = win32evtlog.OpenEventLog(server, log_type)
    flag = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    total = win32evtlog.GetNumberOfEventLogRecords(hand)
    print(f"Total records in {log_type}: {total}\n")

    count = 0
    while count < max_records:
        events = win32evtlog.ReadEventLog(hand, flag, 0)
        if not events:
            break

        for event in events:
            print(f"Record Number: {event.RecordNumber}")
            print(f"Event ID: {event.EventID}")
            print(f"Time Generated: {event.TimeGenerated}")
            print(f"Source Name: {event.SourceName}")

            if event.StringInserts:
                print("Message Data:")
                for msg in event.StringInserts:
                    print(f" {msg}")

            print("-" * 40)
            count += 1

def main():
    read_logs("Security", 5)

if __name__ == "__main__":
    main()