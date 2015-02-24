#author: James Teague II
#date: Spring 2015
#description: Person Module - Handles all functions to maintain Persons within the Simulation

from random import randrange, choice
from Strategy import Strategy
from operator import itemgetter
class Person(object):
	"""Class Person simulates a person.
    
    This class will represent a person we need specifically for
    our El Farol Bar/Minority Game problem. They will have a
    simulated memory and a simulated decision protocol.
    
    Attributes:
        name: A reference to name if ever needed.
        attend: A boolean value to determine whether the person will
            attend the bar this week or not.
        strategies: Dictionary of the key values of strategies
        has_random: A boolean, True if random strategy is assigned
        	else False
        random_dict: Dictionary to hold random strategy value and 
        	score for indivdual person object
    """
	no_inst = 0
	#Randomize attendance of all persons memory
	recent_memory = []
	for i in range(0, 15):
		recent_memory.append(randrange(0,4))

	def __init__(self, name):
		"""Initialize Person with a name for reference and dictionary for strategy keys"""
		super().__init__()
		# Increment the number of instances of people
		Person.no_inst += 1
		self.name = name
		self.strategies = {}
		# self.strategy1 = None
		# self.strategy2 = None
		# self.strategy3 = None
		# If user receives random strategy set to true
		self.has_random = False
		# Default random strategy in the event it is needed
		self.random_dict = {"value": 0, "score": 0}
		# Set default of attending to false
		self.attend = False

	def give_strategies(self):
		"""Give Person 6 distinct strategies at random"""
		while len(self.strategies) < 6:
			key = Strategy.get_new_key()
			if not key in self.strategies:
				self.strategies[key] = None
				if key == "random_attendance":
					self.has_random = True

		# #self.strategy1 = {"name": key, "value": Strategy.strategies[key]}
		# self.strategy1 = key
		# if key == "random_attendance":
		# 	self.has_random = True
		# while key == self.strategy1:
		# 	key = Strategy.get_new_key()
		# #self.strategy2 = {"name": key, "value": Strategy.strategies[key]}
		# self.strategy2 = key
		# if key == "random_attendance":
		# 	self.has_random = True
		# while key == self.strategy1 or key == self.strategy2:
		# 	key = Strategy.get_new_key()
		# #self.strategy3 = {"name": key, "value": Strategy.strategies[key]}
		# self.strategy3 = key
		# if key == "random_attendance":
		# 	self.has_random = True
	def eval_strategies(self):
		"""Finds strategy with highest score then calls function to employ the strategy"""
		strategy = []
		for key in self.strategies:
			# Append tuple, ex. ("min_attendance", 0)
			strategy.append((key, Strategy.strategies[key]["score"]))
		# strategy.append(Strategy.strategies[self.strategy1]["score"])
		# strategy.append(Strategy.strategies[self.strategy2]["score"])
		# strategy.append(Strategy.strategies[self.strategy3]["score"])
		#TODO complete evaluating scores
		# max_ndx = strategy.index(max(strategy))
		# Get the max score from strategy array by checking second spot in the tuple
		# but returning the key
		max_key = max(strategy,key=itemgetter(1))[0]
		# Get the best strategy the person has by looking up the key
		test_point = self.get_test_point(max_key)
		# Test purpose TBR
		self.strat_chose = max_key
		# make the decision based on the value of the strategy
		self.make_decision(test_point["value"])

	def went_to_bar(self):
		"""Return if user went to the bar"""
		return self.attend

	def get_name(self):
		"""Return a reference to the Person object"""
		return self.name

	def get_test_point(self,key):
		"""Look up Strategy in the dictionary and return contents"""
		return Strategy.strategies.get(key, 0)

	def make_decision(self, attendance):
		"""Makes decision on whether to go or stay depending on the attendance"""
		# If attendance is random search own random value
		if attendance == "random":
			if int(self.random_dict["value"]) < 2:
				self.attend = True
			else:
				self.attend = False
		# If over 59 stay home
		elif attendance >= 2:
			self.attend = False
		#else go to the bar
		else:
			self.attend = True

	def eval_random_strategy(self, attendance):
		"""Evaluate indivdual random strategy
			Checks own random dictionary and determines whether the strategy advised wrong
			or right for the current week
		"""
		if self.has_random:
			if self.random_dict["value"] < 2 and attendance < 2:
				self.random_dict["score"] += 1
			elif self.random_dict["value"] >= 2 and attendance >= 2:
				self.random_dict["score"] += 1
			else:
				pass
				# self.random_dict["score"] -= 1

	def get_random_attendance(self):
		"""Chose some random weeks attendance and store it in the random dictionary"""
		if self.has_random:
			self.random_dict["value"] = choice(Person.recent_memory)

	@classmethod
	def get_no_of_instances(cls):
		"Get number of instances of the given class"
		return cls.no_inst

	@classmethod
	def add_to_memory(cls,attendance):
		"""Add the attendance to the memory of the Person, and remove the oldest value"""
		cls.recent_memory.pop(0)
		cls.recent_memory.append(attendance)

#=================== Person Test Code =============================