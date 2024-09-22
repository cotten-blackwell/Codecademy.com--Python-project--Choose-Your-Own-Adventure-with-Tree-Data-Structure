######
# TREENODE CLASS
######
class TreeNode:
  def __init__(self, story_piece):
    print("I am being initialized")
    self.story_piece = story_piece
    self.choices = []

  def add_child(self, node):
    print("Adding child...")
    self.choices.append(node)

  def traverse(self):
    print("Traversing...")
    # assign story_node to self
    story_node = self
    # print out story_node's story_piece
    print(story_node.story_piece)
    # while story_node has choices:
    while story_node.choices != []:
      # get the user's choice using input()
      choice = input("\nEnter 1 or 2 to continue the story: ")
      # if the choice is invalid:
      if choice not in ['1', '2']:
        # tell the user
        # choice = input("\nPlease enter a valid choice:  1 or 2")
        print("\nPlease enter a valid choice:  1 or 2")
      # if the choice is valid:
      else:
        # set choice as the new story_node
        chosen_index = int(choice) - 1
        print("Chosen index = {0}".format(chosen_index))
        chosen_child = story_node.choices[chosen_index]
        print(chosen_child.story_piece)
        story_node = chosen_child

######
# VARIABLES FOR TREE
######

######
# TESTING AREA
######
# user_choice = input("What is your name? ")
# print(user_choice)
print("Once upon a time...")
story_root_string = "\n" + '"""' + "\nYou are in a forest clearing.  There is a path to the left." + "\nA bear emerges from the trees and roars!" + "\nDo you:" "\n1 ) Roar back!" + "\n2 ) Run to the left...." + '\n"""'
story_root = TreeNode(story_root_string)
# print(story_root.story_piece)

choice_a_string = "\n" + '"""' + "\nThe bear is startled and runs away." + "\nDo you:" "\n1 ) Shout 'Sorry bear!'" + "\n2 ) Yell 'Hoorary'" + '\n"""'
choice_a = TreeNode(choice_a_string)
# print(choice_a.story_piece)

choice_b_string = "\n" + '"""' + "\nYou come across a clearing full of flowers.\nThe bear follows you and asks 'what give?'" + "\nDo you:" "\n1 ) Gasp 'A talking bear!'" + "\n2 ) Explain that the bear scared you." + '\n"""'
choice_b = TreeNode(choice_b_string)
# print(choice_b.story_piece)

story_root.add_child(choice_a)
story_root.add_child(choice_b)

choice_a_1_string = "\n" + '"""' + "\nThe bear returns and tells you it's been a rough week.  After making peace with a talking bear, he shows you the way out of the forest." + "\n\nYOU HAVE ESCAPED THE WILDERNESS." + '\n"""'
choice_a_1 = TreeNode(choice_a_1_string)
# print(choice_a_1.story_piece)

choice_a_2_string = "\n" + '"""' + "\nThe bear returns and tells you that bullying is not okay before leaving you alone in the wilderness." + "\n\nYOU REMAIN LOST." + '\n"""'
choice_a_2 = TreeNode(choice_a_2_string)
# print(choice_a_2.story_piece)

choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)

choice_b_1_string = "\n" + '"""' + "\nThe bear is unamused.  After smelling the flowers, it turns around and leaves you alone." + "\n\nYOU REMAIN LOST." + '\n"""'
choice_b_1 = TreeNode(choice_b_1_string)
# print(choice_b_1.story_piece)

choice_b_2_string = "\n" + '"""' + "\nThe bear understands and apologizes for startling you.  Your new friend shows you a path leading out of the forest." + "\n\nYOU HAVE ESCAPED THE WILDERNESS." + '\n"""'
choice_b_2 = TreeNode(choice_b_2_string)
# print(choice_b_2.story_piece)

choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)

story_root.traverse()