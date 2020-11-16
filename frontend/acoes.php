<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>e-Vidence - Economia Baseada em Evidências</title>
    <link rel="stylesheet" href="css/evidence.css">
    <script src="js/evidence.js" defer></script>
</head>
<body>
    <h1>Ações</h1>
    <p> Veja as informações disponíveis sobre ações no mercado da B3.</p>

    <p>Escolha o seu perfil de usuário para saber mais:</p>
    <nav>
        <ul>
            <li><a href="investidor.html">Investidor</a></li>
            <li><a href="gestorpublico.html">Gestor público</a></li>
        </ul>
    </nav>
    <p>Escolha a ação que você deseja ver os dados:</p>
    <form action="../backend/buscaAcao.php">
        <input id = "BuscaAcao" type="search"/>

    </form>
    
    <figure>
        Gráfico do Beta de Sharpe
        (server-sent events javascript code + D3.js)
    </figure>
    <figure>
        Gráfico do Retoro Esperado por ARIMA
        (server-sent events javascript code + D3.js)
    </figure>
    
</body>
</html>
