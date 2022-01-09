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
    set_env(output_max_width='100%', auto_scroll_bottom=True)

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


if __name__ == '__main__':
    start_server(main, debug=True, ipaddress='10.0.0.135', port=80, cdn=False)
