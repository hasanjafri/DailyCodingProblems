class TernarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a new word into the tree
    def insert(self, word):
        self.root = self.insert_recursive(self.root, word, 0)

    def insert_recursive(self, node, word, index):
        # If we've reached the end of the word, mark the node as a leaf
        if index == len(word):
            return {
                'is_end': True,
                'left': None,
                'middle': None,
                'right': None,
                'value': None,
            }

        # If the node doesn't exist, create it
        if not node:
            node = {
                'is_end': False,
                'left': None,
                'middle': None,
                'right': None,
                'value': word[index],
            }

        # Recursively insert the next letter of the word into the appropriate child node
        c = word[index]
        if c < node['value']:
            node['left'] = self.insert_recursive(node['left'], word, index)
        elif c > node['value']:
            node['right'] = self.insert_recursive(node['right'], word, index)
        else:
            node['middle'] = self.insert_recursive(
                node['middle'], word, index + 1)

        return node

    # Search for a word in the tree
    def search(self, word):
        return self.search_recursive(self.root, word, 0)

    def search_recursive(self, node, word, index):
        # If we've reached the end of the tree or the word, return the result
        if not node or index == len(word):
            return node and node['is_end']

        # Otherwise, recursively search the appropriate child node
        c = word[index]
        if c < node['value']:
            return self.search_recursive(node['left'], word, index)
        elif c > node['value']:
            return self.search_recursive(node['right'], word, index)
        else:
            return self.search_recursive(node['middle'], word, index + 1)


tree = TernarySearchTree()

tree.insert('code')
tree.insert('cob')
tree.insert('be')
tree.insert('ax')
tree.insert('war')
tree.insert('we')

if __name__ == '__main__':
    print(tree.search('code'))  # True
    print(tree.search('cob'))  # True
    print(tree.search('be'))  # True
    print(tree.search('ax'))  # True
    print(tree.search('war'))  # True
    print(tree.search('we'))  # True
    print(tree.search('coda'))  # False
