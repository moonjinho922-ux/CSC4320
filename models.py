def create_process(pid, burst_cycles, memory_mb, arrival_time=0):
    return {
        'pid': pid,
        'burst_cycles': burst_cycles,
        'memory_mb': memory_mb,
        'arrival_time': arrival_time
    }


def create_processor(processor_id, speed_ghz, memory_mb):
    return {
        'id': processor_id,
        'speed_ghz': speed_ghz,
        'memory_mb': memory_mb,
        'available_time': 0
    }