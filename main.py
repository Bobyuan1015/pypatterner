import pandas as pd

from src.compare import get_template

if __name__ == "__main__":
    test = []

    df = pd.read_csv('data/set.csv')

    templates = get_template(df['content'].to_list())
    print('Templates:',templates)


