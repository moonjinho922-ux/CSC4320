import csv
import random
from models import create_process


def generate_processes(k=250):
    processes = []

    for pid in range(1, k + 1):
        burst_cycles = random.randint(10**6, 10**12)
        memory_mb = random.randint(1, 16 * 1024)
        arrival_time = 0

        process = create_process(pid, burst_cycles, memory_mb, arrival_time)
        processes.append(process)

    return processes


def save_processes_csv(processes, filename='processes.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['pid', 'burst_cycles', 'memory_mb', 'arrival_time'])

        for process in processes:
            writer.writerow([
                process['pid'],
                process['burst_cycles'],
                process['memory_mb'],
                process['arrival_time']
            ])


def load_processes_csv(filename='processes.csv'):
    processes = []

    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            process = create_process(
                int(row['pid']),
                int(row['burst_cycles']),
                int(row['memory_mb']),
                int(row['arrival_time'])
            )
            processes.append(process)

    return processes