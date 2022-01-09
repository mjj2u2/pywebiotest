from pywebio import start_server
from pywebio.input import input, textarea, select, checkbox
from pywebio.input import radio, slider, actions, file_upload
from pywebio.input import input_group, input_update
from pywebio.output import put_row, put_column, put_code
import pywebio.output as p
from pywebio.session import set_env
import pywebio
from pywebio.output import put_text, put_markdown
from pywebio import pin


def cliceked(value):
    put_text(f'You pressed button {value}')


def show_msg():
    put_text("You clicked the notification.")


def main():
    set_env(auto_scroll_bottom=True)
    pin.put_input(name='in', label='What is your name?')

    # Put info, success, warning, error
    p.put_info('Info')
    p.put_success('Success')
    p.put_warning('Warning')
    p.put_error('Error')

    p.put_html('<h1>Head</h1><b>Bold</b>')

    p.put_link(name='URL Link', url="http://google.com", new_window=True)

    p.put_processbar(name='pbar', label='Process Bar', init=5)

    # Have to figure this out
    # p.put_loading(shape='Boarder', color='Dark')

    p.put_text("\n\nThis is a section of Python code")
    p.put_code(
        '''for _ in range(0, 100): 
        print("Hello World")''', language='Python')

    p.put_table(tdata=[[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2]], header=['a', 'b', 'c', 'd', 'e'])

    p.put_buttons(
        [dict(label='Success', value='Success', color='success'), dict(label='Fail', value='Fail', color='success')],
        onclick=cliceked)

    img = open('python.png', 'rb').read()
    p.put_image(img, width='50px')
    p.put_image('https://www.python.org/static/img/python-logo.png')

    # Put file
    # p.put_file()

    p.put_tabs([
        {'title': 'Text', 'content': 'Hello world'},
        {'title': 'Markdown', 'content': put_markdown('~~Strikethrough~~')},
        {'title': 'More content', 'content': [
            p.put_table([
                ['Commodity', 'Price'],
                ['Apple', '5.5'],
                ['Banana', '7'],
            ]),
            p.put_link('pywebio', 'https://github.com/wang0618/PyWebIO')
        ]},
    ])

    p.toast('This is a message. Hit the X to close it.', position='center', color='#2188ff', duration=0,
            onclick=show_msg)

    # Pop-up message
    p.popup('popup title', 'popup text content', size=p.PopupSize.SMALL)

    # The one above closes automatically to so the next one. This one is an example of more things you can add.
    p.popup('Popup title', [
        p.put_html('<h3>Popup Content</h3>'),
        'html: <br/>',
        p.put_table([['A', 'B'], ['C', 'D']]),
        p.put_buttons(['close_popup()'], onclick=lambda _: p.close_popup())
    ])

    put_text('Here is a grid:')
    p.put_grid([
        [put_text('A'), put_text('B'), put_text('C')],
        [None, p.span(put_text('D'), col=2, row=1)],
        [put_text('E'), put_text('F'), put_text('G')],
    ], cell_width='100px', cell_height='100px')

    put_text('Here is a span in a table.')
    p.put_table([
        ['C'],
        [p.span('E', col=2)],  # 'E' across 2 columns
    ], header=[p.span('A', row=2), 'B'])  # 'A' across 2 rows

    p.put_grid([
        [put_text('A'), put_text('B')],
        [p.span(put_text('A'), col=2)],  # 'A' across 2 columns
    ])

    put_markdown('# Examples of input from pywebio')

    # Test layouts
    put_row([
        put_column([
            put_code('A'),
            put_row([
                put_code('B1'), None,  # None represents the space between the output
                put_code('B2'), None,
                put_code('B3'),
            ]),
            put_code('C'),
        ]), None,
        put_code('D'), None,
        put_code('Now is the time for all good men to come to the aid of their country.'), None
    ])

    # you can use CSS style
    put_text('Hello').style('color: blue; font-size: 40px')

    put_row([
        put_text('hello').style('color: red'),
        # You can also use markdown
        put_markdown("# Markdown")
    ]).style('margin-top: 20px')

    # Input
    put_markdown('# Input')
    put_text('Simple input')
    text = input('Type some text')
    put_text(f'You typed: {text}')

    # Textarea
    put_markdown('# Textarea')
    put_text('I set the size to 5 rows and maximum chars as 500.')
    put_text('I also made it so that it can\'t be blank')
    text_a = textarea(label='Type in the text area', rows=5, maxlength=500, required=True,
                      help_text='Max length is 500')
    put_text(f'You typed: \n{text_a}')

    # Select
    put_markdown('# Select')
    put_text('This is a single selection, the default is Chicken.')
    put_text('Note "Fish" is disabled, so you can\'t select it')
    drop = select(label='Make your selection', options=[
        {'label': 'Hamburger', 'value': 'hamburger', 'selected': False},
        {'label': 'Chicken', 'value': 'chicken', 'selected': True},
        {'label': 'Fish', 'value': 'fish', 'disabled': True},
        {'label': 'Fries', 'value': 'fries', 'selected': False},
    ])
    put_text(f'You selected: {drop}')

    # Select (multiple)
    put_markdown('# Multi Select')
    put_text('This is a multi selection, the default is Chicken.')
    put_text('Note "Fish" is disabled, so you can\'t select it')
    put_text('To select multiples, hold down your Ctrl while clicking')
    drop = select(label='Make your selection', multiple=True, options=[
        {'label': 'Hamburger', 'value': 'hamburger', 'selected': False},
        {'label': 'Chicken', 'value': 'chicken', 'selected': True},
        {'label': 'Fish', 'value': 'fish', 'disabled': True},
        {'label': 'Fries', 'value': 'fries', 'selected': False},
    ])
    outtxt = ''
    for x in drop:
        outtxt = f'{outtxt}\n  -{x}'
    put_text(f'You selected: {outtxt}')

    # Checkbox
    put_markdown('# Checkbox')
    put_text('Checkbox works like select.')
    put_text('You can set defaults, and disable items.')
    check = checkbox(label='Make your selection', options=[
        {'label': 'Hamburger', 'value': 'hamburger', 'selected': False},
        {'label': 'Chicken', 'value': 'chicken', 'selected': True},
        {'label': 'Fish', 'value': 'fish', 'disabled': True},
        {'label': 'Fries', 'value': 'fries', 'selected': False},
    ])
    outtxt = ''
    for x in check:
        outtxt = f'{outtxt}\n  -{x}'
    put_text(f'You selected: {outtxt}')

    # Radio
    put_markdown('# Radio')
    put_text('Radio works just like select, but you can only select 1 item.')
    rdio = radio(label='Make your selection', options=[
        {'label': 'Hamburger', 'value': 'hamburger', 'selected': False},
        {'label': 'Chicken', 'value': 'chicken', 'selected': True},
        {'label': 'Fish', 'value': 'fish', 'disabled': True},
        {'label': 'Fries', 'value': 'fries', 'selected': False},
    ])
    put_text(f'You selected: {rdio}')

    # Slider
    put_markdown('# Slider')
    put_text('Slider allows you to set a min and max.')
    put_text('You can set a step.')
    # Need to figure out "onchange"
    sldr = slider(label='Move the slider', min_value=0, max_value=100, step=5, value=50)
    put_text(f'Slider = {sldr}')

    # file_upload
    put_markdown('# File_upload')
    put_text('Slider allows you to set a min and max.')
    fil = file_upload(label='Select a file to upload', placeholder='Choose a file', multiple=False, )

    put_text(f'Saving {fil["filename"]}...')
    with open(fil['filename'], 'wb') as f:
        f.write(fil['content'])
    put_text('File saved.')

    # input_group
    put_markdown('# Imput_group')
    put_text('You can group multiple inputs together.')

    def check_form(data):
        if len(data['name']) > 6:
            return ('name', 'Name to long!')
        if data['age'] <= 0:
            return ('age', 'Age cannot be negative!')

    data = input_group("Basic info", [
        input('Input your name', name='name'),
        input('Repeat your age', name='age', type='number')
    ], validate=check_form)

    put_text(data['name'], data['age'])

    # Input Update
    put_markdown('# Input_update')
    put_text('This is only used "onchange" callback')
    country2city = {
        'China': ['Beijing', 'Shanghai', 'Hong Kong'],
        'USA': ['New York', 'Los Angeles', 'San Francisco'],
    }
    countries = list(country2city.keys())
    location = input_group("Select a location", [
        select('Country', options=countries, name='country',
               onchange=lambda c: input_update('city', options=country2city[c])),
        select('City', options=country2city[countries[0]], name='city'),
    ])


if __name__ == '__main__':
    start_server(main, debug=True, ipaddress='10.0.0.135', port=80, cdn=False)
