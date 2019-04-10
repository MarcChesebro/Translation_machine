# Translation_machine

## Instructions

### Setup

Using Python 3
```
pip install -r requirements.txt
cd seq2seq
pip install -e .
```
This will install all the requirorments for the project.

### Setting up the data

```
python preprocess_data.py
```
This will take the data and make it into parrellel text format as well as set up the vocabulary dictionaries.

### Training and prediction

To train the model simply run the test_train.sh script

To translate new sentences run the pred.sh script. This currently is set to just run on the validatation set, but this can be set at the top of the script.
