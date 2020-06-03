# -*- coding: utf-8 -*-
import sys
from morph import *


class GoldSolution():
    solutions = {}
    def __init__(self, name, prefixes=None, suffixes=None, underlyingForms=None, substitution=None):
        self.name = name
        self.prefixes = prefixes
        self.suffixes = suffixes
        self.underlyingForms = underlyingForms
        self.substitution = substitution
        GoldSolution.solutions[name] = self

GoldSolution(name="Odden_1.1_Axininca_Campa",
             prefixes=[u'',u'no'],
             suffixes=[u'',u'ti'],
             underlyingForms={
             (u'toniro', u'notoniroti') : u'toniro' ,
             (u'yaarato', u'noyaaratoti') : u'yaarato' ,
             (u'kanari', u'noyanariti') : u'kanari' ,
             (u'kosiri', u'noyosiriti') : u'kosiri' ,
             (u'pisiro', u'nowisiroti') : u'pisiro' ,
             (u'porita', u'noworitati') : u'porita' ,
})

GoldSolution(name="Odden_1.2_Kikuyu",
             prefixes=[u'ko'],
             suffixes=[u'a'],
             underlyingForms={
            ( u'ɣotɛŋɛra', ): u'tɛŋɛr' ,
            ( u'ɣokuua', ): u'kuu' ,
            ( u'ɣokoora', ): u'koor' ,
            ( u'koruɣa', ): u'ruɣ' ,
            ( u'kooria', ): u'ori' ,
            ( u'komɛɲa', ): u'mɛɲ' ,
            ( u'kohɔta', ): u'hɔt' ,
            ( u'ɣočina', ): u'čin' ,
            ( u'koɣeera', ): u'ɣeer' ,
            ( u'koina', ): u'in' ,
            ( u'ɣočuuka', ): u'čuuk' ,
            ( u'ɣokaya', ): u'kay' ,
            ( u'koɣaya', ): u'ɣay' ,
})

GoldSolution(name="Odden_1.3_Korean",
             prefixes=[u'',u''],
             suffixes=[u'ə',u'ko'],
             underlyingForms={
            ( u'ipə', u'ipko', ): u'ip' ,
            ( u'kupə', u'kupko', ): u'kup' ,
            ( u'kap^ha', u'kapko', ): u'kap^h' ,
            ( u'cip^hə', u'cipko', ): u'cip^h' ,
            ( u'tata', u'tatko', ): u'tat' ,
            ( u'put^hə', u'putko', ): u'put^h' ,
            ( u'məkə', u'məkko', ): u'mək' ,
            ( u'čukə', u'čukko', ): u'čuk' ,
            ( u'ikə', u'ikko', ): u'ik' ,
            ( u'taka', u'takko', ): u'tak' ,
            ( u'kaka', u'kakko', ): u'kak' ,
            ( u'səkə', u'səkko', ): u'sək' ,
})

GoldSolution(name="Odden_1.12_English",
             prefixes=[u'',u'',u'',u''],
             suffixes=[u'',u'd',u'z',u'ɩŋ'],
             underlyingForms={
            ( u'ro', u'rod', u'roz', u'roɩŋ', ): u'ro' ,
            ( u'šo', u'šod', u'šoz', u'šoɩŋ', ): u'šo' ,
            ( u'cal', u'cald', u'calz', u'calɩŋ', ): u'cal' ,
            ( u'trn', u'trnd', u'trnz', u'trnɩŋ', ): u'trn' ,
            ( u'græb', u'græbd', u'græbz', u'græbɩŋ', ): u'græb' ,
            ( u'sim', u'simd', u'simz', u'simɩŋ', ): u'sim' ,
            ( u'liv', u'livd', u'livz', u'livɩŋ', ): u'liv' ,
            ( u'mʊv', u'mʊvd', u'mʊvz', u'mʊvɩŋ', ): u'mʊv' ,
            ( u'həg', u'həgd', u'həgz', u'həgɩŋ', ): u'həg' ,
            ( u'lʊk', u'lʊkt', u'lʊks', u'lʊkɩŋ', ): u'lʊk' ,
            ( u'æsk', u'æskt', u'æsks', u'æskɩŋ', ): u'æsk' ,
            ( u'wɛrk', u'wɛrkt', u'wɛrks', u'wɛrkɩŋ', ): u'wɛrk' ,
            ( u'kɩs', u'kɩst', u'kɩsəz', u'kɩsɩŋ', ): u'kɩs' ,
            ( u'fɩš', u'fɩšt', u'fɩšəz', u'fɩšɩŋ', ): u'fɩš' ,
            ( u'kwɩz', u'kwɩzd', u'kwɩzəz', u'kwɩzɩŋ', ): u'kwɩz' ,
            ( u'bʌz', u'bʌzd', u'bʌzəz', u'bʌzɩŋ', ): u'bʌz' ,
            ( u'wet', u'wetəd', u'wets', u'wetɩŋ', ): u'wet' ,
            ( u'wed', u'wedəd', u'wedz', u'wedɩŋ', ): u'wed' ,
            ( u'nid', u'nidəd', u'nidz', u'nidɩŋ', ): u'nid' ,
            ( u'lɩft', u'lɩftəd', u'lɩfts', u'lɩftɩŋ', ): u'lɩft' ,
})

GoldSolution(name="Odden_2.1_Hungarian",
             prefixes=[u'',u'',u'',u''],
             suffixes=[u'',u'ban',u'to:l',u'nak'],
             underlyingForms={
            ( u'kalap', u'kalabban', u'kalapto:l', u'kalapnak', ): u'kalap' ,
            ( u'ku:t', u'ku:dban', u'ku:tto:l', u'ku:tnak', ): u'ku:t' ,
            ( u'ža:k', u'ža:gban', u'ža:kto:l', u'ža:knak', ): u'ža:k' ,
            ( u're:s', u're:zben', u're:stö:l', u're:snek', ): u're:s' ,
            ( u'šro:f ', u'šro:vban ', u'šro:fto:l ', u'šro:fnak', ): u'šro:f' ,
            ( u'laka:š', u'laka:žban', u'laka:što:l', u'laka:šnak', ): u'laka:š' ,
            ( u'ketret^s', u'ketred^zben', u'ketret^stö:l', u'ketret^snek', ): u'ketrat^s' ,
            ( u'test', u'tezdben', u'testtö:l', u'testnek', ): u'test' ,
            ( u'rab', u'rabban', u'rapto:l', u'rabnak', ): u'rab' ,
            ( u'ka:d', u'ka:dban', u'ka:tto:l', u'ka:dnak', ): u'ka:d' ,
            ( u'meleg', u'melegben', u'melektö:l', u'melegnek', ): u'melag' ,
            ( u'vi:z', u'vi:zben', u'vi:stö:l', u'vi:znek', ): u'vi:z' ,
            ( u'vara:ž', u'vara:žban', u'vara:što:l', u'vara:žnak', ): u'vara:ž' ,
            ( u'a:g^y', u'a:g^yban', u'a:k^yto:l', u'a:g^ynak', ): u'a:g^y' ,
            ( u'sem', u'semben', u'semtö:l', u'semnek', ): u'sem' ,
            ( u'bün', u'bünben', u'büntö:l', u'bünnek', ): u'bün' ,
            ( u'toroñ', u'toroñban', u'toroñto:l', u'toroñnak', ): u'toroñ' ,
            ( u'fal', u'falban', u'falto:l', u'falnak', ): u'fal' ,
            ( u'ö:r', u'ö:rben', u'ö:rtö:l', u'ö:rnek', ): u'ö:r' ,
            ( u'sa:y', u'sa:yban', u'sa:yto:l', u'sa:ynak', ): u'sa:y' ,
})

GoldSolution(name="Odden_2.2_Kikuria",
             prefixes=[u'',u''],
             suffixes=[u'a',u'era'],
             underlyingForms={
            ( u'suraaŋga', u'suraaŋgera', ): u'suraaŋg' ,
            ( u'taaŋgata', u'taaŋgatera', ): u'taaŋgat' ,
            ( u'baamba', u'baambera', ): u'baamb' ,
            ( u'reenda', u'reendera', ): u'reend' ,
            ( u'rema', u'remera', ): u'rem' ,
            ( u'hoora', u'hoorera', ): u'hoor' ,
            ( u'roma', u'romera', ): u'rom' ,
            ( u'sooka', u'sookera', ): u'sook' ,
            ( u'tačora', u'tačorera', ): u'tačor' ,
            ( u'siika', u'seekera', ): u'siik' ,
            ( u'tiga', u'tegera', ): u'tig' ,
            ( u'ruga', u'rogera', ): u'rug' ,
            ( u'suka', u'sokera', ): u'suk' ,
            ( u'huuta', u'hootera', ): u'huut' ,
            ( u'riiŋga', u'reeŋgera', ): u'riiŋg' ,
            ( u'siinda', u'seendera', ): u'siind' ,
})

GoldSolution(name="Odden_2.3_Farsi", # unsure
             prefixes=[u'',u''],
             suffixes=[u'',u'an'],
             underlyingForms={
            ( u'zæn', u'zænan', ): u'zæn' ,
            ( u'læb', u'læban', ): u'læb' ,
            ( u'hæsud', u'hæsudan', ): u'hæsud' ,
            ( u'bæradær', u'bæradæran', ): u'bæradær' ,
            ( u'bozorg', u'bozorgan', ): u'bozorg' ,
            ( u'mæleke', u'mælekean', ): u'mæleke' ,
            ( u'valede', u'valedean', ): u'valede' ,
            ( u'kæbire', u'kæbirean', ): u'kæbire' ,
            ( u'ahu', u'ahuan', ): u'ahu' ,
            ( u'hamele', u'hamelean', ): u'hamele' ,
            ( u'bačče', u'baččegan', ): u'baččeg' ,
            ( u'setare', u'setaregan', ): u'setareg' ,
            ( u'bænde', u'bændegan', ): u'bændeg' ,
            ( u'azade', u'azadegan', ): u'azadeg' ,
            ( u'divane', u'divanegan', ): u'divaneg' ,
})

GoldSolution(name="Odden_2.4_Tibetan",
             prefixes=[u'',u'bǰu',u''],
             suffixes=[u'',u'',u'bǰu'],
             underlyingForms={
            ( u'ǰu', None, None, ): u'bǰu' ,
            ( u'ǰig', u'ǰugǰig', None, ): u'gǰig' ,
            ( u'ši', u'ǰubši', u'šibǰu', ): u'bši' ,
            ( u'gu', u'ǰurgu', u'gubǰu', ): u'rgu' ,
            ( u'ŋa', u'ǰuŋa', u'ŋabǰu', ): u'ŋa' ,
})

GoldSolution(name="Odden_2.5_Makonde",
             prefixes=[u'',u'',u''],
             suffixes=[u'áŋga',u'íle',u'a'],
             underlyingForms={
            ( u'amáŋga', u'amíle', u'áma', ): u'ám' ,
            ( u'taváŋga', u'tavíle', u'táva', ): u'táv' ,
            ( u'akáŋga', u'akíle', u'áka', ): u'ák' ,
            ( u'patáŋga', u'patíle', u'póta', ): u'pót' ,
            ( u'tatáŋga', u'tatíle', u'tóta', ): u'tót' ,
            ( u'dabáŋga', u'dabíle', u'dóba', ): u'dób' ,
            ( u'aváŋga', u'avíle', u'óva', ): u'óv' ,
            ( u'amáŋga', u'amíle', u'óma', ): u'óm' ,
            ( u'tapáŋga', u'tapíle', u'tépa', ): u'tép' ,
            ( u'patáŋga', u'patíle', u'péta', ): u'pét' ,
            ( u'aváŋga', u'avíle', u'éva', ): u'év' ,
            ( u'babáŋga', u'babíle', u'béba', ): u'béb' ,
            ( u'utáŋga', u'utíle', u'úta', ): u'út' ,
            ( u'lukáŋga', u'lukíle', u'lúka', ): u'lúk' ,
            ( u'lumáŋga', u'lumíle', u'lúma', ): u'lúm' ,
            ( u'uŋgáŋga', u'uŋgíle', u'úŋga', ): u'úŋg' ,
            ( u'iváŋga', u'ivíle', u'íva', ): u'ív' ,
            ( u'pitáŋga', u'pitíle', u'píta', ): u'pít' ,
            ( u'imbáŋga', u'imbíle', u'ímba', ): u'ímb' ,
            ( u'limáŋga', u'limíle', u'líma', ): u'lím' ,
})

GoldSolution(name="Odden_3.1_Kerewe",
             prefixes=[u'ku',u'ku',u'ku',u'ku',u'kutú',u'kukí',u'kutú',u'kukítú'],
             suffixes=[u'a',u'ana',u'ila',u'ilana',u'a',u'a',u'ila',u'ila'],
             underlyingForms={
            ( u'kubala', u'kubalana', u'kubalila', u'kubalilana', u'kutúbála', u'kukíbála', u'kutúbálila', u'kukítúbalila', ): u'bal' ,
            ( u'kugaya', u'kugayana', u'kugayila', u'kugayilana', u'kutúgáya', u'kukígáya', u'kutúgáyila', u'kukítúgayila', ): u'gay' ,
            ( u'kugula', u'kugulana', u'kugulila', u'kugulilana', u'kutúgúla', u'kukígúla', u'kutúgúlila', u'kukítúgulila', ): u'gul' ,
            ( u'kubála', u'kubálána', u'kubálíla', u'kubálílana', u'kutúbála', u'kukíbála', u'kutúbálila', u'kukítúbalila', ): u'bál' ,
            ( u'kulúma', u'kulúmána', u'kulúmíla', u'kulúmílana', u'kutúlúma', u'kukílúma', u'kutúlúmila', u'kukítúlumila', ): u'lúm' ,
            ( u'kusúna', u'kusúnána', u'kusúníla', u'kusúnílana', u'kutúsúna', u'kukísúna', u'kutúsúnila', u'kukítúsunila', ): u'sún' ,
            ( u'kulába', u'kulábána', u'kulábíla', u'kulábílana', u'kutúlába', u'kukílába', u'kutúlábila', u'kukítúlabila', ): u'láb' ,
})

GoldSolution(name="Odden_76_77_Kerewe",
             prefixes=[u'ku',u'm',u'a',u''],
             suffixes=[u'a',u'a',u'a',u'a'],
             underlyingForms={
            ( u'kupaamba' , u'mpaamba' , u'apaamba' , u'paamba' , ): u'paamb' ,
            ( u'kupaaŋga' , u'mpaaŋga' , u'apaaŋga' , u'paaŋga' , ): u'paaŋg' ,
            ( u'kupima' , u'mpima' , u'apima' , u'pima' , ): u'pim' ,
            ( u'kupuupa' , u'mpuupa' , u'apuupa' , u'puupa' , ): u'puup' ,
            ( u'kupekeča' , u'mpekeča' , u'apekeča' , u'pekeča' , ): u'pekeč' ,
            ( u'kupiinda' , u'mpiinda' , u'apiinda' , u'piinda' , ): u'piind' ,
            ( u'kuhiiga' , u'mpiiga' , u'ahiiga' , u'hiiga' , ): u'hiig' ,
            ( u'kuheeka' , u'mpeeka' , u'aheeka' , u'heeka' , ): u'heek' ,
            ( u'kuhaaŋga' , u'mpaaŋga' , u'ahaaŋga' , u'haaŋga' , ): u'haaŋg' ,
            ( u'kuheeba' , u'mpeeba' , u'aheeba' , u'heeba' , ): u'heeb' ,
            ( u'kuhiima' , u'mpiima' , u'ahiima' , u'hiima' , ): u'hiim' ,
            ( u'kuhuuha' , u'mpuuha' , u'ahuuha' , u'huuha' , ): u'huuh' ,
})

GoldSolution(name="Odden_79_Jita",
             prefixes=[u'oku',u'oku',u'oku',u'oku',u'okúmú',u'okúmú',u'okučí',u'okúčí'],
             suffixes=[u'a',u'ira',u'ana',u'irana',u'a',u'ira',u'a',u'ira'],
             underlyingForms={
            ( u'okuβuma' , u'okuβumira' , u'okuβumana' , u'okuβumirana' , u'okumuβúma' , u'okumuβúmira' , u'okučiβúma' , u'okučiβúmira' , ): u'βum' ,
            ( u'okusiβa' , u'okusiβira' , u'okusiβana' , u'okusiβirana' , u'okumusíβa' , u'okumusíβira' , u'okučisíβa' , u'okučisíβira' , ): u'siβ' ,
            ( u'okulúma' , u'okulumíra' , u'okulumána' , u'okulumírana' , None,  None,  None,  None,  ): u'lúm' ,
            ( u'okukúβa' , u'okukuβíra' , u'okukuβána' , u'okukuβírana' , None,  None,  None,  None,  ): u'kúβ' ,
})

