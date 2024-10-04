import threading
import time
# define a function that will be executed by each thread

def print_numbers():
    for i in range(5):
        print(f"Thread{threading.current_thread().name}: {i}")
        time.sleep(1)  #simulate some work being done
        
#create multiple threads

thread1=threading.Thread(target=print_numbers, name="thread1")
thread2=threading.Thread(target=print_numbers, name="thread2")

#start the threads

thread1.start()
thread2.start()


