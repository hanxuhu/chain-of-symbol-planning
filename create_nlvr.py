import random
import math
import json


class Object:
    def __init__(self, color=None, shape=None, size=None):
        self.color = color
        self.shape = shape
        self.size = size
    def re_str(self):
        res = "one {} {} in {}".format(self.size, self.shape, self.color)
        return res

class Box:
    def __init__(self):
        self.objects_list = []

    def add(self, object_):
        self.objects_list.append(object_)
    def re_str(self):
        res = "there are"
        for i,item in enumerate(self.objects_list):
            if i!=(len(self.objects_list)-1):
                res +=' '+item.re_str() +','
            else:
                res += ' '+item.re_str() +'.'
            
        return res
    def re_objects(self):
        return self.objects_list

        


class Instance:
    def __init__(self, left_box, mid_box, right_box):
        self.left_box = left_box
        self.mid_box  = mid_box
        self.right_box = right_box
    
    def generate_description(self):
        #print(len(bricks))
        res = 'There are three boxes.'
        res+= ' In the left box, ' + self.left_box.re_str() 
        res+= ' In the middle box, '+ self.mid_box.re_str()
        res+= ' In the right box, '+ self.right_box.re_str() 
        return res

if __name__ == "__main__":
    color_list = ['black', 'yellow', 'blue']
    size_list = ['small', 'middle', 'large']
    shape_list = ['square','triangle', 'round']
    place_list = ['left', 'middle', 'right']
    #res_all = 
    instance_all = []
    

    for i in range(1000):
        color_set = set()
        shape_set = set()
        box_list = []
        for j in range(3):
            box = Box()
            for k in range(random.randint(2, 6)):
                n = random.randint(0, 2)
                m = random.randint(0, 2)
                l = random.randint(0, 2)
                object_ = Object(color_list[n], shape_list[m], size_list[l])
                color_set.add(color_list[n])
                #color_set.add(color_list[n])
                shape_set.add(shape_list[m])
                box.add(object_)
            box_list.append(box)
        instance = Instance(box_list[0], box_list[1], box_list[2])
        res = instance.generate_description()
        
        num = random.randint(0,1)
        direct = random.choice(place_list)
        ans = []
        if num==1:
            element = random.choice(list(color_set))
            question = 'How to move all {} objects to the {} box'.format(element, direct)
            if direct=='left':
                print(instance.left_box.re_objects())
                for item in instance.right_box.objects_list:
                    if item.color == element:
                        an = (item.color, item.shape, item.size, 'right')
                        ans.append(an)
                for item in instance.mid_box.objects_list:
                    if item.color == element:
                        an = (item.color, item.shape, item.size, 'middle')
                        ans.append(an)
            if direct=='middle':
                print(instance.left_box.re_objects())
                for item in instance.left_box.objects_list:
                    if item.color == element:
                        an = (item.color, item.shape, item.size, 'left')
                        ans.append(an)
                for item in instance.right_box.objects_list:
                    if item.color == element:
                        an = (item.color, item.shape, item.size, 'right')
                        ans.append(an)
            if direct=='right':
                print(instance.left_box.re_objects())
                for item in instance.left_box.objects_list:
                    if item.color == element:
                        an = (item.color, item.shape, item.size, 'left')
                        ans.append(an)
                for item in instance.mid_box.objects_list:
                    if item.color == element:
                        an = (item.color, item.shape, item.size, 'middle')
                        ans.append(an)
    
        else:
            element = random.choice(list(shape_set))
            question = 'How to move all {}s to the {} box'.format(element, direct)
            if direct=='left':
                #print(instance.left_box.re_objects())
                for item in instance.right_box.objects_list:
                    if item.shape == element:
                        an = (item.color, item.shape, item.size, 'right')
                        ans.append(an)
                for item in instance.mid_box.objects_list:
                    if item.shape == element:
                        an = (item.color, item.shape, item.size, 'middle')
                        ans.append(an)
            if direct=='middle':
                #print(instance.left_box.re_objects())
                for item in instance.left_box.objects_list:
                    if item.shape == element:
                        an = (item.color, item.shape, item.size, 'left')
                        ans.append(an)
                for item in instance.right_box.objects_list:
                    if item.shape == element:
                        an = (item.color, item.shape, item.size, 'right')
                        ans.append(an)
            if direct=='right':
                #print(instance.left_box.re_objects())
                for item in instance.left_box.objects_list:
                    if item.shape == element:
                        an = (item.color, item.shape, item.size, 'left')
                        ans.append(an)
                for item in instance.mid_box.objects_list:
                    if item.shape == element:
                        an = (item.color, item.shape, item.size, 'middle')
                        ans.append(an)
 
        instance = {'story': res, 'question':question, 'answer': ans}
        instance_all.append(instance)
    instance_all
    print(instance_all[:5])
    with open('../data/nlvr_data/nlvr_data.json', 'w') as outfile:
        json.dump(instance_all, outfile)
    


    
    #color_list[m]