GoldSolution(name="Odden_4.10_Sakha_Yakut",
             prefixes=[u'',u'',u''],
             suffixes=[u'',u'lar',u'lɨɨn'],
             underlyingForms={
            ( u'aɣa' , u'aɣalar' , u'aɣalɨɨn' , ): u'aɣa' ,
            ( u'paarta' , u'paartalar' , u'paartalɨɨn' , ): u'paarta' ,
            ( u'tɨa' , u'tɨalar' , u'tɨalɨɨn' , ): u'tɨa' ,
            ( u'kinige' , u'kinigeler' , u'kinigeliin' , ): u'kinige' ,
            ( u'šie' , u'šieler' , u'šieliin' , ): u'šie' ,
            ( u'iye' , u'iyeler' , u'iyeliin' , ): u'iye' ,
            ( u'kini' , u'kiniler' , u'kiniliin' , ): u'kini' ,
            ( u'bie' , u'bieler' , u'bieliin' , ): u'bie' ,
            ( u'oɣo' , u'oɣolor' , u'oɣoluun' , ): u'oɣo' ,
            ( u'Xopto' , u'Xoptolor' , u'Xoptoluun' , ): u'Xopto' ,
            ( u'börö' , u'börölör' , u'börölüün' , ): u'börö' ,
            ( u'tɨal' , u'tɨallar' , u'tɨallɨɨn' , ): u'tɨal' ,
            ( u'ɨal' , u'ɨallar' , u'ɨallɨɨn' , ): u'ɨal' ,
            ( u'kuul' , u'kuullar' , u'kuulluun' , ): u'kuul' ,
            ( u'at' , u'attar' , u'attɨɨn' , ): u'at' ,
            ( u'balɨk' , u'balɨktar' , u'balɨktɨɨn' , ): u'balɨk' ,
            ( u'ɨskaap' , u'ɨskaaptar' , u'ɨskaaptɨɨn' , ): u'ɨskaap' ,
            ( u'oɣus' , u'oɣustar' , u'oɣustuun' , ): u'oɣɨs' ,
            ( u'kus' , u'kustar' , u'kustuun' , ): u'kus' ,
            ( u'tünnük' , u'tünnükter' , u'tünnüktüün' , ): u'tünnɨk' ,
            ( u'sep' , u'septer' , u'septiin' , ): u'sep' ,
            ( u'et' , u'etter' , u'ettiin' , ): u'et' ,
            ( u'örüs' , u'örüster' , u'örüstüün' , ): u'örus' ,
            ( u'tiis' , u'tiister' , u'tiistiin' , ): u'tiis' ,
            ( u'soroX' , u'soroXtor' , u'soroXtuun' , ): u'soroX' ,
            ( u'oX' , u'oXtor' , u'oXtuun' , ): u'oX' ,
            ( u'oloppos' , u'oloppostor' , u'oloppostuun' , ): u'olappos' ,
            ( u'ötöX' , u'ötöXtör' , u'ötöXtüün' , ): u'ötöX' ,
            ( u'ubay' , u'ubaydar' , u'ubaydɨɨn' , ): u'ubay' ,
            ( u'saray' , u'saraydar' , u'saraydɨɨn' , ): u'saray' ,
            ( u'tɨy' , u'tɨydar' , u'tɨydɨɨn' , ): u'tɨy' ,
            ( u'atɨɨr' , u'atɨɨrdar' , u'atɨɨrdɨɨn' , ): u'atɨɨr' ,
            ( u'oyuur' , u'oyuurdar' , u'oyuurduun' , ): u'oyɨur' ,
            ( u'üčügey' , u'üčügeyder' , u'üčügeydiin' , ): u'üčugay' ,
            ( u'ešiiy' , u'ešiiyder' , u'ešiiydiin' , ): u'ešiiy' ,
            ( u'tomtor' , u'tomtordor' , u'tomtorduun' , ): u'tomtor' ,
            ( u'moɣotoy' , u'moɣotoydor' , u'moɣotoyduun' , ): u'moɣotoy' ,
            ( u'kötör' , u'kötördör' , u'kötördüün' , ): u'köter' ,
            ( u'bölköy' , u'bölköydör' , u'bölköydüün' , ): u'bölköy' ,
            ( u'Xatɨŋ' , u'Xatɨŋnar' , u'Xatɨŋnɨɨn' , ): u'Xatɨŋ' ,
            ( u'aan' , u'aannar' , u'aannɨɨn' , ): u'aan' ,
            ( u'tiiŋ' , u'tiiŋner' , u'tiiŋniin' , ): u'tiiŋ' ,
            ( u'sordoŋ' , u'sordoŋnor' , u'sordoŋnuun' , ): u'sordoŋ' ,
            ( u'olom' , u'olomnor' , u'olomnuun' , ): u'olom' ,
            ( u'oron' , u'oronnor' , u'oronnuun' , ): u'oron' ,
            ( u'bödöŋ' , u'bödöŋnör' , u'bödöŋnüün' , ): u'bödeŋ' ,
})

GoldSolution(name="Odden_77_78_English",
             prefixes=[u''],
             suffixes=[u'z'],
             underlyingForms={
            ( u'kæps' , ): u'kæp' ,
            ( u'kæts' , ): u'kæt' ,
            ( u'kaks' , ): u'kak' ,
            ( u'pruwfs' , ): u'pruwf' ,
            ( u'kæbz' , ): u'kæb' ,
            ( u'kædz' , ): u'kæd' ,
            ( u'kagz' , ): u'kag' ,
            ( u'hʊvz' , ): u'hʊv' ,
            ( u'fliyz' , ): u'fliy' ,
            ( u'plæwz' , ): u'plæw' ,
            ( u'pyṛez' , ): u'pyṛe' ,
            ( u'klæmz' , ): u'klæm' ,
            ( u'kænz' , ): u'kæn' ,
            ( u'karz' , ): u'kar' ,
            ( u'gəlz' , ): u'gəl' ,
            ( u'slæps' , ): u'slæp' ,
            ( u'hɩts' , ): u'hɩt' ,
            ( u'powks' , ): u'powk' ,
            ( u'stæbz' , ): u'stæb' ,
            ( u'haydz' , ): u'hayd' ,
            ( u'dɩgz' , ): u'dɩg' ,
            ( u'læfs' , ): u'læf' ,
            ( u'pɩθs' , ): u'pɩθ' ,
            ( u'slæmz' , ): u'slæm' ,
            ( u'kænz' , ): u'kæn' ,
            ( u'hæŋz' , ): u'hæŋ' ,
            ( u'θrayvz' , ): u'θrayv' ,
            ( u'beyðz' , ): u'beyð' ,
            ( u'flayz' , ): u'flay' ,
})

GoldSolution(name="Odden_73_74_Finnish",
             prefixes=[u'',u''],
             suffixes=[u'',u'a'],
             underlyingForms={
            ( u'aamu' , u'aamua' , ): u'aamu' ,
            ( u'hopea' , u'hopeaa' , ): u'hopea' ,
            ( u'katto' , u'kattoa' , ): u'katto' ,
            ( u'kello' , u'kelloa' , ): u'kello' ,
            ( u'kirya' , u'kiryaa' , ): u'kirya' ,
            ( u'külmæ' , u'külmææ' , ): u'külmæ' ,
            ( u'koulu' , u'koulua' , ): u'koulu' ,
            ( u'lintu' , u'lintua' , ): u'lintu' ,
            ( u'hüllü' , u'hüllüæ' , ): u'hüllü' ,
            ( u'kömpelö' , u'kömpelöæ' , ): u'kömpelö' ,
            ( u'nækö' , u'næköæ' , ): u'nækö' ,
            ( u'yoki' , u'yokea' , ): u'yoke' ,
            ( u'kivi' , u'kiveæ' , ): u'kive' ,
            ( u'muuri' , u'muuria' , ): u'muuri' ,
            ( u'naapuri' , u'naapuria' , ): u'naæpuri' ,
            ( u'nimi' , u'nimeæ' , ): u'nime' ,
            ( u'kaappi' , u'kaappia' , ): u'kaappi' ,
            ( u'kaikki' , u'kaikkea' , ): u'kaikke' ,
            ( u'kiirehti' , u'kiirehtiæ' , ): u'kiirehti' ,
            ( u'lehti' , u'lehteæ' , ): u'lehte' ,
            ( u'mæki' , u'mækeæ' , ): u'mæke' ,
            ( u'ovi' , u'ovea' , ): u'ove' ,
            ( u'posti' , u'postia' , ): u'posti' ,
            ( u'tukki' , u'tukkia' , ): u'tukki' ,
            ( u'æiti' , u'æitiæ' , ): u'æiti' ,
            ( u'englanti' , u'englantia' , ): u'englanti' ,
            ( u'yærvi' , u'yærveæ' , ): u'yærve' ,
            ( u'koski' , u'koskea' , ): u'koske' ,
            ( u'reki' , u'rekeæ' , ): u'reke' ,
            ( u'væki' , u'vækeæ' , ): u'væke' ,
})

GoldSolution(name="Odden_81_Korean", 
             prefixes=[u'',u''],
             suffixes=[u'ə',u'nɨnta'],
             underlyingForms={
            ( u'ana' , u'annɨnta' , ): u'an' ,
            ( u'kama' , u'kamnɨnta' , ): u'kam' ,
            ( u'sinə' , u'sinnɨnta' , ): u'sin' ,
            ( u't̚atɨmə' , u't̚atɨmnɨnta' , ): u't̚atɨm' ,
            ( u'nəmə' , u'nəmnɨnta' , ): u'nəm' ,
            ( u'nama' , u'namnɨnta' , ): u'nam' ,
            ( u'č^hama' , u'č^hamnɨnta' , ): u'č^ham' ,
            ( u'ipə' , u'imnɨnta' , ): u'ip' ,
            ( u'kupə' , u'kumnɨnta' , ): u'kup' ,
            ( u'čəpə' , u'čəmnɨnta' , ): u'čəp' ,
            ( u'tata' , u'tannɨnta' , ): u'tat' ,
            ( u'put^hə' , u'punnɨnta' , ): u'put^h' ,
            ( u'čoč^ha' , u'čonnɨnta' , ): u'čoč^h' ,
            ( u'məkə' , u'məŋnɨnta' , ): u'mək' ,
            ( u'sək̚ə' , u'səŋnɨnta' , ): u'sək̚' ,
            ( u'tak̚a' , u'taŋnɨnta' , ): u'tak̚' ,
            ( u'čukə' , u'čuŋnɨnta' , ): u'čuk' ,
            ( u'ikə' , u'iŋnɨnta' , ): u'ik' ,
})

GoldSolution(name="Odden_81_Koasati",
             prefixes=[u'',u'am'],
             suffixes=[u'',u''],
             underlyingForms={
            ( u'apahčá' , u'amapahčá' , ): u'apahčá' ,
            ( u'asikčí' , u'amasikčí' , ): u'asikčí' ,
            ( u'ilkanó' , u'amilkanó' , ): u'ilkanó' ,
            ( u'ifá' , u'amifá' , ): u'ifá' ,
            ( u'a:pó' , u'ama:pó' , ): u'a:pó' ,
            ( u'iskí' , u'amiskí' , ): u'iskí' ,
            ( u'pačokkö́ka' , u'ampačokkö́ka' , ): u'pačokkö́ka' ,
            ( u'towá' , u'antowá' , ): u'towá' ,
            ( u'kastó' , u'aŋkastó' , ): u'kastó' ,
            ( u'bayá:na' , u'ambayá:na' , ): u'bayá:na' ,
            ( u'tá:ta' , u'antá:ta' , ): u'tá:ta' ,
            ( u'čofkoní' , u'añčofkoní' , ): u'čofkoní' ,
            ( u'kitiłká' , u'aŋkitiłká' , ): u'kitiłká' ,
            ( u'toní' , u'antoní' , ): u'toní' ,
})


GoldSolution(name="Odden_85_Samoan",
             prefixes=[u'',u''],
             suffixes=[u'',u'ia'],
             underlyingForms={
            ( u'olo' , u'oloia' , ): u'olo' ,
            ( u'lafo' , u'lafoia' , ): u'lafo' ,
            ( u'aŋa' , u'aŋaia' , ): u'aŋa' ,
            ( u'usu' , u'usuia' , ): u'usu' ,
            ( u'tau' , u'tauia' , ): u'tau' ,
            ( u'taui' , u'tauia' , ): u'taui' ,
            ( u'sa:ʔili' , u'sa:ʔilia' , ): u'sa:ʔili' ,
            ( u'vaŋai' , u'vaŋaia' , ): u'vaŋai' ,
            ( u'paʔi' , u'paʔia' , ): u'paʔi' ,
            ( u'naumati' , u'naumatia' , ): u'naumati' ,
            ( u'sa:uni' , u'sa:unia' , ): u'sa:uni' ,
            ( u'seŋi' , u'seŋia' , ): u'seŋi' ,
            ( u'lele' , u'lelea' , ): u'lele' ,
            ( u'suʔe' , u'suʔea' , ): u'suʔe' ,
            ( u'taʔe' , u'taʔea' , ): u'taʔe' ,
            ( u'tafe' , u'tafea' , ): u'tafe' ,
            ( u'ta:upule' , u'ta:upulea' , ): u'ta:upule' ,
            ( u'palepale' , u'palepalea' , ): u'palepale' ,
            ( u'tu:' , u'tu:lia' , ): u'tu:l' ,
            ( u'tau' , u'taulia' , ): u'taul' ,
            ( u'ʔalo' , u'ʔalofia' , ): u'ʔalof' ,
            ( u'oso' , u'osofia' , ): u'osof' ,
            ( u'sao' , u'saofia' , ): u'saof' ,
            ( u'asu' , u'asuŋia' , ): u'asuŋ' ,
            ( u'pole' , u'poleŋia' , ): u'poleŋ' ,
            ( u'ifo' , u'ifoŋia' , ): u'ifoŋ' ,
            ( u'ula' , u'ulaŋia' , ): u'ulaŋ' ,
            ( u'milo' , u'milosia' , ): u'milos' ,
            ( u'valu' , u'valusia' , ): u'valus' ,
            ( u'vela' , u'velasia' , ): u'velas' ,
            ( u'api' , u'apitia' , ): u'apit' ,
            ( u'eʔe' , u'eʔetia' , ): u'eʔet' ,
            ( u'lava:' , u'lava:tia' , ): u'lava:t' ,
            ( u'u:' , u'u:tia' , ): u'u:t' ,
            ( u'puni' , u'punitia' , ): u'punit' ,
            ( u'siʔo' , u'siʔomia' , ): u'siʔom' ,
            ( u'ŋalo' , u'ŋalomia' , ): u'ŋalom' ,
            ( u'sopo' , u'sopoʔia' , ): u'sopoʔ' ,
            ( u'au' , u'aulia' , ): u'aul' ,
            ( u'ma:tau' , u'ma:taulia' , ): u'ma:taul' ,
            ( u'ili' , u'ilifia' , ): u'ilif' ,
            ( u'ulu' , u'ulufia' , ): u'uluf' ,
            ( u'taŋo' , u'taŋofia' , ): u'taŋof' ,
            ( u'soa' , u'soaŋia' , ): u'soaŋ' ,
            ( u'fesili' , u'fesiliŋia' , ): u'fesiliŋ' ,
            ( u'ʔote' , u'ʔoteŋia' , ): u'ʔoteŋ' ,
            ( u'tofu' , u'tofuŋia' , ): u'tofuŋ' ,
            ( u'laʔa' , u'laʔasia' , ): u'laʔas' ,
            ( u'taŋi' , u'taŋisia' , ): u'taŋis' ,
            ( u'motu' , u'motusia' , ): u'motus' ,
            ( u'mataʔu' , u'mataʔutia' , ): u'mataʔut' ,
            ( u'sau' , u'sautia' , ): u'saut' ,
            ( u'oʔo' , u'oʔotia' , ): u'oʔot' ,
            ( u'ufi' , u'ufitia' , ): u'ufit' ,
            ( u'tanu' , u'tanumia' , ): u'tanum' ,
            ( u'moʔo' , u'moʔomia' , ): u'moʔom' ,
            ( u'tao' , u'taomia' , ): u'taom' ,
            ( u'fana' , u'fanaʔia' , ): u'fanaʔ' ,
})

GoldSolution(name="Odden_88_Palauan", # actually the solution it finds I think is fine
             prefixes=[u'mə',u'',u''], # although really this could be any vowel
             suffixes=[u'',u'all',u'l'], # although really this could be stressed
             underlyingForms={
            ( u'mədáŋəb' , u'dəŋəbáll' , u'dəŋóbl' , ): u'daŋob' ,
            ( u'mətéʔəb' , u'təʔəbáll' , u'təʔíbl' , ): u'teʔib' ,
            ( u'məŋétəm' , u'ŋətəmáll' , u'ŋətóml' , ): u'ŋetom' ,
            ( u'mətábək' , u'təbəkáll' , u'təbákl' , ): u'tabak' ,
            ( u'məʔárəm' , u'ʔərəmáll' , u'ʔəróml' , ): u'ʔarom' ,
            ( u'məsésəb' , u'səsəbáll' , u'səsóbl' , ): u'sesob' ,
})

