import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent

class CliTests(unittest.TestCase):
    def test_fixture_matches_recorded_output(self):
        run = subprocess.run([sys.executable, str(ROOT/'cli.py'), str(ROOT/'example.json')], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(json.loads(run.stdout), json.loads((ROOT/'example-output.json').read_text()))

    def test_malformed_json(self):
        with tempfile.TemporaryDirectory() as directory:
            p=Path(directory)/'bad.json'; p.write_text('{broken')
            run=subprocess.run([sys.executable,str(ROOT/'cli.py'),str(p)],capture_output=True,text=True)
        self.assertEqual(run.returncode,2)
        self.assertIn('Invalid input:',run.stderr)
        self.assertEqual(run.stdout,'')

    def test_missing_required_fields(self):
        with tempfile.TemporaryDirectory() as directory:
            p=Path(directory)/'bad.json'; p.write_text('{}')
            run=subprocess.run([sys.executable,str(ROOT/'cli.py'),str(p)],capture_output=True,text=True)
        self.assertEqual(run.returncode,2)
        self.assertNotIn('Traceback',run.stderr)

if __name__=='__main__': unittest.main()
