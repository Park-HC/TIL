class Vertice():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Rectangle():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def area(self):
        return abs(self.p1.x - self.p2.x) * abs(self.p1.y - self.p2.y)
    
    def overlap(self, other):
        width_overlap = 0
        length_overlap = 0
        
        if other.p1.x <= self.p1.x <= other.p2.x and other.p1.x <= self.p2.x <= other.p2.x:
            width_overlap = self.p2.x - self.p1.x
        elif self.p1.x <= other.p1.x and other.p2.x <= self.p2.x:
            width_overlap = other.p2.x - other.p1.x
        elif other.p1.x <= self.p1.x <= other.p2.x:
            width_overlap = other.p2.x - self.p1.x
        elif other.p1.x <= self.p2.x <= other.p2.x:
            width_overlap = self.p2.x - other.p1.x
        else:
            return 0
        
        if other.p1.y <= self.p1.y <= other.p2.y and other.p1.y <= self.p2.y <= other.p2.y:
            length_overlap = self.p2.y - self.p1.y
        elif self.p1.y <= other.p1.y and other.p2.y <= self.p2.y:
            length_overlap = other.p2.y - other.p1.y
        elif other.p1.y <= self.p1.y <= other.p2.y:
            length_overlap = other.p2.y - self.p1.y
        elif other.p1.y <= self.p2.y <= other.p2.y:
            length_overlap = self.p2.y - other.p1.y
        else:
            return 0
        
        return width_overlap * length_overlap

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
            area_of_overlap += red.overlap(blue)
    
    print(f'#{i} {area_of_overlap}')
            
