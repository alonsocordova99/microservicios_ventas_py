<script setup lang="ts">

import { BASE_URL } from '@/domain/services/api';
import { ProductosService } from '@/domain/services/productos.service';
import type { Producto } from '@/domain/types/producto.types';
import BaseModal from '@/shared/components/BaseModal.vue';
import Pagination from '@/shared/components/Pagination.vue';
import { ref } from 'vue';


const total_paginas = ref(1);
const pagina_actual = ref(1);
const registros_por_pagina = ref(10);
const productos = ref<Producto[]>([]);
const showModal = ref(false);
const emit = defineEmits(['selectProducto']);


const consultarProductos = async () => {
    await ProductosService.listaProductosSelect(pagina_actual.value, registros_por_pagina.value).then((response: any) => {
        productos.value = response.data;
        total_paginas.value = response.total_paginas;
        pagina_actual.value = response.pagina_actual;
    });
};



const openModalAddProducts = () => {
    consultarProductos();
    showModal.value = true;
}


const selectProducto = (producto: Producto) => {
    showModal.value = false;
    emit('selectProducto', {
        producto_id: producto.id,
        nombre: producto.nombre,
        codigo: producto.codigo,
        stock: producto.stock,
        precio: 0,
        cantidad: 0
    });
}

defineExpose({
    openModalAddProducts
})


</script>
<template>
    <BaseModal :model-value="showModal" title="Selecciona Producto" :size-modal="'xl'">
        <form>
            <div class="card lg-3">
                <div class="card-body p-2">
                    <div class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text bg-white border-right-0">
                                <i class="fa fa-search"></i>
                            </span>
                        </div>
                        <input class="form-control border-left-0"
                            placeholder="Buscar productos por nombre o SKU... (F4)" type="text" />
                    </div>
                </div>
            </div>
            <div class="mt-3">
                <div class="row">
                    <div class="col-6 col-lg-3 mb-4" v-for="producto in productos" :key="producto.id"
                        @click="selectProducto(producto)">
                        <div class="card product-card ">
                            <div class="product-img"
                                :style="'background-image: url(\'' + BASE_URL + producto.url_imagen + '\');'">
                            </div>
                            <div class="card-body p-2">
                                <h6 class="card-title mb-1 text-truncate">
                                    {{ producto?.nombre }}
                                </h6>

                                <div class="d-flex justify-content-between align-items-center">
                                    <div>
                                        <span class="small text-muted mb-2">
                                            SKU: {{ producto?.codigo }}
                                        </span>
                                    </div>

                                    <span class="small text-muted">
                                        Stock: {{ producto?.stock }}
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <pagination :total_paginas="total_paginas" :pagina_actual="pagina_actual" />
            </div>
        </form>
    </BaseModal>
</template>
