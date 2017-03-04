# SpeedFinder

[![Build Status](https://travis-ci.org/thomasperrot/speed-finder.svg?branch=master)](https://travis-ci.org/thomasperrot/speed-finder)

An efficient python tool to search keywords in texts.

It currently runs in O(n x log(m)), where n is the length of the text and m is the number of keywords.

## Usage

```python
>>> keywords = ['jam', 'ham', 'chicken']
>>> speed_finder = SpeedFinder(keywords)
>>> text = "I love donuts, jam, ham, bananas, chicken and beer."
>>> list(speed_finder.find_iter(text))
[(15, 'jam'), (20, 'ham'), (34, 'chicken')]
>>> list(speed_finder.find_iter(text, limit=2))
[(15, 'jam'), (20, 'ham')]
>>> text = "I love donuts, jams, ham, bananas, chickens and beer."
>>> list(speed_finder.find_iter(text, match_words=True))
[(21, 'ham')]
>>> speed_finder.add('bananas')
>>> list(speed_finder.find_iter(text, match_words=True))
[(21, 'ham'), (26, 'bananas')]
```
