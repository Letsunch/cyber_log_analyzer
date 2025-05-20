import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_requests_over_time(df):
    if 'startDateTime' not in df.columns:
        print("Timestamp column 'startDateTime' missing.")
        return

    df['Minute'] = df['startDateTime'].dt.floor('min')
    flow_counts = df.groupby('Minute').size()

    plt.figure(figsize=(12, 6))
    sns.lineplot(x=flow_counts.index, y=flow_counts.values)
    plt.title("Flows Over Time")
    plt.xlabel("Time (Minute)")
    plt.ylabel("Flow Count")
    os.makedirs("outputs", exist_ok=True)
    plt.savefig("outputs/flows_over_time.png")
    plt.close()
