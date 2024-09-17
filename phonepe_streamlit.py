import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit_option_menu import option_menu
import mysql.connector

db = mysql.connector.connect(
  host = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
  port = 4000,
  user = "2Ec717sQXDXrbge.root",
  password = "shGX22mUul3ECK8V",
  database = "phonepe_analysis"
)
cursor=db.cursor()


st.set_page_config(page_title= "Phonepe Pulse Data Visualization and Exploration :exclamation:",
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   )

st.sidebar.markdown("# :black[**Hello!**] :wave:")
st.sidebar.markdown("# :black[ Welcome to the dashboard!]")

with st.sidebar:
    st.image("Images/icon2.gif")
    selected = option_menu("Menu", ["Home","Top Charts","Explore Data"], 
                icons=["house","graph-up-arrow","bar-chart-line", "exclamation-circle"],
                menu_icon= "menu-button-wide",
                default_index=0,
                styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "#6F36AD"},
                        "nav-link-selected": {"background-color": "#6F36AD"}})
# MENU 1 - HOME
if selected == "Home":
    
    st.markdown("# :violet[Data Visualization and Exploration]")
    st.markdown("## :violet[A User-Friendly Tool Using Streamlit and Plotly]")
    col1,col2 = st.columns([3,2],gap="medium")
    with col1:
        st.write(" ")
        st.write(" ")
        st.markdown("## :violet[Domain :] Fintech")
        st.markdown("## :violet[Technologies used :]")
        st.markdown("### -Github Cloning")
        st.markdown("### -Python")
        st.markdown("### -Pandas")
        st.markdown("### -MySQL")
        st.markdown("### -sql-connector-python")
        st.markdown("### -Streamlit")
        st.markdown("### -Plotly")
        
    with col2:
        st.image("Images/icon1.jpg")

    st.markdown("## :violet[Overview :]")
    st.markdown("### In this streamlit web app you can visualize the phonepe pulse data and gain lot of insights on transactions, number of users, top 10 state, district, pincode and which brand has most number of users and so on. Bar charts, Pie charts and Geo map visualization are used to get some insights.")

