# -*- coding: utf-8 -*-
from odoo import models, fields, api

class EquipeProjet(models.Model):
	_name = 'revue.projet'
	_description = "Revue Projet"
	
	nomduprojet = fields.Char(string = "Nom du projet")
	nouvellemissions = fields.Char(string = "Nouvelle Missions")
	entreesconfirmeesforcast = fields.Char(string = "Entrées confirmées + forcast")
	departreelforecast = fields.Char(string = "Départ réel + forecast")
	otdmoyen = fields.Char(string = "OTD moyen")
	rftmoyen = fields.Char(string = "RFT Moyen")
	teamcompliance = fields.Char(string = "Team compliance")
	tauxdecroissancecumule = fields.Char(string = "Taux de croissance cumulé")
	tauxdattributioncumule = fields.Char(string = "Taux d'attribution cumulé")
	teamcompliance = fields.Char(string = "Team compliance")
	nombredicenfindemois = fields.Char(string = "Nombre d'IC en fin de mois")
	tauxdintercontratcumule = fields.Char(string = "taux d'intercontrat cumulé")
	daterevue = fields.Date(string = "Date de revue")
	