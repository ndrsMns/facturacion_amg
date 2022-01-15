from django.test import TestCase

from models import Empresa, Contacto


class BaseModelTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(BaseModelTestCase, cls).setUpClass()

        cls.empresa = Empresa.objects.create(
            denominacion='Empresa',
            calle='Corcubion',
            cliente=True,
            proveedor=False,
            nif='B70583539',
            rgsea='rgsea',
            codigo='LCR',
            proveedor_aprobado=False)
        cls.contacto = Contacto.objects.create(
            empresa=cls.empresa,
            nombre='Pepe',
            email='pepe@pepito.com',
            tfno='+34000000000')


class EmpresaModelTestCase(BaseModelTestCase):
    def test_empresa_created(self):
        self.assertEqual(self.empresa.denominacion, 'Empresa')
        self.assertEqual(self.empresa.calle, 'Corcubion')
        self.assertEqual(self.empresa.nif, 'B70583539')
        self.assertEqual(self.empresa.cliente, True)
        self.assertEqual(self.empresa.proveedor, False)

    def test_empresa_str(self):
        self.assertEqual(str(self.empresa), 'Empresa')


class ContactoModelTestCase(BaseModelTestCase):
    def test_contacto_created(self):
        self.assertEqual(str(self.contacto.empresa.denominacion), 'Empresa')
        self.assertEqual(self.contacto.nombre, 'Pepe')
        self.assertEqual(self.contacto.email, 'pepe@pepito.com')
        self.assertEqual(self.contacto.tfno, '+34000000000')
        self.assertEqual(self.contacto.empresa.calle, 'Corcubion')

    def test_contacto_str(self):
        self.assertEqual(str(self.contacto), str(
            self.contacto.nombre) + " " + str(self.empresa))
