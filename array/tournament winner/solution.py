
competitions= [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
  ]
results= [0, 0, 1]

def tournamentWinner(competitions, results):
  home_teams = []
  away_teams =[]
  Score_sheet ={}
  best_team = competitions[0][0]
  for row in competitions:
    home_teams.append(row[0])
    away_teams.append(row[1])
    for member in row:
      if member not in Score_sheet:
        Score_sheet.update({member:0})
  for i in range(len(results)):
    result = results[i]
    if result == 0: # away team wins
      Score_sheet[away_teams[i]] += 3  
      if Score_sheet[away_teams[i]] > Score_sheet[best_team]:
        best_team = away_teams[i]
    else:
      Score_sheet[home_teams[i]] += 3 
      if Score_sheet[home_teams[i]] > Score_sheet[best_team]:
        best_team = home_teams[i]
  return best_team
      

print(tournamentWinner(competitions,results))
