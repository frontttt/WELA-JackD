import event_reader
import analyzer
import alerts

def main():
    print("WINDOWS EVENT LOG ANALYZER")
    print("-========================-")
    events = event_reader.read_logs()
    analysis = analyzer.event_analyze(events)
    print(analysis)

if __name__ == "__main__":
    main()