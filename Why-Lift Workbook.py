import marimo

__generated_with = "0.10.7"
app = marimo.App(
    width="medium",
    layout_file="layouts/Why-Lift Workbook.slides.json",
)


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
    mo.md(r"""## Code""")
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
    mo.md(r"""## Tests""")
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


if __name__ == "__main__":
    app.run()