GoldSolution(name="Odden_2.6_North_Saami",
             prefixes=[u'',u''],
             suffixes=[u'',u'in'],
             underlyingForms={
            ( u'varit', u'varihin', ): u'varih' ,
            ( u'oahpis', u'oahpisin', ): u'oahpis' ,
            ( u'čoarvuš', u'čoarvušin', ): u'čoarvuš' ,
            ( u'lottaaš', u'lottaaǰin', ): u'lottaaǰ' ,
            ( u'čuoivvat', u'čuoivvagin', ): u'čuoivvag' ,
            ( u'ahhkut', u'ahhkubin', ): u'ahhkub' ,
            ( u'suohkat', u'suohkaðin', ): u'suohkað' ,
            ( u'heeǰoš', u'heeǰoǰin', ): u'heeǰoǰ' ,
            ( u'aaǰǰut', u'aaǰǰubin', ): u'aaǰǰub' ,
            ( u'bissobeahtset', u'bissobeahtsehin', ): u'bissobeahtseh' ,
            ( u'čeahtsit', u'čeahtsibin', ): u'čeahtsib' ,
            ( u'yaaʔmin', u'yaaʔmimin', ): u'yaaʔmim' ,
            ( u'čuoivat', u'čuoivagin', ): u'čuoivag' ,
            ( u'laageš', u'laageǰin', ): u'laageǰ' ,
            ( u'gahpir', u'gahpirin', ): u'gahpir' ,
            ( u'gaauhtsis', u'gaauhtsisin', ): u'gaauhtsis' ,
            ( u'aaslat', u'aaslagin', ): u'aaslag' ,
            ( u'baðoošgaattset', u'baðoošgaattsebin', ): u'baðoošgaattseb' ,
            ( u'ahhkit', u'ahhkiðin', ): u'ahhkið' ,
            ( u'bahaanaalat', u'bahaanaalagin', ): u'bahaanaalag' ,
            ( u'beštor', u'beštorin', ): u'beštor' ,
            ( u'heevemeahhtun', u'heevemeahhtunin', ): u'heevemeahhtun' ,
            ( u'beeǰot', u'beeǰohin', ): u'beeǰoh' ,
            ( u'bissomeahtun', u'bissomeahtumin', ): u'bissomeahtum' ,
            ( u'laðas', u'laðasin', ): u'laðas' ,
            ( u'heaiyusmielat', u'heaiyusmielagin', ): u'heaiyusmielag' ,
            ( u'heaŋkkan', u'heaŋkkanin', ): u'heaŋkkan' ,
            ( u'yaman', u'yamanin', ): u'yaman' ,
})


GoldSolution(name="Odden_3.2_Polish",
             prefixes=[u'',u''],
             suffixes=[u'',u'i'],
             underlyingForms={
            ( u'klup', u'klubi', ): u'klub' ,
            ( u'trup', u'trupi', ): u'trup' ,
            ( u'dom', u'domi', ): u'dom' ,
            ( u'snop', u'snopi', ): u'snop' ,
            ( u'žwup', u'žwobi', ): u'žwob' ,
            ( u'trut', u'trudi', ): u'trud' ,
            ( u'dzvon', u'dzvoni', ): u'dzvon' ,
            ( u'kot', u'koti', ): u'kot' ,
            ( u'lut', u'lodi', ): u'lod' ,
            ( u'grus', u'gruzi', ): u'gruz' ,
            ( u'nos', u'nosi', ): u'nos' ,
            ( u'vus', u'vozi', ): u'voz' ,
            ( u'wuk', u'wugi', ): u'wug' ,
            ( u'wuk', u'wuki', ): u'wuk' ,
            ( u'sok', u'soki', ): u'sok' ,
            ( u'ruk', u'rogi', ): u'rog' ,
            ( u'bur', u'bori', ): u'bor' ,
            ( u'vuw', u'vowi', ): u'vow' ,
            ( u'sul', u'soli', ): u'sol' ,
            ( u'buy', u'boyi', ): u'boy' ,
            ( u'šum', u'šumi', ): u'šum' ,
            ( u'žur', u'žuri', ): u'žur' ,
})

GoldSolution(name="Odden_3.3_Ancient_Greek",
             prefixes=[u'',u'',u'',u''],
             suffixes=[u's',u'os',u'i',u'si'],
             underlyingForms={
            ( u'hals', u'halos', u'hali', u'halsi', ): u'hal' ,
            ( u'oys', u'oyos', u'oyi', u'oysi', ): u'oy' ,
            ( u'sus', u'suos', u'sui', u'susi', ): u'su' ,
            ( u'klo:ps', u'klo:pos', u'klo:pi', u'klo:psi', ): u'klo:p' ,
            ( u'p^hle:ps', u'p^hle:bos', u'p^hle:bi', u'p^hle:psi', ): u'p^hle:b' ,
            ( u'kate:lips', u'kate:lip^hos', u'kate:lip^hi', u'kate:lipsi', ): u'kate:lip^h' ,
            ( u'p^hulaks', u'p^hulakos', u'p^hulaki', u'p^hulaksi', ): u'p^hulak' ,
            ( u'ayks', u'aygos', u'aygi', u'ayksi', ): u'ayg' ,
            ( u'salpiŋks', u'salpiŋgos', u'salpiŋgi', u'salpiŋksi', ): u'salpiŋg' ,
            ( u'onuks', u'onuk^hos', u'onuk^hi', u'onuksi', ): u'onuk^h' ,
            ( u't^he:s', u't^he:tos ', u't^he:ti ', u't^he:si', ): u't^he:t' ,
            ( u'k^haris', u'k^haritos', u'k^hariti', u'k^harisi', ): u'k^harit' ,
            ( u'elpis', u'elpidos', u'elpidi', u'elpisi', ): u'elpid' ,
            ( u'korus', u'korut^hos', u'korut^hi', u'korusi', ): u'korut^h' ,
            ( u'ri:s', u'ri:nos', u'ri:ni', u'ri:si', ): u'ri:n' ,
            ( u'delp^hi:s', u'delp^hi:nos', u'delp^hi:ni', u'delp^hi:si', ): u'delp^hi:n' ,
})

GoldSolution(name="Odden_3.5_Catalan",
             prefixes=[u'',u''],
             suffixes=[u'',u'ə'],
             underlyingForms={
            ( u'əkely', u'əkelyə', ): u'əkely' ,
            ( u'mal', u'malə', ): u'mal' ,
            ( u'siβil', u'siβilə', ): u'siβil' ,
            ( u'əskerp', u'əskerpə', ): u'əskerp' ,
            ( u'šop', u'šopə', ): u'šop' ,
            ( u'sɛk', u'sɛkə', ): u'sɛk' ,
            ( u'əspɛs', u'əspɛsə', ): u'əspɛs' ,
            ( u'gros', u'grosə', ): u'gros' ,
            ( u'baš', u'bašə', ): u'baš' ,
            ( u'koš', u'košə', ): u'koš' ,
            ( u'tot', u'totə', ): u'tot' ,
            ( u'brut', u'brutə', ): u'brut' ,
            ( u'pɔk', u'pɔkə', ): u'pɔk' ,
            ( u'prəsis', u'prəsizə', ): u'prəsiz' ,
            ( u'frənses', u'frənsezə', ): u'frənsez' ,
            ( u'gris', u'grizə', ): u'griz' ,
            ( u'kəzat', u'kəzaðə', ): u'kəzad' ,
            ( u'bwit', u'bwiðə', ): u'bwid' ,
            ( u'rɔč', u'rɔžə', ): u'rɔǰ' ,
            ( u'boč', u'božə', ): u'boǰ' ,
            ( u'orp', u'orβə', ): u'orb' ,
            ( u'lyark', u'lyarɣə', ): u'lyarg' ,
            ( u'sek', u'seɣə', ): u'seg' ,
            ( u'fəšuk', u'fəšuɣə', ): u'fəšug' ,
            ( u'grok', u'groɣə', ): u'grog' ,
            ( u'puruk', u'puruɣə', ): u'purug' ,
            ( u'kandit', u'kandiðə', ): u'kandid' ,
            ( u'frɛt', u'frɛðə', ): u'frɛd' ,
            ( u'səɣu', u'səɣurə', ): u'səɣur' ,
            ( u'du', u'durə', ): u'dur' ,
            ( u'səɣəðo', u'səɣəðorə', ): u'səɣəðor' ,
            ( u'kla', u'klarə', ): u'klar' ,
            ( u'nu', u'nuə', ): u'nu' ,
            ( u'kru', u'kruə', ): u'kru' ,
            ( u'flɔñǰu', u'flɔñǰə', ): u'flɔñǰu' ,
            ( u'dropu', u'dropə', ): u'dropu' ,
            ( u'əgzaktə', u'əgzaktə', ): u'əgzaktə' ,
            ( u'əlβi', u'əlβinə', ): u'əlβin' ,
            ( u'sa', u'sanə', ): u'san' ,
            ( u'pla', u'planə', ): u'plan' ,
            ( u'bo', u'bonə', ): u'bon' ,
            ( u'sərɛ', u'sərɛnə', ): u'sərɛn' ,
            ( u'suβlim', u'suβlimə', ): u'suβlim' ,
            ( u'al', u'altə', ): u'alt' ,
            ( u'fɔr', u'fɔrtə', ): u'fɔrt' ,
            ( u'kur', u'kurtə', ): u'kurt' ,
            ( u'sor', u'sorðə', ): u'sord' ,
            ( u'bɛr', u'bɛrðə', ): u'bɛrd' ,
            ( u'san', u'santə', ): u'sant' ,
            ( u'kəlɛn', u'kəlɛntə', ): u'kəlɛnt' ,
            ( u'prufun', u'prufundə', ): u'prufund' ,
            ( u'fəkun', u'fəkundə', ): u'fəkund' ,
            ( u'dəsen', u'dəsentə', ): u'dəsent' ,
            ( u'dulen', u'dulentə', ): u'dulent' ,
            ( u'əstuðian', u'əstuðiantə', ): u'əstuðiant' ,
            ( u'blaŋ', u'blaŋkə', ): u'blaŋk' ,
})

GoldSolution(name="Odden_114_Lithuanian",
             prefixes=[u'at',u'ap'],
             suffixes=[u'ti',u'ti'],
             underlyingForms={
            ( u'ateiti' , None,  ): u'ei' ,
            ( u'atimti' , None,  ): u'im' ,
            ( u'atnešti' , None,  ): u'neš' ,
            ( u'atleisti' , None,  ): u'leis' ,
            ( u'atlikti' , None,  ): u'lik' ,
            ( u'atko:pti' , None,  ): u'ko:p' ,
            ( u'atpraši:ti' , None,  ): u'praši:' ,
            ( u'atkurti' , None,  ): u'kur' ,
            ( None,  u'apeiti' , ): u'ei' ,
            ( None,  u'apieško:ti' , ): u'ieško:' ,
            ( None,  u'apakti' , ): u'ak' ,
            ( None,  u'apmo:ki:ti' , ): u'mo:ki:' ,
            ( None,  u'aptemdi:ti' , ): u'temdi:' ,
            ( None,  u'apšaukti' , ): u'šauk' ,
            ( u'adbekti' , None,  ): u'bek' ,
            ( u'adgauti' , None,  ): u'gau' ,
            ( u'adbukti' , None,  ): u'buk' ,
            ( u'adgimti' , None,  ): u'gim' ,
            ( None,  u'abgauti' , ): u'gau' ,
            ( None,  u'abž^yureti' , ): u'ž^yure' ,
            ( None,  u'abželti' , ): u'žel' ,
            ( None,  u'abdauži:ti' , ): u'dauži:' ,
            ( None,  u'abdraski:ti' , ): u'draski:' ,
})

GoldSolution(name="Odden_116_Armenian",
             prefixes=[u'k'],
             suffixes=[u'am'],
             underlyingForms={
            ( u'kert^ham' , ): u'ert^h' ,
            ( u'kasiem' , ): u'asi' ,
            ( u'kaniem' , ): u'ani' ,
            ( u'kakaniem' , ): u'akani' ,
            ( u'koxniem' , ): u'oxni' ,
            ( u'kurriem' , ): u'urri' ,
            ( u'kətam' , ): u't' ,
            ( u'kəkienam' , ): u'kien' ,
            ( u'gəbəzzam' , ): u'bəzz' ,
            ( u'gəlam' , ): u'l' ,
            ( u'gəzəram' , ): u'zər' ,
            ( u'k^hət^huoyniem' , ): u't^huoyni' ,
            ( u'k^həč^hap^hiem' , ): u'č^hap^hi' ,
            ( u'g^həb^hieřiem' , ): u'b^hiaři' ,
            ( u'g^həg^huom' , ): u'g^hu' ,
            ( u'g^həd^z^hieviem' , ): u'd^z^hiavi' ,
})

GoldSolution(name="Odden_105_Bukusu",
             prefixes=[u'',u'βa',{u'ñ',u'ŋ',u'n',u'm'}],
             suffixes=[u'a',u'a',u'a'],
             underlyingForms={
            ( u'ča' , u'βača' , u'ñǰa' , ): u'č' ,
            ( u'čexa' , u'βačexa' , u'ñǰexa' , ): u'čex' ,
            ( u'čučuuŋga' , u'βačučuuŋga' , u'ñǰučuuŋga' , ): u'čučuuŋg' ,
            ( u'talaanda' , u'βatalaanda' , u'ndalaanda' , ): u'talaand' ,
            ( u'teexa' , u'βateexa' , u'ndeexa' , ): u'teex' ,
            ( u'tiira' , u'βatiira' , u'ndiira' , ): u'tiir' ,
            ( u'piima' , u'βapiima' , u'mbiima' , ): u'piim' ,
            ( u'pakala' , u'βapakala' , u'mbakala' , ): u'pakal' ,
            ( u'ketulula' , u'βaketulula' , u'ŋgetulula' , ): u'ketulul' ,
            ( u'kona' , u'βakona' , u'ŋgona' , ): u'kon' ,
            ( u'kula' , u'βakula' , u'ŋgula' , ): u'kul' ,
            ( u'kwa' , u'βakwa' , u'ŋgwa' , ): u'kw' ,
})

GoldSolution(name="Odden_3.6_Finnish",
             prefixes=[u'',u'',u'',u'',u''],
             suffixes=[u'n',u'',u't',u'lta',u'na'],
             underlyingForms={
            ( u'kanadan', u'kanada', u'kanadat', u'kanadalta', u'kanadana', ): u'kanada' ,
            ( u'kiryan', u'kirya', u'kiryat', u'kiryalta', u'kiryana', ): u'kirya' ,
            ( u'aamun', u'aamu', u'aamut', u'aamulta', u'aamuna', ): u'aamu' ,
            ( u'talon', u'talo', u'talot', u'talolta', u'talona', ): u'talo' ,
            ( u'koiran', u'koira', u'koirat', u'koiralta', u'koirana', ): u'koira' ,
            ( u'hüvæn', u'hüvæ', u'hüvæt', u'hüvæltæ', u'hüvænæ', ): u'hüvæ' ,
            ( u'kuvan', u'kuva', u'kuvat', u'kuvalta', u'kuvana', ): u'kuva' ,
            ( u'lain', u'laki', u'lait', u'lailta', u'lakina', ): u'laki' ,
            ( u'nælæn', u'nælkæ', u'nælæt', u'nælæltæ', u'nælkænæ', ): u'nælkæ' ,
            ( u'yalan', u'yalka', u'yalat', u'yalalta', u'yalkana', ): u'yalka' ,
            ( u'leuan', u'leuka', u'leuat', u'leualta', u'leukana', ): u'leuka' ,
            ( u'paran', u'parka', u'parat', u'paralta', u'parkana', ): u'parka' ,
            ( u'reiæn', u'reikæ', u'reiæt', u'reiæltæ', u'reikænæ', ): u'reikæ' ,
            ( u'nahan', u'nahka', u'nahat', u'nahalta', u'nahkana', ): u'nahka' ,
            ( u'vihon', u'vihko', u'vihot', u'viholta', u'vihkona', ): u'vihko' ,
            ( u'laihan', u'laiha', u'laihat', u'laihalta', u'laihana', ): u'laiha' ,
            ( u'avun', u'apu', u'avut', u'avulta', u'apuna', ): u'apu' ,
            ( u'halvan', u'halpa', u'halvat', u'halvalta', u'halpana', ): u'halpa' ,
            ( u'orvon', u'orpo', u'orvot', u'orvolta', u'orpona', ): u'orpo' ,
            ( u'leivæn', u'leipæ', u'leivæt', u'leivæltæ', u'leipænæ', ): u'leipæ' ,
            ( u'pæivæn', u'pæivæ', u'pæivæt ', u'pæivæltæ ', u'pæivænæ', ): u'pæiva' ,
            ( u'kilvan', u'kilpa', u'kilvat', u'kilvalta', u'kilpana', ): u'kilpa' ,
            ( u'külvün', u'külpü', u'külvüt', u'külvültæ', u'külpünæ', ): u'külpü' ,
            ( u'tavan', u'tapa', u'tavat', u'tavalta', u'tapana', ): u'tapa' ,
            ( u'korvan', u'korva', u'korvat', u'korvalta', u'korvana', ): u'korva' ,
            ( u'æidin', u'æiti', u'æidit', u'æidiltæ', u'æitinæ', ): u'æiti' ,
            ( u'kodin', u'koti', u'kodit', u'kodilta', u'kotina', ): u'koti' ,
            ( u'muodon', u'muoto', u'muodot', u'muodolta', u'muotona', ): u'muoto' ,
            ( u'tædin', u'tæti', u'tædit', u'tædiltæ', u'tætinæ', ): u'tæti' ,
            ( u'kadun', u'katu', u'kadut', u'kadulta', u'katuna', ): u'katu' ,
            ( u'maidon', u'maito', u'maidot', u'maidolta', u'maitona', ): u'maito' ,
            ( u'pöüdæn', u'pöütæ', u'pöüdæt', u'pöüdæltæ', u'pöütænæ', ): u'pöütæ' ,
            ( u'tehdün', u'tehtü', u'tehdüt', u'tehdültæ', u'tehtünæ', ): u'tehtü' ,
            ( u'læmmön', u'læmpö', u'læmmöt', u'læmmöltæ', u'læmpönæ', ): u'læmpö' ,
            ( u'laŋŋan', u'laŋka', u'laŋŋat', u'laŋŋalta', u'laŋkana', ): u'laŋka' ,
            ( u'sæŋŋün', u'sæŋkü', u'sæŋŋüt', u'sæŋŋültæ', u'sæŋkünæ', ): u'sæŋkü' ,
            ( u'hinnan', u'hinta', u'hinnat', u'hinnalta', u'hintana', ): u'hinta' ,
            ( u'linnun', u'lintu', u'linnut', u'linnulta', u'lintuna', ): u'lintu' ,
            ( u'opinnon', u'opinto', u'opinnot', u'opinnolta', u'opintona', ): u'opinto' ,
            ( u'rannan', u'ranta', u'rannat', u'rannalta', u'rantana', ): u'ranta' ,
            ( u'luonnon', u'luonto', u'luonnot', u'luonnolta', u'luontona', ): u'luonto' ,
            ( u'punnan', u'punta', u'punnat', u'punnalta', u'puntana', ): u'punta' ,
            ( u'tunnin', u'tunti', u'tunnit', u'tunnilta', u'tuntina', ): u'tunti' ,
            ( u'kunnon', u'kunto', u'kunnot', u'kunnolta', u'kuntona', ): u'kunto' ,
            ( u'kannun', u'kannu', u'kannut', u'kannulta', u'kannuna', ): u'kannu' ,
            ( u'linnan', u'linna', u'linnat', u'linnalta', u'linnana', ): u'linna' ,
            ( u'tumman', u'tumma', u'tummat', u'tummalta', u'tummana', ): u'tumma' ,
            ( u'auriŋŋon', u'auriŋko', u'auriŋŋot', u'auriŋŋolta', u'auriŋkona', ): u'auriŋko' ,
            ( u'reŋŋin', u'reŋki', u'reŋŋit', u'reŋŋiltæ', u'reŋkinæ', ): u'reŋki' ,
            ( u'vaŋŋin', u'vaŋki', u'vaŋŋit', u'vaŋŋilta', u'vaŋkina', ): u'vaŋki' ,
            ( u'kellon', u'kello', u'kellot', u'kellolta', u'kellona', ): u'kello' ,
            ( u'kellan', u'kelta', u'kellat', u'kellalta', u'keltana', ): u'kelta' ,
            ( u'sillan', u'silta', u'sillat', u'sillalta', u'siltana', ): u'silta' ,
            ( u'kullan', u'kulta', u'kullat ', u'kullalta ', u'kultana ', ): u'kulta' ,
            ( u'virran', u'virta', u'virrat', u'virralta', u'virtana', ): u'virta' ,
            ( u'parran', u'parta', u'parrat', u'parralta', u'partana', ): u'parta' ,
})

