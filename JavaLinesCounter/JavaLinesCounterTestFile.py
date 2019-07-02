import unittest
from JavaLinesCounter import *


class TestJavaLinesCounter(unittest.TestCase):
    def setUp(self) -> None:
        testFile = './test'
        self.linesCounterForTest = JavaLinesCounter(testFile)
        self.assertEqual('./test', self.linesCounterForTest.fileName)
        self.assertEqual('./test', self.linesCounterForTest.targetFile.name)

    def testCountLines(self):
        self.linesCounterForTest.countLines()
        self.assertEqual(11, self.linesCounterForTest.lines)

    def testIsCodeLine(self):
        self.assertTrue(self.linesCounterForTest.isCodeLine('int i = 0'))
        self.assertFalse(self.linesCounterForTest.isCodeLine('//This is a comment line.'))
        self.assertFalse(self.linesCounterForTest.isCodeLine('/*This is a comment block.*/'))
        self.assertFalse(self.linesCounterForTest.isCodeLine(''))

    def testIsCommentLine(self):
        self.assertTrue(self.linesCounterForTest.isCommentLine('//This is a comment line.'))
        self.assertTrue(self.linesCounterForTest.isCommentLine('/*This is a comment block.*/'))
        self.assertFalse(self.linesCounterForTest.isCommentLine('int i = 0'))
        self.assertFalse(self.linesCounterForTest.isCommentLine(''))

    def testIsCommentBlock(self):
        self.assertTrue(self.linesCounterForTest.isCommentBlock('/*Block begins...'))
        self.assertTrue(self.linesCounterForTest.isCommentBlock('This is a line of comment block.'))
        self.assertTrue(self.linesCounterForTest.isCommentBlock('Block ends.*/'))
        self.assertFalse(self.linesCounterForTest.isCommentBlock(''))
        self.assertFalse(self.linesCounterForTest.isCommentBlock('//This is not a comment block.'))
        self.assertFalse(self.linesCounterForTest.isCommentBlock('int i = 0'))

    def testIsBeginAndEndOfCommentBlock(self):
        self.linesCounterForTest.isBeginOfCommentBlock('/*This is the beginning of a comment block.')
        self.assertTrue(self.linesCounterForTest.readingCommentBlock)
        self.linesCounterForTest.isBeginOfCommentBlock('This is not the beginning of a comment block.')
        self.assertTrue(self.linesCounterForTest.readingCommentBlock)
        self.assertFalse(self.linesCounterForTest.isEndOfCommentBlock('This is not the end of a comment block.'))
        self.assertTrue(self.linesCounterForTest.isEndOfCommentBlock('This is the end of a comment block.*/'))
        self.linesCounterForTest.isBeginOfCommentBlock('')
        self.assertFalse(self.linesCounterForTest.readingCommentBlock)
        self.assertFalse(self.linesCounterForTest.isEndOfCommentBlock(''))
        self.linesCounterForTest.isBeginOfCommentBlock('int i = 0')
        self.assertFalse(self.linesCounterForTest.readingCommentBlock)
        self.assertFalse(self.linesCounterForTest.isEndOfCommentBlock('int i = 0'))


if __name__ == '__main__':
    unittest.main()
