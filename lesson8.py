books=['booka','bookb','bookc']

books.append('bookd')

books.remove('bookb')

print(books)
print(books)

print(books.count('bookd'))

print(len(books))

vitabu=['book k','book j']

books.extend(vitabu)#adding arrays together

print(books)

books.insert(0,'book z')

print(books)

person={'name':'john','age':30,'gender':'male','isactive':False}#dictionary

print(person['name'])#access via key value pairs

person['weight']=56

print(person)

for  book in books :
    print(book)

for key,value in person.items() :
    print(key,value)

scores=[{"names":"Maggie","eng":81,"math":48,"swa":51,"geo":77,"chem":51},{"names":"Chester","eng":48,"math":80,"swa":94,"geo":99,"chem":64},{"names":"Amos","eng":96,"math":69,"swa":30,"geo":21,"chem":51},{"names":"Hayes","eng":90,"math":58,"swa":56,"geo":91,"chem":53},{"names":"Hector","eng":62,"math":40,"swa":51,"geo":35,"chem":89},{"names":"Vincent","eng":85,"math":37,"swa":71,"geo":76,"chem":55},{"names":"Deacon","eng":64,"math":58,"swa":48,"geo":32,"chem":68},{"names":"Winifred","eng":84,"math":90,"swa":73,"geo":53,"chem":62},{"names":"Garrett","eng":76,"math":96,"swa":32,"geo":53,"chem":67},{"names":"Alec","eng":43,"math":64,"swa":36,"geo":34,"chem":59},{"names":"Brooke","eng":88,"math":64,"swa":52,"geo":91,"chem":57},{"names":"Ora","eng":67,"math":30,"swa":47,"geo":48,"chem":75},{"names":"Arden","eng":65,"math":100,"swa":42,"geo":87,"chem":30},{"names":"Armando","eng":64,"math":73,"swa":32,"geo":95,"chem":30},{"names":"Shana","eng":86,"math":49,"swa":83,"geo":100,"chem":47},{"names":"Regina","eng":96,"math":36,"swa":82,"geo":57,"chem":21},{"names":"Aiko","eng":95,"math":40,"swa":21,"geo":63,"chem":70},{"names":"Iliana","eng":40,"math":63,"swa":58,"geo":77,"chem":89},{"names":"Briar","eng":56,"math":38,"swa":87,"geo":88,"chem":65},{"names":"Cecilia","eng":47,"math":34,"swa":64,"geo":86,"chem":65},{"names":"Brady","eng":50,"math":54,"swa":25,"geo":62,"chem":62},{"names":"Sacha","eng":43,"math":63,"swa":82,"geo":100,"chem":82},{"names":"Sybill","eng":80,"math":39,"swa":95,"geo":67,"chem":77},{"names":"Quin","eng":41,"math":82,"swa":80,"geo":70,"chem":56},{"names":"Stephanie","eng":63,"math":46,"swa":36,"geo":55,"chem":63},{"names":"Curran","eng":71,"math":66,"swa":61,"geo":97,"chem":22},{"names":"Whitney","eng":100,"math":55,"swa":71,"geo":55,"chem":25},{"names":"Nora","eng":40,"math":77,"swa":70,"geo":67,"chem":94},{"names":"Yoshio","eng":40,"math":73,"swa":42,"geo":76,"chem":49},{"names":"Meredith","eng":96,"math":70,"swa":95,"geo":100,"chem":30},{"names":"Alyssa","eng":51,"math":49,"swa":88,"geo":78,"chem":60},{"names":"Melissa","eng":41,"math":41,"swa":44,"geo":84,"chem":36},{"names":"Henry","eng":96,"math":54,"swa":23,"geo":25,"chem":61},{"names":"Lev","eng":97,"math":39,"swa":28,"geo":100,"chem":84},{"names":"Donovan","eng":40,"math":57,"swa":77,"geo":28,"chem":38},{"names":"Amity","eng":71,"math":87,"swa":83,"geo":85,"chem":61},{"names":"Bianca","eng":58,"math":76,"swa":65,"geo":63,"chem":39},{"names":"Ferdinand","eng":71,"math":84,"swa":98,"geo":52,"chem":45},{"names":"Emerson","eng":95,"math":93,"swa":43,"geo":48,"chem":96},{"names":"Fritz","eng":66,"math":36,"swa":34,"geo":93,"chem":37},{"names":"Dante","eng":68,"math":52,"swa":63,"geo":99,"chem":45},{"names":"Amos","eng":90,"math":64,"swa":53,"geo":25,"chem":36},{"names":"Evelyn","eng":40,"math":55,"swa":50,"geo":24,"chem":79},{"names":"Karina","eng":47,"math":98,"swa":28,"geo":53,"chem":93},{"names":"Lamar","eng":80,"math":49,"swa":54,"geo":97,"chem":64},{"names":"Lilah","eng":98,"math":38,"swa":75,"geo":58,"chem":39},{"names":"Mark","eng":95,"math":83,"swa":66,"geo":37,"chem":27},{"names":"Clinton","eng":40,"math":32,"swa":47,"geo":74,"chem":46},{"names":"Shea","eng":79,"math":42,"swa":68,"geo":28,"chem":82},{"names":"Cleo","eng":46,"math":77,"swa":65,"geo":81,"chem":43},{"names":"Megan","eng":86,"math":33,"swa":35,"geo":78,"chem":91},{"names":"Sheila","eng":91,"math":61,"swa":71,"geo":53,"chem":75},{"names":"Karly","eng":90,"math":63,"swa":43,"geo":78,"chem":61},{"names":"Peter","eng":47,"math":96,"swa":91,"geo":51,"chem":75},{"names":"Laura","eng":62,"math":40,"swa":74,"geo":68,"chem":20},{"names":"Herrod","eng":98,"math":69,"swa":78,"geo":59,"chem":35},{"names":"Mechelle","eng":90,"math":77,"swa":25,"geo":87,"chem":50},{"names":"Britanni","eng":78,"math":42,"swa":95,"geo":49,"chem":84},{"names":"Melanie","eng":60,"math":63,"swa":45,"geo":55,"chem":30},{"names":"Dorothy","eng":91,"math":40,"swa":56,"geo":100,"chem":31},{"names":"Callie","eng":92,"math":67,"swa":36,"geo":92,"chem":87},{"names":"Imani","eng":73,"math":32,"swa":37,"geo":97,"chem":71},{"names":"Micah","eng":54,"math":43,"swa":30,"geo":96,"chem":53},{"names":"McKenzie","eng":72,"math":52,"swa":25,"geo":54,"chem":49},{"names":"Allistair","eng":78,"math":98,"swa":52,"geo":100,"chem":21},{"names":"Signe","eng":47,"math":79,"swa":74,"geo":40,"chem":44},{"names":"Armand","eng":45,"math":85,"swa":22,"geo":39,"chem":33},{"names":"Anika","eng":56,"math":76,"swa":81,"geo":85,"chem":70},{"names":"Angela","eng":93,"math":55,"swa":98,"geo":49,"chem":66},{"names":"Kiara","eng":96,"math":45,"swa":36,"geo":30,"chem":59},{"names":"Martina","eng":54,"math":36,"swa":57,"geo":86,"chem":20},{"names":"Garrett","eng":55,"math":53,"swa":55,"geo":79,"chem":34},{"names":"Kylan","eng":76,"math":30,"swa":84,"geo":78,"chem":91},{"names":"Rhea","eng":77,"math":78,"swa":88,"geo":80,"chem":62},{"names":"Amela","eng":94,"math":50,"swa":70,"geo":51,"chem":98},{"names":"Ruby","eng":44,"math":88,"swa":90,"geo":54,"chem":88},{"names":"Ivy","eng":80,"math":60,"swa":94,"geo":73,"chem":68},{"names":"Sylvia","eng":54,"math":99,"swa":34,"geo":78,"chem":57},{"names":"Angelica","eng":86,"math":50,"swa":41,"geo":93,"chem":88},{"names":"Nichole","eng":81,"math":41,"swa":40,"geo":58,"chem":38},{"names":"Clio","eng":80,"math":66,"swa":20,"geo":71,"chem":93},{"names":"Noah","eng":77,"math":46,"swa":92,"geo":35,"chem":74},{"names":"Anthony","eng":78,"math":44,"swa":53,"geo":28,"chem":47},{"names":"Quon","eng":83,"math":68,"swa":39,"geo":29,"chem":62},{"names":"Boris","eng":94,"math":41,"swa":45,"geo":27,"chem":22},{"names":"Orla","eng":74,"math":73,"swa":24,"geo":88,"chem":43},{"names":"Kelly","eng":52,"math":43,"swa":25,"geo":64,"chem":100},{"names":"Upton","eng":49,"math":81,"swa":70,"geo":50,"chem":27},{"names":"Melyssa","eng":40,"math":75,"swa":58,"geo":70,"chem":53},{"names":"Evan","eng":85,"math":56,"swa":26,"geo":77,"chem":75},{"names":"Malcolm","eng":82,"math":42,"swa":48,"geo":32,"chem":21},{"names":"Dylan","eng":52,"math":31,"swa":66,"geo":76,"chem":32},{"names":"Garrett","eng":64,"math":98,"swa":91,"geo":25,"chem":39},{"names":"Madeson","eng":64,"math":30,"swa":21,"geo":30,"chem":64},{"names":"Sybil","eng":42,"math":64,"swa":84,"geo":54,"chem":69},{"names":"Ginger","eng":46,"math":96,"swa":50,"geo":86,"chem":65},{"names":"Clarke","eng":89,"math":77,"swa":48,"geo":26,"chem":30},{"names":"Ferris","eng":94,"math":34,"swa":96,"geo":37,"chem":26},{"names":"Avye","eng":88,"math":84,"swa":71,"geo":65,"chem":88},{"names":"Moses","eng":81,"math":53,"swa":89,"geo":60,"chem":39}]

