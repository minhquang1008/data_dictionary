import streamlit as st
import streamlit_antd_components as sac
import pandas as pd
import pickle
from searcher import Data
import datetime as dt
import time

returning_dictionary = {0: 'information',
                     1: 'information/dim - branch',
                     2: 'information/dim - branch/row_id',
                     3: 'information/dim - branch/integration_id',
                     4: 'information/dim - branch/datasource_id',
                     5: 'information/dim - branch/branch_code',
                     6: 'information/dim - branch/branch_name',
                     7: 'information/dim - branch/region_id',
                     8: 'information/dim - branch/status',
                     9: 'information/dim - broker',
                     10: 'information/dim - broker/row_id',
                     11: 'information/dim - broker/integration_id',
                     12: 'information/dim - broker/datasource_id',
                     13: 'information/dim - broker/broker_code',
                     14: 'information/dim - broker/broker_name',
                     15: 'information/dim - broker/gender',
                     16: 'information/dim - broker/birthday',
                     17: 'information/dim - broker/region_id',
                     18: 'information/dim - broker/nationality',
                     19: 'information/dim - broker/create_date',
                     20: 'information/dim - broker/modify_date',
                     21: 'information/dim - company',
                     22: 'information/dim - company/row_id',
                     23: 'information/dim - company/integration_id',
                     24: 'information/dim - company/datasource_id',
                     25: 'information/dim - company/company_code',
                     26: 'information/dim - company/company_name',
                     27: 'information/dim - customer',
                     28: 'information/dim - customer/Source ID',
                     29: 'information/dim - customer/Sub Account',
                     30: 'information/dim - customer/Customer Code',
                     31: 'information/dim - customer/Customer Name',
                     32: 'information/dim - customer/Birthday',
                     33: 'information/dim - customer/Gender',
                     34: 'information/dim - customer/Nationality',
                     35: 'information/dim - customer/Region ID',
                     36: 'information/dim - customer/#Count Customer',
                     37: 'information/dim - customer/.Age',
                     38: 'information/dim - territory',
                     39: 'information/dim - territory/row_id',
                     40: 'information/dim - territory/integration_id',
                     41: 'information/dim - territory/flex_province',
                     42: 'information/dim - territory/bravo_province',
                     43: 'information/dim - territory/district_code',
                     44: 'information/dim - territory/district_name',
                     45: 'information/dim - territory/district_en',
                     46: 'information/dim - territory/province_code',
                     47: 'information/dim - territory/province_name',
                     48: 'information/dim - territory/province_en',
                     49: 'information/dim - vendor',
                     50: 'information/dim - vendor/row_id',
                     51: 'information/dim - vendor/integration_id',
                     52: 'information/dim - vendor/customer_subcode',
                     53: 'information/dim - vendor/customer_code',
                     54: 'information/dim - vendor/customer_name',
                     55: 'information/dim - vendor/birthday',
                     56: 'information/dim - vendor/gender',
                     57: 'information/dim - vendor/nationality',
                     58: 'information/dim - vendor/province',
                     59: 'information/dim - vendor/contract_number_normal',
                     60: 'information/dim - vendor/contract_number_margin',
                     64: 'Margin',
                     67: 'Margin/fact - outstanding',
                     68: 'Margin/fact - outstanding/Source ID',
                     69: 'Margin/fact - outstanding/Date Key',
                     70: 'Margin/fact - outstanding/Date Oustanding',
                     71: 'Margin/fact - outstanding/Customer ID',
                     72: 'Margin/fact - outstanding/Oustanding Principal',
                     73: 'Margin/fact - outstanding/Oustanding Remain',
                     74: 'Margin/fact - outstanding/Oustanding Overdue',
                     75: 'Margin/fact - outstanding/Oustanding Paid',
                     76: 'Margin/fact - outstanding/Interest OUT',
                     77: 'Margin/fact - outstanding/Interest Due',
                     78: 'Margin/fact - outstanding/Interest Overdue',
                     79: 'Margin/fact - outstanding/Interest Overdue OUT',
                     80: 'Margin/fact - outstanding/Interest Paid',
                     81: 'Margin/fact - outstanding/Date Disbursement',
                     82: 'Margin/fact - outstanding/Date Start Interest Paid',
                     83: 'Margin/fact - outstanding/Date First Due',
                     84: 'Margin/fact - outstanding/Date Last Due',
                     85: 'Margin/fact - outstanding/Rate Due 1',
                     86: 'Margin/fact - outstanding/Rate Due 2',
                     87: 'Margin/fact - outstanding/Rate Overdue',
                     88: 'Margin/fact - outstanding/Loan Name',
                     89: 'Margin/fact - outstanding/Branch ID',
                     90: 'Margin/fact - outstanding/.Interest Outs',
                     91: 'Margin/fact - outstanding/.Interest Overdue',
                     92: 'Margin/fact - outstanding/.Outs Overdue',
                     93: 'Margin/fact - outstanding/.Outs Principal'
                    }
#st-emotion-cache
# with open('returning_dictionary.pkl', 'wb') as file:
#     pickle.dump(returning_dictionary, file)

# with open('returning_dictionary.pkl', 'rb') as file:
#     returning_dictionary = pickle.load(file)
# https://i.pinimg.com/originals/60/a5/85/60a58511e5c70a418ac743f7df8134fa.gif
# https://wallpapercave.com/uwp/uwp2493549.gif
# https://i.ibb.co/DCb3nvR/crane.jpg
st.title('DATA DICTIONARY')
with st.spinner('Wait for it...'):
    time.sleep(2)
