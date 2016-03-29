name = 'Zed A. Shaw'
age = 35 # not a lie
inch = 1.0 / 2.54
height = 74 # inches
weight = 180.5 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_inch = weight * inch

print "Let's talk about %s." % name
print "He's %g centmiter tall." % weight
print "He's %g inches tall." % height_inch
print "He's %g pounds heavy." % height_inch
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)





