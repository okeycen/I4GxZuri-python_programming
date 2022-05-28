class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age , track, score):
        self.name= str(name)
        self.age=int(age)
        self.track=list(track)
        self.myScore=float(score)
    
    def change_name(obj,new_name):
        obj.change_name=new_name
        return new_name
    
    def change_age(obj,new_age):
        obj.change_age=new_age
        return new_age

    def add_tracks(obj,added_track):
        obj.add_tracks=added_track
        return added_track

    def get_score(obj):
        obj.get_score=obj.myScore
        return  obj.myScore

    def display(self):
        print("Name: ",self.change_name,",", "Age: ",self.change_age,",", "Track: ", self.add_tracks,",", "Score: ",self.get_score)

Bob = Student(name="Bob", age=26, track=["BE,FE"], score=89)

Bob.change_name("John")
Bob.change_age(45)
Bob.add_tracks("UI/UX")
Bob.get_score()

Bob.display()
