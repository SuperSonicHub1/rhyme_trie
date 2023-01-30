from rhyme_trie import rhymes

assert rhymes("jab", "cab") and "rhymes rhyme"
assert not rhymes("jab", "fabulous") and "non-rhymes do not rhyme"
assert not rhymes("jab", "ddddwwfwf") and "words that aren't in the dictionary"
assert rhymes("read", "reed") and "heteronyms part 1"
assert rhymes("read", "bed") and "heteronyms part 2"
