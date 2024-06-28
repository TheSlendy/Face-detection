from deepface import DeepFace
from deepface.modules.streaming import people
from time import time, gmtime

start = time()
DeepFace.stream('database', frame_threshold=5, source=0, enable_face_analysis=False)
end = time() - start
print(end)

t = gmtime(time())

visits_today = 0
unique_visitors_number = len(people)

with open(f"run_data/run_{t.tm_hour}-{t.tm_min}-{t.tm_sec}_{t.tm_mday}-{t.tm_mon}-{t.tm_year}.csv", mode="w") as run:
    for person in people:
        run.write(
            f"{person.path_to_photo}; {person.detects_number}; {person.facial_areas}; "
            f"{person.age}; {person.sex}; {person.moods}\n")
        visits_today += person.detects_number

indexes = []
detects = 0
for person in people:
    if person.detects_number > detects:
        if indexes:
            indexes.clear()
        indexes.append(people.index(person))
        detects = person.detects_number
    elif person.detects_number == detects:
        indexes.append(people.index(person))


constants = [people[i].path_to_photo for i in indexes]
with open(f"day_data.csv", mode="a") as day:
    day.write(f"{t.tm_mday}-{t.tm_mon}-{t.tm_year}; {end}; "
              f"{unique_visitors_number}; {visits_today}; {constants}\n")
