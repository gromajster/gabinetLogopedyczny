from django.utils._os import safe_join
from storages.backends.dropbox import DropBoxFile, DropBoxStorage


class DropBoxFileStorageCustom(DropBoxStorage):
    def _full_path(self, name):
        if name == '/':
            name = ''
        # TODO CHECK IF PATH STARTS WITH ANY LETTER AND : AD THEN REMOVE IT
        return safe_join(self.root_path, name).replace('\\', '/')[2:]
