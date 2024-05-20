import re

FILENAME = "/home/lollo/Cities/worldcities.csv"

def read_csv(filename):
    """this function reads a csv file and returns a list of dictionary 
       where each line is a dictionary 
    """
    cities = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        count =0
        cities_dict = {}
        for raw_line in lines:
            line = raw_line.rstrip()                        #rstrip removes /n from the end of each line
            if count ==0:
                key_list = []
                for k in line.split(','):
                    key = re.sub(r'^"|"$','', k )
                    key_list.append(key)

            else:
                value_list = []
                for v in line.split(','):
                    value = re.sub(r'^"|"$','', v)               #re.sub removes double quotes from each word
                    value_list.append(value)
      
                if len(value_list) == len(key_list):  # we check if last read value list is consistent with keys
                    cities_dict = dict(zip(key_list,value_list))
                    cities.append(cities_dict)
                else:
                    
                    print(f'inconsistent number of fields in line: {count}: got:{len(value_list)} expected:{len(key_list)} line ignored')
          
            count +=1    
            cities.append(cities_dict)
    return cities

def filter_data_by_field(data):
    

    filtered_data = {}

    for row_dict in data:
        for k, v in row_dict.items():
            if k == 'country':
                if v != '24.9408':
                    filtered_data[v] = [row_dict['iso2'],row_dict['iso3']]


    return filtered_data

def main():
    

    city_list = read_csv(FILENAME)
    my_country = filter_data_by_field(city_list)

    for k,v in my_country.items():
        print(f"{k}:{v}")
    
    #for i in city_list:
        #print(i)

if __name__ == "__main__":
    main()