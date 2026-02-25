<?php

class PedidosController extends Controller
{

    public function __construct(){
        parent::__construct([
            'PedidoModel'
        ]);
        $this->validarSesion();
    }

    public function index()
    {
        $registros_por_pagina = 10;
        $pagina_actual = isset($_GET['pagina']) ? (int)$_GET['pagina'] : 1;
        if ($pagina_actual < 1) {
            $pagina_actual = 1;
        }
        $resultado = PedidoModel::consultarPedidos($pagina_actual, $registros_por_pagina);
        // Calcular el número total de páginas
        $total_paginas = PedidoModel::consultarTotalPaginas($registros_por_pagina);

        echo json_encode( [
            'resultado' => $resultado,
            'total_paginas' => $total_paginas,
            'pagina_actual' => $pagina_actual,
            'status' => 'success'
        ]);
    }

    public function nuevo(){
        if($_SERVER['REQUEST_METHOD'] == 'POST'){
            $input = $_POST;
            $proovedor = $input['proovedor'];
            $tipo_documento = $input['tipo_documento'];
            $codigo_documento = $input['codigo_documento'];
            $fecha = $input['fecha'];
            $notas_adicionales = $input['notas_adicionales'];
            $subtotal = $input['subtotal'];
            $igv = $input['igv'];
            $total = $input['total'];
            $productos = $input['productos'];

            $idInsert = PedidoModel::crearPedido(
                $proovedor,
                $tipo_documento,
                $codigo_documento,
                $fecha, 
                $notas_adicionales, 
                $subtotal, 
                $igv, 
                $total
            );
            if($idInsert > 0){
                foreach($productos as $producto){
                    PedidoModel::insertarDetallePedido(
                        $idInsert,
                        $producto['id'],
                        $producto['cantidad'],
                        $producto['precio'],
                        $producto['subtotal']
                    );
                }
            }else{
                echo json_encode([
                    'status' => 'error',
                    'data' => 'Error al crear el pedido'
                ]);
            }
        }
    }
}
