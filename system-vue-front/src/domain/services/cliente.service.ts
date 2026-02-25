import { api } from './api'
import type { Cliente } from '../types/cliente.types'

export const ClientesService = {
    async listarClientes(pagina: number = 1, registros_por_pagina: number = 10) {
        const response = await api.get('clientes', {
            params: {
                pagina: pagina,
                registros_por_pagina: registros_por_pagina
            }
        })
        return response.data as Cliente[]
    },
    async nuevoCliente(cliente: Cliente) : Promise<any>{
        const response = await api.post('clientes', cliente)
        return response.data
    },
}