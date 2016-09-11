import random
from sys import argv

# MAIN MENU
def mainmenu():
    choice = True
    while choice:
        print("Welcome to Stench Mob Python App!\nPress the number for the following:\n\t1. Name Generator\n\t2. Team Generator\n\t3. Death Calculator\n\t99. Exit")
        choice = raw_input("Choice: ")
        if choice == "1":
            namegen()
        elif choice == "2":
            heropicker()
        elif choice == "3":
            deathcalc()
        elif choice == "99":
            print("fuck off then")

# NAME GENERATOR FUNCTION
def namegen():
    firstName = ["Porter", "Frosty", "Albert", "Rufus", "Julio", "Squank", 
                "Jorge", "Jeffy", "Olly", "Swamy", "Reed", "Dillern", "Wagner", "Keith", 
                "Doddy", "Terry", "Carlos", "Chuck", "Chichi", "Chachi", "Penelope", 
                "Xander", "Edwin", "Eduardo", "Alfonso", "Winston", "Toby", "Alfred", 
                "Bruce", "Morty", "Denton", "Charlie", "Wong", "Wang", "Vaughn", "Davion", 
                "Warren", "Laqueefa", "Lauren", "Leonard", "Jackson", "Franz", "Dingus", 
                "Martin", "Dipso", "Chandler", "Pizzle", "Darrel", "Cragg", "Johnny", 
                "Peter", "Davey", "Lonny", "Flavtarian", "Jamal", "Shaqueefa", "Morris", 
                "Mark", "Borf", "Mork", "Micky", "Carl", "Jord", "Frank", "Camtron", 
                "Carlton", "Al", "Stentin", "Rob", "Donatello", "Ricky", "Polly", "Raphael"]

    lastNameOne = ["Wolf", "Frosty", "Spit", "Speed", "Ooze",
                    "Licker", "Frump", "Spinkle", "Mingle", "Bork", "Dendo", "Hurf", "Stank", 
                    "Stinky", "Dirty", "Pork", "Freizen", "Spank", "Dick", "Dong", "Spork", 
                    "Sludge", "Slime", "Booger", "Niggy", "Clam", "Piss", "Shit", "Fart", 
                    "Dumpster", "Dumpster", "Mink", "Blob", "Winkle", "Piss", "Pork", "Hollow", 
                    "Smelly", "Grundle", "Broken"]


    lastNameTwo = ["howell", "funnel",  "bucket", 
                    "knuckles","toes", "pecker", "butt", "nickers", "burger", "pants", 
                    "dripper", "coon", "logg", "bottom", "feetz", "wagon", "flicker",
                    "chucker", "warden", "narf", "boy", "cheese", "snizzle", "stick", "stein", 
                    "wintz", "stern", "rash", "schmidt", "fideous", "funker", "dong", 
                    "wang", "wad", "piss", "stench", "odor", "cockles", "tooth"]

    firstName = random.choice(firstName)
    lastNameOne = random.choice(lastNameOne)
    lastNameTwo = random.choice(lastNameTwo)

    fullName = "%s %s%s" % (firstName, lastNameOne, lastNameTwo)
    print("%s, Welcome to Stench Mob! ...You lucky mother fucker\n" % (fullName))

# RANDOM TEAM GEN FUNCTION
def heropicker():
    heroes = ['Abaddon', 'Alchemist', 'Ancient Apparition', 'Anti-Mage', 'Arc Warden', 'Axe','Bane', 'Batrider','Beastmaster','Bloodseeker','Bounty Hunter',
              'Brewmaster','Bristleback','Broodmother','Centaur Warrunner ','Chaos Knight','Chen','Clinkz','Clockwerk','Crystal Maiden','Dark Seer','Dazzle',
              'Death Prophet','Disruptor','Doom','Dragon Knight','Drow Ranger','Earth Spirit','Earthshaker','Elder Titan','Ember Spirit','Enchantress','Enigma',
              'Faceless Void','Gyrocopter','Huskar','Invoker','Io','Jakiro','Juggernaut','Keeper of the Light','Kunkka','Legion Commander','Leshrac','Lich',
              'Lifestealer','Lina','Lion','Lone Druid','Luna','Lycan','Magnus','Medusa','Meepo','Mirana','Morphling','Naga Siren','Nature\'s Prophet','Necrophos',
              'Night Stalker','Nyx Assassin','Ogre Magi','Omniknight','Oracle','Outworld Devourer','Phantom Assassin','Phantom Lancer','Phoenix','Puck','Pudge',
              'Pugna','Queen of Pain','Razor','Riki','Rubick','Sand King','Shadow Demon','Shadow Fiend','Shadow Shaman','Silencer','Skywrath Mage','Slardar','Slark',
              'Sniper','Spectre','Spirit Breaker','Storm Spirit','Sven','Techies','Templar Assassin','Terrorblade','Tidehunter','Timbersaw','Tinker','Tiny','Treant Protector',
              'Troll Warlord','Tusk','Underlord','Undying','Ursa','Vengeful Spirit','Venomancer','Viper','Visage','Warlock','Weaver','Windranger','Winter Wyvern',
              'Witch Doctor','Wraith King','Zeus']
    
    players = ['Bogdan', 'Ben', 'Allen', 'Dylan', 'Chris', 'Zack']
    random.shuffle(players)
    player_hero_dict = {}
    for player in players[0:5]:
        hero = random.choice(heroes)
        found = False
        while not found:
            if hero not in player_hero_dict.values():
                player_hero_dict[player] = hero
                found = True
    for k,v in player_hero_dict.iteritems():
        print '%s -> %s' % (k,v)
# DEATH CALCULATOR FUNCTION
def deathcalc():
    minutes = 0 
    seconds = 0
    timealive = 0
    
    mdead = 0 
    sdead = 0
    timedead = 0
    
    games = "y"
    
    
    while games == "y":
        minutes += int(raw_input("Enter minutes of length of the game: "))
        seconds += int(raw_input("Enter seconds of the game: "))
        
        mdead += int(raw_input("Enter minutes spent dead: "))
        sdead += int(raw_input("Enter seconds spent dead: "))
         
        games = raw_input("Any more games? y/n: ")  
    
    timealive = float((minutes * 60) + (seconds))
    timedead = float((mdead * 60) + (sdead))
    
    print("Total game length: %d:%d" % (minutes, seconds))
    print("You were dead for: %d:%d" % (mdead, sdead))
    # print("That's %d percent of playing time in the graveyard" % (percent))
    print('You spent {:.1%}'.format(timedead/timealive) + ' of time played dead.\n')
    
mainmenu()
