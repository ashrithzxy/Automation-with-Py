import os
import shutil
source = "Source Path"
fdir1 = os.listdir("folder1")
fdir2 = os.listdir("folder2")
diff = list(set(fdir2) - set(fdir1))
for file in diff:
    shutil.move(os.path.join(source, file), "Destination Path")
