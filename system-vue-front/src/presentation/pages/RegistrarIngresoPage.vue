<script setup lang="ts">

import { onMounted, reactive, ref } from 'vue';
import SelectProductoIngreso from '../components/SelectProductoIngreso.vue';
import { DIGIDES, type Configuracion } from '@/domain/types/empresa.types';
import { EmpresaService } from '@/domain/services/empresa.service';
import { useRouter } from 'vue-router';
import { alertError, alertSuccess } from '@/shared/utils/alerts';
import { IngresoService } from '@/domain/services/ingreso.service';
import type { Ingreso, IngresoProducto } from '@/domain/types/ingreso.type';


const productos = ref<IngresoProducto[]>([]);
const tipos_documentos = ref<Configuracion[]>([]);
const IGV = ref<Configuracion | undefined>();
const router = useRouter();

const modalProductoSelectRef = ref();
const formIngreso = reactive<Ingreso>({
    proovedor: '',
    tipo_documento: '',
    codigo_documento: '',
    fecha: '',
    notas_adicionales: '',
    subtotal: 0,
    igv: 0,
    total: 0
});

const consultarConfiguraciones = async () => {
    await EmpresaService.consultarConfiguraciones([DIGIDES.PARAMETROS_VENTAS, DIGIDES.TIPO_DOCUMENTO])
    .then((response: any) => {
        var configuraciones: Configuracion[] = response.data;
        tipos_documentos.value = configuraciones.filter(c => c.cod_prim == DIGIDES.TIPO_DOCUMENTO && c.cod_sec != null);
        IGV.value = configuraciones.find(c => c.cod_sec == 'IGV');
    });
};

const openModalAddProducts = () => {
    modalProductoSelectRef.value.openModalAddProducts();
}

const onSelectProducto = (product: IngresoProducto) => {

    productos.value.push({
        producto_id: product.producto_id,
        nombre: product.nombre,
        codigo: product.codigo,
        stock: product.stock,
        precio: 0,
        cantidad: 1,
        subtotal: 0
    });
}

const onChangeDatoItem = (product: IngresoProducto) => {
    var subtotal = 0;
    productos.value = productos.value.map(p => {
        if(p.producto_id == product.producto_id){
            p.subtotal = p.cantidad * p.precio;
        }
        subtotal += p.subtotal || 0;
        return p;
    });
    formIngreso.subtotal = subtotal;
    formIngreso.igv = subtotal * 0.16;
    formIngreso.total = subtotal + formIngreso.igv;
}

const saveIngreso = async () => {
    await IngresoService.nuevoIngreso(formIngreso).then(
        (response: any) => {
            alertSuccess(response.data);
            router.push('/system/ingresos');
        },
        (_: any) => {
            alertError('Error al crear ingreso');
        }
    )
}

onMounted(async () => {
    await consultarConfiguraciones();
});

