#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Adding from datatabse setup file
from models import Base, User, Category, CategoryItem

engine = create_engine('sqlite:///vehicle_items.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance

# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
user1 = User(name="HelloToyota", email="toyotamaker@udacity.com",
             picture='https://3.bp.blogspot.com/--gnr6ip6RgA/UNnv8zgXFKI/AAAAAAAAHMw/HX90y9wpkaw/s1600/Toyota+Logo+2.jpg')  # noqa
session.add(user1)
session.commit()


# Adding items for toyota vehicle type
category1 = Category(name="cars", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(
    name="Yaris", user_id=1, description="The Toyota Yaris or Yarisu is a"
    "subcompact car produced by Toyota since 1999, replacing the Starlet."
    "Between 1999 and 2005, some markets received the same vehicles"
    "under the Toyota Echo name.  Toyota has used the Yaris and Echo names"
    "on the export version of several different Japanese-market models."
    "The name Yaris is derived from Charis, the singular form of Charites, the"
    "Greek goddesses of charm and beauty.", category=category1)

session.add(item1)
session.commit()


item2 = CategoryItem(
    name="Corolla", user_id=1, description="The Toyota Corolla is a line of"
    "subcompact and compact cars manufactured by Toyota. Introduced in 1966,"
    "the Corolla was the best-selling car worldwide by 1974 and has been one"
    "of the best-selling cars in the world since then.", category=category1)

session.add(item2)
session.commit()

item3 = CategoryItem(
    name="Camry", user_id=1, description="The Toyota Camry or the Kamuri is"
    "an automobile sold internationally by the Japanese manufacturer Toyota"
    "since 1982, spanning multiple generations.  Originally it was compact in"
    "size, later the Camry models have grown to fit the mid size and"
    "classification wide body.", category=category1)

session.add(item3)
session.commit

item4 = CategoryItem(
    name="Avalon", user_id=1, description="The Toyota Avalon is a full-size"
    "car produced by Toyota in the United States, and is the flagship sedan"
    "of Toyota in the United States, Canada, Puerto Rico, and the Middle East."
    "It was also produced in Australia from 2000 until July 2005, when it was"
    "replaced in November 2006 by the Toyota Aurion. The first production"
    "Avalon rolled off the TMMK assembly line in Georgetown, Kentucky, in"
    "September 1994.", category=category1)

session.add(item4)
session.commit

item5 = CategoryItem(
    name="Eightysix", user_id=1, description="The Toyota eighty six was"
    "introduced in the 2017 modek year with some new features.  It also"
    "got a new name from Scion FRS until Toyota dropped the the youth"
    "oriented brand and moved the lineup under the Toyota umbrella",
    category=category1)

session.add(item5)
session.commit


# Adding items for trucks
category2 = Category(name="trucks", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(
    name="Tacoma", user_id=1, description="The Toyota Tacoma is a pickup"
    "truck manufactured in the U.S. by the Japanese automobile manufacturer"
    "Toyota since 1995. The first generation Tacoma, model years 1995"
    "through 2004, was classified as a compact pickup. The second generation"
    "was classified as mid-size. The Tacoma was Motor Trend Magazine's Truck"
    "of the Year for 2005.", category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(
    name="Tundra", user_id=1, description="The Toyota Tundra is a pickup"
    "truck manufactured in the United States by the Japanese manufacturer"
    "Toyota since May 1999. The Tundra was the first North American full-size"
    "pickup to be built by a Japanese manufacturer.", category=category2)

session.add(item2)
session.commit()


# Items for crossover and suvs
category3 = Category(name="suvs", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(
    name="Chr", user_id=1, description="The Toyota C-HR is a subcompact"
    "crossover SUV produced by Toyota. The production of the C-HR started"
    "in November 2016, and was launched in Japan on 14 December 2016, and"
    "in Europe, Asia, Australia and North America in early 2017.",
    category=category3)

session.add(item1)
session.commit()

item2 = CategoryItem(
    name="Rav4", user_id=1, description="The Toyota RAV4 is a compact"
    "crossover SUV-sport utility vehicle; produced by the Japanese automobile"
    "manufacturer Toyota. This was the first compact crossover SUV. It made"
    "its debut in Japan and Europe in 1994, and in North America in 1995.",
    category=category3)

session.add(item2)
session.commit()

item3 = CategoryItem(
    name="Highlander", user_id=1, description="The Toyota Highlander, also"
    "known as the Toyota Kluger, is a midsize crossover SUV produced by"
    "Toyota. It is built on the same platform as used on the Toyota Camry."
    "Announced in April 2000 at the New York Auto Show and arriving in late"
    "2000 in Japan and January 2001 in North America.",
    category=category3)

session.add(item3)
session.commit()

item4 = CategoryItem(
    name="4runner", user_id=1, description="The Toyota 4Runner is a compact,"
    "later mid-size sport utility vehicle produced by the Japanese"
    "manufacturer Toyota and sold throughout the world from 1984 to present.",
    category=category3)

session.add(item4)
session.commit()

item5 = CategoryItem(
    name="Sequoia", user_id=1, description="The Toyota Sequoia is a"
    "full-size SUV manufactured by Toyota and derived from its Tundra"
    "pickup truck.  Introduced in 2000 and manufactured at Toyota Motor"
    "Manufacturing Indiana in Princeton, Indiana, the Sequoia is the first"
    "vehicle from a Japanese marque in the popular mainstream full-sized SUV"
    "class in North America.", category=category3)

session.add(item5)
session.commit()

item6 = CategoryItem(
    name="Land cruiser", user_id=1, description="The Toyota Land Cruiser"
    "is a series of four - wheel drive vehicles produced by the Japanese"
    "car maker Toyota. It is Toyota's longest running series."
    "Production of the first generation Land Cruiser began in 1951"
    "as Toyota's version of a Jeep like vehicle.",
    category=category3)

session.add(item6)
session.commit()


# Items for hybrids or hydrogens cars (Mirai)
category4 = Category(name="hybrids", user_id=1)

session.add(category4)
session.commit()

item1 = CategoryItem(
    name="Camry hybrid", user_id=1, description="Toyota Camry Hybrid features"
    "a 2.5-liter four-cylinder engine paired with an electric motor."
    "Combined output comes to 200 horsepower and it's routed to the front"
    "wheels through a specialized continuously variable transmission (CVT)"
    "The EPA estimates combined fuel economy at an excellent 40 or 41 mpg,"
    "depending on the trim level.", category=category4)

session.add(item1)
session.commit()

item2 = CategoryItem(
    name="Avalon hybrid", user_id=1, description="The current Toyota Avalon"
    "Hybrid comes in XLE Premium, XLE Touring and Limited trim levels. All"
    "are powered by a 156-horsepower 2.5-liter four-cylinder that joins"
    "forces with an electric motor to bring total output up to 200 hp."
    "A continuously variable transmission (CVT) routes power to the front"
    "wheels. This results in an impressive EPA-estimated 40 mpg combined"
    "rating.", category=category4)

session.add(item3)
session.commit()

item3 = CategoryItem(
    name="Rav4 hybrid", user_id=1, description="The Rav4 is a compact,"
    "sporty RAV4 Hybrid crossover brings style and efficiency to all your"
    "adventures with its chiseled features and spirited 194 net horsepower."
    "It has great power and accelaration, and its hybrid EPA-esimated 34 mpg"
    "city, your wallet will save lots of money.", category=category4)

session.add(item3)
session.commit()

item4 = CategoryItem(
    name="Highlander hybrid", user_id=1, description="The Highlander Hybrid"
    "SUV gets an EPA rating of 27 mpg city and 28 mpg highway, yet maintains"
    "a performance output of 280 hybrid system net power.",
    category=category4)

session.add(item4)
session.commit()

item5 = CategoryItem(
    name="Prius", user_id=1, description="Prius helps you maximize your"
    "efficiency. With more battery capacity and a more powerful electric"
    "motor, you won't have to worry about going out of range. Choose between"
    "full electric and hybrid power and go ever farther because you will"
    "get an EPA-estimated 58 mpg city.", category=category4)

session.add(item6)
session.commit()

item6 = CategoryItem(
    name="Mirai", user_id=1, description="The Toyota Mirai which means"
    "Japanese for future is a hydrogen fuel cell vehicle, one of the first"
    "such vehicles to be sold commercially.  The Mirai was unveiled at the"
    "November 2014 Los Angeles Auto Show. The Mirai has more range than"
    "any plug-in electric vehicle.", category=category4)

session.add(item6)
session.commit()


categories = session.query(Category).all()
for category in categories:
    print "Category:  " + category.name

print "Added toyota items!"
