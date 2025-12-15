from pathlib import Path

log_file_path = Path(__file__).parent / "server.txt"


def read_logs(path: Path) -> list[str]:
    """Read all logs into a list of strings."""
    with open(path, encoding="utf-8") as log_file:  # noqa: PTH123
        all_lines = log_file.readlines()
    return [line.strip() for line in all_lines if line.strip()]


def get_logs_level_summary(lines: list[str]) -> dict:
    """Get logs level summary."""
    # Initialize counters for each log level
    log_levels = {"INFO": 0, "WARNING": 0, "ERROR": 0, "DEBUG": 0}
    # Split each line and check the log level
    for line in lines:
        log_level = line.split(" ")[2]
        if log_level not in log_levels:
            print(f"Log level with name: {log_level} is missing.")
            continue
        log_levels[log_level] = log_levels[log_level] + 1
    return log_levels


def get_most_common_log_level(log_levels_counter: dict) -> str:
    """Get the log name with the biggest count."""
    biggest = ""
    best_count = 0
    for level, count in log_levels_counter.items():
        if count > best_count:
            best_count = count
            biggest = level
    return biggest
    # max(log_levels_counter, key=log_levels_counter.get)  # noqa: ERA001


def write_all_lines_with_level(lines: list[str], most_common_level: str) -> None:
    """Write filtered log lines to file."""
    output_path = Path(__file__).parent / f"server_{most_common_level}.txt"
    with open(output_path, "w", encoding="utf-8") as output_file:  # noqa: PTH123
        for line in lines:
            if most_common_level in line:
                output_file.write(f"{line}\n")


def main() -> None:
    """Run logs analysis."""
    print(f"Starting analysis for file: {log_file_path}")
    all_lines = read_logs(log_file_path)
    print(f"Total lines: {len(all_lines)}")
    log_levels = get_logs_level_summary(all_lines)
    print(log_levels)
    most_common_level = get_most_common_log_level(log_levels)
    print(f"Most common level is: {most_common_level}")
    write_all_lines_with_level(all_lines, most_common_level)


if __name__ == "__main__":
    main()
