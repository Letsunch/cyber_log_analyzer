import pandas as pd
import re
from datetime import datetime

def parse_logs(filepath):
    pattern = re.compile(r'(?P<ip>\S+) - - \[(?P<datetime>.*?)\] "(?P<method>\S+) (?P<url>\S+) (?P<protocol>\S+)" (?P<status>\d{3}) (?P<size>\d+)')
    rows = []
    with open(filepath, 'r') as f:
        for line in f:
            match = pattern.match(line)
            if match:
                row = match.groupdict()
                row['datetime'] = datetime.strptime(row['datetime'], "%d/%b/%Y:%H:%M:%S %z")
                rows.append(row)
    return pd.DataFrame(rows)