import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("sample.csv")))
print("Created: %s" % time.ctime(os.path.getctime("sample.csv")))