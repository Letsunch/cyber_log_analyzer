from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from config import OUTPUT_DIR, REPORT_NAME

def generate_report(df, df_anomalies):
    with PdfPages(f"{OUTPUT_DIR}{REPORT_NAME}") as pdf:
        for img in ["traffic_over_time.png", "top_ips.png", "brute_force_ips.png"]:
            try:
                img_path = f"{OUTPUT_DIR}{img}"
                fig = plt.figure()
                plt.imshow(plt.imread(img_path))
                plt.axis('off')
                pdf.savefig(fig)
                plt.close()
            except FileNotFoundError:
                continue