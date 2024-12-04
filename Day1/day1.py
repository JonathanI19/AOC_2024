def main():
    list1, list2 = loadPrompt()
    list1.sort()
    list2.sort()
    
    sum = computeDiff(list1, list2)
    
    print(f"sum = {sum}")
    
    simScore = calcSimScore(list1, list2)

    print(f"simScore = {simScore}")

def loadPrompt():
    f = open("prompts/q1.txt", "r")
    list1 = []
    list2 = []
    for line in f:
        str = line.split()
        list1.append(str[0])
        list2.append(str[1])
    return list1,list2

def computeDiff(list1, list2):
    sum = 0
    for i in range(len(list1)):
        sum+=abs(int(list1[i])-int(list2[i]))
    return sum

def calcSimScore(list1, list2):
    simScore = 0
    for item in list1:
        num = list2.count(item)
        simScore+=(int(item)*num)
    return simScore

if __name__ == "__main__":
    main()