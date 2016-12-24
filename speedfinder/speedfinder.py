"""
@author: Thomas Perrot
@copyright: 2016 Thomas Perrot

SpeedFinder, an efficient python tool to search keywords in texts.
It currently runs in O(n x log(m)), where n is the length of the text and m is the number of keywords.
"""


from typing import Dict, Union, Iterable, Tuple, Iterator
import re


Tree = Dict[str, Dict]
letter = re.compile(r'[A-za-z]')


class SpeedFinder:
    """
    Class to find as quickly as possible a list of keywords in a given text. It currently runs in O(n x log(m)),
    where n is the length of the text and m is the number of keywords.

    The keywords are represented as a tree (a dict of dicts of dicts ...). When we want to find keywords in a text,
    we simply go through the text and check whether a given sequence of chars reaches a leaf in the tree , which is
    a dict whose value is an empty dict.
    """

    def __init__(self, keywords: Union[str, Iterable[str]]=None) -> None:
        self.tree = {}
        if keywords:
            self.add(keywords)

    def add(self, keywords: Union[str, Iterable[str]]) -> None:
        if isinstance(keywords, str):
            keywords = [keywords]
        for kw in keywords:
            self.tree = self.add_to_tree(self.tree, kw)

    def find_iter(self, text: str, match_words: bool=False, limit: int=0) -> Iterator[Tuple[int, str]]:
        """
        Iterates over the keywords in the text. You can limit results to the first n keywords found.
        Use match_words if you only want to match full words (i.e separate from the rest of the
        text by non letter char.
        Returns an iterator on the matches, which are 2-tuples with the position of the first letter
        of the found keyword in the text, and the keyword itself.
        """

        n_matches = 0
        for i, l in enumerate(text):
            if match_words and i > 0 and letter.match(text[i - 1]):
                continue
            match, complete = self.in_tree(self.tree, text[i:], '')
            if complete:
                if match_words and letter.match(text[i + len(match)]):
                    continue
                n_matches += 1
                yield i, match
            if n_matches >= limit > 0:
                raise StopIteration

    @staticmethod
    def in_tree(tree: Tree, text: str, prev_letters: str) -> Tuple[str, bool]:
        """Recursive function to find whether the given sequence begins by one of the keywords."""

        if not tree:
            return prev_letters, True
        complete = False
        l = text[0]
        if l in tree:
            prev_letters, complete = SpeedFinder.in_tree(tree[l], text[1:], prev_letters + l)
        if complete:
            return prev_letters, True
        return None, False

    @staticmethod
    def add_to_tree(tree, word: str) -> Tree:
        """Recursive function to add a new keyword to the tree."""

        if not word:
            return tree
        l = word[0]
        if l not in tree:
            tree[l] = {}
        SpeedFinder.add_to_tree(tree[l], word[1:])
        return tree
