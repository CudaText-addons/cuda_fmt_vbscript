import os
import json
from . import vbscriptbeautifier as v
from cuda_fmt import get_config_filename

def options():

    op = v.default_options()
    fn = get_config_filename('VBScript Format')
    if not os.path.isfile(fn):
        return op

    with open(fn) as f:
        d = json.load(f)
        op.indent_size = d.get("indent_size", 1)
        op.indent_char = d.get("indent_char", "\t")
        op.indent_with_tabs = d.get("indent_with_tabs", True)
        op.preserve_newlines = d.get("preserve_newlines", True)
        op.max_preserve_newlines = d.get("max_preserve_newlines", 10)
    return op


def do_format(text):

    return v.beautify(text, options())
