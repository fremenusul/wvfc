from google.appengine.ext import ndb

class Checkout(ndb.model):
    # date added
    addedDate = ndb.DateProperty(indexed=False)
    # WVFC Member Number
    wvfcNumber = ndb.IntegerProperty()
    # WVFC Member Name
    wvfcName = ndb.StringProperty()
    # Checkout Type
    checkoutType = ndb.StringProperty()

