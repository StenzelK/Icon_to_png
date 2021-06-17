'''

convert jpg to png

'''
import os, time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import Image
dirs = [[dirs for _, dirs, _ in os.walk('D:\\romy')]][0][0]
folders_to_track = [f'D:\\romy\\{dir}\\Icons' for dir in dirs]

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print('update')

        for root, dirs, files in os.walk(folder_to_track):
            for dir in dirs:
                print(dir)
                for file in files:
                    print(file)
                    if file.endswith('.jpg'):
                        file = os.path.join(dir,file)
                        print(file)
                        im = Image.open(file)
                        os.remove(file)
                        im.save(f'{file[:-4]}.png')
observers = []
event_handler = MyHandler()
observer = Observer()

for folder_to_track in folders_to_track:
    targetPath = str(folder_to_track)
    observer.schedule(event_handler, targetPath, recursive=True)
    observers.append(observer)

observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()