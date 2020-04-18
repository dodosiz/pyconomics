import matplotlib.pyplot as pl

class BaseGraph:
    """
    A base class to create objects for graphical representations.
    Attributes:
        x_data - an array with numbers for the x-axis
        y_data - an array with numbers for the y-axis
        x_name(optional) - a name for the x-axis
        y_name(optional) - a name for the y-axid
    """
    def __init__(self, x_data, y_data, x_name = "", y_name = ""):
        self.x_data = x_data
        self.y_data = y_data
        self.x_name = x_name
        self.y_name = y_name
    
    def render(self, mode):
        """
        Renders the graph based on the difined data for x and y axis.
        Attributes:
            mode the representation of the graph for example
            'r-' red and linear
            'bo' blue and with circles on the data points
            'r--' red and dashed
        """
        fig, ax = pl.subplots()
        ax.plot(self.x_data, self.y_data, mode)
        ax.set_xlabel(self.x_name)
        ax.set_ylabel(self.y_name)
        pl.show()