import requests 
import time 
import json 
from airflow import DAG 
from airflow.operators.python_operator import PythonOperator 
from airflow.operators.python import BranchPythonOperator 
from airflow.operators.dummy import DummyOperator

from datetime import datetime, timedelta 
import pandas as pd 
import numpy as np 
import os

def get_data(**kwargs):
	
	tickers = kwargs['tickers']
	for ticker in tickers:
		api_key = "7QPAUEV4HYKD6KCU"

		url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticker+ "&apikey=" + api_key
		r = requests.get(url)
		
		
		try:
			data = r.json()

			path = "/home/moi/airflow/DATA_CENTER/DATA_LAKE/"
			with open(path + "stock_market_raw_data_" + ticker + "_"  + str(datetime.now()), "w") as outfile: 
				json.dump(data, outfile)
		except:
			pass


default_dag_args = { 
    'start_date': datetime(2022, 9, 1), 
    'email_on_failure': False, 
    'email_on_retry': False, 
    'retries': 1, 
    'retry_delay': timedelta(minutes=5), 
    'project_id': 1 }

with DAG("Market_data_alphavantage_dag", schedule_interval = '@daily', catchup=False, default_args = default_dag_args) as dag_python:

	# here we define our tasks
	task_0 = PythonOperator(task_id = "get_market_data", python_callable = get_data, op_kwargs = {'tickers' : ['IBM','GPV.TRV','SHOP.TRT']})


