import pickle as p
import argparse
from unigram import unigram_model


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', dest='output', default='saved_model.p', help='Path to file to save model.')
    parser.add_argument('input_conllu_file', help='Path to file with train set in conllu format.')
    args = parser.parse_args()
    model = unigram_model(args.input_conllu_file)
    with open(args.output, 'wb') as model_file:
           p.dump(model, model_file, protocol=p.HIGHEST_PROTOCOL)
