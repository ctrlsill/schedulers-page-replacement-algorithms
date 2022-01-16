from numpy import random
import pandas as pd


def page_generator(n):
    pages = []
    for i in range(n):
        pages.append(random.randint(10))
    return pages

def save_to_csv(alogs, filename):
    col_names = ["PAGE", "RAM", "QUEUE[in->out]", "SWAPPED[in:out]"]
    df = pd.DataFrame(alogs, columns=col_names)
    df.to_csv(filename)


def print_logs(alogs):
    col_names = ["PAGE", "RAM", "QUEUE[f->l]", "SWAPPED[in:out]"]
    df = pd.DataFrame(alogs, columns=col_names)
    print(df)


INCOMING = [2, 5, 1, 0, 6, 3, 3, 5, 2, 6, 4, 2, 0, 0, 4, 8, 5, 4, 7, 8]
#INCOMING = page_generator(50)

slots = 4
swap = None
swap_count = 0

queue = []
ram = []
logs = []

#main loop
for page in INCOMING:

    if page not in queue:
        if len(queue) < slots:
            # filling RAM[]
            queue.insert(0, page)
            ram.append(page)
            swap = None

        else:
            # classic fifo
            queue.insert(0, page)
            out = queue.pop()
            swap = (page, out)
            swap_count += 1
            #replacing pages in RAM on right positions
            idx = ram.index(out)
            ram.pop(idx)
            ram.insert(idx, page)



    else:
        queue.insert(0, queue.pop(queue.index(page)))
        swap = None
    logs.append((page, ram[:], queue[:], swap))


print_logs(logs)
print("Total pages swapped: ", swap_count, "\n")
save_to_csv(logs, "lru_logs.csv")