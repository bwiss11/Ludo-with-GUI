# Description: Ludo game with GUI for 4 players with 2 tokens and moving algorithm (no user interaction besides rolling dice).
# Date: 8/14/22
from tkinter import *
import tkinter.messagebox
import random
from PIL import Image, ImageTk

root = Tk()  # creates window for interface - first line of code
root.title('Ludo')
root.geometry('750x750') # sets size of window

# Creates image and places it on canvas
img = Image.open("Ludo Background.png")
resized_image = img.resize((600, 600), Image.Resampling.LANCZOS)
new_image = ImageTk.PhotoImage(resized_image)
canvas_1 = Canvas(root, width = 700, height = 700, bg='gray0') # Creates the canvas


canvas_1.pack(fill = 'both', expand = True)
canvas_1.create_image(75, 75, image = new_image, anchor = 'nw')




#spaces = {'H':[100, 100, 100, 100],
          # '1':[140, 325.5, 161.5, 347], '2':[177, 325.5, 198.5, 347], '3':[215, 325.5, 236.5, 347], '4':[252, 325.5, 273.5, 347], '5': [289, 325.5, 310.5, 347],
          # '6':[326, 289, 347.5, 310.5], '7': [326, 251, 347.5, 272.5], '8': [326, 214, 347.5, 235.5], '9': [326, 177, 347.5, 198.5], '10': [326, 139, 347.5, 160.5], '11':[326, 102, 347.5, 123.5], '12':[363, 102, 384.5, 123.5],
          #  '13':[400, 102, 421.5, 123.5], '14':[400, 139, 421.5, 160.5], '15':[400, 177, 421.5, 198.5], '16':[400, 214, 421.5, 235.5], '17':[400, 251, 421.5, 272.5], '18':[400, 289, 421.5, 310.5],
          # '19':[437, 325.5, 458.5, 347.5], '20':[474, 325.5, 495.5, 347.5], '21':[511, 325.5, 532.5, 347.5], '22':[549, 325.5, 570.5, 347.5], '23':[586, 325.5, 607.5, 347.5], '24':[623, 325.5, 644.5, 347.5], '25':[623, 362.5, 644.5, 384],
          # '26':[623, 399.5, 644.5, 421], '27':[586, 399.5, 607.5, 421], '28':[549, 399.5, 570.5, 421], '29':[511, 399.5, 532.5, 421], '30':[474, 399.5, 495.5, 421], '31':[437, 399.5, 458.5, 421],
          # '32':[400, 436.5, 421.5, 458], '33':[400, 473.5, 421.5, 495], '34':[400, 511.5, 421.5, 533], '35':[400, 548.5, 421.5, 570], '36':[400, 585.5, 421.5, 607], '37':[400, 623, 421.5, 644.5], '38':[363, 623, 384.5, 644.5],
          # '39':[326, 623, 347.5, 644.5], '40':[326, 585.5, 347.5, 607], '41':[326, 548.5, 347.5, 570], '42':[326, 511.5, 347.5, 533], '43':[326, 473.5, 347.5, 495], '44':[326, 436.5, 347.5, 458],
          # '45':[289, 399.5, 310.5, 421], '46':[252, 399.5, 273.5, 421], '47':[215, 399.5, 236.5, 421], '48': [177, 399.5, 198.5, 421], '49':[140, 399.5, 161.5, 421], '50':[103, 399.5, 124.5, 421], '51':[103, 362.5, 124.5, 384],
          # '52':[103, 325.5, 124.5, 347]
          # }

