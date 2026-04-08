import streamlit as st
from streamlit.testing.v1 import AppTest

def test_button_increments_counter():
    """Test that the counter increments when the button is clicked."""
    at = AppTest.from_file("app.py").run()
    at.session_state.count = 1
    # Note: click().run() is necessary to trigger the callback logic
    at.button(key="increment").click().run()
    assert at.session_state.count == 2

def test_button_decrements_counter():
    """Test that the decrement button works."""
    at = AppTest.from_file("app.py").run()
    at.session_state.count = 5
    at.button(key="decrement").click().run()
    assert at.session_state.count == 4

def test_decrement_stops_at_zero():
    """Test that count does not fall below 0 (the specific logic in your decrement function)."""
    at = AppTest.from_file("app.py").run()
    at.session_state.count = 0
    at.button(key="decrement").click().run()
    assert at.session_state.count == 0

def test_button_increments_counter_ten_x():
    """Test that the increment button works in ten_x mode."""
    at = AppTest.from_file("app.py").run()
    # Check the 10x mode checkbox inside the expander
    at.checkbox(key="ten_x").check().run()
    at.button(key="increment").click().run()
    assert at.session_state.count == 10

def test_button_decrements_counter_ten_x():
    """Test that the decrement button works in ten_x mode."""
    at = AppTest.from_file("app.py").run()
    at.session_state.count = 15
    at.checkbox(key="ten_x").check().run()
    at.button(key="decrement").click().run()
    assert at.session_state.count == 5

def test_output_text_correct():
    """Test that the text shows the correct value from st.write."""
    at = AppTest.from_file("app.py").run()
    at.session_state.count = 11
    at.run() 
    # In your app.py, the count is the first markdown/text element
    assert at.markdown[0].value == "Total count is 11"