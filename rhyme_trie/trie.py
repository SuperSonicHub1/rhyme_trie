"""
A rhyming "database" of sorts implemented with a trie.
Thanks to Jair for showing me tries and thanks to Kiera for the interesting challenge.
Some code lifted from https://networkx.org/documentation/stable/auto_examples/graph/plot_morse_trie.html#sphx-glr-download-auto-examples-graph-plot-morse-trie-py 
"""

from typing import List, Optional
from nltk.corpus import cmudict
import networkx as nx

# from nltk import matplotlib = "^3.6.3"

# download('cmudict')

rhyme_trie = nx.DiGraph()

pronunciations = cmudict.entries()
pronunciations_dict = cmudict.dict()

for index, (spelling, pronunciation) in enumerate(pronunciations):
	# For visualization
	# if index >= 100: break

	reversed_pronun = list(reversed(pronunciation))
	stages = [''] + [' '.join(reversed_pronun[:index]) for index in range(1, len(reversed_pronun) + 1)]
	for i in range(len(stages) - 1):
		rhyme_trie.add_edge(stages[i], stages[i + 1], phone=reversed_pronun[i])

def rhymes(word_1: str, word_2: str) -> Optional[List[str]]:
	try:
		word_1_pronunciations = pronunciations_dict[word_1.lower()]
		word_2_pronunciations = pronunciations_dict[word_2.lower()]
	except KeyError:
		return False

	for word_1_pronunciation in word_1_pronunciations:
		for word_2_pronunciation in word_2_pronunciations:
			ancestor = nx.lowest_common_ancestor(
				rhyme_trie,
				" ".join(reversed(word_1_pronunciation)),
				" ".join(reversed(word_2_pronunciation))
			)

			if (ancestor != ""):
				return ancestor.split(" ")[::-1]

	return None

if __name__ == "__main__":
	import matplotlib.pyplot as plt
	
	# For visualization purposes, layout the nodes in topological order
	for i, layer in enumerate(nx.topological_generations(rhyme_trie)):
		for n in layer:
			rhyme_trie.nodes[n]["layer"] = i
	pos = nx.multipartite_layout(rhyme_trie, subset_key="layer", align="horizontal")
	# Flip the layout so the root node is on top
	for k in pos:
		pos[k][-1] *= -1

	# Visualize the trie
	nx.draw(rhyme_trie, pos=pos, with_labels=True)
	elabels = {(u, v): l for u, v, l in rhyme_trie.edges(data="phone")}
	nx.draw_networkx_edge_labels(rhyme_trie, pos, edge_labels=elabels)
	plt.show()
