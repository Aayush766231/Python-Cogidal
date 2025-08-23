import random
import time

def randomDate(startDate, endDate):
    print(f"Printing a random date between {startDate} and {endDate}")
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print(randomDate("5/20/2023", "8/23/2025"))