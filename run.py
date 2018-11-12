from flask import Flask, abort, render_template, url_for

app = Flask(__name__)

@app.route('/')
def view_index():
    return render_template('pages/index.htm.j2', page_id='view_index')

@app.route('/widgets')
def view_widgets():
    return render_template('pages/widgets.htm.j2', page_id='view_widgets')

@app.route('/bootcom')
def view_bootcom():
    return render_template('pages/bootstrap-components.htm.j2', page_id='view_bootcom')

@app.route('/cards')
def view_cards():
    return render_template('pages/cards.htm.j2', page_id='view_cards')

@app.route('/charts')
def view_charts():
    return render_template('pages/charts.htm.j2', page_id='view_charts')

@app.route('/form_fromcom')
def view_fromcom():
    return render_template('pages/form-components.htm.j2', page_id='view_fromcom')


@app.route('/form_custom')
def view_custom():
    return render_template('pages/form_custom_elements.htm.j2', page_id='view_custom')

@app.route('/form_sample')
def view_samples():
    return render_template('pages/form_samples.htm.j2', page_id='view_samples')

@app.route('/form_notifications')
def view_notifications():
    return render_template('pages/form_notifications.htm.j2', page_id='view_notifications')
    

@app.route('/table_basic')
def view_basic():
    return render_template('pages/table_basic.htm.j2', page_id='view_basic')


@app.route('/table_data')
def view_data():
    return render_template('pages/table_data.htm.j2', page_id='view_data')



@app.route('/page_blank')
def view_blank():
    return render_template('pages/page_blank.htm.j2', page_id='view_blank')

@app.route('/page_calendar')
def view_calendar():
    return render_template('pages/page_calendar.htm.j2', page_id='view_calendar')

@app.route('/page_invoice')
def view_invoice():
    return render_template('pages/page_invoice.htm.j2', page_id='view_invoice')

@app.route('/page_mailbox')
def view_mailbox():
    return render_template('pages/page_mailbox.htm.j2', page_id='view_mailbox')

@app.route('/page_error')
def view_error():
    return render_template('pages/page_error.htm.j2', page_id='view_error')

@app.route('/page_user')
def view_user():
    return render_template('pages/page_user.htm.j2', page_id='view_user')


if __name__ == '__main__':
    app.run(debug=True)