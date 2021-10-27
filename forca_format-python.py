erros = 7

# facil
print('-'*30)
print(' '*10,"   ________    ") 
print(' '*10,"  |        {}   " .format ('|' if erros>=0 else " "))  
print(' '*10,"  |       {} {} " .format (('(' if erros>= 1 else " "), (')' if erros>= 1 else " ")))
print(' '*10,"  |       {}{}{}" .format (('\\' if erros >=3  else " "), ('|' if erros >=2  else " "), ('/' if erros >=4  else " ")) )
print(' '*10,"  |        {}   " .format ('|' if erros>= 5 else " "))
print(' '*10,"  |       {} {} ".format (('/' if erros >=6  else " "), ('\\' if erros >=7  else " ")))
print(' '*10,"  |           ")
print(' '*10,"__|__         ")
print('-'*30)

#médio
print('-'*30)
print(' '*10,"   ________    ") 
print(' '*10,"  |        {}   " .format ('|' if erros>=0 else " "))  
print(' '*10,"  |       {} {} " .format (('(' if erros>= 1 else " "), (')' if erros>= 1 else " ")))
print(' '*10,"  |       {}{}{}" .format (('\\' if erros >=2  else " "), ('|' if erros >=2  else " "), ('/' if erros >=3  else " ")) )
print(' '*10,"  |        {}   " .format ('|' if erros>= 4 else " "))
print(' '*10,"  |       {} {} ".format (('/' if erros >=5  else " "), ('\\' if erros >=5  else " ")))
print(' '*10,"  |           ")
print(' '*10,"__|__         ")
print('-'*30)
 
 
 
# dicil
print('-'*30)
print(' '*10,"   ________    ") 
print(' '*10,"  |        {}   " .format ('|' if erros>=0 else " "))  
print(' '*10,"  |       {} {} " .format (('(' if erros>= 1 else " "), (')' if erros>= 1 else " ")))
print(' '*10,"  |       {}{}{}" .format (('\\' if erros >=1  else " "), ('|' if erros >=1  else " "), ('/' if erros >=1  else " ")) )
print(' '*10,"  |        {}   " .format ('|' if erros>= 2 else " "))
print(' '*10,"  |       {} {} ".format (('/' if erros >=3  else " "), ('\\' if erros >=3  else " ")))
print(' '*10,"  |           ")
print(' '*10,"__|__         ")
print('-'*30)


