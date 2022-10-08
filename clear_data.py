def cancerData():
    f = open('breast_cancer.txt')
    lines = f.read().splitlines()
    f.close()
    writeFile = open('correct_breast_cancer.txt', 'w')

    for line in lines:
        correctLine = (line.split(',', 1))[1]
        if (line[-1] == '2'):
            correctLine = correctLine[:-1] + '0'
        else:
            correctLine = correctLine[:-1] + '1'
        writeFile.write(str(correctLine + "\n"))
    
def irisData():
    f = open('iris.txt')
    lines = f.read().splitlines()
    f.close()
    writeFile = open('correct_iris.txt', 'w')
    for index in range(int(len(lines) / 2 + 1)):
        correctLine = lines[index]
        correctSecondLine = lines[len(lines) - index - 1]
        writeFile.write(str(correctLine + "\n"))
        writeFile.write(str(correctSecondLine + "\n"))
        
def main():
    cancerData()
    
if __name__ == "__main__":
    main()