import unittest
import matplotlib.pyplot as plt
from sea_level_predictor import draw_plot

class TestSeaLevelPredictor(unittest.TestCase):

    def test_title(self):
        # Create the plot
        draw_plot()
        
        # Retrieve the title from the plot
        title = plt.gca().get_title()
        self.assertEqual(title, 'Rise in Sea Level')

    def test_labels(self):
        draw_plot()
        
        # Check x and y labels
        xlabel = plt.gca().get_xlabel()
        ylabel = plt.gca().get_ylabel()
        
        self.assertEqual(xlabel, 'Year')
        self.assertEqual(ylabel, 'Sea Level (inches)')

    def test_data_points(self):
        draw_plot()
        
        # Check the data points in the plot
        scatter = plt.gca().collections[0]
        data_points = scatter.get_offsets()
        
        # Check if there are any data points (just an example, adjust as necessary)
        self.assertGreater(len(data_points), 0)

    def test_line_of_best_fit(self):
        draw_plot()
        
        # Ensure there's a line in the plot (we are just checking for one line here)
        lines = plt.gca().get_lines()
        self.assertGreater(len(lines), 0)

if __name__ == '__main__':
    unittest.main()
