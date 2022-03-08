from json import tool


tools = {
    'Python': {
        '2015': 9,
        '2016': 22,
        '2017': 27,
        '2018': 32,
        '2019': 35,
    },
    'JavaScript': {
        '2015': 8,
        '2016': 18,
        '2017': 12,
        '2018': 6,
        '2019': 15,
    },
    'Twitter': {
        '2015': 10,
        '2016': 18,
        '2017': 26,
        '2018': 16,
        '2019': 12,
    },
    'GitHub': {
        '2015': 2,
        '2016': 6,
        '2017': 17,
        '2018': 5,
        '2019': 10,
    },
    'Gephi': {
        '2015': 11,
        '2016': 16,
        '2017': 14,
        '2018': 10,
        '2019': 9,
    },
    'GeoNames': {
        '2015': 2,
        '2016': 4,
        '2017': 3,
        '2018': 1,
        '2019': 8,
    },
    'Transkribus': {
        '2015': 0,
        '2016': 1,
        '2017': 2,
        '2018': 1,
        '2019': 8,
    },
    'Excel': {
        '2015': 5,
        '2016': 9,
        '2017': 3,
        '2018': 6,
        '2019': 7,
    },
    'MySQL': {
        '2015': 0,
        '2016': 6,
        '2017': 9,
        '2018': 5,
        '2019': 7,
    },
}





def tool_function(tools, name):
    sum = 0
    for value in tools[name]:
        sum = tools[name][value] + sum
    return sum
    
print(tool)

class DHTool:
    """Contains methods for maintaining data related to a dh tool

    Methods:
    --------
    add_authors
    add_year_popularity
    calculate_total_popularity
    """
    def __init__(self, name):
        self.tool_name = name
        self.authors = list()
        self.year_values = dict()
        self.total_value = 0


    def add_authors(self, authors):
        """Adds a list of authors of the DH Tool

        Method argument:
        -----------------
        authors(list) -- A list of people who built the dh tool
        """
        if isinstance(authors, list) is False:
            authors = [authors]

        self.authors.extend(authors)


    def add_year_popularity(self, year, value):
        """Adds the popularity value for each year of the DH tool

        Method argument:
        -----------------
        year(integer or string) -- A year 
        value(integer) - Popularity value
        """

        self.year_values[str(year)] = value


    def calculate_total_popularity(self):
        """Calculate the total popularity for a tool
        """

        self.total_popularity = sum(self.year_values.values())
        print(self.total_popularity)

    def get_tool_info(self):
        print(self.__dict__)



a_tool = DHTool("Python")
a_tool.add_authors("Guido van Rossum")
a_tool.add_year_popularity(2015, 9)
a_tool.calculate_total_popularity()
#print(a_tool.total_popularity)

#print(a_tool.add_year_popularity.__doc__) # To view the docstring for the method


print(a_tool.get_tool_info())

sec_tool = DHTool('Github')
sec_tool.add_authors(['Chris Wanstrath','P. J. Hyett','Tom Preston-Werner','Scott Chacon'])
sec_tool.add_year_popularity(2015, 2)
sec_tool.add_year_popularity(2016, 6)
sec_tool.add_year_popularity(2017, 17)
sec_tool.calculate_total_popularity()


print(sec_tool.get_tool_info())