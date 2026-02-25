import { api } from './api'
import type { Empresa } from '../types/empresa.types'

export const EmpresaService = {
    async infoEmpresa() : Promise<Empresa>{
        const response = await api.get('empresa/info')
        return response.data
    },

    async actualizarEmpresa(empresa: Empresa) : Promise<any>{
        const response = await api.put('empresa/update', empresa);
        return response.data
    },

    async consultarConfiguraciones(codigos: number[]) : Promise<any>{
        const response = await api.get('empresa/configuraciones?codigos='+codigos)
        return response.data
    }

}


