import os
import pandas as pd

# Specify the output folder
output_folder = "templates"

# Delete previous version of homepage.html if it exists in the new location
output_file_path = os.path.join(output_folder, "homepage.html")
if os.path.exists(output_file_path):
    os.remove(output_file_path)

# Load DataFrame from CSV file
df = pd.read_csv("output.csv")

# Replace "nan" entries with "unknown"
df = df.fillna("Unknown")

# Concatenate text within each CSV row to enable search across different elements
df["concatenated_text"] = df.apply(lambda row: " ".join(row.values.astype(str)), axis=1)

# Convert DataFrame to HTML
html_results = ""
for index, row in df.iterrows():
    html_results += f"""
    <div class="search-result">
        <h3>{row['project_title']}</h3>
        <p>{row['university_name']}</p>
        <p>{row['supervisors_info']}</p>
        <p>Application Deadline: {row['applications_info']}</p>
        <p><a href="https://www.findaphd.com/{row['project_url']}" target="_blank"><button>More Info</button></a></p>
    </div>
    """

# JavaScript code
js1 = """
<script>
    window.onload = function() {
        var resultsContainer = document.getElementById("resultsContainer");
        // Hide the resultsContainer initially
        resultsContainer.style.display = 'none';
"""
js2 = """
        function searchResults() {
            var input, filter, results, i, rowText;
            input = document.getElementById("searchInput");
            filter = input.value.toLowerCase();
            results = resultsContainer.getElementsByClassName("search-result");

            for (i = 0; i < results.length; i++) {
                rowText = results[i].textContent || results[i].innerText;
                // Check if all search terms are present in any order within the row
                var allTermsPresent = true;
                var searchTerms = filter.split(' ');
                for (var term of searchTerms) {
                    if (!rowText.toLowerCase().includes(term)) {
                        allTermsPresent = false;
                        break;
                    }
                }
                if (allTermsPresent) {
                    results[i].style.display = "";
                } else {
                    results[i].style.display = "none";
                }
            }

            // Hide resultsContainer if user has not entered anything
            if (input.value.trim() !== '') {
                resultsContainer.style.display = 'block';
            } else {
                resultsContainer.style.display = 'none';
            }
        }
"""
js3 = """
        // Event listener for searchResults function on input change
        document.getElementById('searchInput').addEventListener('input', searchResults);
    };
"""

js4 = """
        document.getElementById("searchForm").addEventListener("submit", function(event) {
            event.preventDefault(); // Prevent the default form submission behavior

            // Get the entered search query
            var searchQuery = document.getElementById("searchQuery").value;
        });
</script>
"""

# HTML content for the whole webpage
html_page = f"""
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
    <meta name="description" content="" />
    <meta name="author" content="" />
    <title>PhFree</title>
    <!-- Favicon-->
    <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Nabla&display=swap" rel="stylesheet">
    <!-- Core theme CSS (includes Bootstrap)-->
    <link rel="stylesheet" type="text/css" href="/static/styles.css">
    <style>
        /* Applying Nabla font to the navbar-brand */
        .navbar-brand {{
            font-family: 'Nabla', sans-serif;
        }}

        .nabla-font {{
            font-family: 'Nabla', sans-serif;
        }}

        #resultsContainer {{
            display: none; /* Hide resultsContainer initially */
        }}

    .search-result {{
      margin-bottom: 20px;
    }}
    button {{
      padding: 5px 10px;
      background-color: #003366;
      color: white;
      border: none;
      border-radius: 3px;
      cursor: pointer;
    }}

    .navbar-brand {{
            font-family: 'Nabla', sans-serif;
        }}

        .nabla-font {{
    font-family: 'Nabla', sans-serif;
}}

.search-result {{
  margin-bottom: 20px;
  padding-left: 50px;
  padding-right: 50px;
  padding: 15px;
  border: 1px solid #ccc;
  border-radius: 20px;
}}

#resultsContainer {{
  padding: 20px;
}}


h3 {{
    font-size: 16;
}}
  </style>
    <!-- JavaScript code -->
    {js1}
    {js2}
    {js3}
    {js4}
</head>
<body>
    <!-- Responsive navbar-->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="/">PhFree</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                    <li class="nav-item"><a class="nav-link active" aria-current="page" href="/">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="/about">About</a></li>
                    <li class="nav-item"><a class="nav-link" href="/team">Team</a></li>
                    <li class="nav-item"><a class="nav-link" href="/contact">Contact</a></li>
                    <li class="nav-item dropdown">
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <!-- Page content-->
    <div class="container">
        <div class="text-center mt-5">
            <h1>Welcome to <span class="nabla-font">PhFree</span></h1>
            <p class="lead">It’s 2023. You shouldn’t be paying for a PhD.</p>
            <p>This project was made for <a href="https://cs50.harvard.edu/college/2023/fall/">CS50</a>, by Elissa Day and Asker Kurt-Elli.</p>
            <p>Type in a keyword below to find a PhD opportunity.</p>

            <br>

            <!-- Search bar -->
            <form id="searchForm">
                <label for="searchInput">Search:</label>
                <input type="text" id="searchInput" oninput="searchResults()" onload="initialhide()" placeholder="Keywords">
            </form>

            <br>
            <br>

            <div id="resultsContainer">
                {html_results}
            </div>
        </div>
    </div>

    <br>
    <br>
    <br>
    <br>
    <br>
    <br>

    <div class="container">
        <footer class="py-3 my-4">
            <p class="text-center text-muted">© 2023 Elissa Day and Asker Kurt-Elli </p>
        </footer>
    </div>

    <!-- Bootstrap core JS-->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
    <!-- Core theme JS-->
    <script src="js/scripts.js"></script>
</body>
</html>
"""

# Save the HTML page to a file in the "templates" subfolder
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

output_file_path = os.path.join(output_folder, "homepage.html")
with open(output_file_path, "w") as f:
    f.write(html_page)
