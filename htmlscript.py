
# Name for HTML file
htmlName = ("Company Website.html")

# HTML code for website
htmlContent = (
"""
<html>
<body>
Stay tuned for our amazing summer sale!
</body>
</html>
"""
)

# Function that creates and writes html file
def createHTML(name, content):
    file = open(name, "w")
    file.write(content)
    file.close()
    print("Operation completed.")

createHTML(htmlName, htmlContent)


