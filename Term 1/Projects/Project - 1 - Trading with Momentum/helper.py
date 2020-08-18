import pandas as pd
import os
import tempfile
import zipfile
import glob
from tqdm import tqdm
import math
import requests


color_scheme = {
    'index': '#B6B2CF',
    'etf': '#2D3ECF',
    'tracking_error': '#6F91DE',
    'df_header': 'silver',
    'df_value': 'white',
    'df_line': 'silver',
    'heatmap_colorscale': [(0, '#6F91DE'), (0.5, 'grey'), (1, 'red')],
    'background_label': '#9dbdd5',
    'low_value': '#B6B2CF',
    'high_value': '#2D3ECF',
    'y_axis_2_text_color': 'grey',
    'shadow': 'rgba(0, 0, 0, 0.75)',
    'major_line': '#2D3ECF',
    'minor_line': '#B6B2CF',
    'main_line': 'black'}


def download_quandl_dataset(quandl_api_key, database, dataset, save_path, columns, tickers, start_date, end_date):
    """
    Download a dataset from Quandl and save it to `save_path`.
    Filter by columns, tickers, and date
    :param quandl_api_key: The Quandl API key
    :param database: The Quandl database to download from
    :param dataset: The dataset to download
    :param save_path: The path to save the dataset
    :param columns: The columns to save
    :param tickers: The tickers to save
    :param start_date: The rows to save that are older than this date
    :param end_date: The rows to save that are younger than this date
    """
    scrape_url = 'https://www.quandl.com/api/v3/datatables/{}/{}?qopts.export=true&api_key={}'\
        .format(database, dataset, quandl_api_key)
    scrape_request = requests.get(scrape_url)
    bulk_download_url = scrape_request.json()['datatable_bulk_download']['file']['link']

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_wiki_file = tmp_dir + 'tmp.zip'

        bulk_download_request = requests.get(bulk_download_url, stream=True, cookies=scrape_request.cookies)
        total_size = int(bulk_download_request.headers.get('content-length', 0));
        block_size = 1024 * 1024
        with open(tmp_wiki_file, 'wb') as f:
            for data in tqdm(
                    bulk_download_request.iter_content(block_size),
                    total=math.ceil(total_size // block_size),
                    unit='MB',
                    unit_scale=True,
                    desc='Downloading Data'):
                f.write(data)

        with tqdm(total=5, desc='Transforming Data', unit='Action') as pbar:
            # Unzip downloaded data
            zip_ref = zipfile.ZipFile(tmp_wiki_file, 'r')
            zip_ref.extractall(tmp_dir)
            zip_ref.close()
            pbar.update(1)

            # Check if the zip file only contains one csv file
            #   We're assuming that Quandl will always give us the data in a single csv file.
            #   If it's different, we want to throw an error.
            csv_files = glob.glob(os.path.join(tmp_dir, '*.csv'))
            assert len(csv_files) == 1,\
                'Bulk download of Quandl Wiki data failed. Wrong number of csv files found. Found {} file(s).'\
                    .format(len(csv_files))
            tmp_csv_file = csv_files[0]

            tmp_df = pd.read_csv(tmp_csv_file)
            pbar.update(1)
            tmp_df['date'] = pd.to_datetime(tmp_df['date'])
            pbar.update(1)

            # Remove unused data and save
            tmp_df = tmp_df[tmp_df['date'].isin(pd.date_range(start_date, end_date))]  # Filter unused dates
            tmp_df = tmp_df[tmp_df['ticker'].isin(tickers)]  # Filter unused tickers
            pbar.update(1)
            tmp_df.to_csv(save_path, columns=columns, index=False)  # Filter unused columns and save
            pbar.update(1)


def generate_config():
    return {'showLink': False, 'displayModeBar': False, 'showAxisRangeEntryBoxes': True}