GoldSolution(name="Odden_3.7_Korean",
             prefixes=[u'',u'',u'',u'',u'',u'',u'',u'',u'',u'',u'',u'',u''],
             suffixes=[u'man',u'maŋk^hɨm',u'narɨm',u'',u'tero',u'kwa',u'pota',u'kači',u'i',u'ɨn',u'e',u'ita',u'ɨro'],
             underlyingForms={
            ( u'pamman', u'pammaŋk^hɨm', u'pamnarɨm', u'pap', u'paptero', u'papkwa', u'pappota', u'papkači', u'papi', u'papɨn', u'pape', u'papita', u'papɨro', ): u'pap' ,
            ( u'summan', u'summaŋk^hɨm', u'sumnarɨm', u'sup', u'suptero', u'supkwa', u'suppota', u'supkači', u'sup^hi', u'sup^hɨn', u'sup^he', u'sup^hita', u'sup^hɨro', ): u'sup^h' ,
            ( u'pamman', u'pammaŋk^hɨm', u'pamnarɨm', u'pam', u'pamtero', u'pamkwa', u'pampota', u'pamkači', u'pami', u'pamɨn', u'pame', u'pamita', u'pamɨro', ): u'pam' ,
            ( u'pamman', u'pammaŋk^hɨm', u'pannarɨm', u'pat', u'pattero', u'pakkwa', u'pappota', u'pakkači', u'pač^hi', u'pat^hɨn', u'pat^he', u'pač^hita', u'pat^hɨro', ): u"pat^h" ,
            ( u'namman', u'nammaŋk^hɨm', u'nannarɨm', u'nat', u'nattero', u'nakkwa', u'nappota', u'nakkači', u'nasi', u'nasɨn', u'nase', u'nasita', u'nasɨro', ): u"nas" ,
            ( u'namman', u'nammaŋk^hɨm', u'nannarɨm', u'nat', u'nattero', u'nakkwa', u'nappota', u'nakkači', u'nači', u'načɨn', u'nače', u'načita', u'načɨro', ): u"nač" ,
            ( u'namman', u'nammaŋk^hɨm', u'nannarɨm', u'nat', u'nattero', u'nakkwa', u'nappota', u'nakkači', u'nač^hi', u'nač^hɨn', u'nač^he', u'nač^hita', u'nač^hɨro', ): u"nač^h" ,
            ( u'pamman', u'pammaŋk^hɨm', u'pannarɨm', u'pan', u'pantero', u'paŋkwa', u'pampota', u'paŋkači', u'pani', u'panɨn', u'pane', u'panita', u'panɨro', ): u"pan" ,
})


GoldSolution(name="Odden_4.1_Serbo_Croatian", # ask Timothy about this
             prefixes=[u'',u'',u'',u'',u'',u'',u'',u''],
             suffixes=[u'',u'a',u'o',u'i',u'em',u'l',u'la',u'ló'],
             underlyingForms={
            ( u'križan' , u'križana' , u'križano' , u'križani' , None,  None,  None,  None,  ): u'križan' ,
            ( u'sunčan' , u'sunčana' , u'sunčano' , u'sunčani' , None,  None,  None,  None,  ): u'sunčan' ,
            ( u'svečan' , u'svečana' , u'svečano' , u'svečani' , None,  None,  None,  None,  ): u'svečan' ,
            ( u'bogat' , u'bogata' , u'bogato' , u'bogati' , None,  None,  None,  None,  ): u'bogat' ,
            ( u'rapav' , u'rapava' , u'rapavo' , u'rapavi' , None,  None,  None,  None,  ): u'rapav' ,
            ( u'mlád' , u'mladá' , u'mladó' , u'mladí' , None,  None,  None,  None,  ): u'mlád' ,
            ( u'túp' , u'tupá' , u'tupó' , u'tupí' , None,  None,  None,  None,  ): u'túp' ,
            ( u'blág' , u'blagá' , u'blagó' , u'blagí' , None,  None,  None,  None,  ): u'blág' ,
            ( u'grúb' , u'grubá' , u'grubó' , u'grubí' , None,  None,  None,  None,  ): u'grúb' ,
            ( u'béo' , u'belá' , u'beló' , u'belí' , None,  None,  None,  None,  ): u'bél' ,
            ( u'veseo' , u'vesela' , u'veselo' , u'veseli' , None,  None,  None,  None,  ): u'vesel' ,
            ( u'debéo' , u'debelá' , u'debeló' , u'debelí' , None,  None,  None,  None,  ): u'debél' ,
            ( u'mío' , u'milá' , u'miló' , u'milí' , None,  None,  None,  None,  ): u'míl' ,
            ( u'zelén' , u'zelená' , u'zelenó' , u'zelení' , None,  None,  None,  None,  ): u'zelén' ,
            ( u'kradén' , u'kradená' , u'kradenó' , u'kradení' , None,  None,  None,  None,  ): u'kradén' ,
            ( u'dalék' , u'daleká' , u'dalekó' , u'dalekí' , None,  None,  None,  None,  ): u'dalék' ,
            ( u'visók' , u'visoká' , u'visokó' , u'visokí' , None,  None,  None,  None,  ): u'visók' ,
            ( u'dubók' , u'duboká' , u'dubokó' , u'dubokí' , None,  None,  None,  None,  ): u'dubók' ,
            ( u'yásan' , u'yasná' , u'yasnó' , u'yasní' , None,  None,  None,  None,  ): u'yásn' ,
            ( u'vážan' , u'važná' , u'važnó' , u'važní' , None,  None,  None,  None,  ): u'vážn' ,
            ( u'sítan' , u'sitná' , u'sitnó' , u'sitní' , None,  None,  None,  None,  ): u'sítn' ,
            ( u'ledan' , u'ledna' , u'ledno' , u'ledni' , None,  None,  None,  None,  ): u'ledn' ,
            ( u'tának' , u'tanká' , u'tankó' , u'tankí' , None,  None,  None,  None,  ): u'tánk' ,
            ( u'krátak' , u'kratká' , u'kratkó' , u'kratkí' , None,  None,  None,  None,  ): u'krátk' ,
            ( u'blízak' , u'bliská' , u'bliskó' , u'bliskí' , None,  None,  None,  None,  ): u'blízk' ,
            ( u'úzak' , u'uská' , u'uskó' , u'uskí' , None,  None,  None,  None,  ): u'úzk' ,
            ( u'dóbar' , u'dobrá' , u'dobró' , u'dobrí' , None,  None,  None,  None,  ): u'dóbr' ,
            ( u'óštar' , u'oštrá' , u'oštró' , u'oštrí' , None,  None,  None,  None,  ): u'óštr' ,
            ( u'bodar' , u'bodra' , u'bodro' , u'bodri' , None,  None,  None,  None,  ): u'bodr' ,
            ( u'ustao' , u'ustala' , u'ustalo' , u'ustali' , None,  None,  None,  None,  ): u'ustal' ,
            ( u'múkao' , u'muklá' , u'mukló' , u'muklí' , None,  None,  None,  None,  ): u'múkl' ,
            ( u'óbao' , u'oblá' , u'obló' , u'oblí' , None,  None,  None,  None,  ): u'óbl' ,
            ( u'pódao' , u'podlá' , u'podló' , u'podlí' , None,  None,  None,  None,  ): u'pódl' ,
            ( None,  None,  None,  None,  u'tepém' , u'tépao' , u'teplá' , u'tepló' , ): u'tép' ,
            ( None,  None,  None,  None,  u'skubém' , u'skúbao' , u'skublá' , u'skubló' , ): u'zkúb' ,
            ( None,  None,  None,  None,  u'tresém' , u'trésao' , u'treslá' , u'tresló' , ): u'trés' ,
            ( None,  None,  None,  None,  u'vezém' , u'vézao' , u'vezlá' , u'vezló' , ): u'véz' ,
})

GoldSolution(name="Odden_4.2_Standard_Ukrainian",
             prefixes=[u'',u'',u'',u'',u'',u'',u'',u'',u'',u''],
             suffixes=[u'',u'am',u'ov^yi',u'i',u'ov^yi',u'o',u'a',u'u',u'i',u''],
             underlyingForms={
            ( u'zub' , u'zubam' , u'zubov^yi' , u'zub^yi' , None,  None,  None,  None,  None,  None,  ): u'zub' ,
            ( u'sv^yit' , u'sv^yitam' , u'sv^yitov^yi' , u'sv^yit^yi' , None,  None,  None,  None,  None,  None,  ): u'sv^yit' ,
            ( u'z^yat^y' , u'z^yat^yam' , u'z^yatev^yi' , None,  u'z^yatev^yi' , None,  None,  None,  None,  None,  ): u'z^yat^y' ,
            ( u'koš^yil^y' , u'košel^yam' , u'košelev^yi' , u'košel^yi' , None,  None,  None,  None,  None,  None,  ): u'koš^yel^y' ,
            ( u'zlod^yiy' , u'zlod^yiyam' , u'zlod^yiyev^yi' , None,  u'zlod^yiyev^yi' , None,  None,  None,  None,  None,  ): {u'zlodiy',u'zlod^yiy'} ,
            ( u'm^yis^yat^s^y' , u'm^yis^yat^s^yam' , u'm^yis^yat^sev^yi' , u'm^yis^yat^s^yi' , None,  None,  None,  None,  None,  None,  ): u'm^yis^yat^s^y' ,
            ( u'korovay' , u'korovayam' , u'korovayev^yi' , u'korovayi' , None,  None,  None,  None,  None,  None,  ): u'korovay' ,
            ( u'kam^yin^y' , u'kamen^yam' , u'kamenev^yi' , u'kamen^yi' , None,  None,  None,  None,  None,  None,  ): u'kam^yen^y' ,
            ( u'm^yid^y' , u'm^yid^yam' , u'm^yidev^yi' , u'm^yid^yi' , None,  None,  None,  None,  None,  None,  ): u'mid^y' ,
            ( u'xl^yiw' , u'xl^yivam' , u'xl^yivov^yi' , u'xl^yiv^yi' , None,  None,  None,  None,  None,  None,  ): {u'xliv',u'xl^yiv'},
            ( u'holub' , u'holubam' , u'holubov^yi' , u'holub^yi' , None,  None,  None,  None,  None,  None,  ): u'holub' ,
            ( u's^yin' , u's^yinam' , u's^yinov^yi' , u's^yin^yi' , None,  None,  None,  None,  None,  None,  ): {u'sin',u's^yin' },
            ( u'leb^yid^y' , u'lebed^yam' , u'lebedev^yi' , u'lebed^yi' , None,  None,  None,  None,  None,  None,  ): u'leb^yed^y' ,
            ( u'sus^yid' , u'sus^yidam' , u'sus^yidov^yi' , None,  u'sus^yidov^yi' , None,  None,  None,  None,  None,  ): u'sus^yid' ,
            ( u'čolov^yik' , u'čolov^yikam' , u'čolov^yikov^yi' , None,  u'čolov^yikov^yi' , None,  None,  None,  None,  None,  ): u'čolov^yik' ,
            ( u'l^yid' , u'ledam' , u'ledov^yi' , u'led^yi' , None,  None,  None,  None,  None,  None,  ): u'l^yed' ,
            ( u'bil^y' , u'bol^yam' , u'bolev^yi' , u'bol^yi' , None,  None,  None,  None,  None,  None,  ): u'bol^y' ,
            ( u'riw' , u'rovam' , u'rovov^yi' , u'rov^yi' , None,  None,  None,  None,  None,  None,  ): u'rov' ,
            ( u'stiw' , u'stolam' , u'stolov^yi' , u'stol^yi' , None,  None,  None,  None,  None,  None,  ): u'stol' ,
            ( u'd^yid' , u'd^yidam' , u'd^yidov^yi' , None,  u'd^yidov^yi' , None,  None,  None,  None,  None,  ): u'd^yid' ,
            ( u'l^yit' , u'l^yotam' , u'l^yotov^yi' , u'l^yot^yi' , None,  None,  None,  None,  None,  None,  ): u'l^yot' ,
            ( u'mist' , u'mostam' , u'mostov^yi' , u'most^yi' , None,  None,  None,  None,  None,  None,  ): u'most' ,
            ( u'večir' , u'večoram' , u'večorov^yi' , u'večor^yi' , None,  None,  None,  None,  None,  None,  ): u'večor' ,
            ( None,  None,  None,  None,  None,  u't^yilo' , u't^yila' , u't^yilu' , u't^yil^yi' , u't^yiw' , ): u't^yil' ,
            ( None,  None,  None,  None,  None,  u'koleso' , u'kolesa' , u'kolesu' , u'koles^yi' , u'kol^yis' , ): u'kol^yes' ,
            ( None,  None,  None,  None,  None,  u'ozero' , u'ozera' , u'ozeru' , u'ozer^yi' , u'oz^yir' , ): u'oz^yer' ,
            ( None,  None,  None,  None,  None,  u'selo' , u'sela' , u'selu' , u'sel^yi' , u's^yiw' , ): u"s^yel" ,
            ( None,  None,  None,  None,  None,  u'pole' , u'pol^ya' , u'pol^yu' , u'pol^yi' , u'pil^y' , ): u"pol^y" ,
            ( None,  None,  None,  None,  None,  u'slovo' , u'slova' , u'slovu' , u'slov^yi' , u'sliw' , ): u'slov' ,
            ( None,  None,  None,  None,  None,  u'more' , u'mor^ya' , u'mor^yu' , u'mor^yi' , u'mir^y' , ): u"mor^y" ,
})

