#!/usr/bin/env python3


import datetime
import os
from sqlite3 import Timestamp
import time
import log_entry as le
import log_util as lu


def show_menu():
    delay_time_sec = 1.5
    while True:
        try:
            os.system("cls")
            print("*------------Log Analyzer----------*")
            print("| [1]: Add Log entry               |")
            print("| [2]: Remove Log entry            |")
            print("| [3]: Show Log entries            |")
            print("| [4]: Read Log entries from files |")
            print("| [5]: Show statistic data         |")
            print("| [6]: Get Log entries in range    |")
            print("| [0]: Exit                        |")
            print("*----------------------------------*")

            print()
            selector = int(input("Select: "))

            if selector not in range(0, 7):
                print("Invalid selection!")
                time.sleep(delay_time_sec)
            else:
                return selector

        except ValueError as err:
            print("Invalid Input! Input must be integers")
            time.sleep(delay_time_sec)


def query_user_selection(selection: int):
    filepath = "log.txt"
    le_list, le_dict = lu.create_log_entry_list_and_dict(
        le.read_log_from_file(filepath)
    )

    os.system("cls")
    if selection is 0:
        try:
            log_file = open(filepath, "w")

            for log_entry in le_list:
                log_file.write(
                    f"{log_entry.timestamp} {log_entry.log_level} {log_entry.message}\n"
                )

        except IOError as err:
            print(f"ERROR: {err}")
        finally:
            log_file.close()

        return 0

    if selection in (2):
        print("Function is in development!")
    elif selection is 1:
        while True:
            os.system("cls")
            print("Creating new Log entry:\n")

            timestamp = input("Timestamp: ")
            log_level = input("Log level: ")
            message = input("Message: ")

            if lu.is_valid_timestamp(timestamp) is False:
                print("Invalid timestamp!")
                time.sleep(1.5)

    elif selection is 3:
        print("Log entries:\n")
        for log_entry in le_list:
            print(log_entry)
    elif selection is 4:
        le_list, le_dict = lu.create_log_entry_list_and_dict(
            le.read_log_from_file(filepath)
        )
    elif selection is 5:
        print("Statistic:\n")
        statistic_result = lu.analyze_log_entries(le_dict)
        total_entries = 0
        for key in statistic_result:
            buffer = statistic_result[key]
            print(
                f"There are {buffer} {'entries' if buffer > 1 else 'entry'} at {key} level."
            )
            total_entries += buffer

        print(
            f"Total amount of entries: {total_entries} {'entries' if total_entries > 1 else 'entry'}."
        )
    elif selection is 6:
        print("Selecting entries between timestamps:\n")

        begin_timestamp = input("Begin timestamp: ")
        end_timestamp = input("End timestamp: ")
        queried_log_entries = lu.get_log_in_range(
            le_list, begin_timestamp, end_timestamp
        )
        if queried_log_entries is None:
            pass
        elif len(queried_log_entries) is 0:
            print("No entries!")
        else:
            print()
            for log_entry in queried_log_entries:
                print(log_entry)
    else:
        print("Function is in development!")

    print()
    tmp = input("Enter to back to menu!")
    return 1


def main():
    while True:
        if query_user_selection(show_menu()) is 0:
            os.system("cls")
            print("Closing...")
            time.sleep(1)
            os.system("cls")
            break


main()


# for log_entry in get_log_in_range(
#     le_list, "2023-12-07 10:00:00", "2023-12-07 01:00:00"
# ):
#     print(log_entry)

# print("----")

# for log_entry in le_list:
#     print(log_entry)

# statistic_result = lu.analyze_log_entries(le_dict)
# for key in statistic_result.keys():
#     print(f"{statistic_result[key]} log_entries at {key} level")

# for key in le_dict.keys():
#     print(f"Log level: {key}")
#     for entry in le_dict[key]:
#         print(entry)
