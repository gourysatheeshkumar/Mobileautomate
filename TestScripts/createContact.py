from MobileAutomation2.Utils import Contacts

obj = Contacts.Contacts()

#for i in range(3):
obj.launchContactui()
obj.clickOnContacts()
obj.clickOnPlus()
obj.clickOnFullName()
obj.nameEntryAdb()
obj.clickOnMobile()
obj.phoneNumberEntryAdb()
obj.saveContact()
obj.pressBack2()
obj.pressBack2()
obj.lockScreen()

    # #obj.pressBack()
    # obj.editContact()
    # obj.editMoreName()
    # obj.editName()
    # obj.saveContact()
    # obj.pressBack()
    # obj.selForMore()
    # obj.blockContact()
    # obj.pressBack()
    # obj.selContacttoUnblock()
    # obj.unBlockContact()
    # obj.pressBack()
    # obj.selForMore()
    # obj.deleteContact()
    # obj.pressBack()
    # obj.pressBack()