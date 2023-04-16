#!/usr/bin/env python3
"""
    Reads standard input line by line and computes metrics.
"""
import sys
from collections import defaultdict


def print_metrics(metrics):
    """Prints the computed metrics."""
    print(f"File size: {metrics['file_size']}")
    for code, count in sorted(metrics['codes'].items()):
        if count > 0:
            print(f"{code}: {count}")


def compute_metrics(lines):
    """Computes metrics for a list of lines."""
    metrics = defaultdict(int)
    for line in lines:
        parts = line.split()
        if len(parts) >= 2:
            metrics['file_size'] += int(parts[-1])
            code = parts[-2]
            if code in metrics['codes']:
                metrics['codes'][code] += 1
    return metrics


if __name__ == '__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())
        if len(lines) == 10:
            metrics = compute_metrics(lines)
            print_metrics(metrics)
            lines = []
    if lines:
        metrics = compute_metrics(lines)
        print_metrics(metrics)
