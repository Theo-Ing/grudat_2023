# API example

The following is an example of how an API can be written for the course DD1327. 
This example is for a program that implements a class for randomly selecting colored beads from a bag. 
Features include adding beads to the bag, taking beads out of the bag and peaking at a bead inside the bag.
Below is an API written in markdown, an example of the same API written in as python script can be found [here](https://github.com/Theo-Ing/grudat_2023/blob/main/api/api.py). Note that nothing about how the methods are implemented are described in the API, only what the methods actually achieve.

## API

### Class MarbleBag
Simulates a bag of marbles where colored marbles can be added or randomly withdrawn.
```
class MarbleBag
  def __init__(self, size)
```
Create an empty marble bag.

:param **size**: (_int_) The maximum number of marbles the bag can contain, if set to zero the bag can contain any number of marbles.

#### Method add
```
def add(self, color)
```
Add a colored marble to the bag.

:param **color**: (_string_) The name of the color of the marble.

#### Method take
```
def take(self)
```
Randomly retrieve a marble from the bag. The selected marble is removed from the bag.

:**return**: (_string_) The color of the retrieved marble.

#### Method peek
```
def peek(self)
```
Randomly look at a marble from the bag. The selected marble is put back in the bag.

:**return**: (_string_) The color of the selected marble
