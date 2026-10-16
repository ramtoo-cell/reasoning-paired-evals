"""Paired Evaluation Lab. See METHODS.md for assumptions."""
import math
import random

def analyze(data):
    rows = data['rows']
    if not rows or len({r['id'] for r in rows}) != len(rows):
        raise ValueError('Need nonempty rows with unique task IDs')
    for r in rows:
        if type(r['baseline']) is not bool or type(r['candidate']) is not bool:
            raise ValueError('Outcomes must be JSON booleans')
    draws = data.get('resamples', 2000)
    if type(draws) is not int or not 100 <= draws <= 100000:
        raise ValueError('resamples must be an integer between 100 and 100000')
    diffs = [int(r['candidate']) - int(r['baseline']) for r in rows]
    n = len(rows)
    wins, losses = diffs.count(1), diffs.count(-1)
    m = wins + losses
    p = min(1.0, 2 * sum(math.comb(m, k) for k in range(min(wins, losses)+1)) / 2**m) if m else 1.0
    rng = random.Random(data.get('seed', 17))
    boot = sorted(sum(rng.choices(diffs, k=n))/n for _ in range(draws))
    return {'n': n, 'baseline_accuracy': sum(r['baseline'] for r in rows)/n,
            'candidate_accuracy': sum(r['candidate'] for r in rows)/n,
            'paired_delta': sum(diffs)/n, 'ci95_percentile': [boot[int(.025*draws)], boot[min(draws-1, int(.975*draws))]],
            'wins': wins, 'losses': losses, 'exact_discordance_p': p}
