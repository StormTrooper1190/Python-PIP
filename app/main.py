import utils
import read_csv
import charts
import pandas as pd

#keys, values = utils.get_population()
#print(keys, values)

'''
data = [
  {
    'Country': 'Colombia',
    'Population': 500
  },
  {
    'Country': 'Bolivia',
    'Population': 300
  }
]
'''
def run():
  '''
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  '''
  df = pd.read_csv('data.csv')
  df= df[df['Continent'] == 'Africa']

  countries = df['Country/Territory'].values
  percentges = df['World Population Percentage'].values

  charts.generate_pie_chart(countries, percentges)

  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')
  
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
  
  #print(data[0])


if __name__ == '__main__':
  run()