spaces = {
    '1': [140, 325.5, 161.5, 347], '2': [177, 325.5, 198.5, 347], '3': [215, 325.5, 236.5, 347],
    '4': [252, 325.5, 273.5, 347], '5': [289, 325.5, 310.5, 347],
    '6': [326, 289, 347.5, 310.5], '7': [326, 251, 347.5, 272.5], '8': [326, 214, 347.5, 235.5],
    '9': [326, 177, 347.5, 198.5], '10': [326, 139, 347.5, 160.5], '11': [326, 102, 347.5, 123.5],
    '12': [363, 102, 384.5, 123.5],
    '13': [400, 102, 421.5, 123.5], '14': [400, 139, 421.5, 160.5], '15': [400, 177, 421.5, 198.5],
    '16': [400, 214, 421.5, 235.5], '17': [400, 251, 421.5, 272.5], '18': [400, 289, 421.5, 310.5],
    '19': [437, 325.5, 458.5, 347.5], '20': [474, 325.5, 495.5, 347.5], '21': [511, 325.5, 532.5, 347.5],
    '22': [549, 325.5, 570.5, 347.5], '23': [586, 325.5, 607.5, 347.5], '24': [623, 325.5, 644.5, 347.5],
    '25': [623, 362.5, 644.5, 384],
    '26': [623, 399.5, 644.5, 421], '27': [586, 399.5, 607.5, 421], '28': [549, 399.5, 570.5, 421],
    '29': [511, 399.5, 532.5, 421], '30': [474, 399.5, 495.5, 421], '31': [437, 399.5, 458.5, 421],
    '32': [400, 436.5, 421.5, 458], '33': [400, 473.5, 421.5, 495], '34': [400, 511.5, 421.5, 533],
    '35': [400, 548.5, 421.5, 570], '36': [400, 585.5, 421.5, 607], '37': [400, 623, 421.5, 644.5],
    '38': [363, 623, 384.5, 644.5],
    '39': [326, 623, 347.5, 644.5], '40': [326, 585.5, 347.5, 607], '41': [326, 548.5, 347.5, 570],
    '42': [326, 511.5, 347.5, 533], '43': [326, 473.5, 347.5, 495], '44': [326, 436.5, 347.5, 458],
    '45': [289, 399.5, 310.5, 421], '46': [252, 399.5, 273.5, 421], '47': [215, 399.5, 236.5, 421],
    '48': [177, 399.5, 198.5, 421], '49': [140, 399.5, 161.5, 421], '50': [103, 399.5, 124.5, 421],
    '51': [103, 362.5, 124.5, 384],
    '52': [103, 325.5, 124.5, 347],
    'A1': [140, 325.5, 161.5, 347], 'A2': [140, 362.5, 161.5, 384], 'A3': [177, 362.5, 198.5, 384],
    'A4': [215, 362.5, 236.5, 384], 'A5': [252, 362.5, 273.5, 384], 'A6': [289, 362.5, 310.5, 384],
    'A7': [326, 362.5, 347.5, 384],
    'B1': [400, 139, 421.5, 160.5], 'B2': [363, 139, 384.5, 160.5], 'B3': [363, 177, 384.5, 198.5],
    'B4': [363, 214, 384.5, 235.5], 'B5': [363, 251, 384.5, 272.5], 'B6': [363, 289, 384.5, 310.5],
    'B7': [363, 325.5, 384.5, 347],
    'C1': [586, 399.5, 607.5, 421], 'C2': [586, 362.5, 607.5, 384], 'C3': [549, 362.5, 570.5, 384],
    'C4': [511, 362.5, 532.5, 384], 'C5': [474, 362.5, 495.5, 384], 'C6': [437, 362.5, 458.5, 384],
    'C7': [400, 362.5, 421.5, 384],
    'D1': [326, 585.5, 347.5, 607], 'D2': [363, 585.5, 384.5, 607], 'D3': [363, 548.5, 384.5, 570],
    'D4': [363, 511.5, 384.5, 533], 'D5': [363, 473.5, 384.5, 495], 'D6': [363, 436.5, 384.5, 458],
    'D7': [363, 399.5, 384.5, 421],
}

class Player:
    '''Class that creates a player based on its position ('A', 'B', etc.) and defines several methods for getting information about the player and its tokens'''

    def __init__(self, player_position):
        '''Constructor for the Player class which takes a player position and initializes several characteristics for that player (start/end space, player position, etc.)'''
        start_position_dictionary = {'A': 1, 'B': 14, 'C': 27, 'D': 40}
        end_position_dictionary = {'A': 50, 'B': 8, 'C': 36, 'D': 22}
        self._start_space = start_position_dictionary[player_position]
        self._end_space = end_position_dictionary[player_position]
        self._token_info = {'p':{'position':'H','step count':0},'q':{'position':'H','step count':0}, 'r':{'position':'H','step count':0}, 's':{'position':'H','step count':0}}
        self._player_position = player_position
        self._completed = False
        self._step_count = 0


    def get_start_space(self):
        '''Returns the player's start space, used throughout to get player's current space'''
        return self._start_space

    def get_end_space(self):
        '''Returns the player's end space, used throughout to check if the player has entered their home squares'''
        return self._end_space

    def get_token_dict(self):
        '''Returns the dictionary containing each token's position and step count'''
        return self._token_info

    # def get_completed(self):
    #     '''Returns whether the player has completed the game'''
    #     return self._completed

    def get_token_step_count(self, token):
        '''Returns the number of steps a passed in token has taken, variation of the above two methods which is more flexible'''
        return self.get_token_dict()[token]['step count']

    def get_token_position(self, token):
        '''Returns the position on the board of a passed in token'''
        return self.get_token_dict()[token]['position']

    def set_token_position(self, token, position):
        '''Sets a passed in token's position to a passed in position'''
        self.get_token_dict()[token]['position'] = position

    def get_space_name(self, total_steps):
        '''Returns the player's corresponding space given a passed in number of steps'''
        special_step_counts = {0: 'H', 1: self._start_space, 51: '1', 52: '2', 53: '3', 54: '4', 55: '5', 56: '6', 57: 'E'}
        if total_steps < 1: #space name for home or ready to go positions
            return special_step_counts[total_steps]
        elif total_steps == 59: #space name for reaching end square
            return self.get_player_position() + '7'
        elif total_steps > 52: #space name for getting into home squares
            return self.get_player_position() + str(total_steps - 52)
        elif total_steps + self.get_start_space() - 1 > 52: #space name for going above board space 52 (restarts at 1)
            return str(total_steps + self.get_start_space() - 52)
        else: #space name for spaces between the player's start space and space 52
            return str(total_steps + self.get_start_space() - 1)

    def get_space_name_int(self, total_steps):
        '''Returns the player's corresponding space given a passed in number of steps'''
        special_step_counts = {0: 'H', 1: self._start_space, 53: '1', 54: '2', 55: '3', 56: '4', 57: '5', 58: '6', 59: 'E'}
        if total_steps < 1: #space name for home or ready to go positions
            return special_step_counts[total_steps]
        elif total_steps == 59: #space name for reaching end square
            return self.get_player_position() + '7'
        elif total_steps > 52: #space name for getting into home squares
            return self.get_player_position() + str(total_steps - 52)
        elif total_steps + self.get_start_space() - 1 > 52: #space name for going above board space 52 (restarts at 1)
            return total_steps + self.get_start_space() - 53
        else: #space name for spaces between the player's start space and space 56
            return total_steps + self.get_start_space() - 1

    def get_player_position(self):
        '''Returns the player's position, e.g. "A", "B", etc.'''
        return self._player_position

    def get_token_info(self, token, interest):
        '''Returns either the position or number of steps by a given token'''
        return self._token_info[token][interest]

    def set_completed(self):
        '''Used to set the completed data member to True after both tokens are in the end space'''
        self._completed = True

    def bounced_back(self, token):
        '''Resets a token's data after it's been landed on by an opponent'''
        self.get_token_dict()[token]['position'] = 'H'
        self.get_token_dict()[token]['step count'] = 0

    def update_position_and_steps(self, token_name, steps):
        '''Updates the step count and position of the given token'''
        previous_spot = self.get_token_dict()[token_name]['step count']
        print(previous_spot, 'previous spot')
        if previous_spot == 59:
            pass
        else:
            if previous_spot == 0:
                self.get_token_dict()[token_name]['step count'] = 1
                self.get_token_dict()[token_name]['position'] = self.get_start_space()
            else:
                self.get_token_dict()[token_name]['step count'] += steps
                step_count = self.get_token_dict()[token_name]['step count']

                if step_count > 59: # handles the step count when it goes over 57
                    step_count = 59 - (steps - (59 - (previous_spot)))
                    self.get_token_dict()[token_name]['step count'] = step_count

                current_space = self.get_space_name_int(step_count)
                self.get_token_dict()[token_name]['position'] = current_space # updates the token's position to the current space via the get_space_name() method

    def add_token(self, token_object):
        self._token = token_object

    def get_token(self):
        return self._token











