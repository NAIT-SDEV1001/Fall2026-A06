# Using Jupyter Notebooks with Pandas Fundamentals


## Why is this important?

A lot of data analysis and data science is done in Jupyter Notebooks. Pandas is one of the most popular libraries for data manipulation and analysis in Python. Combining Jupyter Notebooks with Pandas allows for interactive data exploration and visualization, making it easier to understand and communicate insights from data.

In future courses you might use a platform like google colab or a jupyterhub instance to run notebooks in the cloud. But it's also useful to know how to set up and run Jupyter Notebooks on your own machine.

## What are we going to do?

Install Jupyter and Pandas in a virtual environment, and create a simple notebook that uses Pandas to analyze some data.

## Steps

### 1. Create a virtual environment and install jupyter and pandas

1. create the virtual environment, and activate it:
```bash
python -m venv ./venv
.\venv\Scripts\activate # Or source ./venv/bin/activate on macOS/Linux
```
2. install jupyter and pandas:
```bash
pip install jupyter pandas
```
3. Save the dependencies to a requirements file:
```bash
pip freeze > requirements.txt
```

### 2. Start the Jupyter Notebook server

This is going to be a local server, that we're going to leave running while we work with our notebooks.

```bash
jupyter notebook
```
This command will open a new tab in your web browser, showing the Jupyter Notebook interface.
- This interface allows you to create, open, and manage notebooks.
- The server will keep running in your terminal until you stop it (Ctrl+C).

The output of the command will look something like this:
```
[I 2025-10-30 15:53:01.821 ServerApp] Extension package jupyter_lsp took 0.4615s to import
... removed for brevity ...
[C 2025-10-30 15:53:08.423 ServerApp]
    To access the server, open this file in a browser:
        file:///C:/Users/dmouris/AppData/Roaming/jupyter/runtime/jpserver-22644-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/tree?token=24a6388ea60038814d52a16a492093273f84408b37da5f00
        http://127.0.0.1:8888/tree?token=24a6388ea60038814d52a16a492093273f84408b37da5f00```
```

The jupyter interface should open automitcally and look a bit like this:
![Jupyter Notebook Interface](images/jupyter_interface.png)

### 3. Create a new notebook in jupyter

1. In the Jupyter interface, click on "New" and select "Python 3" to create a new notebook.
Here's where it is located:
![Create New Notebook](images/create_new.png)

2. This should create a new notebook with an empty code cell. Rename the file to `first_notebook` by clicking on the title at the top.
It should look like this:
![Rename Notebook](images/new_notebook.png)

3. Inside of these code cells you can write and execute Python code interactively.
Note: you can also change these to markdown cells for text and documentation.
In the first cell let's just do a print statement to see that everything is working:
```python
print("Hello, Jupyter with Pandas!")
```
Execute the cell by pressing Shift+Enter. You should see the output below the cell.

### 4. Use Pandas in the notebook and use some data.

Pandas is a powerful library, here's a link to the documentation: https://pandas.pydata.org/docs/

For this example we're going to load data from the city of edmonton's open data portal about current property assessments. To get the [most recent data go here](https://data.edmonton.ca/City-Administration/Property-Assessment-Data-Current-Calendar-Year-/q7d6-ambg/about_data) and click export -> CSV to download the data.

If you just want to following along without downloading the data, you can use the csv in the `data` folder in this repo.
1. First, import pandas at the top of your notebook:
```python
import pandas as pd
```
2. Next, load the CSV data into a pandas DataFrame. Adjust the file path as necessary:
```python
property_data = pd.read_csv('data/Property_Assessment_Data_(Current_Calendar_Year)_20251030.csv')
```

The `property_data` is a variable that hold what's called a `DataFrame`, which is a table-like data structure in pandas. We're going to take a look at the docs for `DataFrame` so we can see some stuff we can do with it.

3. Now you can explore the data. For example, display the first few rows:
```python
property_data.head()
```

Note do this with seperate cells in the new notebook (you can add new cells with the + button in the toolbar, or by pressing B in command mode), there's also an you can refer to the [appendix](#appendix-handy-jupyter-shortcuts) for some useful shortcuts.

### 5. Let's take a look at some operations that we can do with our pandas `DataFrame`

For each of the following cells we're going to create a new cell in the notebook and run the code to see the output

1. Get a summary of the DataFrame:
```python
property_data.info()
```
2. Let's how many rows and columns we have:

```python
property_data.shape
```
This will return a tuple with the number of rows and columns.

3. Let's get some basic statistics about the numerical columns:
```python
property_data.describe()
```
This is going to give us count, mean, std, min, max, and quartiles for all the numerical columns, which is super useful for getting a quick overview of the data.

4. Let's take a look at all of the neighbourhoods in the data:
```python
property_data["Neighbourhood"].unique()
```
This is going list all of the unique values in the "Neighbourhood" column.

### 6. Let's filter and sort the data to a specific neighborhood

For each of the following cells we're going to create a new cell in the notebook and run the code to see the output

1. Let's say we want to filter the data to see all properties in a specific neighborhood, for example "Downtown":
```python
downtown_properties = property_data[property_data['Neighbourhood'] == 'DOWNTOWN']
print(F"Number of properties in downtown {downtown_properties.shape[0]}")

