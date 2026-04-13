from data_generator import generate_processes, save_processes_csv, load_processes_csv
from metrics import summarize_results
from q1_schedulers import run_fifo, run_sjf, run_rr
from q2_q3_q4_schedulers import run_q2_scheduler, run_q3_scheduler, run_q4_scheduler


def main():
    processes = generate_processes(250)
    save_processes_csv(processes, 'processes.csv')
    processes = load_processes_csv('processes.csv')

    fifo_results = run_fifo(processes)
    sjf_results = run_sjf(processes)
    rr_results = run_rr(processes, quantum=100000000)

    q2_results = run_q2_scheduler(processes)
    q3_results = run_q3_scheduler(processes)
    q4_results = run_q4_scheduler(processes)

    summarize_results(fifo_results, 'Q1 - FIFO')
    summarize_results(sjf_results, 'Q1 - SJF')
    summarize_results(rr_results, 'Q1 - Round Robin')
    summarize_results(q2_results, 'Q2')
    summarize_results(q3_results, 'Q3')
    summarize_results(q4_results, 'Q4')


if __name__ == '__main__':
    main()