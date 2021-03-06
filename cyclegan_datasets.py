"""Contains the standard train/test splits for the cyclegan data."""

"""The size of each dataset. Usually it is the maximum number of images from
each domain."""
DATASET_TO_SIZES = {
    'WFG2FG_train': 1502
}

"""The image types of each dataset. Currently only supports .jpg or .png"""
DATASET_TO_IMAGETYPE = {
    'WFG2FG_train': '.jpg',
    
}

"""The path to the output csv file."""
PATH_TO_CSV = {
    'WFG2FG_train': './project6/input/WFG2FG_train.csv',
    
}
