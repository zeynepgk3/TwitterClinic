import pandas as pd

def writeToFile(content, columns,fileName):
    df=pd.DataFrame(content, columns)
    df.to_csv(fileName)
    print(df)

def writeToExcel(fileName, content):
    ## burayı sonra yaz. veriyi hangi tipte toplayacağına göre değişir çünkü
    return ""

