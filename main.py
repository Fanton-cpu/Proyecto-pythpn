import utils
import read_csv
import charts

def run():
    fish = read_csv.fish_csv('./Analisis/Fish.csv')
    fish = list(filter(lambda metering: metering['Weight'] == '242', fish))
    
    specie = list(lambda x:x[utils.species_by_length(specie= '')])
    metering = utils.length( length_metering = 'Lenght1')
    charts.generate_bar_chart(specie,metering)

    
if __name__ == '__main__':
    run()