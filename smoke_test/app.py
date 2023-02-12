from pathlib import Path
import pandas
from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.output_table("table"),
)


def server(input, output, session):
    @output
    @render.table
    def table():
        infile = Path(__file__).parent / "Posit-Smoke-Test.csv"
        df = pandas.read_csv(infile).replace('\\n', ' ', regex=True)
        return df


app = App(app_ui, server)

