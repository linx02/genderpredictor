# Import libraries
# Import libraries

import os
import numpy as np
import pandas as pd
import cv2

# Vars

ROOT_DIR = os.path.dirname(os.getcwd())
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

        splits = ['train', 'test', 'val']
        genders = ['male', 'female']

        for split in splits:
            data[split] = {}
            for gender in genders:
                num_samples = len(os.listdir(self.dirs[split][gender]))
                data[split][gender] = [1] * num_samples if gender == 'male' else [0] * num_samples

        for gender in genders:
            data['all'][gender] = sum((data[split][gender] for split in splits), [])
        
        data['train']['all'] = data['train']['male'] + data['train']['female']
        data['test']['all'] = data['test']['male'] + data['test']['female']
        data['val']['all'] = data['val']['male'] + data['val']['female']
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

        splits = ['train', 'test', 'val']
        genders = ['male', 'female']

        for split in splits:
            data[split] = {}
            for gender in genders:
                data[split][gender] = [os.path.join(self.dirs[split][gender], file) for file in os.listdir(self.dirs[split][gender])]

        for gender in genders:
            data['all'][gender] = sum((data[split][gender] for split in splits), [])

        data['train']['all'] = data['train']['male'] + data['train']['female']
        data['test']['all'] = data['test']['male'] + data['test']['female']
        data['val']['all'] = data['val']['male'] + data['val']['female']
        data['all']['all'] = data['all']['male'] + data['all']['female']

        return data

    # Read and return files as numpy arrays from dataset
    def images_array(self, normalize:bool = False, resize:bool = False) -> dict:

        image_filepaths = self.image_filepaths()
        
        data = {
            'train': {},
            'test': {},
            'val': {},
            'all': {}
        }

        splits = ['train', 'test', 'val']
        genders = ['male', 'female']

        for split in splits:
            data[split] = {}
            for gender in genders:
                data[split][gender] = []
                image_list = image_filepaths[split][gender]

                for img in image_list:
                    image_array = cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2RGB)
                    if resize:
                        image_array = cv2.resize(image_array, (200, 200))
                    if normalize:
                        image_array = image_array / 255.0
                    data[split][gender].append(image_array)
        
        for gender in genders:
            data['all'][gender] = sum((data[split][gender] for split in splits), [])

        data['train']['all'] = data['train']['male'] + data['train']['female']
        data['test']['all'] = data['test']['male'] + data['test']['female']
        data['val']['all'] = data['val']['male'] + data['val']['female']
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