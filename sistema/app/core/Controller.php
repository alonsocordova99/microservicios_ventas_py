<?php
require_once __DIR__ . '/../core/Model.php';
class Controller
{
    protected $user = null;

    public function __construct($models = []) {
        
        foreach ($models as $model) {
            require_once __DIR__ . '/../models/' . $model . '.php';
        }
    }

    public function validarSesion(){
        $headers = getallheaders();
        if(isset($headers['Authorization'])){
            $tokenHeader = explode(' ', $headers['Authorization']);
            if(count($tokenHeader) == 2){
                $token = $tokenHeader[1];
                $id = self::validarToken($token);
                if($id){
                    $this->user = $id;
                    return true;
                }
            }
        }
        //http_response_code(401);
        header('Content-Type: application/json');
        echo json_encode([
            'status' => 'error',
            'data' => 'Sesión no iniciada',
            'code' => 401
        ]);
        die;
    }

    protected function view($view, $data = [])
    {
        extract($data);
        ob_start();
        require "../app/views/$view.php";
        $content = ob_get_clean();
        if (!isset($_SESSION['email'])) {
            require __DIR__ . '/../views/layouts/main.php';
        } else {
            require __DIR__ . '/../views/layouts/system_layout.php';
        }
    }

    public function getDataJSON(){
        // Leer JSON del body
        $input = json_decode(file_get_contents('php://input'), true);

        if (!$input) {
            http_response_code(400);
            echo json_encode([
                'status' => 'error',
                'data' => 'JSON inválido'
            ]);
            exit;
        }else{
            return $input;
        }
    }


    // generar token
    public static function generarToken($id){

        $payload = [
            'id' => $id,
            'exp' => time() + 3600, // 1 hora
            'rand' => bin2hex(random_bytes(16))
        ];

        $data = json_encode($payload);
        $firma = hash_hmac('sha256', $data, 'secreto');

        return base64_encode($data . '.' . $firma);
    }

    // validar token
    public static function validarToken($token){

        $decoded = base64_decode($token);

        if (!$decoded) return false;

        list($data, $firma) = explode('.', $decoded);

        $firmaValida = hash_hmac('sha256', $data, 'secreto');

        if (!hash_equals($firmaValida, $firma)) {
            return false;
        }

        $payload = json_decode($data, true);

        if ($payload['exp'] < time()) {
            return false;
        }

        return $payload['id'];
    }

}