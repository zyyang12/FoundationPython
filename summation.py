#计算字典中所有值的和
class Summation():
    def __init__(self):
        self.sum = 0

    def __sum_dict(self,my_dict, type_value):
        #global sum
        if not isinstance(my_dict, dict):
            if (type_value == "num"):
                self.sum = self.sum + my_dict
            elif (type_value == "list"):
                self.sum = self.sum + len(my_dict)
            else:
                print("sum_dict函数输入字典求和类型不正确")
        else:
            for key in my_dict:
                self.__sum_dict(my_dict[key],type_value)
        return self.sum

    def sum_dict (self,my_dict, type_value):
        self.sum = 0
        return self.__sum_dict(my_dict, type_value)
summation = Summation()