if selected == "Top Charts":
    st.markdown("## :violet[Top Charts]")
    Type = st.sidebar.selectbox("**Type**", ("Transactions", "Users","Insurance"),index=0)
    Year = st.sidebar.slider("**Year**", min_value=2018, max_value=2023)
    Quarter = st.sidebar.slider("Quarter", min_value=1, max_value=4)

    st.info(
            """
            #### From this menu we can get insights like :
            - Overall ranking on a particular Year and Quarter.
            - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on phonepe.
            - Top 10 State, District, Pincode based on Total phonepe users and their app opening frequency.
            - Top 10 mobile brands and its percentage based on the how many people use phonepe.
            - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on
            """
            )
        

    if Type == "Transactions":
        col1,col2 = st.columns([1,1])
        
        with col1:
            st.markdown("### :violet[State]")
            cursor.execute(f'''select state, sum(Transaction_count) as Total_Transactions, sum(Transaction_amount) as Total_amount from aggregated_transaction 
                           where year = {Year} and quarter = {Quarter} group by state order by Total_amount desc limit 10''')
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Transactions_Count','Total_Amount'])
            fig = px.pie(df, values='Total_Amount',
                             names='State',
                             title='Top 10',
                             color_discrete_sequence=px.colors.sequential.Mint,
                             hover_data=['Transactions_Count'],
                             labels={'Transactions_Count':'Transactions_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)


        with col2:
                st.markdown("### :violet[District]")
                cursor.execute(f'''select district , sum(transaction_count) as Total_Count, sum(transaction_amount) as Total_amount from map_transaction 
                            where year = {Year} and quarter = {Quarter} group by district order by Total_amount desc limit 10''')
                df = pd.DataFrame(cursor.fetchall(), columns=['District', 'Transactions_Count','Total_Amount'])

                fig = px.pie(df, values='Total_Amount',
                                names='District',
                                title='Top 10',
                                color_discrete_sequence=px.colors.sequential.Sunsetdark,
                                hover_data=['Transactions_Count'],
                                labels={'Transactions_Count':'Transactions_Count'})

                fig.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig,use_container_width=True)
            
        st.markdown("### :violet[Pincode]")
        cursor.execute(f'''select pincode, sum(transaction_count) as Total_Transactions_Count, sum(transaction_amount) as Total_amount from top_transaction
                        where year = {Year} and quarter = {Quarter} group by pincode order by Total_amount desc limit 10''')
        df = pd.DataFrame(cursor.fetchall(), columns=['Pincode', 'Transactions_Count','Total_Amount'])
        fig = px.pie(df, values='Total_Amount',
                            names='Pincode',
                            title='Top 10',
                            color_discrete_sequence=px.colors.sequential.Purpor,
                            hover_data=['Transactions_Count'],
                            labels={'Transactions_Count':'Transactions_Count'})

        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)


    if Type == "Users":
        col1,col2= st.columns([1,1],gap="small")
        col3,col4= st.columns([1,1],gap="small")
        with col1:
            st.markdown("### :violet[Brands]")
            if ((Year == 2022 and Quarter in [2,3,4]) or Year == 2023):
                st.markdown('''## No Data to Display for the selected period''')
            else:
                cursor.execute(f'''select brand, sum(transaction_count) as Total_Count, avg(percentage)*100 as Avg_Percentage from aggregated_users
                               where year = {Year} and quarter = {Quarter} group by brand order by Total_Count desc limit 10''')
                df = pd.DataFrame(cursor.fetchall(), columns=['Brand', 'Total_Users','Avg_Percentage'])
                fig = px.bar(df,
                             title='Top 10',
                             x="Total_Users",
                             y="Brand",
                             orientation='h',
                             color='Avg_Percentage',
                             color_continuous_scale=px.colors.sequential.speed)
                st.plotly_chart(fig,use_container_width=True)   
    
        with col2:
            st.markdown("### :violet[State]")
            cursor.execute(f'''select state, sum(registered_user) as Total_Users, sum(app_opens) as Total_Appopens from map_user
                            where year = {Year} and quarter = {Quarter} group by state order by Total_Users desc limit 10''')
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Total_Users','Total_Appopens'])
            fig = px.pie(df, values='Total_Users',
                             names='State',
                             title='Top 10',
                             color_discrete_sequence=px.colors.sequential.Agsunset,
                             hover_data=['Total_Appopens'],
                             labels={'Total_Appopens':'Total_Appopens'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
              
        with col3:
            st.markdown("### :violet[District]")
            cursor.execute(f'''select district, sum(registered_user) as Total_Users, sum(app_opens) as Total_Appopens from map_user 
                           where year = {Year} and quarter = {Quarter} group by district order by Total_Users desc limit 10''')
            df = pd.DataFrame(cursor.fetchall(), columns=['District', 'Total_Users','Total_Appopens'])
            df.Total_Users = df.Total_Users.astype(float)
            fig = px.bar(df,
                         title='Top 10',
                         x="Total_Users",
                         y="District",
                         orientation='h',
                         color='Total_Users',
                         color_continuous_scale=px.colors.sequential.YlOrBr)
            st.plotly_chart(fig,use_container_width=True)
            
        with col4:
            st.markdown("### :violet[Pincode]")
            cursor.execute(f'''select pincode, sum(registered_count) as Total_Users from top_user 
                           where year = {Year} and quarter = {Quarter} group by pincode order by Total_Users desc limit 10''')
            df = pd.DataFrame(cursor.fetchall(), columns=['Pincode', 'Total_Users'])
            fig = px.pie(df,
                         values='Total_Users',
                         names='Pincode',
                         title='Top 10',
                         color_discrete_sequence=px.colors.sequential.haline,
                         hover_data=['Total_Users'])
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            

    if Type == "Insurance":
        col1,col2 = st.columns([1,1])
        if(Year in [2018,2019] or (Year == 2020 and Quarter == 1)):
            st.markdown("## No Data to Display for the selected period")

        else:
            with col1:
                st.markdown("### :violet[State]")
                cursor.execute(f'''select state, sum(insurance_count) as Total_insurance_count, sum(insurance_amount) as Total_insurance_amount from aggregated_insurance 
                                where year = {Year} and quarter = {Quarter} group by state order by Total_insurance_amount desc limit 10''')
                df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Total_insurance_count','Total_insurance_amount'])
                fig = px.pie(df, values='Total_insurance_amount',
                                    names='State',
                                    title='Top 10',
                                    color_discrete_sequence=px.colors.sequential.RdBu,
                                    hover_data=['Total_insurance_count'],
                                    labels={'Total_insurance_count':'Total_insurance_count'})

                fig.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig,use_container_width=True)


            with col2:
                    st.markdown("### :violet[District]")
                    cursor.execute(f'''select district , sum(transactional_count) as Total_Count, sum(transactional_amount) as Total_amount from map_insurance 
                                where year = {Year} and quarter = {Quarter} group by district order by Total_amount desc limit 10''')
                    df = pd.DataFrame(cursor.fetchall(), columns=['District', 'Transactions_Count','Total_Amount'])

                    fig = px.pie(df, values='Total_Amount',
                                    names='District',
                                    title='Top 10',
                                    color_discrete_sequence=px.colors.sequential.YlGn,
                                    hover_data=['Transactions_Count'],
                                    labels={'Transactions_Count':'Transactions_Count'})

                    fig.update_traces(textposition='inside', textinfo='percent+label')
                    st.plotly_chart(fig,use_container_width=True)
                
            st.markdown("### :violet[Pincode]")
            cursor.execute(f'''select pincode, sum(transaction_count) as Total_Transactions_Count, sum(transaction_amount) as Total_amount from top_insurance
                            where year = {Year} and quarter = {Quarter} group by pincode order by Total_amount desc limit 10''')
            df = pd.DataFrame(cursor.fetchall(), columns=['Pincode', 'Transactions_Count','Total_Amount'])
            fig = px.pie(df, values='Total_Amount',
                                names='Pincode',
                                title='Top 10',
                                color_discrete_sequence=px.colors.sequential.turbid,
                                hover_data=['Transactions_Count'],
                                labels={'Transactions_Count':'Transactions_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)



if selected == "Explore Data":
    Type = st.sidebar.selectbox("**Type**", ("Transactions", "Users","Insurance"),index=0)


    if Type == "Transactions":
            Year = st.sidebar.slider("**Year**", min_value=2018, max_value=2023)
            Quarter = st.sidebar.slider("Quarter", min_value=1, max_value=4)
        
            cursor.execute(f'''select state, sum(transaction_count) as Total_Transactions, sum(transaction_amount) as Total_amount from map_transaction
                           where year = {Year} and quarter = {Quarter} group by state order by Total_Transactions desc''')
            df1 = pd.DataFrame(cursor.fetchall(),columns= ['State', 'Total_Transactions', 'Total_amount'])

            fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                      featureidkey='properties.ST_NM',
                      locations='State',
                      color='Total_amount',
                      color_continuous_scale='Rainbow',
                      title='Overall State Data - Transactions Amount')

            fig.update_geos(fitbounds="locations", visible=False)
            fig.update_layout(title_font=dict(size=40), title_font_color='#AD71EF', height=800)
            st.plotly_chart(fig,use_container_width=True)
            
            
            cursor.execute(f'''select state, sum(transaction_count) as Total_Transactions, sum(transaction_amount) as Total_amount from map_transaction 
                           where year = {Year} and quarter = {Quarter} group by state order by Total_Transactions desc''')
            df1 = pd.DataFrame(cursor.fetchall(),columns= ['State', 'Total_Transactions', 'Total_amount'])
            

            fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                      featureidkey='properties.ST_NM',
                      locations='State',
                      color='Total_Transactions',
                      color_continuous_scale='sunset',
                      title='Overall State Data - Transactions Count' )

            fig.update_geos(fitbounds="locations", visible=False)
            fig.update_layout(title_font=dict(size=40), title_font_color='#AD71EF', height=800)
            st.plotly_chart(fig,use_container_width=True)

    
            st.markdown("## :violet[Top Payment Type]")
            cursor.execute(f'''select transaction_type, sum(transaction_count) as Total_Transactions, sum(transaction_amount) as Total_amount from aggregated_transaction
                           where year= {Year} and quarter = {Quarter} group by transaction_type order by transaction_type''')
            df = pd.DataFrame(cursor.fetchall(), columns=['Transaction_type', 'Total_Transactions','Total_amount'])

            fig = px.bar(df,
                        title='Transaction Types vs Total_Transactions',
                        x="Transaction_type",
                        y="Total_Transactions",
                        orientation='v',
                        color='Total_amount',
                        color_continuous_scale=px.colors.sequential.thermal)
            fig.update_layout(title_font=dict(size=40), title_font_color='#AD71EF', height=800)
            st.plotly_chart(fig,use_container_width=False)  

            

            st.markdown("## :violet[Select state to transaction count of each district]")
            selected_state = st.selectbox("",
                             ('Andaman & Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh',
                                'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',
                                'Dadra & Nagar Haveli & Daman & Diu', 'Delhi', 'Goa', 'Gujarat',
                                'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand',
                                'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh',
                                'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland',
                                'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim',
                                'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
                                'Uttarakhand', 'West Bengal'),index=30)
         
            cursor.execute(f'''select state, district, year, quarter, sum(transaction_count) as Total_Transactions, sum(transaction_amount) as Total_amount from map_transaction
                            where year = {Year} and quarter = {Quarter} and state = '{selected_state}' group by state, district, year, quarter order by Total_amount''')
            
            df = pd.DataFrame(cursor.fetchall(), columns=['State','District','Year','Quarter',
                                                            'Total_Transactions','Total_amount'])
            fig = px.bar(df,
                        title=selected_state,
                        x="District",
                        y="Total_Transactions",
                        orientation='v',
                        color='Total_amount',
                        color_continuous_scale=px.colors.sequential.Agsunset)
            fig.update_layout(title_font=dict(size=40), title_font_color='#AD71EF', height=800)
            st.plotly_chart(fig,use_container_width=True)

            

    if Type == "Users":
        Year = st.sidebar.slider("**Year**", min_value=2018, max_value=2023)
        Quarter = st.sidebar.slider("Quarter", min_value=1, max_value=4)
        if(Year ==2018 or (Year== 2019 and Quarter== 1)):
            st.markdown("## No Data availabe to display")
        else:
            cursor.execute(f'''select state, sum(registered_user) as Total_Users, sum(app_opens) as Total_Appopens from map_user 
                        where year = {Year} and quarter = {Quarter} group by state order by Total_Appopens desc''')
            df1 = pd.DataFrame(cursor.fetchall(), columns=['State', 'Total_Users','Total_Appopens'])
            
            fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                    featureidkey='properties.ST_NM',
                    locations='State',
                    color='Total_Appopens',
                    color_continuous_scale='sunset',
                    title= 'Overall State Data - User App opening frequency')

            fig.update_geos(fitbounds="locations", visible=False)
            fig.update_layout(title_font=dict(size=40), title_font_color='#AD71EF', height=800)
            st.plotly_chart(fig,use_container_width=True)
            
        selected_state = st.selectbox("",
                             ('Andaman & Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh',
                                'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',
                                'Dadra & Nagar Haveli & Daman & Diu', 'Delhi', 'Goa', 'Gujarat',
                                'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand',
                                'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh',
                                'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland',
                                'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim',
                                'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
                                'Uttarakhand', 'West Bengal'),index=30)
        
        cursor.execute(f'''select state, year, quarter, district, sum(registered_user) as Total_Users, sum(app_opens) as Total_Appopens from map_user 
                       where year = {Year} and quarter = {Quarter} and state = '{selected_state}' group by state, district, year, quarter order by Total_Users desc''')
        
        df = pd.DataFrame(cursor.fetchall(), columns=['State','year', 'quarter', 'District', 'Total_Users','Total_Appopens'])
        
        fig = px.bar(df,
                     title=selected_state,
                     x="District",
                     y="Total_Users",
                     orientation='v',
                     color='Total_Users',
                     color_continuous_scale=px.colors.sequential.Agsunset)
        fig.update_layout(title_font=dict(size=40), title_font_color='#AD71EF', height=800)
        st.plotly_chart(fig,use_container_width=True)
        
    if Type == "Insurance":
        
        cursor.execute(f'''select state, year, sum(insurance_amount) as Total_insurance from aggregated_insurance
                       group by year,state order by Total_insurance desc''')
        
        df = pd.DataFrame(cursor.fetchall(), columns=['State','Year','Total_insurance'])

        fig = px.bar(df,
                     x="State",
                     y="Total_insurance",
                     orientation='v',
                     color='Year',
                     color_continuous_scale=px.colors.sequential.Agsunset,
                     title="Total insurance amount")
        fig.update_layout(title_font=dict(size=40), title_font_color='#AD71EF', height=800)
        st.plotly_chart(fig,use_container_width=True)

        cursor.execute(f'''select state, year, quarter, sum(transactional_count) as Total_transactions from map_insurance
                       group by year, quarter, state order by Total_transactions desc''')
        
        df = pd.DataFrame(cursor.fetchall(), columns=['State','Year','Quarter','Total_insurance'])

        fig = px.sunburst(df, path=['Year', 'State'], values='Total_insurance', title='Transaction count')
        fig.update_layout(title_font=dict(size=40), title_font_color='#AD71EF', height=800)
        st.plotly_chart(fig,use_container_width=True)

        selected_year = st.selectbox("",
                             ('2020','2021','2022','2023'),index= 0)

        cursor.execute(f'''select state, year, quarter, sum(Transactional_amount) as Total_amount,district from map_insurance
                       where year= {selected_year} group by year, quarter, state, district order by Total_amount desc''')
        
        df = pd.DataFrame(cursor.fetchall(), columns=['State','Year','Quarter','Total_amount','District'])

        fig = px.icicle(df, path=[px.Constant(selected_year), 'Quarter', 'State','District'], 
                        values='Total_amount',
                        color='State',
                        title='Total amount on insurance for each year')
        fig.update_layout(title_font=dict(size=40), title_font_color='#AD71EF', height=1000)
        st.plotly_chart(fig,use_container_width=True)


