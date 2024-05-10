import pandas

def load_data():
    FILE_PATH = "data/data.csv"
    df = pandas.read_csv(FILE_PATH)
    return df


def get_public_orgs():
    df = load_data()
    public_df = df[df["Public?"] == 1]
    num = len(public_df)
    print("There are ", num, "public organizations.")

    return num


def revenue_per_industry():
    df = load_data()
    revenue_by_industry = df.groupby("Industry")["Revenue"].sum()
    count_by_industry = df["Industry"].value_counts()

    rev_ratio = revenue_by_industry / count_by_industry
    print(rev_ratio)

    return rev_ratio

def highest_revenue_industry():
    df = load_data()
    revenue_by_industry = df.groupby("Industry")["Revenue"].sum()
    top_revenue_industry = revenue_by_industry.idxmax()
    print("The industry with the highest revenue is ", top_revenue_industry)

    return top_revenue_industry