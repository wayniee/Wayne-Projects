import streamlit as st
from tabs.tab1b import load_data, display_tab1
from tabs.tab2b import load_data_tab2, display_tab2
from tabs.tab3b import load_data_tab3, display_tab3


def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(
        page_title="Subgroup B",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    st.page_link("Hello.py", label="⬅ BACK")
    st.markdown("# Subgroup B")

    tab1, tab2, tab3 = st.tabs(
        ["📈 Demand Forecast", "💰 Pricing Strategies", "🚚 Supply Chain Efficiency"]
    )

    # Load data
    actual_data, forecast_data, products = load_data()
    data_tab2 = load_data_tab2()
    data_tab3 = load_data_tab3()

    # Display content for tab1
    display_tab1(tab1, actual_data, forecast_data, products)

    # Display content for tab2
    display_tab2(tab2, data_tab2)

    display_tab3(tab3, data_tab3)


if __name__ == "__main__":
    main()
