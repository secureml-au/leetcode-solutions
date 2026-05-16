from threading import Semaphore, Lock

class H2O:
    def __init__(self):
        self.h = Semaphore(2)
        self.o = Semaphore(1)
        self.lock = Lock()
        self.h_count = 0

    def hydrogen(self, releaseHydrogen):
        self.h.acquire()
        self.lock.acquire()
        self.h_count += 1
        if self.h_count == 2:
            self.h_count = 0
            self.o.release()
        self.lock.release()
        releaseHydrogen()

    def oxygen(self, releaseOxygen):
        self.o.acquire()
        releaseOxygen()
        self.h.release()
        self.h.release()