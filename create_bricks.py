import random


import math
import json

class Brick:
    def __init__(self, x, y, z, label='None', shape='None', color = 'None'):
        self.x = x
        self.y = y
        self.z = z
        self.label = label
        self.shape = shape
        self.color = color
    def __str__(self):
        x = self.x
        res = 'Brick at ({}, {}, {}, {}, {}, {})'.format(self.x, self.y, self.z, self.label, self.shape, self.color)
        return res
    
    def get_position_description(self, bricks):
        #print(len(bricks))
        for item in bricks:
            if item.x == self.x and item.y == self.y and abs(item.z - self.z)==1:
                prev_brick = item
                break
            elif item.x == self.x and item.z == self.z and abs(item.y - self.y)==1:
                prev_brick = item
                break
            elif item.y == self.y and item.z == self.z and abs(item.x - self.x)==1:
                prev_brick = item
                break
            else:
                continue
        x_diff = self.x - prev_brick.x
        y_diff = self.y - prev_brick.y
        z_diff = self.z - prev_brick.z

        if x_diff == 0 and y_diff == 0 and z_diff == 1:
            return "The brick {} is on top of the brick {} . ".format(self.label, prev_brick.label)
        elif x_diff == 0 and y_diff == 0 and z_diff == -1:
            return "The brick {} is below the brick {}. ".format(self.label, prev_brick.label)
        elif x_diff == 0 and y_diff == 1 and z_diff == 0:
            return "The brick {} is to the right of the brick {}. ".format(self.label, prev_brick.label)
        elif x_diff == 0 and y_diff == -1 and z_diff == 0:
            return "The brick {} is to the left of the brick {}. ".format(self.label, prev_brick.label)
        elif x_diff == 1 and y_diff == 0 and z_diff == 0:
            return "The brick {} is in front of the brick {}. ".format(self.label, prev_brick.label)
        elif x_diff == -1 and y_diff == 0 and z_diff == 0:
            return "The brick {} is behind the brick {}. ".format(self.label, prev_brick.label)
        else:
            return "next to the previous brick, but not in any particular direction"


def distance(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2 + (a.z - b.z)**2)

def find_nearest_bricks(bricks, target, target_color="white"):
    min_distance = float('inf')
    nearest_brick = None

    for brick in bricks:
        if brick.color == target_color:
            dist = distance(brick, target)
            
            if dist < min_distance:
                min_distance = dist
                nearest_brick = brick
    print("The nearest {} object of brick {} is {}".format(target_color, target.label, nearest_brick.label ))
    return nearest_brick

def find_farthest_bricks(bricks, target, target_color="white"):
    max_distance = float('-inf')
    farthest_brick = None

    for brick in bricks:
        if brick.color == target_color:
            dist = distance(brick, target)
            if dist > max_distance:
                min_distance = dist
                farthest_brick = brick
    print("The farthest {} object of brick {} is {}".format(target_color, target.label, farthest_brick.label ))
    return farthest_brick


def build_bricks(n, m, height, shuffle):
    flag = 65
    bricks=[]
    colors = ['blue', 'yellow','white']
    shapes = ['triangle', 'square']
    all_nums = n*m*height
    label_list = [chr(i+flag) for i in range(all_nums)]
    
    for i in range(n):
        for j in range(m):
            index = random.randint(0, 2)
            color = colors[index]
            index = random.randint(0, 1)
            shape = shapes[index]
            if shuffle:
                random_element = random.choice(label_list)
                label_list.remove(random_element)
            else:
                random_element = chr(flag)
            bricks.append(Brick(i, j, 0, random_element, shape, color ) )
            flag+=1
    
  
    #bricks = [Brick(i, j, 0, chr(flag)) for i in range(n) for j in range(m)]
    #random.shuffle(bricks)

    for z in range(1, height):
        prev_layer_bricks = [brick for brick in bricks if brick.z == z - 1]
        
        prev_layer_coords = [(brick.x, brick.y) for brick in prev_layer_bricks]
        print("prev_layer_coords", prev_layer_coords)
        available_coords = [(i, j) for i in range(n) for j in range(m) if (i, j) in prev_layer_coords]
        print("available_coords", available_coords)
        random.shuffle(available_coords)
        print("shuffled", available_coords)
        if len(available_coords)>1:
            nums = random.randint(1, len(available_coords))
        else:
            nums=1

        print("num", nums)
        
        for item in range(nums):
            index = random.randint(0, 2)
            color = colors[index]
            index = random.randint(0, 1)
            shape = shapes[index]
            (x,y) = available_coords[item]
            print("label_list",label_list)
            if shuffle:
                random_element = random.choice(label_list)
                label_list.remove(random_element)
            else:
                random_element = chr(flag)
            brick = Brick(x, y, z, random_element, shape, color)
            bricks.append(brick)
            flag+=1
            #break

    return bricks

def make_dict(dict_ ,brick, bricks):
    for item in bricks:
        if item.x == brick.x and item.y == brick.y and item.z - brick.z==1:
            dict_[item.label] = brick.label
        else:
            continue
            
