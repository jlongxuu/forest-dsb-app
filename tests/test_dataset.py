import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.dataset import load_train_all, load_test


# tests/test_dataset.py
from src.dataset import load_train_all, load_test

def test_load_train_all_has_rows():
    df = load_train_all()
    assert len(df) > 0

def test_load_test_has_rows():
    df = load_test()
    assert len(df) > 0

