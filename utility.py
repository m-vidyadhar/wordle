import pandas as pd
import re


class fprints:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    PREV_LINE = "\033[F"


def _parse_words_list(regexs, string):
    words = ""
    for (filepath, regex) in regexs.items():
        words = words + re.search(regex, string).group(1).replace("\"", "")
        words_list = words.split(",")
        print(len(words_list))

        pd.DataFrame(words_list, columns=["words"]).to_csv(filepath, index=False)
    return


def load_words(jspath, solpath, dictpath):
    with open(jspath) as file:
        content = file.read()
    
    regexs = {solpath: r"Ma\=\[(.*)\],Oa", dictpath: r"Oa\=\[(.*)\],Ra"}
    _parse_words_list(regexs, content)
    return