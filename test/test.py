from speedfinder import SpeedFinder


def test_functionnal():
    keywords = ['jam', 'ham', 'chicken']
    speed_finder = SpeedFinder(keywords)
    text = "I love donuts, jam, ham, bananas, chicken and beer."
    assert list(speed_finder.find_iter(text)) == [(15, 'jam'), (20, 'ham'), (34, 'chicken')]
    assert list(speed_finder.find_iter(text, limit=2)) == [(15, 'jam'), (20, 'ham')]
    text = "I love donuts, jams, ham, bananas, chickens and beer."
    assert list(speed_finder.find_iter(text, match_words=True)) == [(21, 'ham')]
    speed_finder.add('bananas')
    assert list(speed_finder.find_iter(text, match_words=True)) == [(21, 'ham'), (26, 'bananas')]