def remove_bricks(brick, brick_dict, res):
  
 
    above_bricks = []
    for b, a in brick_dict.items():
        if a == brick:
            above_bricks.append(b)
    for b in above_bricks:
        res = remove_bricks(b, brick_dict,res)
    print(brick)
    if brick not in brick_dict.keys():
        res = res + brick
        return res
    res = res + brick
    brick_dict.pop(brick)
    return res

    
        




if __name__ == "__main__":

    
    n = 1
    m = 1
    shuffle_label = True
    bricks = build_bricks(n, m,4, shuffle_label)
    for brick in bricks:
        print(brick)
    print("------------------------")
    res = "There are a set of bricks. "
    color_set = set({})
    shape_set = set({})
    for i in range(len(bricks)):
        print(bricks[i])
        color_set.add(bricks[i].color)
        shape_set.add(bricks[i].shape)
        if i>0:
            print(i)
            res = res + bricks[i].get_position_description(bricks[:i])
            print(res)
        else:
            #res = res + ", " +"for the brick {}, the shape is {}, and the color is {}".format(bricks[i].label, bricks[i].shape, bricks[i].color)
            res = res  +"There is a brick {}".format(bricks[i].label)
    brick_target = find_farthest_bricks(bricks, bricks[1], target_color="white")
    brick_target = find_nearest_bricks(bricks, bricks[1], target_color="white")
    dict_above = {}
    for item in bricks:
        make_dict(dict_above, item, bricks)
    print(dict_above)
    res = ''
    res = remove_bricks("B", dict_above, res)
    print("res",res)
    print(res, dict_above)
    data_list = []
    for i in range(500):
        list_char = []
        color_set = set({})
        shape_set = set({})
        flag = 65
        #random.randint(1, 2)
        '''
        n = random.randint(1, 2)
        m = random.randint(1, 2)
        '''
        l = random.randint(2, 7)

        n, m = 1, 1

        n = random.randint(2, 3)
        
        num = random.randint(1, 3)
        for j in range(n * m):
            list_char.append(chr(flag+j))
        char_index = random.randint(1, 3)
        
        
        shuffle_label = False
        bricks = build_bricks(n, m,l, shuffle_label)
        for item in bricks:
            color_set.add(item.color)
            shape_set.add(item.shape)
        res = "There are a set of bricks. "
        color_list = list(color_set)
        shape_list = list(shape_set)
        #random.randint(1, )
        shuffled = True
        
        if shuffled:
            res_list = []
            for i in range(len(bricks)):
                if i > 0:
                    res_list.append(bricks[i].get_position_description(bricks[:i]))
                else:
                    res_list.append("For the brick {}, the color is {}. ".format(bricks[i].label, bricks[i].color))
                    
            random.shuffle(res_list)
                    
            

            print("res_list", res_list)
            for item in res_list:
                res = res  + item
        else:
            for i in range(len(bricks)):
              if i>0:
                #print(i)
                res = res +  bricks[i].get_position_description(bricks[:i])
                #print(res)
              else:
                res = res + "For the brick {}, the color is {}. ".format(bricks[i].label, bricks[i].color)
        #res = res +". How to get brick {}".format(brick_target.label) + "?"
        res = res + "Now we have to get a specific brick. "
        rule = 'The bricks must now be grabbed from top to bottom, and if the lower brick is to be grabbed, the upper brick must be removed first. '
        res = res + rule
        num = 3
        if num == 1:
            choiced_color = random.choice(color_list)
            brick_target = find_farthest_bricks(bricks, bricks[char_index-1], target_color=choiced_color)
            if brick_target.label == bricks[char_index-1].label:
                res = res +"How to get brick {}?".format(brick_target.label)
            else:
                res = res +"How to get the farthest {} brick of the brick {}".format(choiced_color, bricks[char_index-1].label) + "?"
        elif num == 2:
            choiced_color = random.choice(color_list)
            brick_target = find_nearest_bricks(bricks, bricks[char_index-1], target_color=random.choice(color_list))
            if brick_target.label == bricks[char_index-1].label:
                res = res +"How to get brick {}?".format(brick_target.label)
            else:
                res = res +"How to get the nearest {} brick of the brick {}".format(choiced_color, bricks[char_index-1].label) + "?"
        elif num == 3:
            brick_target = bricks[char_index-1]
            #rule = 'The bricks must now be grabbed from top to bottom, and if the lower brick is to be grabbed, the upper brick must be removed first.'
            res = res + "How to get brick {}?".format(brick_target.label)
        #res = res + ". What bricks we need to remove in order?"
        dict_above = {}
        for item in bricks:
           make_dict(dict_above, item, bricks)
        label = ''
        label = remove_bricks(brick_target.label, dict_above, label)
        if label==brick_target.label:
            label = 'we dont need to remove'
        data = {"label":label, "data": res}
        data_list.append(data)
    dataset = {"testset": data_list}
    with open('shuffle__2d_fordemo.json', 'w') as outfile:
        json.dump(data_list, outfile)



