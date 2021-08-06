import itertools
import sys
import os
from typing import List


class NoGitFolderInProjectError(Exception):
    def __init__(self):
        self.message = "Didn't find a folder with a .git directory for this project!"
        super().__init__(self.message)


class NoPossibleRootsFound(Exception):
    def __init__(self):
        self.message = "Found no possible ancestor roots in sys.path!"
        super().__init__(self.message)


class ShortestRootIsntGitRoot(Exception):
    def __init__(self, git_root_path: str, shortest_root_path: str):
        self.message = f"The shortest root (ancestor) found was: {shortest_root_path}, but the shortest git root found was {git_root_path}"
        super().__init__(self.message)


def does_file_path_contain_path_component(cur_file_dir: str):
    cur_file_components = os.path.normpath(cur_file_dir).split(os.sep)
    possible_roots = []
    for path in sys.path:
        possible_root_dir = True
        for cur_file_comp, comp in zip(cur_file_components, os.path.normpath(path).split(os.sep)):
            if cur_file_comp != comp:
                possible_root_dir = False
        if possible_root_dir:
            possible_roots.append(path)
    if len(possible_roots) <= 0:
        raise NoPossibleRootsFound()
    return possible_roots


def shortest_possible_root(possible_roots: List[str]):
    shortest_root_len = None
    shortest_root = None
    for root in possible_roots:
        comps = os.path.normpath(root).split(os.sep)
        comp_len = len(comps)
        if shortest_root_len is None or comp_len < shortest_root_len:
            shortest_root_len = comp_len
            shortest_root = root
    if shortest_root is None:
        raise NoPossibleRootsFound()
    return shortest_root


def get_proj_root(ignore_cwd=False):
    """
    :param ignore_cwd: ignore the current working directory for deriving the root path
    :return returns project root path:
    :rtype: str
    """
    cur_file_dir = os.path.dirname(os.path.abspath(__file__))
    if not ignore_cwd and cur_file_dir == os.path.abspath(os.getcwd()):
        return cur_file_dir
    possible_roots = does_file_path_contain_path_component(cur_file_dir)
    return shortest_possible_root(possible_roots)


if __name__ == '__main__':
    res = root_path()
    print(res)

