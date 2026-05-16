from threading import Semaphore, Lock

class DiningPhilosophers:
    def __init__(self):
        self.forks = [Lock() for _ in range(5)]
        self.eat_limit = Semaphore(4)

    def wantsToEat(self, philosopher,
                   pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork):
        left = philosopher
        right = (philosopher + 1) % 5
        
        self.eat_limit.acquire()
        
        self.forks[left].acquire()
        self.forks[right].acquire()
        
        pickLeftFork()
        pickRightFork()
        eat()
        putRightFork()
        putLeftFork()
        
        self.forks[right].release()
        self.forks[left].release()
        
        self.eat_limit.release()