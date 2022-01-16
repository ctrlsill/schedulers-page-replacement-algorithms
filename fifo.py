from numpy import random
import pandas as pd

def page_generator(n):
    pages = []
    for i in range(n):
        pages.append(random.randint(10))
    return pages


def save_to_csv(logs):
    col_names = ["PAGE", "RAM", "QUEUE[f->l]", "SWAPPED[in:out]"]
    df = pd.DataFrame(logs, columns=col_names)
    df.to_csv('fifo_logs.csv')


def print_logs(logs):
    col_names = ["PAGE", "RAM", "QUEUE[f->l]", "SWAPPED[in:out]"]
    df = pd.DataFrame(logs, columns=col_names)
    print(df)


INCOMING = [2, 5, 1, 0, 6, 3, 3, 5, 2, 6, 4, 2, 0, 0, 4, 8, 5, 4, 7, 8]
#page_generator(50)
QUEUE = []
RAM = []
LOGS = []

slots = 4
swap_count = 0
swap = None

#main loop
for page in INCOMING:

    if page not in QUEUE:
        if len(QUEUE) < slots:
            #filling RAM[]
            QUEUE.insert(0, page)
            RAM.append(page)
            swap = None
        else:
            #when RAM is full, start swaping pages
            QUEUE.insert(0, page)
            out = QUEUE.pop()

            swap = (page, out)
            swap_count += 1

            idx = RAM.index(out)
            RAM.pop(idx)
            RAM.insert(idx, page)
    else:
        swap = None

    #saving status of each iteration
    LOGS.append((page, RAM[:], QUEUE[:], swap))


print_logs(LOGS)
print("\nTotal pages swapped: ", swap_count, "\n")
save_to_csv(LOGS)