from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
Bootstrap(app)

morse_cyr = {'А': '*-', 'Б': '-***', 'В': '*−−', 'Г': '−−*', 'Д': '−**', 'Е': '*', 'Ж': '***−', 'З': '−−**',
             'И': '**', 'Й': '*−−−', 'К': '−*−', 'Л': '*−**', 'М': '−−', 'Н': '−*', 'О': '−−−', 'П': '*−−*',
             'Р': '*−*', 'С': '***', 'Т': '−', 'У': '**−', 'Ф': '**−*', 'Х': '****', 'Ц': '−*−*', 'Ч': '−−−*',
             'Ш': '−−−−', 'Щ': '−−*−', 'Ъ': '−−*−−', 'Ы': '−*−−', 'Ь': '−**−', 'Э': '**−**', 'Ю': '**−−', 'Я': '*−*−'}

morse_lat = {'A': '*−', 'B': '−***', 'W': '*−−', 'G': '−−*', 'D': '−**',
             'E': '*', 'V': '***−', 'Z': '−−**', 'I': '**', 'J': '*−−−', 'K': '−*−', 'L': '*−**', 'M': '−−', 'N': '−*',
             'O': '−−−', 'P': '*−−*', 'R': '*−*', 'S': '***', 'T': '−', 'U': '**−', 'F': '**−*', 'H': '****',
             'C': '−*−*', 'Ö': '−−−*', 'Q': '−−*−', 'Ñ': '−−*−−', 'Y': '−*−−', 'X': '−**−', 'É': '**−**', 'Ü': '**−−',
             'Ä': '*−*−'}

morse_arm = {'Ա': '*−', 'Բ': '-***', 'Գ': '--*', 'Դ': '-**', 'Ե': '*', 'Է': '*', 'Զ': '--**', 'Ը': '-*--',
             'Թ': '--*--', 'Ժ': '***-', 'Ի': '**', 'Լ': '*-**', 'Խ': '****', 'Ծ': '*--*-*', 'Կ': '-*-', 'Հ': '*---*',
             'Ձ': '-**-*', 'Ղ': '--*-', 'Ճ': '*-*-*', 'Մ': '--', 'Յ': '*---', 'Ն': '-*', 'Շ': '----', 'Ո': '---',
             'Օ': '---', 'Չ': '---*', 'Պ': '*--*', 'Ջ': '-*-**', 'Ռ': '*-**-*', 'Ս': '***', 'Վ': '*--', 'Տ': '-',
             'Ր': '*-*', 'Ց': '-*-*', 'ՈՒ': '**-', 'Փ': '**-*-', 'Ք': '-**-', 'Ֆ': '**-*'}

morse_grec = {'Α': '*-', 'Β': '-***', 'Γ': '--*', 'Δ': '-**', 'Ε': '*', 'Ζ': '--**', 'Η': '****', 'Θ': '-*-*',
              'Ι': '**', 'Κ': '-*-', 'Λ': '*-**', 'Μ': '--', 'Ν': '-*', 'Ξ': '-**-', 'Ο': '---', 'Π': '*--*',
              'Ρ': '*-*', 'Σ': '***', 'Τ': '-', 'Υ': '-*--', 'Φ': '**-*', 'Χ': '----', 'Ψ': '--*-', 'Ω': '*--'}

morse_ivr = {'א': '*-', 'ב': '-***', 'ג': '--*', 'ד': '-**', 'ה': '---', 'ו': '*', 'ז': '--**', 'ח': '****',
             'ט': '**-', 'י': '**', 'כ': '-*-', 'ל': '*-**', 'מ': '--', 'נ': '-*', 'ס': '-*-*', 'ע': '*---',
             'פ': '*--*', 'צ': '*--', 'ק': '--*-', 'ר': '*-*', 'ש': '***', 'ת': '-'}

