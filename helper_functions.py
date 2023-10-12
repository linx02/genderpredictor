# Import libraries

import cv2
import os
import numpy as np
import pandas as pd

# Vars

ROOT_DIR = os.getcwd()
DATASET_DIR = os.path.join(ROOT_DIR, 'dataset')
TRAIN_DIR, TEST_DIR, VAL_DIR = [os.path.join(DATASET_DIR, 'train'), os.path.join(DATASET_DIR, 'test'), os.path.join(DATASET_DIR, 'val')]
DIRS = {
    'train': {},
    'test': {},
    'val': {}
}

# Create data structure for easy access of individual folders

for train_dir, test_dir, val_dir in zip(os.listdir(TRAIN_DIR), os.listdir(TEST_DIR), os.listdir(VAL_DIR)):
    if train_dir == 'female':
        DIRS['train']['female'] = (os.path.join(TRAIN_DIR, train_dir))
    elif train_dir == 'male':
        DIRS['train']['male'] = (os.path.join(TRAIN_DIR, train_dir))
    
    if test_dir == 'female':
        DIRS['test']['female'] = (os.path.join(TEST_DIR, test_dir))
    elif train_dir == 'male':
        DIRS['test']['male'] = (os.path.join(TEST_DIR, test_dir))
    
    if val_dir == 'female':
        DIRS['val']['female'] = (os.path.join(VAL_DIR, val_dir))
    elif train_dir == 'male':
        DIRS['val']['male'] = (os.path.join(VAL_DIR, val_dir))

# Create project dataset as class
class ProjectDataset:
    global DIRS

    def __init__(self):
        self.dirs = DIRS
    
    # Create and return labels for dataset
    def labels(self) -> dict:

        data = {
            'train': {},
            'test': {},
            'val': {},
            'all': {}
        }

        data['train']['male'] = [1] * len(os.listdir(self.dirs['train']['male']))
        data['test']['male'] = [1] * len(os.listdir(self.dirs['test']['male']))
        data['val']['male'] = [1] * len(os.listdir(self.dirs['val']['male']))
        data['train']['female'] = [0] * len(os.listdir(self.dirs['train']['female']))
        data['test']['female'] = [0] * len(os.listdir(self.dirs['test']['female']))
        data['val']['female'] = [0] * len(os.listdir(self.dirs['val']['female']))
        data['all']['male'] = data['train']['male'] + data['test']['male'] + data['val']['male']
        data['all']['female'] = data['train']['female'] + data['test']['female'] + data['val']['female']
        data['all']['all'] = data['all']['male'] + data['all']['female']

        return data

    # Read and return filepaths for images in dataset
    def image_filepaths(self) -> dict:
        
        data = {
            'train': {},
            'test': {},
            'val': {},
            'all': {}
        }

        data['train']['male'] = [os.path.join(self.dirs['train']['male'], file) for file in os.listdir(self.dirs['train']['male'])]
        data['test']['male'] = [os.path.join(self.dirs['test']['male'], file) for file in os.listdir(self.dirs['test']['male'])]
        data['val']['male'] = [os.path.join(self.dirs['val']['male'], file) for file in os.listdir(self.dirs['val']['male'])]
        data['train']['female'] = [os.path.join(self.dirs['train']['female'], file) for file in os.listdir(self.dirs['train']['female'])]
        data['test']['female'] = [os.path.join(self.dirs['test']['female'], file) for file in os.listdir(self.dirs['test']['female'])]
        data['val']['female'] = [os.path.join(self.dirs['val']['female'], file) for file in os.listdir(self.dirs['val']['female'])]
        data['all']['male'] = data['train']['male'] + data['test']['male'] + data['val']['male']
        data['all']['female'] = data['train']['female'] + data['test']['female'] + data['val']['female']
        data['all']['all'] = data['all']['male'] + data['all']['female']

        return data

    # Read and return files as numpy arrays from dataset
    def images_array(self) -> dict:

        image_filepaths = self.image_filepaths()
        
        data = {
            'train': {},
            'test': {},
            'val': {},
            'all': {}
        }

        data['train']['male'] = [cv2.imread(img) for img in image_filepaths['train']['male']]
        data['test']['male'] = [cv2.imread(img) for img in image_filepaths['test']['male']]
        data['val']['male'] = [cv2.imread(img) for img in image_filepaths['val']['male']]
        data['train']['female'] = [cv2.imread(img) for img in image_filepaths['train']['female']]
        data['test']['female'] = [cv2.imread(img) for img in image_filepaths['test']['female']]
        data['val']['female'] = [cv2.imread(img) for img in image_filepaths['val']['female']]
        data['all']['male'] = data['train']['male'] + data['test']['male'] + data['val']['male']
        data['all']['female'] = data['train']['female'] + data['test']['female'] + data['val']['female']
        data['all']['all'] = data['all']['male'] + data['all']['female']

        return data

    # Create and return dataset as pandas dataframe
    def dataframe(self, type_:str) -> pd.DataFrame:
        if type_ == 'filepath':
            images = self.image_filepaths()
        elif type_ == 'array':
            images = self.images_array()

        labels = self.labels()

        data = {
            'file': images['all']['all'],
            'gender': labels['all']['all']
        }

        df = pd.DataFrame(data=data)

        return df