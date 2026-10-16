import copy
import json
import unittest
from pathlib import Path
from engine import analyze
EXAMPLE=json.loads(Path(__file__).with_name("example.json").read_text())

class Tests(unittest.TestCase):
    def test_identical(self):
        r = analyze({'rows':[{'id':'a','baseline':True,'candidate':True}]})
        self.assertEqual(r['paired_delta'], 0)
        self.assertEqual(r['ci95_percentile'], [0,0])
        self.assertEqual(r['exact_discordance_p'], 1)
    def test_exact(self):
        r=analyze({'rows':[{'id':str(i),'baseline':False,'candidate':True} for i in range(5)]})
        self.assertEqual(r['exact_discordance_p'], .0625)
        self.assertEqual(r['paired_delta'],1)
    def test_duplicate(self):
        with self.assertRaises(ValueError): analyze({'rows':[{'id':'a'},{'id':'a'}]})
    def test_seed(self):
        self.assertEqual(analyze(EXAMPLE), analyze(EXAMPLE))

if __name__=="__main__": unittest.main()
