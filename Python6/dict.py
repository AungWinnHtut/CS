from icecream import ic
Item = {
    "Broiler feed" : [
        {'feed code' : "910",
         'unit' : '50kg',
         'price' : '91550',
         'feeding program' : '1-14days',
         'feed name' : 'pre starter',
         'feed type' : 'crumble'},
        {'feed code' : "911",
         'unit' : '50kg',
         'price' : '87850',
         'feeding program' : '15-24days',
         'feed name' : 'starter',
         'feed type' : 'mini pellet'},
        {'feed code' : "912",
         'unit' : '50kg',
         'price' : '85150',
         'feeding program' : '25days-market',
         'feed name' : 'grower',
         'feed type' : 'pellet'},
        {'feed code' : "912L",
         'unit' : '50kg',
         'price' : '79950',
         'feeding program' : '35days-market',
         'feed name' : 'grower',
         'feed type' : 'pellet'}
    ],
    "Swine feed" :[
        {'feed code' : "950SG",
         'unit' : '5kg',
         'price' : '12600',
         'feeding program' : '5days-20kg',
         'feed name' : 'pre starter',
         'feed type' : 'mini pellet'},
        {'feed code' : "950SG",
         'unit' : '25kg',
         'price' : '61000',
         'feeding program' : '5days-20kg',
         'feed name' : 'pre starter',
         'feed type' : 'mini pellet'},
        {'feed code' : "951SG",
         'unit' : '25kg',
         'price' : '46350',
         'feeding program' : '20kg-60kg',
         'feed name' : 'starter',
         'feed type' : 'pellet'},
        {'feed code' : "952SG",
         'unit' : '25kg',
         'price' : '42950',
         'feeding program' : '60kg up',
         'feed name' : 'grower',
         'feed type' : 'pellet'},
        {'feed code' : "751SG",
         'unit' : '5kg',
         'price' : '11840',
         'feeding program' : '12kg-market',
         'feed name' : 'starter finisher',
         'feed type' : 'mash'},
        {'feed code' : "751SG",
         'unit' : '25kg',
         'price' : '57200',
         'feeding program' : '12kg-market',
         'feed name' : 'starter finisher',
         'feed type' : 'mash'}
         
    ]
}

        
  
for bf in Item['Broiler feed']:
    if bf['feed code'] == '910':
        print(bf)