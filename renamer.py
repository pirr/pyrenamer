import os
import glob
import re


class FileRenamer(object):

    def __init__(self, replace, to, with_regex):
        self.replace = replace
        self.to = to
        self.with_regex = with_regex

    def __call__(self):
        cwd = os.getcwd()
        if self.with_regex:
            self.rx_patt = re.compile(self.replace)
        try:
            for file_name in os.listdir(cwd):
                if not os.path.isfile(os.path.join(cwd, file_name)):
                    continue
                if self.with_regex:
                    new_file_name = self.rx_patt.sub(self.to, file_name)
                else:
                    new_file_name = file_name.replace(self.replace, self.to)
                os.rename(os.path.join(cwd, file_name), os.path.join(cwd, new_file_name))
        except Exception as e:
            raise(e)
        return None
