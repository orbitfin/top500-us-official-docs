# Orbit Top 500 US Official Docs

## Introduction

#### Why Official Filings Matter in Investment Research and Risk & Compliance

Investment research and risk management rely heavily on official filings as they provide the most accurate,
comprehensive, and up-to-date information about a company's financial health, operational performance, and risk
exposures. Documents such as annual reports, earnings releases, and regulatory filings are primary sources of truth,
offering insights critical for:

- Investment Research: Identifying growth drivers, assessing financial performance, and analyzing risk factors.
- Risk & Compliance: Monitoring regulatory disclosures, understanding governance structures, and ensuring compliance
  with evolving standards.
- Systematic Analysis: Developing data-driven models by extracting structured information across multiple companies and
  industries.

However, analyzing these documents at scale is challenging due to their unstructured nature. This dataset is designed to
empower users to build their own RAG (Retrieval-Augmented Generation) solutions, enabling efficient information
extraction and systematic analysis.

#### About the Dataset

This repository provides one year of filings for the top 500 US companies and is updated monthly. The dataset includes
three formats to support diverse use cases:

- Original PDF Files:
    - Direct from official sources, retaining all formatting and annotations.
- Machine-Readable Text Versions:
    - Simplified, raw text extracted from PDFs for NLP and text analysis workflows.
- Vector Versions:
    - Pre-processed for retrieval systems, enabling semantic search and advanced AI applications.

#### Dataset Size

The dataset is organized into approximately 5,713 files, occupying a total S3 storage size of ~314.57 GB. Below is the
breakdown by format:

- PDF Files: ~5.85 GB
- Blocks Data: ~4.37 GB
- Pages Data: ~1.38 GB
- Blocks Text Data: ~290.54 GB
- Pages Text Data: ~12.11 GB

## How to use

#### Set up environment

First of all, you need to clone this repo(By GIT) or download code directly.
When you get the code, you can install Python by using `requirements.txt`.

You are required to install proper AWS CLI tool to get presigned url when you want
to download the raw report and report block information. Refer to
this [link](Installing or updating to the latest version of the AWS CLI)
to know how to install in your desktop.

Use the key(keys.csv) provided to config your AWS CLI.

#### Run the demo

Located to `src` folder, try `python demo_get_report_info.py`, you can get below output. This is sample output for
getting report basic info, raw report, block report, page report info.

```text
Report Title: 10-K
Report Path: s3://filing-reports/reports-data/stock_us/2024/02/21/edgar-data-1045810-000104581024000029-nvda-20240128.htm.pdf
Presigned URL: https://filing-reports.s3.amazonaws.com/reports-data/stock_us/2024/02/21/edgar-data-1045810-000104581024000029-nvda-20240128.htm.pdf?AWSAccessKeyId=AKIAZ2SDT5DU46K54RGA&Signature=yrcrUASsBWTJ6F2ZB04qOXUWlkk%3D&Expires=1732704535
Presigned URL Pages: https://filing-reports.s3.amazonaws.com/txt-vector/reports-data/stock_us/2024/02/21/edgar-data-1045810-000104581024000029-nvda-20240128.htm.pdf/pages.txt?AWSAccessKeyId=AKIAZ2SDT5DU46K54RGA&Signature=x105ImnWAXBrtVswDt34rPqctv8%3D&Expires=1732704535
Presigned URL Blocks: https://filing-reports.s3.amazonaws.com/txt-vector/reports-data/stock_us/2024/02/21/edgar-data-1045810-000104581024000029-nvda-20240128.htm.pdf/blocks.txt?AWSAccessKeyId=AKIAZ2SDT5DU46K54RGA&Signature=%2FosUcHLvKb42Ke5jVa2cIYmM7r0%3D&Expires=1732704535
Presigned URL Blocks Vector: https://filing-reports.s3.amazonaws.com/txt-vector/reports-data/stock_us/2024/02/21/edgar-data-1045810-000104581024000029-nvda-20240128.htm.pdf/pages.txt.vector?AWSAccessKeyId=AKIAZ2SDT5DU46K54RGA&Signature=D1cOvtOV5uTetePojnUxZjhjYFw%3D&Expires=1732704535
Presigned URL Blocks Vector: https://filing-reports.s3.amazonaws.com/txt-vector/reports-data/stock_us/2024/02/21/edgar-data-1045810-000104581024000029-nvda-20240128.htm.pdf/blocks.txt.vector?AWSAccessKeyId=AKIAZ2SDT5DU46K54RGA&Signature=LnXsfFGX5jeh2BGakUmu9PoFnk4%3D&Expires=1732704535
```

If you would like to get more information, you can adjust the code accordingly.

## Glossary

#### Report related files

Raw report: The raw report which you can download, in most cases, the report are in PDF format.

Block report: Orbit extract a report info into pieces, each piece is a block, the principle of a block extraction is
under a human reading habit.

Page report: Orbit extract a report info into pages, each page contains all the information with
machine readable format.

Block report vector: The Block report with vector format.

Page report vector: The Page report with vector format.

## License and Attribution

This dataset is released under a proprietary open source License. Please attribute the repository in any derived work or
publication.

## Feedback and Contributions

We welcome feedback and contributions! Feel free to open an issue or submit a pull request to improve the dataset or
provide additional use cases.
Let us know with emailing to `info@orbitfin.ai` how you’re using the data to power your research or compliance
workflows!

