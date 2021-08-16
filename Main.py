###########################################################################     
#                                                                         #     
#        PyTask (The cli project manger you didn't know you needed)       #     
#                                                                         #     
#                                                                         #     
#  Copyright (c) 2020, Zackery .R. Smith <zackery.smith@hsdgreenbush.org>.#     
#                                                                         #     
#  This program is free software: you can redistribute it and/or modify   #     
#  it under the terms of the GNU General Public License as published by   #     
#  the Free Software Foundation, either version 3 of the License, or      #     
#  (at your option) any later version.                                    #     
#                                                                         #     
#  This program is distributed in the hope that it will be useful,        #     
#  but WITHOUT ANY WARRANTY; without even the implied warranty of         #     
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #     
#  GNU General Public License for more details.                           #     
#                                                                         #     
#  You should have received a copy of the GNU General Public License      #     
#  along with this program. If not, see <http://www.gnu.org/licenses/>.   #     
#                                                                         #     
###########################################################################


# *NOTE*
# This is a early version of PyTask and it is not finished so keep that in mind while checking out this program
# For future plans I would like to make this a "real" command line tool with a better system for commands and such
# A good example would be the 'add' command it is built as follows 'add [TITLE] [DESC] [LABEL]' with DESC and LABEL being optional
# If you would like the title to have spaces you must add '_' inbetween words E.g. 'add Fix_spacing_system'
# But because of the way that I call functions with eval and such adding spaces in not possable
# This kinda stuff is the reason that this is a unfinished test this issue and all other ones are listed in the github issue tracker

# *TODO* 
# *DONE* Make a simple command interpeter
# *DONE 2/2* Finish the todo_list system (Using json while also being able to store labels)
# *RESEARCH* Get font rendering / make a good looking program
# *RESEARCH* Connect to github in some form to see issues and mark them as tasks
# *DOING* For the love of all, please clean up this code I cant even fix issues because I dont know where things are >:I
# *NEED TO DO* Organize code for best viewing and reading

# *NOTES*
# No. this is not NOTE this not me ranting but is things that should be rembered or fixed
#
# 1.) One two many global's are used should fix in next update
# 2.) More informatinal comments should be made for easy reading of my code
# 3.) Organize code.. you heard it, chuncks of code should be rearanged for best reading experince
# 4.) Fix spacing in commands ** More info on github page


         # imports #
#---------------------------#
import os
import readline
import json
#---------------------------#

todo_list = {}
running = True  # Made for quit().. Yes I do know that exit() does exist. Why use this way. Well I dont know I just felt like doing it.
allowed_commands = ('help','cls','clear','credits','add','rm','edit','state','load','export','log','quit')  # This is here to restrict the abuse of eval
disallowed_command_prefixs = ('os.')  # Another method to restrict eval and give the user a special message asking them to stop
log = []
path = str(os.getcwd())+'/'

# main function
# ------------------------------------------------------------------------------------------------------------
def main():
    try:
        global running
        global todo_list
    
        ## Commands
        def credits():
            print('''
> Idea              (YATA by Wiitd | https://wiitd.itch.io/yata)
> Development       (Zackery .R. Smith | https://github.com/WillsCHEATTT)


HUGE thanks to Wiitd for the idea, this is almost a direct copy with more fetures. Please check out Wiitd on his itch.io page >> https://wiitd.itch.io/''')
        
        def help(command=None):
            if command != None:


# credits command help
# ------------------------------------------------------------------------------------------------------------
                def credits_help():
                    print('''
Credits is as it seems shows all credits for PyTask''')
                return


# add command help
# ------------------------------------------------------------------------------------------------------------
                def add_help():
                    print('''
Add, adds a new entry/task. The command is structured in this manner.
    add *title* #desc# #label#

** symbolizes required flags while ## symbolizes optional flags
TITLE > It is how it sounds it is the title/name for the entry/task
DESC > Short term for description. As it sounds it will be a small description, for the entry.
LABEL > Label could also be said as state E.g. DOING, DONE and such the label may be anyhing you disire not just DOING, or DONE

* For more indepth explanations along with code examples please refer to PyTask Git Wiki''')   
                    return


# rm command help
# ------------------------------------------------------------------------------------------------------------
                def rm_help():
                    print('''
Rm, removes an entry with a title being supplied. The command is structured in this manner.
    rm *title*
        ** symbolizes required flags while ## symbolizes optional flags

TITLE > It is how it sounds it is the title/name of the entry''')
                    return


