import pandas as pd
import streamlit as st
pd.set_option('display.max_columns', None)
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image


# Streamlit part

st.set_page_config(layout= "wide")
st.title("AIRBNB DATA ANALYSIS")
st.write("")

def datafr():
    df= pd.read_csv(r"C:\Users\brijesh\Documents\Data Science cheat sheets  and study material\PYTHON GUVI PROJECTS\Airbnb\Airbnb.csv")
    return df

df= datafr()

with st.sidebar:
    select= st.selectbox("Main Menu", ["Home", "Data Exploration", "About"])

if select == "Home":

    #image1= Image.open("C:/Users/vignesh/Desktop/New folder/Airbnb image.jpg")
    #st.image(image1)

    st.header("About Airbnb")
    st.write("")
    st.write('''***Airbnb is an online marketplace that connects people who want to rent out
              their property with people who are looking for accommodations,
              typically for short stays. Airbnb offers hosts a relatively easy way to
              earn some income from their property.Guests often find that Airbnb rentals
              are cheaper and homier than hotels.***''')
    st.write("")
    st.write('''***Airbnb Inc (Airbnb) operates an online platform for hospitality services.
                  The company provides a mobile application (app) that enables users to list,
                  discover, and book unique accommodations across the world.
                  The app allows hosts to list their properties for lease,
                  and enables guests to rent or lease on a short-term basis,
                  which includes vacation rentals, apartment rentals, homestays, castles,
                  tree houses and hotel rooms. The company has presence in China, India, Japan,
                  Australia, Canada, Austria, Germany, Switzerland, Belgium, Denmark, France, Italy,
                  Norway, Portugal, Russia, Spain, Sweden, the UK, and others.
                  Airbnb is headquartered in San Francisco, California, the US.***''')
    
    st.header("Background of Airbnb")
    st.write("")
    st.write('''***Airbnb was born in 2007 when two Hosts welcomed three guests to their
              San Francisco home, and has since grown to over 4 million Hosts who have
                welcomed over 1.5 billion guest arrivals in almost every country across the globe.***''')


if select =="Data Exploration":

    tab1, tab2, tab3, tab4, tab5= st.tabs(["***PRICE ANALYSIS***",
                                           "***AVAILABILITY ANALYSIS***",
                                           "***LOCATION BASED***", 
                                           "***GEOSPATIAL VISUALIZATION***", 
                                           "***TOP CHARTS***"])

    with tab1:
        st.header("Price Analysis")
        st.write("")
        st.write("")

        col1, col2= st.columns(2)

        with col1:
            st.subheader("Price Distribution according to the property type and country")
            matrix = df.pivot_table(values="price", index="country", columns="property_type")

            # Create the heatmap
            fig = px.imshow(matrix, color_continuous_scale="viridis",height=600,width=800)
            #fig.show()
            st.plotly_chart(fig)

            
        st.subheader("Price by categorical values")
        fig3=px.box(df ,
                            x = "property_type",
                            y = "price",
                            color = "room_type",
                            title = "Price by categorical values")
        st.plotly_chart(fig3)

    # Stacked Bar chart 
        st.subheader("Price componets based on property type")
        grouped_df = df.groupby(['property_type', 'room_type'])['price'].mean().reset_index()
        fig4=px.bar(grouped_df,
                                    x="property_type",
                                    y="price",
                                    color="room_type",
                                    title="Price componets based on property type")
        st.plotly_chart(fig4)

    # 3d scatterplot: price vs bedrooms vs bathrooms
        st.subheader("Price vs. Bedrooms vs bathrooms")
        fig5=px.scatter_3d(df,
                            x="price",
                            y="bedrooms",
                            z="bathrooms",
                            color="room_type",
                            title="Price vs. Bedrooms")
        st.plotly_chart(fig5)

    # Scatterplot : price bs number of reviews 
        st.subheader("Price vs. Number of reviews")
        fig6=px.scatter(df,
                                x="price",
                                y="number_of_reviews",
                                color="room_type",
                                title="Price vs. Number of reviews")
        st.plotly_chart(fig6)


                #bar chart: average price for superhosts vs. non-superhosts
        st.subheader("Average price for superhosts vs. non-superhosts")
        fig7=px.bar(df,
                            x="host_is_superhost",
                            y="price",
                            color="room_type",
                            title="Average price for superhosts vs. non-superhosts")
        st.plotly_chart(fig7)
            
