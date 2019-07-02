class JavaLinesCounter:

    def __init__(self, targetFileName):
        self.fileName = targetFileName
        self.targetFile = open(self.fileName, 'r')
        self.lines = 0
        self.__readingCommentBlock = False

    def printResult(self):
        self.countLines()
        print(self.lines)

    def countLines(self):
        for currentLine in self.targetFile.readlines():
            currentLine = currentLine.strip()
            if self.isCodeLine(currentLine):
                self.lines += 1

    def isCodeLine(self, currentLine):
        if len(currentLine) == 0:
            return False
        if self.isCommentLine(currentLine):
            return False
        return True

    def isCommentLine(self, currentLine):
        if currentLine.startswith('//'):
            return True
        return self.isCommentBlock(currentLine)

    def isCommentBlock(self, currentLine):
        if self.isBeginOfCommentBlock(currentLine):
            self.__readingCommentBlock = True
        if self.isEndOfCommentBlock(currentLine):
            self.__readingCommentBlock = False
        return self.__readingCommentBlock

    def isBeginOfCommentBlock(self, currentLine):
        if currentLine.startswith('/*'):
            return True
        return False

    def isEndOfCommentBlock(self, currentLine):
        if currentLine.endswith('*/'):
            self.lines -= 1
            return True
        return False


if __name__ == '__main__':
    obj = JavaLinesCounter('./test')
    obj.printResult()
