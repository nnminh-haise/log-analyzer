import re


class LogEntry:
    def __init__(self, timestamp, log_level, message):
        self.timestamp = timestamp
        self.log_level = log_level
        self.message = message

    def __str__(self):
        return f"({self.timestamp})[{self.log_level}]: {self.message}"


def parse_log_entry(raw_data: str):
    regex_pattern = re.compile(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.*)")
    match = regex_pattern.match(raw_data)

    if match:
        timestamp, log_level, message = match.groups()
        return LogEntry(timestamp, log_level, message)
    else:
        return None


def extract_entries_from_files(raw_data: str):
    raw_entries = raw_data.split("\n")
    log_entries = list()
    for entries in raw_entries:
        log_entry = parse_log_entry(entries)
        if log_entry is not None:
            log_entries.append(log_entry)

        # * This is the simple approach to extract the log_entry's information from files
        # entry_info = entries.split(" ")
        # if len(entry_info) > 4:
        #     log_entries.append(
        #         LogEntry(
        #             timestamp=" ".join(entry_info[0:2]),
        #             log_level=entry_info[2],
        #             message=" ".join(entry_info[3:]),
        #         )
        #     )

    return log_entries


def read_log_from_file(filepath: str):
    try:
        log_file = open(filepath, "r")
        data = log_file.read()
        log_file.close()

        return extract_entries_from_files(data)
    except IOError as err:
        print(f"ERROR: {err}")
        return None
    finally:
        print("File reading process finished!")
