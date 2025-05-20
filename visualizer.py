import matplotlib.pyplot as plt
import pandas as pd

def plot_requests_over_time(df):
    if 'startDateTime' not in df.columns:
        return

    df['startDateTime'] = pd.to_datetime(df['startDateTime'], errors='coerce')
    df = df.dropna(subset=['startDateTime'])

    df['hour'] = df['startDateTime'].dt.hour
    hourly_counts = df.groupby('hour').size()

    plt.figure(figsize=(10, 6))
    hourly_counts.plot(kind='bar', color='skyblue')
    plt.title("Network Requests Per Hour")
    plt.xlabel("Hour of Day")
    plt.ylabel("Number of Requests")
    plt.tight_layout()
    plt.savefig("outputs/requests_over_time.png")
    plt.close()
