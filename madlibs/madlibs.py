from sample_mablibs import hp, code, zombie, hungergames
import random
#this imports diffrent madlibs and then takes a random choce and plays with it
if __name__ == "__main__":
    m = random.choice([hp, code, zombie, hungergames])
    m.madlib()