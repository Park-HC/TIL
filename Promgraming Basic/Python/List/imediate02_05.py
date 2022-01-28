class Vertice():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Rectangle():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __str__(self):
        return print(f'p1 is ({self.p1.x}, {self.p1.y}, p2 is ({self.p2.x}, {self.p2.y})')
    
    def area(self):
        return abs(self.p1.x - self.p2.x) * abs(self.p1.y - self.p2.y)
    
    def inner_vertice(self, other):
        v1 = v2 = 0
        
        if other.p1.x < self.p1.x < other.p2.x or other.p2.x < self.p1.x < other.p1.x:
            v1 = self.p1.x
        elif other.p1.x < self.p2.x < other.p2.x or other.p2.x < self.p2.x < other.p1.x:
            v1 = self.p2.x
        else:
            return
        
        if other.p1.y < self.p1.y < other.p2.y or other.p2.y < self.p1.y < other.p1.y:
            v2 = self.p1.y
        elif other.p1.y < self.p2.y < other.p2.y or other.p2.y < self.p2.y < other.p1.y:
            v2 = self.p2.y
        else:
            return
        
        return Vertice(v1, v2)

    def overlap(self, other):
        n1 = self.inner_vertice(other)
        n2 = other.inner_vertice(self)

        if not(n1 and n2):
            return 0
        else:
            overlap_rectangle = Rectangle(n1, n2)
            return overlap_rectangle.area()

def string_to_numbers(words):
    numbers = list(map(int, words.split(' ')))
    return numbers

num_of_test = int(input())

for i in range(1, num_of_test+1):
    num_of_rectangle = int(input())

    reds = []
    blues = []
    area_of_overlap = 0

    for _ in range(num_of_rectangle):
        numbers = string_to_numbers(input())
        push_Rectangle = Rectangle(Vertice(numbers[0],numbers[1]),Vertice(numbers[2]+1,numbers[3]+1))

        reds.append(push_Rectangle) if numbers[-1] == 1 else blues.append(push_Rectangle)

    for red in reds:
        for blue in blues:
            print(red, blue)
            area_of_overlap += red.overlap(blue)
            print(area_of_overlap)
    
    print(f'#{i} {area_of_overlap}')
            
