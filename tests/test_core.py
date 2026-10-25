"""
test_core.py - Main test
"""
import marimo

__generated_with = "0.25.2"

app = marimo.App(
    width="medium",
    app_title="Test",
    html_head_file="",
    auto_download=["html"],
    sql_output="pandas",
)

@app.cell
def _():
    import marimo as mo
    import jaimo as jm

    return (mo, jm)

@app.cell
def _():
    # f-function test
    print(jm.f("(x+5)**2 + (y+3)**2", x=1, y=1))

    # zero-function test
    print(jm.num.zero("(x-200/7)**3 - 100", 1., 500., 0.0001, 2))
    return

if __name__ == "__main__":
    app.run()