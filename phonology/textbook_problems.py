# -*- coding: utf-8 -*-
from problems import *


# Oden's Introducing Phonology
Odden_Problems = []

Odden_Problems.append(Problem(
	u'''
Russian Odden 68-69''',
	[
	# Nominative sg		Genitive sg  		Gloss
	(u"vagon",			u"vagona"),			# wagon
	(u"avtomobil^y",	u"avtomobil^ya"),	# car
	(u"večer",			u"večera"),			# evening
	(u"muš",			u"muža"),			# husband
	(u"karandaš",		u"karandaša"),		# pencil
	(u"glas",			u"glaza"),			# eye
	(u"golos",			u"golosa"),			# voice
	(u"ras",			u"raza"),			# time
	(u"les",			u"lesa"),			# forest
	(u"porok",			u"poroga"),			# threshold
	(u"vrak",			u"vraga"),			# enemy
	(u"urok",			u"uroka"),			# lesson
	(u"porok",			u"poroka"),			# vice
	(u"t^svet",			u"t^sveta"),		# color
	(u"prut",			u"pruda"),			# pond
	(u"soldat",			u"soldata"),		# soldier
	(u"zavot",			u"zavoda"),			# factory
	(u"xlep",			u"xleba"),			# bread
	(u"grip",			u"griba"),			# mushroom
	(u"trup",			u"trupa"),			# corpse
	], 
	solutions = [
	u'''
	stem
	stem + a
	[-sonorant] -> [-voice] / _ #
	''']
	))

Odden_Problems.append(Problem(
	u'''
Finnish Odden 73-74	
	''',
	[ 
	# a.
	Nominative sg		Partitive sg  		Gloss
	(u"aamu",			u"aamua"),			# morning
	(u"hopea",			u"hopeaa"),			# silver
	(u"katto",			u"kattoa"),			# roof
	(u"kello",			u"kelloa"),			# clock
	(u"kirya",			u"kiryaa"),			# book
	(u"külmæ",			u"külmææ"),			# cold
	(u"koulu",			u"koulua"),			# school
	(u"lintu",			u"lintua"),			# bird
	(u"hüllü",			u"hüllüæ"),			# shelf
	(u"kömpelö",		u"kömpelöæ"),		# clumsy
	(u"nækö",			u"næköæ"),			# appearance

	# b.
	Nominative sg		Partitive sg  		Gloss
	(u"yoki",			u"yokea"),			# river
	(u"kivi",			u"kiveæ"),			# stone
	(u"muuri",			u"muuria"),			# wall
	(u"naapuri",		u"naapuria"),		# neighbor
	(u"nimi",			u"nimeæ"),			# name
	(u"kaappi",			u"kaappia"),		# chest of drawers
	(u"kaikki",			u"kaikkea"),		# all
	(u"kiirehti",		u"kiirehtiæ"),		# hurry
	(u"lehti",			u"lehteæ"),			# leaf
	(u"mæki",			u"mækeæ"),			# hill
	(u"ovi",			u"ovea"),			# door
	(u"posti",			u"postia"),			# mail
	(u"tukki",			u"tukkia"),			# log
	(u"æiti",			u"æitiæ"),			# mother
	(u"englanti",		u"englantia"),		# England
	(u"yærvi",			u"yærveæ"),			# lake
	(u"koski",			u"koskea"),			# waterfall
	(u"reki",			u"rekeæ"),			# sledge
	(u"væki",			u"vækeæ"),			# people
	], 
	solutions = []
	)

Odden_Problems.append(Problem(
	u'''
Kerewe Odden 76-77	
	''',
	[ 
	# Infinitive		1sg habitual		3sg habitual		Imperative		Gloss
	(u"kupaamba",		u"mpaamba",			u"apaamba",			u"paamba"),		# adorn
	(u"kupaaŋga",		u"mpaaŋga",			u"apaaŋga",			u"paaŋga"),		# line up
	(u"kupima",			u"mpima",			u"apima",			u"pima"),		# measure
	(u"kupuupa",		u"mpuupa",			u"apuupa",			u"puupa"),		# be light
	(u"kupekeča",		u"mpekeča".			u"apekeča",			u"pekeča"),		# make fire with stick
	(u"kupiinda",		u"mpiinda",			u"apiinda",			u"piinda"),		# be bent
	(u"kuhiiga",		u"mpiiga",			u"ahiiga",			u"hiiga"),		# hunt
	(u"kuheeka",		u"mpeeka",			u"aheeka",			u"heeka"),		# carry
	(u"kuhaaŋga",		u"mpaaŋga",			u"ahaaŋga",			u"haaŋga"),		# create
	(u"kuheeba",		u"mpeeba",			u"aheeba",			u"heeba"),		# guide
	(u"kuhiima",		u"mpiima",			u"ahiima",			u"hiima"),		# gasp
	(u"kuhuuha",		u"mpuuha",			u"ahuuha",			u"huuha"),		# breath into
	], 
	solutions = []
	))

