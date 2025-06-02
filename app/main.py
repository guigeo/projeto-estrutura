from pipeline.extract import extract_excel
from pipeline.transform import transforma_em_um_unico
from pipeline.load import load_em_um_novo_excel

input_folder='C:/Users/guilherme.barbosa/Documents/meu_git/projeto-estrutura/data/input'
output_folder='C:/Users/guilherme.barbosa/Documents/meu_git/projeto-estrutura/data/output'

df_list = extract_excel(input_folder)
df = transforma_em_um_unico(df_list)
load_em_um_novo_excel(df,output_folder,"output")