
export interface Cliente {
    id?: number;
    nombre: string;
    apellido: string;
    email: string;
    telefono: string;
    direccion: string;
    fecha_nacimiento: string;
    fecha_visita?: string;
    usuario_id?: number;
}
