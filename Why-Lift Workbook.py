import marimo

__generated_with = "0.10.9"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Why Lift Workbook

        This is the main script for the "Why Lift! 💪🤔💭" project, using _Marimo_ :3

        PmXa, 06-2024
        """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Using `pandas`""")
    return


@app.cell
def _(mo):
    mo.md(r"""### Code""")
    return


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import pandas as pd
    return mo, pd, plt


@app.cell
def _(pd):
    """ ---------------------------
    Block 1:
    Read the .xlsx database
    --------------------------- """

    def import_file(file:str) -> pd.DataFrame:
        data = pd.read_csv(file, parse_dates=["Date"])
        return data
    return (import_file,)


@app.cell
def _(pd):
    """ --------------------------------------------
    Block 2:
    Format and perform calculations on the Dataframe
    -------------------------------------------- """

    def process_data(raw_data: pd.DataFrame) -> pd.DataFrame:

        processed_data = raw_data.copy()

        # Get the days elapsed from reference
        processed_data["days"] = (raw_data["Date"] - raw_data.loc[0, "Date"]).dt.days

        # Compute the progress made
        processed_data["total_reps"] = raw_data.iloc[:, 1:].sum(axis=1)
        processed_data["progress"] = 100 * processed_data.loc[:, "total_reps"] / processed_data.loc[0, "total_reps"]

        return processed_data
    return (process_data,)


@app.cell
def _(pd, plt):
    """ --------------------------------------------
    Block 3:
    Plot the results! 😁
    -------------------------------------------- """

    def plot_data(processed_data: pd.DataFrame) -> None:

        # --------
        # Data
        # --------   

        x_data = processed_data.loc[1:,"days"]
        y_data = processed_data.loc[1:,"progress"]

        y_range = range(0, 101, 10)
        y_label = [f"{i:.0f}%" for i in y_range]

        # --------
        # Plot
        # --------

        plt.figure(figsize = (9,6))

        plt.plot(x_data, y_data,
                    "-o",
                    alpha = 0.75,
                    markeredgecolor='k')

        plt.grid(True)
        plt.xlim(0, None)
        plt.ylim(0, 100)
        plt.yticks(y_range, labels = y_label)

        plt.title("Progreso de mi rutina")
        plt.xlabel("Days")
        plt.ylabel("Progress")

        plt.show()
    return (plot_data,)


@app.cell
def _(mo):
    mo.md(r"""### Tests""")
    return


@app.cell
def _(import_file):
    """ ---------------------------------
    🚧 Importing Test Block 🚧
    --------------------------------- """

    data_file:str = "./test_data.csv"

    raw_data = import_file(data_file)
    print(raw_data)
    return data_file, raw_data


@app.cell
def _(process_data, raw_data):
    """ ---------------------------------
    🚧 Processing Test Block 🚧
    --------------------------------- """

    processed_data = process_data(raw_data)
    processed_data.head()
    return (processed_data,)


@app.cell
def _(plot_data, processed_data):
    """ ---------------------------------
    🚧 Plotting Test Block 🚧
    --------------------------------- """

    plot_data(processed_data)
    return


@app.cell
def _(mo):
    mo.md(r"""## Using just Python""")
    return


@app.cell
def _(mo):
    mo.md("""### Code""")
    return


app._unparsable_cell(
    r"""
    \"\"\" ----------------------
    Block 1:
    Read the .csv database
    ---------------------- \"\"\"

    def v_import_file(path:str) -> dict:
        try:
            with open(path, 'r', encoding='utf-8') as file:
                
        except FileNotFoundError:
            print('Raise a warning window here!')
        except Exception as e:
            print('Unknown error: f{e}')
    """,
    name="_"
)


@app.cell
def _(pd):
    """ --------------------------------------------
    Block 2:
    Format and perform calculations on the Dataframe
    -------------------------------------------- """

    def process_data(raw_data: pd.DataFrame) -> pd.DataFrame:

        processed_data = raw_data.copy()

        # Get the days elapsed from reference
        processed_data["days"] = (raw_data["Date"] - raw_data.loc[0, "Date"]).dt.days

        # Compute the progress made
        processed_data["total_reps"] = raw_data.iloc[:, 1:].sum(axis=1)
        processed_data["progress"] = 100 * processed_data.loc[:, "total_reps"] / processed_data.loc[0, "total_reps"]

        return processed_data
    return (process_data,)


@app.cell
def _(pd, plt):
    """ --------------------------------------------
    Block 3:
    Plot the results! 😁
    -------------------------------------------- """

    def plot_data(processed_data: pd.DataFrame) -> None:

        # --------
        # Data
        # --------   

        x_data = processed_data.loc[1:,"days"]
        y_data = processed_data.loc[1:,"progress"]

        y_range = range(0, 101, 10)
        y_label = [f"{i:.0f}%" for i in y_range]

        # --------
        # Plot
        # --------

        plt.figure(figsize = (9,6))

        plt.plot(x_data, y_data,
                    "-o",
                    alpha = 0.75,
                    markeredgecolor='k')

        plt.grid(True)
        plt.xlim(0, None)
        plt.ylim(0, 100)
        plt.yticks(y_range, labels = y_label)

        plt.title("Progreso de mi rutina")
        plt.xlabel("Days")
        plt.ylabel("Progress")

        plt.show()
    return (plot_data,)


@app.cell
def _(mo):
    mo.md(r"""### Tests""")
    return


@app.cell
def _(import_file):
    """ ---------------------------------
    🚧 Importing Test Block 🚧
    --------------------------------- """

    data_file:str = "./test_data.csv"

    raw_data = import_file(data_file)
    print(raw_data)
    return data_file, raw_data


@app.cell
def _(mo):
    mo.md(r"""## Building blocks""")
    return


@app.cell
def _(mo):
    mo.md(r"""### Adding new workout sessions""")
    return


@app.cell
def _(mo):
    mo.md(r"""To add a new row to the DataFrame, it seems it's more efficient to build a dictionary first, then concatenate. This also allows me to parse one date at a time, instead of re-parsing the whole `Date` column over and over:""")
    return


@app.cell
def _(pd):
    girls = {
        "Name": [
            "Abi",
            "Anna",
            "Andén",
            "Anahí"
        ],
        "Year": [
            2015,
            2010,
            2013,
            2009
        ],
        "Place": [
            "College",
            "Middle school",
            "Park",
            "Church"
        ]
    }

    df = pd.DataFrame(girls)

    print(df)
    return df, girls


@app.cell
def _(df, pd):
    new_row = {column: ('Her' if column == 'Name' else [0]) for column in df.columns.values}
    new_entry = pd.DataFrame(new_row)

    print(pd.concat([df, new_entry], ignore_index=True))
    return new_entry, new_row


if __name__ == "__main__":
    app.run()
