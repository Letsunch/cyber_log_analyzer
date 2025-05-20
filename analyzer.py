from config import BRUTE_FORCE_THRESHOLD

def detect_brute_force(df):
    brute_force_attempts = df[
        (df['Label'].str.contains("Brute Force", na=False)) |
        ((df['destinationPort'] == 22) | (df['destinationPort'] == 23))  # SSH/Telnet
    ]
    src_counts = brute_force_attempts['source'].value_counts()
    top_attackers = src_counts[src_counts > BRUTE_FORCE_THRESHOLD].index
    anomalies = brute_force_attempts[brute_force_attempts['source'].isin(top_attackers)]
    return anomalies
