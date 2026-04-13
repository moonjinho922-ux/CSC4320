import heapq

SPEED = 2.0  # GHz, all processors same speed for Q1
NUM_PROCS = 6
QUANTUM = 100000000  # 10^8 cycles

def run_fifo(processes):
    # sort processes by arrival time (all arrive at 0 so order stays the same)
    sorted_procs = sorted(processes, key=lambda p: p['arrival_time'])

    # track when each processor becomes free
    proc_free = [0.0] * NUM_PROCS

    results = []

    for proc in sorted_procs:
        # find which processor is available the earliest
        min_free = proc_free[0]
        min_idx = 0
        for i in range(1, NUM_PROCS):
            if proc_free[i] < min_free:
                min_free = proc_free[i]
                min_idx = i

        start = max(proc['arrival_time'], proc_free[min_idx])
        exec_time = proc['burst_cycles'] / (SPEED * 1000000000)
        finish = start + exec_time

        proc_free[min_idx] = finish

        results.append({
            'pid': proc['pid'],
            'waiting_time': start - proc['arrival_time'],
            'turnaround_time': finish - proc['arrival_time']
        })

    return results

def run_sjf(processes):
    # sort by burst cycles so shortest job runs first
    sorted_procs = sorted(processes, key=lambda p: p['burst_cycles'])

    proc_free = [0.0] * NUM_PROCS

    results = []

    for proc in sorted_procs:
        # pick earliest free processor
        min_free = proc_free[0]
        min_idx = 0
        for i in range(1, NUM_PROCS):
            if proc_free[i] < min_free:
                min_free = proc_free[i]
                min_idx = i

        start = max(proc['arrival_time'], proc_free[min_idx])
        exec_time = proc['burst_cycles'] / (SPEED * 1000000000)
        finish = start + exec_time

        proc_free[min_idx] = finish

        results.append({
            'pid': proc['pid'],
            'waiting_time': start - proc['arrival_time'],
            'turnaround_time': finish - proc['arrival_time']
        })

    return results

def run_rr(processes, quantum=QUANTUM):
    import collections
    speed = SPEED * 1000000000  # convert GHz to cycles per second

    # remaining cycles left for each process
    remaining = {}
    for p in processes:
        remaining[p['pid']] = p['burst_cycles']

    finish_time = {}

    # use deque so popleft() is O(1) instead of O(n)
    ready_queue = collections.deque(
        p['pid'] for p in sorted(processes, key=lambda p: p['arrival_time'])
    )

    # event heap: (time_when_done, processor_id, pid)
    events = []

    # track processors that have no work so they can be woken up later
    idle_procs = []

    # give each processor its first process
    for i in range(NUM_PROCS):
        if ready_queue:
            pid = ready_queue.popleft()
            run_cycles = min(remaining[pid], quantum)
            t = run_cycles / speed
            remaining[pid] -= run_cycles
            if remaining[pid] == 0:
                finish_time[pid] = t
            heapq.heappush(events, (t, i, pid))
        else:
            idle_procs.append(i)

    while events:
        cur_time, proc_id, pid = heapq.heappop(events)

        # if this process still has cycles left, put it back at end of queue
        if remaining[pid] > 0:
            ready_queue.append(pid)
            # wake up an idle processor if one is waiting
            if idle_procs:
                wake_id = idle_procs.pop()
                next_pid = ready_queue.popleft()
                run_cycles = min(remaining[next_pid], quantum)
                t = run_cycles / speed
                remaining[next_pid] -= run_cycles
                if remaining[next_pid] == 0:
                    finish_time[next_pid] = cur_time + t
                heapq.heappush(events, (cur_time + t, wake_id, next_pid))

        # assign next process in queue to this processor
        if ready_queue:
            next_pid = ready_queue.popleft()
            run_cycles = min(remaining[next_pid], quantum)
            t = run_cycles / speed
            remaining[next_pid] -= run_cycles
            if remaining[next_pid] == 0:
                finish_time[next_pid] = cur_time + t
            heapq.heappush(events, (cur_time + t, proc_id, next_pid))
        else:
            idle_procs.append(proc_id)

    # calculate wait and turnaround times
    results = []
    for p in processes:
        pid = p['pid']
        service_time = p['burst_cycles'] / speed
        turnaround = finish_time[pid] - p['arrival_time']
        waiting = turnaround - service_time
        results.append({
            'pid': pid,
            'waiting_time': waiting,
            'turnaround_time': turnaround
        })

    return results