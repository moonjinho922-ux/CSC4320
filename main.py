from data_generator import generate_processes, save_processes_csv, load_processes_csv
from metrics import summarize_results
from q1_schedulers import run_fifo, run_sjf, run_rr
from q2_q3_q4_schedulers import run_q2_scheduler, run_q3_scheduler, run_q4_scheduler


def make_sequential_arrival_copy(processes, arrival_gap=1):
    copied = []
    for index, proc in enumerate(processes):
        next_proc = dict(proc)
        next_proc['arrival_time'] = index * arrival_gap
        copied.append(next_proc)
    return copied


def main():
    processes = generate_processes(250)
    save_processes_csv(processes, 'processes.csv')
    processes = load_processes_csv('processes.csv')

    fifo_results = run_fifo(processes)
    sjf_results = run_sjf(processes)
    rr_results = run_rr(processes, quantum=100000000)

    q2_results = run_q2_scheduler(processes)
    q2_first_200_results = run_q2_scheduler(processes[:200])
    q3_results = run_q3_scheduler(processes[:200])
    q4_processes = make_sequential_arrival_copy(processes)
    q4_results = run_q4_scheduler(q4_processes)

    summarize_results(fifo_results, 'Q1 - FIFO')
    summarize_results(sjf_results, 'Q1 - SJF')
    summarize_results(rr_results, 'Q1 - Round Robin')
    summarize_results(q2_results, 'Q2')
    summarize_results(q2_first_200_results, 'Q2 - First 200 Processes')
    summarize_results(q3_results, 'Q3 - First 200 Processes with Memory Limits')
    summarize_results(q4_results, 'Q4')


if __name__ == '__main__':
    main()
