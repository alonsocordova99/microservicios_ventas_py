<?php

class AuthController extends Controller {

    public function __construct() {
        parent::__construct([
            'UsuariosModel'
        ]);
    }

    public function login() {
        if($_SERVER['REQUEST_METHOD'] == 'POST'){
            $input = $this->getDataJSON();
            $usuario = $input['username'];
            $password = $input['password'];
            
            $resultado = UsuariosModel::consultarUsuario($usuario);
            if($resultado!=null){
                if($password == $resultado['password']){
                    $_SESSION['email'] = $usuario;
                    $_SESSION['id'] = $resultado['id'];
                    $token = $this->generarToken($resultado['id']);
                    echo json_encode([
                        'status' => 'success',
                        'data' => $usuario,
                        'token' => $token
                    ]);
                    return;
                }
            }
            echo json_encode([
                    'status' => 'error',
                    'data' => 'Usuario o contraseña incorrecta'
                ]);
        }
    }

     public function register(){
        if($_SERVER['REQUEST_METHOD'] == 'POST'){
            $input = $this->getDataJSON();
            $nombre = $input['nombre'];
            $password = $input['password'];
            $email = $input['email'];
            if(UsuariosModel::crearUsuario($nombre, $password, $email)){
                echo json_encode([
                    'status' => 'success',
                    'data' => 'Usuario creado correctamente'
                ]);
            }else{
                echo json_encode([
                    'status' => 'error',
                    'data' => 'Error al crear el usuario'
                ]);
            }
        }
    }
}