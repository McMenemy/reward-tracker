import random
import csv

# Reward list class
class Rewards:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.rewards = self.create_array()

    def create_array(self):
        rewards = []
        with open(self.csv_file, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                rewards.append(row)
        return rewards

    def get_random_reward(self):
        index = random.randint(0, len(self.rewards) - 1)
        return self.rewards[index][0]

    def add_reward(self, reward, times):
        rewards = [reward] * int(times)
        with open(self.csv_file, 'a', newline='') as f:
            writer = csv.writer(f)
            for reward in rewards:
                writer.writerow([reward])
        self.rewards = self.create_array()

    def get_info(self):
        print(name + ' has ' + len(self.rewards) + ' rewards remaining.')
        print('your current streak is ' + self.streak)


# make csv models
daily_rewards = Rewards('daily_rewards.csv')
weekly_rewards = Rewards('weekly_rewards.csv')
ninety_days_rewards = Rewards('ninety_days_rewards.csv')
daily_short_tasks = Rewards('daily_short_tasks.csv')

# interface helper functions
def menu_options():
    print('select an option then press enter')
    print('1 - get a daily reward')
    print('2 - get a weekly reward')
    print('3 - get a 90 day reward')
    print('4 - reset streak')
    print('5 - add a daily reward')
    print('6 - add a weekly reward')
    print('7 - add a 90 day reward')
    print('8 - get a daily short task')
    print('9 - add a daily short task')
    print('q - to quit')

def reset_streak():
    with open('streak.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([0])

def get_streak():
    with open('streak.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            return row[0]

def increase_streak():
    current_streak = 0
    with open('streak.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            current_streak = row[0]

    with open('streak.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([int(current_streak) + 1])

def get_model(type):
    if type == 'daily':
        return daily_rewards
    elif type == 'weekly':
        return weekly_rewards
    elif type == 'ninety':
        return ninety_days_rewards
    elif type == 'short':
        return daily_short_tasks

def menu_get_reward(type):
    model = get_model(type)

    print('Congrats, you chose to get a ' + type + ' reward!')
    print('Your reward is: ')
    print('\n' + model.get_random_reward() + '\n')
    print('Enjoy =)')
    increase_streak()
    print('Your current streak is ' + get_streak())
    print('press "q" quit or "m" for more options')

def menu_add_reward(type):
    model = get_model(type)

    print('You chose to add a ' + type + ' reward')
    print('Please type the text of the new ' + type  + ' reward')
    new_reward = input()
    print('How many times should this reward be in your reward bucket?')
    amount_of_times = input()
    model.add_reward(new_reward, amount_of_times)
    print(type.title() + ' reward added')
    print('Back to main menu...')
    menu_options()

# loop for user interaction (main program)

print('\nYour current streak is ' + get_streak())
menu_options()

while True:
    value = input()
    if value == '1': # get a daily reward
        menu_get_reward('daily')
    elif value == '2': # get a weekly reward
        menu_get_daily_reward('weekly')
    elif value == '3': # get a ninety days reward
        menu_get_daily_reward('ninety')
    elif value == '4': # reset streak
        print('You chose to reset streak')
        print('Your streak has been reset')
        reset_streak()
    elif value == '5': # add a daily reward
        menu_add_reward('daily')
    elif value == '6': # add a weekly reward
        menu_add_reward('weekly')
    elif value == '7': # add a ninety days reward
        menu_add_reward('ninety')
    elif value == '8': # get a daily short task
        menu_get_reward('short')
    elif value == '9': # add a daily short task
        menu_add_reward('short')
    elif value == 'q': # quit
        print('Goodbye')
        break
    elif value == 'm': # menu options
        menu_options()
    else:
        print('you chose an invalid option. here are your choices: ')
        menu_options

# daily shorts
# .5 (6) find a new meal to cook or cook a good meal for next days lunch
# 1 (12) yoga / stretch
# 1 (12) walk while listening to music
# .5 (6) tweak exercise doc
# .5 (6) contact friend/family
# .25 (3) journal about life goals
# .5 (3) outline your ideal self
# .25 (3) think about bigger picture
# 2 (24) work on html canvas site
# .25 (3) practice farming league
# .25 (3) find networking events

# daily longs
# 4 (48) league of legends
# 1 (12) watch tv series
# 1 (12) read a fantasy novel
# 1 (12) play a single player game

# weekly longs
# 3 (36) league of legends
# 1 (12) watch a movie
# 2 (24) go explore somewhere in city
# 1 (12) play a new game

# 90 days
# (1) witch 3 trip
# divinity trip w/ felicia

# ones to look into
# shoot basketball
