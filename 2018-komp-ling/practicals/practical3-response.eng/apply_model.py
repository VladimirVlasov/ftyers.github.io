import pickle as p
import argparse
from unigram import unigram_model

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', dest='model_file', default='saved_model.p', help='Path to model.')
    parser.add_argument('input_file', help='Path to input text file.')
    args = parser.parse_args()
    with open(args.model_file, 'rb') as model_file:
        model = p.load(model_file)
    model.transform_file(args.input_file)