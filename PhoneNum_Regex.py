import re

phonenum_Regex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
print("right now, let check the groups")

print("right now, let check the groups with braces")
phonenum_Regex_brace = re.compile(r'(\(\d{3}\)) (\d{3})-(\d{4})')
mo = phonenum_Regex_brace.search('My number is (010) 263-5655')
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))
print(mo.group())
print("greedy or nongreedy")
greedy_Regex = re.compile(r'(Ha){3,5}')
mo1 = greedy_Regex.search('HaHaHaHaHa') 
print(mo1.group())


nongreedy_Regex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedy_Regex.search('HaHaHaHaHa') 
print(mo2.group())

vowel_Regex = re.compile(r'[aeiouAEIOE]')
print(vowel_Regex.findall('RoboCop eats baby food.BABY FOOD.'))
const_Regex = re.compile(r'[^aeiouAEIOE]')
print(const_Regex.findall('RoboCop eats baby food.BABY FOOD.'))

begin_WithHello = re.compile(r'^Hello')
print(begin_WithHello.findall('Hello world!'))
end_WithNum = re.compile(r'\d+$')
print(end_WithNum.findall('Your number is 15110260770'))
at_Regex = re.compile(r'.at')
print(at_Regex.findall('The cat in the hat sat on the flat mat.'))
newline_Regex = re.compile('.*',re.DOTALL)
print(newline_Regex.search('Serve the public trust.\nProtect the innocent.\nUnhold the law.').group())
#Ignore the CASE
robocop_regex = re.compile(r'robocop',re.I | re.DOTALL)
print(robocop_regex.findall('RoboCop is part man, part machine, all cop.\n ROBOCOP protects the innocent.\nAI,why does your programming book talk about\nrobocop so much?'))

agentName_regex = re.compile(r'Agent (\w)\w*')
print(agentName_regex.sub(r'\1***','Agent Alice told Agent Carol that Agent \nEve knew Agent Bob was a double agent.'))


