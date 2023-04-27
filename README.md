# Week 4, Day 3: Homework
## Python Data Structures: Stacks & Queues and Linked Lists


#### Exercise 1 - Adding Elements to LinkedList:
- Start by creating a new method in our LinkedList class called "add_list_elements".
- This method should take in a list as an argument.
- Loop through each element in the list and convert it to a node.
- Add each node to the end of the linked list using the "add_node" method we already have in the class.

[LinkedList.py](https://github.com/geanu02/wk4-dy3-advancedpythonhw/blob/main/LinkedList.py): Lines 80 - 92

#### Exercise 2 - Updating Pokemon:
- Add a new attribute to our Pokemon class called `evolve_chain`.
- This should be initialized as an empty `LinkedList`.
- Create a new method in our Pokemon class called `add_evolve_chain` and adds each pokemon to the `evolve_chain` linked list.
- This will be a new version of `evolve_pokemon` method.
- Updates to old method.
- In the `add_evolve_chain` method, we need to take the current Pokemon and add it to the `evolve_chain` linked list using the `add_node` method we created earlier.
- Remove the `call_poke_api` call since we no longer need  to update our pokemon. Instead, we can use the `add_evolve_chain` method to add the evolution chain for a particular Pokemon.
- Finally, when we reach the last Pokemon in the chain, make sure to add it to the `evolve_chain` linked list before returning.

[Pokemon.py](https://github.com/geanu02/wk4-dy3-advancedpythonhw/blob/main/Pokemon.py): Lines 47 - 67
