import threading
import random
import time

shared_variable = 100
sum_values = 0
lock = threading.Lock()

def producer():
    global shared_variable
    for _ in range(5):
        random_wait = random.randint(1, 3)
        time.sleep(random_wait)
        with lock:
            shared_variable = random.randint(0, 4)

def consumer():
    global shared_variable, sum_values
    for _ in range(5):
        random_wait = random.randint(1, 3)
        time.sleep(random_wait)
        with lock:
            sum_values += shared_variable

def main():
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    with open('sum2.txt', 'w') as file:
        file.write(str(sum_values))

if __name__ == '__main__':
    main()