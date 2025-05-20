from log_parser import parse_logs
from analyzer import detect_anomalies
from visualizer import plot_requests_over_time
from report_generator import generate_report

if __name__ == "__main__":
    df = parse_logs("sample_logs/TestbedMonJun14Flows.csv")
    anomalies = detect_anomalies(df)
    plot_requests_over_time(df)

    print("\n🚨 Top Suspicious IPs Detected:")
    print(anomalies['source'].value_counts().head())

    print("\n🕵️ Sample Anomalous Records:")
    print(anomalies.head())

    generate_report(df, anomalies)
