import pytest
import pandas as pd
import os
import main

# Test 1: Ensure data is loaded correctly
def test_data_loading():
    yearly_stats = main.preprocess_data()
    assert not yearly_stats.empty, "Data loading failed: No data found."


# Test 3: Check if plot image is generated
def test_plot_generation():
    assert os.path.exists("plot.png"), "plot.png not generated"
