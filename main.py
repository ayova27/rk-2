def task1():
    discipline = {
        "math": 4,
        'Chemistry': 3,
        'English': 4
    }
    score = {
        "Math": 85,
        'Chemistry': 73,
        'English': 91
    }
    gpas = {
        95: 4.3,
        90: 4.0,
        85: 3.71,
        80: 3.3,
        75: 3.0,
        70: 2.7,
        65: 2.3,
        60: 2.0,
        55: 1.7,
        50: 1.3,
        45: 1.0,
        40: 0.7
    }
    result = 0
    result2 = 0
    total = 1

    lists = []
    for i, k in discipline.items():
        for t, m in score.items():
            for z, y in gpas.items():
                if m == y and i == t:
                    result = result + y * k
                    result2 += m

    # total = result / result2

    print(total)


task1()

def task2():
    pass