import pandas as pd
if __name__ == '__main__':
    df = pd.read_csv('../asset/top500_reports_list.csv')

    for index, row in df.iterrows():
        report_title = row['Report Title']
        report_path = row['Report Path']
        report_pages_path = row['Pages Path']
        report_block_path = row['Blocks Path']
        report_pages_vector_path = row['Pages Vector Path']
        report_Blocks_vector_path = row['Blocks Vector Path']

        # ...If you need other columns, you can access them like this
        pass

        print(f"Report Title: {report_title}")
        print(f"Report Path: {report_path}")
        print(f"Pages Path: {report_pages_path}")
        print(f"Blocks Path: {report_block_path}")
        print(f"Pages Vector Path: {report_pages_vector_path}")
        print(f"Blocks Vector Path: {report_Blocks_vector_path}")

        break
