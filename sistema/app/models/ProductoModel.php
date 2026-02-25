<?php

class ProductoModel extends Model {

    public static function consultarProductos($pagina, $registros_por_pagina, $tipoConsulta=1){
        // tipoConsulta = 1 (lista productos) 
        //              = 2 (lista productos seleccionados)
        $offset = ($pagina - 1) * $registros_por_pagina;
        $conexion = Database::connect();
        $sql = "";
        if($tipoConsulta == 1){
            $sql = "SELECT 
                    p.id, p.nombre, p.categoria_id, p.codigo, p.costo, p.precio_venta, 
                    p.url_imagen, p.usuario_id, p.fecha_registro, u.nombre as usuario,
                    c.nombre as categoria,
                    coalesce((Select cantidad from stocks s where s.producto_id = p.id order by s.id desc limit 1), 0) as stock
                    FROM productos p
                    INNER JOIN usuarios u ON p.usuario_id = u.id
                    inner join categorias c on p.categoria_id = c.id
                    LIMIT :limit OFFSET :offset";
        }elseif ($tipoConsulta == 2) {
            $sql = "SELECT 
                p.id, p.nombre, p.codigo, p.precio_venta, 
                p.url_imagen, 
                c.nombre as categoria,
                coalesce((Select cantidad from stocks s where s.producto_id = p.id order by s.id desc limit 1), 0) as stock
                
                FROM productos p
                inner join categorias c on p.categoria_id = c.id
                LIMIT :limit OFFSET :offset";
        }
        $resultado = $conexion->prepare($sql);
        $resultado->bindValue(':limit', $registros_por_pagina, PDO::PARAM_INT);
        $resultado->bindValue(':offset', $offset, PDO::PARAM_INT);
        $resultado->execute();
        return $resultado->fetchAll(PDO::FETCH_ASSOC);
    }

    public static function consultarTotalPaginas($registros_por_pagina){
        $conexion = Database::connect();
        $sql = "SELECT COUNT(*) AS total FROM productos";
        $resultado = $conexion->query($sql);
        $total_registros = $resultado->fetch(PDO::FETCH_ASSOC)['total'];
        return ceil($total_registros / $registros_por_pagina);
    }

    public static function crearProducto($nombre, $codigo, $categoria, $costo, $precio, $url_imagen, $usuario_id, $descripcion){
        $conexion = Database::connect();
        
        $sql = "INSERT INTO productos 
        (nombre, codigo, categoria_id, costo, precio_venta, url_imagen, usuario_id, descripcion) 
        VALUES (:nombre, :codigo,:categoria, :costo,:precio, :url_imagen, :usuario_id, :descripcion)";
        
        $stmt = $conexion->prepare($sql);

        $stmt->execute([
            ':nombre' => $nombre,
            ':codigo' => $codigo,
            ':categoria' => $categoria,
            ':costo' => $costo,
            ':precio' => $precio,
            ':url_imagen' => $url_imagen,
            ':usuario_id' => $usuario_id,
            ':descripcion' => $descripcion
        ]);

        // obtener ID generado
        return $conexion->lastInsertId();

    }

    public static function consultarProducto($key, $value){
        $conexion = Database::connect();
        $sql = "SELECT 
            id, nombre, categoria_id, codigo, costo, precio_venta, url_imagen, usuario_id, fecha_registro
             FROM productos WHERE $key = :value";
        $resultado = $conexion->prepare($sql);
        $resultado->bindValue(':value', $value, PDO::PARAM_STR);
        $resultado->execute();
        return $resultado->fetch(PDO::FETCH_ASSOC);
    }

    public static function eliminarProducto($id){
        $conexion = Database::connect();
        $sql = "DELETE FROM productos WHERE id = :id";
        $resultado = $conexion->prepare($sql);
        $resultado->bindValue(':id', $id, PDO::PARAM_INT);
        return $resultado->execute();
    }


    public static function consultarCategorias(){
        $conexion = Database::connect();
        $sql = "SELECT id, nombre FROM categorias";
        $resultado = $conexion->query($sql);
        return $resultado->fetchAll(PDO::FETCH_ASSOC);
    }

    public static function actualizarStock($id, $stock, $stock_anterior){
        $conexion = Database::connect();
        $sql = "INSERT INTO stocks (producto_id, cantidad, cantidad_anterior) VALUES (:id, :stock, :stock_anterior)";
        $resultado = $conexion->prepare($sql);
        $resultado->bindValue(':id', $id, PDO::PARAM_INT);
        $resultado->bindValue(':stock', $stock, PDO::PARAM_INT);
        $resultado->bindValue(':stock_anterior', $stock_anterior, PDO::PARAM_INT);
        return $resultado->execute();
        
    }



}