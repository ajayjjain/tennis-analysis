import csv
import pandas as pd

filename_prefix = "atp_matches_" # change your prefix to your matches directory
filename_suffix = ".csv"
player_last_name = "federer" # last name for the tennis player you are obtaining statistics for 
player_output_file_prefix = "player_output/" + player_last_name # change prefix to your directory
tennis_player = "Roger Federer" # tennis player you are pulling game statistics for

start_year = 1998 # change to year your player went pro on the tennis circuit
end_year = 2018

def sort(filename):
    df = pd.read_csv(filename)
    df = df.sort('player_age')
    df.to_csv(filename, index=False)

def write_player_header():
    write_file_name = player_output_file_prefix + filename_suffix
    read_header_file_name = "header.csv"
    with open(read_header_file_name, 'rb') as infile:
        with open(write_file_name, 'ab') as outfile:
                writer = csv.writer(outfile)
                for line in csv.reader(infile):
                    writer.writerow(line)
   
def write_player_output(year):
    read_file_name = filename_prefix + str(year) + filename_suffix
    with open(read_file_name, 'rb') as infile:
         with open(write_file_name, 'ab') as outfile:
            writer = csv.writer(outfile)
            for line in csv.reader(infile):
                if tennis_player in line:
                   if line[10] == tennis_player:
                       line = line[:17] + line[27:40]
                   else:
                       line = line[:7] + line[17:31] + line[40:]
                   writer.writerow(line)
         sort(write_file_name)


         
write_player_header()
for year in xrange(start_year, end_year):
    write_file_name = player_output_file_prefix + filename_suffix
    write_player_output(year)
 

