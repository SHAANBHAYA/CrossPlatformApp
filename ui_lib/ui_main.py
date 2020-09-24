import webview

def window_render(heading,content):
    """
    Creates a window with supplied heading and content
    """
    webview.create_window(heading,html=content)
    webview.start()



if __name__ == '__main__':
    window_render(heading="Hello World",content="<h1>Hello World</h1>")