GoldSolution(name="Odden_4.3_Somali",
             prefixes=[u'',u'',u'',u'',u'',u''],
             suffixes=[u'',u'ta',u'o',u'ay',u'tay',u'nay'],
             underlyingForms={
            ( u'daar' , u'daarta' , u'daaro' , None,  None,  None,  ): u'daar' ,
            ( u'gees' , u'geesta' , u'geeso' , None,  None,  None,  ): u'gees' ,
            ( u'laf' , u'lafta' , u'lafo' , None,  None,  None,  ): u'laf' ,
            ( u'lug' , u'lugta' , u'luɣo' , None,  None,  None,  ): u'lug' ,
            ( u'naag' , u'naagta' , u'naaɣo' , None,  None,  None,  ): u'naag' ,
            ( u'tib' , u'tibta' , u'tiβo' , None,  None,  None,  ): u'tib' ,
            ( u'sab' , u'sabta' , u'saβo' , None,  None,  None,  ): u'sab' ,
            ( u'bad' , u'bada' , u'baðo' , None,  None,  None,  ): u'bad' ,
            ( u'šid' , u'šida' , u'šiðo' , None,  None,  None,  ): u'šid' ,
            ( u'feeḍ' , u'feeḍa' , u'feeṛo' , None,  None,  None,  ): u'feeḍ' ,
            ( u'ʕiir' , u'ʕiirta' , u'ʕiiro' , None,  None,  None,  ): u'ʕiir' ,
            ( u'ʔul' , u'ʔuša' , u'ʔulo' , None,  None,  None,  ): u'ʔul' ,
            ( u'bil' , u'biša' , u'bilo' , None,  None,  None,  ): u'bil' ,
            ( u'meel' , u'meeša' , u'meelo' , None,  None,  None,  ): u'meel' ,
            ( u'kaliil' , u'kaliiša' , u'kaliilo' , None,  None,  None,  ): u'kaliil' ,
            ( u'nayl' , u'nayša' , u'naylo' , None,  None,  None,  ): u'nayl' ,
            ( u'sun' , u'sunta' , u'sumo' , None,  None,  None,  ): u'sum' ,
            ( u'laan' , u'laanta' , u'laamo' , None,  None,  None,  ): u'laam' ,
            ( u'sin' , u'sinta' , u'simo' , None,  None,  None,  ): u'sim' ,
            ( u'dan' , u'danta' , u'dano' , None,  None,  None,  ): u'dan' ,
            ( u'daan' , u'daanta' , u'daano' , None,  None,  None,  ): u'daan' ,
            ( u'saan' , u'saanta' , u'saano' , None,  None,  None,  ): u'saan' ,
            ( u'nirig' , u'nirigta' , u'nirgo' , None,  None,  None,  ): u'nirg' ,
            ( u'yirid' , u'yirida' , u'yirdo' , None,  None,  None,  ): u'yird' ,
            ( u'hoɣol' , u'hoɣoša' , u'hoglo' , None,  None,  None,  ): u'hogl' ,
            ( u'gaβaḍ' , u'gaβaḍa' , u'gabḍo' , None,  None,  None,  ): u'gabḍ' ,
            ( u'baɣal' , u'baɣaša' , u'baglo' , None,  None,  None,  ): u'bagl' ,
            ( u'waħar' , u'waħarta' , u'waħaro' , None,  None,  None,  ): u'waħar' ,
            ( u'irbad' , u'irbada' , u'irbaðo' , None,  None,  None,  ): u'irbad' ,
            ( u'kefed' , u'kefeda' , u'kefeðo' , None,  None,  None,  ): u'kefed' ,
            ( u'šilin' , u'šilinta' , u'šilino' , None,  None,  None,  ): u'šilin' ,
            ( u'bohol' , u'bohoša' , u'boholo' , None,  None,  None,  ): u'bohol' ,
            ( u'ʔaayad' , u'ʔaayada' , u'ʔaayaðo' , None,  None,  None,  ): u'ʔaayad' ,
            ( u'gaʕan' , u'gaʕanta' , u'gaʕmo' , None,  None,  None,  ): u'gaʕm' ,
            ( u'ʔinan' , u'ʔinanta' , u'ʔinano' , None,  None,  None,  ): u'ʔinan' ,
            ( None,  None,  None,  u'suɣay' , u'sugtay' , u'sugnay' , ): u'sug' ,
            ( None,  None,  None,  u'kaβay' , u'kabtay' , u'kabnay' , ): u'kab' ,
            ( None,  None,  None,  u'siðay' , u'siday' , u'sidnay' , ): u'sid' ,
            ( None,  None,  None,  u'dilay' , u'dišay' , u'dillay' , ): u"dil",
            ( None,  None,  None,  u'ganay' , u'gantay' , u'gannay' , ): u'gan' ,
            ( None,  None,  None,  u'tumay' , u'tuntay' , u'tunnay' , ): u"tum" ,
            ( None,  None,  None,  u'argay' , u'aragtay' , u'aragnay' , ): u"arg" ,
            ( None,  None,  None,  u'gudbay' , u'guðubtay' , u'guðubnay' , ): u"gudb" ,
            ( None,  None,  None,  u'qoslay' , u'qosošay' , u'qosollay' , ): u"qosl" ,
            ( None,  None,  None,  u'hadlay' , u'haðašay' , u'haðallay' , ): u"hadl",
})

GoldSolution(name="Odden_4.4_Latin",
             prefixes=[u'',u'',u''],
             suffixes=[u's',u'is',u'i:'],
             underlyingForms={
            ( u'arks' , u'arkis' , None,  ): u'ark' ,
            ( u'duks' , u'dukis' , None,  ): u'duk' ,
            ( u'daps' , u'dapis' , None,  ): u'dap' ,
            ( u're:ks' , u're:gis' , None,  ): u're:g' ,
            ( u'falanks' , u'falangis' , None,  ): u'falang' ,
            ( u'filiks' , u'filikis' , None,  ): u'filik' ,
            ( u'lapis' , u'lapidis' , None,  ): u'lapid' ,
            ( u'li:s' , u'li:tis' , None,  ): u'li:t' ,
            ( u'fraws' , u'frawdis' , None,  ): u'frawd' ,
            ( u'noks' , u'noktis' , None,  ): u'nokt' ,
            ( u'frons' , u'frontis' , None,  ): u'front' ,
            ( u'frons' , u'frondis' , None,  ): u'frond' ,
            ( u'inku:s' , u'inku:dis' , None,  ): u'inku:d' ,
            ( u'sors' , u'sortis' , None,  ): u'sort' ,
            ( u'fu:r' , u'fu:ris' , None,  ): u'fu:r' ,
            ( u'murmur' , u'murmuris' , None,  ): u'murmur' ,
            ( u'augur' , u'auguris' , None,  ): u'augur' ,
            ( u'arbor' , u'arboris' , None,  ): u'arbor' ,
            ( u'pugil' , u'pugilis' , None,  ): u'pugil' ,
            ( u'sal' , u'salis' , None,  ): u'sal' ,
            ( u'adeps' , u'adipis' , None,  ): u'adep' ,
            ( u'apeks' , u'apikis' , None,  ): u'apek' ,
            ( u'pri:nkeps' , u'pri:nkipis' , None,  ): u'pri:nkep' ,
            ( u'ekwes' , u'ekwitis' , None,  ): u'ekwet' ,
            ( u'miles' , u'militis' , None,  ): u'milet' ,
            ( u'no:men' , u'no:minis' , None,  ): u'no:men' ,
            ( u'karmen' , u'karminis' , None,  ): u'karmen' ,
            ( u'lu:men' , u'lu:minis' , None,  ): u'lu:men' ,
            ( u'wenter' , u'wentris' , None,  ): u'wentr' ,
            ( u'pater' , u'patris' , None,  ): u'patr' ,
            ( u'kada:wer' , u'kada:weris' , None,  ): u'kada:wer' ,
            ( u'tu:ber' , u'tu:beris' , None,  ): u'tu:ber' ,
            ( u'piper' , u'piperis' , None,  ): u'piper' ,
            ( u'karker' , u'karkeris' , None,  ): u'karker' ,
            ( u'die:s' , None,  u'die:i:' , ): u'die:' ,
            ( u'li:ber' , None,  u'li:beri:' , ): u'li:ber' ,
            ( u'miser' , None,  u'miseri:' , ): u'miser' ,
            ( u'ager' , None,  u'agri:' , ): u'agr' ,
            ( u'sinister' , None,  u'sinistri:' , ): u'sinistr' ,
            ( u'liber' , None,  u'libri:' , ): u'libr' ,
            ( u'as' , u'assis' , None,  ): u'ass' ,
            ( u'os' , u'ossis' , None,  ): u'oss' ,
            ( u'far' , u'farris' , None,  ): u'farr' ,
            ( u'mel' , u'mellis' , None,  ): u"mell",
            ( u'o:s' , u'o:ris' , None,  ): u"o:s",
            ( u'flo:s' , u'flo:ris' , None,  ): u"flo:s" ,
            ( u'mu:s' , u'mu:ris' , None,  ): u"mu:s",
            ( u'cru:s' , u'cru:ris' , None,  ): u"kru:s",
            ( u'kinis' , u'kineris' , None,  ): u"kinis",
            ( u'pulvis' , u'pulveris' , None,  ): u"pulvis",
})

GoldSolution(name="Odden_4.5_Turkish",
             prefixes=[u'',u'',u'',u'',u''],
             suffixes=[u'',u'sɨ',u'ya',u'dan',u'lar'],
             underlyingForms={
            ( u'oda' , u'odasɨ' , u'odaya' , u'odadan' , u'odalar' , ): u'oda' ,
            ( u'dere' , u'deresi' , u'dereye' , u'dereden' , u'dereler' , ): u'dere' ,
            ( u'ütü' , u'ütüsü' , u'ütüye' , u'ütüden' , u'ütüler' , ): u'ütü' ,
            ( u'balo' , u'balosu' , u'baloya' , u'balodan' , u'balolar' , ): u'balo' ,
            ( u'arɨ' , u'arɨsɨ' , u'arɨya' , u'arɨdan' , u'arɨlar' , ): u'arɨ' ,
            ( u'la:' , u'la:sɨ' , u'la:ya' , u'la:dan' , u'la:lar' , ): u'la:' ,
            ( u'bina:' , u'bina:sɨ' , u'bina:ya' , u'bina:dan' , u'bina:lar' , ): u'bina:' ,
            ( u'imla:' , u'imla:sɨ' , u'imla:ya' , u'imla:dan' , u'imla:lar' , ): u'imla:' ,
            ( u'be:' , u'be:si' , u'be:ye' , u'be:den' , u'be:ler' , ): u'be:' ,
            ( u'kep' , u'kepi' , u'kepe' , u'kepten' , u'kepler' , ): u'kep' ,
            ( u'at' , u'atɨ' , u'ata' , u'attan' , u'atlar' , ): u'at' ,
            ( u'ek' , u'eki' , u'eke' , u'ekten' , u'ekler' , ): u'ek' ,
            ( u'ok' , u'oku' , u'oka' , u'oktan' , u'oklar' , ): u'ok' ,
            ( u'güč' , u'güǰü' , u'güǰe' , u'güčten' , u'güčler' , ): u'güǰ' ,
            ( u'ahmet' , u'ahmedi' , u'ahmede' , u'ahmetten' , u'ahmetler' , ): u'ahmed' ,
            ( u'kurt' , u'kurdu' , u'kurda' , u'kurttan' , u'kurtlar' , ): u'kurd' ,
            ( u'türk' , u'türkü' , u'türke' , u'türkten' , u'türkler' , ): u'türk' ,
            ( u'genč' , u'genči' , u'genče' , u'genčten' , u'genčler' , ): u'genč' ,
            ( u'halk' , u'halkɨ' , u'halka' , u'halktan' , u'halklar' , ): u'halk' ,
            ( u'üst' , u'üstü' , u'üste' , u'üstten' , u'üstler' , ): u'üst' ,
            ( u'sarp' , u'sarpɨ' , u'sarpa' , u'sarptan' , u'sarplar' , ): u'sarp' ,
            ( u'harp' , u'harbɨ' , u'harba' , u'harptan' , u'harplar' , ): u'harb' ,
            ( u'alt' , u'altɨ' , u'alta' , u'alttan' , u'altlar' , ): u'alt' ,
            ( u'renk' , u'rengi' , u'renge' , u'renkten' , u'renkler' , ): u'reng' ,
            ( u'his' , u'hissi' , u'hisse' , u'histen' , u'hisler' , ): u"hiss",
            ( u'hür' , u'hürrü' , u'hürre' , u'hürden' , u'hürler' , ): u'hürr' ,
            ( u'mahal' , u'mahallɨ' , u'mahalla' , u'mahaldan' , u'mahallar' , ): u'mahall' ,
            ( u'hak' , u'hakkɨ' , u'hakka' , u'haktan' , u'haklar' , ): u"hakk",
            ( u'zam' , u'zammɨ' , u'zamma' , u'zamdan' , u'zamlar' , ): u"zamm",
            ( u'af' , u'affɨ' , u'affa' , u'aftan' , u'aflar' , ): u"aff",
            ( u'arap' , u'arabɨ' , u'araba' , u'araptan' , u'araplar' , ): u'arab' ,
            ( u'koyun' , u'koyunu' , u'koyuna' , u'koyundan' , u'koyunlar' , ): u'koyun' ,
            ( u'pilot' , u'pilotu' , u'pilota' , u'pilottan' , u'pilotlar' , ): u"pilot",
            ( u'kitap' , u'kitabɨ' , u'kitaba' , u'kitaptan' , u'kitaplar' , ): u"kitap",
            ( u'domuz' , u'domuzu' , u'domuza' , u'domuzdan' , u'domuzlar' , ): u"domuz",
            ( u'davul' , u'davulu' , u'davula' , u'davuldan' , u'davullar' , ): u"davul",
            ( u'bayɨr' , u'bayɨrɨ' , u'bayɨra' , u'bayɨrdan' , u'bayɨrlar' , ): u'bayɨr',
            ( u'somun' , u'somunu' , u'somuna' , u'somundan' , u'somunlar' , ): u'somun' ,
            ( u'fikir' , u'fikri' , u'fikre' , u'fikirden' , u'fikirler' , ): u"fikr",
            ( u'isim' , u'ismi' , u'isme' , u'isimden' , u'isimler' , ): u"ism",
            ( u'boyun' , u'boynu' , u'boyna' , u'boyundan' , u'boyunlar' , ): u"boyn" ,
            ( u'čevir' , u'čevri' , u'čevre' , u'čevirden' , u'čevirler' , ): u'čevr' ,
            ( u'devir' , u'devri' , u'devre' , u'devirden' , u'devirler' , ): u"devr",
            ( u'koyun' , u'koynu' , u'koyna' , u'koyundan' , u'koyunlar' , ): u"koyn",
            ( u'karɨn' , u'karnɨ' , u'karna' , u'karɨndan' , u'karɨnlar' , ): u"kam",
            ( u'burun' , u'burnu' , u'burna' , u'burundan' , u'burunlar' , ): u"burn",
            ( u'akɨl' , u'aklɨ' , u'akla' , u'akɨldan' , u'akɨllar' , ): u"akl",
            ( u'šehir' , u'šehri' , u'šehre' , u'šehirden' , u'šehirler' , ):  u'šehr',
            ( u'namaz' , u'namazɨ' , u'namaza' , u'namazdan' , u'namazlar' , ): u"namaz" ,
            ( u'zaman' , u'zama:nɨ' , u'zama:na' , u'zamandan' , u'zamanlar' , ): u"zama:n",
            ( u'harap' , u'hara:bɨ' , u'hara:ba' , u'haraptan' , u'haraplar' , ): u"hara:b",
            ( u'i:kaz' , u'i:ka:zɨ' , u'i:ka:za' , u'i:kazdan' , u'i:kazlar' , ): u"i:ka:z",
            ( u'hayat' , u'haya:tɨ' , u'haya:ta' , u'hayattan' , u'hayatlar' , ): u"haya:t",
            ( u'ispat' , u'ispa:tɨ' , u'ispa:ta' , u'ispattan' , u'ispatlar' , ): u"ispa:t",
            ( u'inek' , u'inei' , u'inee' , u'inekten' , u'inekler' , ): u"inek",
            ( u'mantɨk' , u'mantɨɨ' , u'mantɨa' , u'mantɨktan' , u'mantɨklar' , ): u'mantɨk' ,
            ( u'ayak' , u'ayaɨ' , u'ayaa' , u'ayaktan' , u'ayaklar' , ): u"ayak",
            ( u'čabuk' , u'čabuu' , u'čabua' , u'čabuktan' , u'čabuklar' , ):  u'čabuk',
            ( u'dakik' , u'dakii' , u'dakie' , u'dakikten' , u'dakikler' , ): u"dakik",
            ( u'merak' , u'mera:kɨ' , u'mera:ka' , u'meraktan' , u'meraklar' , ): u"mera:k" ,
            ( u'tebrik' , u'tebri:ki' , u'tebri:ke' , u'tebrikten' , u'tebrikler' , ): u"tebri:k" ,
            ( u'hukuk' , u'huku:ku' , u'huku:ka' , u'hukuktan' , u'hukuklar' , ): u"huku:k",
})

