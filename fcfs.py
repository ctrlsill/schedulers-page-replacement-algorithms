from numpy import random
import pandas as pd

def generator(limit):
    processes = []
    for p in range(limit):
        proc = {"pid":(p+1), "burst":random.randint(1, 10), "arrival":None, "wait":None}
        processes.insert(0, proc)
    return processes

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
    return pids


PROCESSES = generator(5)
READY = []
TERMINATED = []
LOGS = []

save_to_csv(PROCESSES, "processes.csv")

print("PROCESSES:")
print_processes(PROCESSES)
print("==================START=================================")

cycle = 1
current_left = 0

#first load
# load = PROCESSES.pop()
# load["arrival"] = cycle
# READY.insert(0, load)
# print("[i]", "Added", load["pid"], "to READY[].")

#main loop
while True:


    if random.randint(2) and len(PROCESSES) > 0:
        # randomly load new processes from PROCESSES
        load = PROCESSES.pop()
        load["arrival"] = cycle
        READY.insert(0, load)

        print("[i]", "Added", load["pid"], "to READY[].")



    if len(PROCESSES) == 0 and len(READY) == 0 and current_left == 0:
        TERMINATED.append(current)
        print("[i] No more processes to execute")
        break


    if current_left == 0:
        if cycle > 1:
            TERMINATED.append(current)
            print("[i]", current["pid"], "terminated")

        if len(READY) > 0:
            current = READY.pop()
            current["wait"] = cycle - current["arrival"]
            current_left = current["burst"]

            print("[i]", current["pid"], "starts execution")
        else:
            print("[i] Waiting for processes")
            continue
    elif current_left > 0:
        current_left -= 1



    print("\nREADY:")
    print_processes(READY)
    print("CYCLE:", cycle)
    print("CURRENT: ", current["pid"], " (", current_left, " left)", sep="")
    # print("\nPROCESSES:")
    # print_processes(PROCESSES)
    print("\nTERMINATED:")
    print_processes(TERMINATED)
    print("========================================================")



    LOGS.append( (cycle, extract_pids(PROCESSES), extract_pids(READY), (current["pid"], current_left), extract_pids(TERMINATED) ))

    cycle += 1


print("\nPROCESSES:")
print_processes(PROCESSES)
print("\nREADY:")
print_processes(READY)
print("\nTERMINATED:")
print_processes(TERMINATED)

wait_sum = 0
for p in TERMINATED:
    wait_sum += p["wait"]

wait_avg = wait_sum / len(TERMINATED)

print("Total cycles:", cycle)
print("Average wait time: ", wait_avg, "cycle")




print("\n========================= LOGS ==================================\n")
print_logs(LOGS)


save_to_csv(TERMINATED, "terminated.csv")
save_logs_to_csv(LOGS, "logs_fcfs.csv")







