import os
import boto3
from datetime import datetime
from botocore.exceptions import NoCredentialsError
from boto3.session import Session
from django.conf import settings

# ACCESS_KEY = os.environ.get('ACCESS_KEY')
# SECRET_KEY = os.environ.get('SECRET_KEY')
# bucket_name = os.environ.get('bucket_name')
# ACCESS_KEY = "AKIAQUSEYW7ZJKXATXP3"
# bucket_name = "exam-answer-bucket"
# SECRET_KEY = "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"

# def create_bucket(ACCESS_KEY, SECRET_KEY):
#     s3 = boto3.client('s3',
#                       aws_access_key_id=ACCESS_KEY,
#                       aws_secret_access_key=SECRET_KEY)
#     s3.create_bucket(Bucket='exam-answer-bucket')
#
#
# # print(create_bucket(ACCESS_KEY, SECRET_KEY))
#
#
# def get_bucket_list(ACCESS_KEY, SECRET_KEY):
#     import boto3
#
#     # Create an S3 client
#     s3 = boto3.client('s3',
#                       aws_access_key_id=ACCESS_KEY,
#                       aws_secret_access_key=SECRET_KEY)
#     # Call S3 to list current buckets
#     response = s3.list_buckets()
#     # Get a list of all bucket names from the response
#     buckets = [bucket['Name'] for bucket in response['Buckets']]
#     # Print out the region name
#     region_name = s3.meta.region_name
#     print("region_name", region_name)
#     return buckets, region_name
#
#
# print(get_bucket_list(ACCESS_KEY, SECRET_KEY))


def get_file_name(local_file, var_name):
    ext = local_file.split("/")[-1].split(".")[-1]
    name = f"{var_name}/{var_name}_{datetime.now().isoformat()}.{ext}"
    return name


def upload_qr_to_s3(file_name, body, content_type='image/jpg'):
    try:
        s3 = boto3.client('s3', aws_access_key_id=settings.ACCESS_KEY,
                          aws_secret_access_key=settings.AWS_SECRET_KEY)

        try:
            s3.upload_file(body, settings.BUCKET_NAME, file_name)
            url = f"https://{settings.BUCKET_NAME}.s3.amazonaws.com/{file_name}"
            return url
        except Exception as err:
            print("err:", err)
            return False
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except Exception as error:
        return "Unable to connect:  " + str(error)


def upload_to_s3(file_name, body, content_type):
    try:
        session = Session(aws_access_key_id=settings.ACCESS_KEY, aws_secret_access_key=settings.AWS_SECRET_KEY)
        s3 = session.resource('s3')
        s3.Bucket(settings.BUCKET_NAME).put_object(Key=file_name, Body=body, ContentType=content_type)
        url = f"https://{settings.BUCKET_NAME}.s3.amazonaws.com/{file_name}"
        return url
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except Exception as error:
        return "Unable to connect:  " + str(error)


# uploaded = upload_to_aws(image_file, bucket_name)

# ACCESS_KEY = os.environ['ACCESS_KEY']
# SECRET_KEY = os.environ['SECRET_KEY']
# bucket_name = os.environ['bucket_name']
#
#
# image_file = "/Users/zestgeek26/PycharmProjects/testingProject/Dark-Minimalist.jpeg"
# user_id = 6
# answer_sheet = 5
# question_id = 1
# page_number = 1
#
# #
# #
# # def create_bucket(ACCESS_KEY, SECRET_KEY):
# #     s3 = boto3.client('s3',
# #                       aws_access_key_id=ACCESS_KEY,
# #                       aws_secret_access_key=SECRET_KEY)
# #     s3.create_bucket(Bucket='exam-answer-bucket')
# #
# #
# # # print(create_bucket(ACCESS_KEY, SECRET_KEY))
# #
# #
# # def get_bucket_list(ACCESS_KEY, SECRET_KEY):
# #     import boto3
# #
# #     # Create an S3 client
# #     s3 = boto3.client('s3',
# #                       aws_access_key_id=ACCESS_KEY,
# #                       aws_secret_access_key=SECRET_KEY)
# #     # Call S3 to list current buckets
# #     response = s3.list_buckets()
# #     # Get a list of all bucket names from the response
# #     buckets = [bucket['Name'] for bucket in response['Buckets']]
# #     # Print out the region name
# #     region_name = s3.meta.region_name
# #     print("region_name", region_name)
# #     return buckets, region_name
# #
# #
# # # print(get_bucket_list(ACCESS_KEY, SECRET_KEY))
#
#
# def get_file_name(user_id, answer_sheet, question_id, page_number):
#     name = f"{user_id}/{answer_sheet}/{question_id}-{page_number}"
#     return name
#
#
# def upload_to_aws(local_file, bucket_name, s3_file):
#     s3 = boto3.client('s3',
#                       aws_access_key_id=ACCESS_KEY,
#                       aws_secret_access_key=SECRET_KEY)
#
#     try:
#         file_name = get_file_name(user_id, answer_sheet, question_id, page_number)
#         s3.upload_file(s3_file, bucket_name, file_name)
#         url = s3.generate_presigned_url(
#             ClientMethod='get_object',
#             Params={
#                 'Bucket': bucket_name,
#                 'Key': file_name
#             }
#         )
#         # print("Upload Successful", url)
#         url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
#         return True, url
#     except FileNotFoundError:
#         print("The file was not found")
#         return False
#     except NoCredentialsError:
#         print("Credentials not available")
#         return False
#
#
# uploaded = upload_to_aws(image_file, bucket_name, image_file)
