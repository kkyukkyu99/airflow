from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator


with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:

#일반적으로 덱 아이디와 파이썬 파일 명을 일치 시키는게 좋다
#schedule 분, 시, 일, 월, 요일 "0 0 * * *" 매일 0시 0분 마다 돈다의 의미
#start_date 덱이 언제부터 돌 껀지
#catchup 누락된 부분도 도는 것
#dagrun_timeout 타임아웃 값을 설정
#tags 태그 다는 것
#params 태스트에 공통적으로 넘겨줄 파라미터

    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )
#테스크는 오퍼레이터를 통해 만들어진다
#객체명과 테스크 아이디는 똑같이 하는게 좋다
    
    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2