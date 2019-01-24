import threading


def worker(tid):
    """This is what the thread actually executes"""
    for i in range(tid * 100000):
        print("I'm working on thread {} with count {}".format(tid, i))
    return


def main():
    threads = list()
    for i in range(32):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()


if __name__ == "__main__":
    main()