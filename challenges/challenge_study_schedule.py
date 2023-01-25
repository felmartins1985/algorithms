def study_schedule(permanence_period, target_time):
    counter = 0
    if target_time is None:
        return None
    for student in permanence_period:
        if type(student[0]) != int or type(student[1]) != int:
            return None
        if student[0] <= target_time and student[1] >= target_time:
            counter += 1

    return counter
