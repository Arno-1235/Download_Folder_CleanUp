from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os 
import json
import shutil
from datetime import datetime
from time import gmtime, strftime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        FileSizeArr = [[]]
        time.sleep(1)
        for filename in os.listdir(folder_to_track):
            if filename != 'Sorted' and filename != 'desktop.ini':
                if str(os.path.splitext(folder_to_track + '/' + filename)[1]) != ".crdownload":
                    FileSizeArr[0].append(filename)
                    FileSizeArr.append([])
        #print(FileSizeArr)
        for i in range(2):
            for filename in os.listdir(folder_to_track):
                if filename != 'Sorted' and filename != 'desktop.ini' and str(os.path.splitext(folder_to_track + '/' + filename)[1]) != ".crdownload":
                    try:
                        FileSizeArr[FileSizeArr[0].index(filename)+1].append(os.path.getsize(folder_to_track + '/' + filename))
                    except:
                        print("Error")
            time.sleep(5)
        for file in FileSizeArr:
            if FileSizeArr.index(file) != 0:
                Changed = False
                for size in FileSizeArr[FileSizeArr.index(file)]:
                    if size != FileSizeArr[FileSizeArr.index(file)][0]:
                        Changed = True
                
                if Changed == False:
                    filename = FileSizeArr[0][FileSizeArr.index(file)-1]
                    
                    try:
                        new_name = filename
                        extension = 'noname'
                        try:
                            extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                            path = extensions_folders[extension]
                        except Exception:
                            extension = 'noname'

                        folder_destination_path = extensions_folders[extension]

                        file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                        while file_exists:
                            i += 1
                            new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                            new_name = new_name.split("/")[4]
                            file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                        src = folder_to_track + "/" + filename

                        new_name = folder_destination_path + "/" + new_name
                        os.rename(src, new_name)
                    except Exception:
                        print("Error " + filename)
         
        #print(FileSizeArr)
            
            

