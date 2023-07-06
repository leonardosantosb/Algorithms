def study_schedule(permanence_period, target_time):
    if target_time == None:
        return None

    count = 0
    for e, s in permanence_period:
        if not (isinstance(target_time, int) and isinstance(e, int) and isinstance(s, int)):
            return None
        if e <= target_time <= s:
            count += 1

    return count




    raise NotImplementedError
