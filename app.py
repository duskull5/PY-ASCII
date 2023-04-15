from flask import Flask, render_template, request
import pyfiglet

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    fonts = pyfiglet.FigletFont.getFonts()
    selected_font = 'standard'

    if request.method == 'POST':
        text = request.form.get('text', '')
        selected_font = request.form.get('font', 'standard')
        figlet = pyfiglet.Figlet(font=selected_font)
        result = figlet.renderText(text)

    return render_template('index.html', result=result, fonts=fonts, selected_font=selected_font)

if __name__ == '__main__':
    app.run(debug=True)
