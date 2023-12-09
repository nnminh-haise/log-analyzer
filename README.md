# Log Analyzer

> *A small Python script for analyzing log entries.*

One day, I went to a coffee store on Ung Văn Khiêm Street and asked Chat GPT for a small Python project that I could complete in 2 - 3 days and this project is what GPT gave me.

## Project description

Project name: **Log analyzer**

### Project Overview

Create a log analyzer tool that reads log files, extracts information using regular expressions, organizes the data using classes, and performs basic analysis.

### Requirements

1. **Log File:**
    Choose or create a sample log file with entries containing relevant information (e.g., timestamp, log level, message).
2. **Log Entry Class:**
    Create a class to represent a log entry. Include attributes like timestamp, log level, and message.
3. **File Reading:**
    Implement a function to read the log file and create instances of the Log Entry class for each entry.
4. **Regex Extraction:**
    Use regular expressions to extract relevant information (e.g., timestamp, log level, message) from each log entry.
5. **Data Structures:**
    Use data structures to organize log entries. Consider using a list or dictionary to store instances of the Log Entry class.
6. **Analysis Functions:**
    Implement basic analysis functions, such as:
    - Count the total number of log entries.
    - Count the number of entries for each log level.
    - Find entries within a specific time range.
7. **User Interface (Optional):**
    If time permits, you can create a simple command-line interface or a basic GUI to interact with the log analyzer.

### Tips:

- Break down the tasks into smaller functions and methods.
- Test each component individually before combining them into the main program.
- Use modular and well-documented code.

### Example Project Structure:

```
log_analyzer/
|-- log_analyzer.py  # Main program
|-- log_entry.py     # Log Entry class
|-- utils.py         # Helper functions (file reading, regex, analysis)
|-- sample_log.log   # Sample log file

```

### Note:

This project is designed to be flexible, and you can expand it based on your interests and time constraints. If you finish the basic requirements quickly, consider adding more advanced features, such as trend analysis, error prediction, or visualization of log data.

***Sample log files:***

```
2023-12-07 10:15:30 INFO Application started
2023-12-07 10:20:45 WARNING Disk space is running low
2023-12-07 10:25:12 ERROR Connection failed: server unreachable
2023-12-07 10:30:01 INFO User logged in: username123
2023-12-07 10:35:40 DEBUG Processing data
2023-12-07 10:40:55 ERROR Critical error: system crash
2023-12-07 10:45:22 INFO Application shutdown
```

---

## My thoughts

After 10 minutes of reading the description, I got my hand on the project right away. It took me 3 hours to finish all the core functionality of the project. Then the laptop ran out of battery so I had to take a break from that. Then I came back the next day to finish the last two functions.

The project came out okay. I planned to make a CLI but I used a console interface instead. My plan for the next version will be to convert the current project to a CLI application and add more features to it.

## Usage

Requirements: install python.

Run the script by running the `log_analyzer.py` script using the below command:

```
python log_analyzer.py
```
