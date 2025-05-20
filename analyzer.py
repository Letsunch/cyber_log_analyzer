from config import BRUTE_FORCE_THRESHOLD

def detect_anomalies(df):
    if 'Label' not in df.columns or 'source' not in df.columns:
        print("Required columns are missing.")
        return df.head(0)  # Empty DataFrame if structure is wrong

    # Define attack keywords to filter
    attack_keywords = ['Brute', 'DDoS', 'XSS', 'Infiltration', 'Botnet', 'SQL', 'Heartbleed', 'PortScan']

    # Combine into one regex pattern
    attack_pattern = '|'.join(attack_keywords)

    # Filter suspected attack rows
    suspected_attacks = df[df['Label'].str.contains(attack_pattern, case=False, na=False)]

    # Count attacks per source IP
    counts = suspected_attacks['source'].value_counts()

    # Flag IPs with too many suspicious actions
    attackers = counts[counts > BRUTE_FORCE_THRESHOLD].index

    # Return full records of the attackers
    anomalies = df[df['source'].isin(attackers)]

    return anomalies
