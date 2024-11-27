import pandas as pd
import os
from utils import s3_split_path, get_presign_url

if __name__ == '__main__':
    df = pd.read_csv('../asset/top500_reports_list.csv')

    for index, row in df.iterrows():
        report_title = row['Report Title']
        report_path = row['Report Path']
        # ...If you need other columns, you can access them like this
        pass

        # Generate a presigned URL for the report
        s3_path_obj = s3_split_path(report_path)
        bucket_name, store_path = s3_split_path(report_path)
        store_path_pages = os.path.join("txt-vector", store_path, 'pages.txt')
        store_path_blocks = os.path.join("txt-vector", store_path, 'blocks.txt')
        store_path_pages_vector = os.path.join("txt-vector", store_path, 'pages.txt.vector')
        store_path_blocks_vector = os.path.join("txt-vector", store_path, 'blocks.txt.vector')

        presign_url = get_presign_url(bucket_name, store_path)
        presign_url_pages = get_presign_url(bucket_name, store_path_pages)
        presign_url_blocks = get_presign_url(bucket_name, store_path_blocks)
        presign_url_pages_vector = get_presign_url(bucket_name, store_path_pages_vector)
        presign_url_blocks_vector = get_presign_url(bucket_name, store_path_blocks_vector)

        # Print the report title and presigned URL
        print(f"Report Title: {report_title}")
        print(f"Report Path: {report_path}")
        print(f"Presigned URL: {presign_url}")
        print(f"Presigned URL Pages: {presign_url_pages}")
        print(f"Presigned URL Blocks: {presign_url_blocks}")
        print(f"Presigned URL Blocks Vector: {presign_url_pages_vector}")
        print(f"Presigned URL Blocks Vector: {presign_url_blocks_vector}")

        break
