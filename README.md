## Overview

This project simulates a dispatcher/scheduler that assigns 250 synthetic processes to 6 processors. Each process has a random burst time (10⁶ – 10¹² cycles) and memory requirement (1 MB – 16 GB).

## How to Run

```bash
python3 main.py
```

This will:
1. Generate 250 synthetic processes and save them to `processes.csv`
2. Re-load the processes from CSV (so all schedulers use the same data)
3. Run all six schedulers and print average waiting time and average turnaround time for each

## File Structure

| File | Purpose |
|---|---|
| `main.py` | Entry point — runs all schedulers and prints results |
| `data_generator.py` | Generates 250 random processes and saves/loads CSV |
| `models.py` | Helper functions to create process and processor dicts |
| `metrics.py` | Computes and prints average waiting/turnaround time |
| `q1_schedulers.py` | Q1 schedulers: FIFO, SJF, Round Robin (identical processors) |
| `q2_q3_q4_schedulers.py` | Q2–Q4 schedulers: heterogeneous processors, memory constraints, online |

## Notes

- All processes are assigned `arrival_time = 0` for Q1–Q3 (full batch is available upfront)
- Q4 uses the same data but processes in arrival (pid) order with no sorting — simulating an online scheduler
- Burst times are large (up to 10¹² cycles), so turnaround times are in the thousands of seconds by design