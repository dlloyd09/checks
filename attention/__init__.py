import sys

import check50
import check50.py

import tensorflow as tf

from transformers.tokenization_utils_base import BatchEncoding

@check50.check()
def exists():
    """mask.py exists"""
    check50.exists("mask.py")
    check50.include("assets")


@check50.check(exists)
def imports():
    """mask.py imports"""
    sys.path = [""] + sys.path
    check50.py.import_("mask.py")


@check50.check(imports)
def get_mask_token_index_0():
    """get_mask_token_index returns index in middle of sentence"""

    # Setup
    sys.path = [""] + sys.path
    mask = check50.py.import_("mask.py")
    mask_token_index = 103
    inputs = BatchEncoding({"input_ids": tf.constant(
        [[ 101, 2023, 2003, 1037,  103, 3231, 1012,  102]]
    )})

    # Test
    expected = 4
    actual = mask.get_mask_token_index(mask_token_index, inputs)

    try:
        actual = int(actual)
    except ValueError:
        raise check50.Failure("did not return an integer")

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))


@check50.check(imports)
def get_mask_token_index_1():
    """get_mask_token_index returns index at start of sentence"""

    # Setup
    sys.path = [""] + sys.path
    mask = check50.py.import_("mask.py")
    mask_token_index = 103
    inputs = BatchEncoding({"input_ids": tf.constant(
        [[ 101,  103, 2003, 1037, 3231, 1012,  102]]
    )})

    # Test
    expected = 1
    actual = mask.get_mask_token_index(mask_token_index, inputs)

    try:
        actual = int(actual)
    except ValueError:
        raise check50.Failure("did not return an integer")

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))


@check50.check(imports)
def get_mask_token_index_2():
    """get_mask_token_index returns None when mask token not present"""

    # Setup
    sys.path = [""] + sys.path
    mask = check50.py.import_("mask.py")
    mask_token_index = 103
    inputs = BatchEncoding({"input_ids": tf.constant(
        [[ 101, 2023, 2003, 1037, 3231, 1012,  102]]
    )})

    # Test
    expected = None
    actual = mask.get_mask_token_index(mask_token_index, inputs)

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))


@check50.check(imports)
def get_mask_token_index_3():
    """get_mask_token_index handles different mask token ID"""

    # Setup
    sys.path = [""] + sys.path
    mask = check50.py.import_("mask.py")
    mask_token_index = 108
    inputs = BatchEncoding({"input_ids": tf.constant(
        [[ 101, 2023, 2003, 1037,  108, 3231, 1012,  102]]
    )})

    # Test
    expected = 4
    actual = mask.get_mask_token_index(mask_token_index, inputs)

    try:
        actual = int(actual)
    except ValueError:
        raise check50.Failure("did not return an integer")

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))


@check50.check(imports)
def get_color_for_attention_score_0():
    """get_color_for_attention_score_0 handles score of 0"""

    # Setup
    sys.path = [""] + sys.path
    mask = check50.py.import_("mask.py")

    # Test
    expected = (0, 0, 0)
    actual = mask.get_color_for_attention_score(0)

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))


@check50.check(imports)
def get_color_for_attention_score_1():
    """get_color_for_attention_score_0 handles score of 0.3"""

    # Setup
    sys.path = [""] + sys.path
    mask = check50.py.import_("mask.py")

    # Test
    expected = [(77, 77, 77), (76, 76, 76)]
    actual = mask.get_color_for_attention_score(0.3)

    if actual not in expected:
        raise check50.Mismatch(str(expected[0]), str(actual))


@check50.check(imports)
def get_color_for_attention_score_2():
    """get_color_for_attention_score_0 handles score of 0.8"""

    # Setup
    sys.path = [""] + sys.path
    mask = check50.py.import_("mask.py")

    # Test
    expected = (204, 204, 204)
    actual = mask.get_color_for_attention_score(0.8)

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))


@check50.check(imports)
def get_color_for_attention_score_3():
    """get_color_for_attention_score_0 handles score of 1"""

    # Setup
    sys.path = [""] + sys.path
    mask = check50.py.import_("mask.py")

    # Test
    expected = (255, 255, 255)
    actual = mask.get_color_for_attention_score(1)

    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))