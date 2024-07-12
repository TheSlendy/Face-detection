from random import randint


class Person:
    def __init__(self, ID, path, mood, sex, age, visit_time):
        self.id = ID
        self.mood = mood
        self.path_to_photo = path
        self.sex = sex
        self.age = age
        self.seconds = randint(6, 7)
        self.visit_time = visit_time

    def __to_dict__(self):
        return {"id": self.id, "photo": self.path_to_photo,
                "age": self.age, "gender": self.sex,
                "mood": self.mood, "time": self.seconds, "visits": self.visit_time}

    def __to_list__(self):
        return [self.id, self.path_to_photo,
                self.age, self.sex, self.mood, self.seconds, self.visit_time]
