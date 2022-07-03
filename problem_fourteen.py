from collections import Counter #impport counter function used to count
sonnet1='from fairest creatures we desire in increase that thereby beauty rose might never die but as the riper should by time decease his tender heir might bear his memory but thou contracted to thine own bright eyes feed thy light flame with self-substantial fuel making a famine where abundance lies thyself thy foe to thy sweet self too cruel'

#print a dictionary by coverting to lower case to ignore cases and count the word frequency
print(dict(Counter(sonnet1.lower().split())))

