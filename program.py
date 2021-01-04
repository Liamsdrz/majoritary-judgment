#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import random

# Initialize seed so we always get the same result between two runs.
# Comment this out if you want to change results between two runs.
# More on this here: http://stackoverflow.com/questions/22639587/random-seed-what-does-it-do
random.seed(0)

##################################################
#################### VOTES SETUP #################
##################################################

VOTES = 100000
MEDIAN = VOTES / 2
CANDIDATES = {
    "hermione": "Hermione Granger",
    "balou": "Balou",
    "chuck-norris": "Chuck Norris",
    "elsa": "Elsa",
    "gandalf": "Gandalf",
    "beyonce": "Beyoncé"
}

MENTIONS = [
    "A rejeter", "Insuffisant", "Passable", "Assez Bien", "Bien", "Très bien",
    "Excellent"
]


def create_votes():
    return [{
        "hermione": random.randint(3, 6),
        "balou": random.randint(0, 6),
        "chuck-norris": random.randint(0, 2),
        "elsa": random.randint(1, 2),
        "gandalf": random.randint(3, 6),
        "beyonce": random.randint(2, 6)
    } for _ in range(0, VOTES)]


##################################################
#################### FUNCTIONS ###################
##################################################


def initialisation_tableau_candidats(liste_candidats, mentions):
  '''
  Permet de générer un tableau de candidats avec leur mentions
  '''
  candidats = dict()
  for key_candidat in liste_candidats.keys():
    candidats.update({key_candidat : [0]*len(mentions)})
  return candidats      


def ajout_de_votes(tab_candidats,votes):    
  '''
  Permet de comptabiliser les votes pour les mentions de chaque candidat
  '''
  for voix in votes:
    for nom, mention in voix.items():
      tab_candidats[nom][mention] += 1
  return tab_candidats


def repartition_des__scores(ajout_votes,med,candidats):
  '''
  Permet d'obtenir le score d'un candidat avec la mention correspondante
  '''
  score = 0
  tab_score = dict()
  for nom,liste_votes in ajout_votes.items():
    for i in range(len(candidats)):
      if score <= med:
        score += liste_votes[i]
      else:
        tab_score.update({candidats[nom] : [score,i]})
        score=0
        break
  return tab_score


def scores_en_ordre(repartition_scores):
  '''
  Permet de classer les candidats des mieux notés aux moins bien notés.
  '''
  sort_list = list()
  for item in repartition_scores.items():
   sort_list.append(item)
  for i in range(len(sort_list)-1):
    for j in range(len(sort_list)-1):
      if sort_list[j][1][1] <= sort_list[j+1][1][1]:
        sort_list[j],sort_list[j+1] = sort_list[j+1],sort_list[j]
  return sort_list


def affichage_scores(score_ordre,candidats,mentions,votes):
  '''
  Affiche le résultat final des élections
  '''
  donnees_affichage = dict()
  annonce_gagnant = list()
  for i in range(len(score_ordre)) :
    donnees_affichage.update(
      {
      score_ordre[i][0] : f' a obtenu {round((score_ordre[i][1][0]*100)/votes,2)}% de mentions {mentions[score_ordre[i][1][1]]}'
      }) 
  for nom,score in donnees_affichage.items():
    annonce_gagnant.append(f"{nom} {score}")
  print(f"Gagnant : {annonce_gagnant[0]} ")
  for i in range(1,len(annonce_gagnant)):
    print(annonce_gagnant[i])

##################################################
#################### MAIN FUNCTION ###############
##################################################


def main():
    votes = create_votes()
    tableau_candidats = initialisation_tableau_candidats(CANDIDATES, MENTIONS)
    ajout_votes = ajout_de_votes(tableau_candidats,votes)
    repartition_scores = repartition_des__scores(ajout_votes,MEDIAN,CANDIDATES)
    high_score = scores_en_ordre(repartition_scores)
    affich_score = affichage_scores(high_score,CANDIDATES,MENTIONS,VOTES)

if __name__ == '__main__':
    main()
