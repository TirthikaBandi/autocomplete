from django.shortcuts import render
from autocomplete import *

# Create your views here.
def index(request):
    return render(request, 'autocomplete/index.html')


def search(request):
    # keys to form the trie structure. 
    key = "hammer" # key for autocomplete suggestions. 
    status = ["Not found", "Found"] 

    # creating trie object 
    t = Trie() 

    f=open('scrabble.txt','r')
    keys=f.read()
    for word in keys.split():
        t.insert(word)

    t.formTrie(keys) 

    # autocompleting the given key using 
    # our trie structure. 
    comp = t.printAutoSuggestions(key) 

    if comp == -1: 
        print("No other strings found with this prefix\n") 
    elif comp == 0: 
        print("No string found with this prefix\n") 
