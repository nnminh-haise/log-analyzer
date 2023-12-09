#!/usr/bin/env python3


import os
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


def query_user_selection(selection: int, le_list, le_dict, filepath):
    os.system("cls")
    if selection == 0:
        return 0
    elif selection == 1:
        while True:
            os.system("cls")
            print("Creating new Log entry:\n")

            timestamp = input("Timestamp: ")
            log_level = input("Log level: ")
            message = input("Message: ")

            if lu.is_valid_timestamp(timestamp) is False:
                print("Invalid timestamp!")
                time.sleep(1.5)
            elif log_level not in ("INFO", "WARNING", "DEBUG", "ERROR"):
                print("Invalid log level!")
                time.sleep(1.5)
            else:
                new_log_entry = le.LogEntry(timestamp, log_level, message)
                # Add new log entry to list
                log_entry_index = lu.upper_bound_log_entry(le_list, timestamp)
                le_list.insert(log_entry_index, new_log_entry)
                # Add new log entry to dict
                le_dict.setdefault(log_level, []).append(new_log_entry)

                print("Successfully created new log entry!")
                break
    elif selection == 2:
        while True:
            os.system("cls")
            print("Removing Log entry:\n")

            timestamp = input("Timestamp: ")

            if lu.is_valid_timestamp(timestamp) is False:
                print("Invalid timestamp!")
                time.sleep(1.5)
            else:
                targeting_entries = [e for e in le_list if e.timestamp == timestamp]
                print("Removale log entries:")
                index = 1
                for e in targeting_entries:
                    print(f"[{index}] - {e}")
                    index += 1

                remove_item_index = int(input("Remove entry index: "))
                remove_target = targeting_entries[remove_item_index - 1]
                le_dict[remove_target.log_level].remove(remove_target)
                le_list.remove(remove_target)
                print("Successfully remove entry!")

                break

    elif selection == 3:
        print("Log entries:\n")
        for log_entry in le_list:
            print(log_entry)
    elif selection == 4:
        le_list, le_dict = lu.create_log_entry_list_and_dict(
            le.read_log_from_file(filepath)
        )
    elif selection == 5:
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
    elif selection == 6:
        print("Selecting entries between timestamps:\n")

        begin_timestamp = input("Begin timestamp: ")
        end_timestamp = input("End timestamp: ")
        queried_log_entries = lu.get_log_in_range(
            le_list, begin_timestamp, end_timestamp
        )
        if queried_log_entries is None:
            pass
        elif len(queried_log_entries) == 0:
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
    filepath = "log_entries.txt"
    le_list, le_dict = lu.create_log_entry_list_and_dict(
        le.read_log_from_file(filepath)
    )
    while True:
        if query_user_selection(show_menu(), le_list, le_dict, filepath) == 0:
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

            os.system("cls")
            print("Closing...")
            time.sleep(1)
            os.system("cls")
            break


main()