morse_arab = {'ا': '*-', 'ب': '-***', 'ت': '-', 'ث': '-*-*', 'ج': '*---', 'ح': '****', 'خ': '---', 'د': '-**',
              'ذ': '--**', 'ر': '*-*', 'ز': '---*', 'س': '***', 'ش': '----', 'ص': '-**-', 'ض': '***-', 'ط': '**-',
              'ظ': '-*--', 'ع': '*-*-', 'غ': '--*', 'ف': '**-*', 'ق': '--*-', 'ك': '-*-', 'ل': '*-**', 'م': '--',
              'ن': '-*', 'ه': '**-**', 'و': '*--', 'ي': '**', 'ﺀ': '*'}

morse_pers = {'ا': '*-', 'ب': '-***', 'پ': '*--*', 'ت': '-', 'ث': '-*-*', 'ج': '*---', 'چ': '---*', 'ح': '****',
              'خ': '-**-', 'د': '-**', 'ذ': '***-', 'ر': '*-*', 'ز': '--**', 'ژ': '--*', 'س': '***', 'ش': '----',
              'ص': '*-*-', 'ض': '**-**', 'ط': '**-', 'ظ': '-*--', 'ع': '---', 'غ': '**--', 'ف': '**-*', 'ق': '***---',
              'ک': '-*-', 'گ': '--*-', 'ل': '*-**', 'م': '--', 'ن': '-*', 'و': '*--', 'ه': '*', 'ی': '**'}

morse_jap_kat = {'イ': '*-', 'チ': '**-*', 'ヨ': '--', 'ラ': '***', 'ヤ': '*--', 'ア': '--*--', 'ヱ': '*--**', '゛': '**',
                 'ロ': '*-*-', 'リ': '--*', 'タ': '-*', 'ム': '-', 'マ': '-**-', 'サ': '-*-*-', 'ヒ': '--**-', '゜': '**--*',
                 'ハ': '-***', 'ヌ': '****', 'レ': '---', 'ウ': '**-', 'ケ': '-*--', 'キ': '-*-**', 'モ': '-**-*', 'ニ': '-*-*',
                 'ル': '-*--*', 'ソ': '---*', 'ヰ': '*-**-', 'フ': '--**', 'ユ': '-**--', 'セ': '*---*', 'ホ': '-**',
                 'ヲ': '*---', 'ツ': '*--*', 'ノ': '**--', 'コ': '----', 'メ': '-***-', 'ス': '---*-', 'ヘ': '*', 'ワ': '-*-',
                 'ネ': '--*-', 'オ': '*-***', 'エ': '-*--', 'ミ': '**-*-', 'ン': '*-*-*', 'ト': '**-**', 'カ': '*-**',
                 'ナ': '*-*', 'ク': '***-', 'テ': '*-*--', 'シ': '--*-*'}

morse_jap_hir = {'い': '*-', 'ち': '**-*', 'よ': '--', 'ら': '***', 'や': '*--', 'あ': '--*--', 'ゑ': '*--**', '゛': '**',
                 'ろ': '*-*-', 'り': '--*', 'た': '-*', 'む': '-', 'ま': '-**-', 'さ': '-*-*-', 'ひ': '--**-', '゜': '**--*',
                 'は': '-***', 'ぬ': '****', 'れ': '---', 'う': '**-', 'け': '-*--', 'き': '-*-**', 'も': '-**-*', 'に': '-*-*',
                 'る': '-*--*', 'そ': '---*', 'ゐ': '*-**-', 'ふ': '--**', 'ゆ': '-**--', 'せ': '*---*', 'ほ': '-**',
                 'を': '*---', 'つ': '*--*', 'の': '**--', 'こ': '----', 'め': '-***-', 'す': '---*-', 'へ': '*', 'わ': '-*-',
                 'ね': '--*-', 'お': '*-***', 'え': '-*--', 'み': '**-*-', 'ん': '*-*-*', 'と': '**-**', 'か': '*-**',
                 'な': '*-*', 'く': '***-', 'て': '*-*--', 'し': '--*-*'}

