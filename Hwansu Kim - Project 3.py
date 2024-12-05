# Project 3
# Hwansu Kim (Billy)
# 10/13/2021
# This program creates a template for a Python program's banner and section headers.


# Constants (Sections)
SECTION_NAME_1 = "Constants"
SECTION_NAME_2 = "Variables"
SECTION_NAME_3 = "Input"
SECTION_NAME_4 = "Processing"
SECTION_NAME_5 = "Output"


# Global Variables
userName = ""
userDate = ""
userProgramName = ""
userProgramDesc = ""
starLineLength = 100


# Function that displays a line of asterisks.
def displayStarLine():
    print("#", "*" * starLineLength, sep = "")


# Function that creates the individual section headers; calls displayStarLine().
def displaySectHeader(section):
    print()
    print()
    displayStarLine()
    print(format("#", "<7s"), section, sep = "")
    displayStarLine()


# Function that provides arguments for displaySectHeader and displays all the section headers.
def displaySectHeaders():
    displaySectHeader(SECTION_NAME_1)
    displaySectHeader(SECTION_NAME_2)
    displaySectHeader(SECTION_NAME_3)
    displaySectHeader(SECTION_NAME_4)
    displaySectHeader(SECTION_NAME_5)


# Function that creates and displays the banner of the template using arguments from collectInputs().
def displayBanner(name, date, programName, programDesc):
    displayStarLine()
    print(format("#", "<6s"), format("Coder", "<11s"),   ":", name)
    print(format("#", "<6s"), format("Date", "<11s"),    ":", date)
    print(format("#", "<6s"), format("Program", "<11s"), ":", programName)
    print(format("#", "<6s"),        "Description",      ":", programDesc)
    displayStarLine()


# Function that collects the user's inputs, overwriting the global variables.
def collectInputs():
    global userName, userDate, userProgramName, userProgramDesc
    userName =        input("Enter your name: ")
    userDate =        input("Enter the date: ")
    userProgramName = input("Enter the program name: ")
    userProgramDesc = input("Enter short description: ")


# Function that calls all the other functions; displaying the final result.
def main():
    collectInputs()
    print()
    print()
    displayBanner(userName, userDate, userProgramName, userProgramDesc)
    displaySectHeaders()


main()


# Summary

#    I started this project by creating an order for the function calls, luckily a hierarchy chart was provided
# so this process didn't take very long; afterwards, I confirmed which functions would be calling on others and
# which ones didn't need to call on another function. After analyzing the project requirements and using the
# hierarchy chart as a design "template", I started coding function definitions starting from the ones that would be
# at the bottom of the call hierarchy, like displayStarLine(), up to main(); after creating each function definition,
# I called each one individually to make sure they were working as intended on their own, before testing by calling
# main(). After making sure the functions all worked properly, when called individually and via main(), I adjusted
# alignment and line spacing to make the template output look more visually pleasing, and accurate to the example
# output provided in Project3.pdf.
#     As far as where I got stuck, I did have to review function parameters and arguments,
# especially in the case of using global variables; because I forgot that when functions calls on another function
# , that has parameters, you must supply the function call with arguments to fill those parameters. This project
# really provided a useful way to plan programs, that create and use a lot of function definitions and function calls
# via the hierarchy chart; if the chart wasn't provided analyzing and designing the program would have taken a decent
# bit more time. So, in future projects, if I need to create functions and establish a call hierarchy, I'll know to
# create a hierarchy chart during the analyzing and design stages to really flesh out the program's structure.

# Test Cases

# 1. Inputs for collectInputs()
#       - No problem with different types of inputs, as all inputs are stored as strings.
#           -All numerical inputs work.
#               -Examples:
#                   -1, outputs the string "1"
#                   -0, outputs the string "0"
#                   -(-1), outputs the string "-1"
#                   -1.1, outputs the string "1.1"
#           -This also applies for date formatting, everything works.
#               -MM/DD/YYYY
#               -Month DD, YYYY
#           -Leaving input blank also works, but returns no output for the banner; i.e. blank space after Coder :.
#       - Minor issue with input length if user input is longer, character-wise, than starLineLength; the resulting
#         output would stretch beyond the template's boundary. Although, this is fixed by adjusting
#         starLineLength to compensate.
#           - Would like to learn a method to automatically adjust template width, in regards to user input length,
#             so that starLineLength wouldn't need to be manually adjusted.
#               -Or impose a character limit to inputs.

# 2. Function parameters and arguments
#       - Played around with parameter and argument names, more so for code readability rather than testing.
#           -Initially had parameter and argument names that weren't really distinguishable from each other; changed
#            the parameter names to be more like placeholder names and argument names to be more identifiable as
#            the user's input/information.

# 3. Global variables
#       -Tested output, when I removed the global keyword from collectInputs
#           -Resulted in it displaying the default global variables established at the top of the program.
#               -Example: Coder displayed "Billy", regardless of user input.

# 4. Alignment and UI visuals
#       -Tested output alignment individually, starting with the banner and matched the section header's alignment to
#        the banner's alignment.
#           -For displaying the individual section headers, I ended up manipulating a string to provide the initial
#            indents, since the section header names are of varying character counts and using string formatting
#            would result in mismatched alignment.
#           -Had no problem using string formatting for displayBanner(), since each line had its own print statement,
#            unlike displaySectionHeader().
#       -Initially had zero line spacing in between the banners and section headers; this looked cramped and ugly.
#           -Used empty print statements to create breathing room in between each section header and the banner.
#               -Applied two lines of empty space in between section headers, since two is usually a good amount
#                of space between different chunks of unrelated code.
#                   -Like spacing between two different function definitions.
#       -Made changes to the way I coded alignment, via format(), based on feedback from Project 2; I have used format()
#        on the initial "#" instead, so that the alignment number can be the same for all lines of output, instead of
#        using format() on "Coder", "Date", Program", and "Description".
#           -Did the same thing for displaySectHeader()