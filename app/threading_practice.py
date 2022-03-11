from timeit import timeit
import requests
import threading


# Without threading
# Define a function for the thread
l = []
def heavy_func():
    for i in range(10000):
        print(i, end="\r")
        l.append(i)
        for j in l:
            if j%2!=0:
                l.remove(j)


# print(f"Without threading: {timeit('heavy_func()', setup='from __main__ import heavy_func', number=5)}")


# With threading
def heavy_func_threads():
    thread1 = threading.Thread(target=heavy_func, name=f"t1")
    thread2 = threading.Thread(target=heavy_func, name=f"t2")
    thread3 = threading.Thread(target=heavy_func, name=f"t3")
    thread4 = threading.Thread(target=heavy_func, name=f"t4")
    thread5 = threading.Thread(target=heavy_func, name=f"t5")


    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()

heavy_func_threads()

# print(f"With threading: {timeit('heavy_func_threads()', setup='from __main__ import heavy_func_threads')}")
