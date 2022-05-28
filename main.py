class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, tracks, age, score):
        self.name = name
        self.age = age
        self.score = score
        self.tracks = tracks
    
    def change_name(self,new_name):
        print(new_name)
    def change_age(self, new_age):
        if type(new_age)==int:
            print(new_age)
        else:
            print('Invalid age (age has to be an integer!).')
    def add_track(self,new_track):
        self.tracks.append(new_track)
        print(self.tracks)
    
    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
