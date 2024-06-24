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

    return rev_ratio


def highest_revenue_industry():
    df = load_data()
    revenue_by_industry = df.groupby("Industry")["Revenue"].sum()
    top_revenue_industry = revenue_by_industry.idxmax()

    return top_revenue_industry


def main():
    num_public_orgs = get_public_orgs()
    rev_per_industry = revenue_per_industry()
    highest_rev_industry = highest_revenue_industry()

    print("Number of public organizations:", num_public_orgs)
    print("Revenue per industry:")
    print(rev_per_industry)
    print("Industry with the highest revenue:", highest_rev_industry)


if __name__ == "__main__":
    main()
