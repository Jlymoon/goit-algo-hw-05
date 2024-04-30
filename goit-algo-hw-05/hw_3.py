import sys


def parse_log_line(line):
    parts = line.split(" ", 4)
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3] + " " + parts[4] if len(parts) > 4 else parts[3]
    }


def load_logs(file_path):
    logs = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                logs.append(parse_log_line(line.strip()))
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs, level):
    return [log for log in logs if log["level"] == level.upper()]


def count_logs_by_level(logs):
    counts = {}
    for log in logs:
        level = log["level"]
        if level not in counts:
            counts[level] = 1
        else:
            counts[level] += 1
    return counts


def display_log_counts(counts):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in sorted(counts.items()):
        print(f"{level:<16} | {count}")


def main():
    if len(sys.argv) < 2:
        print("Вкажіть шлях до лог-файлу.")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) >= 3:
        level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()
