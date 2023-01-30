# rhyme_trie

A rhyming database implemented with a [trie](https://en.wikipedia.org/wiki/Trie) and the
[CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict).
Man, do I love data structures!

`rhyme_trie.json` is meant for use in any programming language ([see loading it in NetworkX](https://networkx.org/documentation/stable/reference/readwrite/generated/networkx.readwrite.json_graph.tree_graph.html#networkx.readwrite.json_graph.tree_graph)).
If you're already using Python, just add `from rhyme_trie import rhyme_trie` to your script (it's a `networkx.DiGraph`).

Implementing an algorithm for seeing if two pronunciations rhyme is pretty simple:

1. Reverse pronunciations on their phonemes.
2. See if they have a [common ancestor](https://en.wikipedia.org/wiki/Lowest_common_ancestor) in the tree that
isn't the root (`""`).

See the `rhymes` function in `rhyme_trie/trie.py` for an implementation in Python and NetworkX.

Code is under the Unlicense.
Data (`rhyme_trie.json`) is under the same license as `cmudict` (cannot currently find it on the project site).
