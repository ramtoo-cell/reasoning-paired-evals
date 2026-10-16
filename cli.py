"""Paired Evaluation Lab — analyze a local JSON file."""

import argparse
import json
import sys
from engine import analyze

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', help='Path to a JSON input file')
    args=parser.parse_args()
    try:
        with open(args.input,encoding='utf-8') as f: data=json.load(f)
        result=analyze(data)
        print(json.dumps(result,indent=2,sort_keys=True,allow_nan=False))
    except (ValueError,KeyError,TypeError,OSError,RecursionError) as exc:
        print('Invalid input: '+str(exc),file=sys.stderr)
        return 2
    return 0

if __name__=='__main__':
    raise SystemExit(main())
