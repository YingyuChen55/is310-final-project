# importing
import pandas as pd

# read the df
df = pd.read_csv('https://zoeleblanc.com/is310-computing-humanities/assets/files/tools_dh_proceedings.csv')

# 1. next top ten tools based on 2019
df_2019 = df[['Tool','2019']]
df_2019_sorted = df_2019.sort_values(by=['2019'],ascending=False)

first_ten = df_2019_sorted.iloc[:10]
next_top_ten = df_2019_sorted.iloc[10:20]

print('The top ten tools are')
print(first_ten)

print('The next top ten tools are')
print(next_top_ten)

# 2. total field for next ten based on 2019
df['total'] = df['2015'] + df['2016'] + df['2017'] + df['2018'] + df['2019']
tools = [name for name in next_top_ten['Tool']]
df_2019_info = df[df.Tool.isin(tools)]
df_2019_info = df_2019_info.sort_values(by=['2019'],ascending=False)

print('other information about the next top ten')
print(df_2019_info)


# 3. def by name
def info_by_name_pd(name):
    return df[df['Tool']==name]

def info_by_name_v2(name):
    for tools in df['Tool']:
        if tools == name:
            return df[df['Tool']==name]
        else:
            None
print("let's try python!")
print(info_by_name_v2('Python'))

# bonus try
def top_tool_by_year(year):
    df_year = df[['Tool',year]]
    df_year = df_year.sort_values(by=year, ascending=False)
    return df_year[:1]

print("let's try 2019!")
print('the top tool for 2019 is')
print(top_tool_by_year('2019')['Tool'])