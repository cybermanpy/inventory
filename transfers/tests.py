from django.test import TestCase
from .models import Transfer
# from assets.models import Asset
# from descriptions.models import Description
# from brands.models import Brand
# from funders.models import Funder
from documents.models import Document
# from providers.models import Provider
# from statuses.models import Status
# from conservations.models import Conservation

# Create your tests here.

class DocumentTestCase(TestCase):
    def setUp(self):
        Document.objects.create(desdocument='Nota de remision')

    def test_document_have_document(self):
        doc = Document.objects.get(id=1)
        self.assertEqual(doc.desdocument, "Nota de remision")

# class TransferTestCase(TestCase):
#     def setUp(self):
#         Transfer.objects.create(fkasset=1, reason="Entrega Inicial", fkowner=1, fkdepartment=1, datetransfer='18/10/2016', fktypetransfer=1, last=True)

#     def test_transfer_have_last_fkasset(self):
#         trans = Transfer.objects.get(fkasset=1)
#         self.assertEqual(trans.id, 1)
