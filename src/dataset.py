import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")
OLD = DATA_DIR / "forest-dsb-external-data" / "train-set.csv"
NEW = DATA_DIR / "forest-dsb-2023-v2" / "train.csv"
TEST = DATA_DIR / "forest-dsb-2023-v2" / "test-full.csv"

def load_train_old():
    df = pd.read_csv(OLD)
    return df.set_index("Id") if "Id" in df.columns else df

def load_train_new():
    df = pd.read_csv(NEW)
    return df.set_index("Id") if "Id" in df.columns else df

def load_train_all():
    old = load_train_old()
    new = load_train_new()
    return pd.concat([old, new], ignore_index=True if "Id" not in old.index.names else False)

def load_test():
    df = pd.read_csv(TEST)
    return df.set_index("Id") if "Id" in df.columns else df