# edit command help
# ------------------------------------------------------------------------------------------------------------
                def edit_help():
                    print('''
Edit, edits the description of an entry. If DESC is not supplied no changes will be made. The command is structured in this manner.
    edit *title* #desc#
        ** symbolizes required flags while ## symbolizes optional flags

TITLE > It is how it sounds it is the title/name of the entry
DESC > Short term for description. When supplied, it will create a small desc for the entry.''')
                    return


# state command help 
# ------------------------------------------------------------------------------------------------------------
                def state_help():
                    print('''
State, allows for the creation of a label/state aswell as being able to edit a state. The command is structured in this manner.
    state *title* *label*
        ** symbolizes required flags while ## symbolizes optional flags

TITLE > The title/name of the entry you disire to edit
LABEL > The state/label of the entry E.g. [DOING], or [DONE] ** Not limited to these choices''')
                    return


# clear command help 
# ------------------------------------------------------------------------------------------------------------
                def clear_help():
                    print('''
Clear, clears your todo list.''')
                    return


# cls command help
# ------------------------------------------------------------------------------------------------------------
                def cls_help():
                    print('''
Cls, clears the screen. Not to be confused with clear that clears your todo list.''')
                    return


# load command help
# ------------------------------------------------------------------------------------------------------------
                def load_help():
                    print('''
Load, loads a json or txt file and parse's it to task's / entry's
    load *ext*
        ** symbolizes required flags while ## symbolizes optional flags

EXT > Short for extension the two currenly avalable for use are json & txt files''')
                    return


# export command help
# ------------------------------------------------------------------------------------------------------------
                def export_help():
                    print('''
Export, exports your todo list into a json or txt file format
    export *ext*
        ** symbolizes required flags while ## symbolizes optional flags

EXT > Short for extension the two currenly avalable for use are json & txt files''')
                    return


# path command help
# ------------------------------------------------------------------------------------------------------------
                def path_help():
                    print('''
Path, allows for the user to change the path that load & export will use to store & get files
    path *path*
        ** symbolizes required flags while ## symbolizes optional flags

PATH > The path to the location in witch you want load and export to load & export files to''')
                    return


# log command help
# ------------------------------------------------------------------------------------------------------------
                def log_help():
                    print('''
Log, as it sounds it is a log of all actions done. ''')
                    return


# quit command help
# ------------------------------------------------------------------------------------------------------------
                def quit_help():
                    print('''
Quit, pretty simple all it does is quits the application / program ** same result can be produced with ctrl+c''')
                    return


                ## Small chunck of code that connects to the 'help' func
                eval(str(command)+'_help()')
                return


# main help command (with no arguments passed)
# ------------------------------------------------------------------------------------------------------------
            print('''
> credits    (all credits for the development of PyTask)
> add        (adds new entry)
> rm         (removes entry)
> edit       (edits entry)
> state      (changes or sets a label/state E.g. [DOING], [DONE])
> clear      (clear all entrys)
> cls        (clear screen)
> load       (loads list in .txt or .json format)
> export     (exports list in .txt or .json format)
> path       (changes file export path * Default path {path})
> log        (shows all actions performed)
> help       (shows this screen) - Usage >> help *COMMAND*
> quit       (quits script)
            '''.format(path=os.getcwd()))


# load command
# ------------------------------------------------------------------------------------------------------------
        def load(ext):
            global todo_list
            global path
            ## Parameter vaildation check
            if ext not in ['txt', 'json']:
                print("Sorry only 'txt' & 'json' exports are available. Please read the github README.md for more help.")
                return

            elif ext == 'txt':
                with open(path+"todo_list.txt", "r") as todo_list_export:
                    todo_list = json.loads(todo_list_export.readlines()[0])
                    todo_list.pop('EOF')

            elif ext == 'json':
                with open(path+"todo_list.json", "r") as json_file:
                    data = json.load(json_file)
                    todo_list = data
                    todo_list.pop('EOF')


# export command
# ------------------------------------------------------------------------------------------------------------
        def export(ext):
            global todo_list
            global path
            ## Parameter vaildation check
            if ext not in ['txt', 'json']:                                         
                print("Sorry only 'txt' & 'json' exports are available. Please read the github README.md for more help.")
                return 
            
            elif ext == 'txt':
                global todo_list
                with open(str(path)+'todo_list.txt', "w+") as todo_list_export:
                    todo_list_export.truncate(0)
                    todo_list.update({"EOF": "Serves as a place holder to meet syntax of json files ** More info on github page"})
                    todo_list_export.write(str(todo_list).replace("'", '"'))
                    todo_list.pop('EOF')

    
            elif ext == 'json':
                with open(str(path)+'todo_list.json', "w+") as todo_list_export:                    
                    # Clear the whole file then setup a new one
                    todo_list_export.truncate(0)
                    todo_list_export.write('{\n')
                    for i in todo_list.keys():
                        j = todo_list.get(i)
                        todo_list_export.write(f'   "{i}": {j},\n'.replace("'", '"'))
                    todo_list_export.write('   "EOF": "Serves as a place holder to meet syntax of json files ** More info on github page"\n')
                    todo_list_export.write('}')
                    print('.json export completed in {path}'.format(path=os.getcwd()))
                    input('Press enter to continue')
                    print('\n\n\n\n\n\n\n\n\n')


