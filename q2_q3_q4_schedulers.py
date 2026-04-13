def run_q2_scheduler(processes):
    # Q2
    # PA, PB, PC = 2 GHz and PD, PE, PF = 4 GHz
    processors = [
        {'id': 'PA', 'speed_ghz': 2.0, 'avail': 0.0},
        {'id': 'PB', 'speed_ghz': 2.0, 'avail': 0.0},
        {'id': 'PC', 'speed_ghz': 2.0, 'avail': 0.0},
        {'id': 'PD', 'speed_ghz': 4.0, 'avail': 0.0},
        {'id': 'PE', 'speed_ghz': 4.0, 'avail': 0.0},
        {'id': 'PF', 'speed_ghz': 4.0, 'avail': 0.0},
    ]

    # sort by burst cycles to minimize turnaround (shortest job first)
    sorted_procs = sorted(processes, key=lambda p: p['burst_cycles'])

    results = []

    for proc in sorted_procs:
        # find which processor finishes this process the earliest
        best_finish = float('inf')
        best_idx = 0

        for i in range(len(processors)):
            start = max(proc['arrival_time'], processors[i]['avail'])
            exec_time = proc['burst_cycles'] / (processors[i]['speed_ghz'] * 1000000000)
            finish = start + exec_time
            if finish < best_finish:
                best_finish = finish
                best_idx = i

        # assign the process to the best processor
        start_time = max(proc['arrival_time'], processors[best_idx]['avail'])
        exec_time = proc['burst_cycles'] / (processors[best_idx]['speed_ghz'] * 1000000000)
        finish_time = start_time + exec_time
        processors[best_idx]['avail'] = finish_time

        results.append({
            'pid': proc['pid'],
            'waiting_time': start_time - proc['arrival_time'],
            'turnaround_time': finish_time - proc['arrival_time']
        })

    return results


def run_q3_scheduler(processes):
    # Q3
    # PA, PB, PC = 2 GHz 8 GB and PD, PE, PF = 4 GHz 16 GB
    processors = [
        {'id': 'PA', 'speed_ghz': 2.0, 'memory_mb': 8192,  'avail': 0.0},
        {'id': 'PB', 'speed_ghz': 2.0, 'memory_mb': 8192,  'avail': 0.0},
        {'id': 'PC', 'speed_ghz': 2.0, 'memory_mb': 8192,  'avail': 0.0},
        {'id': 'PD', 'speed_ghz': 4.0, 'memory_mb': 16384, 'avail': 0.0},
        {'id': 'PE', 'speed_ghz': 4.0, 'memory_mb': 16384, 'avail': 0.0},
        {'id': 'PF', 'speed_ghz': 4.0, 'memory_mb': 16384, 'avail': 0.0},
    ]

    # sort by burst cycles same as Q2
    sorted_procs = sorted(processes, key=lambda p: p['burst_cycles'])

    results = []

    for proc in sorted_procs:
        best_finish = float('inf')
        best_idx = -1

        for i in range(len(processors)):
            # skip this processor if it doesnt have enough memory
            if proc['memory_mb'] > processors[i]['memory_mb']:
                continue

            start = max(proc['arrival_time'], processors[i]['avail'])
            exec_time = proc['burst_cycles'] / (processors[i]['speed_ghz'] * 1000000000)
            finish = start + exec_time

            if finish < best_finish:
                best_finish = finish
                best_idx = i

        if best_idx == -1:
            # no processor has enough memory, skip process
            continue

        start_time = max(proc['arrival_time'], processors[best_idx]['avail'])
        exec_time = proc['burst_cycles'] / (processors[best_idx]['speed_ghz'] * 1000000000)
        finish_time = start_time + exec_time
        processors[best_idx]['avail'] = finish_time

        results.append({
            'pid': proc['pid'],
            'waiting_time': start_time - proc['arrival_time'],
            'turnaround_time': finish_time - proc['arrival_time']
        })

    return results


def run_q4_scheduler(processes):
    # Q4
    # same hardware as Q3
    processors = [
        {'id': 'PA', 'speed_ghz': 2.0, 'memory_mb': 8192,  'avail': 0.0},
        {'id': 'PB', 'speed_ghz': 2.0, 'memory_mb': 8192,  'avail': 0.0},
        {'id': 'PC', 'speed_ghz': 2.0, 'memory_mb': 8192,  'avail': 0.0},
        {'id': 'PD', 'speed_ghz': 4.0, 'memory_mb': 16384, 'avail': 0.0},
        {'id': 'PE', 'speed_ghz': 4.0, 'memory_mb': 16384, 'avail': 0.0},
        {'id': 'PF', 'speed_ghz': 4.0, 'memory_mb': 16384, 'avail': 0.0},
    ]

    # processes arrive in order, we cant reorder them
    arrival_order = sorted(processes, key=lambda p: (p['arrival_time'], p['pid']))

    results = []

    for proc in arrival_order:
        best_finish = float('inf')
        best_idx = -1

        for i in range(len(processors)):
            if proc['memory_mb'] > processors[i]['memory_mb']:
                continue

            start = max(proc['arrival_time'], processors[i]['avail'])
            exec_time = proc['burst_cycles'] / (processors[i]['speed_ghz'] * 1000000000)
            finish = start + exec_time

            if finish < best_finish:
                best_finish = finish
                best_idx = i

        if best_idx == -1:
            continue

        start_time = max(proc['arrival_time'], processors[best_idx]['avail'])
        exec_time = proc['burst_cycles'] / (processors[best_idx]['speed_ghz'] * 1000000000)
        finish_time = start_time + exec_time
        processors[best_idx]['avail'] = finish_time

        results.append({
            'pid': proc['pid'],
            'waiting_time': start_time - proc['arrival_time'],
            'turnaround_time': finish_time - proc['arrival_time']
        })

    return results