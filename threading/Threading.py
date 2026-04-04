from time import sleep, time
import threading

start_time = time()
def something(id):
    print(f"Going to sleep...{id}")
    sleep(1)
    print(f"Woken up...{id}")

# something()
# something()

# for _ in range(10):
#     something()


# t1 = threading.Thread(target=something, args=[0])
# t2 = threading.Thread(target=something, args=[1])
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

threads = [threading.Thread(target=something, args=[i]) for i in range(10)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time = time()

print(f"Main Thread Ended in {end_time - start_time} seconds")