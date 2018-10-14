from google.appengine.ext import ndb

class Checkout(ndb.model):
    addedDate = ndb.DateProperty(indexed=False)
    wvfcNumber = ndb.IntegerProperty()
    wvfcName = ndb.StringProperty()
    checkoutType = ndb.StringProperty()