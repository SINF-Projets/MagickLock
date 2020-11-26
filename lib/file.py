#!/usr/bin/python3
# -*- coding: utf-8 -*

"""
Librairie d'accès d'utilisation de fichiers rendue disponible pour le P3 du cours de LINFO1001.

Cette librairie est utilisée pour remplacer les fonctionnalités indisponibles au sein du simulateur https://trinket.io/sense-hat.
"""

def read(filename):
	"""
	Lis le contenu d'un fichier et le retourne sous forme de string.

	:param: (str) filename: le nom du fichier à lire
	:return: (str): le contenu complet du fichier
	"""
	with open(filename) as file:
		return file.read().strip()

def write(filename, text):
	"""
	Ecris un texte au sein d'un fichier.

	:param: (str) filename: le nom du fichier dans lequel écrire
	:param: (str) text: le texte à écrire
	"""
	with open(filename, "w") as file:
		file.write(text)

def append(filename, text):
	"""
	Rajoute un texte à la suite d'un fichier.

	:param: (str) filename: le nom du fichier dans lequel écrire
	:param: (str) text: le texte à écrire
	"""
	with open(filename, "a") as file:
		file.write(text.strip())

def exists(filename):
	"""
	Vérifie si un fichier existe dans le simulateur. Un fichier vide est considéré comme non existant.

	:param: (str) filename: le nom d'un fichier à vérifier
	:return: (bool): True si le fichier existe, False sinon
	"""
	try:
		return read(filename) != ""
	except IOError:
		return False

def delete(filename):
	"""
	Supprime un fichier dans le simulateur. Un fichier vide est considéré comme supprimé.

	:param: (str) filename: le nom d'un fichier à supprimer
	"""
	write(filename, "")
