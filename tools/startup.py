#!/usr/bin/python3

print("Checking for nltk")
try:
    import nltk
except ImportError:
    print("You should install nltk before continuing")

print("Checking for numpy")
try:
    import numpy
except ImportError:
    print("You should install numpy before continuing")

print("Checking for scipy")
try:
    import scipy
except:
    print("You should install scipy before continuing")

print("Checking for sklearn")
try:
    import sklearn
except:
    print("You should install sklearn before continuing")

print("Download the Enron dataset")
print("From this hugging face repo: https://huggingface.co/datasets/SnowZeng/enron_mail/resolve/main/enron_mail_20150507.tar.gz")
print("Much faster to download")

# If you want to download from the original source, uncomment the following
# import requests
# url = "https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tar.gz"
# filename = "../enron_mail_20150507.tar.gz"
# with open(filename, "wb") as f:
#     r = requests.get(url)
#     f.write(r.content)
# print("Download Complete!")

print("Unzipping Enron dataset (This may take a while)")
import tarfile
from tqdm import tqdm # for progress bar

# Function to show progress during extraction
def extract_with_progress(tar_file, path="."):
    with tarfile.open(tar_file, "r:gz") as tar:
        total_members = len(tar.getmembers())
        for member in tqdm(tar.getmembers(), total=total_members, desc="Extracting"):
            tar.extract(member, path)

# Unzipping the dataset with progress bar
extract_with_progress("../enron_mail_20150507.tar.gz")

print("You're ready to go!")