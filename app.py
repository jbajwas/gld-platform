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

grid_response = AgGrid(
    df,
    gridOptions=grid_options,
    update_mode=GridUpdateMode.FILTERING_CHANGED,
    enable_enterprise_modules=False,
    height=600,
    theme="streamlit"
)

filtered_count = len(grid_response["data"])
total_count = len(df)
if filtered_count == total_count:
    row_info = f"<strong>{total_count}</strong> rows"
else:
    row_info = f"<strong>{filtered_count}</strong> of <strong>{total_count}</strong> rows"

sort_hint = "<strong>Desktop:</strong> Hold <strong>Ctrl</strong> (Windows) or <strong>⌘ Cmd</strong> (Mac) + click column headers to add multiple sort levels"
st.markdown(
    f'<div style="display: flex; justify-content: space-between; font-size: 0.875rem; color: rgba(49, 51, 63, 0.6);">'
    f'<span>{row_info}</span>'
    f'<span>{sort_hint}</span>'
    f'</div>',
    unsafe_allow_html=True
)
