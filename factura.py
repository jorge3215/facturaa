import qrcode
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
class Factura:   
  def CLIENTEYEMPLEADO(self):
    self.empleado=(input("ingrese el nombre del vendedor: "))
    self.nombre=(input("nombre del cliente: "))
    self.telefono=(input("telefono del cliente: "))
    self.cedula=(input("ingrese la cedula del cliente: "))  
  
  
  def PRODUCTO(self):
    self.nombredelproducto=(input("ingrese el nombre del producto: "))
    self.cantidad=int(input("ingrese la cantidad de lo que desea comprar: "))
    self.precio=int(input("ingrese el precio del producto: "))
    self.total=(self.cantidad*self.precio)
    self.ivadelproducto=(self.total*0.19)
    self.precioconiva=(self.ivadelproducto + self.total)  
      

  
  def mostrar_pdf(self):
    w, h =letter
    c = canvas.Canvas("jorgi.pdf", pagesize=letter)
    c.setLineWidth(.2)
    c.setFont("Helvetica", 11) 
    c.rect(160, h-660,310,700)
    c.drawString(245,h-30,"   SURTIDORA DE BANANOS 2000")
    c.drawString(255,h-42,"NIT 1234568910")
    c.drawString(210,h-65," linea de atencion al cliente 3053159874")
    c.drawString(210,h-79," Ubicado en el sur de neiva al lado de oasis plaza")
    c.drawString(248,h-90,"  jorgeandrespatiber333@gmail.com")
    c.drawString(175,h-140,f"NOMBRE DEL empleado: {self.empleado}")
    c.drawString(175,h-125,"fecha 18/10/2022")
    c.drawString(175,h-155,"=======================================")
    c.drawString(175,h-178,f"NOMBRE DEL CLIENTE: {self.nombre}")
    c.drawString(175,h-193,f"TELEFONO DEL CLIENTE: {self.telefono}")
    c.drawString(175,h-208,f"NUMERO DE DOCUMENTO: {self.cedula}")
    c.drawString(175,h-224,"========================================")
    c.drawString(175,h-236,"UNIDADES   NOMBREPRODU    PRECIO    ")
    c.drawString(175,h-248,f"{self.cantidad}                   {self.nombredelproducto}                  {self.precio}")
    c.drawString(175,h-280,"========================================")
    c.drawString(175,h-296,f"                            SUBTOTAL: {self.total} ")
    c.drawString(175,h-310,"                             IVA 19%:            ")
    c.drawString(175,h-324,f"                            TOTAL: {self.precioconiva}  ")
    c.drawString(175,h-340,"========================================")
    c.drawString(175,h-364,"            METODO DE PAGO: EFECTIVO               ")
    c.drawString(175,h-376,f"            TOTAL A PAGAR: {self.precioconiva}  ")
    c.drawString(175,h-388,"========================================")
    c.drawString(175,h-408,"                GRACIAS POR SU COMPRA DE BANANOS           ")
    codigoqr=qrcode.make(f" {self.empleado}  {self.nombre}  {self.precioconiva}")
    codigoqr.save("factura.png")
    c.drawImage("factura.png", 280,h-510,width=80,height=80)
    c.drawString(175,h-525,"  https://www.instagram.com/surtidora_de_bananos2000/  ")
    c.save()
       
 


factura=Factura()
factura.CLIENTEYEMPLEADO()
factura.PRODUCTO()
factura.mostrar_pdf()