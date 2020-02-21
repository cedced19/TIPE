import os


filename = os.path.abspath('../y-cruncher/10K/pi-dec-chudnovsky.txt')

with open(filename) as f:
  while True:
    c = f.read(1)
    if not c:
      print("End of file")
      break
    print("Read a character:", c)