######################################################################################################################################################

    with tab2:
        
        col1,col2= st.columns(2)
        st.write("")

    with col1:
                        
        st.header("Availability Analysis")
        st.write("")
        st.write("")
        av_df= df[df["availability_365"]!=0]
        st.subheader("Availability based on beds and country")
        fig1= px.histogram(av_df, x="beds", y="country", color="country")
        st.plotly_chart(fig1)


        # scatter plot price vs availability 
        st.subheader("Price vs. Availability")
        fig2=px.scatter(df, 
                                        x="price",
                                        y="availability_365",                # 365
                                        color="room_type",
                                        title="Price vs. Availability")
        st.plotly_chart(fig2)

        st.subheader("Price vs. Availability")
        fig3=px.scatter(df, 
                                        x="price",
                                        y="availability_30",                # 30
                                        color="room_type",
                                        title="Price vs. Availability")
        st.plotly_chart(fig3)

        st.subheader("Price vs. Availability")
        fig4=px.scatter(df, 
                                        x="price",
                                        y="availability_60",                # 60
                                        color="room_type",
                                        title="Price vs. Availability")
        st.plotly_chart(fig4)

        st.subheader("Price vs. Availability")
        fig5=px.scatter(df, 
                                        x="price",
                                        y="availability_90",                # 90
                                        color="room_type",
                                        title="Price vs. Availability")
        st.plotly_chart(fig5)

                        # Heat map 
        st.subheader("Geographic view of availability using latitude and longitude")
        fig6=px.density_mapbox(df, lat="latitude", lon="longitude",  radius=5, zoom=10, mapbox_style="open-street-map")
        st.plotly_chart(fig6)
        
                
######################################################################################################################################################
    with tab3:
        st.header("location analysis")
        col1,col2=st.columns(2)
        st.write("")
        st.write("")

        with col1:
            st.subheader("Geographical view of locations")
            fig7 = px.scatter_mapbox(df, lat="latitude", lon="longitude",  zoom=10, mapbox_style="open-street-map")
            st.plotly_chart(fig7)

            st.subheader("Price Comparison by Area")
            PCA= st.selectbox("Select the country",df["country"].unique())
            df2= df[df["country"] == PCA]
            df2.reset_index(drop= True, inplace= True)
            df_a= df2.groupby(["host_neighbourhood"])["price"].mean().reset_index()

            fig8=px.bar(df_a,x="host_neighbourhood",
                        y="price",
                        color="host_neighbourhood",
                        title="Price Comparison by Area",width= 1200, height= 600)
            
            st.plotly_chart(fig8)
            
            st.subheader("Number of reviews vs the Location")
            df_h= df.groupby(["country","host_neighbourhood"])["number_of_reviews"].max().reset_index()
            #df_h.reset_index(drop= True, inplace= True)
            

            fig_bub= px.scatter(df_h, x="country", 
                               y="number_of_reviews", 
                               size="number_of_reviews", 
                               color="country",
                               hover_name="country",
                               hover_data=["number_of_reviews"], 
                               title="Number of reviews vs. Country", 
                               width= 1200, height= 600) 
                            
            st.plotly_chart(fig_bub)



            st.subheader("Average Number of Reviews by Country and Neighborhood")

            fig = px.treemap(df_h, path=[px.Constant("All"), 'country', 'host_neighbourhood'], 
                 values='number_of_reviews',
                 title='Average Number of Reviews by Country and Neighborhood')
            
            st.plotly_chart(fig)

            NLA = st.selectbox("Select the country_2", df["country"].unique())
            df3 = df[df["country"] == NLA]
            df3.reset_index(drop=True, inplace=True)

            df_b = df3.groupby(["host_neighbourhood", "room_type"])["price"].mean().reset_index()

            fig9 = px.bar(df_b,
                        x="host_neighbourhood",
                        y="price",
                        color="room_type",
                        title=f"Average Price by Neighborhood and Room Type in {NLA}",
                        labels={"price": "Average Price", "host_neighbourhood": "Neighborhood", "room_type": "Room Type"},
                        barmode="group")
            st.plotly_chart(fig9)


    with tab4:
        st.header("Geographical view of locations")
        fig7 = px.scatter_mapbox(df, lat="latitude", lon="longitude",  zoom=10, mapbox_style="open-street-map")
        st.plotly_chart(fig7)

        st.subheader("Price Comparison by Area")
        df['price_category'] = pd.cut(df['price'], 
                              bins=[-float('inf'), 100, 1000, float('inf')], 
                              labels=['Low', 'Medium', 'High'])

        
        fig8 = px.scatter_mapbox(df,
                        lat="latitude",
                         lon="longitude",
                         color="price_category",
                         color_discrete_map={'Low': 'green', 'Medium': 'yellow', 'High': 'red'},
                         hover_name="name",
                         hover_data=["price", "name"],
                         title="Price Comparison by Area",
                         width=600, 
                         height=600,
                         mapbox_style="open-street-map")

        st.plotly_chart(fig8)


        st.subheader("Number of reviews vs the Location")
        df_h = df.groupby(["country","host_neighbourhood","latitude","longitude"])["number_of_reviews"].max().reset_index()
        #df_h.reset_index(drop= True, inplace= True)
        

        fig_bub = px.scatter_mapbox(df_h, lat="latitude", 
                           lon="longitude", 
                           size="number_of_reviews", 
                           color="country",
                           hover_name="country",
                           hover_data=["number_of_reviews"], 
                           title="Number of reviews vs. Country", 
                           width= 600, height= 600,
                           mapbox_style="open-street-map") 
                        
        st.plotly_chart(fig_bub)

    with tab5:
        st.header("Top Charts")
        st.write("")
        st.write("")
        st.subheader("Top 10 properties based on number of reviews")
        top10 = df.nlargest(10, 'number_of_reviews')
        fig10 = px.bar(top10, x='name', y='number_of_reviews', title="Top 10 properties based on number of reviews")
        st.plotly_chart(fig10)

        st.subheader("Top 10 properties based on price")
        top10_2=df.nlargest(10, 'price')
        fig11= px.bar(top10_2,
                      x= 'name',
                      y= 'price',
                      title= "Top 10 properties based on price",
                      hover_data='country')
        st.plotly_chart(fig11)

        st.subheader("Top Property Types in all countries")
        Top10_4= st.selectbox("Select the country_12", df["country"].unique())
        df_10= df[df["country"] == Top10_4]
        df_10= df_10.groupby(["property_type"])["price"].max().reset_index()
        df_10 = df_10.sort_values(by="price", ascending=False).reset_index(drop=True)

        df_10.reset_index(drop=True,inplace=True)
        
        fig11=px.bar(df_10,x="property_type",
                        y="price",
                        color="property_type",
                        title="Price Comparison by Area",width= 1200, height= 600)
            
        st.plotly_chart(fig11)

        st.subheader("Top 10 properties based on stay price")
        top10_3=df.nlargest(10, 'minimum_nights')
        fig12= px.bar(top10_3,
                      x= 'name',
                      y= 'minimum_nights',
                      title= "Top 10 properties based on minimum_nights",
                      hover_data='country')
        st.plotly_chart(fig12)

        st.subheader("Top 10 costliest Property prices in each country")
        Top10_5 = st.selectbox("Select the country_5", df["country"].unique())
        df_11 = df[df["country"] == Top10_5]
        df_11 = df_11.sort_values(by="price", ascending=False).reset_index(drop=True)
        df_11 = df_11.nlargest(10, "price")  # Get the top 10 costliest properties
        
        fig13 = px.bar(df_11, x="name",  # Use name as the x-axis
                       y="price",
                       color="property_type",
                       title="Price Comparison by Property Name", width=1200, height=600)
        st.plotly_chart(fig13)

