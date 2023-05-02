ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


#your code here
ft_list[1] = "World!"
print(ft_list)

ft_tuple = list(ft_tuple)
ft_tuple[1] = "Germany"
ft_tuple = tuple(ft_tuple)
print(ft_tuple)

ft_set = {"Hello", "Wolfsburg!"}
print(ft_set)

ft_dict["Hello"]  = "42 Wolfsburg"
print(ft_dict)