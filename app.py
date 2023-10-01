from flask import Flask, render_template, request
from metaphor_python import Metaphor
from bs4 import BeautifulSoup

app = Flask(__name__)
metaphor = Metaphor("625585c3-ae21-409c-bfca-dbd9a3794e27")

def strip_html_tags(text):
    """Utility function to strip HTML tags from a string."""
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

@app.route('/', methods=['GET', 'POST'])
def index():
    suggestions = []
    content = ""

    if request.method == 'POST':
        user_input = request.form['story_start']
        
        # Search for relevant articles based on user input
        search_response = metaphor.search(user_input, num_results=5)

        for result in search_response.results:
            # Append both the title and the URL to the suggestions list
            suggestions.append({
                'title': result.title,
                'url': result.url,
                'id': result.id  # store the ID as well
            })

        # Assume you want the content for the first result (this can be changed as needed)
        if suggestions:
            contents_response = metaphor.get_contents([suggestions[0]['id']])  # use the ID, not the URL
            if contents_response.contents:
                content_text = strip_html_tags(contents_response.contents[0].extract)
                content = (content_text[:300] + '...') if len(content_text) > 300 else content_text

    return render_template('storytelling.html', suggestions=suggestions, content=content)


if __name__ == '__main__':
    app.run(debug=True)
