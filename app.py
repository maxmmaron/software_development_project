import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Set page config
st.set_page_config(page_title="US Vehicle Listings Analysis", layout="wide")

# Add title with markdown styling
st.markdown("# 🚗 US Vehicle Listings Analysis")

# Load data with error handling
@st.cache_data  # Cache the data loading
def load_data():
    try:
        df = pd.read_csv('./cleaned_vehicles_us.csv')
        return df
    except FileNotFoundError:
        st.error("Data file not found. Please ensure 'cleaned_vehicles_us.csv' is in the correct directory.")
        return None
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

df = load_data()

if df is not None:
    # First visualization: Vehicle types by brand
    st.subheader('📊 Distribution of Vehicle Types by Brand')
    fig1 = px.histogram(
        df, 
        x='manufacturer', 
        color='type',
        title='Vehicle Types Distribution by Manufacturer',
        labels={'manufacturer': 'Manufacturer', 'type': 'Vehicle Type'},
        height=500
    )
    fig1.update_layout(bargap=0.1)
    st.plotly_chart(fig1, use_container_width=True)

    # Second visualization: Price distribution comparison
    st.subheader('💰 Price Distribution Comparison')
    col1, col2 = st.columns(2)
    with col1:
        manufacturer1 = st.selectbox('Select First Manufacturer', 
                                   sorted(df['manufacturer'].unique()), 
                                   index=0)
    with col2:
        # Ensure second manufacturer is different from the first
        other_manufacturers = sorted([x for x in df['manufacturer'].unique() if x != manufacturer1])
        manufacturer2 = st.selectbox('Select Second Manufacturer', 
                                   other_manufacturers,
                                   index=0)
    
    normalized = st.checkbox('Show Normalized Distribution', value=True)
    
    # Create price distribution comparison
    hist_data = []
    for mfr in [manufacturer1, manufacturer2]:
        hist_data.append(
            go.Histogram(
                x=df[df['manufacturer'] == mfr]['price'],
                name=mfr,
                opacity=0.75,
                histnorm='percent' if normalized else None
            )
        )
    
    fig2 = go.Figure(data=hist_data)
    fig2.update_layout(
        barmode='overlay' if normalized else 'group',
        title='Price Distribution Comparison',
        xaxis_title='Price ($)',
        yaxis_title='Percentage' if normalized else 'Count',
        height=500
    )
    st.plotly_chart(fig2, use_container_width=True)

    # Third visualization: Scatter plot matrix
    st.subheader('📈 Multi-dimensional Analysis')
    
    # Filter to only numeric columns for scatter matrix
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    if len(numeric_cols) >= 3:
        # Allow selection of multiple dimensions
        selected_dims = st.multiselect(
            'Select dimensions for analysis (select 3-4 dimensions)',
            numeric_cols,
            default=numeric_cols[:3]  # Default to first 3 numeric columns
        )
        
        color_var = st.selectbox(
            'Select color variable',
            df.columns,
            index=df.columns.get_loc('manufacturer') if 'manufacturer' in df.columns else 0
        )
        
        if len(selected_dims) >= 2:
            fig3 = px.scatter_matrix(
                df,
                dimensions=selected_dims,
                color=color_var,
                title=f'Scatter Plot Matrix colored by {color_var}',
                height=800
            )
            fig3.update_traces(diagonal_visible=False)
            st.plotly_chart(fig3, use_container_width=True)
        else:
            st.warning("Please select at least 2 dimensions for the scatter plot matrix.")
    else:
        st.error("Not enough numeric columns for scatter plot matrix analysis.")

    # Add data summary
    st.subheader("📝 Data Summary")
    st.write(f"Total number of vehicles: {len(df):,}")
    st.write(f"Number of manufacturers: {df['manufacturer'].nunique():,}")
    st.write(f"Price range: ${df['price'].min():,.2f} - ${df['price'].max():,.2f}")
