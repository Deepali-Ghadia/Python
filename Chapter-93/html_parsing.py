# Beautiful Soup is a Python library for pulling data out of HTML and XML files.
# Use SELECT() method to find multiple elements and select_one() to find a single element

from bs4 import BeautifulSoup

data = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Div tag in HTML</title>

    <style>
        .main-div{
            background-color: aquamarine;
            padding: 20px;
        }

        .sub-div{
            background-color: teal;
            margin: 20px;
            padding: 10px;
            color: whitesmoke;
        }
    </style>

</head>
<body>
    <h2>Implementing div tag in HTML</h2>
    <div class="main-div">
        <div class="sub-div">
            <p>This is the first paragraph inside sub-div tag.</p>
        </div>
        <div class="sub-div">
            <p>This is the second paragraph inside sub-div tag.</p>
        </div>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(data, "html.parser")
for item in soup.select("div.sub-div"):
    print(item)
# gives all the div elements that belong to sub-div class 

