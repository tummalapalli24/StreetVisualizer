"""
    File    : street.py
    
    Purpose : This program creates a visualization of a city street by 
              allowing the user to input a one-line specification of various
              street elements, including buildings, parks, and empty lots. 
              It renders an ASCII representation of the street based on 
              the specified widths and heights of the elements provided
              by the user.
"""

class Building:
    """
    Represents a building with a specified width, height, and brick symbol 
    used for rendering.
    
    The Building class provides functionality to visualize the building 
    at a given height, returning a string that represents its appearance. 
    If the specified height is greater or equal to building's height, 
    it returns a blank space representation; otherwise, it displays the 
    building's symbol with a width given.
    """
    
    def __init__(self, width, height, brick):
        """
        Initializes a Building instance with width, height, and brick
        character used for rendering.

        Parameters:
            width (int): The width of the building.
            height (int): The height of the building.
            brick (str): The symbol used to represent the building visually.
        """
        self._width = width
        self._height = height
        self._symbol = brick
    
    def at_height(self,height):
        """
        This method is used to return the string representation of the 
        building at the specified height.

        Parameters:
            height (int): The height at which to render the building.
        
        Returns:
            str: A string representing the building or empty space
                based on its height.
        """
        if height >=self._height :
            return " "*self._width
        else:
            return self._symbol*self._width

class EmptyLot:
    """
    Represents an empty lot with a specified width and pattern.
    
    The EmptyLot class allows for visual representation of an empty lot,
    with the option to fill it with specific symbols or spaces. It can return
    a representation based on the height specified, which determines
    if the lot is visible or hidden.
    """
    
    def __init__(self,width,trash):
        """
        Initializes an EmptyLot instance with width and symbol.

        Parameters:
            width (int): The width of the empty lot.
            trash (str): The symbol used to represent the empty 
                            lot visually.
        """
        self._width = width 
        self._pattern = trash
    
    def lot_helper(self,answer,reference,width):
        """
        This method is a helper function to recursively build the string
        representation of the lot.

        Parameters:
            answer (str): The current accumulated string representation.
            reference (int): The current index for the trash pattern 
                            being processed.
            width (int): The remaining width to fill in the representation.
        
        Returns:
            str: The final string representation of the empty lot.
        """
        # Return the accumulated answer when width is zero
        if width == 0 :
            return answer
        else:
            if reference == len(self._pattern):
                # Reset reference if it exceeds pattern length
                reference = 0
            if self._pattern[reference] == "_" :
                # Add a space if the current pattern is an underscore
                answer += " "
                # Recursive call with updated parameters
                return self.lot_helper(answer,reference+1,width-1)
            else:
                # Recursive call with updated parameters if not a underscore.
                answer += self._pattern[(reference % len(self._pattern))]
                # Recursive call with updated parameters
                return self.lot_helper(answer,reference+1,width-1)
        
    def at_height(self,height):
        """
        Returns the string representation of the empty lot at the specified 
        height.

        Parameters:
            height (int): The height at which to render the empty lot.
        
        Returns:
            str: A string representing the empty lot or empty space based on 
                    its height.
        """
        if height == 0 :
            return self.lot_helper("",0,self._width)
        else:
            return " " * self._width 
    
class Park :
    """
    Represents a park with a specified width and symbol.
    
    The Park class provides a way to visualize a park at various heights,
    returning different representations depending on the height specified.
    The visual representation includes a tree at lower heights and a 
    grassy area at higher heights, creating a dynamic visual experience.
    """
    
    def __init__(self,width,foliage):
        """
        Initializes a Park instance with width and symbol.

        Parameters:
            width (int): The width of the park.
            foliage (str): The symbol used to represent the park visually.
        """
        self._width = width 
        self._symbol = foliage 
    
    def at_height(self,height):
        """
        This method returns the string representation of the park at the 
        specified height.

        Parameters:
            height (int): The height at which to render the park.
        
        Returns:
            str: A string representing the park based on its height.
        """
        if 0 <= height <= 1:
            return " "*int((self._width-1)/2)+"|"+" "*int((self._width-1)/2)
        # Grass representation based on the height 
        elif 2<= height <= 4:
            return  " "*int((self._width-(5-((height-2)*2)))/2) + \
                        self._symbol*(5-((height-2)*2)) + \
                            " "*int((self._width-(5-((height-2)*2)))/2)
        # Return empty space for height above 4
        else:
            return " "*self._width
    
def street_helper(final,elements,height):
    """
    Recursively constructs a string representation of street elements
    at a specified height.
    
    Parameters:
        final (str): The current string being built to represent the street.
        elements (list): A list of street elements that have a method 
                        'at_height' for rendering.
        height (int): The height at which to render the street elements.
        
    Returns:
        str: A string representation of the street elements at the
            specified height.
    """
    # Base case: If there no elements to process, returns final string + "|".
    if elements == []:
        return final +"|"
    else:
        # Add the current element at the specified height to the final string.
        final += elements[0].at_height(height)
        # Recursive call with the remaining elements.
        return street_helper(final,elements[1:],height)

