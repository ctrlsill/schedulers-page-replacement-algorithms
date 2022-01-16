from numpy import random
import pandas as pd

def page_generator(n):
    pages = []
    for i in range(n):
        pages.append(random.randint(10))
    return pages


def save_to_csv(alogs, filename):
    col_names = ["PAGE", "RAM", "QUEUE[f->l]", "SWAPPED[in:out]"]
    df = pd.DataFrame(alogs, columns=col_names)
    df.to_csv(filename)


def print_logs(alogs):
    col_names = ["PAGE", "RAM", "QUEUE[f->l]", "SWAPPED[in:out]"]
    df = pd.DataFrame(alogs, columns=col_names)
    print(df)


incoming = [2, 5, 1, 0, 6, 3, 3, 5, 2, 6, 4, 2, 0, 0, 4, 8, 5, 4, 7, 8]
#page_generator(50)
queue = []
ram = []
logs = []

slots = 4
swap_count = 0
swap = None

#main loop
for page in incoming:

    if page not in queue:
        if len(queue) < slots:
            #filling RAM[]
            queue.insert(0, page)
            ram.append(page)
            swap = None
        else:
            #when RAM is full, start swaping pages
            queue.insert(0, page)
            out = queue.pop()

            swap = (page, out)
            swap_count += 1

            idx = ram.index(out)
            ram.pop(idx)
            ram.insert(idx, page)
    else:
        swap = None

    #saving status of each iteration
    logs.append((page, ram[:], queue[:], swap))


print_logs(logs)
print("\nTotal pages swapped: ", swap_count, "\n")
save_to_csv(logs, "fifo_logs.csv")