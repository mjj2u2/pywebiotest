from pywebio import start_server, pin
import pywebio.output as o
import pywebio.input as i
import pywebio.session as s
import functools as f


def main():
    o.put_markdown(f'# Bob2')


if __name__ == '__main__':
    main()

