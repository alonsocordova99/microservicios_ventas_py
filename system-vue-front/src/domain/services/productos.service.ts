
import { api } from './api'
import type { Producto, Categoria } from '../types/producto.types'
import type { Paginated } from '../types/general.types'

export const ProductosService = {
    async infoCategorias() : Promise<Categoria[]>{
        const response = await api.get('productos/categorias')
        return response.data
    },

    async productos(pagina: number = 1, registros_por_pagina: number = 10) {
        const response = await api.get('productos', {
            params: {
                pagina: pagina,
                registros_por_pagina: registros_por_pagina
            }
        })
        return response.data as Paginated<Producto>
    },
    async listaProductosSelect(pagina: number = 1, registros_por_pagina: number = 10) {
        const response = await api.get('productos/listaSelect', {
            params: {
                pagina: pagina,
                registros_por_pagina: registros_por_pagina
            }
        })
        return response.data as Paginated<Producto>
    },
    async nuevoProducto(producto: Producto) : Promise<any>{
        
        const formData = new FormData();
        formData.append('imagen', producto.imagen || '');
        formData.append('nombre', producto.nombre);
        formData.append('codigo', producto.codigo);
        formData.append('descripcion', producto.descripcion);
        formData.append('categoria_id', producto?.categoria_id+'');
        formData.append('costo', producto.costo + '');
        formData.append('precio_venta', producto.precio_venta + '');

        const response = await api.post('productos', formData)
        return response.data
    },



}