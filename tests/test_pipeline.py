import pandas as pd

from app.pipeline.transform import transforma_em_um_unico


df1 = pd.DataFrame({"col_1": [1, 2], "col_2": [3, 4]})
df2 = pd.DataFrame({"col_1": [5, 6], "col_2": [7, 8]})

def testar_a_concatenacao_de_lista_de_df():

    data_frame_list = [df1, df2]
    data_frame = pd.concat(data_frame_list, ignore_index=True)

    df = transforma_em_um_unico(data_frame_list)

    assert df.shape == (4,2)
    assert data_frame.equals(df)

