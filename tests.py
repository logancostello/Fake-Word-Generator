import unittest
from fakewordgenerator import create_empty_edge_list,load_words, \
    count_frequencies


class TestCountFrequencies(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.english_words = load_words()
        cls.graph = create_empty_edge_list()
        count_frequencies(cls.english_words, cls.graph)

    @classmethod
    def tearDownClass(cls):
        del cls.english_words
        del cls.graph

    def testPK(self): self.assertEqual(self.graph['p']['k'], 71)
    def testQU(self): self.assertEqual(self.graph['q']['u'], 5763)
    def testYY(self): self.assertEqual(self.graph['y']['y'], 9)
    def testFL(self): self.assertEqual(self.graph['f']['l'], 4104)
    def testEE(self): self.assertEqual(self.graph['e']['e'], 7312)
    def testKL(self): self.assertEqual(self.graph['k']['l'], 1194)
    def testLK(self): self.assertEqual(self.graph['l']['k'], 901)
    def testZQ(self): self.assertEqual(self.graph['z']['q'], 4)
    def testAA(self): self.assertEqual(self.graph['a']['a'], 255)
    def testII(self): self.assertEqual(self.graph['i']['i'], 579)
    def testGG(self): self.assertEqual(self.graph['g']['g'], 2113)
    def testStart(self): self.assertEqual(self.graph['a']['#'], 0)
    def testEnd(self): self.assertEqual(self.graph['.']['a'], 0)




