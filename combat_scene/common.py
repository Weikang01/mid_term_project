"""
make your life easier
让生活更简单
"""
import os


def absolute_path(dir_name='./combat_scene'):
    path_e = os.path.abspath(dir_name).split('/')[0:-2]
    return '/'.join(path_e) + '/'


if __name__ == '__main__':
    print(absolute_path())
