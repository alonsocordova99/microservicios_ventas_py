
export interface Categoria {
    id: number;
    nombre: string;
}

export interface Producto {
    id?: number;
    nombre: string;
    codigo: string;
    descripcion: string;
    categoria?: string;
    categoria_id: number;
    costo: number;
    precio_venta: number;
    url_imagen?: string;
    usuario_id?: number;
    fecha_registro?: string;
    imagen?: File | null;
    stock?: number;
}
