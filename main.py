from utils.processing import load_data, clean_data, process_data
from utils.analysis import analyze_data, generate_report, plot_graph
import os
import time

def show_menu():
    print("\n" + "=" * 50)
    print("         MAIN MENU")
    print("=" * 50)
    print("  1. Load and Process Data")
    print("  2. View Analysis Report")
    print("  3. Generate Graphs")
    print("  4. Export Report to CSV")
    print("  5. Auto Process New Data Files")
    print("  6. Exit")
    print("=" * 50)
    return input("  Enter your choice (1-6): ")

def auto_process():
    print("\n" + "=" * 50)
    print("STEP 7 - AUTOMATION")
    print("=" * 50)
    files = [f for f in os.listdir("data") if f.endswith(".csv")]
    print(f"Found {len(files)} file(s): {files}")
    import pandas as pd
    all_data = []
    for f in files:
        df = load_data(f"data/{f}")
        df = clean_data(df)
        df = process_data(df)
        all_data.append(df)
    final = pd.concat(all_data, ignore_index=True)
    final.to_csv("reports/auto_report.csv", index=False)
    print("Auto report saved to reports/auto_report.csv")
    return final

def main():
    print("\n" + "=" * 50)
    print("  AUTOMATED DATA PROCESSING & ANALYTICS SYSTEM")
    print("=" * 50)
    df = None
    while True:
        choice = show_menu()
        if choice == "1":
            df = load_data("data/sales.csv")
            df = clean_data(df)
            df = process_data(df)
            input("\n  Press Enter to continue...")
        elif choice == "2":
            if df is None:
                print("  Please load data first! Choose option 1")
            else:
                category_sales, top_products, monthly_sales = analyze_data(df)
            input("\n  Press Enter to continue...")
        elif choice == "3":
            if df is None:
                print("  Please load data first! Choose option 1")
            else:
                category_sales, top_products, monthly_sales = analyze_data(df)
                plot_graph(category_sales, top_products, monthly_sales)
            input("\n  Press Enter to continue...")
        elif choice == "4":
            if df is None:
                print("  Please load data first! Choose option 1")
            else:
                generate_report(df)
            input("\n  Press Enter to continue...")
        elif choice == "5":
            df = auto_process()
            input("\n  Press Enter to continue...")
        elif choice == "6":
            print("\n  Goodbye!")
            break
        else:
            print("  Invalid choice!")

if __name__ == "__main__":
    main()
