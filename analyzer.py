from config import BRUTE_FORCE_THRESHOLD

def detect_anomalies(df):
    brute_force_attempts = df[(df['url'].str.contains('/login')) & (df['status'] == '401')]
    counts = brute_force_attempts['ip'].value_counts()
    attackers = counts[counts > BRUTE_FORCE_THRESHOLD].index
    anomalies = df[df['ip'].isin(attackers)]
    return anomalies