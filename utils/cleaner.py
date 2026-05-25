import os
import time

DOWNLOAD_DIR = "downloads"


def clean_old_files(hours=1):

    now = time.time()

    if not os.path.exists(DOWNLOAD_DIR):
        return

    for file in os.listdir(DOWNLOAD_DIR):

        path = os.path.join(
            DOWNLOAD_DIR,
            file
        )

        if os.path.isfile(path):

            file_age = now - os.path.getmtime(path)

            if file_age > hours * 3600:

                try:
                    os.remove(path)

                except:
                    pass
