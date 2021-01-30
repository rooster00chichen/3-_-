import re
import os


class File_open():
    def __init__(self, mode=100) -> None:

        super().__init__()

        self.max_list = 0

        txt_file_url = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "webpage.txt")
        txt_file_app = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "application.txt")
        txt_file_string = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "string.txt")

        with open(txt_file_url, "r")as url_file:
            i = 0
            self.url_list = []
            read_text = url_file.readlines()
            search_text = re.compile("\w+://.*")
            for text in read_text:
                self.url_list.append(search_text.search(
                    text).group())
                i += 1
                if i == mode:
                    break

            self.url_list_count = i
            if i > self.max_list:
                self.max_list = i

        with open(
                txt_file_app, "r") as app_file:
            i = 0
            self.app_list = []
            app_list_v = app_file.readlines()

            for text in app_list_v:
                self.app_list.append(text)
                i += 1
                if i == mode:
                    break

            self.app_list_count = i

            if self.app_list_count > self.max_list:
                self.max_list = self.app_list_count

        with open(txt_file_string, "r") as string_file:
            i = 0
            self.string_list = []
            string_list_v = string_file.readlines()
            for text in string_list_v:
                self.string_list.append(text)
                i += 1
                if i == mode:
                    break
            self.string_list_count = i

            if self.string_list_count > self.max_list:
                self.max_list = self.string_list_count
