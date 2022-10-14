import os


class Path:

    @classmethod
    def get_root_path(cls) -> str:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        split_folders = current_dir.split('/')[:-2]
        return '/'.join(split_folders)
