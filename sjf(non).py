from numpy import random
import pandas as pd

def generator(limit):
    processes = []
    for p in range(limit):
        proc = {"pid":(p+1), "burst":random.randint(1, 10), "arrival":None, "wait":None}
        processes.insert(0, proc)
    return processes[:]

def print_processes(proc):
    if len(proc) == 0:
        print("[empty]")
        return

    proc_list = []
    for p in proc:
        p = list(p.values())
        proc_list.append(p)

    col_names = ["PID", "burst", "arrival", "wait"]
    df = pd.DataFrame(proc_list, columns=col_names)
    print(df, "\n")

def save_to_csv(proc, filename):
    if len(proc) == 0:
        return

    proc_list = []
    for p in proc:
        p = list(p.values())
        proc_list.append(p)

    col_names = ["PID", "burst", "arrival", "wait"]
    df = pd.DataFrame(proc_list, columns=col_names)
    df.to_csv(filename)

def print_logs(logs):
    if len(logs) == 0:
        return

    col_names = ["cycle", "PROCESSES[]", "READY[]", "current (left)", "TERMINATED[]"]
    df = pd.DataFrame(logs, columns=col_names)
    print(df)

def save_logs_to_csv(logs, filename):
    if len(logs) == 0:
        return

    col_names = ["cycle", "PROCESSES[]", "READY[]", "current (left)", "TERMINATED[]"]
    df = pd.DataFrame(logs, columns=col_names)
    df.to_csv(filename)

def extract_pids(proc):
    pids = []
    for p in proc:
        pids.append(p["pid"])
    return pids[:]


def sjf_sort(proc):
    has_swapped = True

    while (has_swapped):
        has_swapped = False
        for i in range(len(proc) - 1):
            if proc[i]["burst"] < proc[i + 1]["burst"]:
                proc[i], proc[i + 1] = proc[i + 1], proc[i]
                has_swapped = True
    return proc[:]


processes = generator(10)
ready = []
terminated = []
logs = []

save_to_csv(processes, "processes.csv")

print("PROCESSES:")
print_processes(processes)
print("==================START=================================")

cycle = 1
current_left = 0


#main loop
while True:

    if random.randint(2) and len(processes) > 0:
        # randomly load new processes from PROCESSES
        load = processes.pop()
        load["arrival"] = cycle
        ready.insert(0, load)

        ready = sjf_sort(ready)



        print("[i]", "Added", load["pid"], "to READY[].")





    if current_left == 0:
        if cycle > 1:
            terminated.append(current)
            print("[i]", current["pid"], "terminated")

        if len(processes) == 0 and len(ready) == 0:
            logs.append((cycle, extract_pids(processes), extract_pids(ready), (current["pid"], current_left),
                         extract_pids(terminated)))
            print("[i] No more processes to execute")
            break

        if len(ready) > 0:
            current = ready.pop()
            current["wait"] = cycle - current["arrival"]
            current_left = current["burst"]

            print("[i]", current["pid"], "starts execution")
        else:
            print("[i] Waiting for processes")
            continue
    elif current_left > 0:
        current_left -= 1



    print("\nREADY:")
    print_processes(ready)
    print("CYCLE:", cycle)
    print("CURRENT: ", current["pid"], " (", current_left, " left)", sep="")
    print("\nTERMINATED:")
    print_processes(terminated)
    print("========================================================")

    logs.append((cycle, extract_pids(processes), extract_pids(ready), (current["pid"], current_left), extract_pids(terminated)))
    cycle += 1


print("\nPROCESSES:")
print_processes(processes)
print("\nREADY:")
print_processes(ready)
print("\nTERMINATED:")
print_processes(terminated)



wait_sum = 0
for p in terminated:
    wait_sum += p["wait"]
wait_avg = wait_sum / len(terminated)

print("Total cycles:", cycle)
print("Average wait time: ", wait_avg, "cycle")



print("\n========================= LOGS ==================================\n")
print_logs(logs)


save_to_csv(terminated, "terminated_sjf.csv")
save_logs_to_csv(logs, "logs_sjf.csv")