</script>
<template>
    <div class="mb-4 border-bottom">
        <div class="mb-2">
            <router-link to="/system/ingresos" class="btn btn-sm btn-success">
                <i class="fa fa-arrow-left"></i> Volver
            </router-link>
        </div>
 
        <div>
            <h1 class="h2 font-weight-bold">Entradas al Almacén</h1>
            <p class="text-muted">Registrar nueva entrada de mercancía al inventario central</p>
        </div>
    </div>
    <div class="row">
        <div class="col-lg-8 my-2">
            <div class="card my-2">
                <div class="card-header">
                    Información del Proveedor
                </div>
                <div class="card-body">
                    <div class="form-row">
                        <div class="form-group col-12 col-lg-6">
                            <label class="small font-weight-bold">Proveedor</label>
                            <div class="input-group">
                                <div class="input-group-prepend">
                                    <span class="input-group-text">
                                        <i class="fa fa-user"></i>
                                    </span>
                                </div>
                                <input class="form-control" placeholder="" type="text"
                                    v-model="formIngreso.proovedor" />
                            </div>
                        </div>
                        <div class="form-group col-lg-2 col-sm-6">
                            <label class="small font-weight-bold">Tipo de Documento</label>
                            <select class="form-control" v-model="formIngreso.tipo_documento"

                            >
                                <option value="" selected hidden>Seleccione...</option>
                                <option v-for="tipo_documento in tipos_documentos" :key="tipo_documento.cod_sec"
                                    :value="tipo_documento.cod_sec">
                                    {{ tipo_documento.nombre }}
                                </option>
                            </select>
                        </div>
                        <div class="form-group col-lg-4 col-sm-6">
                            <label class="small font-weight-bold">Número de Factura</label>
                            <div class="input-group">
                                <div class="input-group-prepend">
                                    <span class="input-group-text">
                                        <i class="fa fa-file"></i>
                                    </span>
                                </div>
                                <input class="form-control" placeholder="FAC-0000" type="text" 
                                    v-model="formIngreso.codigo_documento" />
                            </div>
                        </div>
                        <div class="form-group col-lg-3 col-sm-6">
                            <label class="small font-weight-bold">Fecha</label>
                            <input class="form-control" type="date" 
                                v-model="formIngreso.fecha"
                            />
                        </div>
                    </div>
                </div>
            </div>
            <div class="card my-2">
                <div class="card-header d-flex justify-content-between align-items-center">
                    <span>Detalle de Productos</span>
                    <button class="btn btn-primary btn-sm" @click="openModalAddProducts">
                        <i class="fa fa-cart-plus"></i> Productos
                    </button>
                </div>
                <div class="table-responsive">
                    <table class="table table-hover mb-0" id="tablaProductos">
                        <thead>
                            <tr>
                                <th style="width: 40%">Producto / SKU</th>
                                <th style="width: 20%">Cantidad</th>
                                <th style="width: 20%">Costo Unit.</th>
                                <th style="width: 15%">Subtotal</th>
                                <th style="width: 5%"></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="producto in productos" :key="producto.producto_id">
                                <td>
                                    <input type="text" value="1" name="id" hidden />
                                    <span type="text" 
                                        class=" p-0 font-weight-bold">
                                        {{ producto.nombre }}
                                    </span>
                                    <div class="sku-text text-uppercase">
                                        SKU: {{ producto.codigo }}
                                    </div>
                                </td>
                                <td>
                                    <div class="input-group input-group-sm">
                                        <input class="form-control" type="number" value="10" 
                                            v-model="producto.cantidad"
                                            @change="onChangeDatoItem(producto)"
                                        />
                                    </div>
                                </td>
                                <td>
                                    <div class="input-group input-group-sm">
                                        <div class="input-group-prepend">
                                            <span class="input-group-text">S/.</span>
                                        </div>
                                        <input class="form-control" type="number" 
                                            v-model="producto.precio"
                                            @change="onChangeDatoItem(producto)"
                                        />
                                    </div>
                                </td>
                                <td class="align-middle font-weight-bold">
                                    $ {{ producto.subtotal }}
                                </td>
                                <td class="align-middle text-center">
                                    <button class="btn btn-link text-danger p-0">
                                        <i class="fa fa-trash"></i>
                                    </button>
                                </td>
                            </tr>
                            <tr v-if="productos.length == 0">
                                <td colspan="5" class="text-center">
                                    <i class="fa fa-info-circle text-primary"></i>
                                    No hay productos seleccionados
                                </td>
                            </tr>

                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="col-lg-4 my-2">
            <div class="card">
                <div class="card-header">
                    Resumen de Entrada
                </div>
                <div class="card-body">
                    <div class="form-group">
                        <label class="small font-weight-bold">Notas Adicionales</label>
                        <textarea class="form-control form-control-sm" placeholder="Observaciones sobre la recepción..."
                            rows="3" v-model="formIngreso.notas_adicionales"></textarea>
                    </div>
                    <hr />
                    <div class="d-flex justify-content-between mb-2">
                        <span class="text-muted">Subtotal</span>
                        <span class="font-weight-bold">
                            S/. {{ formIngreso.subtotal }}
                        </span>
                    </div>
                    <div class="d-flex justify-content-between mb-3">
                        <span class="text-muted">IGV {{ (IGV?.valor_dec||0) *100 }} % </span>
                        <span class="font-weight-bold">
                            S/. {{ formIngreso.igv }}
                        </span>
                    </div>
                    <div class="d-flex justify-content-between align-items-end border-top pt-3 mb-4">
                        <span class="small font-weight-bold text-uppercase">Total General</span>
                        <span class="total-value">
                            S/. {{ formIngreso.total }}
                        </span>
                    </div>
                    <button class="btn btn-primary btn-lg btn-block mb-2" @click="saveIngreso">
                        Confirmar Entrada
                    </button>
                    <a class="btn btn-link btn-block text-muted btn-sm" href="/pedidos">
                        Cancelar Operación
                    </a>
                </div>
            </div>
            <div class="alert alert-info border-0 shadow-sm small mt-3">
                <div class="d-flex gap-2">
                    <i class="fa fa-info-circle h1"></i>
                    <div>
                        Asegúrese de que los costos unitarios coincidan con la factura física para mantener la
                        precisión del inventario.
                    </div>
                </div>
            </div>
        </div>
    </div>


    <select-producto-ingreso 
        ref="modalProductoSelectRef"
        @selectProducto="onSelectProducto"
    ></select-producto-ingreso>

</template>