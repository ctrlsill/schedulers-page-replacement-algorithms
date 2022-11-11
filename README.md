### This repository contains simulation of 4 OS algorithms:

### Processors Time Scheduling

1. FCFS (First Come First Serve) - [fcfs.py](http://fcfs.py/)
2. SJF non preemptive (Shortest Path Firs in non preemptive version) - sjf(non).py

### Memory Page Replacement Algorithms:

1. FIFO (First In First Out) - [fifo.py](http://fifo.py/)
2. LRU (Least Recently Used) - [lru.py](http://lru.py/)

<aside>
💡 Every .py file works as independent Python script

</aside>

# Processors Time Scheduling Algorithms Details

### **INPUT:**

number of processes to be generated (default = 5 for demonstration reasons)

<aside>
💡 1 while loop cycle represents one processor clock time cycle

</aside>

### Steps of scripts execution:

1. Generator returns given number of processes and loads it to processes[]
2. Processes are being randomly added in real time to ready queue (ready[]):
    - if there is no processes in queue in current cycle → program goes to next cycle waiting for processes
    - if there are some ready processes → queue is processed by according sorting algorithm and then 1 process from the front of queue is loaded for execution by processor
3. Loaded process is being executed, while new process loads to ready queue
4. When current process finish its execution it terminates and frees up CPU for next process  
5. Whole operation repeats until all of processes are handled
6. When there’s no more processes waiting, program prints out summary of its execution 

### OUTPUT:

Script prints out to the console the state of every execution cycle:

- ℹ️ - info messages of performed actions in current cycle like: loading of the next process or termination of process
- current queue of ready processes
- number of current cycle
- currently running process PID and time left to end of its execution
- list of already terminated processes

When all of generated processes end its execution, program prints out summary of its execution:

- total cycles
- average waiting time
- logs

# Memory Page Replacement Algorithms Details
