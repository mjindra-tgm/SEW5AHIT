import threading
import random, time

class Producer(threading.Thread):
    def __init__ (self):
        threading.Thread.__init__(self)
        self.x = random.randint(0,20)
        self.y = 0
        self.xvel=random.randint(-2,2)
        self.yvel= random.randint(1,3)

    def run(self):
        while True:
            self.x += self.xvel
            if self.x<0:
                self.x=19
            if self.x>19:
                self.x=0
            self.y += self.yvel
            if self.y > 10:
                with Consumer.lock:
                    Consumer.counter += 1
                break
            time.sleep (0.5)

class Consumer(threading.Thread):
    lock = threading.Lock()
    counter = 0

    def __init__ (self, erree):
        threading .Thread.__init__ (self)
        self.erree = erree


    def run(self):
        while True:
            print("+----------------------------------------------------------------------------------------------------+")
            for y in range(10):
                txt=""
                for x in range(20):
                    for i in self.erree:
                        if x==i.x and y==i.y:
                            txt += "*"
                        else:
                            txt += " "
                print("|"+txt+"|")
            print("+----------------------------------------------------------------------------------------------------+")
            with Consumer.lock:
                print("Anzahl der Schneeflocken, welche den Boden erreicht haben: "+ str(Consumer.counter))
                if Consumer.counter==len(self.erree):
                    for p in erree:
                        p.join()
                    return
            time.sleep(0.5)


if __name__ == '__main__':
    erree = []
    anzThreads=5

    for i in range(anzThreads):
        p = Producer()
        erree.append(p)

    for i in erree:
        i.start()
        time.sleep(0.1)


    c1 = Consumer(erree)
    c1.start ()

    for p in erree:
        p.join()
    c1.join()




