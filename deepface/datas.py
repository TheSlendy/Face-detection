import csv
from time import gmtime, time


def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i

    return num


def most_frequent_index(List):
    counter = 0
    num = 0
    for i in range(len(List)):
        curr_frequency = List.count(List[i])
        if curr_frequency > counter:
            counter = curr_frequency
            num = i

    return num


class DataProcess:
    def __init__(self):
        self.start = time()
        self.people = []
        self.length = 0
        t = gmtime(time())
        self.run_filename = f"visits_{t.tm_hour}-{t.tm_min}-{t.tm_sec}_{t.tm_mday}-{t.tm_mon}-{t.tm_year}.csv"
        with open(self.run_filename, "w") as csv_file:
            csv_file.write("id;photo;age;gender;mood;time;visit_time\n")

    def update_run_data(self):
        with open(self.run_filename, "a") as csv_file:
            lines = (len(self.people) - self.length) * -1
            self.length = len(self.people)
            writer = csv.writer(csv_file, delimiter=';')
            for person in self.people[lines:]:
                writer.writerow(person.__to_list__())
        self.update_day_data()

    def update_day_data(self):
        with open("day_data.csv", "w") as csv_file:
            csv_file.write("average_time;average_mood;average_age;"
                           "average_gender;most_frequent_visitor;longest_visitor\n")
            with open(self.run_filename, "r") as visits:
                visits_list = list(csv.reader(visits, delimiter=";"))[1:]
                visits_list = [visit for visit in visits_list if visit]
                average_time = sum([int(visit[5]) for visit in visits_list]) / len(
                    set([visit[0] for visit in visits_list]))
                average_mood = most_frequent([visit[4] for visit in visits_list])
                average_age = sum([int(visit[2]) for visit in visits_list]) / len(visits_list)
                average_gender = most_frequent([visit[3] for visit in visits_list])
                most_frequent_visitor = most_frequent([visit[0] for visit in visits_list])
                longest_visitor = visits_list[most_frequent_index([visit[-2] for visit in visits_list])][0]
                csv_file.write(f"{average_time};{average_mood};{average_age};"
                               f"{average_gender};{most_frequent_visitor};{longest_visitor}\n")
