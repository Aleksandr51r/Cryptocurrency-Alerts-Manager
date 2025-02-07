import threading
import time

def task(name, delay):
    print(f"Start {name}")
    time.sleep(delay)
    print(f"end {name} ")

thread2 = threading.Thread(target=task, args=("B", 3))
thread1 = threading.Thread(target=task, args=("A", 2))

thread1.start()
thread2.start()

thread1
thread2

print("All stoped")
