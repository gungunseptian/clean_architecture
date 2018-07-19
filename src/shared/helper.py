from datetime import datetime
from collections import namedtuple

def get_now_timestamp():
    return datetime.now()

def get_value_from_dict(adict, key, default):
    output = default
    try:
        output = int(adict[key])
    except KeyError as e:
        print("Key Error: {}".format(e))
    except ValueError as e:
        print("Value Error: {}".format(e))

    return output

def build_next_url(url, cur_page, next_page):
    if not next_page:
        next_page = cur_page
    return url.replace("page={}".format(cur_page), "page={}".format(next_page))


def build_prev_url(url, cur_page, prev_page):
    if not prev_page:
        prev_page = cur_page
    return url.replace("page={}".format(cur_page), "page={}".format(prev_page))

def dict_to_obj(adict):

    return namedtuple('Struct', adict.keys())(*adict.values())

