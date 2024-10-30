def tally(rows):
    #Defined a List to collect the data from row
    table_database = []

    #Create header adds the header to the table
    final_table = create_header()

    #if empty the table can just be returned
    if rows == []:
        return final_table

    #loops through rows and splits into lists these lists are added to the database creating a 2d array
    for row in rows:
        row = prep_row(row)
        results = add_row(row,table_database)

    #sorts the retults first alphabetically then numerically to provide table as indicated
    sorted_results = sort_results(results)

    #Formats rows as per requested in results
    for row in sorted_results:
        final_table.append(
            row[0]
            +' '*(31-len(row[0]))
            +'| '+str(row[1]+row[2]+row[3])
            +' |'
            +' '*(3-len(str(row[1])))
            +str(row[1])
            +' |  '+str(row[2])
            +' |  '+str(row[3])
            +' |'+' '*(3-len(str(3*row[1]+row[2])))
            +str(3*row[1]+row[2])
            )
        
    return final_table

#Simple function that appends header to table 
def create_header():
    table = []
    table.append('Team                           | MP |  W |  D |  L |  P')
    return table

#I split the row into list to look at individual elements of the given data
def prep_row(row):
    prepared_row = row.split(';')
    return prepared_row

#Checks to see if row is already in database, add if isnt, and tallies W,L and D yes this is stupid way of doing this and i'd probably get fired from any job :)
def add_row(row,table_database):

    if all(row[0] not in table_entry for table_entry in table_database):
        table_database.append([row[0],0,0,0])
        
    if all(row[1] not in table_entry for table_entry in table_database):
        table_database.append([row[1],0,0,0])

    for table_entry in table_database:
        if row[2] == 'Win' and row[0] in table_entry:
            table_entry[1] += 1
            for table_entry in table_database:
                if row[1] in table_entry:
                    table_entry[3] +=1
        
        if row[2] == 'Draw' and row[0] in table_entry:
            table_entry[2] += 1  
            
        if row[2] == 'Draw' and  row[1] in table_entry:   
            table_entry[2] += 1
            
        if row[2] == 'Loss' and row[0] in table_entry:
            table_entry[3] +=1
            for table_entry in table_database:
                if row[1] in table_entry:
                    table_entry[1] +=1 
                    
    return table_database

#sorts as per above comment when func is called
def sort_results(results):
    
    alphabetical_teams = sorted(results, key=lambda x: x[0])
    sorted_teams = sorted(alphabetical_teams,key = lambda x:3*x[1]+x[2], reverse=True)
    return sorted_teams

results = [
    'Glasgow;Leinster;Loss',
    'Glasgow;Ospreys;Win',
    'Glasgow;Cardiff;Draw',
    'Glasgow;Munster;Loss',
    'Glasgow;Edinburgh;Win',
    'Glasgow;Ulster;Loss',
    'Glasgow;Scarlets;Win',
    'Glasgow;Benetton;Draw',
    'Glasgow;Connacht;Win',
    'Glasgow;Dragons;Loss',
    'Glasgow;Zebre;Win',
    'Leinster;Ospreys;Win',
    'Leinster;Cardiff;Win',
    'Leinster;Munster;Loss',
    'Leinster;Edinburgh;Win',
    'Leinster;Ulster;Win',
    'Leinster;Scarlets;Draw',
    'Leinster;Benetton;Win',
    'Leinster;Connacht;Win',
    'Leinster;Dragons;Win',
    'Leinster;Zebre;Win',
    'Ospreys;Cardiff;Win',
    'Ospreys;Munster;Loss',
    'Ospreys;Edinburgh;Win',
    'Ospreys;Ulster;Loss',
    'Ospreys;Scarlets;Draw',
    'Ospreys;Benetton;Win',
    'Ospreys;Connacht;Win',
    'Ospreys;Dragons;Win',
    'Ospreys;Zebre;Win',
    'Cardiff;Munster;Loss',
    'Cardiff;Edinburgh;Draw',
    'Cardiff;Ulster;Loss',
    'Cardiff;Scarlets;Loss',
    'Cardiff;Benetton;Win',
    'Cardiff;Connacht;Loss',
    'Cardiff;Dragons;Win',
    'Cardiff;Zebre;Draw',
    'Munster;Edinburgh;Win',
    'Munster;Ulster;Win',
    'Munster;Scarlets;Win',
    'Munster;Benetton;Win',
    'Munster;Connacht;Win',
    'Munster;Dragons;Win',
    'Munster;Zebre;Win',
    'Edinburgh;Ulster;Draw',
    'Edinburgh;Scarlets;Draw',
    'Edinburgh;Benetton;Win',
    'Edinburgh;Connacht;Loss',
    'Edinburgh;Dragons;Win',
    'Edinburgh;Zebre;Win',
    'Ulster;Scarlets;Draw',
    'Ulster;Benetton;Win',
    'Ulster;Connacht;Win',
    'Ulster;Dragons;Win',
    'Ulster;Zebre;Win',
    'Scarlets;Benetton;Loss',
    'Scarlets;Connacht;Win',
    'Scarlets;Dragons;Win',
    'Scarlets;Zebre;Win',
    'Benetton;Connacht;Win',
    'Benetton;Dragons;Win',
    'Benetton;Zebre;Win',
    'Connacht;Dragons;Win',
    'Connacht;Zebre;Win',
    'Dragons;Zebre;Win'
]
league_table = tally(results)



for team in league_table:
    print(team)