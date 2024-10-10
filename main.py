with open("books/frankenstien.txt") as f:
   file_contents = f.read()
   print(file_contents)

   def num_words(file_contents):
      words = file_contents.split()
      print(len(words))

   num_words(file_contents)