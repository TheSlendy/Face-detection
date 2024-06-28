class Person:
    def __init__(self, path, facial_area, sex, age):
        self.detects_number = 1
        self.moods = []
        self.path_to_photo = path
        self.facial_areas = facial_area
        self.sex = sex
        self.age = age

    def __str__(self):
        return (f"Person has been detected {self.detects_number}\n"
                f"Path to photo is {self.path_to_photo}\n"
                f"Facial areas are {self.facial_areas}")
