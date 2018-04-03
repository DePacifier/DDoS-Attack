import ThreadClass

if __name__ == '__main__':
    noOfThreads = input("Insert the number of DoS attacker you want to create: ")
    print("Starting %s threaded requests: " % noOfThreads)
    for i in range(0, int(noOfThreads)):
        newThread = ThreadClass.ThreadClass("Thread " + str(i))
        newThread.start()
