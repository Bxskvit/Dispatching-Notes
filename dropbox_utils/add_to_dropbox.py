from dropbox.exceptions import ApiError
from .dropbox_connection import connect_to_dropbox
from utils import current_month_list


def upload_file(local_file_path=None, dropbox_file_path="/2024/load_lists/"):
    if local_file_path is None:
        local_file_path = current_month_list()

    dbx = connect_to_dropbox()

    if dbx is not None:
        # Include the file name in the dropbox_file_path
        dropbox_file_name = local_file_path.split("/")[-1]  # Get the file name from the local path
        full_dropbox_path = f"{dropbox_file_path}{dropbox_file_name}"

        try:
            with open(local_file_path, 'rb') as file:
                # Upload the file to Dropbox
                dbx.files_upload(file.read(), full_dropbox_path)
                print(f"File uploaded to {full_dropbox_path}")
        except ApiError as e:
            print(f"Error uploading file: {e}")