GoldSolution(name="Odden_4.6_Kera",
             prefixes=[u'',u'',u'',u'',u'',u''],
             suffixes=[u'n',u'm',u'i',u'u',u'a',u'ŋ'],
             underlyingForms={
            ( u'haman' , u'hamam' , u'hɨmi' , u'hɨmu' , u'hama' , u'hamaŋ' , ): u'ham' ,
            ( u'se:nen' , u'se:nem' , u'si:ni' , u'si:nu' , u'se:na' , u'se:neŋ' , ): u'se:n' ,
            ( u'kolon' , u'kolom' , u'kuli' , u'kulu' , u'kola' , u'koloŋ' , ): u'kol' ,
            ( u'gi:din' , u'gi:dim' , u'gi:di' , u'gi:du' , u'gi:dɨ' , u'gi:diŋ' , ): u'gi:d' ,
            ( u'cɨ:rɨn' , u'cɨ:rɨm' , u'ci:ri' , u'cu:ru' , u'cɨ:rɨ' , u'cɨ:rɨŋ' , ): u'cɨ:r',
            ( u'gunun' , u'gunum' , u'guni' , u'gunu' , u'gunɨ' , u'gunuŋ' , ): u"gun",
            ( u'bɨlan' , u'bɨlam' , u'bɨli' , u'bɨlu' , u'bɨla' , u'bɨlaŋ' , ): u"bal",
            ( u'ŋɨfan' , u'ŋɨfam' , u'ŋɨfi' , u'ŋɨfu' , u'ŋɨfa' , u'ŋɨfaŋ' , ): u'ŋaf',
            ( u'ʔasan' , u'ʔasam' , u'ʔɨsi' , u'ʔɨsu' , u'ʔasa' , u'ʔasaŋ' , ): u'ʔas',
            ( u'ʔapan' , u'ʔapam' , u'ʔɨpi' , u'ʔɨpu' , u'ʔapa' , u'ʔapaŋ' , ): u'ʔap' ,
            ( u'haran' , u'haram' , u'hɨri' , u'hɨru' , u'hara' , u'haraŋ' , ): u'har' ,
            ( u'balnan' , u'balnam' , u'bɨlni' , u'bɨlnu' , u'balna' , u'balnaŋ' , ): u"baln" ,
            ( u'ŋafnan' , u'ŋafnam' , u'ŋɨfni' , u'ŋɨfnu' , u'ŋafna' , u'ŋafnaŋ' , ): u'ŋafn',
})

GoldSolution(name="Odden_4.9_Lardil",
             prefixes=[u'',u'',u'',u''],
             suffixes=[u'',u'in',u'ŋar',u'uṛ'],
             underlyingForms={
            ( u'kentapal' , u'kentapalin' , u'kentapalŋar' , u'kentapaluṛ' , ): u'kentapal' ,
            ( u'ketar' , u'ketarin' , u'ketarŋar' , u'ketaruṛ' , ): u'ketar' ,
            ( u'miyaṛ' , u'miyaṛin' , u'miyaṛŋar' , u'miyaṛuṛ' , ): u'miyaṛ' ,
            ( u'yupur' , u'yupurin' , u'yupurŋar' , u'yupuruṛ' , ): u'yupur' ,
            ( u'taŋur' , u'taŋurin' , u'taŋurŋar' , u'taŋuruṛ' , ): u'taŋur' ,
                 # you are not allowed to have /nu/
                 # so you have to break it up with a /k/
                 # this is reasonable because we basically never see /nu/ on the surface
                 # also delete nasal following nasal
            ( u'yaraman' , u'yaramanin' , u'yaramanar' , u'yaramankuṛ' , ): u'yaraman' ,
            ( u'maaṇ' , u'maaṇin' , u'maaṇar' , u'maaṇkuṛ' , ): u'maaṇ' ,
            ( u'pirŋen' , u'pirŋenin' , u'pirŋenar' , u'pirŋenkuṛ' , ): u'pirŋen' ,
                 # V > 0 / V _
            ( u'mela' , u'melan' , u'melaŋar' , u'melaṛ' , ): u'mela' ,
            ( u'tawa' , u'tawan' , u'tawaŋar' , u'tawaṛ' , ): u'tawa' ,
            ( u'wanka' , u'wankan' , u'wankaŋar' , u'wankaṛ' , ): u'wanka' ,
            ( u'kuŋka' , u'kuŋkan' , u'kuŋkaŋar' , u'kuŋkaṛ' , ): u'kuŋka' ,
            ( u'tarŋka' , u'tarŋkan' , u'tarŋkaŋar' , u'tarŋkaṛ' , ): u'tarŋka' ,
                 # some kind of harmony
                 # contrast with above cases: very similar
                 # what must be going on is u > a, not the other way around
            ( u'ŋuka' , u'ŋukun' , u'ŋukuŋar' , u'ŋukuṛ' , ): u'ŋuku' ,
            ( u'ŋuṛa' , u'ŋuṛun' , u'ŋuṛuŋar' , u'ŋuṛuṛ' , ): u'ŋuṛu' ,
            ( u'kaṭa' , u'kaṭun' , u'kaṭuŋar' , u'kaṭuṛ' , ): u'kaṭu' ,
            ( u'muṇa' , u'muṇun' , u'muṇuŋar' , u'muṇuṛ' , ): u'muṇu' ,
            ( u'ŋawa' , u'ŋawun' , u'ŋawuŋar' , u'ŋawuṛ' , ): u'ŋawu' ,
                 # this is where I get confused
            ( u'keṇṭe' , u'keṇṭin' , u'keṇṭiŋar' , u'keṇṭiwuṛ' , ): u'keṇṭi',
            ( u'tyimpe' , u'tyimpin' , u'tyimpiŋar' , u'tyimpiwuṛ' , ): u'tyimpi' ,
            ( u'ŋiṇe' , u'ŋiṇin' , u'ŋiṇiŋar' , u'ŋiṇiwuṛ' , ): u'ŋiṇi' ,
            ( u'pape' , u'papin' , u'papiŋar' , u'papiwuṛ' , ): u'papi' ,
            ( u'tyempe' , u'tyempen' , u'tyempeŋar' , u'tyempeṛ' , ): u'tyempe' ,
            ( u'wiṭe' , u'wiṭen' , u'wiṭeŋar' , u'wiṭeṛ' , ): u'wiṭe' ,
            ( u'waŋal' , u'waŋalkin' , u'waŋalkar' , u'waŋalkuṛ' , ): u'waŋalk' ,
            ( u'menyel' , u'menyelkin' , u'menyelkar' , u'menyelkuṛ' , ): u'menyelk' ,
            ( u'makar' , u'makarkin' , u'makarkar' , u'makarkuṛ' , ): u'makark' ,
            ( u'yalul' , u'yalulun' , u'yaluluŋar' , u'yaluluṛ' , ): u'yalulu' ,
            ( u'mayar' , u'mayaran' , u'mayaraŋar' , u'mayaraṛ' , ): u'mayara' ,
            ( u'talkur' , u'talkuran' , u'talkuraŋar' , u'talkuraṛ' , ): u'talkura' ,
            ( u'wiwal' , u'wiwalan' , u'wiwalaŋar' , u'wiwalaṛ' , ): u'wiwala' ,
            ( u'karikar' , u'karikarin' , u'karikariŋar' , u'karikariwuṛ' , ): u'karikari' ,
            ( u'yiliyil' , u'yiliyilin' , u'yiliyiliŋar' , u'yiliyiliwuṛ' , ): u'yiliyili' ,
            ( u'yukar' , u'yukarpan' , u'yukarpaŋar' , u'yukarpaṛ' , ): u'yukarpa' ,
            ( u'pulŋar' , u'pulŋarpan' , u'pulŋarpaŋar' , u'pulŋarpaṛ' , ): u'pulŋarpa' ,
            ( u'wulun' , u'wulunkan' , u'wulunkaŋar' , u'wulunkaṛ' , ): u'wulunka' ,
            ( u'wuṭal' , u'wuṭaltyin' , u'wuṭaltyiŋar' , u'wuṭaltyiwur' , ): u'wuṭaltyi' ,
            ( u'kantukan' , u'kantukantun' , u'kantukantuŋar' , u'kantukantuṛ' , ): u'kantukantu' ,
            ( u'karwakar' , u'karwakarwan' , u'karwakarwaŋar' , u'karwakarwaṛ' , ): u'karwakarwa' ,
            ( u'turara' , u'turaraŋin' , u'turaraŋar' , u'turaraŋkuṛ' , ): u'turaraŋ' ,
            ( u'ŋalu' , u'ŋalukin' , u'ŋalukar' , u'ŋalukuṛ' , ): u'ŋaluk' ,
            ( u'kurka' , u'kurkaŋin' , u'kurkaŋar' , u'kurkaŋkuṛ' , ): u'kurkaŋ' ,
            ( u'taŋku' , u'taŋkuŋin' , u'taŋkuŋar' , u'taŋkuŋkuṛ' , ): u'taŋkuŋ' ,
            ( u'kurpuṛu' , u'kurpuṛuŋin' , u'kurpuṛuŋar' , u'kurpuṛuŋkuṛ' , ): u'kurpuṛuŋ' ,
            ( u'putu' , u'putukan' , u'putukaŋar' , u'putukaṛ' , ): u'putuka' ,
            ( u'maali' , u'maaliyan' , u'maaliyaŋar' , u'maaliyaṛ' , ): u'maaliya' ,
            ( u'tyiṇtirpu' , u'tyiṇtirpuwan' , u'tyiṇtirpuwaŋar' , u'tyiṇtirpuwaṛ' , ): u'tyiṇtirpuwa' ,
            ( u'pukatyi' , u'pukatyiyan' , u'pukatyiyaŋar' , u'pukatyiyaṛ' , ): u'pukatyiya' ,
            ( u'murkuni' , u'murkuniman' , u'murkunimaŋar' , u'murkunimaṛ' , ): u'murkunima' ,
            ( u'ŋawuŋa' , u'ŋawuŋawun' , u'ŋawuŋawuŋar' , u'ŋawuŋawuṛ' , ): u'ŋawuŋawa' ,
            ( u'tipiti' , u'tipitipin' , u'tipitipiŋar' , u'tipitipiwuṛ' , ): u'tipitipi' ,
            ( u'tapu' , u'taputyin' , u'taputyiŋar' , u'taputyiwuṛ' , ): u'taputyi' ,
            ( u'muŋkumu' , u'muŋkumuŋkun' , u'muŋkumuŋkuŋar' , u'muŋkumuŋkuṛ' , ): u'muŋkumuŋku' ,
            ( u'tyumputyu' , u'tyumputyumpun' , u'tyumputyumpuŋar' , u'tyumputyumpuṛ' , ): u'tyumputyumpu'
})

GoldSolution(name="Odden_4.11_Sadzava_Ukrainian",
             prefixes=[u'',u'',u'',u'',u'',u'',u'',u''],
             suffixes=[u'',u'a',u'i',u'',u'',u'',u'',u''],
             underlyingForms={
            ( u'plast' , u'plasta' , u'plas^yk^yi' , None,  None,  None,  None,  None,  ): u'plast' ,
            ( u'skorux' , u'skoruxa' , u'skorus^yi' , None,  None,  None,  None,  None,  ): u'skorux' ,
            ( u'ɣ^yr^yix' , u'ɣ^yr^yixa' , u'ɣ^yr^yis^yi' , None,  None,  None,  None,  None,  ): u'ɣrix' ,
            ( u'pastux' , u'pastuxa' , u'pastus^yi' , None,  None,  None,  None,  None,  ): u'pastux' ,
            ( u'm^yn^yux' , u'm^yn^yuxa' , u'm^yn^yus^yi' , None,  None,  None,  None,  None,  ): u'mn^yux' ,
            ( u'pluɣ' , u'pluɣa' , u'pluz^yi' , None,  None,  None,  None,  None,  ): u'pluɣ' ,
            ( u's^yt^yiɣ' , u'stoɣa' , u'stoz^yi' , None,  None,  None,  None,  None,  ): u'stoɣ' ,
            ( u'sak' , u'saka' , u'sats^yi' , None,  None,  None,  None,  None,  ): u'sak',
            ( u'bek' , u'bəka' , u'bəts^yi' , None,  None,  None,  None,  None,  ): u"bek",
            ( u'lest' , u'ləsta' , u'ləs^yk^yi' , None,  None,  None,  None,  None,  ): u"lest" ,
            ( u'lest' , u'lesta' , u'les^yk^yi' , None,  None,  None,  None,  None,  ): u'lest' ,
            ( u'p^yl^yit' , u'plota' , u'plok^yi' , None,  None,  None,  None,  None,  ): u"plot" ,
            ( u's^ym^yr^yid' , u'smroda' , u'smrog^yi' , None,  None,  None,  None,  None,  ): u"smrod" ,
            ( u'f^yist' , u'fosta' , u'fos^yk^yi' , None,  None,  None,  None,  None,  ): u"fost" ,
            ( u'm^yist' , u'mosta' , u'mos^yk^yi' , None,  None,  None,  None,  None,  ): u"most",
            ( u'l^yid' , u'lædu' , u'lədu' , None,  None,  None,  None,  None,  ): u"lod",
            ( u'd^yr^yit' , u'drota' , u'drok^yi' , None,  None,  None,  None,  None,  ): u"drot" ,
            ( u'm^yid' , u'mædu' , u'mədu' , None,  None,  None,  None,  None,  ): u'mæd',
            ( u'v^yil' , u'vola' , u'vol^yi' , None,  None,  None,  None,  None,  ):  u'vol',
            ( u'v^yiz' , u'voza' , u'voz^yi' , None,  None,  None,  None,  None,  ): u"voz",
            ( u'ser' , u'sera' , u'ser^yi' , None,  None,  None,  None,  None,  ): u"ser",
            ( u's^yn^yip' , u'snopa' , u'snop^yi' , None,  None,  None,  None,  None,  ): u"snop" ,
            ( u'ɣreb' , u'ɣrəba' , u'ɣrəb^yi' , None,  None,  None,  None,  None,  ): u'ɣreb',
            ( u'læb^yid' , u'læbəda' , u'læbəg^yi' , None,  None,  None,  None,  None,  ): u'læbæd' ,
            ( u'bær^yiɣ' , u'bærəɣa' , u'bærəz^yi' , None,  None,  None,  None,  None,  ): u'bæræɣ',
            ( u'pər^yiɣ' , u'pəroɣa' , u'pəroz^yi' , None,  None,  None,  None,  None,  ): u'pəroɣ' ,
            ( u'por^yiɣ' , u'poroɣa' , u'poroz^yi' , None,  None,  None,  None,  None,  ): u'poroɣ' ,
            ( u'bol^yek' , u'bol^yəka' , u'bol^yəts^yi' , None,  None,  None,  None,  None,  ): u'bol^yek' ,
            ( u'vor^yiɣ' , u'voroɣa' , u'voroz^yi' , None,  None,  None,  None,  None,  ): u'voroɣ' ,
            ( u'konək' , u'konəka' , u'konəts^yi' , None,  None,  None,  None,  None,  ): u'konək' ,
            ( u'pot^yik' , u'potoka' , u'potots^yi' , None,  None,  None,  None,  None,  ): u'potok' ,
            ( u't^yik' , u'toka' , u'tots^yi' , None,  None,  None,  None,  None,  ): u'tok' ,
            ( u'k^yil' , u'kola' , u'kol^yi' , None,  None,  None,  None,  None,  ): u'kol',
            ( None,  None,  None,  u'koval^y' , u'koval^ye' , u'kovale' , None,  None,  ): u'koval^y' ,
            ( None,  None,  None,  u'ǰm^yil^y' , u'ǰm^yil^ye' , u'ǰm^yile' , None,  None,  ): u'ǰmil^y' ,
            ( None,  None,  None,  u'k^yr^yil^y' , u'k^yr^yil^ye' , u'k^yr^yile' , None,  None,  ): u'kril^y' ,
            ( None,  None,  None,  u'učetəl^y' , u'učetəl^yə' , u'učetələ' , None,  None,  ): u'učetəl^y' ,
            ( None,  None,  None,  u'græb^yin^y' , u'græbən^yə' , u'græbənə' , None,  None,  ): u'græbæn^y' ,
            ( None,  None,  None,  u'olən^y' , u'olən^yə' , u'olənə' , None,  None,  ): u'olən^y' ,
            ( None,  None,  None,  u'yač^ym^yin^y' , u'yačmæn^yə' , u'yačmænə' , None,  None,  ): u'yačmæn^y' ,
            ( None,  None,  None,  u'yas^yin^y' , u'yasən^yə' , u'yasənə' , None,  None,  ): u'yæsæn^y' ,
            ( None,  None,  None,  u'z^yek^y' , u'z^yek^yə' , u'z^yetə' , None,  None,  ): u'z^yet^y' ,
            ( None,  None,  None,  None,  None,  None,  u'mas^yk^y' , u'mastə' , ): u'mast^y' ,
            ( None,  None,  None,  None,  None,  None,  u's^ym^yir^yk^y' , u'smærtə' , ): u'smært^y' ,
            ( None,  None,  None,  None,  None,  None,  u'v^yis^yk^y' , u'v^yistə' , ): u'vist^y' ,
            ( None,  None,  None,  None,  None,  None,  u'rag^yis^yk^y' , u'radostə' , ): u"radost^y",
            ( None,  None,  None,  None,  None,  None,  u's^yil^y' , u'solə' , ): u'sol^y' ,
            ( None,  None,  None,  None,  None,  None,  u'poš^yis^yk^y' , u'pošəstə' , ): u'pošest^y'  ,
            ( None,  None,  None,  None,  None,  None,  u'zam^yik^y' , u'zamətə' , ): u'zamæt^y',
            ( None,  None,  None,  None,  None,  None,  u'skatər^yk^y' , u'skatərtə' , ): u'skatərt^y' ,
            ( None,  None,  None,  None,  None,  None,  u'k^yis^yk^y' , u'kostə' , ): u'kost^y',
})

