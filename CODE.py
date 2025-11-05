def sort_books(books):
  shelves = {i:[] for i in range(1, 50)}
  # assuming the input is in the following format:
  # books = [{shelf: 5, order: 3}, {shelf: 2, order: 1}, {shelf: 5, order: 2}]
  # place each book on the correct shelf
  for book in books:
    s = book[shelf]
    shelves[s].append(book)
  # sort the individual shelves
  output = []
  for key in shelves.keys():
    # sort the val
    insertion_sort(shelves[key])
    output.extend(shelves[key])
  return output

def insertion_sort(val):
  for i in range(len(val)):
    for j in range(i, 0, -1):
      if val[j][order] < val[j - 1][order]:
        val[j], val[j- 1] = val[j-1], val[j]

