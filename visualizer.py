# visualizer.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from config import OUTPUT_DIR

sns.set(style="whitegrid")

def generate_visuals(df, df_anomalies):
    df['datetime'] = pd.to_datetime(df['datetime'])
    df.set_index('datetime', inplace=True)

    # Traffic over time
    plt.figure(figsize=(10, 4))
    df.resample('1H').size().plot()
    plt.title("Traffic Over Time")
    plt.ylabel("Requests")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}traffic_over_time.png")
    plt.close()

    # Top IPs
    plt.figure(figsize=(10, 4))
    df['ip'].value_counts().head(10).plot(kind='bar')
    plt.title("Top IPs")
    plt.ylabel("Request Count")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}top_ips.png")
    plt.close()

    # Brute Force IPs
    if not df_anomalies.empty:
        plt.figure(figsize=(10, 4))
        df_anomalies['ip'].value_counts().plot(kind='bar', color='red')
        plt.title("Detected Brute Force IPs")
        plt.ylabel("Attempt Count")
        plt.tight_layout()
        plt.savefig(f"{OUTPUT_DIR}brute_force_ips.png")
        plt.close()
