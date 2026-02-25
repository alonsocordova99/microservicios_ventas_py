export interface IngresoProducto {
    producto_id: number;
    nombre: string;
    codigo: string;
    stock: number;
    precio: number;
    cantidad: number;
    subtotal?: number;
}

export interface Ingreso {
    proovedor: string;
    tipo_documento: string;
    codigo_documento: string;
    fecha: string;
    notas_adicionales: string;
    subtotal: number;
    igv: number;
    total: number;
    productos?: IngresoProducto[];
}

