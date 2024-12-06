
# Part 1
num_safe_reports = 0


def check_diff(x, y, pattern) -> bool:

    follows_pattern = (y-x > 0) == pattern
    abs_dif = abs(x-y)
    return (abs_dif >= 1 and abs_dif <= 3) and follows_pattern


with open('inp.txt', 'r') as f:
    for line in f:
        report = list(map(int, line.split()))

        is_inc = False
        safe_report = True

        if report[1] - report[0] > 0:
            is_inc = True

        for i in range(len(report)-1):
            cur = report[i]
            nex = report[i+1]
            if not check_diff(cur, nex, is_inc):
                safe_report = False
                break

        if safe_report:
            num_safe_reports += 1


print(num_safe_reports)

# Part 2


def check_diff2(seq) -> bool:
    return all((int(seq[i+1] - seq[i]) >= 1 and int(seq[i+1] - seq[i]) <= 3) for i in range(len(seq)-1)) or all((int(seq[i] - seq[i+1]) >= 1 and int(seq[i] - seq[i+1]) <= 3) for i in range(len(seq)-1))


num_safe_reports = 0

with open('inp.txt', 'r') as f:
    for line in f:
        report = list(map(int, line.split()))

        if check_diff2(report):
            num_safe_reports += 1
        else:
            for i in range(len(report)-1):
                if check_diff2(report[:i] + report[i+1:]) or check_diff2(report[:i+1] + report[i+2:]):
                    num_safe_reports += 1
                    break

print(num_safe_reports)
