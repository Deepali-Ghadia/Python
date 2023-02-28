# Using Python ZipFile.extractall() to decompress a ZIP file
from zipfile import ZipFile
file_to_unzip = "C:/Users/user/OneDrive/Desktop/Mobile_Wallpaper.zip"
unzip = ZipFile(file_to_unzip, 'r')
print(unzip.extractall())
unzip.close()
