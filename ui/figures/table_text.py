import matplotlib.pyplot as plt
class TableText:
    def __init__(self, name=None, list_table=None):
        self.name = name
        self.list_table = list_table
""""
        from matplotlib import pyplot as plt
        data_values = list(map(lambda x:x.speed_value + " " + x.speed_unit, list_table))
        data_name = list(map(lambda x:x.name, list_table))
        rows = ['', '']
        columns = [data_values, data_name]
        fig=plt.figure()
        ax = plt.gca()
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        self.table = ax.table(cellText=[],
                              rowLabels=rows,
                              rowColours=None,
                              colLabels=columns,
                              loc='bottom')

        print("")"""
