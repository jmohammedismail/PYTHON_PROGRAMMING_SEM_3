# MODULE 4 - MINI PROJECT
# JSON-Based Log File Analyzer
#
# Reads application log records from logs.json, displays every valid
# record, counts INFO/WARNING/ERROR messages, and handles missing or
# invalid JSON files.

import json

FILE_NAME = "logs.json"
LOG_LEVELS = ("INFO", "WARNING", "ERROR")


def load_logs():
    """Load and validate the JSON log data."""
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("The JSON root must contain a list of log records.")

        return data

    except FileNotFoundError:
        print(f"Error: {FILE_NAME} was not found.")
    except json.JSONDecodeError as error:
        print("Error: Invalid JSON data.")
        print("Details:", error)
    except (OSError, ValueError) as error:
        print("Error while loading log data:", error)

    return None


def analyze_logs():
    logs = load_logs()

    if logs is None:
        return

    counts = {level: 0 for level in LOG_LEVELS}
    valid_records = []

    # Validate each record before displaying or counting it.
    for index, record in enumerate(logs, start=1):
        if not isinstance(record, dict):
            print(f"Skipping invalid record {index}: expected a JSON object.")
            continue

        timestamp = record.get("timestamp")
        level = record.get("level")
        message = record.get("message")

        if not all(isinstance(value, str) and value.strip()
                   for value in (timestamp, level, message)):
            print(f"Skipping invalid record {index}: missing or invalid fields.")
            continue

        level = level.upper()
        if level not in counts:
            print(f"Skipping record {index}: unknown log level '{level}'.")
            continue

        valid_records.append({
            "timestamp": timestamp,
            "level": level,
            "message": message
        })
        counts[level] += 1

    print("\n========== APPLICATION LOGS ==========")

    if not valid_records:
        print("No valid log records found.")
    else:
        for record in valid_records:
            print(
                f"{record['timestamp']} | "
                f"{record['level']:<7} | "
                f"{record['message']}"
            )

    print("\n========== LOG SUMMARY ==========")
    print("Total valid log records:", len(valid_records))
    for level in LOG_LEVELS:
        print(f"Total {level} messages: {counts[level]}")


if __name__ == "__main__":
    analyze_logs()
