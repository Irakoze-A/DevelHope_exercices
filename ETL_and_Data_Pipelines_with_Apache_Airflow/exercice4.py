import time 
import json 
from airflow import DAG 
from airflow.operators.postgres_operator import PostgresOperator 
from datetime import timedelta

from airflow.utils.dates import days_ago

default_args = { 'owner': 'airflow',
'retries': 1, 'retry_delay': timedelta(minutes=5), }

create_query=""" 
CREATE TABLE employee (
    name VARCHAR(250) NOT NULL,
    age  INT          NOT NULL
);
"""



insert_data_query=""" 
INSERT INTO employee (name, age) VALUES
    ('Ami', 15),
    ('Mister', 25),
    ('Aris', 35);
"""

calculating_averag_age = """SELECT AVG(age) FROM employee; """

dag_postgres = DAG(dag_id = "Postgres_dag_connection", default_args = default_args, schedule_interval = None, start_date = days_ago(1))

create_table = PostgresOperator(task_id = "creation_of_table", sql = create_query, dag = dag_postgres, postgres_conn_id = "postgres_default")

insert_data = PostgresOperator(task_id = "insertion_of_data", sql = insert_data_query, dag = dag_postgres, postgres_conn_id = "postgres_default")

group_data = PostgresOperator(task_id = "calculating_averag_age", sql = calculating_averag_age, dag = dag_postgres, postgres_conn_id = "postgres_default")

create_table >> insert_data >> group_data
