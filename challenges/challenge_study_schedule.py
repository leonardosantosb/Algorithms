def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None

    count = 0
    for e, s in permanence_period:
        if not (isinstance(e, int) and isinstance(s, int) and e <= s):
            return None
        if e <= target_time <= s:
            count += 1

    return count

    raise NotImplementedError
