<script setup lang="ts">
import { ClientesService } from '@/domain/services/cliente.service';
import { alertError, alertSuccess } from '@/shared/utils/alerts';
import { reactive } from 'vue';
import { useRouter } from 'vue-router';

interface FormData {
    nombre: string;
    apellido: string;
    email: string;
    telefono: string;
    direccion: string;
    fecha_nacimiento: string;
}
const formData = reactive<FormData>({
    nombre: '',
    apellido: '',
    email: '',
    telefono: '',
    direccion: '',
    fecha_nacimiento: '',
});

const router = useRouter();

const submitForm = async (e: Event) => {
    e.preventDefault();
    await ClientesService.nuevoCliente(formData).then(
        (response: any) => {
            alertSuccess(response.data);
            router.push('/system/clientes');
        },
        (_: any) => {
            alertError('Error al crear cliente');
        }
    )
}

</script>
<template>

    <div class="container p-3">

        <router-link to="/system/clientes" class="btn btn-primary mb-2">
            <i class="fa fa-arrow-left"></i> Volver
        </router-link>
        <h2>Crear Cliente</h2>



        <form @submit="submitForm">
            <div class="row">
                <div class="col-md-6">
                    <div class="form-group my-2">
                        <label for="nombre">Nombre</label>
                        <input type="text" id="nombre" name="nombre" class="form-control" v-model="formData.nombre"
                            required>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="form-group my-2">
                        <label for="apellido">Apellido</label>
                        <input type="text" id="apellido" name="apellido" class="form-control"
                            v-model="formData.apellido" required>
                    </div>
                </div>
            </div>

            <div class="form-group my-2">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" class="form-control" v-model="formData.email" required>
            </div>

            <div class="row">
                <div class="col-md-6">
                    <div class="form-group my-2">
                        <label for="telefono">Teléfono</label>
                        <input type="tel" id="telefono" name="telefono" class="form-control" v-model="formData.telefono"
                            required>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="form-group my-2">
                        <label for="fecha_nacimiento">Fecha de Nacimiento</label>
                        <input type="date" id="fecha_nacimiento" name="fecha_nacimiento" class="form-control"
                            v-model="formData.fecha_nacimiento" required>
                    </div>
                </div>
            </div>

            <div class="form-group my-2">
                <label for="direccion">Dirección</label>
                <input type="text" id="direccion" name="direccion" class="form-control" v-model="formData.direccion"
                    required>
            </div>

            <div class="d-flex justify-content-center">
                <button type="submit" class="btn btn-success btn-lg">
                    <i class="fa fa-save"></i> Guardar
                </button>
            </div>

        </form>
    </div>



</template>