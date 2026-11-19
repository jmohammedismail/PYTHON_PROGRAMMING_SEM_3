# MODULE 5 – Python Programming Lab

This module contains the three lab exercises and one mini project listed in the practical syllabus.

## Programs

| No. | Program | Main concepts |
|---|---|---|
| 1 | Bank Account Management System | Classes, objects, encapsulation, deposits and withdrawals |
| 2 | Library Management System | Classes, lists, issue/return operations, search |
| 3 | Dice Simulator | `random` module, loops and input validation |
| 4 | Retail Sales Dashboard | CSV processing, aggregation and Matplotlib charts |

## Folder structure

```
MODULE_5/
├── README.md
├── requirements.txt
├── bank_account_system.py
├── library_management_system.py
├── dice_simulator.py
├── retail_sales_dashboard.py
├── data/
│   └── retail_sales.csv
└── sample_outputs/
    ├── bank_account_system_output.txt
    ├── library_management_system_output.txt
    ├── dice_simulator_output.txt
    └── retail_sales_dashboard_output.txt
```

## Run the programs

Run commands from the repository root:

```bash
python MODULE_5/bank_account_system.py
python MODULE_5/library_management_system.py
python MODULE_5/dice_simulator.py
pip install -r MODULE_5/requirements.txt
python MODULE_5/retail_sales_dashboard.py
```

The retail dashboard reads the included CSV file and opens Matplotlib charts. If the chart window is unavailable, use a graphical Python environment.

All sample outputs are illustrative terminal sessions. Dice values and menu interactions can differ between runs.
