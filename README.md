# Forest DSB Streamlit App

Data expected at:
- `data/forest-dsb-external-data/train-set.csv`
- `data/forest-dsb-2023-v2/train.csv`
- `data/forest-dsb-2023-v2/test-full.csv`

## Run locally
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
