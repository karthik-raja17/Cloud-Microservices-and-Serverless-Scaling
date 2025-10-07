import os
import logging
from azure.storage.blob import BlobServiceClient

def main(input: tuple) -> list:
    connect_str, container_name = input
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client(container_name)
    
    data = []
    for blob in container_client.list_blobs():
        blob_client = container_client.get_blob_client(blob.name)
        blob_data = blob_client.download_blob().readall().decode("utf-8")
        data.extend(blob_data.splitlines())
    
    return data