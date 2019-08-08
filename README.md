# valqio
Sample Server Implementation for ValQ APIs

1. Install the dependencies

`pip install -r requirements.txt`

2. Update the mongodb credentials in .env

3. Start the server

`python run.py`


# GET Collection List 
**URL**
`http://127.0.0.1:5000/scenarios?where={"author": "Dharan"}&projection={"_id": 1, "author": 1, "name": 1, "_created": 1, "_updated": 1}`

 **Response**
```
{
  "_items": [
    {
      "_id": "5d2ec90d10414b327057a34d",
      "author": "Dharan",
      "name": "Collection 1",
      "_updated": "Wed, 24 Jul 2019 06:30:18 GMT",
      "_created": "Wed, 17 Jul 2019 07:06:53 GMT"
    },
    {
      "_id": "5d2ec90d10414b327057a3er",
      "author": "Dharan",
      "name": "Collection 2",
      "_updated": "Wed, 24 Jul 2019 06:30:18 GMT",
      "_created": "Wed, 17 Jul 2019 07:06:53 GMT"
    }
  ]
}
```

# GET Collection
**URL**
`http://127.0.0.1:5000/scenarios/{id}`

 **Response**
```
{
  "_id": "5d4bc90410414b3a84ceb119",
  "document": "Document Name",
  "application": "Application Name",
  "author": "UNKNOWN",
  "name": "My Collection",
  "description": "Description",
  "scenarios": [
    {
      "name": "1",
      "title": "Scenario 1",
      "descr": "",
      "defaultDescr": "",
      "compare": true,
      "simVar": [],
      "author": "UNKNOWN",
      "simActions": {},
      "activeInitiative": "1",
      "initiatives": [
        {
          "id": 1,
          "name": "i1",
          "title": "Initiative 1",
          "descr": "",
          "defaultDescr": "Revenue: 39%",
          "compare": true,
          "simVar": [
            {
              "name": "N1",
              "value": "38.57",
              "sMeth": "P",
              "manSim": []
            }
          ],
          "simActions": {},
          "author": "UNKNOWN",
          "isInitiative": true,
          "relatedScenario": "1",
          "enabled": true,
          "comments": {
            "N1": {
              "comments": [
                {
                  "userName": "UNKNOWN",
                  "comment": "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness",
                  "time": 1565247732808,
                  "id": "comment_0_N1_i1",
                  "index": 0,
                  "relatedScenario": "i1"
                }
              ],
              "commentColor": "blue"
            }
          }
        }
      ]
    }
  ],
  "activeScenario": "i1",
  "_updated": "Thu, 08 Aug 2019 07:02:26 GMT",
  "_created": "Thu, 08 Aug 2019 07:02:26 GMT"
}
```

# POST Scenario 
**URL**
`http://127.0.0.1:5000/scenarios/{id}`

**payload**
```
{
  "document": "InitiativesBK.lumx",
  "application": "SCENARIO_API",
  "author": "UNKNOWN",
  "name": "My Collection",
  "description": "Description",
  "scenarios": [
    {
      "name": "1",
      "title": "Scenario 1",
      "descr": "",
      "defaultDescr": "",
      "compare": true,
      "simVar": [],
      "author": "UNKNOWN",
      "simActions": {},
      "activeInitiative": "1",
      "initiatives": [
        {
          "id": 1,
          "name": "i1",
          "title": "Initiative 1",
          "descr": "",
          "defaultDescr": "Revenue: (33%)",
          "compare": true,
          "simVar": [
            {
              "name": "N1",
              "value": "-32.88",
              "sMeth": "P",
              "manSim": []
            }
          ],
          "simActions": {},
          "author": "UNKNOWN",
          "isInitiative": true,
          "relatedScenario": "1",
          "enabled": true,
          "comments": {
            "N1": {
              "comments": [
                {
                  "userName": "UNKNOWN",
                  "comment": "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness",
                  "time": 1565247732808,
                  "id": "comment_0_N1_i1",
                  "index": 0,
                  "relatedScenario": "i1"
                }
              ],
              "commentColor": "blue"
            }
          }
        }
      ]
    }
  ],
  "activeScenario": "i1"
}
```



