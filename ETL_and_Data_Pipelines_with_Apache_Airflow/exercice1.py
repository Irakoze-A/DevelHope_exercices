from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_dag_args = { 
	'start_date' : datetime( 2022, 1, 1), 
	'email_on_failure' : False, 
	'email_on_retry': False, 
	'retries': 1, 
	'retry_delay': timedelta(minutes=5), 
	'project_id': 1 }

with DAG("First_DAG", schedule_interval = None, default_args = default_dag_args) as dag:

	# here at this level we define our tasks of the DAG
	task_0 = BashOperator(task_id = 'bash_task', bash_command = "echo 'command executed from Bash Operator' ")
	task_1 = BashOperator(task_id = 'bash_task_move_data', 
		bash_command = "cp /home/moi/DATA_CENTER/DATA_LAKE/dataset_raw.txt  /home/moi/DATA_CENTER/CLEAN_DATA")
	task_2 = BashOperator(task_id = 'bash_task_remove_source', bash_command = "rm /home/moi/DATA_CENTER/DATA_LAKE/dataset_raw.txt")


	# in the end of your DAG definition, we want to write the dependencies between tasks. >> <<
	task_0 >> task_1 >> task_2

