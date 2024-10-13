import dropbox
from config import DROPBOX_TOKEN


def connect_to_dropbox():
    dbx = dropbox.Dropbox(DROPBOX_TOKEN)
    try:
        dbx.users_get_current_account()  # Verifies connection
        return dbx
    except Exception as e:
        print(f"Error connecting to Dropbox: {e}")
        return None
