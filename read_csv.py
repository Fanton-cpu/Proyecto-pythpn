import csv

def fish_csv(path):
    with open(path, 'r') as csvfish:
        reader = csv.reader(csvfish, delimiter=',' )
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            length_metering = {key: value for key, value in iterable}
            data.append(length_metering)
        return data 
    
if __name__ == '__main__':
        data = fish_csv('./Analisis/Fish.csv')
        print(data[0])