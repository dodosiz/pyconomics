import matplotlib.pyplot as pl

class SingleGraph:
    """
    A base class to create objects for graphical representations of a single plot.
    Attributes:
        x_data - an array with numbers for the x-axis
        y_data - an array with numbers for the y-axis
    """
    def __init__(self, x_data, y_data, title):
        self.x_data = x_data
        self.y_data = y_data
        self.title = title
    
    def render(self, x_name = "", y_name = ""):
        """
        Renders a single graph.
        Attributes:
            x_name(optional) - a name for the x-axis
            y_name(optional) - a name for the y-axid
        """
        fig, ax = pl.subplots()
        ax.plot(self.x_data, self.y_data)
        ax.set_xlabel(x_name)
        ax.set_ylabel(y_name)
        ax.grid(True)
        ax.set_title(self.title)
        pl.show()

class DualGraph:
    """
    A class to create objects for graphical representations with two plots.
    Attributes:
        plot_1 a single graph object for the first plot
        plot_2 a single graph object for the second plot
    """
    def __init__(self, plot_1, plot_2, title):
        self.plot_1 = plot_1
        self.plot_2 = plot_2
        self.title = title
        
    def render(self, x_name = "", y_name = ""):
        """
        Renders two graphs together.
        Attributes:
            x_name(optional) - a name for the x-axis
            y_name(optional) - a name for the y-axid
        """
        fig, ax = pl.subplots()
        ax.plot(self.plot_1.x_data, self.plot_1.y_data, label=self.plot_1.title)
        ax.plot(self.plot_2.x_data, self.plot_2.y_data, label=self.plot_2.title)
        ax.set_xlabel(x_name)
        ax.set_ylabel(y_name)
        ax.grid(True)
        ax.set_title(self.title)
        ax.legend()
        pl.show()
        
        