def moyenne(notes):
      res1=0
      sommes=0
      moyenne=0
      for nb in notes:
            if nb < 5:
                  sommes = sommes + 0
            else:
                  sommes=sommes + 1
      for nb in notes:
            if nb > 5:
                  res1= res1 + nb
      moyenne=res1/sommes
      print(sommes)
      return moyenne
      
print (moyenne([17,0,12,10,8,4,20,17]))



