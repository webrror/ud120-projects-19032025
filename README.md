ud120-projects
==============

Starter project code for students taking Udacity ud120

#### Updated on 19 March 2025

### Last tried on Windows 11 with Python 3.13.2

### Setup
- Create a virtual environment for Python 3.9 or higher.
  python -m venv . (. is the current directory, use the name of your choice)
  - Activate the virtual environment.
    - Windows: `.\Scripts\activate`
    - Linux/Mac: `source ./bin/activate`
- ```
  pip install -r requirements.txt
  ```
- Download the dataset from [here](https://huggingface.co/datasets/SnowZeng/enron_mail/resolve/main/enron_mail_20150507.tar.gz). Much faster to download.
- Place the dataset at source directory.
- Run and wait for the dataset to be extracted:
  
  ```
  python tools/startup.py
  ```

### Contribution Note
The code in this repo has been upgraded from Python 2 to Python 3 by [Siddharth Kekre](https://github.com/iSiddharth20) in this [PR](https://github.com/udacity/ud120-projects/pull/302). Refer to the [Change Log](https://github.com/iSiddharth20/ud120-projects/blob/master/CHANGELOG.md) for more details. 

### Path Note
According to your `ud120-projects` location you may have to change the path for every `sys.path.append(os.path.abspath(("../tools/")))` to `sys.path.append(os.path.abspath(("./tools/")))` (Basically '../' to './' for all of the files path) or vice-versa in your `.py` files.

### Outputs

#### Lesson 2 (Naive Bayes)

```
No. of Chris training emails :  7936
No. of Sara training emails :  7884
Training Time: 0.993 s
Predicting Time: 0.177 s
Accuracy Score: 0.9732650739476678
```
