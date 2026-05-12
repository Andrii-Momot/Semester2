from abc import ABC, abstractmethod

class FileReader():
    def __init__(self, filename):
        self.filename = filename
        self.subscribers=[]
    def read(self):
        with open("input.txt") as f:
            for l in f:
                for s in self.subscribers:
                    s.onReceive(l)
                #print(l.rstrip())
    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

class Observer(ABC):
    @abstractmethod
    def onReceive(self, line):
        pass

class FilePrint(Observer):
    def onReceive(self, line):
        print(line.rstrip())

class WordCounter(Observer):
    def __init__(self):
        self.counter = 0
    def onReceive(self, line):
        words = line.split()
        self.counter += len(words)
    def __str__(self):
        return str(self.counter)

if __name__ == "__main__":
    reader = FileReader("input.txt")
    fp=FilePrint()
    fc=WordCounter()
    reader.subscribe(fp)
    reader.subscribe(fc)
    reader.read()
    print(fc)

