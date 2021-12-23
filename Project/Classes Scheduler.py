def schedule_classes(classes, times):
    schedule = []

    index = 0
    while index < len(classes):
        schedule_classes = classes[index] + " : " + times[index]
        schedule.append(schedule_classes)
        index += 1

    return schedule

classes = ["UI/UX", "Russian", "France", "Python"]
times = ["11a.m", "8a.m", "4p.m", "1p.m"]

schedule = schedule_classes(classes, times)
print(f"Monday's schedule : {schedule}")
