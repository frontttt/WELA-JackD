import event_reader
import analyzer
import alerts

def main():
    print("WINDOWS EVENT LOG ANALYZER")
    print("-========================-")
    events = event_reader.read_logs("Security", 1000)
    analysis = analyzer.event_analyze(events)
    alerts.display_alerts(analysis)

if __name__ == "__main__":
    main()