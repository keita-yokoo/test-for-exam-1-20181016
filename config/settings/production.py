from .base import *
import os
import boto3

# 設定値リスト
keys = [
    "DEBUG",
    "A_TEST",
    "TEST"
]


# AWS System Manager パラメータストアから本番環境用設定値を取得する
def get_params():
    response = boto3.client("ssm", region_name="us-east-1").get_parameters(
        Names=keys,
        WithDecryption=True
    )

    return {param["Name"]: param["Value"] for param in response["Parameters"]}


# パラメータストアから取得した値をグローバル変数に代入しSettingsから参照できるようにする
parameters = get_params()
for key in keys:
    exec("{0}='{1}'".format(key, parameters[key]))


# def get_param_test(key, parameters):
#     for param in parameters:
#         if param["Name"] == key:
#             return param["Value"]
#     raise KeyError(key)


# SECURITY WARNING: don't run with debug turned on in production!
# print(os.environ.keys())
# DEBUG = get_param("DEBUG")

# print(DEBUG)
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