symbols = {'1': '*−−−−', '2': '**−−−', '3': '***−−', '4': '****−', '5': '*****', '6': '−****', '7': '−−***',
           '8': '−−−**', '9': '−−−−*', '0': '−−−−−', '.': '******', ',': '*−*−*−', ';': '−*−*−*', '"': '*−**−*',
           '—': '−****−', '/': '−**−*', '_': '**−−*−', '?': '**−−**', '!': '−−**−−', ':': '−−−***', '(': '−*−−*',
           ')': '−*−−*−', '&': '*−***', '=': '−***−', '$': '***−**−', '@': '*−−*−*', ' ': '*******', '’': '*----*'}


def language(lang):
    if lang == 'Cyrillic':
        morse = morse_cyr.copy()
        morse.update(symbols)
        return morse
    elif lang == 'Latin':
        morse = morse_lat.copy()
        morse.update(symbols)
        return morse
    elif lang == 'Armenian':
        morse = morse_arm.copy()
        morse.update(symbols)
        return morse
    elif lang == 'Greek':
        morse = morse_grec.copy()
        morse.update(symbols)
        return morse
    elif lang == 'Hebrew':
        morse = morse_ivr.copy()
        morse.update(symbols)
        return morse
    elif lang == 'Arab':
        morse = morse_arab.copy()
        morse.update(symbols)
        return morse
    elif lang == 'Persian':
        morse = morse_pers.copy()
        morse.update(symbols)
        return morse
    elif lang == 'Japanese(Katakana)':
        morse = morse_jap_kat.copy()
        morse.update(symbols)
        return morse
    elif lang == 'Japanese(Hiragana)':
        morse = morse_jap_hir.copy()
        morse.update(symbols)
        return morse


class ToMorseForm(FlaskForm):
    select_lang = SelectField('Choose a Language', choices=['Cyrillic', 'Latin', 'Armenian', 'Greek', 'Hebrew', 'Arab',
                                                            'Persian', 'Japanese(Katakana)', 'Japanese(Hiragana)'])
    text = StringField('Source Text', validators=[DataRequired()])
    morse_text = TextAreaField('Morse Code')
    convert = SubmitField('Convert')


class ConvertMorseForm(FlaskForm):
    morse_text = StringField('Morse Code (Use characters: - *)', validators=[DataRequired()])
    select_lang = SelectField('Choose a Language', choices=['Cyrillic', 'Latin', 'Armenian', 'Greek', 'Hebrew', 'Arab',
                                                            'Persian', 'Japanese(Katakana)', 'Japanese(Hiragana)'])
    convert_text = TextAreaField('Convert Text')
    convert = SubmitField('Convert')


@app.route('/', methods=['POST', 'GET'])
def home():
    to_morse = True
    form = ToMorseForm()
    if form.validate_on_submit():
        upper_text = form.text.data.upper()
        morse_data = language(form.select_lang.data)
        morse_res = ''
        for letter in upper_text:
            for key in morse_data:
                if key == letter:
                    morse_res += f'{morse_data[key]} '
            if letter not in morse_data:
                flash('These letters are not available in the selected language, change the language!')
                break
        form.morse_text.data = morse_res
        return render_template('index.html', form=form, to_morse=to_morse)
    return render_template('index.html', form=form, to_morse=to_morse)


@app.route('/morse', methods=['POST', 'GET'])
def morse():
    to_morse = False
    form = ConvertMorseForm()
    if form.validate_on_submit():
        split_text = form.morse_text.data.strip().split(' ')
        morse_data = language(form.select_lang.data)
        morse_res = ''
        for symbol in split_text:
            for key in morse_data:
                if morse_data[key] == symbol:
                    morse_res += key
        try:
            form.convert_text.data = morse_res[0].upper() + morse_res[1:].lower()
        except IndexError:
            flash('Please, use these characters: - *')
        return render_template('index.html', form=form, to_morse=to_morse)
    return render_template('index.html', form=form, to_morse=to_morse)


if __name__ == '__main__':
    app.run(debug=True)
