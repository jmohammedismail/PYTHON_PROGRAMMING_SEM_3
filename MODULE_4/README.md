# MODULE 4 - Python File Handling and CSV Programs

This module contains the three lab exercises.

## Files

| Lab | Python program | Sample output |
|---|---|---|
| Lab 1 | `LAB1_LOG_FILE_READER.py` | `LAB1_SAMPLE_OUTPUT.txt` |
| Lab 2 | `LAB2_STUDENT_DATA_MANAGER.py` | `LAB2_SAMPLE_OUTPUT.txt` |
| Lab 3 | `LAB3_CSV_BASED_PAYROLL_MANAGEMENT.py` | `LAB3_SAMPLE_OUTPUT.txt` |

## How to run

Open a terminal in this folder and run the required program:

```bash
python LAB1_LOG_FILE_READER.py
python LAB2_STUDENT_DATA_MANAGER.py
python LAB3_CSV_BASED_PAYROLL_MANAGEMENT.py
```

Lab 1 reads `log.txt), which must be placed in this folder. Labs 2 and 3 create their data files automatically:

- Lab 2: `students.txt`
- Lab 3: `payroll.csv`

All three programs use exception handling for common input and file errors.

## Mini Project - JSON-Based Log File Analyzer

| File | Purpose |
|---|---|
| `MINI_PROJECT_JSON_BASED_LOG_FILE_ANALYZER.py` | Python application |
| `logs.json` | Sample JSON log input |
| `MINI_PROJECT_SAMPLE_OUTPUT.txt` | Sample input and expected output |

Run it from this folder:

```bash
python MINI_PROJECT_JSON_BASED_LOG_FILE_ANALYZER.py
```

The program uses Python's `json` module, displays valid log records,
counts INFO, WARNING and ERROR entries, and handles missing files,
invalid JSON, and invalid records.
