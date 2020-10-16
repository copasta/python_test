DEBUG = False
dir = './inputs/'
f_name = 'input.txt' # [sample1, sample2, input]
path = dir + f_name

setting = {}
problem = None
flag = True

with open(path) as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n', '')
        line = line.split(':')
        if len(line) == 2:
            setting[int(line[0])] = line[1]
        else:
            problem = int(line[0])
            answer = int(line[0])

setting = sorted(setting.items(), key=lambda x:x[0])

for k, v in setting:
    if problem % k == 0:
        if flag:
            answer = ''
            flag = False
        answer += v

if DEBUG:
    print(setting)
    print(problem)

print(answer)