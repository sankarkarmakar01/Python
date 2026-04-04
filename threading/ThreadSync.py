import threading

balance = 200

lock = threading.Lock()

def deposit(amount, times,lock):
    global balance
    for _ in range(times):
        lock.acquare()
        balance += amount
        lock.release()


def withdraw(amount, times,lock):
    global balance
    for _ in range(times):
        lock.acquare()
        balance -= amount
        lock.release()

deposite_thread = threading.Thread(target=deposit, args=[1,10000,lock])
withdraw_thread = threading.Thread(target=withdraw, args=[1,10000,lock])

deposite_thread.start()
withdraw_thread.start()

deposite_thread.join()
withdraw_thread.join()

print(balance)