if select == "About":
    def about_page():
        st.title("About This Airbnb EDA Project")

        st.write("""
        This Exploratory Data Analysis (EDA) project on Airbnb data is designed to develop and showcase a wide range of data science and analytics skills. Through this project, I've gained hands-on experience in:
        """)

        skills = [
            "Data Manipulation using pandas",
            "Data Visualization with libraries like Matplotlib, Seaborn and Plotly",
            
            "Python Programming and efficient code writing",
            "Domain Knowledge of the short-term rental market",
            "Feature Engineering to create meaningful variables",
            "Geospatial Analysis using latitude and longitude data",
            "Time Series Analysis for identifying trends and patterns",
            "Data Storytelling to present insights clearly",
            "Critical Thinking in formulating and testing hypotheses",
            "Data Quality Assessment and ensuring data reliability",
            "Exploratory Techniques to uncover hidden patterns",
            "Business Acumen in translating data insights to recommendations",
            "Proficiency in data analysis tools and libraries",
            "Consideration of Data Ethics and privacy implications",
            
            "Clear Documentation of the analysis process",
            "Problem-Solving skills in overcoming data challenges"
        ]

        st.write("Key skills developed:")
        for skill in skills:
            st.write(f"- {skill}")

        st.write("""
        This project provided invaluable experience in applying these skills to real-world data, 
        enhancing my capabilities as an aspiring data scientist/analyst. The insights gained from 
        this analysis can be used to understand pricing trends, popular locations, and factors 
        influencing customer choices in the Airbnb market.
        """)

        st.write("""
        For more information about this project or to connect with me, please visit my GitHub profile 
        or LinkedIn page. https://www.linkedin.com/in/brijeshanuj/ 
                          https://github.com/brijesh2202
        """)


    about_page()
        

        

    
        


            
            
            











    
            
            








