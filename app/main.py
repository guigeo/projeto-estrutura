from pipeline.extract import extract_excel

input_folder='C:/Users/guilherme.barbosa/Documents/meu_git/projeto-estrutura/data/input'

df = extract_excel(input_folder)
print (df)