# producer.py
import time

def produce():
    while True:
        with open("producerOut.txt", "a") as file:
            file.write(f"Produced data at {time.ctime()}\n")
        time.sleep(5)

if __name__ == "__main__":
    produce()
