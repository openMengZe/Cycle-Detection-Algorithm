import numpy as np # This provides more functionalities to 'array'

# Create a new data structure
class Node():
    def __init__(self, state, pos, action):
        self.state = state
        self.pos = pos
        self.action = action


class QueneFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def is_empty(self):
        if len(self.frontier) == 0:
            return True
        else:
            return False
    
    def remove(self):
        if(self.is_empty()):
            return 
        else:
            return self.frontier.pop(0)


# Pretty much useless for this problem unless the array is huge
class StackFrontier(QueneFrontier):
    def remove(self):
        if(self.is_empty()):
            return False
        else:
            return self.frontier.pop(-1)


# Interesting stuffs in here
class Detector():
    def __init__(self, graph):
        self.frontier = QueneFrontier()
        self.explored_action = set()
        self.graph = graph
    

    def check_cycle(self):
        x = 0
        y = 0

        node = Node(self.graph[y][x], (y, x), None)
        self.frontier.add(node)

        while True:
            if self.frontier.is_empty():
                return False # meaning no cycle detected
            else:
                node = self.frontier.remove()

                if node.state == 0:
                    try:
                        x += 1
                        node_next = Node(self.graph[y][x], (y, x), None)
                    except IndexError:
                        try:
                            self.graph = np.delete(self.graph, y, 0)
                            self.graph = np.delete(self.graph, y, 1)
                        except:
                            return False
                       
                        y = 0
                        x = 0          

                    self.frontier.add(node_next)
                
                else:
                    action = (y, x)
                    y = x
                    x = 0

                    if action in self.explored_action:
                        print("Cycle: \n")
                        for i in self.explored_action:
                            print(i)
                        print()

                        return True

                    self.explored_action.add(node.pos)

                    node_next = Node(self.graph[y][x], (y, x), action)

                    self.frontier.add(node_next)
                 


# For testing only
if __namw__ == '__main__':
    graph = np.array([
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0]
    ])

    detector = Detector(graph)

    cycle = detector.check_cycle()

    if not cycle:
        print("No cycle was found!")
