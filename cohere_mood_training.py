import cohere
import re
co = cohere.Client('HT8OEn0M36OmOLYY76E3Y7mxxwsWTs50HJEl4rQF')

from cohere.responses.classify import Example

examples=[
    # happy
    Example("The weather was nice", "hap"),
    Example("I'm in a good mood","hap"),
    Example("Today went well","hap"),
    Example("I loved ","hap"),
    Example("I won","hap"),
    Example("I saw the most amazing thing","hap"),
    Example("I thought it was so funny","hap"),
    Example("It was a beautiful day","hap"),
    Example(":)","hap"),
    Example("I'm happy","hap"),
    Example("I feel satisfied","hap"),

    # hyped
    Example("I was surprised","hyp"),
    Example("This is exciting","hyp"),
    Example("I feel like dancing","hyp"),
    Example("I can't believe it","hyp"),
    Example("Yay","hyp"),
    Example("I'm so lucky","hyp"),
    Example("Today was the best day","hyp"),
    Example("My dreams came true","hyp"),
    Example("I can't wait","hyp"),
    Example(":D","hyp"),
    Example("I'm amazed","hyp"),

    # sad
    Example("I have a problem","sad"),
    Example("Things aren't working","sad"),
    Example("I want to cry","sad"),
    Example("I had the worst experience","sad"),
    Example("I ruined it","sad"),
    Example("I'm upset","sad"),
    Example("I miss","sad"),
    Example("This has been hard on me","sad"),
    Example("I feel dpressed","sad"),
    Example(":(","sad"),
    Example("I need space","sad"),
    Example("I need someone","sad"),
    Example("I'm anxious","sad"),
    Example("I'm hurt","sad"),

    # angry
    Example("It's so frustrating","ang"),
    Example("I want to scream","ang"),
    Example("That was so annoying","ang"),
    Example("I'm so upset","ang"),
    Example("I failed","ang"),
    Example("I hate","ang"),
    Example(">:(","ang"),
    Example("My mind isn't working","ang"),
    Example("This is disappointing","ang"),
    Example("I was embarrassed","ang"),
    Example("I give up","ang"),
    Example("It sucks","ang"),

    # tired
    Example("It's been a long day","tir"),
    Example("I don't want to do this anymore","tir"),
    Example("I want to sleep","tir"),
    Example("I can't wait to go to bed","tir"),
    Example("I'm nervous","tir"),
    Example("I need some time","tir"),
    Example("I need sleep","tir"),
    Example("There's a lot on my mind","tir"),
    Example("I'm bored","tir"),
    Example("This is overwhelming","tir"),
    Example("I was exhausted","tir"),
    Example("I'm sick","tir"),

    # neutral
    Example("Nothing much happened","neu"),
    Example("The day went okay","neu"),
    Example("I should have done something differently","neu"),
    Example("Things used to be better","neu"),
    Example("I had a weird dream","neu"),
    Example("It was fine","neu"),
    Example("Why did I","neu"),
    Example(":|","neu"),
    Example("I forgot","neu"),
    Example("It's not that important","neu"),
    Example("Things are going normally","neu")

]

inputs =[
    #user input form will go here:

    # sample inputs below
    #"I thought today was a good day",
    #"I'm so happy things are doing incredible",
    #"I'm going to cry",
    #"I need a nap",
    #"Things are alright",
    #"I thought today was a good day, and it was. I'm so happy! Things are going incredibly. However, I'm going to cry. I need a nap. But things are alright.",
    #"Today was the best day ever! I'm so surprised with how well it went. I passed my math test with flying colours and I cried of excitement.",
    "Today was a normal day, I woke up on time and ate the regular breakfast. Lunch was good and I talked with my friends. I am going to play baseball at the park."
    #"My cat is sick so I had to go to the vet today."
]

response = co.classify(
  inputs=inputs,
  examples=examples,
)
#print(response)
restr = str(response)
print(restr[29:32])
# instead, we will take out the prediction: "" part to classify the emotion
# hap = happy
# hyp = hyped
# sad = sad
# ang = angry
# tir = tired
# neu = neutral