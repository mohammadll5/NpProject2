# consumer.py
import time

def consume():
    while True:
        with open("producerOut.txt", "r") as file:
            lines = file.readlines()
            if lines:
                print(lines[-1].strip())
        time.sleep(5)

if __name__ == "__main__":
    consume()
