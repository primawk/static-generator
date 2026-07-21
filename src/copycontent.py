import os
import shutil

def copy_content(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
        os.mkdir(destination)
    else:
        os.mkdir(destination)

    for filename in os.listdir(source):
            src = os.path.join(source, filename)
            dst = os.path.join(destination, filename)

            if os.path.isfile(src):
                shutil.copy(src, dst)
            else:
                copy_content(src, dst)

             

