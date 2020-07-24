# Binary search tree
class Node:
    def __init__(self, mid):
        self.left = None
        self.right = None
        self.mid = mid
    
    def insert(self, data):
        if self.mid:
            if data > self.mid:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            elif data < self.mid:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
        else:
            self.mid = data
    
    def find(self, val):
        if val < self.mid:
            if self.left is None:
                print(val,"Not found")
            else:
                self.left.find(val)
        elif val > self.mid:
            if self.right is None:
                print(val,"Not found")
            else:
                self.right.find(val)
        else:
            print(val,"Found")
    
    def display(self):
        if self.left is not None:
            _theleft = self.left.display()
        print(self.mid)
        if self.right:
            _theright = self.right.display()

if __name__ == "__main__":
    root = Node(5)
    root.insert(6)
    root.insert(7)
    root.insert(8)
    root.insert(3)
    root.insert(1)
    root.display()
    root.find(8)
    root.find(10)