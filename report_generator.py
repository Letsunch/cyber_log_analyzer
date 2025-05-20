import pandas as pd

def generate_report(df, anomalies, output_path="outputs/report_summary.txt"):
    with open(output_path, "w") as f:
        f.write("Cybersecurity Log Analysis Report\n")
        f.write("="*40 + "\n\n")
        f.write(f"Total Records: {len(df)}\n")
        f.write(f"Anomalies Detected: {len(anomalies)}\n\n")
        f.write("Top Suspicious IPs:\n")
        f.write(str(anomalies['source'].value_counts().head()))
        f.write("\n\nSample Anomalies:\n")
        f.write(str(anomalies.head()))

    print(f"\n✅ Report saved to {output_path}")
