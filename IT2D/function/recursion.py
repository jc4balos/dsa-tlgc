def countdown(n):
  if n <= 0:
    print("Done!")  #Base Case
  else:
    print(n)
    countdown(n - 1)

def countdown2(n):
  print(n)
  countdown2(n - 1)

countdown2(5)

