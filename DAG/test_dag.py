from airflow.decorators import dag, task, task_group
from airflow.exceptions import AirflowFailException, AirflowSkipException
from airflow.utils.trigger_rule import TriggerRule
from airflow.providers.amazon.aws.operators.s3 import S3CopyObjectOperator, S3DeleteObjectsOperator, S3ListOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.utils.email import send_email_smtp
from airflow.operators.email import EmailOperator
from airflow.models import Variable