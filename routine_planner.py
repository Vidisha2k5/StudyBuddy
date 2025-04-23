# routine_planner.py

import datetime

def generate_routine(days_left, topics):
    routine = {}
    for i in range(days_left):
        date = (datetime.date.today() + datetime.timedelta(days=i)).strftime("%d %b")
        topic = topics[i % len(topics)]
        routine[date] = topic
    return routine
