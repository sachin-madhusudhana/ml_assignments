import pandas as pd

A = pd.read_excel('ABVolvo-43.xlsx')
B = pd.read_excel('ABVolvo-44.xlsx')

C = (A.iloc[:,0])
D = (B.iloc[:,0])

difference = C[C!=D]
#print (difference)



writer = pd.ExcelWriter('diff.xlsx')
difference.to_excel(writer,'Sheet1',index=False)
writer.save()
