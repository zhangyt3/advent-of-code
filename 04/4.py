import sys
from datetime import datetime
from pprint import pprint


# Read in all events
events = []
for line in sys.stdin:
    tokens = line.split(" ")
    date_time = tokens[:2]
    event = tokens[2:]

    # Convert string to datetime representation
    t = datetime.strptime(" ".join(date_time)[1:-1], '%Y-%m-%d %H:%M')

    # Remove newlines and stuff and add to list
    event = [x.strip() for x in event]
    events.append((t, event))

# Sort events by time
events = sorted(events, key=lambda x: x[0])
pprint(events[:10])

# Process events to see which guard is asleep the most
sleep = dict()
mins = dict()
asleep_at = None
curr_guard = None
for t, event in events:
    case = event[0]
    if case == "Guard":
        # Now processing a new guard
        guard_id = event[1]
        curr_guard = guard_id
    elif case == "falls":
        asleep_at = t
    else:
        # Changing state from asleep to awake
        # See how much time was spent sleeping
        delta = t - asleep_at
        begin = asleep_at.minute
        end = t.minute
        print("Begin, End: {}, {}".format(begin, end))
        
        if sleep.get(guard_id) is None:
            sleep[guard_id] = delta
            m = [0 for _ in range(60)]
            for i in range(begin, end):
                m[i] += 1
            mins[guard_id] = m
        else:
            sleep[guard_id] += delta
            m = mins[guard_id]
            for i in range(begin, end):
                m[i] += 1


# Find the guard with maximum time slept
best_guard = None
best_sleep = datetime(1000, 1, 1)
for guard, sleep_time in sleep.items():
    if best_guard is None or sleep_time > best_sleep:
        best_guard = guard
        best_sleep = sleep_time

print(best_guard)
print(best_sleep)

# Find out which minute this guard was sleeping the most
guard_events = []
append = False
for t, event in events:
    if event[1] == best_guard:
        guard_events.append((t, event))
        append = True
    elif event[1] == "falls" or event[1] == "wakes":
        guard_events.append(t, event)
    else:
        append = False

minute_hist = mins[best_guard]
best_minute = 0
times_asleep = 0
for i in range(1, 60):
    if minute_hist[i] > times_asleep:
        times_asleep = minute_hist[i]
        best_minute = i

print(best_minute * int(best_guard[1:]))

gid = None
min_asleep_most = 0
times_asleep_that_min = 0
for guard_id, min_hist in mins.items():
    for minute, count in enumerate(min_hist):
        if count > times_asleep_that_min:
            times_asleep_that_min = count
            min_asleep_most = minute
            gid = guard_id

print("Guard {} slept {} times on minute {}".format(gid, times_asleep_that_min, min_asleep_most))
print(int(gid[1:]) * min_asleep_most)
