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
for p in people:
    print(p)
with open(f"run_data/run_{t.tm_hour}-{t.tm_min}-{t.tm_sec}_{t.tm_mday}-{t.tm_mon}-{t.tm_year}.csv", mode="w") as run:
    for person in people:
        run.write(
            f"{person.path_to_photo}; {person.detects_number}; {person.facial_areas}; "
            f"{person.age}; {person.sex}; {person.moods}\n")
        visits_today += person.detects_number

with open(f"day_data.csv", mode="a") as day:
    day.write(f"{t.tm_mday}-{t.tm_mon}-{t.tm_year}, {end}, {unique_visitors_number}, {visits_today}\n")
