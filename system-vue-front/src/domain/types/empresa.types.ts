 
export interface Empresa {
    nombre: string;
    ident_fiscal: string;
    direccion: string;
    moneda_base: string;
    zona_horaria: string;
    is_alert_inventar_bajo: boolean;
    is_modo_offline: boolean;
}

export interface Configuracion {
    cod_prim: number;
    cod_sec: string;
    nombre: string;
    descripcion: string;
    valor_int: number;
    valor_dec: number;
    valor_str: string;
    estado: boolean;
    fecha_registro: string;
}

export const DIGIDES = {
  'MONEDAS':1,
  'ZONA_HORARIA':2,
  'TIPO_DOCUMENTO':3,
  'TIPO_MOVIMIENTO':4,
  'ROL':5,
  'ESTADO_STOCK':6,
  'PARAMETROS_VENTAS':7,
}
