from datetime import datetime
import log_entry as le


def create_log_entry_list_and_dict(log_entries: list):
    log_entry_dict = dict()
    log_entry_list = list()

    for log_entry in log_entries:
        log_entry_dict.setdefault(log_entry.log_level, []).append(log_entry)

        if len(log_entry_list) == 0:
            log_entry_list.append(log_entry)
        else:
            left, right = 0, len(log_entry_list) - 1
            while left <= right:
                mid = left + (right - left) // 2

                if log_entry_list[mid].timestamp <= log_entry.timestamp:
                    left = mid + 1
                else:
                    right = mid - 1

            log_entry_list.insert(left, log_entry)

    return log_entry_list, log_entry_dict


def is_valid_timestamp(timestamp: str):
    try:
        datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
    except ValueError as err:
        print(f"ERROR: {err}")
        return False

    return True


def lower_bound_log_entry(le_list: list, timestamp: str):
    left, right = 0, len(le_list) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if le_list[mid].timestamp >= timestamp:
            right = mid - 1
        else:
            left = mid + 1

    return left


def upper_bound_log_entry(le_list: list, timestamp: str):
    left, right = 0, len(le_list) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if le_list[mid].timestamp <= timestamp:
            left = mid + 1
        else:
            right = mid - 1

    return left


def get_log_in_range(le_list: list, begin_timestamp: str, end_timestamp: str):
    if False in (
        is_valid_timestamp(begin_timestamp),
        is_valid_timestamp(end_timestamp),
    ):
        return None

    if datetime.strptime(begin_timestamp, "%Y-%m-%d %H:%M:%S") > datetime.strptime(
        end_timestamp, "%Y-%m-%d %H:%M:%S"
    ):
        return tuple()

    left, right = lower_bound_log_entry(
        le_list, begin_timestamp
    ), upper_bound_log_entry(le_list, end_timestamp)

    return tuple(le_list[left:right])


def analyze_log_entries(le_dict: dict):
    return {log_level: len(log_entries) for log_level, log_entries in le_dict.items()}
