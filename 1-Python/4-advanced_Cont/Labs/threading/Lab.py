#import the threading module
import threading

def task1(num):
    for i in range(0,num):
        print('task1')

def task2(num):
    for i in range(0,num):
        print('task2')

if __name__ == "__main__":
    #creating threads
    t1 = threading.Thread(target=task1,args=(5,))
    t2 = threading.Thread(target=task2,args=(5,))

    #starting thread 1
    t1.start()
    #starting thread 2
    t2.start()
    #wait until thread 1 is completely executed
    t1.join()
    #wait until thread 2 is completely executed
    t2.join()

    #both threads are completely executed
    print('Done!')