def display_alerts(results):
    print()
    print("=== Analysis Report ===")

    print(f"Successful Logins: {results["successful_logins"]}")
    print(f"Failed Logins: {results["failed_logins"]}")

    if results["alerts"]:
        print()
        print("=== ALERTS ===")

        print(results["alerts"])