totals=[ ];
for score in scores:
    # print(score['eng']+score['math']+score['geo']+score['swa']+score['chem'])
    score['totals']=score['eng']+score['math']+score['geo']+score['swa']+score['chem']
    print(score)

print(scores)

new_scores=sorted(scores,key = lambda k :k ["totals"],reverse=True)

print(new_scores)

#print top ten,bottom ten,average for each student,best subject for each student(new list)
#worst subject
#area of equilateral triangle
#all odd years between 200 and 300
#all numbers between 1-100, but if you enconter a number that is divisble by 12, print your name
#prime numbers between 10 and 50


top_ten = new_scores[:10]

print(top_ten)
print(tuple)
bottom_ten = new_scores[-10:]
print(bottom_ten)

for score in new_scores:
      print(score)
     # print((score['eng']+score['math']+score['geo']+score['swa']+score['chem'])/5)
      score['average']=(score['eng']+score['math']+score['geo']+score['swa']+score['chem'])/5
     # print(average)


# sets
watu=('john','mary','mike','jane','john')

for score in new_scores:
    # print(score['names'], score['average'])
    greatest= 'eng'
    if score['math'] > score['eng']:
        greatest='math'
    if score['swa']> score[greatest]:
        greatest='swa'
    if score['geo']> score[greatest]:
        greatest='geo'
    if score['chem']> score[greatest]:
        greatest='chem'

    print(greatest, score[greatest], score['names'])


for score in new_scores:
    worst = 'geo'
    if score['chem'] < score['geo']:
        worst= 'chem'
    if score['swa'] < score[worst]:
        worst= 'swa'
    if score['eng'] < score[worst]:
        worst= 'eng'
    if score['math'] < score[worst]:
        worst= 'math'

    print(worst, score[worst], score['names'])