def findMaxProfit(jobProfitAndDDL, ddl):
	maxProfit = 0
	for item in jobProfitAndDDL:
		if item[1] == ddl:
			maxProfit = max(maxProfit, item[2])
	return maxProfit

def findJobCountMoreProfit(jobProfitAndDDL, ddl, profit):
	count = 0
	for item in jobProfitAndDDL:
		if item[1] == ddl and item[2] > profit:
			count += 1
	return count

def findNextDDL(jobProfitAndDDL, ddl):
	for item in jobProfitAndDDL:
		if item[1] == ddl and item[2] > profit:
			count += 1
	return count

for _ in range(int(input().strip())):
	numOfJob = int(input().strip())
	jobProfitAndDDLs = list(map(int, input().strip().split()))
	jobProfitAndDDL = []
	i = 0
	maxddl = 0
	while i < len(jobProfitAndDDLs)-2:
		jobProfitAndDDL.append([jobProfitAndDDLs[i], jobProfitAndDDLs[i+1], jobProfitAndDDLs[i+2]])
		maxddl = max(maxddl, jobProfitAndDDLs[i+2])
		i += 3
	jobProfitAndDDL.sort(reverse=True, key=lambda x: (x[2], -x[0]))
	maxProfit = 0
	ddl = 1
	while ddl < maxddl:
		maxProfit1 = findMaxProfit(jobProfitAndDDL, ddl)
		count = findJobCountMoreProfit(jobProfitAndDDL, ddl+1, maxProfit1)

