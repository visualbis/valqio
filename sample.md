**Global Variables**

    url = "https://valqio.herokuapp.com/"
    app = ""
    author = ""
    doc = ""

**Global Functions**    

> **initVariables()**:<br/>
Assigns default values to the global variable<br/>
***Event:*** Application - `On Startup` <br/>

    doc = APPLICATION.getDocumentInfo().name;
    var appInfo = APPLICATION.getInfo();
    app = appInfo.name;
    author = appInfo.user;
    

> **loadCollection()**<br/>
>  Load a specific scenario collection to VDT<br/>
> ***Event:***  List Box - `On Select`<br/>

    var URL = url+'scenarios/' + LISTBOX_1.getSelectedValue();
    VDT_1.loadScenarioCollection(URL);

> **saveCollection()**<br/>
>  Update all the scenarios as a collection on the server<br/>
>  ***Event:***  Button - `On Click`<br/>

    var updateURL = url+'scenarios';
    var scenarioname = INPUTFIELD_1.getValue();
    VDT_1.saveCollection(updateURL,scenarioname , "Description");
    GLOBAL_SCRIPTS_1.closePopup();

> **updataList()**<br/>
>  Fetch the scenario collections from the server<br/>
>  ***Event:***  VDT - `Save Scenario Success`, `Save Scenario Failure`<br/>

    var URL = url+'scenarios?projection={"_id": 1, "author": 1, "name": 1, "_created": 1, "_updated": 1}&where={"author": "'+ author +'", "document": "'+ doc +'", "application": "'+ app +'"}';
    VDT_1.loadScenarioCollectionList(URL);


> **updateListBox()**<br/>
>  Update the List Box after fetching the collection<br/>
>  ***Event:***  VDT - `After Scenario Collection Fetch`<br/>

    LISTBOX_1.removeAllItems();
    var scs = VDT_1.getScenarioCollectionList();
    scs.forEach(function(sc, index) {
      LISTBOX_1.addItem(sc.id, sc.name);
    });
