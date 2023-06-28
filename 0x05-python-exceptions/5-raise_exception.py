#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            quotient = 0
            if i < len(my_list_1) and i < len(my_list_2):
                quotient = my_list_1[i] / my_list_2[i]
            elif i >= len(my_list_1):
                raise IndexError("my_list_1 is too short")
            elif i >= len(my_list_2):
                raise IndexError("my_list_2 is too short")

        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except (TypeError, ValueError):
            print("wrong type")
            result.append(0)
        except IndexError as e:
            print(str(e))
            result.append(0)

        else:
            result.append(quotient)
        
        finally:
            pass
