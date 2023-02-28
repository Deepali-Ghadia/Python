# examining zipfile contents
from zipfile import ZipFile
with ZipFile("C:/Users/user/OneDrive/Desktop/Mobile_Wallpaper.zip") as zip:
    zip.printdir()
    
    
# extracting zipfile contents to a directory
with ZipFile("C:/Users/user/OneDrive/Desktop/Mobile_Wallpaper.zip") as zip:
    zip.extractall('Chapter-132/')