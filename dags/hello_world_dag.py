from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Following are defaults which can be overridden later on
args = {
    'owner': 'dimon',
    'start_date':datetime(2018, 11, 1),
    'provide_context':True
}

with DAG('Hello-world', description='Hello-world', schedule_interval='*/1 * * * *',  catchup=False, default_args=args) as dag: #0 * * * *   */1 * * * *
    t1 = BashOperator(
        task_id='task_1',
        bash_command='echo "Hello World from Task 1"')

    t2 = BashOperator(
        task_id='task_2',
        bash_command='echo "Hello World from Task 2"')

    t3 = BashOperator(
        task_id='task_3',
        bash_command='echo "Hello World from Task 3"')

    t4 = BashOperator(
        task_id='task_4',
        bash_command='echo "Hello World from Task 4"')

    t1 >> t2
    t1 >> t3
    t2 >> t4
    t3 >> t4

# dag = DAG('Hello-world', default_args=default_args)

# # t1, t2, t3 and t4 are examples of tasks created using operators

# t1 = BashOperator(
#     task_id='task_1',
#     bash_command='echo "Hello World from Task 1"',
#     dag=dag)

# t2 = BashOperator(
#     task_id='task_2',
#     bash_command='echo "Hello World from Task 2"',
#     dag=dag)

# t3 = BashOperator(schedule_interval='0 * * * *',  catchup=False,
#     task_id='task_3',
#     bash_command='echo "Hello World from Task 3"',
#     dag=dag)

# t4 = BashOperator(
#     task_id='task_4',
#     bash_command='echo "Hello World from Task 4"',
#     dag=dag)

# t2.set_upstream(t1)
# t3.set_upstream(t1)
# t4.set_upstream(t2)
# t4.set_upstream(t3)
