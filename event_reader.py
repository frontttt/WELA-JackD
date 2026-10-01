import win32evtlog

def read_logs(log_type="System", max_records=100):
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
            event.EventID
            count += 1