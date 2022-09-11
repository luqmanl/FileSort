import datetime
import os
import shutil

from tqdm import tqdm

image_extensions = [".png", ".jpeg", ".jpg", ".gif", ".raw"]
video_extensions = [".mp4", ".mov", ".wmv", ".avi", ".mkv"]

def main():
    path = os.path.curdir
    filenames = os.listdir(path)

    for filename in tqdm(filenames):
        if os.path.isfile(filename):
            sort_by_date_and_type(filename)

"""
    Moves the given file to another directory containing only files with the same file type and date (by month/year).
"""
def sort_by_date_and_type(path: str):
    (_, file_extension) = os.path.splitext(path)
    created_date = get_creation_date(path)
    dest_path = os.path.curdir

    # Add to image or video directory
    file_extension = file_extension.lower()
    if file_extension in image_extensions:
        dest_path = dest_path + "/images/"
    elif file_extension in video_extensions:
        dest_path += "/videos/"
    else:
        return

    # Add to directory within correct year and month
    month = datetime.datetime.strptime(str(created_date.month), "%m")
    dest_path += str(created_date.year) + "/" + month.strftime("%B") + "/"

    if not os.path.exists(dest_path):
        os.makedirs(dest_path, exist_ok=False)
    shutil.move(path, dest_path)
    

def get_creation_date(f: str):
    t = os.path.getmtime(f)
    return datetime.datetime.fromtimestamp(t)


if __name__ == '__main__':
    main()


