def average_waiting_time(results):
    if not results:
        return 0

    total = 0
    for process in results:
        total += process['waiting_time']

    return total / len(results)


def average_turnaround_time(results):
    if not results:
        return 0

    total = 0
    for process in results:
        total += process['turnaround_time']

    return total / len(results)


def summarize_results(results, title=''):
    avg_wait = average_waiting_time(results)
    avg_turn = average_turnaround_time(results)

    print()
    print(title)
    print('Average Waiting Time:', avg_wait)
    print('Average Turnaround Time:', avg_turn)