from pathlib import Path

log_file_path = Path(__file__).parent / "server.txt"


def read_logs(path: Path) -> list[str]:
    """Read all logs into a list of strings."""
    with open(path, encoding="utf-8") as log_file:  # noqa: PTH123
        all_lines = log_file.readlines()
    return [line.strip() for line in all_lines if line.strip()]


def show_logs_level_summary(lines: list[str]) -> None:
    """Show logs level summary."""
    # Initialize counters for each log level
    # Split each line and check the log level
    # Create a summary dictionary
    # Print the summary
    # Example log levels: INFO, WARNING, ERROR, DEBUG


def main() -> None:
    """Run logs analysis."""
    print(f"Starting analysis for file: {log_file_path}")
    all_lines = read_logs(log_file_path)
    print(f"Total lines: {len(all_lines)}")
    show_logs_level_summary(all_lines)


if __name__ == "__main__":
    main()
