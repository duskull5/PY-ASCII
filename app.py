from flask import Flask, render_template, request, jsonify
import pyfiglet
import random

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

@app.route('/generate_ascii', methods=['POST'])
def generate_ascii():
    text = request.form.get('text', '')
    selected_font = request.form.get('font', 'standard')
    figlet = pyfiglet.Figlet(font=selected_font)
    result = figlet.renderText(text)
    return result

@app.route('/font_suggestions', methods=['POST'])
def font_suggestions():
    num_suggestions = 3
    text = request.form.get('text', '')
    fonts = pyfiglet.FigletFont.getFonts()
    suggested_fonts = random.sample(fonts, num_suggestions)

    results = []
    for font in suggested_fonts:
        figlet = pyfiglet.Figlet(font=font)
        result = figlet.renderText(text)
        results.append({"font": font, "result": result})

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
