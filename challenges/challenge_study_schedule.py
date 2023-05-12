def study_schedule(permanence_period, target_time):
    try:
        count = 0
        for login, logout in permanence_period:
            if login <= target_time <= logout:
                count += 1
        return count
    except TypeError:
        return None
