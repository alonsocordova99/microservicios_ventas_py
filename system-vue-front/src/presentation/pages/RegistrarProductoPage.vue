<script setup lang="ts">
interface FileEntity {
    imagen: File | null;
    isHidden: boolean;
    path: string;
}

import { ProductosService } from '@/domain/services/productos.service';
import type { Categoria, Producto } from '@/domain/types/producto.types';
import { alertError, alertSuccess } from '@/shared/utils/alerts';
import { onMounted, reactive, ref } from 'vue';
import { useRouter } from 'vue-router';

const categorias = ref<Categoria[]>([]);
const productoForm = reactive<Producto>({
    nombre: '',
    codigo: '',
    descripcion: '',
    categoria_id: 0,
    costo: 0,
    precio_venta: 0,
    imagen: null
});

const router = useRouter();

const infoCategorias = async () => {
    await ProductosService.infoCategorias().then((response: any) => {
        categorias.value = response.data;
    });
};

onMounted(() => {
    infoCategorias();
});



const dataForm = reactive<FileEntity>({
    imagen: null,
    isHidden: true,
    path: ''
});
const clearImage = () => {
    dataForm.imagen = null;
    dataForm.isHidden = true;
    dataForm.path = '';
}


const onChangeImagen = (e: Event) => {
    const file = (e.target as HTMLInputElement).files?.[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            dataForm.imagen = file;
            dataForm.path = e.target?.result as string;
            // al label del input agregar el nombre tambien
            dataForm.isHidden = false;
        };
        reader.readAsDataURL(file);
    }
};

const submitForm = async (e: Event) => {
    e.preventDefault();
    productoForm.imagen = dataForm.imagen;
    await ProductosService.nuevoProducto(productoForm).then((response: any) => {
        if(response.status == 'success'){
            alertSuccess(response.data);
            // redirect to productos
            router.push('/system/productos');
        }else{
            alertError(response.data);
        }
    })
    .catch((_: any) => {
        alertError("Error al agregar producto");
    });
};

</script>
<template>
    <div class="py-3">
        <a href="/system/productos" class="btn btn-primary">
            <i class="fa fa-arrow-left"></i> Volver
        </a>
        <h1>Agregar Producto</h1>

    </div>


    <form  method="POST" @submit="submitForm">
        <div class="row">
            <div class="col-lg-8">
                <div class="card mb-4">
                    <div class="card-body p-4">
                        <div class="form-section-title">
                            <i class="fa fa-info-circle text-primary"></i>
                            Información General
                        </div>
                        <div class="form-group">
                            <label class="font-weight-600" for="nombre">Nombre del Producto <span
                                    class="text-danger">*</span></label>
                            <input class="form-control form-control-lg" id="nombre"
                                placeholder="Ej. Camiseta Algodón Premium" required type="text" 
                                v-model="productoForm.nombre"
                                />
                        </div>
                        <div class="form-group">
                            <label class="font-weight-600" for="descripcion">Descripción</label>
                            <textarea class="form-control" id="descripcion"
                                placeholder="Describe las características principales del producto..."
                                rows="4"
                                v-model="productoForm.descripcion"
                                ></textarea>
                        </div>
                        <div class="row">
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label class="font-weight-600" for="codigo">SKU / Código <span
                                            class="text-danger">*</span></label>
                                    <div class="input-group">
                                        <div class="input-group-prepend">
                                            <span class="input-group-text">
                                                <i class="fa fa-barcode"></i>
                                            </span>
                                        </div>
                                        <input class="form-control" id="codigo" 
                                            placeholder="00-000000" 
                                            required
                                            type="text" 
                                            v-model="productoForm.codigo"
                                        />
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label class="font-weight-600" for="categoria">Categoría</label>
                                    <select class="form-control" id="categoria"
                                        v-model="productoForm.categoria_id"
                                    >
                                        <option value="" hidden>Seleccionar categoría</option>
                                        <option v-for="categoria in categorias" :key="categoria.id" :value="categoria.id">
                                            {{ categoria.nombre }}
                                        </option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <hr class="my-4" />
                        <div class="form-section-title">
                            <i class="fa fa-money text-primary"></i>
                            Precios e Inventario
                        </div>
                        <div class="row">
                            <div class="col-md-4">
                                <div class="form-group">
                                    <label class="font-weight-600" for="precio">Costo</label>
                                    <div class="input-group">
                                        <div class="input-group-prepend">
                                            <span class="input-group-text">$</span>
                                        </div>
                                        <input class="form-control" id="precio" placeholder="0.00" 
                                            step="0.01"
                                            type="number" 
                                            v-model="productoForm.costo"
                                            />
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-4">
                                <div class="form-group">
                                    <label class="font-weight-600" for="precioVenta">Precio de Venta</label>
                                    <div class="input-group">
                                        <div class="input-group-prepend">
                                            <span class="input-group-text">$</span>
                                        </div>
                                        <input class="form-control" id="precioVenta" 
                                            placeholder="0.00" 
                                            step="0.01"
                                            type="number" 
                                            v-model="productoForm.precio_venta"
                                        />
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-4">
                <div class="card mb-4">
                    <div class="card-body p-4">
                        <div class="form-section-title">
                            <i class="fa fa-image text-primary"></i>
                            Multimedia
                        </div>
                        <label class="font-weight-600 mb-2">Imagen del Producto</label>
                        <div class="form-group">
                            <div class="custom-file">
                                <input class="custom-file-input" ref="imagenElement" type="file"
                                    @change="onChangeImagen">
                                <label class="custom-file-label" for="imagen">
                                    {{ dataForm.imagen?.name ? dataForm.imagen?.name : 'Elegir archivo...' }}
                                </label>
                            </div>
                            <small class="form-text text-muted mt-2">PNG, JPG hasta 10MB</small>
                        </div>
                        <div class="border rounded p-2 mt-3 d-flex align-items-center" v-if="!dataForm.isHidden">
                            <div class="bg-light mr-3">
                                <img alt="Preview" class="preview-thumbnail" :src="dataForm.path" />
                            </div>
                            <div class="flex-grow-1 overflow-hidden">
                                <div class="text-truncate font-weight-bold small">
                                    {{ dataForm.imagen?.name }}
                                </div>
                                <div class="text-muted small">
                                    {{ dataForm.imagen?.size }} KB
                                </div>
                            </div>
                            <button class="btn btn-sm text-danger" type="button" @click="clearImage">
                                <i class="fa fa-trash"></i>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="text-center">
            <button class="btn btn-primary d-inline-flex align-items-center" type="submit">
                <i class="fa fa-save mr-2"></i> Guardar Producto
            </button>
        </div>
    </form>


</template>