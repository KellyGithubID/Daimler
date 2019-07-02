import JavaLinesCounter

if __name__ == '__main__':
    testCounter = JavaLinesCounter.JavaLinesCounter('./test')
    assert testCounter.fileName == './test', 'fileName should be "./test"!'
    assert testCounter.targetFile.name == './test', 'targetFile should be "./test"!'
    assert testCounter.lines == 0, 'current number of lines should be 0!'

