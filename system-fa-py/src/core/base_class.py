from .database import Base

#import all the models
from src.models.empresa import Empresa, Configuracion
from src.models.clientes import Clientes
from src.models.productos import Productos, Categorias, Stocks, Movimientos
from src.models.ingresos import Ingresos, Ingresos_productos
from src.models.ventas import Ventas, Ventas_productos
from src.models.usuarios import Usuarios