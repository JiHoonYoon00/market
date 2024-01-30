# _*_ coding:utf-8 _*_

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import altair as alt
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.graph_objects as go 
import plotly.express as px 
from plotly.subplots import make_subplots 
import plotly as pt


@st.cache_data
def load_data():
    orders_df = pd.read_csv("/Users/yoonjihoon/market/data/order_random.csv")
    products_df = pd.read_csv("/Users/yoonjihoon/market/data/products.csv")
    order_products_prior_df = pd.read_csv("/Users/yoonjihoon/market/data/order_products_prior_random.csv")
    aisles_df = pd.read_csv("/Users/yoonjihoon/market/data/aisles.csv")
    departments_df = pd.read_csv("/Users/yoonjihoon/market/data/departments.csv")
    
    return orders_df, products_df, order_products_prior_df, aisles_df, departments_df



def main():
    orders, products, order_products_prior, aisles, departments = load_data()
    tab1, tab2, tab3, tab4, tab5 = st.tabs(['orders', 'products', 'order_products_prior', 'aisles', 'departments'])

    new_data = products.merge(departments, how ='left', on = 'department_id')
    #uni_new_data = new_data['product_name'].unique()
    with tab1:
        st.write("주문 데이터 :")
        st.write(orders)
        
        selected_category = st.sidebar.selectbox("주문데이터", ['사람들의 주문시간', '요일별 데이터'])
        if selected_category == '사람들의 주문시간':
            st.header("사람들의 주문시간")
            fig, ax = plt.subplots()
            sns.histplot(x=orders["order_hour_of_day"], kde=False, ax=ax,binwidth=1)
            st.pyplot(fig)

        elif selected_category == '요일별 데이터':
            st.header("요일별 데이터")
            fig, ax = plt.subplots()
            sns.histplot(x=orders["order_dow"], kde=False, ax=ax)
            st.pyplot(fig)



    with tab2:
        st.write("제품 데이터 :")
        st.write(new_data)
        

        selected_category = st.sidebar.selectbox("제품데이터", ['항목별 제품갯수', '항목별 제품종류'])
        if selected_category == '항목별 제품갯수':
            st.header("항목별 제품갯수")
            fig, ax = plt.subplots()
            sns.barplot(x=products["department_id"], y=products.index, ax=ax)
            ax.set_xticklabels(departments["department"].tolist(), rotation=45, ha="right")
            st.pyplot(fig)

        elif selected_category == '항목별 제품종류':
            
            st.header("항목별 제품종류")
            options = st.selectbox('원하는 항목을 골라 주세요',('frozen','other','bakery',
            'produce','alcohol','international','beverages','pets'))
            
            uni = new_data[new_data['department']==options]
           
            st.write('선택된 항목의 제품 종류:', uni['product_name'].unique())

       
    with tab3:
        st.write("주문 데이터 :")
        st.write(order_products_prior)

    with tab4:
        st.write("주문 데이터 :")
        st.write(aisles)

    with tab5:
        st.write("주문 데이터 :")
        st.write(departments)



if __name__ == "__main__":
    main()
    