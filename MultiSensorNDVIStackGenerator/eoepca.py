
class Process:
    
    def retrieve(self, format):
        return f"<<data of type {format}>>"

class Collection:

    def coverage(self, extent):
        return Coverage()

class Coverage:

    def process(self, name):
        return Process()

class ParallelTasks:

    def process(self, name):
        return Process()

class Platform:

    def auth(self, id, token):
        return self

    def collection(self, name):
        return Collection()

    def parallel(self, tasks):
        return ParallelTasks()

def platform(name = "local"):
    return Platform()
