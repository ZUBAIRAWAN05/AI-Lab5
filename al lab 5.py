class Trie:
  def __init__(self):
    self.character = {}
    self.isLeaf = False
     

def insert(root, string):
  current = root
  for character in string:
    current = current.character.setdefault(character, Trie())

  current.isLeaf = True  
     

row = [-1, -1, -1, 0, 1, 0, 1, 1]
column = [-1, 1, 0, -1, -1, 1, 0, 1]
     

def isSafe(x, y, processed, board, character):
  return (0 <= x < len(processed)) and (0 <= y < len(processed[0])) and not processed[x][y] and (board[x][y] == character)
     

def searchBoggle(root, board, i, j, processed, path, result):
  if root.isLeaf:
    result.add(path)

  processed[i][j] = True

  for key, value in root.character.items():

    for k in range(len(row)):
      if isSafe(i + row[k], j + column[k], processed, board, key):
        searchBoggle(value, board, i + row[k], j + column[k], processed, path + key, result)

  processed[i][j] = False
     

def searchInBoggle(board, words):
  result = set()

  if not board or not len(board):
    return

  root = Trie()
  for word in words:
    insert(root, word)  

  (M, N) = (len(board), len(board[0]))

  processed = [[False for x in range(N)] for y in range(M)]

  for i in range(M):
    for j in range(N):
      character = board[i][j]

      if character in root.character:
        searchBoggle(root.character[character], board, i, j, processed, character, result)

  return result
     

if __name__ == '__main__':
  board = [
      ['M', 'S', 'E', 'F'],
      ['R', 'A', 'T', 'D'],
      ['L', 'O', 'N', 'E'],
      ['K', 'A', 'F', 'B']
  ]

  words = ['START', 'NOTE', 'SAND', 'STONED']
  validWords = searchInBoggle(board, words)

  print('Valid Words: ', validWords)
