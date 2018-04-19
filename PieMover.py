import shutil
import os
source = "Source Path"
for file in os.listdir("Source Path"):
    if file.endswith(".py"):
        shutil.move(os.path.join(source, file), "Destination Path")
