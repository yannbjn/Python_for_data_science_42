ft_list = ["Hello", "tata!"]
ft_tuple    = ("Hello", "toto!")
ft_set  = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# ft_list.remove("tata!")
# ft_list.append('World')

#easy way bcs I'm a dumbass
ft_list[1] = "World!"
ft_tuple = ("Hello", "France!")

ft_set.discard("tutu!")
ft_set.add("Paris!")

ft_set = sorted(list(ft_set)) #if i don't do this, it will print in a random order since there is no indexing in sets

ft_dict["Hello"] = "42Paris"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
