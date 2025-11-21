import json
import regex as re

def mut_regall(string):
    pattern = r"'pos': (?P<position>\d+), 'from_nt': '(?P<from_nt>[\w]+)', 'from_aa': '(?P<from_aa>[\w\*]+)', 'to_nt': '(?P<to_nt>['\w\*]+)', 'to_aas': \[(?P<to_aas>['\w,\s\*]+)], 'unique': (?P<unique>\d+), 'total': (?P<total>\d+), 'intermediate_aa': '(?P<intermediate_aa>[\w\d\*])'"

    tjson = json.loads(string)
    
    if "ALL" in str(tjson["regions"].keys()):
        all_value = str(tjson["regions"]["ALL"])
        find = re.findall(pattern,all_value)
        return find
    
    else:
        else_value = str(tjson["regions"])
        return else_value