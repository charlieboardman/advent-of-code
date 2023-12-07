import math

t_tot = 55826490
d_rec = 246144110121111
 
#Test values
#time = 71530
#rec_dist = 940200

# Algebra:
# d = t_p * (t_tot - t_p)
# d = t_p * t_tot - t_p**2

#Quadradic formula
t_p_1 = (t_tot - math.sqrt(t_tot**2 - 4*d_rec))/2
t_p_2 = (t_tot + math.sqrt(t_tot**2 - 4*d_rec))/2

#Both of these need to be rounded up since this is a discrete problem:
t_p_1 = math.ceil(t_p_1)
t_p_2 = math.ceil(t_p_2)

winning_times = t_p_2 - t_p_1

print(winning_times)