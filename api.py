import webview

class Api:
    def open_directory_dialog(self):
        print("Opening directory dialog...")  # Debugging line
        directory = webview.windows[0].create_file_dialog(webview.FOLDER_DIALOG)
        if directory:
            return directory[0]
        return ""
