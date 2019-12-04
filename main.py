picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
for row in picture:
  for elements_in_row in row: 

    if elements_in_row == 1:
      print ("*", end='')
    elif elements_in_row==0:
      print(" ",end='')

  print(" ")