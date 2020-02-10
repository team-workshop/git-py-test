# git-py-test

Initiation to git versioning and testing in python 


## Versioning

### Cloning the source repository

```
#cd path/to/projects/folder
cd 
git clone https://github.com/team-workshop/git-py-test.git
```

### Todo
...

## Testing framework

### Prerequisites

#### Setup python env

```
cd git-py-test
virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements.txt
```

### Create a new branch to start developing a new feature or fixing a bug

```
# Start from the default branch feature/initiation-python-test-dev
git checkout feature/initiation-python-test

# Create you own branch
git checkout -b feature/initiation-python-test-your-name
```

### Launch tests in command line

```
cd git-py-test
python -m unittest tests/test_eeg_quality.py
```

**Tests are all failing!**

### Your work

Our goal is to go through `eeg_quality.py: compute_quality_index` and validate 
the implementation of the algorithm.

Thus we will patch/add tests in `tests/test_eeg_quality.py`.

Some todos are embedded into the code to guide you a little. 
The workflow might be the following:

1. Patch existing tests
2. Add additional tests
3. Refactor compute_quality_index method
4. Commit and push your work
5. Pull request to merge your branch into dev