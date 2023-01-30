"""
Generate JSON file of tree for use outside of Python.
"""

import json
from networkx.readwrite import json_graph
from .trie import rhyme_trie

with open("rhyme_trie.json", 'w') as f:
	json.dump(json_graph.tree_data(rhyme_trie, ""), f)
