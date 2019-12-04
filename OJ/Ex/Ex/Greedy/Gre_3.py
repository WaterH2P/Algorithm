# Given a set of n jobs where each job i has a deadline and profit associated to it. 
# Each job takes 1 unit of time to complete and only one job can be scheduled at a time. 
# We earn the profit if and only if the job is completed by its deadline. 
# The task is to find the maximum profit and the number of jobs done.

# Input
# The first line of input contains an integer T denoting the number of test cases. 
# Each test case consist of an integer N denoting the number of jobs and 
# the next line consist of Job id, Deadline and the Profit associated to that Job.

# Sample
'''
1
5
1 2 100 2 1 19 3 2 27 4 1 25 5 1 15
'''
# 2 127

for _ in range(int(input().strip())):
    n = int(input().strip())
    datas = list(map(int, input().strip().split()))
    jobs = []
    i = 0
    while i < len(datas):
        jobs.append([datas[i+1], datas[i+2]])
        i += 3
    jobs.sort(key=lambda x: (x[0], -x[1]))
    ddl = 1
    works = [[*jobs[0]]]
    for job in jobs:
        # 如果 job.ddl == ddl，那必须替换一个才能执行该 job。
        if job[0] == ddl:
            for i in range(len(works)):
                work = works[i]
                if job[1] > work[1]:
                    works[i] = [*job]
                    break
        # 如果 job.ddl > ddl，那该 job 可以直接执行。
        elif job[0] > ddl:
            works.append([*job])
            ddl += 1
        # 按照 profit 排序
        works.sort(key=lambda x: x[1])
    profit = 0
    for work in works:
        profit += work[1]
    print(str(len(works)) + ' ' + str(profit))