from log_parser import parse_apache_logs
from analyzer import detect_brute_force
from visualizer import plot_requests_over_time
from report_generator import generate_report

if __name__ == "__main__":
    df = parse_apache_logs("sample_logs/access.log")
    anomalies = detect_brute_force(df)
    plot_requests_over_time(df)
    generate_report(df, anomalies)