downtown_properties.head()
```

2. Let's sort the downtown properties by assessed value in descending order:
```python
sorted_downtown = downtown_properties.sort_values(by='Assessed Value', ascending=False)
sorted_downtown.head()
```

3. Let's display the top 10 most expensive properties in downtown:
```python
print(sorted_downtown[:10])
```
This is going to show us the top 10 most expensive properties in downtown Edmonton based on the assessed value.
Note: the data isn't that nice to look at so let's just take a look at few columns

4. Let's display only the Address, Assessed Value, and Property Type columns for the top 10 most expensive properties in downtown:
```python
print(sorted_downtown[['House Number', 'Street Name',  'Assessed Value']][:10])
```

### 7. Grouping and aggregating the data

Often we want to summarize data by category — for example, "what's the average assessed value in each neighbourhood?" or "how many properties are in each ward?". Pandas gives us two main tools for this: `value_counts()` and `groupby()`.

- **`value_counts()`** works on a single column and just counts how often each unique value appears. It's a quick shortcut when all you want is the frequency of each category.
- **`groupby()`** is more general: it splits the data into groups based on a column, then lets you apply *any* aggregation (mean, sum, count, min, max, etc.) on one or more other columns. This is the "split-apply-combine" pattern that you'll see a lot of in data analysis.

For each of the following cells we're going to create a new cell in the notebook and run the code to see the output

1. Let's count how many properties are in each neighbourhood using `value_counts()`:
```python
property_data['Neighbourhood'].value_counts()
```
This returns a Series with neighbourhood names sorted from most properties to fewest. Notice that we didn't have to tell pandas how to count — it figures that out for us because `value_counts()` is purpose-built for this.

> **Note on display truncation:** You'll see that pandas only shows the first 5 and last 5 rows with `...` in between, even though the `Length: 406` at the bottom tells you there are 406 neighbourhoods in the result. That `...` is purely a *display* shortcut — the data is all still there in the Series. Pandas does this for any output longer than ~60 rows by default. If you want to see more rows, you can:
> - Use `.head(50)` or `.tail(50)` to look at a larger chunk
> - Call `.to_string()` to print the whole thing without truncation: `print(property_data['Neighbourhood'].value_counts().to_string())`
> - Temporarily change the display limit with `pd.set_option('display.max_rows', None)` (and reset with `pd.reset_option('display.max_rows')` when you're done)
>
> This same truncation applies to almost every pandas display — DataFrames, `groupby()` results, everything.

2. Now let's get the average assessed value per neighbourhood using `groupby()`:
```python
avg_value_by_neighbourhood = property_data.groupby('Neighbourhood')['Assessed Value'].mean()
print(avg_value_by_neighbourhood)
```
Here we're grouping by `Neighbourhood`, then taking the `mean()` of the `Assessed Value` column within each group. Compare this with `value_counts()` above — `groupby()` required us to pick both the column to group on *and* the column to aggregate, and to choose the aggregation (`.mean()`). That's the tradeoff: more flexibility, more to specify.

3. We can sort the result to find the neighbourhoods with the highest average property values:
```python
avg_value_by_neighbourhood.sort_values(ascending=False).head(10)
```

4. `groupby()` also lets you apply multiple aggregations at once with `.agg()`:
```python
property_data.groupby('Ward')['Assessed Value'].agg(['mean', 'min', 'max', 'count'])
```
This returns a DataFrame with one row per ward and one column for each aggregation — useful when you want to compare summary statistics side by side.

## Exercises

Using what you've learned so far, try to answer the following questions by creating new cells in your notebook:

1. How many properties are there in the
"ELLERSLIE" neighborhood?

2. What is the average assessed value of properties in the "KINGSWAY" neighborhood?

3. Get the top 3 most expensive properties in the "EDMONTON SOUTH WEST" neightbourhood.

4. Using `value_counts()`, find which **ward** has the most properties.

5. Using `groupby()`, calculate the average assessed value per **ward**, then sort the result from highest to lowest.

## Summary

In this lesson we covered how to set up a virtual environment, install Jupyter and Pandas, and create a simple Jupyter Notebook to explore and analyze data using Pandas.

## Appendix: handy jupyter shortcuts
| Command                     | Description                                      |
| --------------------------- | ------------------------------------------------ |
| `Shift + Enter`             | Run the current cell and move to the next cell   |
| `Ctrl + Enter`              | Run the current cell and stay in it              |
| `Alt + Enter`               | Run the current cell and insert a new one below  |
| `Esc`                       | Enter command mode (blue border)                 |
| `Enter`                     | Enter edit mode (green border)                   |
| `A` (in command mode)       | Insert a new cell **above**                      |
| `B` (in command mode)       | Insert a new cell **below**                      |
| `D, D` (press D twice)      | Delete the selected cell                         |
| `Z`                         | Undo the last cell deletion                      |
| `M`                         | Change cell to **Markdown**                      |
| `Y`                         | Change cell to **Code**                          |
| `L`                         | Toggle line numbers in the current cell          |
| `Shift + M`                 | Merge selected cells                             |
| `Ctrl + S`                  | Save the notebook                                |
| `0, 0` (press 0 twice)      | Restart the kernel                               |
| `I, I` (press I twice)      | Interrupt the kernel                             |
| `Ctrl + /`                  | Toggle comment on selected lines (in edit mode)  |
| `Ctrl + Shift + -`          | Split a cell at the cursor                       |
| `Tab`                       | Autocomplete or show function signature          |
| `Shift + Tab`               | Show tooltip/documentation for an object         |
| `!command`                  | Run a shell command (e.g. `!ls`, `!pip install`) |
| `%time`                     | Measure execution time of a single line of code  |
| `%%time`                    | Measure execution time of a whole cell           |
| `%who`                      | List all variables in the namespace              |
| `%whos`                     | Detailed list of variables with types and sizes  |
| `%pwd`, `%cd`, `%ls`        | File system navigation commands                  |
| `%matplotlib inline`        | Display plots inline (common for matplotlib)     |
| `?object` or `help(object)` | Show documentation for an object                 |
