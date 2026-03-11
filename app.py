import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

from queries import QueryService

st.set_page_config(
    page_title="GLD Platform",
    page_icon="📊",
    layout="wide"
)


@st.cache_data(ttl=300)
def load_data():
    qs = QueryService.get_instance()
    return qs.get_gld_availability()


df = load_data()

gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_default_column(
    filterable=True,
    sortable=True,
    resizable=True,
    filter=True
)
gb.configure_grid_options(suppressPaginationPanel=True)
gb.configure_side_bar(filters_panel=True, columns_panel=True)
grid_options = gb.build()

AgGrid(
    df,
    gridOptions=grid_options,
    update_mode=GridUpdateMode.FILTERING_CHANGED,
    enable_enterprise_modules=False,
    height=600,
    theme="streamlit"
)
