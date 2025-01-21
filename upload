from google.colab import files
from google.oauth2 import service_account

up = files.upload()

k_p = list(up.keys())[0]
c = service_account.Credentials.from_service_account_file(k_p)
c

from itertools import product
from google.cloud import bigquery

cli = bigquery.Client(credentials=c, project=c.project_id)

job = cli.load_table_from_dataframe(df, 'animal.df')
job.result()
print(f'Uploaded{job.output_rows} rows to {job.destination}')