extensions_folders = {
#No name
    'noname' : "/Users/Arno/Downloads/Sorted/Other/Uncategorized",
#Audio
    '.aif' : "/Users/Arno/Downloads/Sorted/Media/Audio",
    '.cda' : "/Users/Arno/Downloads/Sorted/Media/Audio",
    '.mid' : "/Users/Arno/Downloads/Sorted/Media/Audio",
    '.midi' : "/Users/Arno/Downloads/Sorted/Media/Audio",
    '.mp3' : "/Users/Arno/Downloads/Sorted/Media/Audio",
    '.mpa' : "/Users/Arno/Downloads/Sorted/Media/Audio",
    '.ogg' : "/Users/Arno/Downloads/Sorted/Media/Audio",
    '.wav' : "/Users/Arno/Downloads/Sorted/Media/Audio",
    '.wma' : "/Users/Arno/Downloads/Sorted/Media/Audio",
    '.wpl' : "/Users/Arno/Downloads/Sorted/Media/Audio",
    '.m3u' : "/Users/Arno/Downloads/Sorted/Media/Audio",
#Text
    '.txt' : "/Users/Arno/Downloads/Sorted/Text/TextFiles",
    '.doc' : "/Users/Arno/Downloads/Sorted/Text/Microsoft/Word",
    '.docx' : "/Users/Arno/Downloads/Sorted/Text/Microsoft/Word",
    '.odt ' : "/Users/Arno/Downloads/Sorted/Text/TextFiles",
    '.pdf': "/Users/Arno/Downloads/Sorted/Text/PDF",
    '.rtf': "/Users/Arno/Downloads/Sorted/Text/TextFiles",
    '.tex': "/Users/Arno/Downloads/Sorted/Text/TextFiles",
    '.wks ': "/Users/Arno/Downloads/Sorted/Text/TextFiles",
    '.wps': "/Users/Arno/Downloads/Sorted/Text/TextFiles",
    '.wpd': "/Users/Arno/Downloads/Sorted/Text/TextFiles",
#Video
    '.3g2': "/Users/Arno/Downloads/Sorted/Media/Video",
    '.3gp': "/Users/Arno/Downloads/Sorted/Media/Video",
    '.avi': "/Users/Arno/Downloads/Sorted/Media/Video",
    '.flv': "/Users/Arno/Downloads/Sorted/Media/Video",
    '.h264': "/Users/Arno/Downloads/Sorted/Media/Video",
    '.m4v': "/Users/Arno/Downloads/Sorted/Media/Video",
    '.mkv': "/Users/Arno/Downloads/Sorted/Media/Video",
    '.mov': "/Users/Arno/Downloads/Sorted/Media/Video",
    '.mp4': "/Users/Arno/Downloads/Sorted/Media/Video",
    '.mpg': "/Users/Arno/Downloads/Sorted/Media/Video",
    '.mpeg': "/Users/Arno/Downloads/Sorted/Media/Video",
    '.rm': "/Users/Arno/Downloads/Sorted/Media/Video",
    '.swf': "/Users/Arno/Downloads/Sorted/Media/Video",
    '.vob': "/Users/Arno/Downloads/Sorted/Media/Video",
    '.wmv': "/Users/Arno/Downloads/Sorted/Media/Video",
#Images
    '.ai': "/Users/Arno/Downloads/Sorted/Media/Images",
    '.bmp': "/Users/Arno/Downloads/Sorted/Media/Images",
    '.gif': "/Users/Arno/Downloads/Sorted/Media/Images",
    '.ico': "/Users/Arno/Downloads/Sorted/Media/Images",
    '.jpg': "/Users/Arno/Downloads/Sorted/Media/Images",
    '.JPG': "/Users/Arno/Downloads/Sorted/Media/Images",
    '.jpeg': "/Users/Arno/Downloads/Sorted/Media/Images",
    '.JPEG': "/Users/Arno/Downloads/Sorted/Media/Images",
    '.png': "/Users/Arno/Downloads/Sorted/Media/Images",
    '.PNG': "/Users/Arno/Downloads/Sorted/Media/Images",
    '.ps': "/Users/Arno/Downloads/Sorted/Media/Images",
    '.psd': "/Users/Arno/Downloads/Sorted/Media/Images",
    '.svg': "/Users/Arno/Downloads/Sorted/Media/Images",
    '.tif': "/Users/Arno/Downloads/Sorted/Media/Images",
    '.tiff': "/Users/Arno/Downloads/Sorted/Media/Images",
    '.CR2': "/Users/Arno/Downloads/Sorted/Media/Images",
#Internet
    '.asp': "/Users/Arno/Downloads/Sorted/Other/Internet",
    '.aspx': "/Users/Arno/Downloads/Sorted/Other/Internet",
    '.cer': "/Users/Arno/Downloads/Sorted/Other/Internet",
    '.cfm': "/Users/Arno/Downloads/Sorted/Other/Internet",
    '.cgi': "/Users/Arno/Downloads/Sorted/Other/Internet",
    '.pl': "/Users/Arno/Downloads/Sorted/Other/Internet",
    '.css': "/Users/Arno/Downloads/Sorted/Other/Internet",
    '.htm': "/Users/Arno/Downloads/Sorted/Other/Internet",
    '.js': "/Users/Arno/Downloads/Sorted/Other/Internet",
    '.jsp': "/Users/Arno/Downloads/Sorted/Other/Internet",
    '.part': "/Users/Arno/Downloads/Sorted/Other/Internet",
    '.php': "/Users/Arno/Downloads/Sorted/Other/Internet",
    '.rss': "/Users/Arno/Downloads/Sorted/Other/Internet",
    '.xhtml': "/Users/Arno/Downloads/Sorted/Other/Internet",
#Compressed
    '.7z': "/Users/Arno/Downloads/Sorted/Other/Compressed",
    '.arj': "/Users/Arno/Downloads/Sorted/Other/Compressed",
    '.deb': "/Users/Arno/Downloads/Sorted/Other/Compressed",
    '.pkg': "/Users/Arno/Downloads/Sorted/Other/Compressed",
    '.rar': "/Users/Arno/Downloads/Sorted/Other/Compressed",
    '.rpm': "/Users/Arno/Downloads/Sorted/Other/Compressed",
    '.tar.gz': "/Users/Arno/Downloads/Sorted/Other/Compressed",
    '.z': "/Users/Arno/Downloads/Sorted/Other/Compressed",
    '.zip': "/Users/Arno/Downloads/Sorted/Other/Compressed",
#Disc
    '.bin': "/Users/Arno/Downloads/Sorted/Other/Disc",
    '.dmg': "/Users/Arno/Downloads/Sorted/Other/Disc",
    '.iso': "/Users/Arno/Downloads/Sorted/Other/Disc",
    '.toast': "/Users/Arno/Downloads/Sorted/Other/Disc",
    '.vcd': "/Users/Arno/Downloads/Sorted/Other/Disc",
#Data
    '.csv': "/Users/Arno/Downloads/Sorted/Programming/Database",
    '.dat': "/Users/Arno/Downloads/Sorted/Programming/Database",
    '.db': "/Users/Arno/Downloads/Sorted/Programming/Database",
    '.dbf': "/Users/Arno/Downloads/Sorted/Programming/Database",
    '.log': "/Users/Arno/Downloads/Sorted/Programming/Database",
    '.mdb': "/Users/Arno/Downloads/Sorted/Programming/Database",
    '.sav': "/Users/Arno/Downloads/Sorted/Programming/Database",
    '.sql': "/Users/Arno/Downloads/Sorted/Programming/Database",
    '.tar': "/Users/Arno/Downloads/Sorted/Programming/Database",
    '.xml': "/Users/Arno/Downloads/Sorted/Programming/Database",
    '.json': "/Users/Arno/Downloads/Sorted/Programming/Database",
#Executables
    '.apk': "/Users/Arno/Downloads/Sorted/Other/Executables",
    '.bat': "/Users/Arno/Downloads/Sorted/Other/Executables",
    '.com': "/Users/Arno/Downloads/Sorted/Other/Executables",
    '.exe': "/Users/Arno/Downloads/Sorted/Other/Executables",
    '.gadget': "/Users/Arno/Downloads/Sorted/Other/Executables",
    '.jar': "/Users/Arno/Downloads/Sorted/Other/Executables",
    '.wsf': "/Users/Arno/Downloads/Sorted/Other/Executables",
#Fonts
    '.fnt': "/Users/Arno/Downloads/Sorted/Other/Fonts",
    '.fon': "/Users/Arno/Downloads/Sorted/Other/Fonts",
    '.otf': "/Users/Arno/Downloads/Sorted/Other/Fonts",
    '.ttf': "/Users/Arno/Downloads/Sorted/Other/Fonts",
#Presentations
    '.key': "/Users/Arno/Downloads/Sorted/Text/Presentations",
    '.odp': "/Users/Arno/Downloads/Sorted/Text/Presentations",
    '.pps': "/Users/Arno/Downloads/Sorted/Text/Presentations",
    '.ppt': "/Users/Arno/Downloads/Sorted/Text/Presentations",
    '.pptx': "/Users/Arno/Downloads/Sorted/Text/Presentations",
#Programming
    '.c': "/Users/Arno/Downloads/Sorted/Programming/C&C++",
    '.class': "/Users/Arno/Downloads/Sorted/Programming/Java",
    '.dart': "/Users/Arno/Downloads/Sorted/Programming/Dart",
    '.py': "/Users/Arno/Downloads/Sorted/Programming/Python",
    '.sh': "/Users/Arno/Downloads/Sorted/Programming/Shell",
    '.swift': "/Users/Arno/Downloads/Sorted/Programming/Swift",
    '.html': "/Users/Arno/Downloads/Sorted/Programming/C&C++",
    '.h': "/Users/Arno/Downloads/Sorted/Programming/C&C++",
#Spreadsheets
    '.ods' : "/Users/Arno/Downloads/Sorted/Text/Microsoft/Excel",
    '.xlr' : "/Users/Arno/Downloads/Sorted/Text/Microsoft/Excel",
    '.xls' : "/Users/Arno/Downloads/Sorted/Text/Microsoft/Excel",
    '.xlsx' : "/Users/Arno/Downloads/Sorted/Text/Microsoft/Excel",
#System
    '.bak' : "/Users/Arno/Downloads/Sorted/Text/Other/System",
    '.cab' : "/Users/Arno/Downloads/Sorted/Text/Other/System",
    '.cfg' : "/Users/Arno/Downloads/Sorted/Text/Other/System",
    '.cpl' : "/Users/Arno/Downloads/Sorted/Text/Other/System",
    '.cur' : "/Users/Arno/Downloads/Sorted/Text/Other/System",
    '.dll' : "/Users/Arno/Downloads/Sorted/Text/Other/System",
    '.dmp' : "/Users/Arno/Downloads/Sorted/Text/Other/System",
    '.drv' : "/Users/Arno/Downloads/Sorted/Text/Other/System",
    '.icns' : "/Users/Arno/Downloads/Sorted/Text/Other/System",
    '.ico' : "/Users/Arno/Downloads/Sorted/Text/Other/System",
    '.ini' : "/Users/Arno/Downloads/Sorted/Text/Other/System",
    '.lnk' : "/Users/Arno/Downloads/Sorted/Text/Other/System",
    '.msi' : "/Users/Arno/Downloads/Sorted/Text/Other/System",
    '.sys' : "/Users/Arno/Downloads/Sorted/Text/Other/System",
    '.tmp' : "/Users/Arno/Downloads/Sorted/Text/Other/System",
}

folder_to_track = '/Users/Arno/Downloads'
folder_destination = '/Users/Arno/Downloads/Sorted'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:           
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
