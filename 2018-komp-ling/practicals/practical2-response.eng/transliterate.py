import re
import argparse
import hfst


# Pasport ICAO
class transliterator:
    def __init__(self):
        letters_cyr = 'йцукенгшщзхъфывапролджэячсмитьбюё'
        letters_lat = ['j', 'c', 'u', 'k', 'e', 'n', 'g', ' sh', 'shch', 'z', 'kh', 'ie', 'f', 'y', 'v', 'a', 'p',
                       'r', 'o', 'l', 'd', 'zh', 'e', 'ia', 'ch', 's', 'm', 'i', 't', '0', 'b', 'iu', 'e']
        letters_cyr += letters_cyr.upper()
        letters_lat += [trans[0].upper() + trans[1:] for trans in letters_lat]
        regexes = []
        for i in range(len(letters_cyr)):
            regexes.append(hfst.regex(' {0} -> {1} || _'.format(letters_cyr[i], letters_lat[i])))
        tr = regexes[0]
        for reg in regexes[1:]:
            tr.compose(reg)
        self.tr = tr

    def transliterate(self, sents):
        result = []
        for sent in sents:
            curr_sent = [sent]
            for word in re.findall(r'[\w]+\b', sent):
                look = self.tr.lookup(word)
                curr_sent.append((word, re.sub('@_EPSILON_SYMBOL_@', '', look[0][0])))
            result.append(curr_sent)
        return result

    def transliterate_from_file_to_file(self, in_file_path, out_file_path):
        lines = [line for line in open(in_file_path, 'r')]
        transletirated = self.transliterate(lines)
        with open(out_file_path, 'w') as out_file:
            for sent in transletirated:
                for line in sent:
                    if type(line) == str:
                        out_file.write(line + '\n')
                    else:
                        out_file.write('\t'.join(line) + '\n')
                out_file.write('\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--in-file', '-i', help='input file')
    parser.add_argument('--out-file', '-o', help='output file')
    args = parser.parse_args()
    trans = transliterator()
    trans.transliterate_from_file_to_file(args.in_file, args.out_file)