st.markdown('''
<style>
[data-testid="stAppViewContainer"] {
background-image: url('https://janegee.com/cdn/shop/articles/janegee-clean-beauty-natural-blog-creating-white-space-2.jpg?v=1578514704');
background-size: cover;
background-repeat: no-repeat;
}
[data-testid="stSidebar"] {
background-image: url('https://i.pinimg.com/564x/b3/cd/06/b3cd06d39f7c85313649d605041b4c3d.jpg');
background-size: cover;
margin-top: 0px;
margin-left: 40px;
opacity: 0.9;
background-repeat: no-repeat;
border-style: double;
border-color: #34693a;
border-radius: 20px;
}
[class="block-container st-emotion-cache-1y4p8pa ea3mdgi4"] {
background-color: #FFFFFF;
padding-top: 5px;
margin-top: 0px;
opacity: 0.9;
background-repeat: no-repeat;
border-style: double;
border-color: #34693a;
border-radius: 20px;
line-height: 1.0;
}
[data-testid='stHeader'] {
background-color: #FFFFFF;
opacity: 0.0;
background-repeat: no-repeat;
}
[class='css-zq5wmm ezrtsby0'] {
background-color: #e8e1e0;
opacity: 0.9;
background-repeat: no-repeat;
}
</style>
''', unsafe_allow_html=True)
with open('last_search.pkl', 'rb') as file:
    last_search = pickle.load(file)
df_search = pd.DataFrame(list(returning_dictionary.items()), columns=['index', 'path'])
text_search = st.selectbox("Search column's name", df_search['path'])
if text_search != last_search:
    t2 = dt.datetime.now()
    with open('last_search.pkl', 'wb') as file:
        pickle.dump(text_search, file)
else:
    t2 = dt.datetime(1993, 4, 16)
with st.sidebar:

    st.image("logo.png", width=200)
    with open('last_clicked.pkl', 'rb') as file:
        last_clicked = pickle.load(file)
    clicked = sac.tree(items=[
        sac.TreeItem('Information', tooltip='item1 tooltip', children=[
            sac.TreeItem('Branch', icon='table', children=[sac.TreeItem(f'{i}', icon='arrow-return-right') for i in
                                        [returning_dictionary.get(k).split('/')[-1] for k in range(2, 9, 1)]]),
            sac.TreeItem('Broker', icon='table', children=[sac.TreeItem(f'{i}', icon='arrow-return-right') for i in
                                        [returning_dictionary.get(k).split('/')[-1] for k in range(10, 21, 1)]]),
            sac.TreeItem('Company', icon='table', children=[sac.TreeItem(f'{i}', icon='arrow-return-right') for i in
                                        [returning_dictionary.get(k).split('/')[-1] for k in range(22, 27, 1)]]),
            sac.TreeItem('Customer', icon='table', children=[sac.TreeItem(f'{i}', icon='arrow-return-right') for i in
                                        [returning_dictionary.get(k).split('/')[-1] for k in range(28, 38, 1)]]),
            sac.TreeItem('Territory', icon='table', children=[sac.TreeItem(f'{i}', icon='arrow-return-right') for i in
                                        [returning_dictionary.get(k).split('/')[-1] for k in range(39, 49, 1)]]),
            sac.TreeItem('Vendor', icon='table', children=[sac.TreeItem(f'{i}', icon='arrow-return-right') for i in
                                        [returning_dictionary.get(k).split('/')[-1] for k in range(50, 61, 1)]])
        ]),
        sac.TreeItem('Trading', tooltip='item2 tooltip', disabled=True, children=[
            sac.TreeItem('Trading', disabled=True, icon='table'),
            sac.TreeItem('Price Board',  disabled=True, icon='table')
        ]),
        sac.TreeItem('Margin', tooltip='item3 tooltip', children=[
            sac.TreeItem('Room', disabled=True, icon='table'),
            sac.TreeItem('Margin Detail',  disabled=True, icon='table'),
            sac.TreeItem('Outstanding', icon='table', children=[sac.TreeItem(f'{i}', icon='arrow-return-right') for i in
                                        [returning_dictionary.get(k).split('/')[-1] for k in range(68, 94, 1)]])
        ]),
    ],  label='Table',
        index=0,
        format_func='title',
        icon='folder-fill',
        height=None,
        open_index=None,
        open_all=False,
        checkbox=False,
        show_line=True,
        checkbox_strict=False,
        return_index=True)
    if clicked != last_clicked:
        t1 = dt.datetime.now()
        with open('last_clicked.pkl', 'wb') as file:
            pickle.dump(clicked, file)
    else:
        t1 = dt.datetime(1993, 4, 16)
# ----------------------------------------------------------------------------
data = Data()
if clicked and text_search and t1 > t2:
    the_path = returning_dictionary.get(clicked[0])
else:
    the_path = text_search
st.text(the_path.title())
if len(the_path.split('/')) == 3:
    data.table = the_path.split('/')[1].title()
    df = data.getData(the_path.split('/')[-1])
    st.write(f'''## {the_path.split('/')[-1].title()}''')
    st.write('article - ' + str(df['article'].iloc[0].strftime("%d/%m/%Y")))
    if str(df['Description'].iloc[0]) != 'nan':
        st.write(str(df['Description'].iloc[0]))
    st.write('### Managed by')
    st.write(str(df['Managed by'].iloc[0]))
    st.write('### Data source')
    st.write(df[['Source', 'Table', 'Field']].style.hide(axis="index").to_html(), unsafe_allow_html=True)
    if str(df['Formula'].iloc[0]) != 'nan':
        st.write('### Formula')
        st.write(str(df['Formula'].iloc[0]))