# path command
# ------------------------------------------------------------------------------------------------------------
        def path(location):
            global path
            path = location


# log command
# ------------------------------------------------------------------------------------------------------------
        # the log func parses the 'log' variable and prints it
        def log():
            global log
            # I know this is very chunky but for now it works
            print(str(str(str(str(log).replace(',', '\n')).replace('[', '')).replace(']', '')).replace('"', ''))


# cls command
# ------------------------------------------------------------------------------------------------------------
        # Windows inspired screen clear
        def cls():
            global log
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')


# clear command
# ------------------------------------------------------------------------------------------------------------
        # Clears the todo_list
        def clear():
            global todo_list
            global log
            todo_list.clear()
            log.append('todo list was cleared')


# add command
# ------------------------------------------------------------------------------------------------------------
        # Creates a new entry / task
        def add(title, desc=None, label=None):
            global todo_list
            global log
            todo_list |= {str(title):["" if desc == None else str(desc),"" if label == None else '['+str(label)+']']}
            log.append(f"new entry '{title}'"+str("" if desc == None else f" with the description of '{desc}'"))


# rm command
# ------------------------------------------------------------------------------------------------------------
        # Removes an entry
        def rm(title):
            global todo_list
            global log
            try:
                todo_list.pop(title)
                print(f"'{title}' Was removed")
                log.append(f"'{title}' entry was removed")
            except:
                raise Exception(f"'{title}' does not exist")


# edit command
# ------------------------------------------------------------------------------------------------------------
        # Edits an entry's description
        def edit(title, desc=None):
            global todo_list
            label = list(todo_list.get(title))[1]
            todo_list.update({str(title): ['' if desc == None else str(desc), '' if label == '' else str(label)]})


# state command
# ------------------------------------------------------------------------------------------------------------
        # Edits or adds a 'label' / state E.g. [DOING], or [DONE] ** Not restricted to these two options
        def state(title, label):
            global todo_list
            desc = list(todo_list.get(title))[0]
            todo_list.update({str(title): [str(desc), "["+str(label)+"]"]})
        

# quit command
# ------------------------------------------------------------------------------------------------------------
        def quit():
            running = False
            print('\n\nif you found an issue please report it on my github :)\nSame thing applies to addition requests I would love to hear your request!')
            exit()


# main input method
# ------------------------------------------------------------------------------------------------------------
        ## CLI type input thing..
        while running:
            # I would like to make things look nicer but that's not my thing :P
            for i in todo_list.keys():
                label = list(todo_list.get(i))[1]
                title = i
                desc = list(todo_list.get(i))[0]
                print('{label} {title}      ({desc})'.format(label=str(label).replace('_', ' '), title=str(title).replace('_', ' '), desc=str(desc).replace('_', ' ')))
            
            ## Tab auto complete
            def completer(text, state):
                global allowed_commands
                options = [i for i in allowed_commands if i.startswith(text)]
                if state < len(options):
                    return options[state]
                else:
                    return None
            
            readline.parse_and_bind("tab: complete")
            readline.set_completer(completer)
            
            try:
                usr_input = input('>> ').split(' ')
            except KeyboardInterrupt:
                quit()
            cls()
            command = usr_input.pop(0)
            # Get flags from list
            flags = ''
            for i in usr_input:
                flags += "'"+str(i) + "',"
            if command in allowed_commands:
                # Before you look down upon me for this line of code, just know I can't think or find any other "good" way to convert a string into a func call (If those are the right terms) 
                eval(str(command)+str(f'({flags})'))
            else:
                if command.startswith(disallowed_command_prefixs):
                    raise Exception("Uh oh it seems like you are trying to abuse my code.. please stop.")
                raise Exception(f"'{command}' Does not exsist, please look at the github  or do 'help' to see commands.") 
    # Two excepts one to catch ctrl+c and the other for all other errors
    except KeyboardInterrupt:
        quit()
    
    
    # main bug catcher
    # ------------------------------------------------------------------------------------------------------------
    except Exception as exc:
        print(f'An error has occured details below\n{exc}\n\nPress enter to re-open old session')
        if input() == 'debug':  # Allows for live testing and debuging
            eval(input())
        main()
main()

