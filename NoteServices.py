from NoteDBNodel import  Notes
class Note():
    def shareOne(self):
        return False

    def createOne(self,title,owner_id,contains,edit_date):
        note = Notes(title,owner_id,contains,edit_date)
        return note.create()

    def deleteOne(self,_id):
        note = Notes("","","","")
        return note.delete(_id)

    def updateOne(self,_note):
        note=Notes("","","","")
        return note.update(_note)

    def getAll(self,owner_id):
        note=Notes("","","","")
        return  note.getAll(owner_id)