GoldSolution(name="Odden_68_69_Russian",
             prefixes=[u'',u''],
             suffixes=[u'',u'a'],
             underlyingForms={
            ( u'vagon' , u'vagona' , ): u'vagon' ,
            ( u'avtomobil^y' , u'avtomobil^ya' , ): u'avtomobil^y' ,
            ( u'večer' , u'večera' , ): u'večer' ,
            ( u'muš' , u'muža' , ): u'muž' ,
            ( u'karandaš' , u'karandaša' , ): u'karandaš' ,
            ( u'glas' , u'glaza' , ): u'glaz' ,
            ( u'golos' , u'golosa' , ): u'golos' ,
            ( u'ras' , u'raza' , ): u'raz' ,
            ( u'les' , u'lesa' , ): u'les' ,
            ( u'porok' , u'poroga' , ): u'porog' ,
            ( u'vrak' , u'vraga' , ): u'vrag' ,
            ( u'urok' , u'uroka' , ): u'urok' ,
            ( u'porok' , u'poroka' , ): u'porok' ,
            ( u't^svet' , u't^sveta' , ): u't^svet' ,
            ( u'prut' , u'pruda' , ): u'prud' ,
            ( u'soldat' , u'soldata' , ): u'soldat' ,
            ( u'zavot' , u'zavoda' , ): u'zavod' ,
            ( u'xlep' , u'xleba' , ): u'xleb' ,
            ( u'grip' , u'griba' , ): u'grib' ,
            ( u'trup' , u'trupa' , ): u'trup' ,
})

GoldSolution(name="Halle_115_Russian", # RERUN, TODO
             prefixes=[u'',u'',u'',u''],
             suffixes=[u'ú',u'l',u'la',{u'l^yi',u'li'}],
             underlyingForms={
                 # roots end in vowels
            ( u'v^yirnú' , u'v^yirnúl' , u'v^yirnúla' , u'v^yirnúl^yi',  ): u'v^yirnú' ,
            ( u'vrú' , u'vrál' , u'vralá' , u'vrál^yi' , ): u'vrá' ,
            ( u'stayú' , u'stayál' , u'stayála' , u'stayál^yi' , ): u'stayá' ,
                 # roots end in consonant
            ( u'p^yikú' , u'p^yók' , u'p^yiklá' , u'p^yikl^yí' , ): u'p^yók' ,
            ( u'v^yizú' , u'v^yós' , u'v^yizlá' , u'v^yizl^yí' ,  ): u'v^yóz' ,
            ( u'magú' , u'mók' , u'maglá' , u'magl^yí' ,  ): u'móg' ,
                 # how do you make sense of the /n/
            ( u'móknu' , u'mók' , u'mókla' , u'mókl^yi' , ): u'mókn' ,
})

GoldSolution(
    name="Halle_149_Russian",
    prefixes=[u'',u'',u'',u''],
    suffixes=[u'á',u'',u'ɛ́',u'ɨ'],
    underlyingForms={
        ( u'luná' , u'lún' , u'lun^yɛ́' , u'lúnɨ' , ): u'lún' ,
        ( u'dɨrá' , u'dɨ́r' , u'dɨr^yɛ́' , u'dɨ́rɨ' , ): u'dɨ́r' ,
        ( u'travá' , u'tráf' , u'trav^yɛ́' , u'trávɨ' , ): u'tráv' ,
        ( u'p^yilá' , u'p^yíl' , u'p^yil^yɛ́' , u'p^yílɨ' , ): u'p^yíl' ,
        ( u'valná' , u'vóln' , u'valn^yɛ́' , u'vólnɨ' , ): u'vóln',
        ( u'galavá' , u'galóf' , u'galav^yɛ́' , u'gólavɨ' , ): u'gólov' ,
        ( u'žɨl^yizá' , u'žɨl^yós' , u'žɨl^yiz^yɛ́' , u'žél^yizɨ' , ): u'žél^yoz',
        ( u'žɨná' , u'žón' , u'žɨn^yɛ́' , u'žónɨ' , ): u'žón',
        ( u'zm^yiyá' , u'zm^yéy' , u'zm^yiyɛ́' , u'zm^yéyi' , ): u"zm^yéy",
        # how to explain this alternation?
        # the suffix changes
        # I don't trust anything onward
        ( u'm^yɛ́na' , u'm^yɛ́n' , u'm^yén^yi' , u'm^yɛ́nɨ' , ): u"m^yɛ́n^y",
        ( u'p^yil^yiná' , u'p^yil^yón' , u'p^yil^yin^yɛ́' , u'p^yil^yinɨ́' , ): u'p^yilón' ,
        ( u'b^yis^yɛ́da' , u'b^yis^yɛ́t' , u'b^yis^yéd^yi' , u'b^yis^yɛ́dɨ' , ): u'b^yisɛ́d',
        ( u'b^yidá' , u'b^yɛ́t' , u'b^yid^yɛ́' , u'b^yɛ́dɨ' , ): u'b^yɛ́d' ,
        ( u'p^yitá' , u'p^yát' , u'p^yit^yɛ́' , u'p^yitɨ́' , ): u'p^yát',
        ( u'st^yiná' , u'st^yɛ́n' , u'st^yin^yɛ́' , u'st^yɛ́nɨ' , ): u'stɛ́n' ,

        # three relate to velar
        ( u'r^yiká' , u'r^yɛ́k' , u'r^yik^yɛ́' , u'r^yék^yi' , ): u'rɛ́k',
        # this is correct
        ( u'slugá' , u'slúk' , u'slug^yɛ́' , u'slúg^yi' , ): u'slúg^y' ,
        ( u'blaxá' , u'blóx' , u'blax^yɛ́' , u'blóx^yi' , ): u'blóx^y' ,
    })

# nb: this can be analyzed with either insertion or deletion
GoldSolution(name="Odden_170_Yawelmani",
             prefixes=[u'',u'',u'',u''],
             suffixes=[u'hin',u'ka',u'al',u'it'],
             underlyingForms={
            ( u'xathin' , u'xatka' , u'xatal' , u'xatit' , ): u'xat' ,
            ( u'dubhun' , u'dubka' , u'dubal' , u'dubut' , ): u'deb' ,
            ( u'xilhin' , u'xilka' , u'xilal' , u'xilit' , ): u'xil' ,
            ( u'koʔhin' , u'koʔko' , u'koʔol' , u'koʔit' , ): u'koʔ' ,
            ( u'doshin' , u'dosko' , u'do:sol' , u'do:sit' , ): u'do:s' ,
            ( u'ṣaphin' , u'ṣapka' , u'ṣa:pal' , u'ṣa:pit' , ): u'ṣa:p' ,
            ( u'lanhin' , u'lanka' , u'la:nal' , u'la:nit' , ): u'la:n' ,
            ( u'mekhin' , u'mekka' , u'me:kal' , u'me:kit' , ): u'me:k' ,
            ( u'wonhin' , u'wonko' , u'wo:nol' , u'wo:nit' , ): u'wo:n' ,
            ( u'paxathin' , u'paxatka' , u'paxa:tal' , u'paxa:tit' , ): u'paxa:t' ,
            ( u'hiwethin' , u'hiwetka' , u'hiwe:tal' , u'hiwe:tit' , ): u'hiwe:t' ,
            ( u'ʔopothin' , u'ʔopotko' , u'ʔopo:tol' , u'ʔopo:tit' , ): u'ʔopo:t' ,
            ( u'yawalhin' , u'yawalka' , u'yawa:lal' , u'yawa:lit' , ): u"yawa:l" ,
            ( u'paʔiṭhin' , u'paʔiṭka' , u'paʔṭal' , u'paʔṭit' , ): {u'paʔiṭ',u'paʔṭ'} ,
            ( u'ʔilikhin' , u'ʔilikka' , u'ʔilkal' , u'ʔilkit' , ): {u'ʔilik',u'ʔilk'} ,
            ( u'logiwhin' , u'logiwka' , u'logwol' , u'logwit' , ): {u'logiw',u'logw'} ,
            ( u'ʔugunhun' , u'ʔugunka' , u'ʔugnal' , u'ʔugnut' , ): {u'ʔugun',u'ʔugn'} ,
            ( u'lihimhin' , u'lihimka' , u'lihmal' , u'lihmit' , ): {u'lihim',u'lihm'} ,
            ( u'ʔayiyhin' , u'ʔayiyka' , u'ʔayyal' , u'ʔayyit' , ): {u'ʔayy',u'ʔayiy'}  ,
            ( u'toyixhin' , u'toyixka' , u'toyxol' , u'toyxit' , ): {u'toyix',u'toyx'} ,
            ( u'lukulhun' , u'lukulka' , u'luklal' , u'luklut' , ): {u'lukl',u'lukul'} ,
            ( u'so:nilhin' , u'so:nilka' , u'sonlol' , u'sonlit' , ): {u"so:nil",u"so:nl"},
            ( u'ʔa:milhin' , u'ʔa:milka' , u'ʔamlal' , u'ʔamlit' , ): {u'ʔa:mil',u'ʔa:ml'},
            ( u'mo:yinhin' , u'mo:yinka' , u'moynol' , u'moynit' , ): {u'mo:yin',u'mo:yn'},
            ( u'ṣa:likhin' , u'ṣa:likka' , u'ṣalkal' , u'ṣalkit' , ): {u'ṣa:lik',u'ṣa:lk'} ,
})


GoldSolution(name="Halle_153_Yokuts", # nb: this can be analyzed either with insertion or deletion
             prefixes=[u'',u'',u''],
             suffixes=[u'it',u'hin',u'nit'],
             underlyingForms={
            ( u'xatit' , u'xathin' , u'xatnit' , ): u'xat' ,
            ( u'gopit' , u'gophin' , u'gopnit' , ): u'gop' ,
            ( u'giyit' , u'giyhin' , u'giynit' , ): u'giy' ,
            ( u'mutut' , u'muthun' , u'mutnut' , ): u'mut' ,
            ( u'sa:pit' , u'saphin' , u'sapnit' , ): u'sa:p' ,
            ( u'go:bit' , u'gobhin' , u'gobnit' , ): u'go:b' ,
            ( u'me:kit' , u'mekhin' , u'meknit' , ): u'me:k' ,
            ( u'ʔo:tut' , u'ʔothun' , u'ʔotnut' , ): u'uʔo:t' ,
            ( u'panat' , u'pana:hin' , u'pana:nit' , ): u'pana:' ,
            ( u'hoyot' , u'hoyo:hin' , u'hoyo:nit' , ): u'hoyo:' ,
            ( u'ʔilet' , u'ʔile:hin' , u'ʔile:nit' , ): u'ʔile:' ,
            ( u'cuyot' , u'cuyo:hun' , u'cuyo:nut' , ): u'cuyo:' ,
            ( u'paxa:tit' , u'paxathin' , u'paxatnit' , ): u'paxa:t' ,
            ( u'ʔopo:tit' , u'ʔopothin' , u'ʔopotnit' , ): u'ʔopo:t' ,
            ( u'hibe:yit' , u'hibeyhin' , u'hibeynit' , ): u'hibe:y' ,
            ( u'sudo:kut' , u'sudokhun' , u'sudoknut' , ): u'sudo:k' ,
})

GoldSolution(name="Halle_85_Turkish",
             prefixes=[u'',u'',u'',u''],
             suffixes=[u'',u'un',u'lar',u'larɨn'],
             underlyingForms={
            ( u'ip' , u'ipin' , u'ipler' , u'iplerin' , ): u'ip' ,
            ( u'kɨz' , u'kɨzɨn' , u'kɨzlar' , u'kɨzlarɨn' , ): u'kɨz' ,
            ( u'yüz' , u'yüzün' , u'yüzler' , u'yüzlerin' , ): u'yüz' ,
            ( u'pul' , u'pulun' , u'pullar' , u'pullarɨn' , ): u'pul' ,
            ( u'el' , u'elin' , u'eller' , u'ellerin' , ): u'el' ,
            ( u'čan' , u'čanɨn' , u'čanlar' , u'čanlarɨn' , ): u'čan' ,
            ( u'köy' , u'köyün' , u'köyler' , u'köylerin' , ): u'köy' ,
            ( u'son' , u'sonun' , u'sonlar' , u'sonlarɨn' , ): u'son' ,
})

GoldSolution(name="Halle_97_Turkish", # ask about harmony
             prefixes=[u'',u''],
             suffixes=[u'',u'i'],
             underlyingForms={
            ( u'ip' , u'ipi' , ): u'ip' ,
            ( u'bit' , u'biti' , ): u'bit' ,
            ( u'sebep' , u'sebebi' , ): u'sebib' ,
            ( u'kanat' , u'kanadɨ' , ): u'kanɨd' ,
            ( u'šeref' , u'šerefi' , ): u'šerif' ,
            ( u'kɨč' , u'kɨčɨ' , ): u'kɨč' ,
            ( u'pilot' , u'pilotu' , ): u'pilot' ,
            ( u'demet' , u'demeti' , ): u'demet' ,
            ( u'šarap' , u'šarabɨ' , ): u'šarab' ,
            ( u'ahmet' , u'ahmedi' , ): u'ahmed' ,
            ( u'pabuč' , u'pabuǰu' , ): u'pabuǰ' ,
            ( u'güč' , u'güǰü' , ): u'güǰ' ,
            ( u'sepet' , u'sepeti' , ): u'sepet' ,
            ( u'sanat' , u'sanatɨ' , ): u'sanɨt' ,
            ( u'kep' , u'kepi' , ): u'kep' ,
            ( u'kurt' , u'kurdu' , ): u'kurd' ,
            ( u'sač' , u'sačɨ' , ): u'sač' ,
            ( u'renk' , u'rengi' , ): u'reng' ,
})

GoldSolution(name="Halle_125_Indonesian", # unsure, but this is funny
             prefixes=[u'',u'məŋ'],
             suffixes=[u'',u''],
             underlyingForms={
            ( u'lempar' , u'məlempar' , ): u'lempar' ,
            ( u'rasa' , u'mərasa' , ): u'rasa' ,
            ( u'wakil' , u'məwakili' , ): u'wakil' ,
            ( u'yakin' , u'məyakini' , ): u'yakin' ,
            ( u'masak' , u'məmasak' , ): u'masak' ,
            ( u'nikah' , u'mənikah' , ): u'nikah' ,
            ( u'ŋaco' , u'məŋaco' , ): u'ŋaco' ,
            ( u'ɲaɲi' , u'məɲaɲi' , ): u'ɲaɲi' ,
            ( u'hituŋ' , u'məŋhituŋ' , ): u'hituŋ' ,
            ( u'gambar' , u'məŋgambar' , ): u'gambar' ,
            ( u'kirim' , u'məŋirim' , ): u'kirim' ,
            ( u'dəŋar' , u'məndəŋar' , ): u'dəkar' ,
            ( u'tulis' , u'mənulis' , ): u'tulis' ,
            ( u'bantu' , u'məmbantu' , ): u'bantu' ,
            ( u'pukul' , u'məmukul' , ): u'pukul' ,
            ( u'ǰahit' , u'mən̆ǰahit' , ): u'ǰahit' ,
            ( u'čatat' , u'mən̆čatat' , ): u'čatat' ,
            ( u'ambil' , u'məŋambil' , ): u'ambil' ,
            ( u'isi' , u'məŋisi' , ): u'isi' ,
            ( u'undaŋ' , u'məŋundaŋ' , ): u'undaŋ' ,
})

GoldSolution(name="Halle_109_Russian", # UNSURE
             prefixes=[u'at',u'b^yiz',u'u'],
             suffixes=[u'',u'',u''],
             underlyingForms={
            ( u'atrózɨ' , u'b^yizrózɨ' , u'urózɨ' , ): u'rózɨ' ,
            ( u'atálɨ' , u'b^yizálɨ' , u'uálɨ' , ): u'álɨ' ,
            ( u'atkaróvɨ' , u'b^yizkaróvɨ' , u'ukaróvɨ' , ): u'karóvɨ' ,
            ( u'adbaradɨ́' , u'b^yizbaradɨ́' , u'ubaradɨ́' , ): u'baradɨ́' ,
            ( u'ats^yistrɨ́' , u'b^yiss^yistrɨ́' , u'us^yistrɨ́' , ): u's^yistrɨ́' ,
})

GoldSolution(name="Halle_127_Japanese", # unsure
             prefixes=[u'',u'',u'',u'',u''],
             suffixes=[u'ru',u'anai',u'itai',u'ta',u'yoo'],
             underlyingForms={
            ( u'neru' , u'nenai' , u'netai' , u'neta' , u'neyoo' , ): u'ne' ,
            ( u'miru' , u'minai' , u'mitai' , u'mita' , u'miyoo' , ): u'mi',
            ( u'šinu' , u'šinanai' , u'šinitai' , u'šinda' , u'šinoo' , ): u'šin' ,
            ( u'yomu' , u'yomanai' , u'yomitai' , u'yonda' , u'yomoo' , ): u'yom' ,
            ( u'yobu' , u'yobanai' , u'yobitai' , u'yonda' , u'yoboo' , ): u'yob' ,
            ( u'kat^su' , u'katanai' , u'kačitai' , u'katta' , u'katoo' , ): u'kat^s' ,
            ( u'kasu' , u'kasanai' , u'kašitai' , u'kašita' , u'kasoo' , ): u'kas' ,
            ( u'waku' , u'wakanai' , u'wakitai' , u'waita' , u'wakoo' , ): u'wak' ,
            ( u't^sugu' , u't^suganai' , u't^sugitai' , u't^suida' , u't^sugoo' , ): u't^sug' ,
            ( u'karu' , u'karanai' , u'karitai' , u'katta' , u'karoo' , ): u'kar' ,
            ( u'kau' , u'kawanai' , u'kaitai' , u'katta' , u'kaoo' , ): u'kaw'
})

