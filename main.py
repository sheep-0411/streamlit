import streamlit as st
import pandas as pd

#タイトルの追加
st.title('注記検索')

df = pd.read_csv('test_combine1228-3.csv',encoding='cp932',usecols=['日本語','値','会社名'])
df = df.dropna(subset=['値'])
input1 = st.text_input('①検索キーワードを入力してください')

option = st.slider('②表示させたい会社数を選択してください', 0, 100 ,10)

df = df[df['値'].str.contains(input1)]
df = df.reset_index(drop=True)
multi_select = st.multiselect('（任意）③項目でさらに絞り込む場合に選択してください',df['日本語'].drop_duplicates().reset_index(drop=True))
if multi_select != []:
    df = df[df['日本語'].isin(multi_select)]
    df = df.reset_index(drop=True)

#df_data = st.dataframe(df,height=500,width=1000)

display = st.checkbox('検索結果を表示する')
if display:
    try:
        if len(df) < option:
            option = len(df)
        st.write('【検索結果】' + str(len(df)) + '件一致しました。' + str(len(df)) + '件中' + str(option) + '件表示しています。')
        for i in range(0,option):
            st.write(str(i + 1) + '.' +df.loc[i,'会社名'] + 'の「' + df.loc[i,'日本語'] + '」で一致しました')
            height = st.slider('高さを調整できます' + str(i+1), 0, 1000 ,100)
            text = df.loc[i,'値']
            text = text.replace(input1,'<mark>' + input1 +'</mark>')
            st.components.v1.html(text,height=height,scrolling=True)
    except Exception as e:
        st.write('エラーが発生しました。')
    