def print_street_at_height(elements,height):
    """
    Prints the string representation of street elements for each height
    from the given height down to 0.
    
    Parameters:
        elements (list): A list of street elements that have a method 
                        'at_height' for rendering.
        height (int): The maximum height to print the street elements.
        
    Returns:
        str: An empty string if height is -1; otherwise, it prints each 
                height's street representation.
    """
    # Base case: If the height is -1, return an empty string.
    if height == -1 :
        return ""
    else:
        # Print the street representation at the current height.
        print(street_helper("|" ,elements,height))
        # Recursive call to print representation for the next lower height.
        return print_street_at_height(elements,height-1)
    
def create_street_classes(class_list):
    """
    Recursively creates a list of street class instances from the provided
    class_list, where each string represents a street element formatted as
    'p:width,height' for parks, 'b:width,height,brick' for buildings, and
    'e:width,trash' for empty lots. The function constructs and returns
    instances of the Park, Building, or EmptyLot classes based on the input.
    
    Parameters:
        class_list (list): A list of strings representing different 
                            street elements.

    Returns:
        list: A list of instances of Park, Building, or EmptyLot corresponding
                to the input strings.
    """
    # Base case: If the list is empty, return an empty list.
    if len(class_list) == 0:
        return []
    else:
        # Get the current element from the class list.
        current_class = class_list[0]
        # Handling the case for parks (type 'p').
        if current_class[0] == 'p':
            park_info = current_class.split(":")
            # Get width and foliage by splitting on ','.
            park_dimensions = park_info[-1].split(',')
            return [Park(int(park_dimensions[0]), park_dimensions[1])]\
                    + create_street_classes(class_list[1:])
        # Handling the case for buildings (type 'b').
        elif current_class[0] == 'b':
            # Skip the 'b:' prefix.
            building_info = current_class[2:]
            # Split dimensions for width, height, and brick.
            building_dimensions = building_info.split(',')
            return [Building(int(building_dimensions[0]), \
                int(building_dimensions[1]), building_dimensions[2])] \
                    + create_street_classes(class_list[1:])
        # Handling the case for empty lots (type 'e').
        else: 
            empty_lot_info = current_class.split(":")
            # Get width and trash pattern.
            empty_lot_dimensions = empty_lot_info[1].split(",")
            return [EmptyLot(int(empty_lot_dimensions[0]),\
            empty_lot_dimensions[1])]+create_street_classes(class_list[1:])

def sum_width(dimensions_list):
    """
    Recursively calculates the total width from a list of dimension strings 
    formatted as 'type:width,foliage' or 'type:width,height,brick' or 
    'type:width,trash' by summing the widths of all objects represented 
    in the list.

    Args:
        dimensions_list (list): A list of dimension strings representing 
                                different objects.
        
    Returns:
        int: The total width calculated from the dimension strings.
    """
    # Base case: If the list is empty, return 0 (no width to add).
    if len(dimensions_list) == 0 :
        return 0 
    else:
        # Split by ':' to separate the type from dimensions.
        dimensions = dimensions_list[0].split(":")
        # Getting the width and height by splitting on ','
        dimension_values = dimensions[1].split(",")
        # adding int width it to the sum of widths from the remaining list.
        return int(dimension_values[0]) + sum_width(dimensions_list[1:])
    
def max_height(maximum,lst):
    """
    Recursively calculates the maximum height from list of dimension strings.
    
    Parameters:
        maximum (int): The current maximum height found .
        lst (list): A list of dimension strings representing different objects.
        
    Returns:
        int: The maximum height found among the objects in the list.
    """
    # Base case: If the list is empty, return the maximum height found.
    if len(lst) == 0 :
        return maximum
    else:
        # Split first element to determine the object type and its dimensions.
        dimensions = lst[0].split(":")
        dimension_type = dimensions[0]
        dimensions_values = dimensions[1].split(",")
        if len(dimensions_values) == 2 and dimension_type == 'p':
            # Parks have a maximum height of 5.
            maximum = max(maximum,5)
            # Recursive call for the next object.
            return max_height(maximum,lst[1:])
        elif len(dimensions_values) == 2 and dimension_type == 'e':
            # Empty lots have a maximum height of 1.
            maximum = max(maximum,1)
            # Recursive call for the next object.
            return max_height(maximum,lst[1:])
        else:
            # For buildings,update maximum height based on building height.
            maximum = max(maximum,int(dimensions_values[1]))
            # Recursive call for the next object.
            return max_height(maximum,lst[1:])
        
def main():
    street_input = input("Street: ")
    list_of_classes = street_input.split()
    width_sum = sum_width(list_of_classes)
    height_max = max_height(0,list_of_classes)
    street_classes = create_street_classes(list_of_classes)
    print("+" + '-'*width_sum + "+")
    print_street_at_height(street_classes,height_max)
    print("+" + '-'*width_sum + "+")
main()  