class Recorder:
    def __init__(self, player_list):
        self._rolls = ['n']
        self._last_oval = 'None'
        self._players = []
        self._stacked_tracker = {}
        for player in player_list:
            self._players.append(Player(player))
            self._stacked_tracker[player] = {}
            self._stacked_tracker[player]['p'] = [False, None]
            self._stacked_tracker[player]['q'] = [False, None]
            self._stacked_tracker[player]['r'] = [False, None]
            self._stacked_tracker[player]['s'] = [False, None]
        self._current_outline = None
        self._winner = None
        self._current_click = []
        self._loop_status = False
        self._current_possible_moves = []
        self._player_turn = None
        self._cyan_squares_list = []
        self._blocked_spaces = {}
        self._starting_token_dict = {'A': {'p': [167.5 ,167.5, 189, 189, 'navy', 'white'], 'q': [223.5,167.5, 245, 189, 'navy', 'white'], 'r':[167.5 ,224.5, 189, 246, 'navy','white'], 's': [223.5 ,224.5, 245, 246, 'navy','white']},
        'B': {'p': [501.75 ,167.5, 523.25, 189, 'red3', 'white'], 'q': [557.75 ,167.5, 579.25, 189, 'red3', 'white'], 'r':[501.75 ,224.5, 523.25, 246, 'red3', 'white'], 's': [557.75 ,224.5, 579.25, 246, 'red3', 'white']},
        'C': {'p': [501.75, 502, 523.25, 523.5, 'dark green', 'white'], 'q': [557.75, 502, 579.25, 523.5, 'dark green', 'white'], 'r':[501.75, 559, 523.25, 580.5, 'dark green', 'white'], 's': [557.75, 559, 579.25, 580.5, 'dark green', 'white']},
        'D': {'p': [168 ,502, 189.5, 523.5, 'yellow2', 'black'], 'q': [224 ,502, 245.5, 523.5, 'yellow2', 'black'], 'r':[168 ,559, 189.5, 580.5, 'yellow2', 'black'], 's': [224 ,559, 245.5, 580.5, 'yellow2', 'black']}}
        self._vertical_stack_spaces = ['1', '2', '3', '4', '5', '12', '19', '20', '21', '22', '23', '24', '26', '27', '28', '29', '30', '31',
                                       '38', '45', '46', '47', '48', '49', '50',
                                       '52', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7']
        self._horizontal_stack_spaces = ['6', '7', '8', '9', '10', '11', '13', '14', '15', '16', '17', '18', '25', '32', '33', '34', '35', '36', '37',
                                         '39', '40', '41', '42', '43', '44', '51', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7']



        self._current_positions = {'A':{'p':['H', canvas_1.create_oval(self._starting_token_dict['A']['p'][0], self._starting_token_dict['A']['p'][1], self._starting_token_dict['A']['p'][2], self._starting_token_dict['A']['p'][3], fill = self._starting_token_dict['A']['p'][4], outline = self._starting_token_dict['A']['p'][5])],
                                                                       'q':['H', canvas_1.create_oval(self._starting_token_dict['A']['q'][0], self._starting_token_dict['A']['q'][1], self._starting_token_dict['A']['q'][2], self._starting_token_dict['A']['q'][3], fill = self._starting_token_dict['A']['p'][4], outline = self._starting_token_dict['A']['p'][5])],
                                        'r': ['H', canvas_1.create_oval(self._starting_token_dict['A']['r'][0], self._starting_token_dict['A']['r'][1], self._starting_token_dict['A']['r'][2], self._starting_token_dict['A']['r'][3], fill = self._starting_token_dict['A']['r'][4], outline = self._starting_token_dict['A']['r'][5])],
                                   's': ['H', canvas_1.create_oval(self._starting_token_dict['A']['s'][0], self._starting_token_dict['A']['s'][1], self._starting_token_dict['A']['s'][2], self._starting_token_dict['A']['s'][3], fill = self._starting_token_dict['A']['s'][4], outline = self._starting_token_dict['A']['s'][5])]},
                                   'B': {'p': ['H', canvas_1.create_oval(self._starting_token_dict['B']['p'][0],
                                                                         self._starting_token_dict['B']['p'][1],
                                                                         self._starting_token_dict['B']['p'][2],
                                                                         self._starting_token_dict['B']['p'][3],
                                                                         fill=self._starting_token_dict['B']['p'][4],
                                                                         outline=self._starting_token_dict['B']['p'][
                                                                             5])],
                                         'q': ['H', canvas_1.create_oval(self._starting_token_dict['B']['q'][0],
                                                                         self._starting_token_dict['B']['q'][1],
                                                                         self._starting_token_dict['B']['q'][2],
                                                                         self._starting_token_dict['B']['q'][3],
                                                                         fill=self._starting_token_dict['B']['p'][4],
                                                                         outline=self._starting_token_dict['B']['p'][
                                                                             5])],
                                         'r': ['H', canvas_1.create_oval(self._starting_token_dict['B']['r'][0],
                                                                         self._starting_token_dict['B']['r'][1],
                                                                         self._starting_token_dict['B']['r'][2],
                                                                         self._starting_token_dict['B']['r'][3],
                                                                         fill=self._starting_token_dict['B']['r'][4],
                                                                         outline=self._starting_token_dict['B']['r'][
                                                                             5])],
                                         's': ['H', canvas_1.create_oval(self._starting_token_dict['B']['s'][0],
                                                                         self._starting_token_dict['B']['s'][1],
                                                                         self._starting_token_dict['B']['s'][2],
                                                                         self._starting_token_dict['B']['s'][3],
                                                                         fill=self._starting_token_dict['B']['s'][4],
                                                                         outline=self._starting_token_dict['B']['s'][
                                                                             5])]
                                         },
                                   'C': {'p': ['H', canvas_1.create_oval(self._starting_token_dict['C']['p'][0],
                                                                         self._starting_token_dict['C']['p'][1],
                                                                         self._starting_token_dict['C']['p'][2],
                                                                         self._starting_token_dict['C']['p'][3],
                                                                         fill=self._starting_token_dict['C']['p'][4],
                                                                         outline=self._starting_token_dict['C']['p'][
                                                                             5])],
                                         'q': ['H', canvas_1.create_oval(self._starting_token_dict['C']['q'][0],
                                                                         self._starting_token_dict['C']['q'][1],
                                                                         self._starting_token_dict['C']['q'][2],
                                                                         self._starting_token_dict['C']['q'][3],
                                                                         fill=self._starting_token_dict['C']['p'][4],
                                                                         outline=self._starting_token_dict['C']['p'][
                                                                             5])],
                                         'r': ['H', canvas_1.create_oval(self._starting_token_dict['C']['r'][0],
                                                                         self._starting_token_dict['C']['r'][1],
                                                                         self._starting_token_dict['C']['r'][2],
                                                                         self._starting_token_dict['C']['r'][3],
                                                                         fill=self._starting_token_dict['C']['r'][4],
                                                                         outline=self._starting_token_dict['C']['r'][
                                                                             5])],
                                         's': ['H', canvas_1.create_oval(self._starting_token_dict['C']['s'][0],
                                                                         self._starting_token_dict['C']['s'][1],
                                                                         self._starting_token_dict['C']['s'][2],
                                                                         self._starting_token_dict['C']['s'][3],
                                                                         fill=self._starting_token_dict['C']['s'][4],
                                                                         outline=self._starting_token_dict['C']['s'][
                                                                             5])]
                                         },
                                   'D': {'p': ['H', canvas_1.create_oval(self._starting_token_dict['D']['p'][0],
                                                                         self._starting_token_dict['D']['p'][1],
                                                                         self._starting_token_dict['D']['p'][2],
                                                                         self._starting_token_dict['D']['p'][3],
                                                                         fill=self._starting_token_dict['D']['p'][4],
                                                                         outline=self._starting_token_dict['D']['p'][
                                                                             5])],
                                         'q': ['H', canvas_1.create_oval(self._starting_token_dict['D']['q'][0],
                                                                         self._starting_token_dict['D']['q'][1],
                                                                         self._starting_token_dict['D']['q'][2],
                                                                         self._starting_token_dict['D']['q'][3],
                                                                         fill=self._starting_token_dict['D']['p'][4],
                                                                         outline=self._starting_token_dict['D']['p'][
                                                                             5])],
                                         'r':['H', canvas_1.create_oval(self._starting_token_dict['D']['r'][0],
                                                                         self._starting_token_dict['D']['r'][1],
                                                                         self._starting_token_dict['D']['r'][2],
                                                                         self._starting_token_dict['D']['r'][3],
                                                                         fill=self._starting_token_dict['D']['r'][4],
                                                                         outline=self._starting_token_dict['D']['r'][
                                                                             5])],
                                         's':['H', canvas_1.create_oval(self._starting_token_dict['D']['s'][0],
                                                                         self._starting_token_dict['D']['s'][1],
                                                                         self._starting_token_dict['D']['s'][2],
                                                                         self._starting_token_dict['D']['s'][3],
                                                                         fill=self._starting_token_dict['D']['s'][4],
                                                                         outline=self._starting_token_dict['D']['s'][
                                                                             5])]}
                                   }


    def get_players(self):
        '''Returns the players list'''
        return self._players

    def get_current_positions(self):
        '''Returns the current positions dictionary'''
        return self._current_positions

    def get_rolls(self):
        return self._rolls

    def get_last_oval(self):
        return self._last_oval

    def get_current_position(self, player, token):
        return self._current_positions[player][token][0]

    def record_roll(self, roll):
        self.get_rolls().append(roll)

    def update_current_position(self, player, token):
        self._current_positions[player.get_player_position()][token][0] = str(player._token_info[token]['position'])

    def same_space_check(self, player_1, token, position):
        '''Checks whether a player's token is on the same space as another player's token'''
        player_position = player_1.get_player_position()

        if position == 'E' or position == 'R' or position == 'H':
            return
        else:
            bounced_back_dict = {}
            for player in self._current_positions:
                if player == player_position:
                    pass
                else:
                    for token in self._current_positions[player_position]:
                        if self._current_positions[player][token][0] == position:
                            if len(bounced_back_dict) == 0:
                                bounced_back_dict[player] = [token]
                                self._stacked_tracker[player][token] = [False, None]
                            else:
                                bounced_back_dict[player].append(token)
                                self._stacked_tracker[player][token] = [False, None]
            return bounced_back_dict

    def blocked_spaces(self):
        try:
            for player in self._stacked_tracker:
                player_object = self.get_player_by_position(player)
                for token in self._stacked_tracker[player]:
                    if self._stacked_tracker[player][token][0] == True:
                        space = self._current_positions[player][token][0]
                        if player not in space:
                            self._blocked_spaces[space] = player #when in home square, spaces aren't blocked
                        if player in space:
                            if player == 'A':
                                previous_space = 53 + int(space[-1]) - 1 - r1._rolls[-1]
                            else:
                                previous_space = player_object.get_start_space() + int(space[-1]) - 1 - r1._rolls[-1]
                        elif int(space) - r1._rolls[-1] < 1:
                            previous_space = 51 + int(space) - r1._rolls[-1]
                        else:
                            previous_space = int(space) - r1._rolls[-1]
                        if str(previous_space) in self._blocked_spaces:
                            del(self._blocked_spaces[str(previous_space)])
        except ValueError:
            pass

    def stacked_check(self, player, token, position):
        player_name = player.get_player_position()
        for token1 in self._current_positions[player_name]:
            if token1 == token:
                pass
            elif self._current_positions[player_name][token1][0] == position and self._stacked_checker[player_name][token1][0] == False:
                self._stacked_tracker = [True, token1]

    # def moving_algorithm(self, player):
    #     player_name = player.get_player_position()
    #     for token1 in self._current_positions[player_name]:
    #         if token1 == token:
    #             pass
    #         elif self._current_positions[player_name][token1][0] == position:
    #             self._stacked_tracker = [True, token1]

    def get_player_by_position(self, position):
        '''Gets the player object based on a passed in player position'''
        valid_strings = []
        for player in self.get_players():
            valid_strings.append(player.get_player_position())

        if position not in valid_strings:
            return "Player not found!"
        else:
            for player in self.get_players():
                if player.get_player_position() == position:
                    return player


    def check_completed(self):
        completed_list = []
        for player in self._players:
            if self._current_positions[player.get_player_position()]['p'][0] == player.get_player_position() + '7' and self._current_positions[player.get_player_position()]['q'][0] == player.get_player_position() + '7' and self._current_positions[player.get_player_position()]['r'][0] == player.get_player_position() + '7' and self._current_positions[player.get_player_position()]['r'][0] == player.get_player_position() + '7':
                completed_list.append(player.get_player_position())
        return completed_list

    def possible_moves(self, player_name, roll):
        moves_dict = {}
        potential_new_step_count = None
        player = self.get_player_by_position(player_name)
        print(self._current_positions, 'possible moves current posiitons')
        print(roll)
        for token in self._current_positions[player_name]:

            if roll == 6 and self._current_positions[player_name][token][0] == 'H':
                if self.get_player_by_position(player_name).get_start_space() in moves_dict:
                    pass # avoids adding the same position to the moves list and thus moving the token twice
                else:
                    if str(player.get_start_space()) not in moves_dict:
                        moves_dict[str(player.get_start_space())] = token #doesn't add token if it's already in the list - makes sure 'p' is moved first, 'q' second, etc.

            elif self._current_positions[player_name][token][0] != 'H':
                previous_spot = player.get_token_dict()[token]['step count']

                if previous_spot == 59:
                    pass
                elif previous_spot == 0:
                    potential_new_step_count = 1
                else:
                    potential_new_step_count = previous_spot + roll

                    if potential_new_step_count > 59:  # handles the step count when it goes over 57
                        potential_new_step_count = 59 - (roll - (59 - (previous_spot)))

                if potential_new_step_count is not None:
                    potential_new_space = player.get_space_name_int(potential_new_step_count)
                    if str(potential_new_space) not in moves_dict:
                        moves_dict[str(potential_new_space)] = token

        return moves_dict

    def stacked_checker(self, player_name):
        stacked_list = []
        for token in self._stacked_tracker:
            if self._stacked_tracker[player_name][token][0] == True:
                stacked_list.append(token)
        return stacked_list

    def move_token(self, player, token, position, player_color, player_outline):
        print('move token',token,'to position', position)
        lookup = spaces[position]
        player_name = player.get_player_position()
        print(self._current_positions, 'before deleted token', token)
        canvas_1.delete(self._current_positions[player.get_player_position()][token][1])
        print(self._current_positions, 'deleted token', token)
        for square in r1._cyan_squares_list:
            canvas_1.delete(square) # clears out cyan squares indicating possible moves from the board
        self._current_positions[player.get_player_position()][token][1] = canvas_1.create_oval(lookup[0], lookup[1], lookup[2], lookup[3], fill = player_color, outline = player_outline)
        ending_position = self._current_positions[player.get_player_position()][token][0]
        bounced = self.same_space_check(player, token, ending_position)
        if bounced is not None:
            for name in bounced:
                for player1 in self.get_players():
                    if name == player1.get_player_position():
                        print(name)
                        for token1 in bounced[name]:
                            print(token1)
                            player1.bounced_back(token1)
                            self._current_positions[player1.get_player_position()][
                                token1][0] = 'H'
                            canvas_1.delete(self._current_positions[player1.get_player_position()][token1][1])
                            self._current_positions[player1.get_player_position()][token1][0] = 'H'
                            print(self._current_positions, 'current positions bounced')
                            print(player1._token_info, 'token info bounced')
                            print('creating oval 1')
                            my_oval = canvas_1.create_oval(self._starting_token_dict[name][token1][0],
                                                           self._starting_token_dict[name][token1][1],
                                                           self._starting_token_dict[name][token1][2],
                                                           self._starting_token_dict[name][token1][3],
                                                           fill=self._starting_token_dict[name][token1][4],
                                                           outline=self._starting_token_dict[name][token1][
                                                               5])

                            self._current_positions[name][token1][1] = my_oval

        #new code
        other_token = None
        print('token is ', token)
        if self._stacked_tracker[player_name][token][0] == True:
            other_token = self._stacked_tracker[player_name][token][1]
        else:
            for token1 in self._current_positions[player_name]:
                if token1 == token:
                    pass
                elif self._current_positions[player_name][token1][0] == ending_position and self._stacked_tracker[player_name][token1][0] == False:
                    other_token = token1
        print(token, 'is token and other token is', other_token)
        if self._current_positions[player_name][token][0] != 'H' and other_token is not None:
            canvas_1.delete(self._current_positions[player_name][token][1])
            canvas_1.delete(self._current_positions[player_name][other_token][1])
            print('creating oval 2')
            my_oval = canvas_1.create_oval(lookup[0], lookup[1],
                                           lookup[2], lookup[3],
                                           fill=player_color, outline=player_outline)
            my_oval2 = canvas_1.create_oval(lookup[0], lookup[1] - 10,
                                            lookup[2], lookup[3] - 10,
                                            fill=player_color, outline=player_outline)
            self._current_positions[player_name][token][1] = my_oval
            self._current_positions[player_name][other_token][1] = my_oval2
            self._stacked_tracker[player_name][token] = [True, other_token]
            self._stacked_tracker[player_name][other_token] = [True, token]




r1 = Recorder(['A', 'B', 'C', 'D'])

count = 0

spaces_rectangle = {'H': [100, 100, 100, 100],
              '1': [132, 317, 172, 357], '2': [169, 317, 209, 357], '3': [206, 317, 246, 357], '4': [243, 317, 283, 357], '5': [280, 317, 320, 357],
              '6': [317, 280, 357, 320], '7': [317, 242, 357, 282], '8': [317, 205, 357, 245], '9': [317, 168, 357, 208], '10': [317, 131, 357, 171], '11': [317, 93, 357, 134],
              '12': [354, 93, 394, 134],
              '13': [391, 93, 431, 134], '14': [391, 131, 431, 171], '15': [391, 168, 431, 208], '16': [391, 205, 431, 245], '17': [391, 242, 431, 282], '18': [391, 280, 431, 320],
              '19': [428, 317, 468, 357], '20': [466, 317, 505, 357], '21': [503, 317, 542, 357], '22': [540, 317, 579, 357], '23': [577, 317, 616, 357], '24': [614, 317, 653, 357],
              '25': [614, 354, 653, 394],
              '26': [614, 391, 653, 431], '27': [577, 391, 616, 431], '28': [540, 391, 579, 431], '29': [503, 391, 542, 431], '30': [466, 391, 505, 431], '31': [428, 391, 468, 431],
              '32': [391, 428, 431, 468], '33': [391, 465, 431, 505], '34': [391, 503, 431, 543], '35': [391, 540, 431, 580], '36': [391, 577, 431, 617], '37': [391, 614, 431, 655],
              '38': [354, 614, 394, 655],
              '39': [317, 614, 357, 655], '40': [317, 577, 357, 617], '41': [317, 540, 357, 580], '42': [317, 503, 357, 543], '43': [317, 465, 357, 505], '44': [317, 428, 357, 468],
              '45': [280, 391, 320, 431], '46': [243, 391, 283, 431], '47': [206, 391, 246, 431], '48': [169, 391, 209, 431], '49': [132, 391, 172, 431], '50': [94, 391, 134, 431],
              '51': [94, 354, 134, 394],
              '52': [94, 317, 134, 357],
              'A1': [132, 317, 172, 357], 'A2': [132, 354, 172, 394], 'A3': [169, 354, 209, 394], 'A4': [206, 354, 246, 394], 'A5': [243, 354, 283, 394], 'A6': [280, 354, 320, 394], 'A7': [317, 354, 357, 394],
              'B1': [391, 131, 431, 171], 'B2': [354, 131, 394, 171], 'B3': [354, 168, 394, 208], 'B4': [354, 205, 394, 245], 'B5': [354, 242, 494, 282], 'B6': [354, 280, 394, 320], 'B7': [354, 317, 394, 357],
              'C1': [577, 391, 616, 431], 'C2': [577, 354, 616, 394], 'C3': [540, 354, 579, 394], 'C4': [503, 354, 542, 394], 'C5': [466, 354, 505, 394], 'C6': [428, 354, 468, 394], 'C7': [391, 354, 431, 394],
              'D1': [317, 577, 357, 617], 'D2': [354, 577, 394, 617], 'D3': [354, 540, 394, 580], 'D4': [354, 503, 394, 543], 'D5': [354, 465, 394, 505], 'D6': [354, 428, 394, 468], 'D7': [354, 391, 394, 431],
              }




# def clicked(event):
#     global count # inform function to use external variable `count`
#     count = count + 1


def roller():
    if count % 4 == 1:
        player_name = 'A'
    elif count % 4 == 2:
        player_name = 'B'
    elif count % 4 == 3:
        player_name = 'C'
    elif count % 4 == 0:
        player_name = 'D'
    for square in r1._cyan_squares_list:
        canvas_1.delete(square)

    spaces_rectangle = {'H': [100, 100, 100, 100],
                        '1': [132, 317, 172, 357], '2': [169, 317, 209, 357], '3': [206, 317, 246, 357],
                        '4': [243, 317, 283, 357], '5': [280, 317, 320, 357],
                        '6': [317, 280, 357, 320], '7': [317, 242, 357, 282], '8': [317, 205, 357, 245],
                        '9': [317, 168, 357, 208], '10': [317, 131, 357, 171], '11': [317, 93, 357, 134],
                        '12': [354, 93, 394, 134],
                        '13': [391, 93, 431, 134], '14': [391, 131, 431, 171], '15': [391, 168, 431, 208],
                        '16': [391, 205, 431, 245], '17': [391, 242, 431, 282], '18': [391, 280, 431, 320],
                        '19': [428, 317, 468, 357], '20': [466, 317, 505, 357], '21': [503, 317, 542, 357],
                        '22': [540, 317, 579, 357], '23': [577, 317, 616, 357], '24': [614, 317, 653, 357],
                        '25': [614, 354, 653, 394],
                        '26': [614, 391, 653, 431], '27': [577, 391, 616, 431], '28': [540, 391, 579, 431],
                        '29': [503, 391, 542, 431], '30': [466, 391, 505, 431], '31': [428, 391, 468, 431],
                        '32': [391, 428, 431, 468], '33': [391, 465, 431, 505], '34': [391, 503, 431, 543],
                        '35': [391, 540, 431, 580], '36': [391, 577, 431, 617], '37': [391, 614, 431, 655],
                        '38': [354, 614, 394, 655],
                        '39': [317, 614, 357, 655], '40': [317, 577, 357, 617], '41': [317, 540, 357, 580],
                        '42': [317, 503, 357, 543], '43': [317, 465, 357, 505], '44': [317, 428, 357, 468],
                        '45': [280, 391, 320, 431], '46': [243, 391, 283, 431], '47': [206, 391, 246, 431],
                        '48': [169, 391, 209, 431], '49': [132, 391, 172, 431], '50': [94, 391, 134, 431],
                        '51': [94, 354, 134, 394],
                        '52': [94, 317, 134, 357],
                        'A1': [132, 317, 172, 357], 'A2': [132, 354, 172, 394], 'A3': [169, 354, 209, 394],
                        'A4': [206, 354, 246, 394], 'A5': [243, 354, 283, 394], 'A6': [280, 354, 320, 394],
                        'A7': [317, 354, 357, 394],
                        'B1': [391, 131, 431, 171], 'B2': [354, 131, 394, 171], 'B3': [354, 168, 394, 208],
                        'B4': [354, 205, 394, 245], 'B5': [354, 242, 394, 282], 'B6': [354, 280, 394, 320],
                        'B7': [354, 317, 394, 357],
                        'C1': [577, 391, 616, 431], 'C2': [577, 354, 616, 394], 'C3': [540, 354, 579, 394],
                        'C4': [503, 354, 542, 394], 'C5': [466, 354, 505, 394], 'C6': [428, 354, 468, 394],
                        'C7': [391, 354, 431, 394],
                        'D1': [317, 577, 357, 617], 'D2': [354, 577, 394, 617], 'D3': [354, 540, 394, 580],
                        'D4': [354, 503, 394, 543], 'D5': [354, 465, 394, 505], 'D6': [354, 428, 394, 468],
                        'D7': [354, 391, 394, 431],
                        }




    outline_dict = {'A': [136, 136, 278, 278, ], 'B': [470, 136, 612, 278], 'C': [470, 470, 612, 612],
                    'D': [136, 470, 278, 612]}
    canvas_1.delete(
        r1._current_outline)  # deletes last player's cyan circle and creates a new one for the player whose turn it is
    print('creating oval 3')
    r1._current_outline = canvas_1.create_oval(outline_dict[player_name][0], outline_dict[player_name][1], outline_dict[player_name][2],
                                           outline_dict[player_name][3], fill='', outline='cyan', width=7.5)

    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    dice_values = {'\u2680':1, '\u2681':2, '\u2682':3, '\u2683':4, '\u2684':5, '\u2685':6}
    current_roll = random.choice(dice)
    text = Label(text = current_roll, font = ("Courier", 50), bg = 'white', width = 2)
    text.place(x=340, y =10)
    current_roll = dice_values[current_roll]
    r1.record_roll(current_roll)

    r1._player_turn = player_name
    print(player_name, current_roll, 'current player and roll')
    print(r1._current_positions[player_name])
    possible_moves = r1.possible_moves(player_name, current_roll)

    r1._current_possible_moves = possible_moves
    r1.blocked_spaces()
    spaces_blocked_by_others = [key for key,value in r1._blocked_spaces.items() if value != player_name]

    global cyan_square
    global blocked_moves
    blocked_moves = []
    print(spaces_blocked_by_others, 'spaces blocked by others')
    print(possible_moves, 'possible moves')
    for position in possible_moves:
        for blocked_spot in spaces_blocked_by_others:
            if blocked_spot == str(position):
                print('same position', blocked_spot)
                pass
            elif int(position) > int(blocked_spot):
                if int(position) - r1._rolls[-1] < int(blocked_spot):
                    blocked_moves.append(position)

        if len(blocked_moves) == 0:
            position = str(position)
            print(r1._current_positions, 'current positiones')
            cyan_square = canvas_1.create_rectangle(spaces_rectangle[position][0], spaces_rectangle[position][1], spaces_rectangle[position][2], spaces_rectangle[position][3], fill='', outline='cyan', width=5)
            r1._cyan_squares_list.append(cyan_square)
        else:
            pass




    # r1.move(current_roll, player)

def get_click(event):
    player_colors = {'A': 'navy', 'B': 'red3', 'C': 'dark green', 'D': 'yellow2'}
    player_name = r1._player_turn
    player = r1.get_player_by_position(player_name)
    possible_moves = r1.possible_moves(player_name, r1._rolls[-1])
    possible_clickable_spaces = {}
    r1.blocked_spaces()
    # code marker
    print(blocked_moves, 'blocked moves')
    print(possible_moves, 'possible moves')
    for move in possible_moves:
        if move not in blocked_moves:
            possible_clickable_spaces[possible_moves[move]] = (spaces_rectangle[str(move)])
    print(possible_clickable_spaces, 'possible clickable spaces')


    global x, y, count
    x = event.x
    y = event.y
    if 5 < x < 85 and 1 < y < 20:
        count = count + 1

    count1 = 0
    current_roll = r1._rolls[-1]
    print(possible_clickable_spaces)
    for item in possible_clickable_spaces:
        if possible_clickable_spaces[item][0] < x < possible_clickable_spaces[item][2] and possible_clickable_spaces[item][1] < y < possible_clickable_spaces[item][3]:
            token = item
            player.update_position_and_steps(token, current_roll)
            r1.update_current_position(player, token)
            player_color = player_colors[player_name]
            if player_name != 'D':
                player_outline = 'white'
            else:
                player_outline = 'black'
            player_colors = {'A': 'navy', 'B': 'red3', 'C': 'dark green', 'D':'yellow2'}

            if r1._stacked_tracker[player_name][token][0] == True:
                print('moving ', token)
                other_token = r1._stacked_tracker[player_name][token][1]
                print('move_stack')
                r1.move_token(player, token, r1._current_positions[player_name][token][0], player_color,
                              player_outline)
                player.update_position_and_steps(other_token, current_roll)
                r1.update_current_position(player, other_token)
                r1.move_token(player, other_token, r1._current_positions[player_name][other_token][0], player_color,
                              player_outline)
            else:
                r1.move_token(player, token, r1._current_positions[player_name][token][0], player_color, player_outline)
            #print('clicked in a possible space!!!', possible_moves[count1])
        print(possible_clickable_spaces, 'possible clickable spaces')
        print()
        print(r1._current_positions, 'get click current positions')
        print()
        print(r1._stacked_tracker, 'stacked tracker')
        r1.blocked_spaces()
        print()
        print(r1._blocked_spaces, 'blocked spaces')
        print()
        print()
        print()
        print()
        count1 += 1

root.bind("<Button-1>", get_click)


b1 = Button(root, text="Roll the Dice!", foreground='blue', command=roller)
b1.bind("<Button-2>", get_click)
b1.place(x=0, y=0)
b1.pack()




root.mainloop() # last line of code