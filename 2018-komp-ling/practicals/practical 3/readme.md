There are two python scripts. Both of them have --help command.

train.py takes path to input conllu file. And saves trained model to ouput file (optional -o argument)

apply_model.py applies this model and produce text with tags to standart output. It must take path to parsed file and can take -m argumant with model file.
