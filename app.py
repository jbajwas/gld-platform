import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

from queries import QueryService

st.set_page_config(
    page_title="GLD Platform",
    page_icon="📊",
    layout="wide"
)


@st.cache_data(ttl=300, show_spinner="Loading data...")
def load_data():
    qs = QueryService.get_instance()
    return qs.get_gld_availability()


df = load_data()

gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_default_column(
    filterable=True,
    sortable=True,
    resizable=True,
    filter=True,
    type=["rightAligned"]
)
gb.configure_grid_options(
    suppressPaginationPanel=True,
    multiSortKey="ctrl"
)
gb.configure_column("country", sort="asc", sortIndex=0, type=["rightAligned"])
gb.configure_column("year", sort="asc", sortIndex=1, type=["rightAligned"])
gb.configure_column("survey", type=["rightAligned"])
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

st.caption("**Desktop:** Hold **Ctrl** (Windows) or **⌘ Cmd** (Mac) + click column headers to add multiple sort levels")
