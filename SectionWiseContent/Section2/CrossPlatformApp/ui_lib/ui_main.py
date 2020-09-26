"""
Entry point for the application.
"""
import webview


def render_window(title,content):
    """
    Renders the content in a webview window.
    :param title: Title of the window
    :param content: html content to render
    """
    webview.create_window(title=title, html=content)
    webview.start()


if __name__ == '__main__':
    render_window("Hello World","<h1>Hello World</h1>")
