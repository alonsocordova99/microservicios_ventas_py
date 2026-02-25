
--------------------------------------------
-- INSERT CONFIGURACION
--------------------------------------------
insert into configuracion (cod_prim, cod_sec, nombre, descripcion, valor_int, valor_dec, valor_str, estado) 
values 
(1, null, 'MONEDAS', 'Monedas soportadas', null, null, null,1),
(1, 'PEN', 'Nuevo Sol', 'Sol (S/.)', null, 1, 'S/.',1),
(1, 'DOL', 'Dólar Estadounidense', 'Dólar Estadounidense (USD)', null, 3.5, '$/. ',1),
(1, 'EUR', 'Euro', 'Euro (EUR)', null, 4, '€ ',1),
(2, null, 'ZONA HORARIA', 'Zona horaria soportada', null, null, null,1),
(2, 'GMT-5', '(GMT-05:00) Bogota', '(GMT-05:00) Bogotá', null, null, null,1),
(2, 'GMT-6', '(GMT-06:00) Mexico City', '(GMT-06:00) Ciudad de México', null, null, null,1),
(2, 'GMT+1', '(GMT+01:00) Madrid', '(GMT+01:00) Madrid', null, null, null,1),
(3, null, 'TIPO DOCUMENTO', 'Tipo de documento soportado', null, null, null,1),
(3, 'FACTURA', 'Factura', 'Factura', null, null, null,1),
(3, 'BOLETA', 'Boleta', 'Boleta', null, null, null,1),
(3, 'N_CREDITO', 'Nota de Crédito', 'Nota de Crédito', null, null, null,1),
(3, 'N_DEBITO', 'Nota de Débito', 'Nota de Débito', null, null, null,1),
(4, null, 'TIPO MOVIMIENTO', 'Tipo de movimiento soportado', null, null, null,1),
(4, 'INGRESO', 'Ingreso', 'Ingreso', null, null, null,1),
(4, 'EGRESO', 'Egreso', 'Egreso', null, null, null,1),
(4, 'DEVOLUCION', 'Devolución', 'Devolución', null, null, null,1),
(5, null, 'Rol', 'Rol de usuario', null, null, null,1),
(5, 'CAJERO', 'Cajero', 'Cajero', null, null, null,1),
(5, 'GERENTE', 'Gerente', 'Gerente', null, null, null,1),
(5, 'ADMIN', 'Administrador', 'Administrador', null, null, null,1),
(6, null, 'ESTADO STOCK', 'Estado del stock', null, null, null,1),
(6, 'SIN_STOCK', 'Sin Stock', 'Sin Stock', 5, null, 'danger',1),
(6, 'STOCK_BAJO', 'Stock Bajo', 'Stock Bajo', 15, null, 'warning',1),
(6, 'NORMAL', 'Abierto', 'Abierto', 100000, null, 'success',1),
(7, null, 'PARAMETROS DE VENTAS', 'Parametros de ventas', null, null, null,1),
(7, 'IGV', 'Importe General de Ventas', 'Importe General de Ventas', null, 0.18, null,1)
;

insert into empresa (nombre, ident_fiscal, direccion, moneda_base, zona_horaria) 
values 
('Soluciones Tech S.A. de C.V.', 'ABC123456XYZ', 'Av. Reforma 450, Piso 12, Ciudad de México, CP 06600', 'PEN', 'GMT-5');

insert into clientes (nombre, apellido, email, telefono) 
values 
('Juan', 'Perez', 'juan.perez@gmail.com', '123456789'),
('Maria', 'Gomez', 'maria.gomez@gmail.com', '123456789'),
('Pedro', 'Lopez', 'pedro.lopez@gmail.com', '123456789');

insert into usuarios (nombre, email, rol, sucursal, password)
values 
('Juan', 'juan@email.com', 'CAJERO', 'CENTRO', '123456'),
('Maria', 'maria@email.com', 'GERENTE', 'NORTE', '123456'),
('Pedro', 'pedro@email.com', 'ADMIN', 'SUR', '123456');

insert into categorias (nombre, descripcion)
values 
('Ropa y Accesorios', 'Ropa y Accesorios'),
('Electrónica', 'Electrónica'),
('Hogar', 'Hogar'),
('Deportes', 'Deportes');
