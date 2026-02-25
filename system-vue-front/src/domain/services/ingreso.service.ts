
import type { Ingreso } from '../types/ingreso.type'
import { api } from './api'

export const IngresoService = {
    async nuevoIngreso(ingreso: Ingreso) : Promise<any>{
        const response = await api.post('ingresos', ingreso)
        return response.data
    },
    async listarIngresos(pagina: number = 1, registros_por_pagina: number = 10) {
        const response = await api.get('ingresos', {
            params: {
                pagina: pagina,
                registros_por_pagina: registros_por_pagina
            }
        })
        return response.data as Ingreso[]
    },
}