GoldSolution(name="Halle_133_Swahili",
             prefixes=[u'u',u'',u'ma'],
             suffixes=[u'',u'',u''],
             underlyingForms={
                 # I think you are not allowed to start with an unaspirated stop
                 # and you have to prepend a nasal in that case
                 # deaspirate when not word initial
            ( u'ubale' , u'm̩bale' , None,  ): u'bale' ,
            ( u'udago' , u'n̩dago' , None,  ): u'dago' ,
            ( u'ugimbi' , u'ŋ̩gimbi' , None,  ): u'gimbi' ,
            ( u'uǰia' , u'ɲ̩ǰia' , None,  ): u'ǰia' ,
            ( u'upaǰa' , u'p^haǰa' , u'mapaǰa' , ): u'p^haǰa' ,
            ( u'upamba' , u'p^hamba' , None,  ): u'p^hamba' ,
            ( u'utunzo' , u't^hunzo' , u'matunzo' , ): u't^hunzo' ,
            ( u'utunda' , u't^hunda' , None,  ): u't^hunda' ,
            ( u'ukelele' , u'k^helele' , u'makelele' , ): u'k^helele' ,
            ( u'ukumbi' , u'k^humbi' , None,  ): u'k^humbi' ,
            ( u'učoma' , u'č^homa' , u'mačoma' , ): u'č^homa' ,
            ( u'učaŋgo' , u'č^haŋgo' , None,  ): u'č^haŋgo' ,
            ( u'ufuasi' , u'fuasi' , u'mafuasi' , ): u'fuasi' ,
            ( u'ufuko' , u'fuko' , None,  ): u'fuko' ,
            ( u'uvušo' , u'vušo' , u'mavušo' , ): u'vušo' ,
            ( u'uvumbi' , u'vumbi' , None,  ): u'vumbi' ,
            ( u'usiku' , u'siku' , u'masiku' , ): u'siku' ,
            ( u'usira' , u'sira' , None,  ): u'sira' ,
            ( u'ušono' , u'šono' , u'mašono' , ): u'šono' ,
            ( u'ušaŋga' , u'šaŋga' , None,  ): u'šaŋga' ,
                 # word initial {w,l,r} > [+stop] / #_
            ( u'uwiŋgu' , u'm̩biŋgu' , None,  ): u'biŋgu' ,
            ( u'uwili' , u'm̩bili' , None,  ): u'wili' ,
            ( u'ulimi' , u'n̩dimi' , None,  ): u'limi' ,
            ( u'urefu' , u'n̩defu' , None,  ): u'refu' ,
            ( u'umio' , u'mio' , None,  ): u'mio' ,
                 # u > w / _ V
            ( u'wimbo' , u'ɲimbo' , None,  ): u'imbo' ,
            ( u'wembe' , u'ɲembe' , None,  ): u'embe' ,
                 ( u'wakati' , u'ɲakati' , None,  ): u'akati',
                 # u > 0 / u_
            ( u'uši' , u'ɲuši' , None,  ): u'uši',
            ( u'šoka' , None,  u'mašoka' , ): u'šoka' ,
            ( u'tunda' , None,  u'matunda' , ): u'tunda' ,
            ( u'kaša' , None,  u'makaša' , ): u'kaša' ,
})

GoldSolution(name="Roca_104_Tunica",
             prefixes=[u'',u'',u'',u''],
             suffixes=[u'',u'ʔuhki',u'ʔɔki',u'hkʔaki'],
             underlyingForms={
            ( u'pó' , u'póʔuhki' , u'póʔɔki' , u'póhkʔaki' , ): u'pó' ,
            ( u'pí' , u'píʔuhki' , u'píʔɛki' , u'píhkʔaki' , ): u'pí' ,
            ( u'já' , u'jáʔuhki' , u'jáʔaki' , u'jáhkʔaki' , ): u'já' ,
            ( u'čú' , u'čúʔuhki' , u'čúʔɔki' , u'čúhkʔaki' , ): u'čú' ,
            ( u'hára' , u'hárʔuhki' , u'hárʔaki' , u'hárahkʔaki' , ): u'hára' ,
            ( u'hípu' , u'hípʔuhki' , u'hípʔɔki' , u'hípuhkʔaki' , ): u'hípu' ,
            ( u'náši' , u'nášʔuhki' , u'nášʔɛki' , u'nášihkʔaki' , ): u'náši' ,
})

GoldSolution(name="Roca_16_German",
             prefixes=[u'',u'',u'',u''],
             suffixes=[u'',u'ə',u'ən',u'ər'],
             underlyingForms={
            ( u'tak' , u'tagə' , None,  None,  ): u'tag' ,
            ( u'volk' , u'volkə' , None,  None,  ): u'volk' ,
            ( u'pəriskop' , u'pəriskopə' , None,  None,  ): u'pəriskop' ,
            ( u'hof' , u'höfə' , None,  None,  ): u'hof' ,
            ( u'wək' , u'wəgə' , None,  None,  ): u'wəg' ,
            ( u'ros' , u'rosə' , None,  None,  ): u'ros' ,
            ( u'raup' , None,  u'raubən' , None,  ): u'raub' ,
            ( u'ləit' , None,  u'ləidən' , None,  ): u'ləid' ,
            ( u'lop' , None,  u'lobən' , None,  ): u'lob' ,
            ( u'lant' , None,  u'landən' , None,  ): u'land' ,
            ( u'rat' , None,  u'ratən' , None,  ): u'rat' ,
            ( u'grəis' , u'grəizes' , None,  None,  ): u'grəiz' ,
            ( u'braf' , None,  None,  u'bravər' , ): u'brav' ,
})

GoldSolution(name="Roca_17_Dutch", 
             prefixes=[u''],
             suffixes=[{u'tə',u'də'}], # can be analyzed either way
             underlyingForms={
            ( u'klaptə' , ): u'klap' ,
            ( u'krabdə' , ): u'krab' ,
            ( u'rɛdə' , ): u'rɛd' ,
            ( u'vɩstə' , ): u'vɩs' ,
            ( u'razdə' , ): u'raz' ,
            ( u'zɛtə' , ): u'zɛt' ,
            ( u'maftə' , ): u'maf' ,
            ( u'klovdə' , ): u'klov' ,
            ( u'lɛɣdə' , ): u'lɛɣ' ,
            ( u'laxtə' , ): u'lax' ,
            ( u'rumdə' , ): u'rum' ,
            ( u'zundə' , ): u'zun' ,
            ( u'meŋdə' , ): u'meŋ' ,
            ( u'rurdə' , ): u'rur' ,
            ( u'rɔldə' , ): u'rɔl' ,
            ( u'ajdə' , ): u'aj' ,
            ( u'skidə' , ): u'ski' ,
})

GoldSolution(name="Roca_25_Zoque",
             prefixes=[u'',u'ŋ'],
             suffixes=[u'',u''],
             underlyingForms={
            ( u'pama' , u'mbama' , ): u'pama' ,
            ( u'tatah' , u'ndatah' , ): u'tatah' ,
            ( u'kwarto' , u'ŋgwarto' , ): u'kwarto' ,
            ( u'plato' , u'mblato' , ): u'plato' ,
            ( u'trama' , u'ndrama' , ): u'trama' ,
            ( u'disko' , u'ndisko' , ): u'disko' ,
            ( u'gaju' , u'ŋgaju' , ): u'gaju' ,
            ( u'čoʔngoja' , u'ɲǰoʔngoja' , ): {u'čoʔnkoja',u'čoʔngoja'} ,
            ( u'tsima' , u'ndzima' , ): u'tsima' ,
            ( u'sʌk' , u'sʌk' , ): u'sʌk' ,
            ( u'faha' , u'faha' , ): u'faha' ,
            ( u'šapun' , u'šapun' , ): u'šapun' ,
})

GoldSolution(name="Roca_35_Icelandic",
             prefixes=[u'',u'',u'',u'',u'',u''],
             suffixes=[u'r',u'',u'ri',u's',u'um',u'a'],
             underlyingForms={
                 # 0 > u / C_r#
            ( u'dagur' , u'dag' , None,  None,  None,  None,  ): u'dag' ,
            ( u'staður' , u'stað' , None,  None,  u'stöðum' , None,  ): u'stað' ,
            ( u'hestur' , u'hest' , None,  None,  None,  None,  ): u'hest' ,
            ( u'bær' , u'bæ' , None,  None,  None,  None,  ): u'bæ' ,
            ( u'læknir' , u'lækni' , None,  None,  None,  None,  ): u'lækni' ,
            ( u'lifur' , None,  u'lifri' , None,  None,  None,  ): u'lif' ,
            ( u'akur' , None,  u'agri' , None,  u'ökrum' , None,  ): u'ak' ,
            ( u'aldur' , None,  u'aldri' , None,  u'öldrum' , None,  ): u'ald' ,
            ( u'lüfur' , u'lüf' , None,  u'lüfs' , u'lüfjum' , u'lüfja' , ): u'lüfurj' ,
            ( u'bülur' , u'bül' , None,  u'büls' , u'büljum' , u'bülja' , ): u'bülj' ,
            ( u'söngur' , u'söng' , None,  u'söngs' , u'söngvum' , u'söngva' , ): u'söngv' ,
                 # uncertain onward
            ( u'barn' , None,  None,  None,  u'börnum' , None,  ): u'börn' ,
            ( u'baggi' , None,  None,  None,  u'böggull' , None,  ): u'bögg' ,
            ( u'jaki' , None,  None,  None,  u'jökull' , None,  ): u'jök' ,
            ( u'θagga' , None,  None,  None,  u'θögull' , None,  ): u'θög'  ,
            ( u'kalla' , None,  None,  None,  u'köllum' , None,  ): u'köll' 
})

GoldSolution(name="Roca_37_Anxiang",
             prefixes=[u'',u''],
             suffixes=[u'',u'iər'],
             underlyingForms={
            ( u'tie' , u'tietiər' , ): u'tiet' ,
            ( u'mian' , u'mianmiər' , ): u'mian' ,
            ( u'tai' , u'taitər' , ): u'tai' ,
            ( u'pau' , u'paupər' , ): u'pau' ,
            ( u'ke' , u'kekər' , ): u'ke' ,
            ( u'fa' , u'fafər' , ): u'fa' ,
            ( u'o' , u'oər' , ): u'o' ,
            ( u'ti' , u'titiər' , ): u'ti' ,
            ( u'tin' , u'tintiər' , ): u'tin' ,
            ( u'p^hu' , u'p^hup^hər' , ): u'p^hu' ,
            ( u'tx̯y' , u'tx̯ytx̯yər' , ): u'tx̯y'
})

GoldSolution(name="Roca_89_Lumasaaba",
             prefixes=[{u'iŋ',u'im',u'in',u'iɲ'},u'xa'],
             suffixes=[u'',u''],
             underlyingForms={
            ( u'iɲɉele' , u'xaçele' , ): u'çele' ,
            ( u'iŋga:fu' , u'xaxa:fu' , ): u'xa:fu' ,
            ( u'imbeβa' , u'xaβeβa' , ): u'βeβa' ,
            ( u'iŋgoxo' , u'xakoxo' , ): u'koxo' ,
            ( u'iŋgwe' , u'xakwe' , ): u'kwe' ,
            ( u'indali' , u'xatali' , ): u'tali' ,
            ( u'imboko' , u'xaβoko' , ): u'βoko' ,
})



GoldSolution(name="Halle_49_Ewe",
             # I think either direction works
             substitution={u'l': u'r'})
GoldSolution(name="Halle_51_Ganda",
             substitution={u'r': u'l'})
GoldSolution(name="Halle_53_Papago",
             substitution={u'ǰ': u'd', u'č': u't'})
GoldSolution(name="Halle_55_Proto_Bantu",
             substitution={u'b': u'β', u'd': u'l', u'g': u'ɣ'}) # UNSURE
GoldSolution(name="Halle_59_Mohawk",
             substitution={u'b': u'p', u'd': u't', u'g': u'k'})
GoldSolution(name="Odden_A1_Kikurai",
             substitution={u'b': u'β', u'd': u'r', u'g': u'ɣ'})
GoldSolution(name="Odden_A2_Modern_Greek",
             substitution={u'x^y': u'x', u'k^y': u'k'})
GoldSolution(name="Odden_A3_Farsi",
             substitution={u'ř': u'r̃'})
GoldSolution(name="Odden_A4_Osage",
             substitution={u'd': u'ð'})
GoldSolution(name="Odden_A5_Amharic", # we get this wrong??
             substitution={u'ɛ': u'ə'})
GoldSolution(name="Odden_A6_Gen",
             substitution={u'r': u'l'})
GoldSolution(name="Odden_A7_Kishambaa",
             substitution={u'm': u'm̥', u'n': u'n̥'}) # this wrong??
GoldSolution(name="Odden_A8_Thai",
             substitution={u'p': u'p̚', u'k': u'k̚', u't': u't̚'}) # this wrong??
GoldSolution(name="Odden_A9_Palauan",
             substitution={u'd': u'θ'})
GoldSolution(name="Odden_A10_Quechua_Cuzco_dialect",
             substitution={u'e': u'i', u'o': u'u', u'N': u'ŋ'})
GoldSolution(name="Odden_A11_Lhasa_Tibetan",
             substitution={u'b': u'p', u'd': u't', u'G': u'g', u'ḍ': u'ṭ', u'N': u'ŋ', u'q': u'k', u'g': u'k'})


if __name__ == "__main__":
    from problems import Problem
    from textbook_problems import *
    import argparse
    import pickle
    import sys
    print len(GoldSolution.solutions),"solutions."
    if len(sys.argv) < 2:
        print "here is what we have already graded:"
        already_graded = list(sorted(GoldSolution.solutions.keys()))
        for name in already_graded: print name
        print "here is what still needs to be graded:"
        for to_do in set(Problem.named.keys()) - set(already_graded):
            BAD = {"Roca_31_Verlan","Kevin"}
            if any( bd in to_do for bd in BAD ): continue
            if Problem.named[to_do].supervised: continue
            
            
            print to_do
        sys.exit(0)
        
    parser = argparse.ArgumentParser(description = "")
    parser.add_argument("path")
    arguments = parser.parse_args()

    if arguments.path == "verify":
        for name,solution in GoldSolution.solutions.iteritems():
            assert name in Problem.named
            problem = Problem.named[name]
            if problem.parameters is not None and problem.parameters.get("type",None) == "alternation":
                continue
            print "verifying",name
            def encoding(r):
                return tuple(None if m is None else Morph(m)
                             for m in r)
            discrepancy = list(\
                               set(encoding(r) for r in solution.underlyingForms.keys()) ^ \
                               set(encoding(r) for r in problem.data))
            assert len(discrepancy) == 0, "discrepancy: %s"%discrepancy
        sys.exit(0)

    with open(arguments.path,"rb") as handle:
        data = pickle.load(handle)

    
    def morphToUnicode(m):
        if m is None: return u"None"
        m = u"".join(m.phonemes)
        return u"u'%s'"%(m)
        return unicode((m,))[1:][:-2]

    if "alternation" in arguments.path:
        name = arguments.path[arguments.path.rindex('/')+1:]
        name = name[:name.rindex('.')]
        substitution = u", ".join( u"u'" + a + u"': u'" + b + "'"
                                   for a,b in data.substitution.iteritems())
        
        print "GoldSolution(name=\"%s\","%(name)
        print "             substitution={%s})"%(substitution)
        print data.rules
        sys.exit(0)
        

    prefixes = "[%s]"%(u",".join(morphToUnicode(prefix) for prefix in data.finalFrontier.prefixes ))
    suffixes = "[%s]"%(u",".join(morphToUnicode(suffix) for suffix in data.finalFrontier.suffixes ))

    print "GoldSolution(name=\"%s\","%(data.problem)
    print "             prefixes=%s,"%prefixes
    print "             suffixes=%s,"%suffixes
    print "             underlyingForms={"
    for surfaces in Problem.named[data.problem].data:
        print "            (",
        for s in surfaces:
            if s is None:
                print "None, ",
            else:
                print morphToUnicode(Morph(s)),",",
        print "):",
        surfaces = tuple(Morph(s) if s is not None else None
                         for s in surfaces )
        ur = data.finalFrontier.underlyingForms.get(surfaces,None)
        print morphToUnicode(ur),","
    print "})"

    print 
    for r in data.finalFrontier.MAP().rules:
        print r
    print 


    for surfaces in Problem.named[data.problem].data:
        for s in surfaces:
            if s is None:
                print "(n/a)\t",
            else:
                print s,"\t",
        print ""
        
