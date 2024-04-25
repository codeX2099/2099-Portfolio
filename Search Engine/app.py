import pandas as pd
from flask import Flask, render_template, request

# Load the dataset
df = pd.read_csv("Models/Output_Result_V2.csv")

# Fill NaN values in 'Movies&WebSeries' column with an empty string
df['name'].fillna('', inplace=True)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_text = request.form.get("search_text")
        if search_text:
            # Filter the DataFrame to find matches
            filtered_df = df[df['name'].str.contains(search_text, case=False, na=False)]
            results = []
            for idx, row in filtered_df.iterrows():
                # Get the name, numeric ID, and content up to 5 lines
                name = row['name']
                num_id = idx
                results.append((name, num_id))
            return render_template("results.html", search_text=search_text, results=results)
        else:
            return render_template("results.html", search_text="Nothing", results=None)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
